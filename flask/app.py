from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        target = request.form.get('target', '')

        if target:
            result = subprocess.run(['ping', '-c', '3', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8') if result.returncode == 0 else f"Error: {result.stderr.decode('utf-8')}"
        else:
            output = "Invalid input. Please enter a valid IP address or hostname."

    return render_template('index.html', output=output)

@app.route('/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    output = ''
    if request.method == 'POST':
        target_vulnerable = request.form.get('target_vulnerable', '')

        if target_vulnerable:
            command = f'ping -c 3 {target_vulnerable}'
            try:
                output = os.popen(command).read()
            except FileNotFoundError as fnf_error:
                output = f'You Got {fnf_error}, probably /bin/sh is not found'
        else:
            output = "Invalid input. Please enter a valid IP address or hostname."

    return render_template('vulnerable.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
