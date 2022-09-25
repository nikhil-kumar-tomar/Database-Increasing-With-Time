import subprocess
import os, time
command='python "e:\Important Programs\Copying files from one folder to another.py"'
path_to_watch = "E:\Testing"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
    p = subprocess.Popen(f"{command}",shell=True, stdout=subprocess.PIPE)
  before = after
