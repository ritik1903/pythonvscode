from flask import Flask, render_template, url_for
from flask import request, redirect, flash, make_response, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Shoes_Setup import Base, ShoeCompanyName, ShoeNames, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
import datetime

engine = create_engine('sqlite:///shoes.db',
                       connect_args={'check_same_thread': False}, echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json',
                            'r').read())['web']['client_id']
APPLICATION_NAME = "Shoes Store"

DBSession = sessionmaker(bind=engine)
session = DBSession()
# Create anti-forgery state token
shoe_catlg = session.query(ShoeCompanyName).all()


# login


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    shoe_catlg = session.query(ShoeCompanyName).all()
    sn = session.query(ShoeNames).all()
    return render_template('login.html',
                           STATE=state, shoe_catlg=shoe_catlg, sn=sn)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius: 150px;'
    '-webkit-border-radius: 150px; -moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print ("done!")
    return output


# User Helper Functions
def createUser(login_session):
    User1 = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(User1)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception as error:
        print(error)
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session

#####
# Home


@app.route('/')
@app.route('/home')
def home():
    shoe_catlg = session.query(ShoeCompanyName).all()
    return render_template('myhome.html', shoe_catlg=shoe_catlg)

#####
# Shoe Category for admins


@app.route('/ShoeStore')
def ShoeStore():
    try:
        if login_session['username']:
            name = login_session['username']
            shoe_catlg = session.query(ShoeCompanyName).all()
            scn = session.query(ShoeCompanyName).all()
            sn = session.query(ShoeNames).all()
            return render_template('myhome.html', shoe_catlg=shoe_catlg,
                                   scn=scn, sn=sn, uname=name)
    except:
        return redirect(url_for('showLogin'))

######
# Showing shoes based on shoe category


@app.route('/ShoeStore/<int:scnid>/AllCompanys')
def showShoes(scnid):
    shoe_catlg = session.query(ShoeCompanyName).all()
    scn = session.query(ShoeCompanyName).filter_by(id=scnid).one()
    sn = session.query(ShoeNames).filter_by(shoecompanynameid=scnid).all()
    try:
        if login_session['username']:
            return render_template('showShoes.html', shoe_catlg=shoe_catlg,
                                   scn=scn, sn=sn,
                                   uname=login_session['username'])
    except:
        return render_template('showShoes.html',
                               shoe_catlg=shoe_catlg, scn=scn, sn=sn)

#####
# Add New Shoe


@app.route('/ShoeStore/addShoeCompany', methods=['POST', 'GET'])
def addShoeCompany():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        company = ShoeCompanyName(name=request.form['name'],
                                  user_id=login_session['user_id'])
        session.add(company)
        session.commit()
        return redirect(url_for('ShoeStore'))
    else:
        return render_template('addShoeCompany.html', shoe_catlg=shoe_catlg)

########
# Edit Shoe Category


@app.route('/ShoeStore/<int:scnid>/edit', methods=['POST', 'GET'])
def editShoeCategory(scnid):
    if 'username' not in login_session:
        return redirect('/login')
    editedShoe = session.query(ShoeCompanyName).filter_by(id=scnid).one()
    creator = getUserInfo(editedShoe.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You cannot edit this Shoe Category."
              "This is belongs to %s" % creator.name)
        return redirect(url_for('ShoeStore'))
    if request.method == "POST":
        if request.form['name']:
            editedShoe.name = request.form['name']
        session.add(editedShoe)
        session.commit()
        flash("Shoe Category Edited Successfully")
        return redirect(url_for('ShoeStore'))
    else:
        # shoe_catlg is global variable we can them in entire application
        return render_template('editShoeCategory.html',
                               sk=editedShoe, shoe_catlg=shoe_catlg)

######
# Delete Shoe Category


@app.route('/ShoeStore/<int:scnid>/delete', methods=['POST', 'GET'])
def deleteShoeCategory(scnid):
    sk = session.query(ShoeCompanyName).filter_by(id=scnid).one()
    creator = getUserInfo(sk.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You cannot Delete this Shoe Category."
              "This is belongs to %s" % creator.name)
        return redirect(url_for('ShoekStore'))
    if request.method == "POST":
        session.delete(sk)
        session.commit()
        flash("Shoe Category Deleted Successfully")
        return redirect(url_for('ShoeStore'))
    else:
        return render_template('deleteShoeCategory.html',
                               sk=sk, shoe_catlg=shoe_catlg)
# Add New Shoe Name Details


@app.route('/ShoeStore/addCompany/addShoeDetails/<string:scnname>/add',
           methods=['GET', 'POST'])
def addShoeDetails(scnname):
    if 'username' not in login_session:
        return redirect('/login')
    scn = session.query(ShoeCompanyName).filter_by(name=scnname).one()
    # See if the logged in user is not the owner of shoe
    creator = getUserInfo(scn.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You can't add new Shoe edition"
              "This is belongs to %s" % creator.name)
        return redirect(url_for('showShoes', scnid=scn.id))
    if request.method == 'POST':
        name = request.form['name']
        sole = request.form['sole']
        closure = request.form['closure']
        material = request.form['material']
        lifestyle = request.form['lifestyle']
        price = request.form['price']
        shoedetails = ShoeNames(
            name=name, sole=sole,
            closure=closure, material=material,
            lifestyle=lifestyle,
            price=price,
            date=datetime.datetime.now(),
            shoecompanynameid=scn.id,
            user_id=login_session['user_id'])
        session.add(shoedetails)
        session.commit()
        return redirect(url_for('showShoes', scnid=scn.id))
    else:
        return render_template('addShoeDetails.html',
                               scnname=scn.name, shoe_catlg=shoe_catlg)

######
# Edit Shoe details


@app.route('/ShoeStore/<int:scnid>/<string:scmname>/edit',
           methods=['GET', 'POST'])
def editShoe(scnid, scmname):
    sk = session.query(ShoeCompanyName).filter_by(id=scnid).one()
    shoedetails = session.query(ShoeNames).filter_by(name=scmname).one()
    # See if the logged in user is not the owner of shoe
    creator = getUserInfo(sk.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You can't edit this Shoe edition"
              "This is belongs to %s" % creator.name)
        return redirect(url_for('showShoes', scnid=sk.id))
    # POST methods
    if request.method == 'POST':
        shoedetails.name = request.form['name']
        shoedetails.sole = request.form['sole']
        shoedetails.closure = request.form['closure']
        shoedetails.material = request.form['material']
        shoedetails.lifestyle = request.form['lifestyle']
        shoedetails.price = request.form['price']
        shoedetails.date = datetime.datetime.now()
        session.add(shoedetails)
        session.commit()
        flash("Shoe Edited Successfully")
        return redirect(url_for('showShoes', scnid=scnid))
    else:
        return render_template('editShoe.html',
                               scnid=scnid, shoedetails=shoedetails,
                               shoe_catlg=shoe_catlg)

#####
# Delte Shoe Edit


@app.route('/ShoekStore/<int:scnid>/<string:scmname>/delete',
           methods=['GET', 'POST'])
def deleteShoe(scnid, scmname):
    sk = session.query(ShoeCompanyName).filter_by(id=scnid).one()
    shoedetails = session.query(ShoeNames).filter_by(name=scmname).one()
    # See if the logged in user is not the owner of shoe
    creator = getUserInfo(sk.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You can't delete this Shoe edition"
              "This is belongs to %s" % creator.name)
        return redirect(url_for('showShoes', scnid=sk.id))
    if request.method == "POST":
        session.delete(shoedetails)
        session.commit()
        flash("Deleted Shoe Successfully")
        return redirect(url_for('showShoes', scnid=scnid))
    else:
        return render_template('deleteShoe.html',
                               scnid=scnid, shoedetails=shoedetails,
                               shoe_catlg=shoe_catlg)

####
# Logout from current user


@app.route('/logout')
def logout():
    access_token = login_session['access_token']
    print ('In gdisconnect access token is %s', access_token)
    print ('User name is: ')
    print (login_session['username'])
    if access_token is None:
        print ('Access Token is None')
        response = make_response(
            json.dumps('Current user not connected....'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = \
        h.request(uri=url, method='POST', body=None,
                  headers={
                      'content-type': 'application/x-www-form-urlencoded'})[0]

    print (result['status'])
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps(
            'Successfully disconnected user..'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successful logged out")
        return redirect(url_for('showLogin'))
        # return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

#####
# Json


@app.route('/ShoeStore/JSON')
def allShoesJSON():
    shoecategories = session.query(ShoeCompanyName).all()
    category_dict = [c.serialize for c in shoecategories]
    for c in range(len(category_dict)):
        shoes = [i.serialize for i in session.query(
                 ShoeNames).filter_by(
                     shoecompanynameid=category_dict[c]["id"]).all()]
        if shoes:
            category_dict[c]["shoe"] = shoes
    return jsonify(ShoeCompanyName=category_dict)

####


@app.route('/shoeStore/shoeCategories/JSON')
def categoriesJSON():
    shoes = session.query(ShoeCompanyName).all()
    return jsonify(shoeCategories=[c.serialize for c in shoes])

####


@app.route('/shoeStore/shoes/JSON')
def itemsJSON():
    items = session.query(ShoeNames).all()
    return jsonify(shoes=[i.serialize for i in items])

#####


@app.route('/shoeStore/<path:shoe_name>/shoes/JSON')
def categoryItemsJSON(shoe_name):
    shoeCategory = session.query(
                   ShoeCompanyName).filter_by(name=shoe_name).one()
    shoes = session.query(ShoeNames).filter_by(shoename=shoeCategory).all()
    return jsonify(shoeEdtion=[i.serialize for i in shoes])

#####


@app.route('/shoeStore/<path:shoe_name>/<path:edition_name>/JSON')
def ItemJSON(shoe_name, edition_name):
    shoeCategory = session.query(
        ShoeCompanyName).filter_by(name=shoe_name).one()
    shoeEdition = session.query(ShoeNames).filter_by(
           name=edition_name, shoename=shoeCategory).one()
    return jsonify(shoeEdition=[shoeEdition.serialize])

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='127.0.0.1', port=8888)