# Tasks
from project.tasks import add


def run_async_task():
    result = add.delay(4,4)
    print(result.get())
    result.forget()


if __name__ == '__main__':
    
    run_async_task()
    