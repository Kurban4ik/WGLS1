#include <iarduino_RTC.h>                               // подключение библиотеки
iarduino_RTC time(RTC_DS1302, 8, 6, 7);         // Задаем правильно название нашего модуля, а также указываем к каким цифровым пинам его подключаем(в нашем случае – 8,6,7)
#define gas 9
#define food 3
#define trash 4
#define light 5
#define cout Serial.println
#define ts time.gettime
#define depth A0
using namespace std;
// параметры уровня воды 1 - норма, 2 - недостача, 3 - переполнение

void turn (int a, int b){
  if (b) pinMode(a, OUTPUT);
  else pinMode(a, INPUT );
  
}

void work(int module, int de){
  turn(module, 1);
  delay(de);
  turn(module, 0);
}

void setup()
{
  delay(300);
  Serial.begin(9600);
  time.begin();
  time.settime(0, 0, 10, 13, 0, 0, 0); // 0  сек, 30 мин, 18 часов, 12, июня, 2020, четверг
}

int com = -1;
void loop()
{
  
  if (com == -1);
    com = Serial.parseInt();
  
  if (com == 1) {work(food, 1000); cout("ok 1");}
  if (com == 2) {work(trash, 1000); cout("ok 2");}
  if (com == 4) {work(gas, 1000); cout("ok 3");}
  if (com == 3) {
    if (com == 0) {turn(light, 0); cout("ok 4");}
    else {turn(light, 1); cout("ok 5");}
  }
  
  if (600 <= analogRead(depth) && analogRead(depth) <= 675) cout("0 1");
  else if (analogRead(depth) < 600) cout("0 2");
  else cout("0 3");
  
  delay(500);
  
}
