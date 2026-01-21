from flask import Flask, render_template
from services.user_service.routes import user_bp
from services.repo_service.routes import repo_bp

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

app.register_blueprint(user_bp)
app.register_blueprint(repo_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
