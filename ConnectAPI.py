import ollama
from datetime import datetime
import json
import re


def extract_json_from_text(text):
    try  :
        match = re.search(r'```json\n(.*?)\n```', text, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                job_data = json.loads(json_str)
                return job_data
            except json.JSONDecodeError:
                print("Error: Extracted JSON is not valid.")
                return None
        else:
            print("Error: No JSON found in the text.")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def openai(data):
    try :
        desire_model = 'deepseek-r1:1.5b' 
        response = ollama.chat(model=desire_model, messages=[
        {
            "role": "user",
            "content": f"""
            Your task is to deeply analyze his skills and experience to generate a job description.
            Example:
            Company name: {data['company']}  
            Location: {data['location']}  
            Job Title: {data['job-title']}
            Job Type: {data['job-type']}
            Post on: {datetime.now()}
            Experience: {data['experience']} years
            Skills: {data['skills']}  
            Education Requirement: {data['education']} 

            The job description should include:
            - **Company name**: Company Name.
            - **Location**: Location.
            - **Post on**:The posted date should be today's date in the format dd/mm/yyyy.
            - **Experience**: Experience years
            - **Type**: Type of the Job
            - **Job Title**: A suitable title for the job.
            - **Job Summary**: A brief overview of the role.
            - **Key Responsibilities**: A list of main duties and tasks.
            - **Required Skills & Qualifications**: Deeply analyze the skills and experience to generate a list of required skills and qualifications.

            **Response Format:**
            The response must be in JSON format only. Ensure that:
            1. "Key Responsibilities" and "Required Skills & Qualifications" are in list format.
            2. The response is structured correctly in JSON format.
            3. The language used is English.

            **Expected JSON Response Format:**
            ```json
            {{
                "Company name": "Zeb",
                "Location": "Chennai,Coimbatore",
                "Experience": "5",
                "Type": "Full Time",
                "Post on": "12/12/2022",
                "Job Title": "AI Software Engineer",
                "Job Summary": "We are looking for an experienced AI Software Engineer to design, develop, and deploy AI-powered applications. The ideal candidate will have expertise in Python, JavaScript, React, cloud platforms (AWS, Azure), and full-stack development.",
                "Key Responsibilities": [
                    "Design and develop AI-powered applications using Python and JavaScript.",
                    "Implement and optimize RAG-based solutions for efficient information retrieval.",
                    "Develop and maintain full-stack applications with React, backend frameworks, and SQL/NoSQL databases."
                ],
                "Required Skills & Qualifications": [
                    "Bachelor's degree in Computer Science, Engineering, or a related field.",
                    "Proficiency in: Python, JavaScript, React, SQL/NoSQL databases, API development.",
                    "Experience with: AI/ML model deployment, RAG-based solutions, cloud services (AWS, Azure).",
                    "Strong problem-solving skills and ability to work in an agile environment.",
                    "Familiarity with automation testing and CI/CD pipelines."
                ]
            }}
            ```
            """
        }])
        result= response['message']['content']
        print(result)
        result=extract_json_from_text(result)
        return {
            "data":result,
            "statusCode": 200
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            "Error": str(e),
            "statusCode": 500
        }