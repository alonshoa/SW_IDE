import tkinter as tk
import pdb, sys
from scripts.breakable_textarea import BreakableTextarea # contains bta.text(text area holding the code), bta.breakpoints (set of breakpoints locations)  
from tkinter import messagebox

class MyDebugger:
   def __init__(self,app,text):
      self.app = app
      self.text = text
      self.breakpoints = set()
      self.current_line = 0
      self.code = ''
      self.debugger = pdb.Pdb()
      self.debugger.set_trace(sys._getframe().f_back)

   def continue_(self):
      self.debugger.set_continue()
      self.debugger.set_trace(sys._getframe().f_back)

   def step_over(self,event=None):
      self.debugger.set_step()
      self.debugger.set_trace(sys._getframe().f_back)

   def step_in(self,event=None):
      self.debugger.set_next(sys._getframe().f_back)
      self.debugger.set_trace(sys._getframe().f_back)

   def set_breakpoint(self,event=None):
      self.breakpoints.add(self.text.index(tk.INSERT))
      self.text.tag_add('breakpoint',self.text.index(tk.INSERT))

   def clear_breakpoint(self,event=None):
      self.breakpoints.remove(self.text.index(tk.INSERT))
      self.text.tag_remove('breakpoint',self.text.index(tk.INSERT))

   def clear_all_breakpoints(self,event=None):
      self.breakpoints.clear()
      self.text.tag_remove('breakpoint','1.0',tk.END)

   def run(self,event=None):
      self.code = self.text.get('1.0',tk.END)
      self.debugger.run('exec(self.code)')

   def run_file(self,event=None):
      self.code = self.text.get('1.0',tk.END)
      self.debugger.run(self.code)

   def set_trace(self,frame):
      self.current_line = frame.f_lineno
      self.text.tag_remove('current_line','1.0',tk.END)
      self.text.tag_add('current_line','{}.0'.format(self.current_line))
      self.text.see('{}.0'.format(self.current_line))
      if self.current_line in self.breakpoints:
         messagebox.showinfo('Breakpoint reached','Breakpoint reached at line {}'.format(self.current_line))
         self.debugger.set_trace(frame)

   def user_call(self,frame,argument_list):
      """This method is called when there is the remote possibility
      that we ever need to stop in this function."""
      if self.stop_here(frame):
         print("--Call--")
         self.interaction(frame, None)

   def user_line(self,frame):
      """This function is called when we stop or break at this line."""
      if self.stop_here(frame):
         print("--Line--")
         self.interaction(frame, None)

   def user_return(self,frame,return_value):
      """This function is called when a return trap is set here."""
      if self.stop_here(frame):
         print("--Return--")
         self.interaction(frame, None)

   def user_exception(self,frame,exc_info):
      """This function is called if an exception occurs,
      but only if we are to stop at or just below this level."""
      if self.stop_here(frame):
         print("--Exception--")
         self.interaction(frame, exc_info)

   def stop_here(self,frame):
      """This function returns True if we want to stop in this frame."""
      return True

   def interaction(self,frame,traceback):
      self.set_trace(frame)





if __name__ == '__main__':
    root = tk.Tk()
    bta = BreakableTextarea(root)
    bta.pack(fill=tk.BOTH, expand=True)
    debugger = MyDebugger(root,bta)
    text.bind('<F5>',debugger.run)
    text.bind('<F6>',debugger.run_file)
    text.bind('<F7>',debugger.set_breakpoint)
    text.bind('<F8>',debugger.clear_breakpoint)
    text.bind('<F9>',debugger.clear_all_breakpoints)
    text.bind('<F10>',debugger.step_over)
    text.bind('<F11>',debugger.step_in)
    text.bind('<F12>',debugger.continue_)
    root.mainloop()
