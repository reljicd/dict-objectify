from typing import Any, List, Optional

from dict_objectify.constants import NONE_EQUIVALENT_VALUES
from dict_objectify.fields.field_base import FieldBase
from dict_objectify.utils.logger import get_logger

LOGGER = get_logger(__name__)


class EnumField(FieldBase):
    def __init__(self,
                 enumeration: List[Any],
                 tag: str = None,
                 *,
                 strict: bool = True,
                 primary: bool = False,
                 nullable: bool = True) -> None:
        """
        Args:
            enumeration: A list of allowed (if strict)
                or expected (if not strict) values.
            strict: If True, no other values will be allowed. If False, values
                not in enumeration will only raise a warning.
        """
        super().__init__(tag, primary=primary, nullable=nullable)

        if any([e in NONE_EQUIVALENT_VALUES for e in enumeration]):
            raise ValueError(
                f'Got a None-equivalent as an allowed enumeration value in '
                f'enum with tag [Tag: {self.tag}] '
                f'Please use the parameter `nullable` to allow this field to '
                f'be `None`. [Enumeration: {enumeration}]'
            )
        # All the element must have the same type.
        assert len({type(e) for e in enumeration}) <= 1

        self.enumeration = enumeration
        self.strict = strict

    def __get__(self, instance, owner) -> Optional[Any]:
        if instance is not None:
            element = super().__get__(instance, owner)

            if element in self.enumeration:
                return element

            if not self.strict and element not in NONE_EQUIVALENT_VALUES:
                LOGGER.warning(
                    f'Found unexpected value [Value: {element}] '
                    f'of type [Type: {type(element)}] '
                    f'in a class of type [Type: {type(instance)}] '
                    f'in enumeration with tag [Tag: {self.tag}]. '
                    f'The value has been returned.'
                )
                return element

            if self.nullable:
                if element not in NONE_EQUIVALENT_VALUES:
                    LOGGER.warning(
                        f'Found unallowed value [Value: {element}] '
                        f'of type [Type: {type(element)}] '
                        f'in a class of type [Type: {type(instance)}] '
                        f'in enumeration with tag [Tag: {self.tag}]. '
                        f'Returning None.'
                    )
                return None
        else:
            return self

        raise ValueError(
            f'Found unallowed value [Value: {element}] '
            f'of type [Type: {type(element)}] '
            f'in a class of type [Type: {type(instance)}] '
            f'in enumeration with tag [Tag: {self.tag}].'
        )

    def __set__(self, instance, value):
        if value in self.enumeration or (self.nullable and
                                         value in NONE_EQUIVALENT_VALUES):
            super().__set__(instance, value)
        elif not self.strict:
            LOGGER.warning(
                f'Attempted to set unexpected value [Value: {value}] '
                f'of type [Type: {type(value)}] '
                f'in a class of type [Type: {type(instance)}] '
                f'in enumeration with tag [Tag: {self.tag}]. '
                f'Expected values are [Enumeration: {self.enumeration}], '
                f'and the tag {"is" if self.nullable else "is not"} nullable.'
            )
            super().__set__(instance, value)
        else:
            raise ValueError(
                f'Attempted to set unallowed value [Value: {value}] '
                f'of type [Type: {type(value)}] '
                f'in a class of type [Type: {type(instance)}] '
                f'in enumeration with tag [Tag: {self.tag}]. '
                f'Allowed values are [Enumeration: {self.enumeration}], '
                f'and the tag {"is" if self.nullable else "is not"} nullable.'
            )

    def _process(self, element: Any) -> Optional[Any]:
        return element
