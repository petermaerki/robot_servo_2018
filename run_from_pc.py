
import pathlib

import mp.micropythonshell

if __name__ == "__main__":
  if True:
    shell = mp.micropythonshell.MicropythonShell()
    shell.sync_folder(directory_local='software')
    # shell.machine_reset()
    # shell.soft_reset()
    shell.repl()
    shell.close()
