import ollama

def screen_resume(resume_text, job_desc):

    prompt = f"""
    You are a senior Technical recruiter with 20 years of experience.
    Your goal is to objectively evealuate a candidate based on a job description (JD).

    Job Description :
    {job_desc}

    Candidate Resume:
    {resume_text}

    TASK:
    Analyse the resume against the JD. Look for key skills, experience levels, and project relevance.
    Be strict but fair. "React" matches "React.js". "AWS" mathces "Amazon web Services".

    Output Format;
    Provide the response in valid JSON format ONLY. Do not add any conversational text.
    structure:
    {{
        "candidate_name" : "extracted name",
        "match_score" : "0-100",
        "key_strengths" : ["list of 3 key strengths"],
        "missing_critical_skills" : ["list of missing skills"],
        "recommendation" : "Interview" or "Reject",
        "reasoning": "A 2-sentence summary of why."
    }}
    """

    response = ollama.chat(model='llama3', messages = [
        {'role' : 'user', 'content' : prompt},
    ])

    return response['message']['content']