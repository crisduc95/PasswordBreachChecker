import hashlib
import requests
import getpass
from tkinter import *


class PasswordVerified:

    def __init__(self, password):
        self.password = password
    
    def __encodeSha1(self):
        algoritmo = hashlib.sha1(self.password.encode()) # cifrar Dato
        cifrado = (algoritmo.hexdigest()) # convierte la clave cifrada en una cadena de texto legible
        return cifrado
    
    def verified(self):
        cifrado = self.__encodeSha1()
        caracteres = (cifrado[:5])
        resto_hash = (cifrado[5:])
        url = "https://api.pwnedpasswords.com/range/"+caracteres
        response = requests.get(url)
        hashes = (line.split(':') for line in response.text.splitlines())
        if response.status_code == 200:

            for hashcompleto, count in hashes:
                if hashcompleto.lower() == resto_hash:
                    print(f"Contraseña encontrada. Se ha visto {count} veces")
                    
                    return True
            else:
                print(f"Contraseña no encontrada")
                return False
        else:
            print(f"API no responde")
    
    def modoGrafico(self):
        pass


if __name__ == "__main__":
    p = getpass.getpass()
    passve = PasswordVerified(p)
    passve.verified()


