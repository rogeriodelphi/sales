# from config.wsgi import *
# from core.erp.models import *
#
# data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
#         'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
#         'Grasas, aceite y mantequilla']
#
# for i in data:
#     cat = Category(name=i)
#     cat.save()
#     print('Guardado registro N°{}'.format(cat.id))



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
