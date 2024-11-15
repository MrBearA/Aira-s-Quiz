from flask import Flask, request, render_template, jsonify
import joblib  # Use joblib to load the model
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')  # Ensure model.pkl exists and is compatible with joblib

# Define job profiles with related skills
job_profiles = {
    "Software Developer": ["programming", "logic", "problem-solving"],
    "Web Developer": ["design", "programming", "user-experience"],
    "Mobile Developer": ["mobile", "programming", "platforms"],
    "Data Analyst": ["data-analysis", "statistics", "problem-solving"],
    "Data Scientist": ["data-analysis", "machine-learning", "statistics"],
    "System Administrator": ["networking", "security", "system-management"],
    "Network Engineer": ["networking", "security", "hardware"],
    "Cybersecurity Analyst": ["security", "analysis", "threat-detection"],
    "Database Administrator": ["databases", "management", "sql"],
    "Cloud Architect": ["cloud", "system-design", "security"],
    "DevOps Engineer": ["automation", "cloud", "programming"],
    "IT Project Manager": ["management", "communication", "organization"],
    "UX/UI Designer": ["design", "user-experience", "creativity"],
    "Machine Learning Engineer": ["machine-learning", "ai", "programming"],
    "Artificial Intelligence Engineer": ["ai", "machine-learning", "logic"],
    "Technical Writer": ["writing", "documentation", "communication"],
}

@app.route('/quiz', methods=['GET'])
def quiz():
    job = request.args.get('job', 'Unknown Job')
    return render_template('quiz.html', job=job)

@app.route('/api/quiz', methods=['POST'])
def process_quiz():
    quiz_data = request.json
    job_interest = quiz_data.pop('job-interest', 'Unknown').title()  # User-selected job
    
    # Prepare features based on quiz_data
    try:
        # Map the quiz responses to binary features for the selected job's skills
        job_skills = job_profiles.get(job_interest, [])
        features = np.array([[1 if skill in quiz_data.values() else 0 for skill in job_skills]]).astype(int)
        
        # Predict the job
        predicted_job = model.predict(features)[0]
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": "Prediction failed"}), 500

    # Check for a match and recommend alternative jobs if needed
    match_result = (predicted_job == job_interest)
    recommended_jobs = []

    if not match_result:
        # Recommend jobs based on skill overlap
        recommended_jobs = [
            job for job, skills in job_profiles.items()
            if any(skill in quiz_data.values() for skill in skills) and job != predicted_job
        ]

    return jsonify({
        "matchResult": match_result,
        "predictedJob": predicted_job,
        "recommendedJobs": recommended_jobs
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
