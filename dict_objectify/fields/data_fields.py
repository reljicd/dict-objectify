from datetime import datetime
from typing import Dict, Optional, Union

from str2bool import str2bool

from dict_objectify.fields.field_base import FieldBase
from dict_objectify.utils.logger import get_logger

LOGGER = get_logger(__name__)


class Integer(FieldBase):
    def _parse_string(self, element: str) -> int:
        return int(element)

    def _parse_integer(self, element: int) -> int:
        return element

    def _parse_float(self, element: float) -> int:
        return int(element)

    def __get__(self, instance, owner) -> Optional[int]:
        return super().__get__(instance, owner)


class Float(FieldBase):
    def _parse_string(self, element: str) -> float:
        return float(element)

    def _parse_integer(self, element: int) -> float:
        return float(element)

    def _parse_float(self, element: float) -> float:
        return element

    def __get__(self, instance, owner) -> Optional[float]:
        return super().__get__(instance, owner)


class Text(FieldBase):
    def _parse_string(self, element: str) -> str:
        return element

    def _parse_float(self, element: float) -> str:
        return str(element)

    def _parse_bytes(self, element: bytes) -> str:
        return element.decode("utf-8")

    def _parse_dict(self, element: Dict) -> str:
        text = element.get('#text')
        if text:
            return text
        else:
            return list(element.values())[0]

    def __get__(self, instance, owner) -> Optional[str]:
        return super().__get__(instance, owner)


class Bool(FieldBase):
    def _parse_string(self, element: str) -> bool:
        return str2bool(element)

    def _parse_bool(self, element: bool) -> bool:
        return element

    def __get__(self, instance, owner) -> Optional[bool]:
        return super().__get__(instance, owner)


DEFAULT_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class Datetime(FieldBase):
    def __init__(self,
                 tag: str = None,
                 *,
                 datetime_format: str = DEFAULT_FORMAT,
                 primary: bool = False,
                 nullable: bool = True) -> None:
        self.datetime_format = datetime_format
        super().__init__(tag, primary=primary, nullable=nullable)

    def __set__(self, instance, value: Union[str, datetime]):
        if hasattr(value, 'strftime'):
            value = value.strftime(self.datetime_format)

        super().__set__(instance, value)

    def _parse_datetime(self, element: datetime) -> datetime:
        return element

    def _parse_string(self, element: str) -> Optional[datetime]:
        standard_formats = [DEFAULT_FORMAT,
                            self.datetime_format,
                            '%Y-%m-%d']

        for standard_format in standard_formats:
            try:
                return datetime.strptime(element, standard_format)
            except ValueError:
                pass

        raise ValueError(
            f'The standardised Datetime field '
            f'parses only the following formats: '
            f'{standard_formats}. The value "{element}" is incompatible.')

    def __get__(self, instance, owner) -> Optional[datetime]:
        return super().__get__(instance, owner)
