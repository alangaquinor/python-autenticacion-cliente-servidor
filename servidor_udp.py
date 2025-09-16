import socket
from datetime import datetime

def cargar_usuarios():
    usuarios = {}
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            if ":" in linea:
                u, c = linea.strip().split(":")
                usuarios[u] = c
    return usuarios

def log_actividad(addr, accion, resultado):
    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[{tiempo}] {addr} - {accion} - {resultado} (UDP)\n"
    with open("logs.txt", "a") as archivo_log:
        archivo_log.write(log)

def servidor_udp():
    usuarios = cargar_usuarios()
    host = "127.0.0.1"
    puerto = 9090

    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((host, puerto))
    print(f"Servidor UDP escuchando en {host}:{puerto}...")

    while True:
        datos, addr = servidor.recvfrom(1024)
        partes = datos.decode().split(":")
        if len(partes) != 3:
            servidor.sendto("Formato inválido".encode(), addr)
            log_actividad(addr, "Formato inválido", "Rechazado")
            continue

        opcion, usuario, clave = partes

        if opcion == "1":
            accion = "Inicio de sesión"
            if usuario in usuarios and usuarios[usuario] == clave:
                respuesta = "Acceso concedido"
            else:
                respuesta = "Acceso denegado"

        elif opcion == "2":
            accion = "Registro"
            if usuario in usuarios:
                respuesta = "Nombre de usuario ya existe"
            else:
                with open("usuarios.txt", "a") as archivo:
                    archivo.write(f"{usuario}:{clave}\n")
                usuarios[usuario] = clave
                respuesta = "Usuario registrado con éxito"
        else:
            accion = "Opción inválida"
            respuesta = "Opción inválida"

        servidor.sendto(respuesta.encode(), addr)
        log_actividad(addr, accion, respuesta)

if __name__ == "__main__":
    servidor_udp()
