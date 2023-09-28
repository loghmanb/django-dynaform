# -*- coding: utf-8 -*-
##############################################################################
#
#    DjangoDynaForm,
#    Copyright (C) 2023 Loghman Barari (<https://github.com/loghmanb/django-dynaform>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from typing import Any, Dict, List, Optional, Union

from .models import DynaForm, DynaFormData


def get_dynaform_and_data(dynaform_name: str) -> Union[None, List[Dict[str, Any]]]:
    """Get DynaForm and its data."""
    try:
        result: List[Dict[str, Any]] = []
        dynaform = DynaForm.objects.get(name=dynaform_name)
        structure = dynaform.structure
        choice_fields = {}
        for field, field_stru in structure.items():
            if field_stru["type"] == "choice":
                choice_fields[field] = {x[0]: x[1] for x in field_stru["choices"]}
        dynaform_data = DynaFormData.objects.filter(dynaform_id=dynaform.id).order_by(
            "-list_order", "-id"
        )
        for record in dynaform_data:
            data = DynaFormRecordData(
                record.id,
                dynaform,
                record.data,
                choice_fields,
            )
            result.append(data)
        return result

    except DynaForm.DoesNotExist:
        return None


class ChoiceFieldValue(str):
    """Choice field value class."""

    _value: Optional[Union[str, int]] = None
    _choices: Dict = {}

    def init(self, value: Optional[Union[str, int]], choices: Dict) -> None:
        """Init class."""
        self._value = value
        self._choices = choices

    @property
    def label(self) -> str:
        """Return label of the choice option."""
        return self._choices.get(self._value)

    @property
    def value(self) -> Optional[Union[str, int]]:
        """Return value of the choice option."""
        return self._value


class DynaFormRecordData:
    """DynaForm record."""

    def __init__(
        self,
        record_id: int,
        dynaform: DynaForm,
        data: Dict[str, Any],
        choice_fields: Dict,
    ) -> None:
        data["id"] = record_id
        data["dynaform"] = dynaform
        for field, stru in choice_fields.items():
            data[field] = ChoiceFieldValue(str(data[field]))
            data[field].init(data[field], stru)
        self._data = data

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)


class DynaFormContext:
    """Lazy loading service for accessing to DynaForm data."""

    def __init__(self) -> None:
        self._data: Dict[str, List] = {}

    def __getattr__(self, name: str) -> Union[None, List[Dict[str, Any]]]:
        if name not in self._data:
            self._data[name] = get_dynaform_and_data(name)

        return self._data[name]
