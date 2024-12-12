from datetime import datetime


class TasksControl:
    tasks = []
    @staticmethod
    def add_task(obj):
        return TasksControl.tasks.append(obj)

    @staticmethod
    def print_uncompleted():
        for i in range(len(list(TasksControl.tasks))):
            if (TasksControl.tasks[i].status == "No") :
                print(f"{TasksControl.tasks[i].description}")




class Task():
    def __init__(self, description="", release_date=datetime.now().date(), status="No"):
        self.description = description
        self.release_date = release_date
        self.status = status

    def description_set(self, text):
        self.description = text

    def description_get(self):
        return self.description

    def release_date_set(self,date):
        self.release_date = date

    def release_date_get(self):
        return self.release_date

    def status_set(self, status):
        self.status = status

    def status_get(self):
        return self.status


t = Task()
#t.status_set("")
print(f"{t.release_date} {t.status}")
TasksControl.tasks= TasksControl.add_task(t)
#TasksControl.print_uncompleted()
print(TasksControl.tasks)

