import socket
import hashlib

def hashear(clave):
    return hashlib.sha256(clave.encode()).hexdigest()

def cliente_udp():
    host = "127.0.0.1"
    puerto = 9090  # Distinto al TCP para no interferir.

    print("1. Iniciar sesión")
    print("2. Registrarse")
    opcion = input("Elige una opción (1/2): ")

    usuario = input("Usuario: ")
    clave = input("Clave: ")
    clave_hash = hashear(clave)

    mensaje = f"{opcion}:{usuario}:{clave_hash}".encode()

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.sendto(mensaje, (host, puerto))

    respuesta, _ = cliente.recvfrom(1024)
    print(f"Servidor UDP: {respuesta.decode()}")
    cliente.close()

if __name__ == "__main__":
    cliente_udp()
