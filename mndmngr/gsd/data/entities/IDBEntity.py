from abc import ABC, abstractmethod
from mndmngr.gsd.data.entities.IDBEntityData import IDBEntityData


class IDBEntity(ABC):
    _path: str
    _data: IDBEntityData | None

    @abstractmethod
    def __init__(self, path: str, data: IDBEntityData | None = None):
        pass

    @staticmethod
    @abstractmethod
    def get_entity_path() -> str:
        pass

    def get_data(self) -> IDBEntityData | None:
        return self._data

    def get_path(self) -> str:
        return self._path

    def is_initialized(self) -> bool:
        return self._data is not None
