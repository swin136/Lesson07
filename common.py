import os
import json

DATA_DIR = 'data'
STUDENTS_DATA = 'students.json'
PROFESSIONS_DATA = 'professions.json'



def load_students(filename: str):
    """
    Загружает список студентов из файла
    :return: dict
    """
    try:
        with open(os.path.join(DATA_DIR.strip(), filename.strip()), "r", encoding='utf-8') as file:
            data = json.load(file)
        return data


    except json.decoder.JSONDecodeError:
        print(f'Ошибка декодирования данных студентов из файла {filename}')
        return None

    except FileNotFoundError:
        print(f'Файл {filename} с данными студентов не найден.')
        return None
    except PermissionError:
        print(f'Ошибка доступа к файлу {filename} с данными студентов.')
        return None
    except IOError:
        print(f'Ошибка ввода-вывода при доступе к файлу {filename} с данными студентов.')
        return None


def load_professions(filename: str):
    """
    Загружает список профессий из файла
    :return: dict
    """
    try:
        with open(os.path.join(DATA_DIR.strip(), filename.strip()), "r", encoding='utf-8') as file:
            data = json.load(file)
        return data


    except json.decoder.JSONDecodeError:
        print(f'Ошибка декодирования данных профессий из файла {filename}')
        return None

    except FileNotFoundError:
        print(f'Файл {filename} с данными профессий не найден.')
        return None
    except PermissionError:
        print(f'Ошибка доступа к файлу {filename} с данными профессий .')
        return None
    except IOError:
        print(f'Ошибка ввода-вывода при доступе к файлу {filename} с данными профессий.')
        return None


def get_student_by_pk(students: dict, pk: int):
    """
    Получает словарь с данными студента по его коду
    :param students:
    :param pk:
    :return: dict (None - в случае ошибки)
    """
    try:
        for student in students:
            if student['pk'] == pk:
                return student
        return None
    except KeyError:
        print('Ошибка доступа к данным студентов!')
        return None


def get_profession_by_title(professions: list, title: str):
    """
    Получает словарь с данными профессии по её названию
    :param professions:
    :param title:
    :return: dict (None - в случае ошибки)
    """
    try:
        for profession in professions:
            if profession['title'] == title:
                return profession
        return None
    except KeyError:
        print('Ошибка доступа к данным специальностям!')
        return None


def check_fitness(student, profession: dict):
    """
    Возращает словарь с параметрами пригодности студента к данной специальности
    :param student:
    :param profession:
    :return: dict
    """
    try:
        student_skills = set(student['skills'])
        profession_skills = set(profession['skills'])

        # print(f"Данные студента {student_skills}")
        # print(f"Данные профессии {profession_skills}")

        has = student_skills.intersection(profession_skills)
        lacks = profession_skills.difference(student_skills)

        # print(f"Знает {has}")
        # print(f"Не знает {lacks}")

        fit_percent = round(len(has) / len(profession_skills) * 100)
        # print(f"Пригодность {fit_percent}%")
        return {
            'has': list(has),
            'lacks': list(lacks),
            'fit_percent': fit_percent
        }

    except KeyError:
        return None

