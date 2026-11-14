# users = garcia,12345,2005 - boris,23456,2006 - carter,34567,2007
from bottle import route,run,template,request,response,redirect
import sqlite3

@route('/', method = 'GET') 
def index():
    return template('index')  #login form for localhost

@route('/logout',method = ['GET','POST'])
def logout():
    response.delete_cookie('year')
    redirect('/')

@route('/login', method = ['GET','POST']) # occurs when click submit button
def login():
    # check for existing valid cookie
    existing_year = request.get_cookie('year')
    if existing_year:
        data = {'title': 'welcome', 'user': 'back'}  # setup pairs for template file
        return template('main menu', data)  # call the template file
    # if not valid cookie
    username = request.forms.get('username')
    password = request.forms.get('password') #get username and password from login pg.

    con = sqlite3.connect('movies5.db') # connect to database
    cur = con.cursor()  # allow changes to database

    sql = "SELECT year FROM users WHERE name = ? AND password = ?"

    cur.execute(sql, (username, password))
    year = cur.fetchone()
    
    cur.close()
    

    if year:
        response.set_cookie('year', year[0], max_age=300)  #test for cookie with time limit, after 5min it resets the cookie so you have to sign in again

        data = {'title':'welcome','user':username} # setup pairs for template file
        return template ('main menu', data)   #call the template file

    else:
        mess = {'msg': 'HAHA You don\'t know how to log in to your account, JUST KIDDING, PLEASE TRY AGAIN'}  # it wouldn't log on
        return template('message', mess)

@route('/showallmovies', method = 'GET')
def movie_table():
    year = request.get_cookie('year')  #check for cookie
    if not year:
        log = {'msg': 'Tis confusion, I don\'t know who you are'}   # no cookie don't pass go template
        return template('message', log)    # call the template

    con = sqlite3.connect('movies5.db') # connect to database
    cur = con.cursor()  # allow changes to database          

    sql = '''SELECT film_id, title, description, release_year, length, categories.name FROM films, categories
       WHERE categories.category = films.category AND release_year = ?'''

    
    cur.execute(sql,[year])
    data = cur.fetchall()
    
    return template('displayfilms',rows=data)
        
@route('/addmovie', method = ['GET','POST'])  #add a movie page
def add_movie():
    if request.method == 'GET':             #get stuff
        year = request.get_cookie('year') #get cookie
        if not year:
            log = {'msg': 'Tis confusion, I don\'t know who you are'}  #no cookie
            return template('message', log)

        return template ('add_movie')   #yes cookie get add movie template
    else:                                   #post stuff
        year = request.get_cookie('year')   
        if not year:
            log = {'msg': 'WHO ARE YOU'}   #no cookie
            return template('message', log)
        
        movie = [] #empty list
       
        movie.append(request.forms.get('title'))   # add filled in forms to list
        movie.append(request.forms.get('description'))
        movie.append(request.get_cookie('year'))  #add cookie year to list
        movie.append(request.forms.get('length'))
        movie.append(request.forms.get('category'))
       
        con = sqlite3.connect('movies5.db') # connect to database
        cur = con.cursor()  # allow changes to database

        cur.execute('INSERT INTO films (title, description, release_year, length, category) VALUES(?,?,?,?,?)', movie)
        con.commit() #save to database
        con.close()
        return '<h1> film inserted successfully</h1> <a href="/login"><button>Main Menu</button></a>' #lets you know it worked & a button to go back

@route('/rem_movie', method = ['GET','POST'])
def rem_movie():

    if request.method == 'GET':             #get stuff
        year = request.get_cookie('year') #get cookie
        if not year:
            log = {'msg': 'Tis confusion, I don\'t know who you are'}  #no cookie
            return template('message', log)

        return template ('rem_movie')   #yes cookie get remove movie template
    else:
        year = request.get_cookie('year')
        if not year:
            log = {'msg': 'WHO ARE YOU'}   #no cookie
            return template('message', log)
        else:
            movie_info = [request.forms.get('I.D.'), request.forms.get('title') ]

            con = sqlite3.connect('movies5.db')  # connect to database
            cur = con.cursor()  # allow changes to database
            if not all (movie_info):  #check if all information has been added
                log = {'msg': 'UHH OHH YOU MESSED UP!!'}  # no information added
                return template('message_2', log)
            else:
                cur.execute('DELETE FROM films WHERE film_id=? AND title = ?', movie_info)   # sql statement with parameterized query,for movie_info list)
                con.commit()  # save to database
                con.close()
                return redirect('/login')
                #return template('displayfilms', rows=data)



run(host='0.0.0.0', port=8083)
