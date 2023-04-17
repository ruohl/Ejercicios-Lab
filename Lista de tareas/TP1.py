class Tareas:
    def __init__(self):
        self.__HistorialTareas = []
        
    def AgregarTareas(self, Titulo: str, Descripción: str, Estado: str):
        with open("Lista de tareas/TareasGuardadas.txt", "r") as f:           
            if f.read() == "":
                self.__HistorialTareas.append({Titulo :[Descripción, Estado]})
                with open("Lista de tareas/TareasGuardadas.txt", "w") as f:
                    f.write(str(self.__HistorialTareas))
            else:
                with open("Lista de tareas/TareasGuardadas.txt", "r") as f:  
                    # eliminar comillas de cada diccionario en la lista
                    self.__HistorialTareas = [{Clave:Valor for Clave, Valor in NuevoDicc.items()} for NuevoDicc in eval(f.read().strip())]
                    # agregar nuevo diccionario a la lista
                    self.__HistorialTareas.append({Titulo :[Descripción, Estado]})
                    # guardar lista actualizada en el archivo
                    with open("Lista de tareas/TareasGuardadas.txt", "w") as f:
                        f.write(str(self.__HistorialTareas))

    def MostrarTareas(self):
        ListaDeTareas = []
        with open("Lista de tareas/TareasGuardadas.txt", "r") as f:
            self.__HistorialTareas = [{Clave:Valor for Clave, Valor in NuevoDicc.items()} for NuevoDicc in eval(f.read().strip())]
            Max = len(self.__HistorialTareas)
            for x in range(0, Max):
                for Titulo, DescripcionyEstado in self.__HistorialTareas[x].items():
                    ListaDeTareas.append("\nTitulo: " + Titulo + "\nDescripción: " + DescripcionyEstado[0] + "\nEstado: " + DescripcionyEstado[1])
            return ListaDeTareas               
    
    def MarcarCompletada(self, Titulo: str):
        TareaCompletar = ""
        with open("Lista de tareas/TareasGuardadas.txt", "r+") as f:
            self.__HistorialTareas = [{Clave:Valor for Clave, Valor in NuevoDicc.items()} for NuevoDicc in eval(f.read().strip())]
            Max = len(self.__HistorialTareas)
            for x in range(0, Max):
                for Nombre, DescripcionyEstado in self.__HistorialTareas[x].items():
                    if Titulo == Nombre:
                        TareaCompletar = x
            if TareaCompletar == x:
                for Titulo, DescripcionyEstado in self.__HistorialTareas[TareaCompletar].items():
                        DescripcionyEstado[1] = "Completado"
                        with open("Lista de tareas/TareasGuardadas.txt", "w") as f:
                            f.write(str(self.__HistorialTareas))
            else:
                raise Exception("La tarea no existe")
    
    def EliminarTarea(self, Titulo: str):
        with open("Lista de tareas/TareasGuardadas.txt", "r+") as f:
            self.__HistorialTareas = [{Clave:Valor for Clave, Valor in NuevoDicc.items()} for NuevoDicc in eval(f.read().strip())]
            Max = len(self.__HistorialTareas)
            for x in range(0, Max):
                for Nombre, DescripcionyEstado in self.__HistorialTareas[x].items():
                    if Titulo == Nombre:
                        TareaEliminar = x
            if TareaEliminar == x:
                with open("Lista de tareas/TareasGuardadas.txt", "w") as f:
                            f.write(str(self.__HistorialTareas))
            else:
                raise Exception("La tarea no existe")
                

    def FiltrarTareas(self, Estado: str):
        ListaDeTareas = []
        with open("Lista de tareas/TareasGuardadas.txt", "r+") as f:
            self.__HistorialTareas = [{Clave:Valor for Clave, Valor in NuevoDicc.items()} for NuevoDicc in eval(f.read().strip())]
            Max = len(self.__HistorialTareas)
            for x in range(0, Max):
                for Titulo, DescripcionyEstado in self.__HistorialTareas[x].items():
                    if DescripcionyEstado[1] == Estado:
                        ListaDeTareas.append("\nTitulo: " + Titulo + "\nDescripción: " + DescripcionyEstado[0] + "\nEstado: " + DescripcionyEstado[1])
            return ListaDeTareas


Usu = Tareas()
#Usu.AgregarTareas("Tarea de laboratorio", "Hacer codigo :(", "Pendiente")
#print(*Usu.MostrarTareas())
#Usu.MarcarCompletada("Mate")
#print(*Usu.MostrarTareas())
#Usu.EliminarTarea("Mate")
print(*Usu.MostrarTareas())
print(*Usu.FiltrarTareas("Pendiente"))