from flask import Flask, request, render_template_string

app = Flask(__name__)
info_repository = []

@app.route('/')
def home():
    return render_template_string('''
        <form method="post" action="/add">
            정보: <input type="text" name="info">
            <input type="submit" value="저장">
        </form>
        <h2>저장된 정보:</h2>
        <ul>
            {% for info in info_repository %}
                <li>{{ info }}</li>
            {% endfor %}
        </ul>
    ''', info_repository=info_repository)

@app.route('/add', methods=['POST'])
def add_info():
    info = request.form['info']
    info_repository.append(info)
    return home()

if __name__ == '__main__':
    app.run(debug=True)
