from django.contrib.auth.models import User
from django.db import models

areas = (
    ('Aerodinâmica', 'Aerodinâmica'),
    ('Direção', 'Direção e Suspenção'),
    ('Eletrica', 'Elétrica'),
    ('Estrutura', 'Estrutura'),
    ('Freio e Ergonomia', 'Freio e Ergonomia'),
    ('Powewtrain', 'Powewtrain'),
    ('Comercial', 'Comercial'),
    ('Financeiro', 'Financeiro'),
    ('Gestão', 'Gestão de Pessoas'),
    ('Marketing', 'Marketing'),
    ('Qualidade', 'Qualidade'),
    ('NA', 'Nenhuma'),
)

cursos = (
    ('AD', 'Análise e Desenvolvimento de Sistemas'),
    ('AU', 'Automação Industrial'),
    ('CC', 'Ciência da Computação'),
    ('EB', 'Engenharia de Bio. e Biotec.'),
    ('EL', 'Engenharia Elétrica'),
    ('MC', 'Engenharia Mecânica'),
    ('QM', 'Engenharia Química'),
    ('EP', 'Engenharia de Produção'),
    ('FM', 'Fabricação Mecânica'),
)

situacao = (
    ('AF', 'A fazer'),
    ('FA', 'Fazendo'),
    ('FE', 'Feito'),
)

funcao_choices = (
    ('Cordenador', 'Cordenador'),
    ('Assesor', 'Assesor'),
    ('Conselheiro', 'Conselheiro'),
    ('Capitão', 'Capitão(ã)'),
    ('Vice Capitão', 'Vice Capitão(ã)'),
    ('Diretor de Projetos', 'Diretor(a) de Projetos'),
    ('Diretor Administrativo', 'Diretor(a) Administrativo'),
)


class ObjetivosArea(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200)
    area = models.CharField(max_length=50, choices=areas, default='Nenhuma')

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural = 'Objetivos'


class FluxodeCX(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = 'Fluxo de Caixa'
        verbose_name_plural = 'Fluxo de Caixa'


class Integrantes(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50, choices=funcao_choices)
    area = models.CharField(max_length=50, choices=areas)
    curso = models.CharField(max_length=100, choices=cursos)
    email = models.EmailField(blank=True, null=True)
    RG = models.IntegerField(help_text='apenas numeros', blank=True, null=True)
    CPF = models.IntegerField(help_text='apenas numeros', blank=True, null=True)
    RA = models.IntegerField(help_text='apenas numeros', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='integrantes', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    def __str__(self):
        return self.nome


class Lembrete(models.Model):
    lemb = models.CharField('lembrete', max_length=80)

    def __str__(self):
        return self.lemb


class Prazos(models.Model):
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    entrega = models.DateField()
    dias_restantes = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Prazo'
        verbose_name_plural = 'Prazos'
