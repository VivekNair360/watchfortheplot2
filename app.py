import cgi
import datetime
import os
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
app = Flask(__name__)
fbAuth = {
  "type": "service_account",
  "project_id": "ghostwriter-d436e",
  "private_key_id": "f82bb21219a23c98514222f064752c5f09252736",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCx88OddsJe9C0x\nRudb2SGJ6/9Orhpr05+SvCvWMHuTyx4uB9+udFEGsrE2utayr3ntFj2UTjGZR+PA\ndZRrNg+NE9wRGXChwztCyEQFedm/QoDgUjM8nY1UfOh28jJ+YsbWg6G66n83/Mzg\nbUZkYgHQ/LPZs14bog2Nm6n9WZzcqndGHuNBpdt72Qmk/Q1rX7YVkk9cAiNvVemc\n2NDYESRP5B1SYB2ttAThc3fIWj5z04KxbI0dJL0IlGZl7xK7HlbvO5pApMrAHyr8\n4GzEayEQ8v8ztuTolFxEtOx8x+v50QQ0etknXrWiO6O1kc0VyGjZXnQ+mjxgOK+Z\nlCwK90WpAgMBAAECggEABiULsSlDpvG5icUQAhzqSo/qnfXnFagWD4QN43SDH+RY\no3BEKgr8LUYIVoJ3HW5vwF8PO0rD7a4M0D1/JYCVYuK3q6N8Pym1pyWxK5s8iJ0s\nRBKykDpEghFaGZldYv3YLdoXwJOOVwmUrX84egjkVSoUr8TA0CV1YFlqskPg5cGy\nXFl+PGXobmxRxDgHpUEz1y5T+4WXDvsLFq8cuybXOhAamMyBNhX1r/e2qLndQYXt\n0XIqOUR2u/yBXek4gHc6IYtqgRTU2HwsfLc1UJOarrBm+qhTPXkclho4ObFYN2xi\nyDE5hUdZoZtZ7G19+zmM3RzzVYD77g1/LuecyxvLDQKBgQDkhUwT7vV11+B3N0iv\n1CEGE0cf+xvSpKCv9hiOrfBzL04Szhn0JM02OvDi01S01e4+6AmGgUn1VLj7fy4E\nf29+RsM6Xz8EiAt5OOtt7LCEyUn/l5/8xWUVFDhTG9O9Y1LObfZOoBDtvY0rr+t9\neDwiI7u6rp9Q4E0zo8g1geimrwKBgQDHWcis8hCSZnWqdo0geLfyJKoT6ASuKvcO\nPhaja+a6wPVxeH9m5PcfbecUDxgXizWLWhMVmvwmygCYcX2zNCJkR3X+T6fY2UbU\nZNqiVNp7cNPo+maOyst+73ZXGQ4195k5N4cs6vsY5SLQSK9tgyFAL7e3IqqNfUUN\nR37Ys8BvJwKBgHCD4S1/XoQjQnXwVm2cOJZRL5fjf5N7U1LQDM9TfSx5gitoJwc6\nh3/IDYrhGrffDWsTvHzpc4zDpkDOIc49IJxAIye+dby5b0zEZca93zvCEBk0gqVm\nW5rBVeo1rU92c/MH2VplHXCw/60e9QfWB2WXynrkN7UOe3SNk6okyHQpAoGADidM\nvSKulIZbwk+Kc4y+mp2JycIGWwtH4SX9W3r0tbuvcW/5s6d7+CpIZr8vmbRTh+JM\nSpNnZaWf5zLfltKTwoTkVrr3EslSYxAKCc52eJ8pHHhywZ6aVhfQUhzASoqawVo0\n6baBP2I9V4ZhlifiO3ln1MPMUiFbvradxer1Na8CgYBcUyIHWIlJe+qllURuYYqV\n9TXAA0QXWqSLMVOk0jKkpDd36JIit1EP1TWDe4bTugNEwIhFiuIaZVlkBrZL3QKF\nJlcztLeKRHLJFi5UkIUexW/EaflhVkc0nUN9lJ7PpgqFbS2xWqZGRTUNDiavb7dt\nxA4CZMTcX+v0XAWZC9PEVw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cnyy5@ghostwriter-d436e.iam.gserviceaccount.com",
  "client_id": "109821058527601237661",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cnyy5%40ghostwriter-d436e.iam.gserviceaccount.com"
}
<<<<<<< HEAD
class phpThread(object):
=======

""" class phpThread(object):
>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13
  def __init__(self, phpId, username, currentPage):
    self.phpId = phpId
    self.username = username
    self.currentPage = currentPage """
class League(object):
  #Initializes League object
  def __init__(self, players, topic, dates, futures, ID):
    self.players = players
    self.topic = topic
    self.futures = futures
    self.dates = dates
    self.ID = ID

  #Stores Leagues as dictionary objects in the database for ease of storage.  
  def toDict(self):
    data = {
      "topic":self.topic,
      "players":self.players,
      "futures":self.futures 
    }
    return data
  
  #String representation of League object (s) for troubleshooting.
  def __repr__(self):
    out = self.topic + "\n with players: \n"
    for p in self.players:
      out += ' ' +p
      out += "\n and futures: \n"
    for f in self.futures:
      out += ' ' + f.__repr__  
    return out
class Future(object):

  #Initializes the Future object
  def __init__(self, literal, owner):
    self.owner = owner
    self.literal = literal

  #String representation of Future object (s) for troubleshooting.  
  def __repr__(self):
    return self.literal + self.owner[0:1]
""" def addSession(phpID):
  if phpID not in sessions:
    sessions.append(phpID)
    writeToFile(bf, '/php '+phpID) """
#Writes to file object on python server for communication between front end and back end.
def writeToFile(f, message):
  f.write('\n' + message)
<<<<<<< HEAD
=======

#Went to Sign Up page, registered, a user name, and password.
>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13
def signUp(User):
  db.collection('users').document(User).set({User, User})
  return User

#Does validity check on time for draft night.
def matchesTime(time):
    curTime = datetime.datetime.now().strftime("%x")
    if curTime == time:
        return True
    return False

<<<<<<< HEAD
#User side URL sites

=======
#Default page of front - end
>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13
@app.route('/', methods=['GET'])
def idleHomeScreen():
  return render_template('idleHomeScreen.html')

@app.route('/wrongpassword', methods=['GET'])
def wrongPassword():
  return render_template('wrongpassword.html')

@app.route('/signin', methods=['GET'])
def signin():
  print("currently in the def: signin")
  return render_template('signin.html')

@app.route('/signup', methods = ['GET'])
def signupdisplay():
  return render_template('signup.html')

@app.route('/homePageForUser')
def homePageForUser():
  leaguesAdmin=[]
  leaguesPlayer=[]
  leaguesUnaf=[]
  for league in db.collection('leagues').get():
    if(league.to_dict()['players'][0] == currentuser):
      leaguesAdmin.append(league)
  return render_template('homepage2.html', username=currentuser, administrator=leaguesAdmin, member =leaguesPlayer, uninvolved =leaguesUnaf)


#/url for data transfer
'''
@app.route('/registerAccount', methods =  ['POST'])
def processSignup():
  print("got to processsignup")
  print(request.format('username'))
  usinput = request.format['username']
  psinput = request.format['password']
  print(usinput)
  print(psinput)
  originateUser(usinput,psinput)
  return redirect(url_for('homePageForUser'))
  '''
@app.route('/review', methods = ['POST'])
def processReview():
  print("processing degencases reviewed")
  #removeCaseFromPool(request.form['input'])
  return redirect(url_for('homePageForUser'))
@app.route('/login', methods =['POST'])
def login():
  print('attempting to sign into account')
  print(request.form['username'])
  un = request.form['username']
  print(un)
  ps = request.form['password']
  key = userReference(un)
  if(key != -1):
    if(key[1]==ps):
      currentuser = un
    else:
      return redirect(url_for('wrongpassword'))
  else:
    originateUser(un[0], ps[0])
    login()
  return redirect(url_for('homePageForUser'))


os.getcwd()
cd = os.path.basename(os.getcwd()) + '/watchfortheplot3/static/ghostwriter-d436e-firebase-adminsdk-cnyy5-f82bb21219.json'
cred = credentials.Certificate(fbAuth)
firebase_admin.initialize_app(cred)
db = firestore.client()
sessions = []
bf = open('BF.txt', 'a')
fb = open('FB.txt', 'a')
currentuser = ""
users = []

#checking for user input and responding
#while operational
# for users in connectedSockets:
#     checkIfNewInput(user.getPacket()) 

#def checkIfNewInput(cmd):
#     Figure out what type of cmd
#     What arguments are relevant
      #all methods also take arg ()
#     execute either addToPool("String"), requestTrade("[String myAssets, ...], [String yourAssets, ...]"), confirmTrade(boolean), markDegen([String markedFuture]), orderPref(["String Future", int pref]), newLeague(), setTime()

#When admin logs into page corresponding with creating a league. 
def originateLeague(usr, php, input):
  vals = input.split('|')
  topic = vals[2]
  dates = [] 
  invitees = [usr]
  for date in vals[3].split(","):
    dates.append(date)
  for invitee in vals[4].split(","):
    invitees.append(invitee)
  re = 0
  for ns in db.collection('leagues').get():
    re+=1
  l = League(invitees, topic, dates, [], re)
  #
  temp = db.collection('leagues').document(usr + "'s League!")
  temp.set(l.toDict())

<<<<<<< HEAD
def originateUser(username, password):
=======
#When user logs into page corresponding with setting a user account
def originateUser(username, password, phpThread):
>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13
  #userlist = db.collection('users').get()
  #for user in userlist:
   # print(user.to_dict())
  #db.collection('users').document('user').set({'Shaad':'Baptism'})
  if(userReference(username) == -1):
<<<<<<< HEAD
    users.append({username, password})
  
=======
    db.collection('users').document(username).set({username, password})

#Used to reference different users in the database  
>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13
def userReference(usrname):
  for user in db.collection('users').get():
    if(usrname == user.id):
      return user.to_dict()
  return -1

#Method that takes a very long string containing predictions separated by a comma.
def addToPool(usr, php, input, league):
  for future in input.split(","):
    league.futures.append(future)
  

#Method that allows a trade to be made.
def addTrade(Future, preferences, drops):
  for i in Future:
    for j in preferences:
      Future.append(preferences)
  Future.remove(drops)
  return 0

def setPreferences(Future):
  preferences = Future
  return preferences

def draft(Future):
  Future = setPreferences(Future)
  return 0

""" def originateSession(php):
  if getSessionFromPHP(php) == -1:
    sessions.append(phpThread(php, "", 000))

def getSessionFromPHP(php):
  for session in sessions:
    if(session.phpId == php):
      return session
  return -1 """
#######start of alpha databases##########
<<<<<<< HEAD
'''
l1 = League(["Andrew", "Shaad", "Vivek", "Drew"],"The Office", ['06-06-2066'],["Michael dies", "Michael marries holly", "Michael kills holly"], 0)
=======
""" l1 = League(["Andrew", "Shaad", "Vivek", "Drew"],"The Office", ['06-06-2066'],["Michael dies", "Michael marries holly", "Michael kills holly"], 0)
>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13
league1 = db.collection('leagues').document('League1')
league1.set(l1.toDict())

l2 = League(["David"], "Infinity War",['06-06-2066'], ["David will win!"], 1) 
league2 = db.collection('leagues').document('League2')
league2.set(l2.toDict())
originateLeague("TroubleShooterVivek", "0.0.0.0.0.0.0", "new |TroubleShooterVivek|troubleshooting_DUH!|06/06/2016,06/10/2017|Andrew, Shaad, Vivek")
leagues = db.collection('leagues').get()
for league in leagues:
  print(league.id)
  print(league.to_dict())
<<<<<<< HEAD
#myThread = phpThread("0.0.0.0","AndrewRiordan",00)
#originateUser("AndrewRiordan", "lmao",myThread)
=======
myThread = phpThread("0.0.0.0","AndrewRiordan",00)
originateUser("AndrewRiordan", "lmao",myThread) """

>>>>>>> 16892b9f9c0cb50f80ef88f46a1acb9bfd4e6f13

'''
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
