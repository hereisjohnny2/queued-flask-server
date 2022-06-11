from flask import current_app
from rq import Connection, Queue
import redis
from app.background import service


def list_jobs():
    with create_connection():
        q = Queue()

    return {
        "status": "successful",
        "jobs_count": len(q)
    }


def create_job(expression: str):
    with create_connection():
        q = Queue()
        job = q.enqueue(service.run, expression)

    return {
        "status": "successful",
        "job_count": len(q),
        "job": {
            "id": job.get_id(),
        }
    }
    

def get_job(job_id: str):
    with create_connection():
        q = Queue()
        job = q.fetch_job(job_id)
    
    if not job:
        return { 
            "status": "error",
            "msg": "no job found with such id"
        }
    
    return {
        "status": "successful",
        "job": {
            "id": job.get_id(),
            "status": job.get_status(),
            "result": job.result
        }
    }
    
    
def create_connection():
    redis_url = current_app.config["REDIS_URL"]
    return Connection(redis.from_url(redis_url))