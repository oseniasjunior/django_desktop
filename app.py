import os

from django.db.models import Sum

from core import helpers


# método padrão para iniciar o django
def django_initialize():
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curso_python.settings")
        from django.core.wsgi import get_wsgi_application

        get_wsgi_application()

    except Exception as e:
        print(e)


# classe que controla o menu da aplicação
class Menu:
    # variável que vai controlar as opções que usuário vai inserir
    # essa variável será da classe, então ela precisa ser acessada com SELF
    option = -1

    def __init__(self):
        # importa o models do app core
        from core import models
        # guarda a referência do import dentro de uma variável, para que seja reutilizada dentro da classe
        # uma vez que o import foi feito de forma local dentro do método __init__
        self.models = models

    # método para adicionar uma pessoa no banco de dados
    def add_person(self):
        # instância para uma nova pessoa
        person = self.models.Person()
        # atribui o que o usuário digitou no nome da pessoa
        person.name = input('Name: ')
        # atribui o que o usuário digitou no sexo da pessoa
        person.gender = input('Gender: ')
        # atribui o que o usuário digitou no salário da pessoa e faz a conversão da string para float
        person.salary = float(input('Salary: '))
        # atribui o que o usuário digitou na data de nascimento da pessoa e faz a conversão de string para data
        person.date_birth = helpers.transform_date(input('Date birth (YYYY-MM-DD): '))

        print('Agora você precisa informar o cargo. Veja abaixo na listagem qual o cargo desejado.')
        self.list_rule()
        rule_code = int(input('Digite o código do cargo: '))
        person.rule = self.obtains_rule(rule_code)
        # salva o objeto no banco de dados
        person.save()

    def obtains_rule(self, rule_code):
        try:
            return self.models.Rule.objects.get(pk=rule_code)
        except self.models.Rule.DoesNotExist:
            print('Código do cargo inválido')

    def list_person(self):
        # lista todos as pessoas (select * from person) usando o mecanismo do django
        # realiza um foreach nos itens que retornaram do banco de dados
        for person in self.models.Person.objects.all():
            # imprime a pessoa corrente
            print(
                ' Id: ', person.id,
                ', Name: ', person.name,
                ', Gender: ', person.gender,
                ', Salary: ', person.salary,
                ', Date birth: ', person.date_birth,
                ', Age: ', person.age,
                ', Rule: ', person.rule.name if person.rule is not None else '-', '\n'
            )

    def add_rule(self):
        rule = self.models.Rule()
        rule.name = input('Name: ')
        rule.save()

    def list_rule(self):
        for rule in self.models.Rule.objects.all():
            print(
                ' Id: ', rule.id,
                ', Name: ', rule.name
            )

    def sum_salary(self):
        # consulta para totalizar os salários por sexo
        # select cs_gender, sum(nb_salary) as sum_salary from person group by cs_gender;
        result = self.models.Person.objects.values('gender').annotate(
            sum_salary=Sum('salary')
        ).values('gender', 'sum_salary')
        for r in result:
            # imprime o resultado da consulta
            print('Gender: ', r['gender'], ', Salary: ', r['sum_salary'])

    def show(self):
        # exibição do menu com suas respectivas opções
        while not self.option == 0:
            print('1 - Add employee')
            print('2 - Employee list')
            print('3 - Sum male/famale salary')
            print('4 - Add rule')
            print('5 - Rule list')
            self.option = int(input('Option: '))

            print('\n')

            if self.option == 1:
                self.add_person()
            elif self.option == 2:
                self.list_person()
            elif self.option == 3:
                self.sum_salary()
            elif self.option == 4:
                self.add_rule()
            elif self.option == 5:
                self.list_rule()
            else:
                if not self.option == 0:
                    print('Invalid option')


if __name__ == '__main__':
    # método principal da aplicação
    django_initialize()

    menu = Menu()
    menu.show()
