
class Empleado:
    def __init__(self,id, usuario, contraseña, nombre, apellido, dni, fechaNac, genero, domicilio, email, tel, idTurno, idPuesto, rol):
        self.__id = id
        self.__usuario = usuario
        self.__contraseña = contraseña
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__fechaNac = fechaNac
        self.__genero = genero
        self.__domicilio = domicilio
        self.__email = email
        self.__tel = tel
        self.__idTurno = idTurno
        self.__idPuesto = idPuesto
        self.__rol = rol
        
    def MostrarInfo(self):
        print ("Nombre: ",self.__nombre, "\nApellido: ", self.__apellido, "\nDNI: ", self.__dni, 
               "\nFecha de nacimiento: ",self.__fechaNac,"\nGenero: ",self.__genero, 
               "\nDomicilio: ", self.__domicilio, "\nE-mail: ",self.__email, "\nTeléfono: ",self.__tel,
               "\nTurno: ",self.__idTurno,"\nPuesto: ",self.__idPuesto, "\n ")
        
    def CambiarDomicilio(self,domicilio):
        self.__domicilio = domicilio 
        
    def VerNombre(self):
       return self.__nombre   
    
    def TraerIdPuesto(self):
        resId = self.__idPuesto
        return resId
    
    def TraerRol(self):
        rol = self.__rol
        return rol
   
    def MenuCoordinadorClases(self):
        bucle = 0
        opcion = 0 
        while bucle !=1:
            try:
                opcion = int(input("Menú coordinadores de clases:\n 1- Crear una nueva clase\n 2- Editar una clase\n 3- Eliminar una clase\n 4- Ver todas las clases\n 5- Buscar clase por actividad\n 6- Volver al menú principal\n"))
            except ValueError:
                print("Se ingregó mal la opción. Vuelva a intentar.")
            if opcion == 1:
                print("#self.CrearClase()") 
                print("--<>--\n Este método le solicitará al coordinador, los datos de la nueva clase que desea crear.\n",
                      " Se completará automáticamente los datos del id, nombre del coordinador y fecha de la clase creada.\n--<>--\n"
                      )
            elif opcion == 2:
                print("#self.EditarClase()")
                print("--<>--\n El método le solicitará el id de la clase que desea modificar y luego podrá modificar los datos.\n",
                      " Al finalizar le indicará que se hicieron los cambios correctamente.\n--<>--\n")
            elif opcion == 3:
                print("#self.EliminarClase()")
                print("--<>--\n El método le solicitará el id de la clase que desea eliminar.\n",
                      " Al finalizar le indicará si la clase se eliminó correctamente.\n--<>--\n")
                
            elif opcion == 4:
                print("#self.VerClases()")
                print("--<>--\n Este método le mostrará el listado de todas las clases creadas.\n--<>--\n")
            elif opcion == 5:
                print("#self.BuscarClasePorActividad()")
                print("--<>--\n Se ingresará a un menú con el listado de las actividades que son por clase.\n",
                      "Al elegir una actividad, mostrará el listado de todas las clases (clase,día, horario y profesor).\n",
                      "Y tendrá disponible un menú para ingresar a ver los detalles de una clase, modificarla o eliminarla.\n--<>--\n")            
            elif opcion == 6:
               bucle = 1
        print ("Regresó al menú principal.")                 
        
        #print ("MenuCoordinadorClases")
        
    def MenuCoordinadorMusculacion(self):
        bucle = 0
        opcion = 0 
        while bucle !=1:
            try:
                opcion = int(input("Menú coordinadores de musculación:\n 1- Ver datos de un alumno por id\n 2- Asignar alumno a un profesor de musculación\n 3- Volver al menú principal\n"))
            except ValueError:
                print("Se ingregó mal la opción. Vuelva a intentar.")
            if opcion == 1:
                print("#self.BuscarAlumnoPorId()")
                print("--<>--\n El coordinador de musculación podrá ver los datos de cualquier cliente ingresando el id de usuario del cliente.\n--<>--\n") 
            elif opcion == 2:
                print("#self.AsignarAlumnoPersonalizado(self, idUsuario, idEmpleado)")
                print ("--<>--\n  Se recibirá una lista de los alumnos que tengan el idProfesorAsignado ==null y la horaPersonalizado != null\n",
                       " El coordinador verá los datos de los alumnos, y los nombres de los profesores que trabajan dentro del turno del horario solicitado por el cliente.",
                       " Y tendrá la opción de asignar un profesor a cada alumno segun sus objetivos\n",
                       " Para realizar el cambio, el metodo le solicitará el id del cliente y el id del profesor que le será asignado\n--<>--\n")
            elif opcion == 3:
               bucle = 1
        print ("Regresó al menú principal.")     
                    
        #print ("MenuCoordinadorMusculacion")
        
    def MenuProfeClases(self):
        bucle = 0
        opcion = 0 
        while bucle !=1:
            try:
                opcion = int(input("Menú profesores de clases de gimnasia:\n 1- Ver clases asignadas\n 2- Volver al menú principal\n"))
            except ValueError:
                print("Se ingregó mal la opción. Vuelva a intentar.")
            if opcion == 1:
                print("#self.VerClasesAsignadas()") 
                print("--<>--\n El profesor que da clases en el gimnasio, puede entrar en esta opción para consultar cuáles son todas sus clases asignadas al momento.\n",
                     " El método toma el id del profesor y realiza la consulta, mostrando el resultado obtenido.\n--<>--\n")
            elif opcion == 2:
               bucle = 1
        print ("Regresó al menú principal.")               

        #print ("MenuProfeClases")
        
    def MenuProfeMusculacion(self):
        
        bucle = 0
        opcion = 0 
        while bucle !=1:
            try:
                opcion = int(input("Menú profesores de musculación:\n 1- Crear ejercicio\n 2- Ver listado de alumnos asignados\n 3- Realizar seguimiento\n 4- Crear nueva rutina\n 5- Volver al menú principal\n"))
            except ValueError:
                print("Se ingregó mal la opción. Vuelva a intentar.")
            if opcion == 1:
                print("#self.CrearEjercicio()") 
                print ("--<>--\n Al ingresar en esta opción, el profesor de musculación podrá crear un nuevo ejercicio.\n",
                       " El método irá solicitándole todos los datos para cargar al sistema (nombre del ejercicio y su descripción detallada de como ejecutarlo correctamente).\n--<>--\n")   
            elif opcion == 2:
                print("#self.VerListadoAlumnos()")
                print("--<>--\n Este método, tomando el id del profesor que realiza la consulta, mostará el listado de los alumnos que le han sido asignados para su entrenamiento personalizado.\n--<>--\n")
                
            elif opcion == 3:
                print("#self.SeguimientoAlumno()")
                print("--<>--\n Ingresando el id del cliente o su nombre y apellido, ingresará a la rutina del alumno para hacer el seguimiento.\n",
                      " Tendrá un menú para seleccionar si desea modificar la rutina o crear una nueva.\n--<>--\n") 
            elif opcion == 4:
                print("#self.CrearRutina()")
                print("--<>--\n Con esta opción, el profesor de musculación creará una rutina nueva para su alumno.\n",
                      " El método le pedirá los datos necesarios, y de manera automática, completará el id del autor y la fecha de creación de la rutina.\n--<>--\n")
            elif opcion == 5:
               bucle = 1
        print ("Regresó al menú principal.")     
                    
        #print ("MenuProfeMusculacion")
        
            
        