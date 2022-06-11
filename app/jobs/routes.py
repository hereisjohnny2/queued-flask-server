from flask import Blueprint, jsonify, request
from app.jobs import service


jobs_blueprint = Blueprint("jobs", __name__)

@jobs_blueprint.route("")
def list_jobs():
    response = service.list_jobs()   
    return jsonify(response)

@jobs_blueprint.route("", methods=["POST"])
def create_job():
    data = request.get_json()
    
    if "expression" not in data:
        return jsonify({ "msg": "Missing 'expression' param" })

    expression = data["expression"]
    response = service.create_job(expression)     
    
    return response

@jobs_blueprint.route("<job_id>", methods=["GET"])
def get_job_status(job_id):
    response = service.get_job(job_id)
    return jsonify(response)
    
    
        