class biblioteca():
    def __init__(self, libro,usuario):
      self.libro = libro
      self._usuario = usuario 

    


      class usuario(biblioteca):
        def __init__(self, nombre):
              self.nombre = nombre 
        def informacion_usuario(self):
           return self.nombre   

        def usuarios_nuevos(sel,usuario_nuevo):
           self.usuario_nuevo = usuario_nuevo
           if usuario_nuevo == usuario :
              raise TypeError("El usuario ya existe.")
           print("el usuario a sido aceptado correctamente. ")
           
           
        class libro (biblioteca):
            def __init__(self,categoria):
                self.categoria = categoria 
                romance = libro("romance ")

            def nuevo_libro(self):
               
            

              

