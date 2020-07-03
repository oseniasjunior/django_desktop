import os


def django_initialize():
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curso_python.settings")
        from django.core.wsgi import get_wsgi_application

        get_wsgi_application()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    django_initialize()

    from core import models
    from datetime import date

    # person = models.Person()
    # person.name = 'Ozzy'
    # person.gender = 'M'
    # person.salary = 2000.00
    # person.date_birth = date(1987, 10, 28)
    # person.save()
    #
    # person.name = 'Ozzy Oliveira'
    # person.save()
    #
    # person2 = models.Person.objects.create(
    #     name='Gustavo',
    #     gender='M',
    #     salary=3000.00,
    #     date_birth=date(2000, 1, 1)
    # )
    #
    # data = {
    #     'name': 'Taty',
    #     'gender': 'F',
    #     'salary': 4000.00,
    #     'date_birth': date(2000, 1, 1)
    # }
    #
    # models.Person.objects.create(**data)

    person_list = models.Person.objects.all()

    print(
        person_list
    )

    person = models.Person.objects.get(id=1)
    person2 = models.Person.objects.filter(id=2).first()
    person3 = models.Person.objects.filter(name='Taty').first()

    print(person.name)
    print(person2.name)
    print(person3.name)
