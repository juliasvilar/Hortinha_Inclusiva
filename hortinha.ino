#include <LiquidCrystal.h>
#define umidadeAnalogica A0 //Atribui o pino A0 a variável umidade - leitura analógica do sensor
#define umidadeDigital 7 //Atribui o pino 7 a variável umidadeDigital - leitura digital do sensor

int valorumidade; //Declaração da variável que armazenará o valor da umidade lida - saída analogica
int valorumidadeDigital; //Declaração da variável que armazenara a saída digital do sensor de umidade do solo

//Define os pinos que serão utilizados para ligação ao display
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
 
void setup()
{
  Serial.begin(9600); //Incia a comunicação serial
  pinMode(umidadeAnalogica, INPUT); //Define umidadeAnalogica como entrada
  pinMode(umidadeDigital, INPUT); //Define umidadeDigital como entrada
  //Define o número de colunas e linhas do LCD
  lcd.begin(16, 2);
}
 
void loop()
{
  //Limpa a tela
  lcd.clear();
  //Posiciona o cursor na coluna 3, linha 0;

  valorumidade = analogRead(umidadeAnalogica); //Realiza a leitura analógica do sensor e armazena em valorumidade
  valorumidade = map(valorumidade, 1023, 315, 0, 100); //Transforma os valores analógicos em uma escala de 0 a 100

  Serial.print("Umidade encontrada: "); //Imprime mensagem
  Serial.print(valorumidade); //Imprime no monitor serial o valor de umidade em porcentagem
  Serial.println(" % " );

  // valorumidadeDigital = digitalRead(umidadeDigital); //Realiza a leitura digital do sensor e armazena em valorumidadeDigital
  if (valorumidade > 45) { 
    Serial.println("Status: Solo úmido");
    lcd.setCursor(0, 0);
    lcd.print("Terra molhadinha");
    lcd.setCursor(7, 1);
    lcd.print(valorumidade);
    lcd.print("%");
  }
  else { // se esse valor for igual a 1, será mostrado no monitor serial que o solo está seco e o led vermelho se acende
    Serial.println("Status: Solo seco");
    lcd.setCursor(1, 0);
    lcd.print("Terra sequinha");
    lcd.setCursor(7, 1);
    lcd.print(valorumidade);
    lcd.print("%");
  }
  delay(500); //Atraso de 500ms
}
