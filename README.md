# 🚰 Hostel Smart Water Management System

A web-based dashboard and simulation tool for monitoring and optimizing hostel water usage using smart analytics.

---

## 📌 Overview

This project combines:
- A **Flask backend** that runs a real-time water usage simulation.
- A **SimPy** discrete-event simulation for realistic tank behavior, leakage, greywater reuse, and refilling.
- A **responsive dashboard** with Chart.js to visualize usage, tank levels, leaks, overflow risk, and more.

---

## ✅ Features

- 📈 **Real-time water usage simulation** for each hour of the day.
- 🕒 **Peak hour logic** for realistic usage patterns.
- 💧 **Leakage detection** and risk alerting.
- ⚠️ **Overflow risk detection**.
- 🔁 **Greywater reuse tracking**.
- 📊 **Interactive charts** for consumption and tank level.
- 🗂️ **Event log** for clear hourly status.
- 🚨 **Visual alerts** for leaks & risks.

---

## ⚙️ Tech Stack

| Tech | Purpose |
|------|---------|
| **Python (Flask)** | Web server |
| **SimPy** | Discrete event simulation |
| **HTML/CSS/JavaScript** | Dashboard frontend |
| **Chart.js** | Interactive charts |
| **Bootstrap (optional)** | UI styling framework |

---

## 📂 Project Structure

hostel-smart-water-management/
├── app.py # Flask backend
├── simulation.py # SimPy simulation logic (or merge inside app.py)
├── templates/
│ └── index.html # Dashboard UI
├── static/
│ └── water.jpg # Background image
├── requirements.txt # Python dependencies
├── README.md # Project documentation


## 🚀 How to Run

Follow these steps to set up and run the project on your local machine.

---

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MahimaSinghRathore/water_management_system.git
cd hostel-smart-water-management
