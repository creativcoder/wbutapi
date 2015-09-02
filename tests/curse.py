import curses

# init curses mode
def init_session():
	stdscr = curses.initscr()
	curses.noecho()		# no echoeing of keys back
	curses.cbreak() 	# reactive mode
	stdscr.keypad(1)   # enable keypad mode

	begin_x = 20
	begin_y = 7
	win = curses.newwin(300,300,begin_y,begin_x)
	win.refresh()

# exit curses mode
def exit_session():
	# restore all defaults
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

init_session()
exit_session()