import os

from django.db.models import Sum

from core import helpers


def django_initialize():
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curso_python.settings")
        from django.core.wsgi import get_wsgi_application

        get_wsgi_application()

    except Exception as e:
        print(e)


class Menu:
    option = -1

    def __init__(self):
        from core import models
        self.models = models

    def add(self):
        person = self.models.Person()
        person.name = input('Name: ')
        person.gender = input('Gender: ')
        person.salary = float(input('Salary: '))
        person.date_birth = helpers.transform_date(input('Date birth (YYYY-MM-DD): '))
        person.save()

    def list(self):
        for person in self.models.Person.objects.all():
            print(
                ' Name: ', person.name, '\n',
                'Gender: ', person.gender, '\n',
                'Salary: ', person.salary, '\n',
                'Date birth: ', person.date_birth, '\n',
                'Age: ', person.age, '\n\n'
            )

    def sum_salary(self):
        result = self.models.Person.objects.values('gender').annotate(
            sum_salary=Sum('salary')
        ).values('gender', 'sum_salary')
        for r in result:
            print('Gender: ', r['gender'], ', Salary: ', r['sum_salary'])

    def show(self):
        while not self.option == 0:
            print('1 - Add employee')
            print('2 - Employee list')
            print('3 - Sum male/famale salary')
            print('4 - Add rule')
            print('5 - Rule list')
            self.option = int(input('Option: '))

            print('\n')

            if self.option == 1:
                self.add()
            elif self.option == 2:
                self.list()
            elif self.option == 3:
                self.sum_salary()
            else:
                if not self.option == 0:
                    print('Invalid option')


if __name__ == '__main__':
    django_initialize()

    menu = Menu()
    menu.show()
