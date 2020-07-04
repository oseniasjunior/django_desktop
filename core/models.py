from django.db import models
from datetime import datetime


# Criação do modelo (classe) referente ao banco de dados
class Person(models.Model):
    # campo pk da tabela de pessoa
    id = models.AutoField(
        db_column='id',  # definie o nome da coluna no banco de dados
        null=False,  # define se a coluna é ou não obrigatória no banco de dados
        primary_key=True  # define que a coluna é pk da tabela
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=100  # define o tamanho máximo da string no banco
    )
    gender = models.CharField(
        db_column='cs_gender',
        null=False,
        max_length=1
    )
    salary = models.DecimalField(
        db_column='nb_salary',
        null=False,
        max_digits=10,  # define o tamanho máximo do valor decimal incluindo o ponto
        decimal_places=2  # define que as últimas duas casas são decimais
    )
    date_birth = models.DateField(
        db_column='dt_birth',
        null=False
    )
    rule = models.ForeignKey(
        to='Rule',
        on_delete=models.DO_NOTHING,
        db_column='id_rule',
        null=True
    )

    class Meta:
        # define o nome da tabela no banco de dados
        db_table = 'person'
        # define se o django gerencia ou não a tabela
        managed = True

    @property  # decoratorator para transformar o médoto em uma propriedade
    def age(self):
        # obtem a data atual
        _now = datetime.now().date()
        # subtrai a data atual da data de aniversário
        diff = _now - self.date_birth
        # pega a diferença de dias na subtração e divide por 365 para chegar na idade da pessoa
        return int(diff.days / 365)


class Rule(models.Model):
    id = models.AutoField(
        db_column='id',  # definie o nome da coluna no banco de dados
        null=False,  # define se a coluna é ou não obrigatória no banco de dados
        primary_key=True  # define que a coluna é pk da tabela
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=50
    )
