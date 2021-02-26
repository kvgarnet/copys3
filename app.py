from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
import copys3
app = Flask(__name__)
app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listsrcbucket', methods=['GET','POST'])
def listsrcbucket():
    if request.method == 'POST':
        sourcebucket=request.form['sourcebucket']
        objlist=copys3.listobject(sourcebucket)
        return render_template('listsrc.html',objectlist=objlist,bucketname=sourcebucket)
    return render_template('listsrc.html')

@app.route('/listdestbucket', methods=['GET','POST'])
def listdestbucket():
    if request.method == 'POST':
        destbucket=request.form['destbucket']
        objlist=copys3.listobject(destbucket)
        return render_template('listdest.html',objectlist=objlist,bucketname=destbucket)
    return render_template('listdest.html')
@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        # urls = {}

        # if os.path.exists('urls.json'):
            # with open('urls.json') as urls_file:
                # urls = json.load(urls_file)
        sourcebucket=request.form['sourcebucket']
        destbucket=request.form['destbucket']
        sizemb=float(request.form['sizemb'])
        # sizemb=request.form['sizemb']
        flash(f"Copying files larger than {sizemb}MB from {sourcebucket}...")
        copys3.checkobject(sourcebucket,destbucket,sizemb)
        # return redirect(url_for('home'))
        return render_template('your_url.html')

        # if request.form['code'] in urls.keys():
            # flash('That short name has already been taken. Please select another name.')
            # return redirect(url_for('home'))

        # urls[request.form['code']] = {'url':request.form['url']}
        # with open('urls.json','w') as url_file:
            # json.dump(urls, url_file)
        # return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))
if __name__ == '__main__':
    app.run()
