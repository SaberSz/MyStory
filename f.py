'''
Created on 02-Feb-2018

@author: dylan
'''
import mysql.connector as ms
from flask import Flask
app = Flask(__name__)
cnx = ms.connect(unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='root', host='localhost', database='snp',)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container w3-green">
  <h1>Fun Facts</h1> 
  <p>Did you know?</p> 
</div>

<div class="w3-row-padding">
  <div class="w3-third">
    <h2>London</h2>
    <p>London is the capital city of England.</p>
    <p>It is the most populous city in the United Kingdom,
    with a metropolitan area of over 13 million inhabitants.</p>
  </div>

  <div class="w3-third">
    <h2>Paris</h2>
    <p>Paris is the capital of France.</p> 
    <p>The Paris area is one of the largest population centers in Europe,
    with more than 12 million inhabitants.</p>
  </div>

  <div class="w3-third">
    <h2>Tokyo</h2>
    <p>Tokyo is the capital of Japan.</p>
    <p>It is the center of the Greater Tokyo Area,
    and the most populous metropolitan area in the world.</p>
  </div>
</div>

</body>
</html>
    '''

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id   

@app.route('/database/<sk>')
def db_access(sk):
    #sk is not used
    try:
        cur=cnx.cursor()
        
        cur.execute("Select * from enquiry ;")
        d= cur.fetchall()
        
        cnx.commit()  
        return '''
       
    <!DOCTYPE html>
<html>
<body>
<h1 style="font-size:100x;color:blue;text-align:center;"> Here's your data <del>CUNT</del> TWAT!!!</h1>
<h3 style="font-size:40x;"> {}</h2>
<br>
<br>
<h1 style="font-size:100x;color:blue;text-align:center;"> <sup>Whamen</sup> and <sub>Men</sub></h1>
</body>
</html>
        '''.format(str(d))
        
    except ms.Error as e:
        print("Something went wrong: {}".format(e))    
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    