# from config.wsgi import *
# from core.erp.models import *
# import random
#
# data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
#         'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
#         'Grasas, aceite y mantequilla']
#
# # delete from public.erp_category;
# # ALTER SEQUENCE erp_category_id_seq RESTART WITH 1;
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#            'u', 'v', 'w', 'x', 'y', 'z']
#
# for i in range(1, 6000):
#     name = ''.join(random.choices(letters, k=5))
#     while Category.objects.filter(name=name).exists():
#         name = ''.join(random.choices(letters, k=5))
#     Category(name=name).save()
#     print('Guardado registro {}'.format(i))


# from core.erp.models import Type

# Listar
# query = Type.objects.all()
# print(query)

# # Inserir
# t = Type(name='Analista de TI').save()
# # t.name = 'Purekjas'
# t.save()

# #  Editar
# t = Type.objects.get(id=1)
# t.name = 'teste'
# t.save()
# print(t.name)

# # Deletar
# try:
#     t = Type.objects.get(id=1)
#     t.delete()
# except Exception as e:
#     print(e)

# contenha 'ana'
# obj = Type.objects.filter(name__contains='ana')

# comece com p
# obj = Type.objects.filter(name__startswith='p')
# termina com
# obj = Type.objects.filter(name__endswith='i')

# que tenha exatamente
# obj = Type.objects.filter(name__exact='Presidente')

# que se encontra em
# obj = Type.objects.filter(name__in=['Presidente', 'Analista de TI'])

# contando os registros
# obj = Type.objects.filter(name__in=['Presidente', 'Analista de TI']).count()

# mostrando a query
# obj = Type.objects.filter(name__in=['Presidente', 'Analista de TI']).query

# contenha letra 'a', porém exclua o id=5
# obj = Type.objects.filter(name__contains='a').exclude(id=5)
# obj = Type.objects.filter(name__contains='a').exclude(name='Analista de TI')

# laço for filtrando nome que contenha 'a' e exclua id=4
# for i in Type.objects.filter(name__contains='a').exclude(id=4):
#     print(i.name)

# laço for filtrando nome que contenha 'a' e retorna os últimos 5
# for i in Type.objects.filter(name__contains='a')[:3]:
#     print(i.name)

# obj = Employee.objects.filter(type__id=1)

# for i in Type.objects.filter(name__contains='a')[:3]:
#     print(i.name)
