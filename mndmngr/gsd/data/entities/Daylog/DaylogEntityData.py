from mndmngr.gsd.data.entities.IDBEntityData import IDBEntityData
from mndmngr.gsd.data.entities.Task.TaskDBEntity import TaskDBEntity


class DaylogEntityData(IDBEntityData):
    def __init__(
        self,
        title: str,
        path: str,
        created: str,
        id: str,
        tasks: dict[str, list[tuple[TaskDBEntity, bool]]],
        todos: list[tuple[str, bool]],
        notes: str,
        today_summary: str,
        yesterday_summary: str,
        raw: list[str],
    ) -> None:
        self.title = title
        self.path = path
        self.created = created
        self.id = id
        self.tasks = tasks
        self.todos = todos
        self.notes = notes
        self.today_summary = today_summary
        self.yesterday_summary = yesterday_summary
        self.raw = raw
