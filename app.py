from flask import Flask, render_template_string
import random

app = Flask(__name__)

DATA = [
    {
        "reference": "Matthew 24:14",
        "text": "And this good news of the Kingdom will be preached in all the inhabited earth...",
        "missing_word": "Kingdom"
    },
    {
        "reference": "Psalm 83:18",
        "text": "May people know that you, whose name is Jehovah, You alone are the Most High over all the earth.",
        "missing_word": "Jehovah"
    },
    {
        "reference": "Revelation 21:4",
        "text": "And he will wipe out every tear from their eyes, and death will be no more...",
        "missing_word": "death"
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>JW Scripture Challenge</title>
    <style>
        body { 
            font-family: 'Segoe UI', sans-serif; 
            text-align: center; 
            background: #f0f2f5; 
            background-image: radial-gradient(#3498db 0.5px, transparent 0.5px);
            background-size: 20px 20px; /* Subtle geometric dot pattern */
            padding: 50px; 
        }
        .card { 
            background: white; 
            padding: 40px; 
            border-radius: 12px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.1); 
            display: inline-block; 
            max-width: 500px; 
            border-top: 8px solid #3498db;
        }
        .reference { color: #3498db; font-weight: bold; font-size: 1.4em; margin-bottom: 20px; }
        .text { font-size: 1.1em; color: #2c3e50; line-height: 1.6; margin-bottom: 25px; }

        input { 
            padding: 12px; 
            width: 80%; 
            border: 2px solid #ddd; 
            border-radius: 8px; 
            font-size: 1em; 
            outline: none;
            transition: 0.3s;
        }

        .correct { border-color: #2ecc71; background-color: #eafaf1; }
        .wrong { border-color: #e74c3c; background-color: #fdeaeb; }

        .btn-group { margin-top: 25px; }
        button { 
            background-color: #3498db; 
            color: white; 
            padding: 12px 24px; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer; 
            font-weight: bold;
        }
        .next-btn { background-color: #95a5a6; margin-left: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="reference">{{ scripture.reference }}</div>
        <p class="text">"{{ scripture_display }}"</p>

        <input type="text" id="userInput" placeholder="Type the missing word..." autocomplete="off">

        <div class="btn-group">
            <button onclick="checkAnswer()">Check Answer</button>
            <button class="next-btn" onclick="window.location.reload()">Next</button>
        </div>
        <p id="feedback"></p>
    </div>

    <script>
        const correctWord = "{{ scripture.missing_word }}".toLowerCase();

        function checkAnswer() {
            const input = document.getElementById('userInput');
            const feedback = document.getElementById('feedback');
            const val = input.value.trim().toLowerCase();

            if (val === correctWord) {
                input.className = 'correct';
                feedback.innerHTML = "✨ Exactly right!";
                feedback.style.color = "#2ecc71";
            } else {
                input.className = 'wrong';
                feedback.innerHTML = "Try again!";
                feedback.style.color = "#e74c3c";
            }
        }
    </script>
</body>
</html>
"""


@app.route('/')
def home():
    selected = random.choice(DATA)
    # Create the display version of the text with underscores
    display_text = selected['text'].replace(selected['missing_word'], "_______")
    return render_template_string(HTML_TEMPLATE, scripture=selected, scripture_display=display_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)