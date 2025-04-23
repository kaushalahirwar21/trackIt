# trackIt

# 📊 TrackIt

**TrackIt** एक वेब-आधारित एप्लिकेशन है जिसे Python Flask, MySQL, HTML, CSS, और JavaScript की मदद से बनाया गया है। यह ऐप यूज़र डेटा को इनपुट, ट्रैक और मैनेज करने की सुविधा देता है। साथ ही CSV फाइलों के ज़रिए डेटा को export/import भी किया जा सकता है।

---

## 🚀 Features

- 🔐 User session management
- 🗂 CSV export / import support
- 🗓 Date & time logging using `datetime`
- 📄 Templated frontend with HTML & Jinja
- ⚡ Connected to MySQL database
- 🔁 Data submission via forms

---

## ⚙️ Technologies Used

- **Python** (Flask 2.2.5)
- **MySQL** (`mysql-connector-python 8.0.33`)
- **HTML/CSS/JavaScript**
- **CSV module** for file handling
- **Jinja2** templating
- **Sessions** for login/user flow

---

## 🧑‍💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaushalahirwar21/trackit.git
   cd trackit
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your MySQL database**
   - Create a database and tables as per your app schema.
   - Update the database connection details in your Flask config or `.env` file.

5. **Run the app**
   ```bash
   flask run
   ```

6. **Visit**
   ```
   http://localhost:5000
   ```

---

## 📦 Requirements

```
Flask==2.2.5  
mysql-connector-python==8.0.33
```

---

## 📁 File Structure (optional)

```
/trackit
├── static/               # CSS, JS, images
├── templates/            # HTML (Jinja2 templates)
├── app.py                # Main Flask application
├── requirements.txt      
└── README.md
```

---

## 📄 License

Licensed under the **MIT License**.

---

## 👤 Author

**Kaushal Ahirwar**  
GitHub: [@kaushalahirwar21](https://github.com/kaushalahirwar21)

---

> 💬 Feel free to open issues or pull requests for suggestions and improvements!
