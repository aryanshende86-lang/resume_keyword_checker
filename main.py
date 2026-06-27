import os
import re
import sys
def load_file(file_path, file_description):
    """Safely loads text from a file and handles missing or unreadable files."""
    if not os.path.exists(file_path):
        print(f"Error: The {file_description} file was not found at '{file_path}'.")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_description}: {e}")
        return None

def analyze_resume(jd_path, resume_path):
    print("Scanning files and initializing check...")
    
    
    jd_text = load_file(jd_path, "Job Description")
    resume_text = load_file(resume_path, "Resume")
    
    if jd_text is None or resume_text is None:
        print("Analysis aborted due to missing or invalid inputs.")
        return

    print("Extracting keywords from the Job Description...")
    
    keywords = set(re.findall(r'\b[a-zA-Z0-9+#]{2,}\b', jd_text.lower()))
    
   
    stop_words = {'and', 'the', 'for', 'with', 'you', 'will', 'are', 'that', 'this', 'from', 'have', 'with', 'your'}
    keywords = keywords - stop_words

    if not keywords:
        print("Warning: No valid keywords were found in the Job Description.")
        return

    print(f"Found {len(keywords)} potential keywords to check.")
    print("Matching keywords against your resume...")
    
    
    resume_text_lower = resume_text.lower()
    
    matched_keywords = []
    missing_keywords = []

    for kw in sorted(keywords):
      
        pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, resume_text_lower):
            matched_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    
    match_score = (len(matched_keywords) / len(keywords)) * 100

    
    print("\n" + "="*40)
    print("        RESUME ANALYSIS RESULTS        ")
    print("="*40)
    print(f"Overall Match Score: {match_score:.2f}%")
    print(f"Keywords Matched:    {len(matched_keywords)} / {len(keywords)}")
    print("-"*40)
    
    print("\nMissing Keywords:")
    if missing_keywords:
        for kw in missing_keywords:
            print(f" - {kw}")
    else:
        print("Incredible! Your resume covers all extracted keywords.")
    print("="*40 + "\n")

if __name__ == "__main__":

    DEFAULT_JD = "job_description.txt"
    DEFAULT_RESUME = "resume.txt"
    
    analyze_resume(DEFAULT_JD, DEFAULT_RESUME)
