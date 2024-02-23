from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz questions and answers
quiz_data = [
    {"question": "1.What is the capital city of India?", "options": ["Mumbai", "New Delhi", "Kolkata"], "answer": "New Delhi"},
    {"question": "2.Who is known as the 'Father of the Nation' in India?", "options": ["Subhas Chandra Bose", "Jawaharlal Nehru", "Mahatma Gandhi"], "answer": "Mahatma Gandhi"},
    {"question": "3.Which river is considered sacred in Hinduism and is also known as the Ganges?", "options": ["Ganga", "Yamuna", "Brahmaputra"], "answer": "Ganga"},
    {"question": "4.What is the national currency of India?", "options": ["Rupiah", " Indian Rupee (INR)", "Baht"], "answer": "Indian Rupee (INR)"},
    {"question": "5.Which planet is known as the 'Red Planet'?", "options": ["Venus", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "6.Which country is known as the 'Land of the Rising Sun'?", "options": ["China", "South Korea", "Japan"], "answer": "Japan"},
    {"question": "7.Who holds the record for the most goals scored in FIFA World Cup history?", "options": ["Cristiano Ronaldo", "Pele", "Lionel Messi"], "answer": "Pele"},
    {"question": "8.In which sport would you perform a slam dunk?", "options": ["Basketball", "Tennis", "Soccer"], "answer": "Basketball"},
    {"question": "9.Which country hosted the 2016 Summer Olympics?", "options": ["China", "United States", "Brazil"], "answer": "Brazil"},
    {"question": "10.What is the scoring term used in golf when a player completes a hole in one stroke under par?", "options": ["Birdie", "Eagle", "Albatross"], "answer": "Birdie"} 
    
]   

@app.route('/')
def index():
    return render_template('index.html', quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    user_answers = request.form.to_dict()
    
    for question in quiz_data:
        if user_answers.get(question['question']) == question['answer']:
            score += 1

    return f'Your score: {score}/{len(quiz_data)}'

if __name__ == '__main__':
    app.run(debug=True)

