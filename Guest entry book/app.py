from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store guestbook entries (won't survive server restart tho)
entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if name and message:
            with open("guestbook.txt", "a") as f:
                f.write(f"{name}|{message}\n")
            return redirect(url_for("entries_page"))
    return render_template("index.html")

@app.route("/entries")
def entries_page():
    entries = []
    try:
        with open("guestbook.txt", "r") as f:
            for line in f:
                name, message = line.strip().split("|")
                entries.append({"name": name, "message": message})
    except FileNotFoundError:
        pass
    return render_template("entries.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
