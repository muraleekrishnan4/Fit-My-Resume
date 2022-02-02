# Fit-My-Resume
Fit My Resume is job description keyword extractor that find apt keywords using NLP (Natural Language Processing) and most frequent words from the given job description. You can include these keywords in your resume to get good score for ATS (Application Tracking Systems).

**How Application Tracking System works** <br>
Creating an ATS-friendly resume is an effective method for increasing your interview chances. Your resume will reach a recruiter if it passes through an Application Tracking System. ATS mainly works on job-specific keywords.

**How Fit-My-Resume will help you** <br>
You should Copy and Paste the Job description of your desired job in our site and submit. After processing the data, we will provide you with a list of best keywords. Pick the suitable keywords and add them to your resume. Your resume will get high ATS score which increases the chance of passing the ATS and making sure it reaches your recruiter.

**Most frequent keywords**: Keywords from unsupervised automatic keyword extraction method. It provides you the most important keywords from the Job Description.<br>
**Most frequent words**: Finds the specific words that the Job Description keeps repeating.

<br>

Site: https://fit-my-resume.herokuapp.com/

<br>

# For Developers

Languages used: 
  1. Python (Flask)
  2. HTML
  3. CSS

Deployment:
  1. Heroku

How this works: <br>
The tool will extract the keywords in two different ways and provides the result.<br>
  1) First way is using YAKE (Yet Another Keyword Extractor) [Read more:  https://github.com/LIAAD/yake ] 
  2) Second way is to split the whole string into separate words after cleaning the data and showing the most frequent words.
