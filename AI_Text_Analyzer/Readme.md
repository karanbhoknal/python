AI Text Analyzer
Browser-Based Python Project (No Flask/Django)

A lightweight AI Text Analyzer that runs entirely in the browser using Python, HTML, CSS, and JavaScript. Users can input text and get instant insights such as word count, character count, sentence count, frequent words, sentiment analysis, and reading time.

Features

Count words, characters, sentences, and paragraphs

Identify most frequent words

Perform sentiment analysis (Positive / Negative / Neutral)

Estimate reading time

Real-time analysis without page reload

Tech Stack

Python 3 – backend text analysis

TextBlob – NLP & sentiment analysis

collections.Counter – frequent word calculation

HTML / CSS – frontend UI

JavaScript – communication between browser & Python server

Folder Structure
AI-Text-Analyzer/
│
├── index.html       # Main frontend page
├── style.css        # Styling for UI
├── script.js        # JS to send text & display results
├── server.py        # Python HTTP server & analysis logic
├── requirements.txt # Python dependencies
└── README.md        # Project description

Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-link>
cd AI-Text-Analyzer

2️⃣ Install Dependencies
pip install textblob
python -m textblob.download_corpora

3️⃣ Run the Python Server
python server.py


Server will run at: http://localhost:8000

4️⃣ Open in Browser

Open http://localhost:8000

Enter text and click Analyze

View results instantly on the page


How It Works (Step-by-Step)

User enters text in the browser interface

JavaScript sends text to a Python HTTP server


Python calculates:

Word count

Character count

Sentence & paragraph count

Most common words

Sentiment analysis using TextBlob

Reading time

Server sends results back as JSON

JavaScript dynamically displays results on the page



Skills Learned

Real-time Python ↔ frontend integration

Basic NLP and sentiment analysis

Handling JSON requests/responses

Building interactive web tools


Future Enhancements

Add text summarization

Highlight keywords in the text

Save analysis results as CSV or JSON

Add color-coded sentiment visualization
