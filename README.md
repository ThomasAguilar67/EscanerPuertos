# 📡 Escáner de Puertos Táctico (Red Team)

Herramienta de reconocimiento de redes desarrollada en Python. Simula el comportamiento de escáneres de seguridad profesionales (como Nmap) para descubrir servicios activos en servidores remotos.

## 🚀 Características
* **Reconocimiento Activo:** Uso de Sockets TCP (`socket.SOCK_STREAM`) para testear conexiones.
* **Descubrimiento de Servicios:** Identificación de puertos críticos abiertos (SSH, HTTP, FTP, Bases de Datos).
* **Manejo de Tiempos:** Implementación de "Timeouts" para evitar bloqueos y acelerar el escaneo.
* **Manejo de Excepciones:** Captura de errores de red y cancelaciones del usuario (`KeyboardInterrupt`).

## 🛠️ Conceptos Aplicados
* Hacking Ético y Reconocimiento (Footprinting).
* Protocolos de red (TCP/IP).
* Programación de redes en Python puro.