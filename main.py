from flask import Flask

app = Flask(__name__)
courseName = "Python Website"
tutor = "Halippudin"


@app.route("/")  # https://localhost:5000
def Hello():
    return f"Hiiii!!!! I'm currently learning {courseName} avec mon tuteur {tutor} :3"


if __name__ == "__main__":
    app.run()
