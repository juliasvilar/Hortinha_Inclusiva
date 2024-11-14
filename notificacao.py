from tkinter.commondialog import Dialog
import serial
import time

# Configura a conexão serial (substitua 'COM3' pela porta que seu Arduino está conectado)
arduino = serial.Serial('COM5', 9600, timeout=1)  # Adiciona um timeout para evitar travamentos
time.sleep(2)

__all__ = ["showwarning"]

# icons
WARNING = "warning"

# replies
OK = "ok"
CANCEL = "cancel"
YES = "yes"
NO = "no"

class Message(Dialog):
    "A message box"

    command  = "tk_messageBox"

def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and "icon" not in options:    options["icon"] = _icon
    if _type and "type" not in options:    options["type"] = _type
    if title:   options["title"] = title
    if message: options["message"] = message
    res = Message(**options).show()
    # In some Tcl installations, yes/no is converted into a boolean.
    if isinstance(res, bool):
        if res:
            return YES
        return NO
    # In others we get a Tcl_Obj.
    return str(res)

def showwarning(title=None, message=None, **options):
    "Show a warning message"
    return _show(title, message, WARNING, OK, **options)

def ler_dados():
    if arduino.in_waiting > 0:  # Verifica se há dados disponíveis na porta serial
        dados = arduino.readline()  # Lê a linha de dados e remove espaços e quebras de linha
        dados_string = dados.decode('utf-8').strip() # Converte para string
        try:
            return int(dados_string)  # Tenta converter os dados para um inteiro
        except ValueError:
            print("Erro.\n")  # Caso não consiga converter, retorna N one
    return None

if __name__ == "__main__":
    while True:
        dados = ler_dados()
        if dados is not None:
            if dados > 45:
                print("warning", showwarning("Umidade baixa... :(", "Hora de regar sua plantinha!"))
            else:
                print("Não precisa regar.\n")
        else:
            print("Nenhum dado recebido.\n")
        time.sleep(1)
