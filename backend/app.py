import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Identitas injected dari Kubernetes environment variables
user_name = os.getenv('USER_NAME', 'Nama Default')
user_nim  = os.getenv('USER_NIM',  'NIM Default')

# Data Job Listings
jobs = [
    {
        "id": 1,
        "title": "Backend Engineer",
        "company": "Gojek",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "salary": "Rp 15.000.000 - 25.000.000",
        "tags": ["Python", "Go", "Kubernetes"],
        "posted": "2 days ago"
    },
    {
        "id": 2,
        "title": "Frontend Developer",
        "company": "Tokopedia",
        "location": "Remote",
        "type": "Full-time",
        "salary": "Rp 12.000.000 - 20.000.000",
        "tags": ["React", "TypeScript", "Next.js"],
        "posted": "5 days ago"
    },
    {
        "id": 3,
        "title": "DevOps Engineer",
        "company": "Traveloka",
        "location": "Bandung, Indonesia",
        "type": "Full-time",
        "salary": "Rp 18.000.000 - 30.000.000",
        "tags": ["Docker", "Kubernetes", "Azure"],
        "posted": "1 week ago"
    },
    {
        "id": 4,
        "title": "Data Scientist",
        "company": "Shopee",
        "location": "Remote",
        "type": "Contract",
        "salary": "Rp 20.000.000 - 35.000.000",
        "tags": ["Python", "TensorFlow", "SQL"],
        "posted": "3 days ago"
    },
    {
        "id": 5,
        "title": "Cloud Architect",
        "company": "Blibli",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "salary": "Rp 25.000.000 - 45.000.000",
        "tags": ["Azure", "GCP", "Terraform"],
        "posted": "Just now"
    },
    {
        "id": 6,
        "title": "Mobile Developer (Android)",
        "company": "OVO",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "salary": "Rp 14.000.000 - 22.000.000",
        "tags": ["Kotlin", "Android", "Jetpack"],
        "posted": "4 days ago"
    }
]


@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({
        "app": "JobBoard App",
        "developer": user_name,
        "nim": user_nim,
        "total_jobs": len(jobs)
    })


@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    job_type = request.args.get('type')
    if job_type:
        filtered = [j for j in jobs if j['type'].lower() == job_type.lower()]
        return jsonify(filtered)
    return jsonify(jobs)


@app.route('/api/jobs', methods=['POST'])
def add_job():
    data = request.json
    required = ['title', 'company', 'location', 'type', 'salary', 'tags']
    if not all(k in data for k in required):
        return jsonify({"error": "Data tidak lengkap"}), 400

    new_job = {
        "id": len(jobs) + 1,
        "title": data['title'],
        "company": data['company'],
        "location": data['location'],
        "type": data['type'],
        "salary": data['salary'],
        "tags": data['tags'],
        "posted": "Just now"
    }
    jobs.append(new_job)
    return jsonify(new_job), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)