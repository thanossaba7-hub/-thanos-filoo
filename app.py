from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def love_counter():
    name1 = "Θάνος"
    name2 = "Φιλομένη"

    met_in_person = datetime(2025, 12, 22, 12, 0)
    relationship_start = datetime(2026, 1, 24, 18, 15)
    now = datetime.now()

    known = now - met_in_person
    together = now - relationship_start

    def breakdown(td):
        days = td.days
        hours = td.seconds // 3600
        minutes = (td.seconds % 3600) // 60
        return days, hours, minutes

    kd, kh, km = breakdown(known)
    td, th, tm = breakdown(together)

    return f"""
    <html>
    <head>
        <title>Θάνος & Φιλομένη 💖</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: Arial; text-align:center; background:#ffe4e1; padding:30px;">
        <h1>💖 {name1} & {name2} 💖</h1>

        <p>⏳ <b>Γνωριζόμαστε:</b><br>
        {kd} μέρες, {kh} ώρες, {km} λεπτά</p>

        <p>💞 <b>Είμαστε μαζί:</b><br>
        {td} μέρες, {th} ώρες, {tm} λεπτά</p>

        <p>💌 Φιλομένη, από τη στιγμή που μπήκες στη ζωή μου,
        νιώθω τέλεια μαζίσου. ❤️</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
