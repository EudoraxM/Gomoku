# 🎮 Pět v řadě – Python konzolová hra

Jednoduchá konzolová hra napsaná v jazyce **Python**, ve které se dva hráči střídají na hrací ploše a snaží se umístit **pět svých symbolů v řadě** – horizontálně, vertikálně nebo diagonálně.

---

## 🧠 Popis hry
Každý hráč střídavě zadává souřadnice **X a Y**, kam chce umístit svůj symbol:
- Hráč **X** má „křížky“
- Hráč **O** má „kolečko“

Cílem hry je **umístit pět svých symbolů vedle sebe** v libovolném směru.  
Jakmile se to podaří, hra skončí a zobrazí vítěze.

---

## 🚀 Funkce programu

| Funkce | Popis |
|---------|--------|
| `vytvor_pole(velikost)` | Vytvoří hrací plochu (2D seznam) z prázdných políček |
| `vykresli_hraci_plochu(hraci_plocha)` | Vykreslí hrací pole do konzole v přehledné mřížce |
| `tah_hrace(hraci_plocha, hrac)` | Umožní hráči zadat souřadnice tahu, ověří platnost pozice |
| `kontrola_vyhry(hraci_plocha)` | Kontroluje, zda má někdo 5 symbolů v řadě (řádek, sloupec, diagonála) |

---

## 💻 Jak hru spustit

1. Ujisti se, že máš nainstalovaný **Python 3.10+**  
   [Stáhni z python.org](https://www.python.org/downloads/)

2. Ulož tento skript do souboru, např.:

3. Spusť hru v terminálu nebo v IDE:
```bash
python piskvorky.py