class usuario():
      def __init__(self, nombre):
              self.nombre = nombre 
      def informacion_usuario(self):
       return f"el usuario es: {self.nombre}"

      def usuarios_nuevos(sel,usuario_nuevo):
           self.usuario_nuevo = usuario_nuevo
           if usuario_nuevo == usuario :
              raise TypeError("El usuario ya existe.")
           print("el usuario a sido aceptado correctamente. ")
           
class libro ():
       def __init__(self,categoria,titulo):
        self.categoria = categoria
        self.titulo = titulo

       def infomacion_libro(self):
           return f"categoria, {self.categoria}, libro, {self.titulo}"
    
      
               
class biblioteca():
    def __init__(self, libro,usuario):
      self.libro = libro
      self._usuario = usuario                 
               
            

              

