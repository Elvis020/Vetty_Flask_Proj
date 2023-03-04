from flask import Flask, render_template, request
from utils import read_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    args = request.args
    filename = args.get('filename', None)
    start_param = args.get('start', '0')
    end_param = args.get('end', '0')

    if not list(args.values()):
        return render_template('template.html', contents=read_file()), 200

    if filename not in [None, 'file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']:
        return render_template('file_name_error.html', filename=filename)

    if start_param.isalpha() or end_param.isalpha():
        return render_template('page_interval_error_3.html',
                               start=args.get('start'),
                               end=args.get('end')), 500

    start_param, end_param = int(start_param), int(end_param)
    if start_param > end_param:
        return render_template('page_interval_error.html',
                               start=start_param,
                               end=end_param), 500

    if start_param != 0 and end_param != 0 and start_param == end_param:
        return render_template('page_interval_error_2.html',
                               start=start_param,
                               end=end_param), 500

    return render_template('template.html',
                           contents=read_file(filename=args.get('filename'),
                                              start=start_param,
                                              end=end_param)), 200


if __name__ == '__main__':
    app.run(debug=True)
