
# 🛡️ Universal Evasion Framework

*A modular cybersecurity research framework that demonstrates polymorphic payload generation, fileless execution, AI-driven evasion, and dynamic C2 communication — designed for ethical use in controlled environments.*

---

## 🧠 Project Overview

The **Universal Evasion Framework** showcases how modern adversarial techniques can bypass static detection using:

- 🔄 **Polymorphic Payload Generation**
- 🧠 **AI-based Code Obfuscation**
- 🧬 **In-memory Execution (Fileless)**
- 🌐 **Simulated C2 Communication**
- ✅ **Test Suite for Validation**

> ⚠️ This project is created for **educational and research purposes only**, especially for those exploring **EDR/AV evasion** techniques in **ethical hacking** and **red teaming** labs.

---

## 🧩 Module Breakdown

| Module                             | Description                                                        |
|------------------------------------|--------------------------------------------------------------------|
| `payload_generator/generator.py`   | Generates randomized Python payloads with unique signatures        |
| `payload_generator/payload.py`     | Resulting payload: basic "print" with randomized string            |
| `memory_loader/loader.py`          | Loads and executes payload directly from memory (fileless-style)   |
| `ai_evasion/adaptive_ai.py`        | Obfuscates payload using simple AI-driven transformation           |
| `payload_generator/payload_ai.py`  | Obfuscated payload generated from `adaptive_ai.py`                 |
| `c2_manager/c2.py`                 | Simulates a basic C2 (Command & Control) connection using sockets  |
| `evaluation_suite/tester.py`       | (Optional) Placeholder for automated detection bypass testing      |
| `tests/`                           | Add your test scripts here                                         |

---

## 🚀 How to Run

> **Requirements**: Python 3.x, netcat (`nc`), Linux environment

````
### 🔹 1. Generate a Polymorphic Payload
```bash
python3 payload_generator/generator.py
````

### 🔹 2. Run the Payload Normally

```bash
python3 payload_generator/payload.py
```

### 🔹 3. Run the Payload In-Memory (Fileless)

```bash
python3 memory_loader/loader.py
```

### 🔹 4. AI-Driven Payload Mutation

```bash
python3 ai_evasion/adaptive_ai.py
python3 payload_generator/payload_ai.py
```

### 🔹 5. Simulated C2 Communication

**Start Listener (Attacker side):**

```bash
nc -lvnp 4444
```

**Connect from Client (Payload side):**

```bash
python3 c2_manager/c2.py
```

---

## 📁 Project Structure

```
universal-evasion-framework/
├── ai_evasion/
│   └── adaptive_ai.py
├── c2_manager/
│   └── c2.py
├── docs/
├── evaluation_suite/
│   └── tester.py
├── memory_loader/
│   └── loader.py
├── payload_generator/
│   ├── generator.py
│   ├── payload.py
│   └── payload_ai.py
├── tests/
└── README.md
```

---

## ⚠️ Disclaimer

This project is **strictly for educational and ethical research purposes only**.

* 🚫 Do **not** use this framework on unauthorized systems or networks.
* 👨‍💻 The developer is **not responsible** for any misuse, damage, or legal consequences.

> By using this project, you agree to use it **only in controlled environments** for **ethical purposes**.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project may be licensed under a custom license depending on distribution.
Please check with the developer or maintainer before public use or redistribution.


