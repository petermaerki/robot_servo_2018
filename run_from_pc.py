import os
import re
import pathlib

import mp
import mp.mpfshell

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).absolute().parent

class RobotRunner:
  def __init__(self, str_port):
    if re.match(r'^COM\d+$', str_port) is None:
      raise Exception('Expected a string like "COM5", but got "{}"'.format(str_port))
    self.str_port = str_port
    str_port2 = 'ser:' + self.str_port

    self.fs = mp.mpfshell.MpFileShell(color=False, caching=False, reset=True)
    self.fs.do_open(args=str_port2)

  @property
  def is_connected(self):
    return self.fs.fe is not None

  def upload_files(self, directory):
    assert self.is_connected
    filename_timestamp = DIRECTORY_OF_THIS_FILE.joinpath(f'{directory}/timestamp_{self.str_port}.tmp')
    timestamp_last_replication = 0.0
    if filename_timestamp.exists():
      timestamp_last_replication = filename_timestamp.lstat().st_mtime
    for filename in DIRECTORY_OF_THIS_FILE.joinpath(directory).glob('*.py'):
      msg = f'  download "{directory}/{filename.name}"'
      if filename.lstat().st_mtime < timestamp_last_replication:
        print(f'{msg}: SKIPPED(not edited)')
        continue
      print(msg)
      self.fs.fe.put(src=filename.absolute(), dst=filename.name)
      filename_timestamp.touch()

  def soft_reset(self):
    assert self.is_connected
    self.fs.fe.con.write(b"\x04")  # ctrl-D: soft reset

  def machine_reset(self):
    assert self.is_connected
    self.fs.fe.exec_('import machine')
    self.fs.fe.exec_('machine.reset()')

  def repl(self):
    assert self.is_connected
    self.fs.do_repl(args=None)

  def close(self):
    assert self.is_connected
    self.fs.do_close(args=None)

if __name__ == "__main__":
  if True:
    r = RobotRunner(str_port='COM9')
    r.upload_files(directory='software')
    # r.machine_reset()
    r.soft_reset()
    r.repl()
    r.close()
