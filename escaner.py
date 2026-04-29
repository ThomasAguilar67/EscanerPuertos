import socket
from datetime import datetime

# 1. Definimos nuestro objetivo (Un servidor de pruebas legal para Hacking Ético)
objetivo = "scanme.nmap.org"

# 2. Elegimos qué "puertas" queremos revisar
# 21: FTP (Archivos), 22: SSH (Consola), 80: HTTP (Web), 443: HTTPS (Web Segura)
puertos_estrategicos = [21, 22, 80, 443, 3306, 8080]

print("-" * 50)
print(f"[*] INICIANDO RECONOCIMIENTO TÁCTICO")
print(f"[*] Objetivo: {objetivo}")
print(f"[*] Hora de inicio: {datetime.now().strftime('%H:%M:%S')}")
print("-" * 50)

try:
    for puerto in puertos_estrategicos:
        # Creamos la "sonda" de red (Un socket TCP)
        sonda = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Le damos 1 segundo máximo para responder (si no, asumimos que está cerrado)
        socket.setdefaulttimeout(1) 
        
        # Intentamos golpear la puerta. Si devuelve '0', es que está abierta.
        resultado = sonda.connect_ex((objetivo, puerto))
        
        if resultado == 0:
            print(f"[+] ALERTA: El puerto {puerto} está ABIERTO")
        else:
            print(f"[-] El puerto {puerto} está cerrado o bloqueado por Firewall")
            
        # Cerramos la sonda para volver a usarla en el siguiente puerto
        sonda.close()

except KeyboardInterrupt:
    print("\n[!] Escaneo cancelado manualmente por el usuario.")
except socket.error:
    print("\n[!] Error fatal: No se pudo conectar a la red objetivo.")

print("-" * 50)
print("[*] RECONOCIMIENTO FINALIZADO")