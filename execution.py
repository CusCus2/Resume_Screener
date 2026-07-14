import brain as br
import reader as rd

import json

job_description = """
We are looking for a Junior Data Scientist.
Must have:
- Python (Pandas, NumPy, Scikit-Learn)
- Experience with SQL
- Basic understanding of Machine Learning algorithms
- Good communication skills
Nice to have:
- Experience with AWS or Cloud deployment
- Knowledge of NLP
"""

try:
    resume = rd.extract_text_from_pdf("CV/Cormac_McCusker_CV.pdf")
    print("Resume loaded. Length: ", len(resume), " characters.")
except Exception as e:
    print("Error loading resume: ", e)
    exit()

print("AI is analysing the candidate.....")
result_json_string = br.screen_resume(resume, job_description)

try:
    clean_json = result_json_string.replace("```json", "").replace("```", "").strip()
    result_data = json.loads(clean_json)

    print("\n--- SCREENING REPORT ---")
    print(f"Candidate: {result_data.get('candidate_name', 'Unknown')}")
    print(f"Score: {result_data.get('match_score')}/100")
    print(f"Decision: {result_data.get('recommendation').upper()}")
    print(f"Reasoning: {result_data.get('reasoning')}")
    print(f"Missing Skills: {', '.join(result_data.get('missing_critical_skills', []))}")
except json.JSONDecodeError:
    print("Failed to parse JSON. Raw output: ")
    print(result_json_string)