from common import *

def main():
    """
    Реализует бизнес-логику проекта
    :return: None
    """
    # Инициализация исходных данных для работы программы

    students = load_students(STUDENTS_DATA)
    professions = load_professions(PROFESSIONS_DATA)

    if students is None or professions is None:
        print('Ошибка инициализации данных!\nПрограмма будет завершенна')
        return None

    # Получаем номер студента
    while True:
        user_choice = input('Введите номер студента ').strip()
        if user_choice.isdigit():
            break

    # Получаем данные о студенте
    student = get_student_by_pk(students, int(user_choice))

    # Студента с таким номером нет
    if student is None:
        print("У нас нет такого студента")
        return None
    # Выод информации о студенте и его навыках
    print(f"Студент {student['full_name']}")
    print(f"Знает {', '.join(student['skills'])}")

    user_choice = ""
    while True:
        user_choice = input(f'Выберите специальность для оценки студента {student["full_name"]} ').strip().title()
        if len(user_choice) > 0:
            break

    profession = get_profession_by_title(professions, user_choice)
    if profession is None:
        print("У нас нет такой специальности")
        return None
    # Вычисляем пригодность студента к выбранной специальности
    fitness = check_fitness(student, profession)
    if fitness is None:
        print('Критическая ошибка выполнения программы!')
        return None
    # Выводим результаты оценки пригодности студента
    print(f"Пригодность {fitness['fit_percent']}%")
    if fitness['fit_percent'] > 0:
        print(f"{student['full_name']} знает {', '.join(fitness['has'])}")
    print(f"{student['full_name']} не знает {', '.join(fitness['lacks'])}")

    input("[+] Нажмите Enter для завершения работы программы ... ")


if __name__ == "__main__":
    main()
