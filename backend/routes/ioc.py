from flask import Blueprint,jsonify

from modules.ioc_extractor.ioc_engine import generate_ioc_report

ioc_bp=Blueprint("ioc",__name__)

@ioc_bp.route("/api/iocs")
def iocs():

    return jsonify(generate_ioc_report())