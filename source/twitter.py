#! /usr/bin/env python

import curses

def init():
  """
  Initializes the curses environment. Returns the environment variable
  """

  scr=curses.initscr()
  curses.noecho()
  curses.cbreak()
  scr.keypad(1)
  return scr

def exitp():
  """
  Deactivates curses options and terminates program
  """

  curses.nocbreak()
  curses.echo()
  scr.keypad(0)
  curses.endwin()
  exit()

if __name__=="__main__":
  try:
    scr=init()
    scr.addstr(0,0,"PATATATEST",curses.A_BLINK)
    screen1=curses.newwin(10,10,5,5)
    screen1.refresh()
    scr.refresh()
    scr.getch()
    exitp()
  except:
    exitp()