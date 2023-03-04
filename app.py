from flask import Flask, render_template, request

app = Flask(__name__)


def read_file(filename='file1.txt', start=None, end=None):
    with open(filename, 'r') as f:
        contents = f.readlines()
    if start and end is not None:
        return '\n'.join(map(lambda x: x.rstrip(), contents[start:end]))
    return '\n'.join(map(lambda x: x.rstrip(), contents))


@app.route('/')
def hello_world():
    args = request.args
    if not list(args.values()):
        return render_template('template.html', contents=read_file())
    start_param, end_param = int(args.get('start', None)), int(args.get('end', None))
    return render_template('template.html', contents=read_file(start=start_param, end=end_param))


if __name__ == '__main__':
    app.run(debug=True)
