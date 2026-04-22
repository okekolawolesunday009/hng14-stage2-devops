import redis
import time

print("Worker starting...")

# Retry connection
while True:
    try:
        r = redis.Redis(host="redis", port=6379)
        r.ping()
        print("Connected to Redis")
        break
    except Exception as e:
        print("Waiting for Redis...", e)
        time.sleep(2)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")

while True:
    print("Waiting for job...")
    job = r.brpop("job", timeout=5)
    if job:
        _, job_id = job
        process_job(job_id.decode())