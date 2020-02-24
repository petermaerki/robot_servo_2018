import lib_servo

import initialize_robot_servo_2018

def initialize(s):
  initialize_robot_servo_2018.initialize_serial1(s)

def run(s):
  def handorgel(winkel= 0.8): 
    s('A', 0.6, 1000, move='L')
    s('B,D,F', winkel, 3000, move='L')
    s('C,E', -winkel, 3000, move='L')
    s('G', -winkel/2.0-winkel/5.0, 3000, move='L')
    s.move()

  def bogen(winkel= -0.2): 
    s('B,C,D,E,F', winkel, 1000, move='L')
    s('A,G', 1, 1000, move='L')
    s.move()

  def bogenbogen(n=3): 
    s('A', 1, 1000, move='L')
    s('G', 1, 1000, move='L')
    for i in range(n):
      s('B,C,D,E,F', -0.1, 2000, move='L')
      s.move()
      s('B,C,D,E,F', -0.2, 2000, move='L')
      s.move()

  def init_flach(): 
    pause = 300
    s('A', 0.5, pause, move='L')
    s.move()
    s('B', 0.0, pause, move='L')
    s.move()
    s('C', 0.0, pause, move='L')
    s.move()
    s('D', 0.0, pause, move='L')
    s.move()
    s('E', 0.0, pause, move='L')
    s.move()
    s('F', 0.0, pause, move='L')
    s.move()
    s('G', 0.0, pause, move='L')
    s.move()
    s('T', 0.0, pause, move='L')
    s.move()
    s('K', 0.0, pause, move='L')
    s.move()
    s('Z', 0.0, pause, move='L')
    s.move()
    
  def end_flach(): 
    pause = 1000
    s('A', 0.5, pause, move='L')
    s('B,C,D,E,F,G,T,K,Z', 0.0, pause, move='L')
    s.move()

  def aufrichten(): 
    pause = 300
    s('A', 0.8, pause, move='L')
    s.move()
    s('C', 0.7, pause, move='L')
    s.move()
    s('A', 0.3, 2000, move='L')
    s('C', 0.0, 2000, move='L')
    s('D', 0.7, 2000, move='L')
    s.move()
    s('D', 0.0, 2000, move='L')
    s('E', 0.7, 2000, move='L')
    s.move()


  def nino(): 
    for i in range(5):
      pause = 2000
      s('T', 0.8, pause, move='S')
      s.move()
      s('T', 0.0, pause, move='S')
      s.move()
    s('T', -0.8, pause, move='L')
    s.move()
    s('Z', 1, pause, move='S')
    s.move()
    s('Z', 0, pause, move='S')
    s.move()


  def singlestep(axes = 'BCDE',  movetime_ms = 4000, first_step = False): #foreward = True,
    # time_part, argument, argument, argument, argument
    steptable = [(1.0/9.0,0.48125,-0.9625,0.48125,0),
                (1.0/9.0,0.56875,-0.91875,0.23625,0.1225),
                (1.0/9.0,0.60375,-0.83125,0,0.245),
                (1.0/9.0,0.56875,-0.67375,-0.2625,0.3675),
                (1.0/9.0,0.48125,-0.44625,-0.44625,0.48125),
                (1.0/9.0,0.3675,-0.2625,-0.67375,0.56875),
                (1.0/9.0,0.245,0,-0.83125,0.60375),
                (1.0/9.0,0.1225,0.23625,-0.91875,0.56875),
                (1.0/9.0,0,0.48125,-0.9625,0.48125)]
    if not first_step:
      steptable.pop(0) # remove first step
    # if not foreward:
    #   axes = axes[::-1]
    for row in steptable:
      time_part = row[0]
      arguments = row[1:]
      assert len(arguments) == len(axes)
      for i in range(len(axes)):
        s(axes[i], arguments[i], time_part * movetime_ms, move='L')
      s.move()

  def one_wave(foreward = True, wave_time_ms = 4000):
    string = 'BCDEFG'
    if foreward:
      string = ''.join(reversed(string))
    steps = len(string)-3
    for i in range(steps):
      part = string[i:i+4]
      print(part)
      singlestep(part, movetime_ms = wave_time_ms / steps , first_step = (i==0))
    s('B,C,D,E,F,G', 0.0, 1000, move='L')
    s.move()

  def move(steps = 1, wave_time_ms = 4000, foreward = True):
    for i in range(steps):
      one_wave(foreward = foreward, wave_time_ms = wave_time_ms)

  #handorgel(0.3)
  #bogen(-0.3)
  #bogenbogen()
  #aufrichten()

  # init_flach()
  # singlestep('BCDE')
  # singlestep('EDCB')
  # end_flach()
  
  init_flach()
  #one_wave(foreward = False)
  move(steps = 1,  wave_time_ms = 10000, foreward = True)
  s.move(ms=1000)
  move(steps = 3,  wave_time_ms = 3000, foreward = True)
  s.move(ms=1000)
  move(steps = 4,  wave_time_ms = 3000, foreward = False)
  end_flach()


if __name__ == '__main__':
  s = lib_servo.Servos()
  initialize(s)
  run(s)
