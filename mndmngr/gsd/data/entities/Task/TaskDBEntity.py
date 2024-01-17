import os, sys, dotenv

if __name__ == "__main__":
    dotenv.load_dotenv()
    sys.path.append(os.environ["PROJECT_ROOT"])

from mndmngr.gsd.data.entities.IDBEntity import IDBEntity
from mndmngr.gsd.data.entities.Task.TaskEntityData import TaskEntityData


class TaskDBEntity(IDBEntity[TaskEntityData]):
    def __init__(self, path: str, data: TaskEntityData | None = None):
        if (data is not None) and (not isinstance(data, TaskEntityData)):
            raise TypeError("data must be of type TaskEntityData")

        self._rel_path = path
        self._data = data

    @staticmethod
    def get_entity_path_rel() -> str:
        return os.environ["TASKS_REL_PATH"]

    @staticmethod
    def get_entity_path_absolute() -> str:
        return os.environ["TASKS_PATH"]
