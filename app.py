from flask import Flask, render_template, request

app = Flask(__name__)


def read_file(filename='file4.txt', start=None, end=None):
    with open(filename, 'r', encoding="utf16") as f:
        contents = f.readlines()
    if start and end is not None:
        return '\n'.join(map(lambda x: x.rstrip(), contents[start:end]))
    return '\n'.join(map(lambda x: x.rstrip(), contents))


@app.route('/')
def hello_world():
    args = request.args
    if not list(args.values()):
        return render_template('template.html', contents=read_file()), 200
    if args.get('start').isalpha() or args.get('end').isalpha():
        return render_template('page_interval_error_3.html', start=args.get('start'), end=args.get('end')), 500

    start_param, end_param = int(args.get('start', None)), int(args.get('end', None))
    if start_param > end_param:
        return render_template('page_interval_error.html', start=start_param, end=end_param), 500
    if start_param == end_param:
        return render_template('page_interval_error_2.html', start=start_param, end=end_param), 500

    return render_template('template.html', contents=read_file(start=start_param, end=end_param)), 200


if __name__ == '__main__':
    app.run(debug=True)
