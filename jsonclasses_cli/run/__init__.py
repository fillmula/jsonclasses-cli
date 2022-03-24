from os import system


def run():
    system('uvicorn app:app --reload')
