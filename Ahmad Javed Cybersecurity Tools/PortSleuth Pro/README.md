# PortSleuth Pro



**A Python-based Advanced Multi‑Threaded Network Port Scanner with Professional Report Generation**


# Key Features

## Multi‑Threaded Port Scanning

Fast scanning using **parallel threads** to significantly reduce scan time.

* Configurable thread count
* Adjustable connection timeout
* Scan large port ranges efficiently

---

## Service Detection

Automatically detects common services based on port numbers.

Examples:

* SSH
* HTTP / HTTPS
* FTP
* SMTP
* MySQL
* PostgreSQL

---

## Banner Grabbing

Attempts to retrieve service banners from open ports to identify:

* Web servers
* Mail servers
* SSH versions
* Database services

---

## Risk Assessment

Each detected service is automatically classified into:

| Risk Level | Description                             |
| ---------- | --------------------------------------- |
| HIGH       | Potentially dangerous exposed services  |
| MEDIUM     | Common services that require monitoring |
| LOW        | Low‑risk open ports                     |

---

## Multiple Report Formats

PortSleuth Pro generates **professional reports** in several formats:

* TXT
* JSON
* CSV
* HTML
* PDF

Reports include:

* Target information
* Scan timestamp
* Port results
* Service identification
* Risk classification
* Service banners

---

## Command Line Interface (CLI)

The tool provides a **clean CLI interface** for flexible scanning operations.

You can control:

* Port range
* Thread count
* Timeout
* Report format

---

## Organized Output

All generated reports are automatically saved in:

```
reports/
```

Each report includes a **timestamp** for easy tracking.

---

# Installation

## Prerequisites

Before installing, ensure you have:

* Python **3.8 or higher**
* pip package manager
* Internet connection (for scanning external hosts)

---

## Setup

Clone the repository:

```
git clone https://github.com/yourusername/PortSleuth-Pro.git
cd PortSleuth-Pro
```

Create a virtual environment (recommended):

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

### Linux / macOS

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Dependencies

PortSleuth Pro uses the following Python libraries:

| Library   | Purpose                 |
| --------- | ----------------------- |
| colorama  | Colored terminal output |
| reportlab | PDF report generation   |
| jinja2    | HTML report templating  |
| tqdm      | Progress bars           |
| tabulate  | Table formatting        |

---

# Usage

## Basic Scan

Scan common ports on a target:

```
python -m src.core_scanner scanme.nmap.org
```

---

## Scan Specific Port Range

```
python -m src.core_scanner scanme.nmap.org -s 20 -e 1000
```

Options:

| Flag | Description |
| ---- | ----------- |
| -s   | Start port  |
| -e   | End port    |

---

## Generate Reports

Generate **HTML report**:

```
python -m src.core_scanner scanme.nmap.org --report html
```

Generate **PDF report**:

```
python -m src.core_scanner scanme.nmap.org --report pdf
```

Generate **all report formats**:

```
python -m src.core_scanner scanme.nmap.org --report all
```

---

## Advanced Scan Example

```
python -m src.core_scanner scanme.nmap.org -s 1 -e 2000 -t 200 -T 0.5 --report html
```

Options:

| Flag     | Description            |
| -------- | ---------------------- |
| -t       | Number of threads      |
| -T       | Timeout per connection |
| --report | Report format          |

---

# Testing the Tool

You can safely test the scanner using:

### Localhost

```
python -m src.core_scanner 127.0.0.1
```

### Nmap Test Server

```
python -m src.core_scanner scanme.nmap.org
```

This server is **designed for security testing**.

---

# Example Output

Terminal Output Example:

```
TARGET: scanme.nmap.org
PORT RANGE: 1-1024
THREADS: 100

[OPEN] Port 22 : ssh
[OPEN] Port 80 : http

SCAN COMPLETED
Duration: 2.4 seconds
Open Ports Found: 2
```

---

# Example TXT Report

```
PORTSLEUTH PRO - NETWORK PORT SCAN REPORT

Target: scanme.nmap.org
Date: 2026-03-13
Duration: 2.41 seconds

PORT     SERVICE     RISK
22       SSH         MEDIUM
80       HTTP        MEDIUM
```

Reports are saved automatically inside:

```
reports/
```

Example file:

```
reports/scan_45_33_32_156_20260313.html
```

---

# Project Structure

```
PortSleuth-Pro/
│
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── core_scanner.py
│   ├── report_generator.py
│   └── utils.py
│
├── docs/
│   └── usage.md
│
├── examples/
│   └── example_scan.py
│
├── tests/
│   └── test_basic.py
│
└── reports/
```

---

# Security & Ethical Use

⚠️ **Important**

PortSleuth Pro is intended **only for authorized security testing and educational purposes.**

Do **NOT** scan:

* random websites
* networks without permission
* private infrastructure

Always obtain **explicit permission** before scanning any system.

---

# Future Improvements

Planned features for future versions:

* UDP Port Scanning
* Nmap Integration
* OS Detection
* Network Discovery
* Vulnerability Scanning
* Interactive HTML Dashboard
* GUI Interface
* Docker Deployment

---

# Author

Developed by **AJ**

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

⭐ **If you found this project useful, consider starring the repository!**
