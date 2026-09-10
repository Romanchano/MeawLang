# MeawLang 

MeawLang — это минималистичный и масштабируемый байт-ориентированный эзотерический язык программирования в кошачьем стиле. Он вдохновлен такими классическими эзотерическими языками, как MiniStringFuck и Chicken, а также использует принципы унарной системы счисления для управления аргументами.

```text
 /\_/\   MeawLang by S.A. Roman
( o.o )  [ Байт-ориентированный ]
 > ^ <   [  кошачий эзотерик  ]
```

## Концепция и уникальность
В отличие от других эзотерических языков (например, Brainfuck или MiniStringFuck), где для изменения значения памяти нужно писать один и тот же символ десятки раз подряд, MeawLang использует подход «Одно слово — одна атомарная операция».

Мощность (аргумент n) любой команды регулируется количеством букв "a" внутри кошачьего «слова», а буква "w" всегда выступает в роли маркера завершения конструкции. Код подается исключительно в виде строки команд, разделенных пробелами или переносами строк.

## Технические характеристики
* Память: Язык работает с одним-единственным байтом памяти.
* Диапазон: Значения байта составляют от 0 до 255.
* Переполнение: При достижении значения 256 байт автоматически сбрасывается в 0. Если значение опускается ниже 0, оно переходит в 255.

## Список команд

| Конструкция | Имя функции | Что делает | Пример |
| :--- | :--- | :--- | :--- |
| **`Mi(a*n)w`** | Increment | Добавляет n к значению байта | `Miaw` (+1), `Miaaaaaw` (+5) |
| **`My(a*n)w`** | Decrease | Вычитает n из значения байта | `Myaw` (-1), `Myaaaaw` (-4) |
| **`Me(a*n)w`** | Echo | Выводит текущий символ по ASCII-коду n раз подряд | `Meaw` (1 раз), `Meaaw` (2 раза подряд) |

## Примеры программ

### 1. Hello, World!
Классический пример:
```text
Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaw Meaaw Miaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaw Meaw Miaaaw Meaw Myaaaaaaw Meaw Myaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw
```

### 2. Авторство проекта
Код, выводящий фразу "Conceived by S.A. Roman!":
```text
Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaw Meaw Myaaaaaaw Meaw Miaaaaaaaaw Meaw Miaaaaaaw Meaw Myaaaaaw Meaw Myaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaw Meaw Myaaaaaw Meaw Myaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw
```

## Содержимое репозитория
* `Interpreter.py` — Интерпретатор кода.
* `Compiler.py` — Компилятор обычного текста в код MeawLang.
* `examples/` — Папка с примерами программ (файлы с расширением .meaw).

---
Автор концепции: S.A. Roman, 9 сентября 2026 г. Лицензировано под MIT License.
