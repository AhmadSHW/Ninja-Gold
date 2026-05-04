# Ninja Gold - Flask Web Application

A fun, interactive mini-game built with the **Flask** framework. The goal is to guide your ninja through various locations to gather gold, manage a real-time activity log, and try to reach a winning gold target!

## 🎮 Game Features

* **Multiple Locations:** Earn different amounts of gold by visiting the Farm, Cave, House, or the risky Casino.
* **Real-time Activity Log:** Tracks every move with a timestamp and color-coded messages (Green for gains, Red for losses).
* **Session Management:** Uses Flask Session to persist gold balance and activity history across requests.
* **Winning Parameters:** Challenges the user to reach a specific gold target within a limited number of moves.
* **Responsive Design:** A clean, CSS-flexbox based layout inspired by the classic Ninja Gold wireframe.

## 🚀 Technical Highlights

* **Backend:** Python 3.12+ with Flask.
* **Frontend:** HTML5, CSS3 (Flexbox), and Jinja2 Templating.
* **Logic Optimization:** Implemented location-based rewards using dictionary mapping to avoid redundant conditional statements (Sensei Bonus).
* **Data Handling:** Efficient use of `session` to store and update game state without a database.

## 🛠️ Concepts Applied

* Handling **POST** requests and form data.
* Server-side redirects and URL routing.
* Dynamic HTML rendering using the `|safe` filter and Jinja loops.
* Logic implementation with the Python `random` and `datetime` modules.

## 📝 Author
**Ahmed** - Junior Full Stack Developer in training.