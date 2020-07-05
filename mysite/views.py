from django.shortcuts import render
from django.http import HttpResponse
#from .models import Usuario
#from .models import Perfil
from django.db import connection
from collections import namedtuple
from django.template import loader

def home(request):
    result = 0
    template = loader.get_template('mysite/home.html')
    context = {'home_result_list': result,}

    return HttpResponse(template.render(context,request))

def query1(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT DISTINCT servico.nome,\
                                servico.classe\
                    FROM servico\
                INNER JOIN tutelamento ON (tutelamento.id_servico=servico.id_servico)\
                ORDER BY servico.nome asC\
                ')
        result = named_tuple_fetchall(cursor)
        print(result)
    
    template = loader.get_template('mysite/query1.html')
    context = {'query1_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query2(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT DISTINCT servico.nome, servico.classe\
                FROM servico\
                INNER JOIN pertence ON (pertence.id_servico=servico.id_servico)\
                INNER JOIN possui ON (possui.id_perfil=pertence.id_perfil)\
                INNER JOIN usuario ON (usuario.id_usuario=possui.id_usuario)\
                WHERE usuario.id_tutor is NULL\
                ORDER BY servico.nome ASC\
                ')
        result = named_tuple_fetchall(cursor)
    print(result)
    template = loader.get_template('mysite/query2.html')
    context = {'query2_result_list': result,}
    
    return HttpResponse(template.render(context, request))


def query3(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT servico.classe\
                COUNT(servico.classe)\
                    from log_timestamp\
                INNER JOIN servico ON (servico.id_servico=log_timestamp.id_servico)\
                GROUP BY servico.classe\
                ORDER BY COUNT(servico.classe) DESC\
                LIMIT 3\
                ')
        result = named_tuple_fetchall(cursor)
    print(result)
    template = loader.get_template('mysite/query3.html')
    context = {'query3_result_list': result,}
    
    return HttpResponse(template.render(context, request))

def query4(request):
    with connection.cursor() as cursor:
        cursor.execute('\
                SELECT DISTINCT tutelamento.id_tutor, tutelamento.id_tutelado FROM tutelamento;\
                SELECT pessoa.nome\
                   COUNT(DISTINCT tutelamento.id_tutor) AS "quantos tutores tem"\
                    from pessoa\
                INNER JOIN usuario ON (usuario.id_pessoa=pessoa.id_pessoa)\
                INNER JOIN tutelamento ON (tutelamento.id_tutor=usuario.id_usuario)\
                GROUP BY pessoa.nome\
                ORDER BY COUNT(DISTINCT tutelamento.id_tutor), pessoa.nome DESC\
                ')
        result = named_tuple_fetchall(cursor)
    print(result)
    template = loader.get_template('mysite/query4.html')
    context = {'query4_result_list': result,}
    
    return HttpResponse(template.render(context, request))




#metodos auxiliares
def named_tuple_fetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    result = [nt_result(*row) for row in cursor.fetchall()]

    return result
