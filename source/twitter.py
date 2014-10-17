#! /usr/bin/env python

import curses, datetime, traceback
import math

#example data
tweets=[{"user":"testuser","name":"Fakey McFakename","time":"1h ago","msg":"HUEHUEHUEHUEHUEHUE"},
        {"user":"potato","name":"Mashed Thingie", "time":"2014-01-01","msg":"Happy year of the potato"},
        {"user":"therealcolumbus","name":"Chris Columbus", "time":"1492-10-12","msg":"Hey this India thing is neat. Kida wish we had planes tho."},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
        {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"}]
mentions=[{"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"},
          {"user":"fillerbot","name":"Free Filler","time":"soon","msg":"12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"}]
messages=[{"from":"Spammy User","fromalias":"WonderfulSpam","time":"1745","msg":"Hey check out this crap"},
          {"from":"Spammy User","fromalias":"WonderfulSpam","time":"1745","msg":"Hey check out this karp"},
          {"from":"Spammy User","fromalias":"WonderfulSpam","time":"1745","msg":"Hey check out this kart"},
          {"from":"Spammy User","fromalias":"WonderfulSpam","time":"1745","msg":"Hey check out this mart"}]
options={"Option1":"Status1","Option2":"Status2","Option3":"Status3","Option4":"Status4",
        "Option5":"Status5","Option6":"Status6","Option7":"Status7","Option8":"Status8",
        "Option9":"Status9","Option10":"Status10","Option11":"Status11","Option12":"Status12"}

def init():
  """
  Initializes the curses environment. Returns the environment variable
  """

  scr=curses.initscr()
  curses.noecho()
  curses.cbreak()
  scr.keypad(1)
  if curses.has_colors(): curses.start_color()
  return scr

def exitp():
  """
  Deactivates curses options and terminates program
  """

  curses.nocbreak()
  curses.echo()
  scr.keypad(0)
  curses.endwin()

def refresh(screens):
  """
  Receives an array with screens and refreshes them in order.

  Make sure the screens in the background are in the first positions of the list.
  """

  for screen in screens: screen.refresh()

def print_tweets():
  """
  Receives a screen and prints some tweets in it 
  """

  #screen.addstr("Tweets\n\n")

  #Print last tweets in order
  try:
    for tweet in tweets:
      lcscr.addstr("@%s %s [%s] \n %s\n\n"%(tweet["user"],tweet["name"],tweet["time"],tweet["msg"]))
  #If print is outside limits, stop printing.
  except:
    pass

def print_notif():
  """
  Receives a screen and prints notifications in it 
  """

  rcscr.addstr("Mentions\n\n")

  #Print last mentions in order, like tweets
  try:
    for mention in mentions:
      rcscr.addstr("@%s %s [%s] \n %s\n\n"%(mention["user"],mention["name"],mention["time"],mention["msg"]))
  #Out of range exception avoidance maneuver
  except:
    pass

def print_config():
  """
  Prints the option menu in the selected screen
  """

  rcscr.addstr("Config\n\n")

  try:
    for opt,sel in options.iteritems():
      rcscr.addstr("%s - %s\n\n"%(opt,sel))
  except:
    pass

def print_dms():
  """
  Prints a list of DMs in the screen
  """

  rcscr.addstr("DMs\n\n")

  try:
    for msg in messages:
      rcscr.addstr("@%s %s [%s] \n %s\n\n"%(msg["from"],msg["fromalias"],msg["time"],msg["msg"]))
  except:
    pass

def print_account():
  """
  Prints account status
  """

  rcscr.addstr("Account\n\n")
  rcscr.addstr("Logged in as\n @%s\n\n"%username)
  rcscr.addstr("[Disconnect]\n")
  rcscr.addstr("[Edit permissions]\n")
  rcscr.addstr("[Some other option]\n")


def print_header():
  """
  Prints the program header 

  The selection indicates the option in the header that is highlighted
  """

  if flags["config"]:
    scr.addstr(0,1,"(F1)Config ")
    scr.addstr(0,13,"| (F2)Account | (F3)DMs | (F10)Clear | (F11)Exit",curses.A_REVERSE)
    scr.chgat(-1, curses.A_REVERSE)
  elif flags["account"]:
    scr.addstr(0,1,"(F1)Config |",curses.A_REVERSE)
    scr.addstr(0,14," (F2)Account ")
    scr.addstr(0,27,"| (F3)DMs | (F10)Clear | (F11)Exit",curses.A_REVERSE)
    scr.chgat(-1,curses.A_REVERSE)
  elif flags["dms"]:
    scr.addstr(0,1,"(F1)Config | (F2)Account |",curses.A_REVERSE)
    scr.addstr(0,28," (F3)DMs ")
    scr.addstr(0,37,"| (F10)Clear | (F11)Exit",curses.A_REVERSE)
    scr.chgat(-1,curses.A_REVERSE)
  else:
    scr.addstr(0,1,"(F1)Config | (F2)Account | (F3)DMs | (F10)Clear | (F11)Exit",curses.A_REVERSE)
    scr.chgat(-1, curses.A_REVERSE)

def print_status():
  """
  Prints the status bar
  """

  scr.addstr(curses.LINES-1,1,"@%s - [%i] Unread messages - Last updated %s - %s"%(username,msgs,now.strftime("%Y-%m-%d %H%M"),status))

def print_boxes():
  """
  Prints borders in the window containers
  """

  screenl.box()
  screenr.box()

def print_cycle():
  """
  Common printing operations
  """

  for screen in screens: screen.clear()
  print_header()
  print_status()
  print_boxes()
  print_tweets()

def std_cycle():
  """
  Standard printin process. Tweets on left screen and mentions on right one
  """

  print_cycle()
  print_notif()

if __name__=="__main__":
  #Initialize screen array
  screens=[]
  #Create flags for menu elements
  flags={"config":0,"account":0,"dms":0}
  #Global variables
  status="updated"
  username="testuser"
  msgs=4

  try:
    #Initialize main screen and print menu and status bars
    scr=init()
    screens.append(scr)
    now=datetime.datetime.now()

    #Print header and status bars
    print_header()
    print_status()
    
    #Create left and right screen borders
    screenl=curses.newwin(curses.LINES-2,int(math.floor(curses.COLS/2)),1,0)
    screenl.box()
    screens.append(screenl)
    screenr=curses.newwin(curses.LINES-2,int(math.floor(curses.COLS/2)),1,curses.COLS-int(math.floor(curses.COLS/2)))
    screenr.box()
    screens.append(screenr)

    #Create left and right content screens
    lcscr=curses.newwin(curses.LINES-4,int(math.floor(curses.COLS/2))-2,2,1)
    screens.append(lcscr)
    rcscr=curses.newwin(curses.LINES-4,int(math.floor(curses.COLS/2))-2,2,curses.COLS-int(math.floor(curses.COLS/2))+1)
    screens.append(rcscr)

    #Initial content print
    print_notif()
    print_tweets()
    #Call to refresh to update all the screens
    refresh(screens)

    #Event loop
    while 1:
      now=datetime.datetime.now()
      action=scr.getch()

      #Choices and flag evaluation
      if action==curses.KEY_F1 and not flags["config"]: 
        flags["config"]=1
        for key,val in {key:0 for key,val in flags.iteritems() if key!="config"}.iteritems(): flags[key]=val
        print_cycle()
        print_config()
        
      elif action==curses.KEY_F1 and flags["config"]:
        flags["config"]=0
        print_cycle()        
        print_notif()

      elif action==curses.KEY_F2 and not flags["account"]:
        flags["account"]=1
        for key,val in {key:0 for key,val in flags.iteritems() if key!="account"}.iteritems(): flags[key]=val
        print_cycle()
        print_account()
      elif action==curses.KEY_F2 and flags["account"]:
        flags["account"]=0
        print_cycle()
        print_notif()

      elif action==curses.KEY_F3 and flags["dms"]==0:
        flags["dms"]=1
        for key,val in {key:0 for key,val in flags.iteritems() if key!="dms"}.iteritems(): flags[key]=val
        print_cycle()
        print_dms()
      elif action==curses.KEY_F3 and flags["dms"]==1:
        flags["dms"]=0
        print_cycle()
        print_notif()

      elif action==curses.KEY_F10:
        tweets=[]
        for key,val in {key:0 for key,val in flags.iteritems() if key!=-1}.iteritems(): flags[key]=val
        std_cycle()
      elif action==curses.KEY_F11:
        exitp()
        exit()
      else:pass

      #After printing, refresh all screens
      refresh(screens)

  #If there is an error clear curses settings, print the exception and exit
  except:
    exitp()
    traceback.print_exc()
    exit()