from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Min, Max


situacao = (
    ('AF', 'A fazer'),
    ('FA', 'Fazendo'),
    ('FE', 'Feito'),
)


areas = (
    ('Aerodinamica', 'Aerodinâmica'),
    ('Direcao', 'Direção e Suspenção'),
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


class Atividade_Gantt(models.Model):
    area = models.CharField(max_length=100, choices=areas)
    atividade = models.CharField(max_length=50)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    situacao = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.atividade


class Sub_Atividades(models.Model):
    atividade = models.ForeignKey(Atividade_Gantt, on_delete=models.CASCADE)
    area = models.CharField(max_length=100, blank=True)
    sub_atividade = models.CharField(max_length=300)
    situacao = models.CharField(max_length=100, choices=situacao, default=0)
    custo = models.DecimalField(max_digits=9, decimal_places=2)
    data_inicio = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return self.sub_atividade

    class Meta:
        verbose_name = 'Sub_Atividade'
        verbose_name_plural = 'Sub_Atividades'


class Gantt_Chart(models.Model):
    id_name = models.CharField(max_length=100)
    nome = models.CharField(max_length=300)
    recurso = models.CharField(max_length=300)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    percent_complete = models.IntegerField(default=0, null=True)
    dependencia = models.CharField(max_length=300)
    area = models.CharField(max_length=100, default='')
    is_atividade = models.BooleanField(default=False)
    inicio_atividade = models.DateField(null=True)


def define_area(sender, instance, **kwargs):
    """ Definir a area de cada subatividade, conforme sua respectiva atividade """
    if hasattr(instance, 'atividade'):
        instance.area = instance.atividade.area


def model_gantt_sub(sender,instance,created,**kwargs):
    """ Post Save das subatividades Gantt """
    # Calcular o inicio e fim das atividades conforme suas respectivas subatividades
    dados1 = Sub_Atividades.objects.values('atividade').annotate(data_menor=Min('data_inicio'),
                                                                 data_maior=Max('data_final'))
    for a in range(dados1.count()):
        linha = Atividade_Gantt.objects.get(pk=dados1[a]['atividade'])
        linha.data_inicio = dados1[a]['data_menor']
        linha.data_final = dados1[a]['data_maior']
        linha.save()

    if created:
        # Criar os gantt charts conforme forem criados as subatividades
        if instance.situacao == 'FE':
            Gantt_Chart.objects.get_or_create(id_name=instance.atividade, nome=instance.sub_atividade,
                                              recurso=instance.atividade, data_inicio=instance.data_inicio,
                                              data_final=instance.data_final, percent_complete=100, area=instance.area,
                                              inicio_atividade=instance.atividade.data_inicio,
                                              dependencia=instance.atividade)
        else:
            Gantt_Chart.objects.get_or_create(id_name=instance.atividade, nome=instance.sub_atividade,
                                              recurso=instance.atividade, data_inicio=instance.data_inicio,
                                              data_final=instance.data_final, percent_complete=0, area=instance.area,
                                              inicio_atividade=instance.atividade.data_inicio,
                                              dependencia=instance.atividade)

    # Atualizar os gantt charts conforme as subatividades forem atualizadas
    else:
        linha = Gantt_Chart.objects.get(nome=instance.sub_atividade)
        linha.data_inicio = instance.data_inicio
        linha.data_final = instance.data_final
        linha.inicio_atividade = instance.atividade.data_inicio
        if instance.situacao == 'FE':
            linha.percent_complete = 100
        else:
            linha.percent_complete = 0
        linha.save()

    # Em todo Save das Sub atividades calcular a situação das atividades
    x = Atividade_Gantt.objects.get(atividade=instance.atividade)
    x.situacao = int((Sub_Atividades.objects.all().filter(atividade=instance.atividade, situacao='FE').count() /
                      Sub_Atividades.objects.all().filter(atividade=instance.atividade).count()) * 100)
    x.save()


def model_gantt_ativ(sender,instance,created,**kwargs):
    # Na criação de toda atividade, criar um gantt chart
    if created:
        Gantt_Chart.objects.get_or_create(id_name=instance.atividade, nome=instance.atividade, recurso=instance.area, is_atividade=True, area=instance.area, dependencia='null')
    # Atualizar a todo save das atividades, a situacao e datas nos gantt chart
    else:
        linha = Gantt_Chart.objects.get(nome=instance.atividade)
        linha.data_inicio = instance.data_inicio
        linha.data_final = instance.data_final
        linha.percent_complete = instance.situacao
        linha.save()

    for a in Gantt_Chart.objects.all():
        if a.id_name == instance.atividade:
            a.inicio_atividade = instance.data_inicio
            a.save()


def pre_gantt_chart(sender, instance, **kwargs):
    pass


pre_save.connect(define_area, sender=Sub_Atividades)
pre_save.connect(pre_gantt_chart, sender=Gantt_Chart)
post_save.connect(model_gantt_sub, sender=Sub_Atividades)
post_save.connect(model_gantt_ativ, sender=Atividade_Gantt)
