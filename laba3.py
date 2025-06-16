from flask import Flask, render_template, request

app = Flask(__name__)

# лабораторная 4
# def get_most_common_word(text: str) -> str:
#     text = text.lower()
#     for ch in '.,!?:;()"[]{}-':
#         text = text.replace(ch, '')
#     words = text.split()
#     word_counts = {}
#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1
#     if word_counts:
#         return max(word_counts, key=word_counts.get)
#     return None

# лабораторная 3
def get_most_common_word(text: str) -> str:
    text = text.lower()
    for ch in '.,!?:;()"[]{}-':
        text = text.replace(ch, '')
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    if word_counts:
        return max(word_counts, key=word_counts.get)
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    most_common_word = None

    if request.method == 'POST':
        uploaded_file = request.files.get('text_file')
        if uploaded_file and uploaded_file.filename.endswith('.txt'):
            content = uploaded_file.read().decode('utf-8')
            most_common_word = get_most_common_word(content)

    return render_template('index.html', result=most_common_word)

if __name__ == '__main__':
    app.run()

