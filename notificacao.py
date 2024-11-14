from tkinter.commondialog import Dialog
from tkinter import Tk, messagebox
import serial

# Configura a conexão serial (substitua 'COM3' pela porta que seu Arduino está conectado)
arduino = serial.Serial('COM3', 9600, timeout=1)  # Adiciona um timeout para evitar travamentos

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
        dados = dados.decode('utf-8').strip() # Converte para string
        try:
            return int(dados)  # Tenta converter os dados para um inteiro
        except ValueError:
            return None  # Caso não consiga converter, retorna N one
    return None  # Caso não haja dados

if __name__ == "__main__":
      # Verifica se o valor é válido
        print("warning", showwarning("Umidade baixa... :(", "Hora de regar sua plantinha!"))
