# resume_keyword_checker

An automated terminal-based script designed to streamline the recruitment optimization process. The tool processes a target Job Description (JD) text file, extracts critical technical keywords via regular expressions, and benchmarks a resume text file against them to calculate a match score and isolate missing phrases.

## Features

 **Regex-Driven Extraction:** Automatically isolates industry terms, programming languages, and alphanumeric tools utilizing clean word boundary matching patterns (`\b`).
 
 **Bulletproof Error Tapping:** Features custom file-system validation blocks to gracefully handle missing files, preventing unhandled script crashes.
 
 **Intuitive Terminal UI:** Logs sequential, clean real-time status and progress updates directly to the console console.
 
 **Zero External Dependencies:** Built purely on native, standard Python libraries—no complex environment setups or external installations required.

##  System Demonstration

### 1. Terminal Execution & Match Output
Below is the live terminal output displaying a successful analysis execution, calculating the exact alignment percentage, and compiling missing phrases:

<img width="906" height="954" alt="image" src="https://github.com/user-attachments/assets/b7022d3e-6141-4086-b73d-1325f20520b9" />

<img width="487" height="475" alt="image" src="https://github.com/user-attachments/assets/8a706a3c-aaff-4b84-bd64-ac7623303936" />

### 2. Error Tapping Test
Here is what happens if a file goes missing or is named incorrectly. The error tapping catches it immediately and shuts down safely:

<img width="644" height="207" alt="image" src="https://github.com/user-attachments/assets/ccf71ae3-4f79-48c2-8485-a95dc09c92a1" />

#### Why this error occurs:
This error occurs because the script utilizes `os.path.exists()` to verify that both `job_description.txt` and `resume.txt` are physically present in the directory before attempting to open them. 

In this test case, I intentionally renamed `resume.txt` to see how the script reacts. Instead of throwing a massive, unhandled Python stack trace that crashes the terminal, my custom `load_file()` wrapper caught the missing file exception, logged a clean warning message to the user, and exited the program safely.

##  Installation & Setup

1. **Clone the Project Repository**
   
   git clone <your-github-repo-link>
   cd <your-repo-folder-name>

## Establish Environment Source Files
Place your evaluation files directly in the root project folder alongside your script:
### job_description.txt: 
Contains the benchmark job requirements.

sample :
<img width="1149" height="265" alt="image" src="https://github.com/user-attachments/assets/26d311a2-2039-4965-8471-5151c183f60b" />

### resume.txt: 
Contains the applicant's current CV/resume text.

sample :
<img width="1270" height="294" alt="image" src="https://github.com/user-attachments/assets/4becd59d-8b62-4fd3-917c-9eafd0585658" />

## Run 
In the vs code execute using
### python keyword.py
