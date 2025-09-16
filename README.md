# 🔑 Sistema Cliente-Servidor en Python

Este repositorio contiene un proyecto en **Python** que implementa un 
sistema **cliente-servidor con autenticación básica**, desarrollado por 
**Alan G. Aquino R.**

El programa permite practicar y aplicar conceptos como:
- Comunicación en red usando **sockets TCP y UDP**.
- Autenticación de usuarios con credenciales.
- Registro de nuevos usuarios.
- Manejo de múltiples conexiones con **multithreading**.
- Uso de **hash SHA-256** para proteger contraseñas.
- Registro de actividad mediante logs.

---

# 📂 Contenido

Cada archivo cumple una función dentro del sistema:

1. `cliente.py` → Cliente TCP con soporte login y registro.  
2. `servidor.py` → Servidor TCP multicliente con logs y autenticación.  
3. `cliente_udp.py` → Cliente alternativo usando UDP.  
4. `servidor_udp.py` → Servidor alternativo usando UDP.  
5. `usuarios.txt` → Archivo con credenciales.  
6. `logs.txt` → Archivo de actividad generado automáticamente.   
8. `README.md` → Documento de explicaciones e instrucciones.  
9. ` Documento Informe Autenticación Básica en Python.docx` → Informe del proyecto.  
10. `Imagen Diagrama de flujo.png` → Diagrama de flujo del sistema.  

---

# 🚀 Ejecución

## TCP
1. Ejecutar el servidor:
   python servidor.py

2. En otra terminal ejecutar el cliente:
   python cliente.py

3. Seleccionar opción:
   - Iniciar sesión.
   - Registrarse.

## UDP
1. Ejecutar el servidor UDP:
   python servidor_udp.py

2. En otra terminal ejecutar el cliente UDP:
   python cliente_udp.py

---

# 📖 Requisitos

- Python 3.8 o superior.  
- Sistema operativo: Windows, Linux o macOS.

---

# 🤝 Contribuciones

¡Las mejoras son bienvenidas!  
Puedes agregar nuevas funcionalidades como:
- Bases de datos en lugar de archivos de texto.   
- Interfaces gráficas para cliente-servidor.  
---

# 👨‍💻 Autor

Desarrollado por **Alan G. Aquino R.**  
Estudiante de Ingeniería en Informática.  

---

# 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.  
Eres libre de usar, modificar y compartir el código con fines educativos o profesionales.
