---

# Password Verified 🔒

**Password Verified** es una herramienta en Python que permite verificar si una contraseña ha sido comprometida en una brecha de datos utilizando la API de [PwnedPasswords](https://haveibeenpwned.com/Passwords). Puedes usarla tanto en modo **CLI** como en una interfaz **GUI** simple e intuitiva.

---

## Características

- **Modo CLI**: Ejecuta la herramienta desde la terminal.
- **Modo GUI**: Interfaz gráfica para verificar contraseñas.
- **API de PwnedPasswords**: Utiliza una API confiable para comprobar la seguridad de la contraseña.
- **SHA-1 Hashing**: Las contraseñas se codifican con SHA-1 antes de ser enviadas a la API.

---

## Requisitos

**Instala las dependencias:**

   Este script requiere `requests` y `tkinter`. Instálalo con pip:

   ```bash
   pip install requests
   pip install tkinter
   pip install argparse
   ```

## Uso

### Modo CLI

Para verificar una contraseña desde la terminal:

```bash
python PasswordVerified.py
```

El programa pedirá la contraseña de manera segura (oculta en la entrada).

### Modo Gráfico

Para ejecutar el modo gráfico:

```bash
python PasswordVerified.py --g
```

Este comando abrirá una interfaz gráfica donde podrás ingresar tu contraseña y ver el resultado.

---

## Funcionamiento

1. La contraseña ingresada se codifica con SHA-1 para obtener un hash.
2. Los primeros 5 caracteres del hash se envían a la API de PwnedPasswords.
3. La API devuelve una lista de posibles coincidencias, que se comparan con el hash completo de la contraseña.
4. Si se encuentra una coincidencia, el programa muestra cuántas veces ha sido comprometida esa contraseña.

---

---
