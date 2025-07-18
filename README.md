
# 🧠 LLM Architect CLI – Terminal Chatbot for Software Architecture (powered by LLaMA 3.3)

This project is a command-line interface (CLI) chatbot that simulates an Ubuntu terminal assistant. It uses **Ollama** with **LLaMA 3.3** locally to generate software architecture scaffolding and design using high-level prompts.

---

## 📐 Use Case

Ideal for developers who want to:

- Scaffold projects using **Clean Architecture**, **MVC**, or **Microservices**
- Generate full code modules based on **natural language prompts**
- Run everything **locally** with privacy using **LLaMA 3.3 + Ollama**

---

## 📦 Project Structure

```
llm_architect_cli/
├── cli.py                     # Terminal chatbot with typewriter output
├── ollama_interface.py        # Interface to run prompts via Ollama
├── prompt_templates/
│   └── clean_architecture.txt # Example template for Clean Architecture
├── requirements.txt
└── README.md
```

---

## 🧠 Example Prompt Template: Clean Architecture

```
You're an expert software architect. I want to build a [project_type] in [language] using Clean Architecture.

Please generate:
1. A directory structure with the following layers: Domain, Application, Infrastructure, Interfaces.
2. The entity and service logic for [component] (e.g., User/Auth).
3. REST interface definition using [framework] (e.g., FastAPI/NestJS).
4. Repository interface and test stub.

Use SOLID principles. Return code only.
```

Prompt placeholders:
- `[project_type]`: e.g. e-commerce app
- `[language]`: e.g. Python
- `[component]`: e.g. User

---

## 🚀 How to Deploy

### 🐍 Step 1: Setup Python Environment

```bash
conda create -n architect-cli python=3.10 -y
conda activate architect-cli
pip install -r requirements.txt
```

### 🦙 Step 2: Install Ollama + LLaMA 3.3

```bash
# Download Ollama from: https://ollama.com/download
ollama serve
ollama pull llama3
```

### 💬 Step 3: Run the Chatbot

```bash
python cli.py
```

Type your architectural prompt like:

```
🧠 > Generate a clean architecture for a FastAPI e-commerce backend with PostgreSQL.
```

---

## 🧰 Optional Enhancements

- Add `prompt_templates/mvc.txt`, `microservices.txt`
- Support logging, autocomplete, or multi-turn session
- Wrap into a pip-installable CLI tool

---

## 📜 License

MIT License – Free for personal and commercial use.
