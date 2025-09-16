import socket
import hashlib

def hashear(clave):
    return hashlib.sha256(clave.encode()).hexdigest()

def cliente():
    host = "127.0.0.1"
    puerto = 8080

    print("1. Iniciar sesión")
    print("2. Registrarse")
    opcion = input("Elige una opción (1/2): ")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    clave_hash = hashear(clave)
    mensaje = f"{opcion}:{usuario}:{clave_hash}"

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))
    cliente.send(mensaje.encode())

    respuesta = cliente.recv(1024).decode()
    print(f"Servidor: {respuesta}")
    cliente.close()

if __name__ == "__main__":
    cliente()
