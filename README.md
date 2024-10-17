# resume-filtering
A powerful tool to parse and filter resumes using Natural Language Processing (NLP). It allows HR teams to automatically extract important information from resumes and filter candidates based on key qualifications.



Resume Parsing: Extracts key information such as name, contact details, skills, education, and work experience from resumes.
Resume Filtering: Automatically filters resumes based on predefined criteria like skills, experience, or qualifications.
NLP-powered: Leverages natural language processing techniques to understand and process resumes with high accuracy.
Customizable: Easily add or modify the parsing logic based on your organization’s specific needs.


Before you begin, ensure you have the following installed:

Python 3.x
Pip (Python package installer)
Steps
Clone the repository:

git clone https://github.com/roushanronny/Resume-NLP-Parser.git
cd Resume-NLP-Parser

Install the required dependencies:


pip install -r requirements.txt


To run the resume parser:


python parse_resume.py --input <resume-file> --output <output-file>

python parse_resume.py --input resumes/sample_resume.pdf --output parsed_output.json
This will parse the resume and save the extracted information in a JSON file.

Folder Structure
Here’s an overview of the project structure:



Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m "Added a new feature").
Push to your branch (git push origin feature-branch).
Open a pull request.

