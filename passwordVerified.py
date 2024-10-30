import hashlib
import requests
import getpass
import argparse
from tkinter import *
from tkinter import messagebox

# Clase para verificar si una contraseña ha sido filtrada en brechas de seguridad.
class PasswordVerified:

    # Constructor de la clase. Acepta un parámetro opcional `password` para el modo CLI y `entrada_password` para el modo gráfico.
    def __init__(self, password="1234", entrada_password=""):
        self.password = password
        self.entrada_password = entrada_password  # Entrada para el modo gráfico.

    # Método privado para codificar la contraseña usando el algoritmo SHA-1.
    def __encodeSha1(self):
        # Convierte la contraseña en un hash SHA-1
        algoritmo = hashlib.sha1(self.password.encode())
        cifrado = algoritmo.hexdigest()  # Convierte el hash en una cadena hexadecimal legible.
        return cifrado
    
    # Verifica si la contraseña ha sido comprometida utilizando la API de PwnedPasswords.
    def verified(self):
        cifrado = self.__encodeSha1()  # Genera el hash SHA-1 de la contraseña.
        caracteres = cifrado[:5]       # Toma los primeros 5 caracteres del hash (para la API).
        resto_hash = cifrado[5:]       # El resto del hash se usa para la comparación.
        
        # Llama a la API de PwnedPasswords con los primeros 5 caracteres del hash.
        url = "https://api.pwnedpasswords.com/range/" + caracteres
        response = requests.get(url)
        hashes = (line.split(':') for line in response.text.splitlines())  # Procesa los hashes devueltos por la API.

        if response.status_code == 200:
            # Recorre los hashes devueltos por la API y compara con el hash de la contraseña.
            for hashcompleto, count in hashes:
                retornar = [True, count]  # Estructura de retorno cuando la contraseña es comprometida.
                if hashcompleto.lower() == resto_hash:
                    # Mensaje si la contraseña ha sido encontrada en una brecha de datos.
                    resultado = f"Contraseña encontrada. Se ha visto {count} veces"
                    print(resultado)
                    return retornar
            else:
                # Mensaje si la contraseña no ha sido encontrada.
                resultado = "Contraseña no encontrada"
                print(resultado)
                return False
        else:
            # Mensaje de error si la API no responde.
            print("API no responde")

    # Verifica la contraseña ingresada en el modo gráfico y muestra el resultado en una ventana emergente.
    def verificarPassword(self):
        self.password = self.entrada_password.get()  # Obtiene la contraseña ingresada en el campo de entrada.
        resul = passve.verified()  # Llama a la función verified para comprobar la contraseña.
        
        # Verifica si la contraseña fue encontrada en una brecha de seguridad.
        if self.password:
            if resul:
                resultado = f"Contraseña encontrada. Se ha visto {resul[1]} veces"
                messagebox.showinfo("Resultado", resultado)  # Muestra el mensaje si la contraseña es vulnerable.
            else:
                mensajeError = "Contraseña no encontrada"
                messagebox.showinfo("Resultado", mensajeError)  # Muestra el mensaje si la contraseña no ha sido encontrada.
        else:
            # Muestra un mensaje de advertencia si no se ingresa una contraseña.
            mensaje = "Por favor, ingrese contraseña"
            print(mensaje)
            messagebox.showwarning("Advertencia", mensaje)

    # Inicia la interfaz gráfica para ingresar y verificar la contraseña.
    def modoGrafico(self):
        app = Tk()
        app.geometry("400x200")  # Define el tamaño de la ventana.
        app.title("Verificador de contraseñas")  # Título de la ventana.
        
        # Etiqueta para indicar al usuario que ingrese la contraseña.
        label = Label(app, text="Ingresa la contreaseña: ", font=("Arial", 12))
        label.pack(pady=10)
        
        # Campo de entrada de contraseña (oculta el texto).
        self.entrada_password = Entry(app, show="*", font=("Arial", 12))
        self.entrada_password.pack(pady=5)
        
        # Botón para verificar la contraseña ingresada.
        verify_button = Button(app, text="Verificar", command=self.verificarPassword, font=("Arial", 12))
        verify_button.pack(pady=10)

        app.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica.


# Código principal para ejecutar la herramienta.
if __name__ == "__main__":
    # Configuración de argparse para seleccionar entre modo gráfico o CLI.
    parser = argparse.ArgumentParser(description="Verificador de contraseña filtrada")
    parser.add_argument("--g", "--gui", action="store_true", required=False, help="--g. Activa el modo gráfico")
    
    args = parser.parse_args()
    grafic = args.g

    if grafic:
        # Si se pasa el argumento --g, inicia el modo gráfico.
        passve = PasswordVerified()
        passve.modoGrafico()
    else:
        # Si no, inicia el modo CLI y solicita la contraseña en la consola.
        p = getpass.getpass()
        passve = PasswordVerified(p)
        passve.verified()
