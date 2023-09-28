from Empleado import Empleado
from Cliente import Cliente
from Rutina import Rutina
from Puesto import Puesto
from TurnoLaboral import TurnoLaboral
from Dia import Dia

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#CREO LOS PUESTOS DE TRABAJO QUE SON CONSTANTES
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
coordinadorDeClases = Puesto (1, "coordinador de clases")
coordinadorDeMusculacion = Puesto (2, "Coordinador de musculación")
profesorDeMusculacion = Puesto (3, "Profesor de Musculación")
profesorDeAerobica = Puesto (4, "Profesor de Aerobica")
profesorDeCrossFit = Puesto (5, "Profesor de CrossFit")
profesorDeYoga = Puesto (6, "Profesor de Yoga")
profesorDeFuncional = Puesto (7, "Profesor de Funcional")
profesorDeStretching = Puesto (8, "Profesor de Stretching")
profesorDeSpinning = Puesto (9, "Profesor de Spinning")
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#CREO LOS TURNOS DE TRABAJO QUE SON CONSTANTES
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
turnoMañana1 = TurnoLaboral (1, "Turno Mañana 1", 7,15)
turnoTarde = TurnoLaboral (2, "Turno Tarde", 10, 18)
turnoNoche = TurnoLaboral (3, "Turno Noche", 15, 23)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#CREO LOS DIAS QUE SON CONSTANTES
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
lunes = Dia (1, "Lunes")
martes = Dia (2, "Martes")
miercoles = Dia (3, "Miércoles")
jueves = Dia (4, "Jueves")
viernes = Dia (5, "Viernes")
sabado = Dia (6, "Sabado")
domingo = Dia (7, "Domingo")
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





yo = Empleado (1,"adri","latorre", "Adrian", "Campos", 24821072, "17/08/75", "H", "Varela 1460", "adri@gmail.com", 1135794494,1,1,1)




#////////////////////////////////////////
#LOGIN
#///////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#CREO EL MENÚ PRINCIPAL 
bucle =0
opcion =0
print ("Hola ", yo.VerNombre(), ", bienvenido al menú principal.")
while bucle !=1:
  try:
    opcion = int(input("Ingrese una opción: \n 1- Menú coordinadores\n 2- Menú profesores\n 3- Menú clientes\n 4- Salir\n"))  
    
  except ValueError:
    print("Se ingresó mal la opción.  Vuelva a intenrar.")
  if opcion == 1:
    #////////////////////////////////////////////////////////////
    #Traigo los datos del login  
    yo = Empleado (1,"adri","latorre", "Adrian", "Campos", 24821072, "17/08/75", "H", "Varela 1460", "adri@gmail.com", 1135794494,1,1,1)
    #///////////////////////////////////////////////////////////
    if yo.TraerRol() == 1:
        if yo.TraerIdPuesto()==1:
            yo.MenuCoordinadorClases()
        elif yo.TraerIdPuesto()==2:
            yo.MenuCoordinadorMusculacion()
        elif yo.TraerIdPuesto()>2:
            print ("Usted no tiene permiso para ingresar a esta opción del menú.\nIngrese la opción correcta para continuar.")
    else:
        print ("Usted no tiene permiso para ingresar a esta opción del menú.\nIngrese la opción correcta para continuar. ")
       
    
  elif opcion == 2:
    #////////////////////////////////////////////////////////////
    #Traigo los datos del login    
    yo = Empleado (1,"adri","latorre", "Adrian", "Campos", 24821072, "17/08/75", "H", "Varela 1460", "adri@gmail.com", 1135794494,1,3,1)
    #///////////////////////////////////////////////////////////
    if yo.TraerRol() == 1:
        if yo.TraerIdPuesto()==3:
            yo.MenuProfeMusculacion()
        elif yo.TraerIdPuesto()>3 and yo.TraerIdPuesto()<=9:
            yo.MenuProfeClases()
        elif yo.TraerIdPuesto()<3 or yo.TraerIdPuesto()>9:
            print ("Usted no tiene permiso para ingresar a esta opción del menú.\nIngrese la opción correcta para continuar.")         
    else:
        print ("Usted no tiene permiso para ingresar a esta opción del menú.\nIngrese la opción correcta para continuar. ")
    
  elif opcion == 3:
    #////////////////////////////////////////////////////////////
    #Traigo los datos del login        
    yo = Cliente (1, "Luquis", "1234", "Lucas", "Blanco", 33120210, "01/03/2002", "H", "J. B. Alberdi 1008", "LuW@hotmail.com", 1155889632, 63, 1,70, 21, "null", "null", "null",0)
    #///////////////////////////////////////////////////////////
    if yo.TraerRol() == 0:
        yo.MenuClientes()
    else:
        print ("Usted no tiene permiso para ingresar a esta opción del menú.\nIngrese la opción correcta para continuar. ")
  elif opcion == 4:
    bucle = 1
print ("Final") 