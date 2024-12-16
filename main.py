from datetime import datetime, timedelta


class TasksControl:
    tasks = []
    @staticmethod
    def add_task(task):
        return TasksControl.tasks.append(task)

    @staticmethod
    def delete_task(task):
        TasksControl.tasks.remove(task)

    @staticmethod
    def print_uncompleted():
        #for i in range(len(list(TasksControl.tasks))):
            #if (TasksControl.tasks[i].status == "No") :
                #print(f"{TasksControl.tasks[i].description}")
        for tsk in TasksControl.tasks:
            if tsk.status_get() == "No":
                print(f"{tsk.description_get()} не выполнена, срок выполнения: {tsk.release_date_get()}")
            else:
                print(f"Задача {tsk.description_get()} выполнена, удалить ее из списка?(Y|N)")
                tmp = input()
                if tmp == "Y":
                    TasksControl.delete_task(tsk)


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

    def __str__(self):
        return f'{self.description}; {self.release_date}; {self.status}'


t = Task("Problem1")
t1 = Task("Problem2","01/01/2025")
#t.status_set("")
print(f"{t.release_date_get()} {t.status_get()}")
print(TasksControl.tasks)
#tctrl = TasksControl()
#tctrl.add_task(t)
#tctrl.add_task(t1)
TasksControl.add_task(t)
TasksControl.add_task(t1)
#TasksControl.print_uncompleted()
print(TasksControl.tasks[1].status_get())
TasksControl.tasks[1].status_set("Yes")
print(TasksControl.tasks[1].status)
TasksControl.print_uncompleted()

