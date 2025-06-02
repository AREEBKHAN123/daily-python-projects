# 🌡️ Temperature Controller — Python If-Else Logic

A beginner-level Python script that simulates basic **automation logic** based on the current temperature (Celsius). Depending on the temperature value, it decides whether to turn on a **heater**, do nothing, or turn on the **AC**.

---

## 🚀 What It Does

- Takes the **current temperature** as user input.
- Uses `if-elif` statements to determine the environment status:
  - ❄️ **20°C or below** → `"Turn on heater!"`
  - 🌤️ **Between 21°C and 25°C** → `"It's Normal!"`
  - 🔥 **Above 26°C** → `"Turn on the AC!"`

---

## 🧾 Sample Output

```bash
Enter Current Temperature (Celsius): 17
------Turn on heater!-------

Enter Current Temperature (Celsius): 23
------Its Normal!-------

Enter Current Temperature (Celsius): 29
--------Turn on the AC!!----------
