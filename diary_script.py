import random
from datacenter.models import Schoolkid, Mark, Subject, Chastisement, Commendation, Lesson

commendation_examples = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!', 'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!', 'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def get_student_if_exists(student_name: str) -> Schoolkid:
    try:
        student = Schoolkid.objects.get(full_name__contains=student_name)
        return student
    except Schoolkid.DoesNotExist:
        return 'Ученика с таким именем не существует.'
    except Schoolkid.MultipleObjectsReturned:
        return 'Найдено несколько учеников с таким именем!'


def fix_marks(student_name: str) -> int:
    student = get_student_if_exists(student_name)
    bad_marks = Mark.objects.filter(schoolkid=student, points__in=[1, 2, 3])
    if not bad_marks:
        print('Нет плохих оценок!')
        return
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    print('Плохие оценки удалены!')


def remove_chastisements(student_name: str) -> int:
    student = get_student_if_exists(student_name)
    chastisements = Chastisement.objects.filter(schoolkid=student)
    if not chastisements:
        print('Замечаний нет!')
        return
    chastisements.delete()
    print('Все замечания удалены!')


def create_commendation(student_name: str, subject: str) -> Commendation:
    student = get_student_if_exists(student_name)
    try:
        lessons = Lesson.objects.filter(
            subject__title__contains=subject,
            year_of_study=student.year_of_study,
            group_letter=student.group_letter
        ).order_by('?')
        lesson = lessons.first()
        commendation = Commendation.objects.create(
            text=random.choice(commendation_examples),
            created=lesson.date,
            teacher=lesson.teacher,
            subject=lesson.subject,
            schoolkid=student
        )
        print(f'Благодарность по предмету {subject} от учителя- {lesson.teacher} c текстом "{commendation.text}" создана.')
    except Subject.DoesNotExist:
        return f'Предмет {subject} не найден в {student.year_of_study}{student.group_letter}классe.'
    except Lesson.DoesNotExist:
        return f'Урок не найден'
