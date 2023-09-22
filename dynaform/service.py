from typing import Any, Dict, List
from .const import *
from .models import DynaForm, DynaFormData

def get_dynaform_and_data(dynaform_name: str) -> List:
    result: Dict[str, List[Dict[str, Any]]] = {}
    dynaform_id = DynaForm.objects.get(name=dynaform_name).id
    dynaform_data = DynaFormData.objects.filter(
        dynaform_id=dynaform_id
        ).order_by("-list_order", "-id")
    result: List = []
    for record in dynaform_data:
        data = DynaFormRecordData(
            record.id, record.dynaform, record.data)
        result.append(data)
    return result


class DynaFormRecordData:
    def __init__(self, record_id: int, dynaform: DynaForm, data: Dict[str, Any]) -> None:
        data['id'] = record_id
        data['dynaform'] = dynaform
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
