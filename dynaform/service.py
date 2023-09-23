from typing import Any, Dict, List, Optional, Union
from .const import *
from .models import DynaForm, DynaFormData


def get_dynaform_and_data(dynaform_name: str) -> List:
    result: Dict[str, List[Dict[str, Any]]] = {}
    dynaform = DynaForm.objects.get(name=dynaform_name)
    structure = dynaform.structure
    choice_fields = {}
    for field, field_stru in structure.items():
        if field_stru["type"]=="choice":
            choice_fields[field] = { x[0]: x[1] for x in field_stru["choices"] }
    dynaform_data = DynaFormData.objects.filter(
        dynaform_id=dynaform.id
        ).order_by("-list_order", "-id")
    result: List = []
    for record in dynaform_data:
        data = DynaFormRecordData(
            record.id, 
            dynaform, 
            record.data,
            choice_fields,
            )
        result.append(data)
    return result


class ChoiceFieldValue(str):
    def init(self, value: Optional[Union[str, int]], choices: Dict) -> None:
        self._value = value
        self._choices = choices

    @property
    def label(self) -> str:
        return self._choices.get(self._value)
    
    @property
    def value(self) -> Union[str, int]:
        return self._value


class DynaFormRecordData:
    def __init__(
            self, 
            record_id: int, 
            dynaform: DynaForm, 
            data: Dict[str, Any],
            choice_fields: Dict,
            ) -> None:
        data['id'] = record_id
        data['dynaform'] = dynaform
        for field, stru in choice_fields.items():
            data[field] = ChoiceFieldValue(str(data[field]))
            data[field].init(data[field], stru)
        self._data = data

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)


class DynaFormContext:
    def __init__(self) -> None:
        self._data: Dict[str, List] = {}

    def __getattr__(self, name: str) -> Any:
        if name not in self._data:
            self._data[name] = get_dynaform_and_data(name)

        return self._data[name]
