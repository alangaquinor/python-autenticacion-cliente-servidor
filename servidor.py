import socket
import threading
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
    log = f"[{tiempo}] {addr} - {accion} - {resultado}\n"
    with open("logs.txt", "a") as archivo_log:
        archivo_log.write(log)

def manejar_cliente(conn, addr, usuarios):
    print(f"[+] Nueva conexión desde {addr}")
    try:
        datos = conn.recv(1024).decode()
        partes = datos.split(":")
        if len(partes) != 3:
            conn.send("Formato inválido".encode())
            log_actividad(addr, "Formato inválido", "Rechazado")
            return

        opcion, usuario, clave = partes

        if opcion == "1":  # Iniciar sesión.
            accion = "Inicio de sesión"
            if usuario in usuarios and usuarios[usuario] == clave:
                respuesta = "Acceso concedido"
            else:
                respuesta = "Acceso denegado"

        elif opcion == "2":  # Registro.
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

        conn.send(respuesta.encode())
        log_actividad(addr, accion, respuesta)

    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
        log_actividad(addr, "Error", str(e))
    finally:
        conn.close()
        print(f"[-] Conexión cerrada con {addr}")

def servidor():
    usuarios = cargar_usuarios()
    host = "127.0.0.1"
    puerto = 8080

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(5)
    print(f"Servidor escuchando en {host}:{puerto}...")

    while True:
        conn, addr = servidor.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr, usuarios))
        hilo.start()
        print(f"[INFO] Clientes activos: {threading.active_count() - 1}")

if __name__ == "__main__":
    servidor()
