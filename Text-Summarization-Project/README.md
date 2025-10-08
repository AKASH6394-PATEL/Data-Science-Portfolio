# Text Summarization Project
# Text Summarization Project

## Project Goal
Is project ka goal ek Machine Learning model banana tha jo kisi bhi bade text document (jaise ek article ya notes) ko padhkar uski ek choti si, saaranshpurn (concise) summary apne aap bana de.

## Tools Used
* Python
* NLTK / spaCy (Text processing ke liye - aapne jo use kiya ho, woh likhein)
* Scikit-learn (TF-IDF jaise feature extraction ke liye)
* Pandas

## Workflow
1. Ek text document ko input ke roop mein liya.
2. Text ko saaf kiya (jaise stopwords hatana, punctuation hatana).
3. Text ke sentences ki importance score calculate ki.
4. Sabse zyada score waale sentences ko chun kar ek summary banayi.

## Zaroori Note
Is project ka trained model file (.pkl file) uske bade size (38 MB) ki wajah se repository mein shaamil nahi kiya gaya hai. Is project ke code ko run karne par model file apne aap generate ho sakti hai.
