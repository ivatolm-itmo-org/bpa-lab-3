# Национальный исследовательский университет ИТМО
# Лабараторная работа №3
## Вариант 3015
### Толмачев Иван (P3130)

# Исходная программа

```
271:  0283 ; ~unknown~        ; ~переменная A~
272:  0200 ; CLA              ; ~буфер~
273:  4000 ; ADD   0          ; ~счетчик цикла~
274:  0200 ; CLA              ; ~результат~
275: +0200 ; CLA              ; Загрузить 0
276:  EEFD ; ST    (IP-0x3)   ; Сохранить в [274]
277:  AF03 ; LD    #0x3       ; Загрузить 3
278:  EEFA ; ST    (IP-0x6)   ; Сохранить в [273]
279:  4EF7 ; ADD   (IP-0x9)   ; Сложить с [271]
27A:  EEF7 ; ST    (IP-0x9)   ; Сохранить в [272]
27B:  ABF6 ; LD   -(IP-[0xa]) ; Загрузить [[272] - 1]
27C:  F303 ; BPL   3          ; Если + прыгнуть на [280]
27D:  AEF6 ; LD    (IP-0xa)   ; Загрузить из [274]
27E:  0700 ; INC              ; Добавить 1
27F:  EEF4 ; ST    (IP-0xc)   ; Сохранить в [274]
280:  8273 ; LOOP  273        ; [273] -= 1, если [273] <= 0, то IP += 1
281:  CEF9 ; JUMP  (IP-0x7)   ; Прыгнуть на 27A
282:  0100 ; HALT             ; Стоп
283:  074D ; ~unknown~        ; ~переменная B~ ; элемент массива
284:  02A5 ; ~unknown~        ; ~переменная C~ ; элемент массива
285:  F800 ; BLT   0          ; ~переменная D~ ; элемент массива
```

## Перевод в читаемый вид
```
[274] = 0                     ; res = 0
[273] = 3                     ; cntr = 3
[272] = [271] + [273]         ; tmp = a + cntr
do {                          ; do {
  if ([[272] - 1] >= 0)       ;   if (*(tmp--) >= 0)
    continue                  ;     continue
  [274] = [274] + 1           ;   result++
} while ([273]--; [273] <= 0) ; } while (cntr--; cntr <= 0)
```

# Предназначение и описание программы
Данная программа считает количество неотрицательных чисел в массиве с конца.
Представление программы со всеми переменными в псевдокоде.
```
a = 0x283
arr = [0x74d, 0x2a5, 0xf800]
res = 0
cntr = 3
tmp = a + cntr
do {
  if (arr[tmp--] >= 0)
    continue
  result++
} while (cntr--; cntr <= 0)
```

# Область определения и область значений
Исходные данные, то есть переменные A, B, C, D отличаются областями определения.
Для пременных B, C, D это любое 16-ричное значение, то есть значения от 0 до 2^16 - 1 или от -2^15 до 2^15 - 1.
Для переменной A есть ограничения. Так как участвует в вычислении адреса, а адрес неотрицательный, то она может принимать значения от -3 до 2^16 - 1 - 3. По факту, для того чтобы значения были определены, она должна быть от 0x271 до 0x283.

Областью значений функции является отрезок от 0 до 3 (кол-во эл-ов массива).

Буфер тоже сильно ограничен из-за a и cntr.

# Трассировка программы
A =
B =
C =
D =