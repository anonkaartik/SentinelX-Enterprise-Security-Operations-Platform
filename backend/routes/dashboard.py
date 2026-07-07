from flask import Blueprint,jsonify,render_template

from backend.services.dashboard_service import get_dashboard_data

dashboard_bp=Blueprint("dashboard",__name__)

@dashboard_bp.route("/")
def dashboard():

    return render_template("dashboard.html")

@dashboard_bp.route("/api/dashboard")
def dashboard_api():

    return jsonify(get_dashboard_data())