#para manipular la base de datos usamos una libreria llamada sqlalchemy
#Debemos de instalar la lbreria sqlchemy en el entorno virtual que estamos creado
#Typing paquete de python para usar los tipar el codigo
from sqlalchemy import create_engine, text
from typing import List, Dict, Any


def consultar() -> List[Dict[str, Any]]:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()

    consulta = text("SELECT * FROM administradores")
    result = connectio.execute(consulta)

    listaC = []
    for i in result:
        listaC.append({
            "id_administrador": i[0],
            "nombre_admi": i[1],
            "contraseña_admi": i[2],
            "numero_telefonico_admi": i[3]
        })

    return listaC


# print(consultar())


def crear(nombre_admi: str, contraseña_admi: str, numero_telefonico_admi: int) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_insert = text(f"INSERT INTO administradores (`nombre_admi`, `contraseña_admi`, `numero_telefonico_admi`) VALUES ('{nombre_admi}', '{contraseña_admi}', '{numero_telefonico_admi}')")
    connectio.execute(sql_insert)


#crear(nombre_admi="serrato", contraseña_admi="123df", numero_telefonico_admi=2123)


def actualizar(id_administrador: int, nombre_admi: str) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_actualizar = text(f"UPDATE administradores SET nombre_admi='{nombre_admi}' WHERE id_administrador= '{id_administrador}'")
    connectio.execute(sql_actualizar)


#actualizar(id_administrador=5, nombre_admi="serrato sanchez")
#print(consultar())

def eliminar(id_administrador: int) -> None:
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", echo=True)
    connectio = engine.connect()
    sql_eliminar = text(f"DELETE FROM administradores WHERE id_administrador='{id_administrador}'")
    connectio.execute(sql_eliminar)


#eliminar(id_administrador=6)

#Usamos un menu de opcines para provar las funciones creadas y mayor usablidad

a = 0
while a != 5:
    print("""
    Menu
    ingrese una de las opciones del CRUD
    1: Consultar
    2: Crear Administrador
    3: Actualizar
    4: Eliminar
    5: Salir
""")
    entrada = int(input("Opcion: "))
    a = entrada

    if entrada == 1:
        print(consultar())
    elif entrada == 2:
        nombre_admi=input("Ingre el nombre del administrador: ")
        contraseña_admi=input("Ingrese la contraseña: ")
        numero_telefonico_admi = int(input("ingrese el telefono: "))
        crear(nombre_admi, contraseña_admi, numero_telefonico_admi)
        print("Administrador creado")
    elif entrada == 3:
        id_administrador = int(input("Ingrese en id del administrador al que desea actualizarle el nombre: "))
        nombre_admi=input("Ingrese el nombre del administrador")
        actualizar(id_administrador, nombre_admi)
        print(consultar())
    elif entrada == 4:
        id_administrador=int(input("Ingrese el id del administrador que desea eliminar: "))
        eliminar(id_administrador)
        print("Administrador eliminado")
    else:
        print("""
        
        ¡GRACIAS!
        
        """)




