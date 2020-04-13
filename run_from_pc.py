
import time
import pathlib

import mp.micropythonshell

def measure_roundtrip(shell):
  MICROPYTHON_CODE = '''
import pyb
led = pyb.LED(1)
def toggle():
  led.toggle()
'''
  shell.MpFileExplorer.exec_(MICROPYTHON_CODE)
  start_s = time.time()
  COUNT = 1000
  for _i in range(COUNT):
    shell.MpFileExplorer.exec_('toggle()')
  duration_s = time.time() - start_s
  print(f'Roundtrip takes {duration_s/COUNT*1000:0.1f} ms')

if __name__ == "__main__":
  if True:
    shell = mp.micropythonshell.MicropythonShell()
    shell.sync_folder(directory_local='software')
    measure_roundtrip(shell)
    # shell.machine_reset()
    # shell.soft_reset()
    shell.repl()
    shell.close()
