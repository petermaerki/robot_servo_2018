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
    s('A', 0.0, pause, move='L')
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
    pause = 3000
    s('A,B,C,D,E,F,G,T,K,Z', 0.0, pause, move='L')
    s.move(pause)

  def aufrichten(): 
    pause = 300
    s.move()
    s('A', -0.2, pause, move='L')
    s('C', 0.7, pause, move='L')
    s.move()
    s('A', 0.3, 2000, move='L')
    s('C', 0.0, 2000, move='L')
    s('D', 0.7, 2000, move='L')
    s.move()
    s('D', 0.0, 2000, move='L')
    s('E', 0.7, 2000, move='L')
    s.move()

  def ablegen(): 
    s.move()

  def schwanzwackel(n=4): 
    pause = 300
    for i in range(n):
      s('T', 0.8, pause, move='S')
      s.move(pause)
      s('T', 0.5, pause, move='S')
      s.move(pause)


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
      s.move(ms = time_part * movetime_ms)


  def f_lift(foreward = True, wave_time_ms = 4000): # erster oder letzer Schritt bei F
    amplitude = 0.35
    part_time = 0.1
    if foreward: # F anheben
      s('G,E', amplitude, wave_time_ms * part_time, move='L')
      s('F', -2 * amplitude, wave_time_ms * part_time, move='L')
    else:
      s('G,F,E', 0.0, wave_time_ms * part_time, move='L') # am Schluss ablegen
    s.move(ms = wave_time_ms * part_time)

  def b_lift(foreward = True, wave_time_ms = 4000): # erster oder letzer Schritt bei F
    amplitude = 0.35
    part_time = 0.1
    if foreward == False: # B anheben
      s('A,C', amplitude, wave_time_ms * part_time, move='L')
      s('B', -2 * amplitude, wave_time_ms * part_time, move='L')
    else:
      s('A,B,C', 0.0, wave_time_ms * part_time, move='L') # am Schluss ablegen
    s.move(ms = wave_time_ms * part_time)

  def one_wave(foreward = True, wave_time_ms = 4000):
    string = 'ABCDEFG'
    if foreward:
      string = ''.join(reversed(string))
      f_lift(foreward, wave_time_ms)
    else:
      b_lift(foreward, wave_time_ms)
    steps = len(string)-3
    for i in range(steps):
      part = string[i:i+4]
      print(part)
      singlestep(part, movetime_ms = wave_time_ms / steps , first_step = (i==0))
    if foreward:
      b_lift(foreward, wave_time_ms)
    else:
      f_lift(foreward, wave_time_ms)

  def move(steps = 1, wave_time_ms = 4000, foreward = False):
    for i in range(steps):
      s('T', i%2 * 0.5 + 0.3, wave_time_ms * 0.8) # wave tail
      one_wave(foreward = foreward, wave_time_ms = wave_time_ms)

  #handorgel(0.3)
  #bogen(-0.3)
  #bogenbogen()
  

  # init_flach()
  # singlestep('BCDE')
  # singlestep('EDCB')

  
  import lib_commands


  #init_flach()
  #s('T', 0)
  #s.move()
  #s('T', 0.8, 10000, move='L')

  # move(steps = 3,  wave_time_ms = 3000, foreward = True)

  aufrichten()
  s.move(ms=1000) # etwas warten
  ablegen()
  # end_flach()
  #lib_commands.buzzer(3)
  #move(steps = 3,  wave_time_ms = 2000, foreward = False) # Vor oder zurueck bewegen: wave_time_ms minimal 4000, gemuetlich 10000
  #schwanzwackel(n=3)
  s.move(ms=1000) # etwas warten
  end_flach()

if __name__ == '__main__':
  s = lib_servo.Servos()
  initialize(s)
  run(s)
