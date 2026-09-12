# MeawLang

**MeawLang** is a minimalist, scalable, byte-oriented esoteric programming language with a feline-inspired syntax. It is heavily inspired by classic esolangs like MiniStringFuck and Chicken, utilizing unary numeral system concepts for handling arguments.

```text
 /\_/\   
( o.o ) 
 > ^ <  
```

## Concept and Uniqueness
Unlike other esoteric languages (e.g., Brainfuck or MiniStringFuck) where modifying memory values requires writing the same character dozens of times consecutively, MeawLang introduces a "One word — one atomic operation" approach.

The magnitude (argument n) of any command is controlled by the number of "a" letters inside the feline "word", while the letter "w" always acts as the end-of-instruction marker. The source code is parsed exclusively as a sequence of whitespace-separated or newline-separated string commands.

## Technical Specification
* **Memory:** The language operates on a single byte of memory.
* **Range:** The byte value ranges from 0 to 255.
* **Overflow:** Reaching a value of 256 automatically wraps around to 0. Dropping below 0 wraps around to 255.

## Instruction Set

| Syntax | Instruction | Description | Example |
| :--- | :--- | :--- | :--- |
| **`Mi(a*n)w`** | Increment | Adds n to the current byte value | `Miaw` (+1), `Miaaaaaw` (+5) |
| **`My(a*n)w`** | Decrease | Subtracts n from the current byte value | `Myaw` (-1), `Myaaaaw` (-4) |
| **`Me(a*n)w`** | Echo | Outputs the current ASCII character n times | `Meaw` (once), `Meaaw` (twice consecutively) |

## Code Examples

### 1. Hello, World!
A classic example:
```text
Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaw Meaaw Miaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaw Meaw Miaaaw Meaw Myaaaaaaw Meaw Myaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw
```

### 2. Project Authorship
Code that outputs the phrase "Conceived by S.A. Roman!":
```text
Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaw Meaw Myaaaaaaw Meaw Miaaaaaaaaw Meaw Miaaaaaaw Meaw Myaaaaaw Meaw Myaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Miaaaaaaaaaaaaaaaw Meaw Myaaaaaw Meaw Myaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw Myaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaw Meaw
```

## Repository Structure
* `Interpreter.py` — The code interpreter.
* `Compiler.py` — An text-to-MeawLang compiler.
* `examples/` — A directory containing sample programs (with the .meaw extension).

---
Concept created by: S.A. Roman, September 9, 2026.
