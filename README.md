# 🔧 Infrastructure Automation Demo with Ansible

🚀 This is a mini infrastructure automation project developed by **Kevin Dule** as a practical showcase for the **Infrastructure Automation Engineer** role at **Engineering Albania**.

It automates the provisioning of a web server (Apache) using **Ansible**, with optional triggering via a **Python script**. The project simulates real-world infrastructure tasks and reflects best practices in automation and scripting.

## 📁 Project Structure

```

infra-automation-demo/
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   └── roles/
│       └── apache/
│           ├── tasks/main.yml
│           └── templates/index.html.j2
├── scripts/
│   └── trigger\_playbook.py
└── README.md

```

---

## ⚙️ Technologies Used

- 🔸 **Ansible** (playbooks, roles, templating)
- 🐍 **Python** (automation triggering)
- 🧠 **Jinja2** (dynamic web content)
- 🧾 **Git** (version control, CI/CD-ready)
- ☁️ **WSL/Linux** (local test environment)

---

## 🚀 How to Use

### 📌 Requirements:

- Linux machine or WSL
- Ansible installed (`sudo apt install ansible`)
- Python 3

### ✅ Run manually:

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

### 🐍 Run via Python script:

```bash
python3 scripts/trigger_playbook.py
```

### 🔍 Test locally:

Visit `http://localhost` or run:

```bash
curl http://localhost
```

---

## 📦 What This Project Demonstrates

✔️ **Infrastructure as Code** using Ansible
✔️ **Modular and Reusable Roles**
✔️ **API-Triggerable Automation** with Python
✔️ **Git-based Workflow Ready**
✔️ Prepares the ground for **CI/CD pipelines (GitHub Actions)**

---

## 🔧 CI/CD Integration (Coming Soon)

In the next step, this repo will include:

- ✅ **Ansible Lint** via GitHub Actions
- ✅ Automated Playbook Validation on every push

---

## 🙋‍♂️ About the Author

**Kevin Dule**
📍 Tirana, Albania
🌐 [LinkedIn](https://www.linkedin.com/in/kevindule)
🧠 Passionate about automation, scripting, cloud, and building resilient infrastructure.

---

> 💼 _This repository is part of my technical showcase for the Engineering Albania Infrastructure Automation Engineer position._
