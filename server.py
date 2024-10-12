from flask import Flask,render_template,request
from uuid6 import uuid6
import os
from ResumeApi.ResumeMatcher import extractTextFromResume,filterResumeByJobPosition
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = ".\\static\\input_resume"
# Allowed file extensions (PDF)
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/filter-resume")
def resultPage():
    return render_template("result.html")

@app.route("/filter-resume",methods=["POST"])
def filterReume():
    shortlisted_resume = []
    files = request.files.getlist("files")
    job_keywords = request.form.get('job_keywords')
    job_keywords = [x.lstrip().rstrip().lower() for x in job_keywords.split(",")]
    if len(job_keywords) == 0:
        return "Please enter Some Keywords related to the job position"
    if len(files) == 0:
        return "No file selected"
    for file in files:
        if file and allowed_file(file.filename):
            
            filename = uuid6().hex+"."+file.filename.rsplit('.', 1)[1].lower()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # # Process the uploaded resume
            resume_keywords = extractTextFromResume(file_path)
            #print(filename,resume_keywords)
            print()
            #keywords = ["python", "flask", "django", "sql", "rest", "api", "oop", "pandas", "numpy", "data"]
            keywords = job_keywords

            # # Filter the resume based on the job position
            matched_keywords = filterResumeByJobPosition(resume_keywords, keywords)
            print(matched_keywords)
            threshold = 4*len(matched_keywords)-1
            score = 0
            for x in matched_keywords:
                score = score + x[1]

            if score >= threshold:
                shortlisted_resume.append({"filename":filename,"path":file_path,"score":score,"match_keyword":matched_keywords})

            
            
            # if len(matched_keywords) >= threshold:
            #     return f"Resume matches the  keywors with relevant keywords!"
            # else:
            #     return f"Resume does not match"
    
    print(shortlisted_resume)
    return render_template("result.html",data=shortlisted_resume,total_resume = len(files))




app.run(debug=True)