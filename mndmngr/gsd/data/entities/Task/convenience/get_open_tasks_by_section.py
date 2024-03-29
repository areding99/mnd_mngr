from mndmngr.gsd.data.entities.Task.TaskDBEntity import TaskDBEntity
from mndmngr.gsd.data.entities.Task.TaskDBEntityDataParser import TaskDBEntityDataParser
from mndmngr.gsd.data.queries.GlobPathDBQuery import GlobPathDBQuery
from mndmngr.gsd.data.entities.Task.convenience.get_task_sections import (
    get_task_sections,
)
import mndmngr.gsd.data.EntityManager as EntityManager


def get_open_tasks_by_section() -> dict[str, list[TaskDBEntity]]:
    tasks_by_section: dict[str, list[TaskDBEntity]] = {}

    for section in get_task_sections():
        if section not in tasks_by_section:
            tasks_by_section[section] = []

        path = TaskDBEntity.get_entity_path_absolute()
        path += "/" + section + "/*.md"

        query = GlobPathDBQuery()
        query.set_query_args(path)

        tasks = EntityManager.get_many(TaskDBEntity, TaskDBEntityDataParser(), query)

        if tasks is None:
            return {}

        tasks_by_section[section] = tasks

    open_tasks_by_section: dict[str, list[TaskDBEntity]] = {}

    for section in tasks_by_section:
        for task in tasks_by_section[section]:
            if not task.is_initialized():
                raise ValueError("task is not initialized")

            data = task.get_data()
            if data is None:
                raise ValueError("data cannot be None if task is initialized")

            if section not in open_tasks_by_section:
                open_tasks_by_section[section] = []

            if data.status != "closed":
                open_tasks_by_section[section].append(task)

    return open_tasks_by_section
