import cgi
import datetime
import os
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
app = Flask(__name__)

class League(object):
  def __init__(self, players, topic, futures):
    self.players = players
    self.topic = topic
    self.futures = futures
  def toDict(self):
    data = {
      "topic":self.topic,
      "players":self.players,
      "futures":self.futures 
    }
    return data
  def __repr__(self):
    out = self.topic + "\n with players: \n"
    for p in self.players:
      out += ' ' +p
      out += "\n and futures: \n"
    for f in self.futures:
      out += ' ' + f.__repr__  
    return out
class Future(object):
  def __init__(self, literal, owner):
    self.owner = owner
    self.literal = literal  
  def __repr__(self):
    return self.literal + self.owner[0:1]
def addSession(phpID):
  if phpID not in sessions:
    sessions.append(phpID)
    writeToFile(bf, '/php '+phpID)
    

  
def writeToFile(f, message):
  f.write('\n' + message)

def signUp(User):
  return User

def matchesTime(time):
    curTime = datetime.datetime.now().strftime("%x")
    if curTime == time:
        return True
    return False


@app.route('/', methods=['GET'])
def index():
  
  return render_template('index.html')


@app.route('/user', methods=['POST'])
def user():
 form = cgi.FieldStorage()
  username = form.getvalue('username_id')
  password = form.getvalue('password_id')
  session = form.getvalue('session_id')
  return redirect(url_for('index'))
os.getcwd()
cd = os.path.basename(os.getcwd()) + '/watchfortheplot3/static/ghostwriter-d436e-firebase-adminsdk-cnyy5-f82bb21219.json'
cred = credentials.Certificate(cd)
firebase_admin.initialize_app(cred)
db = firestore.client()
sessions = []
bf = open('BF.txt', 'a')
fb = open('FB.txt', 'a')
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
#checking for user input and responding
#while operational
# for users in connectedSockets:
#     checkIfNewInput(user.getPacket()) 

#def checkIfNewInput(cmd):
#     Figure out what type of cmd
#     What arguments are relevant
      #all methods also take arg ()
#     execute either addToPool("String"), requestTrade("[String myAssets, ...], [String yourAssets, ...]"), confirmTrade(boolean), markDegen([String markedFuture]), orderPref(["String Future", int pref]), newLeague(), setTime()

#######start of alpha databases##########



l1 = League(["Andrew", "Shaad", "Vivek", "Drew"],"The Office", ["Michael dies", "Michael marries holly", "Michael kills holly"])
league1 = db.collection('leagues').document('League1')
league1.set(l1.toDict())

l2 = League(["David"], "Infinity War", ["David will win!"]) 
league2 = db.collection('leagues').document('League2')
league2.set(l2.toDict())

leagues = db.collection('leagues').get()
for league in leagues:
  print(league.id)
  print(league.to_dict())
###End of temp Database###



