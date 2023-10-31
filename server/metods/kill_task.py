import os


def kill_task(taskname):
    try:
        os.system(f"taskkill /IM {taskname} -F")
        result = f"Процесс \"{taskname}\" убит"
    except Exception as e:
        result = f"Произошла ошибка: {e}"
    return result




