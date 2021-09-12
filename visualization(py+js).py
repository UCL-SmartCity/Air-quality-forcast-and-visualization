# -*- encoding:utf-8 -*-

import csv
import os
import time

from flask import (Flask, abort, jsonify, redirect, render_template, request,
                   session, url_for)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kyes'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    args = request.args.get("type", "")
    if args == "":
        args = 'next hour'
    datas = []
    with open('data/monitoring.csv', 'r+')as f:
        reader = csv.reader(f)
        print(type(reader))

        for rows in reader:
            list1 = []
            print(rows)
            for row in rows:
                result = row
                if args in row:
                    for ro in str(row).split('\n'):
                        if args in ro:
                            result = ro.replace(args+':', '')
                            break
                list1.append(result)
            datas.append(list1)
    datas = datas[1:]

    return render_template('index.html', datas=datas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
