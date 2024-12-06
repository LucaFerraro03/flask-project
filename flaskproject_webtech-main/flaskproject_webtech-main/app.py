from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

def load_team_data():
    team_members = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/team.csv')

    try:
        with open(csv_path, mode = 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                team_members.append(row)
        return team_members
    except FileNotFoundError:
        print(f'Error: File {csv_path} not found.')
        return []
    except Exception as e:
        print(f'Error loading team data: {e}')
        return []
    
def load_books_data():
    books = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/books.csv')

    try:
        with open(csv_path, mode = 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                books.append(row)
        return books
    except FileNotFoundError:
        print(f'Error: File {csv_path} not found.')
        return []
    except Exception as e:
        print(f'Error loading books data: {e}')
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    team_members = load_team_data()
    return render_template('team.html', team_members = team_members)

@app.route('/books')
def books():
    books = load_books_data()
    return render_template('books.html', books = books)

if __name__ == '__main__':
    app.run(debug=True)