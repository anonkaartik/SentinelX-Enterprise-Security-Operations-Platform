from flask import Flask

from backend.routes.dashboard import dashboard_bp
from backend.routes.ioc import ioc_bp

app=Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

app.register_blueprint(dashboard_bp)
app.register_blueprint(ioc_bp)

if __name__=="__main__":
    app.run(debug=True)