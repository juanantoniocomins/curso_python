# ⚙️ Operadores en Python

Python cuenta con varios tipos de operadores que permiten realizar operaciones aritméticas, lógicas, de comparación y más.  
A continuación se listan todos los operadores clasificados por tipo.

---

## ➕ Operadores Aritméticos

| Operador | Descripción | Ejemplo | Resultado |
|-----------|--------------|----------|------------|
| `+` | Suma | `5 + 2` | `7` |
| `-` | Resta | `5 - 2` | `3` |
| `*` | Multiplicación | `5 * 2` | `10` |
| `/` | División (float) | `5 / 2` | `2.5` |
| `//` | División entera | `5 // 2` | `2` |
| `%` | Módulo (resto) | `5 % 2` | `1` |
| `**` | Exponente | `5 ** 2` | `25` |

---

## ⚖️ Operadores de Comparación

| Operador | Descripción | Ejemplo | Resultado |
|-----------|--------------|----------|------------|
| `==` | Igualdad | `5 == 5` | `True` |
| `!=` | Desigualdad | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `3 < 5` | `True` |
| `>=` | Mayor o igual que | `5 >= 5` | `True` |
| `<=` | Menor o igual que | `3 <= 5` | `True` |

---

## 🔄 Operadores de Asignación

| Operador | Descripción | Ejemplo | Equivale a |
|-----------|--------------|----------|-------------|
| `=` | Asignación | `x = 5` | — |
| `+=` | Suma y asigna | `x += 3` | `x = x + 3` |
| `-=` | Resta y asigna | `x -= 3` | `x = x - 3` |
| `*=` | Multiplica y asigna | `x *= 3` | `x = x * 3` |
| `/=` | Divide y asigna | `x /= 3` | `x = x / 3` |
| `//=` | División entera y asigna | `x //= 3` | `x = x // 3` |
| `%=` | Módulo y asigna | `x %= 3` | `x = x % 3` |
| `**=` | Exponente y asigna | `x **= 3` | `x = x ** 3` |

---

## 🧠 Operadores Lógicos

| Operador | Descripción | Ejemplo | Resultado |
|-----------|--------------|----------|------------|
| `and` | Verdadero si ambos son verdaderos | `True and False` | `False` |
| `or` | Verdadero si al menos uno es verdadero | `True or False` | `True` |
| `not` | Invierte el valor lógico | `not True` | `False` |

---

## 🧩 Operadores de Identidad

| Operador | Descripción | Ejemplo | Resultado |
|-----------|--------------|----------|------------|
| `is` | Verdadero si ambos son el mismo objeto | `a is b` | `True` o `False` |
| `is not` | Verdadero si **no** son el mismo objeto | `a is not b` | `True` o `False` |

---

## 📦 Operadores de Pertenencia

| Operador | Descripción | Ejemplo | Resultado |
|-----------|--------------|----------|------------|
| `in` | Verdadero si el valor está en la secuencia | `'a' in 'hola'` | `True` |
| `not in` | Verdadero si el valor **no** está en la secuencia | `'z' not in 'hola'` | `True` |

---

## ⚙️ Operadores Bit a Bit (Bitwise)

| Operador | Descripción | Ejemplo | Resultado (en binario) |
|-----------|--------------|----------|------------------------|
| `&` | AND bit a bit | `5 & 3` | `0b1` |
| `|` | OR bit a bit | `5 \| 3` | `0b111` |
| `^` | XOR bit a bit | `5 ^ 3` | `0b110` |
| `~` | NOT bit a bit (inversión) | `~5` | `-6` |
| `<<` | Desplaza bits a la izquierda | `5 << 1` | `10` |
| `>>` | Desplaza bits a la derecha | `5 >> 1` | `2` |

---

## 🧮 Prioridad de Operadores (de mayor a menor)

| Prioridad | Operadores |
|------------|-------------|
| 1️⃣ | `()` Paréntesis |
| 2️⃣ | `**` |
| 3️⃣ | `+x`, `-x`, `~x` |
| 4️⃣ | `*`, `/`, `//`, `%` |
| 5️⃣ | `+`, `-` |
| 6️⃣ | `<<`, `>>` |
| 7️⃣ | `&` |
| 8️⃣ | `^` |
| 9️⃣ | `|` |
| 🔟 | Comparación (`==`, `<`, `>`, `<=`, `>=`, `!=`, `is`, `in`, etc.) |
| 11️⃣ | `not` |
| 12️⃣ | `and` |
| 13️⃣ | `or` |

---

📘 **Nota:** Python evalúa las expresiones de izquierda a derecha respetando esta jerarquía, a menos que se utilicen paréntesis para alterar el orden.

---

