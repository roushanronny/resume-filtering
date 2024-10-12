from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import PyPDF2
import spacy
import collections
import pandas as pd
import warnings

warnings.filterwarnings("ignore")    
nlp = spacy.load("en_core_web_lg")

# Global variables
resume = []
stopwords2 = []
resumeText = ''
resumeWords = ''
stwords = ''

# List of job-related keywords for 'Python Developer'
job_keywords = {
    "Python Developer": ["python", "flask", "django", "sql", "rest", "api", "oop", "pandas", "numpy", "data"]
}

def extractTextFromResume(file_path):
    global resume
    global stopwords2
    global resumeText
    global resumeWords
    global stwords
    
    # Open and read the resume PDF file
    pdfFileObj = open(file_path, 'rb') 
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # Extract text from all pages in the resume
    raw_text = ''
    for page_num in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page_num]
        raw_text += pageObj.extract_text().replace('\n', ' ')

    stwords = set(stopwords.words('english'))

    # Tokenize the resume content into sentences
    resumeText = raw_text
    resumeWords = getWordCount(resumeText, 10, '')  # Get the most frequent words
    
    pdfFileObj.close()
    
    return resumeWords





def getWordCount(lst, nPrint, companyName):
    wordcount = {}
    
    for word in lst.lower().split():
        finalStr = ''.join([c for c in word if c.isalnum()])  # Clean word
        if finalStr not in stwords and finalStr not in stopwords2 and len(finalStr) > 3 and finalStr != companyName:
            if finalStr not in wordcount:
                wordcount[finalStr] = 1
            else:
                wordcount[finalStr] += 1
    
    word_counter = collections.Counter(wordcount)
    lst = word_counter.most_common(len(wordcount))
    #df = pd.DataFrame(lst, columns=['Word', 'Count'])
    #return wordcount
    return lst  # Return the full dictionary of words and their counts


def filterResumeByJobPosition(resume_keywords, job_related_keywords):
    matched_keywords = []
    
    
    # Count how many job-related keywords are present in the resume
    for keyword in resume_keywords:
       
        if keyword[0].lower() in job_related_keywords:
            matched_keywords.append(keyword)
    return matched_keywords


# # Example usage of the functions
# resume_path = './ResumeApi/resume2.pdf'  # Input your resume path here
# resume_keywords = extractTextFromResume(resume_path)

# # Input job position
# job_position = "Python Developer"
# matched_keywords_count = filterResumeByJobPosition(resume_keywords, job_position)

# # Threshold for considering the resume a match
# threshold = 4  # If 4 or more job keywords match, consider the resume a match

# if matched_keywords_count >= threshold:
#     print(f"Resume matches the '{job_position}' position with {matched_keywords_count} relevant keywords!")
# else:
#     print(f"Resume does not match the '{job_position}' position. Only {matched_keywords_count} relevant keywords found.")
