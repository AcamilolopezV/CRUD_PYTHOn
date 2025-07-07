import personaDatos as per

#pandoles datos a la funcion personas para insertar registros en la DB
# persona = {
#             "dni":"10538074146996",
#             "nombre":"Camilo",
#             "apellido":"Lopez",
#             "edad":"fdfd",
#             "direccion":"Calle 37 # 23",
#             "correo":"camilo396@correo.com"
#         }

#listando todos los resgistros de la DB ejecutando funcion findAll
# res = per.findAll()
# print(res)
res = per.findAll()
print(res)
# res = per.find("1053807414")
# print(res)
# res = per.update({
#     "dni": "55555555",  # El DNI de la persona que deseas actualizar
#     "edad": 9,
#     "nombre": "Emanuel",
#     "apellido": "Peña",
#     "direccion": "Calle 100",
#     "correo": "isabela@prueba.com"
# })
# print(res)

# res = per.save({
#     "dni": "55555555",
#     "edad": 55,
#     "nombre": "Cicuenta",
#     "apellido": "Cinco",
#     "direccion": "Calle 200",
#     "correo": "Kailo@kailo.com"
# })
# print(res)
# res = per.delete(4)
# print(res)




