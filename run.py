from flask import Flask

from backend.routes.dashboard import dashboard_bp

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)