class Cliente:
    def __init__(self,id, usuario, contraseña, nombre, apellido, dni, fechaNac, genero, domicilio, email, tel, peso, altura, imc, edad, idProfesorAsignado, horaPersonalizado, objetivo, rol):
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
        self.__peso = peso
        self.__altura = altura
        self.__imc = imc
        self.__edad = idProfesorAsignado
        self.__horaPersonalizado = horaPersonalizado
        self.__objetivo = objetivo
        self.__rol = rol
        
    def MostrarInfo(self):
        print ("Nombre: ",self.__nombre, "\nApellido: ", self.__apellido,"\nGenero: ",self.__genero, 
               "\nDomicilio: ", self.__domicilio, "\nE-mail: ",self.__email, "\nTeléfono: ",self.__tel,
               "\npeso: ",self.__peso,"\naltura: ",self.__altura, "\nimc:  ",self.__imc,
               "\nedad: ",self.__edad,"\nhoraPersonalizsdo: ",self.__horaPersonalizado,
               "\nobjetivo: ",self.__objetivo,"\n") 
        
    def TraerRol(self):
        rol = self.__rol
        return rol
          
    def MenuClientes(self):
        bucle = 0
        opcion = 0 
        while bucle !=1:
            try:
                opcion = int(input("Menú clientes:\n 1- Ver clases disponibles\n 2- Buscar clases por actividad\n 3- Buscar ejercicio por el nombre\n 4- Consultar rutina actual\n 5- Ver historial de entrenamiento\n 6- Ver mi perfil\n 7- Volver al menú principal\n"))
            except ValueError:
                print("Se ingregó mal la opción. Vuelva a intentar.")
            if opcion == 1:
                print("#self.VerClases()") 
                print("--<>--\n El cliente al ingresar en esta opción, obtendrá la lista de todas las clases que estan disponibles en el gimnasio.\n--<>--\n")
            elif opcion == 2:
                print("#self.BuscarClasePorActividad()") 
                print("--<>--\n Al elegir esta opción, accede a un menú con todas las actividades que ofrecen clases,\n ",
                      " al seleccionar una opción, verá todos los días y horarios en los que tiene disponibles esas clases.\n--<>--\n")
            elif opcion == 3:
                print("#self.BuscarEjercicioPorNombre()") 
                print("--<>--\n El cliente al elegir esta opción, puede ver los detalles de un ejercicio.  Lo buscará ingresando su nombre.\n--<>--\n")
            elif opcion == 4:
                print("#self.ConsultaRutina()") 
                print ("--<>--\n El método al contar con los datos del cliente, buscará la ultima rutina y le mostrará toda la información de ella.\n--<>--\n")
            elif opcion == 5:
                print("#self.VerHistorialEntrenamiento()") 
                print ("--<>--\n Con el id del cliente, este método podrá recuperar la información de todas las rutinas que tuvo el alumno a lo largo de todo su entrenamiento personalizado.\n--<>--\n")            
            elif opcion == 6:
                print("#self.VerPerfil()") 
                print ("--<>--\n Opción que muestra los datos del cliente, para que el mismo pueda controlar que todo se encuentra al día y de manera correcta.\n--<>--\n")
            elif opcion == 7:    
               bucle = 1
        print ("Regresó al menú principal.")              
        
        #print ("MenuCoordinadorClases")
              