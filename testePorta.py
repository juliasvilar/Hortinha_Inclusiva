import serial
import time

# Configura a porta serial (substitua 'COM3' pelo nome da porta do seu Arduino)
porta_serial = 'COM5'  # ou '/dev/ttyUSB0' no Linux
baud_rate = 9600  # O mesmo baud rate definido no Arduino (9600)

try:
    # Inicializa a comunicação serial
    arduino = serial.Serial(porta_serial, baud_rate)
    print("Conexão com Arduino estabelecida.")
    time.sleep(2)  # Tempo para garantir a inicialização da conexão
except serial.SerialException:
    print("Erro ao conectar à porta serial. Verifique a porta e tente novamente.")
    exit()

def ler_dados_serial():
    while True:
        # Verifique se há dados para ler
        if arduino.in_waiting > 0:
            try:
                # Lê e exibe os dados do Arduino
                linha = arduino.readline().decode('utf-8').strip()
                print("Recebido do Arduino:", linha)
            except UnicodeDecodeError:
                print("Erro de decodificação. Pulando mensagem.")
        time.sleep(0.5)  # Delay para reduzir a velocidade de leitura

try:
    ler_dados_serial()
except KeyboardInterrupt:
    print("\nInterrompido pelo usuário.")
finally:
    arduino.close()
    print("Conexão com Arduino encerrada.")
