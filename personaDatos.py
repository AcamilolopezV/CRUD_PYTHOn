import conexion as con

#funcion para guardar registros de personas en la DB
def save (persona):
    persona = dict(persona)
    try:
        db = con.conectar()
        cursor = db.cursor()
        columnas = tuple(persona.keys())
        valores = tuple(persona.values())
        sql = """
        INSERT INTO personas{campos} VALUES (?,?,?,?,?,?)
        """.format(campos=columnas)
        cursor.execute(sql,(valores))
        creada = cursor.rowcount > 0
        db.commit()
        if creada:
            cursor.close()
            db.close()
            return {"respuesta: ":creada,"mensaje":"Persona registrada"}
        else:
            cursor.close()
            db.close()
            return {"respuesta: ":creada,"mensaje":"No se logro registrar a la persona"} 
    except Exception as ex:
        if "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje = "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "dni" in str(ex):
            mensaje = "Ya existe una persona con ese dni"
        else:
            mensaje = str(ex)
            cursor.close()
            db.close()
        return {"respuesta: ": False,"mensaje": mensaje}

#funcion para buscar por dni uno solo
def find(dniPersona):
    db = con.conectar()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM personas WHERE dni = ?", (dniPersona,))
        res = cursor.fetchall()
        if res:
            info = res[0]
            persona = {"id":info[0],
                       "dni":info[1],
                       "edad":info[2],
                       "nombre":info[3],
                       "apellido":info[4],
                       "direccion":info[5],
                       "correo":info[6]}
            #(1, '1053807414', 26, 'Camilo', 'Lopez', 'Calle 37 # 23', 'correo@correo.com')
            cursor.close()
            db.close()
            return {"respuesta":True,"persona":persona,"mensaje":"Persona Encontrada"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":False,"mensaje":"No existe persona asociada al dni"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta":False,"mensaje":str(ex)}

#funcion para retornar todas las personas de la base de datos
def findAll():
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
        if personas:
            cursor.close()
            db.close()
            return {"respuesta":True,"personas":personas,"mensaje":"Listado OK"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":False,"personas":personas,"mensaje":"No ahi personas registradas"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta":False,"mensaje":str(ex)}
    
#funcion para buscar por dni
def findDni(dniPersona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT id, dni, edad, nombre, apellido, direccion, correo FROM personas WHERE dni = ?", (dniPersona,))
        res = cursor.fetchall()
        if res:
            info = res[0]
            #(1, '1053807414', 26, 'Camilo', 'Lopez', 'Calle 37 # 23', 'camilo@correo.com')
            persona = {"id":info[0],
                       "dni":info[1],
                       "nombre":info[2],
                       "apellido":info[3],
                       "direccion":info[4],
                       "correo":info[5]}
            cursor.close()
            db.close()
            return {"respuesta":True,"mensaje":"Persona Encontrada"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":False,"mensaje":"No existe persona asociada al dni"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta":False,"mensaje":str(ex)}

#funcion para actualizar datos de una persona
def update(persona):
    try:
        persona = dict(persona)
        dniPersona = persona.get('dni')
        persona.pop('dni') 
        valores = tuple(persona.values())
        db = con.conectar()
        cursor = db.cursor()
        sql = """
            UPDATE personas SET edad = ?, nombre = ?,apellido = ?,direccion = ?,correo = ? WHERE dni = '{dni}'
        """.format(dni=dniPersona)
        cursor.execute(sql, valores)
        modificada = cursor.rowcount > 0
        db.commit()
        cursor.close()
        db.close()
        if modificada:
            return {"respuesta":modificada,"mensaje":"Persona actualizada"}
        else:
            return {"respuesta":modificada,"mensaje":"No se logro actualizar a la persona"}
    except Exception as ex:
        if "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje = "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "dni" in str(ex):
            mensaje = "Ya existe una persona con ese dni"
        else:
            mensaje = str(ex)
            cursor.close()
            db.close()
        return {"respuesta": False,"mensaje": mensaje}
    
#funcion para eliminar registros
def delete(idPersona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        sql = """DELETE FROM personas WHERE id = '{id}'""".format(id=idPersona)
        cursor.execute(sql)
        Eliminada = cursor.rowcount > 0
        db.commit()
        cursor.close()
        db.close()
        if Eliminada:
            return {"respuesta":Eliminada,"mensaje":"Persona eliminada"}
        else:
            return {"respuesta":Eliminada,"mensaje":"No se logro eliminar a la persona con ese ID"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta": False,"mensaje": str(ex)}
    