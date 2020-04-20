import lib_servo
import initialize_robot_servo_2018

def initialize(s):
  initialize_robot_servo_2018.initialize_serial1(s)

def run(s):
  def handorgel(winkel= 0.8, movetime_ms = 2000): 
    s('A', -winkel, movetime_ms, move='S')
    s('B,D,F', winkel, movetime_ms, move='S')
    s('C,E', -winkel, movetime_ms, move='S')
    s('T', 0.5, movetime_ms/2, move='S')
    s('G', -winkel/2.0-winkel/5.0, movetime_ms, move='S')
    s.move()
    end_flach()

  def bogen(winkel= -0.3, movetime_ms = 4000): 
    s('B,C,D,E,F', winkel, movetime_ms, move='S')
    s('A', (-2.5 * winkel)-0.3, movetime_ms, move='S')
    s('G', -2 * winkel, movetime_ms, move='S')
    s.move(movetime_ms)

  def bogenbogen(n=3): 
    bogen(winkel= -0.3, movetime_ms = 2000)
    bogen(winkel= -0.2, movetime_ms = 1000)
    bogen(winkel= -0.3, movetime_ms = 1000)
    bogen(winkel= -0.2, movetime_ms = 1000)
    bogen(winkel= 0, movetime_ms = 1000)

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
    pause = 2000
    rechtwinkel = 0.72
    axes = 'BCDE'
    s('A', -0.5, pause, move='S')
    s('B', rechtwinkel, pause, move='S')
    s.move()
    for index in range(len(axes)-1):
        s(axes[index], 0, pause, move='S')
        s(axes[index+1], rechtwinkel, pause, move='S')
        s.move()

  def ablegen(): 
    pause = 2000
    rechtwinkel = 0.75
    axes = 'EDCB'
    for index in range(len(axes)-1):
        s(axes[index], 0, pause, move='S')
        s(axes[index+1], rechtwinkel, pause, move='S')
        s.move(ms=1500)
    s('A', 0, pause, move='S')
    s('B', 0, pause, move='S')
    s.move()

  def schwanzwackel(n=4): 
    pause = 300
    for i in range(n):
      s('T', 0.8, pause, move='S')
      s.move(pause)
      s('T', 0.5, pause, move='S')
      s.move(pause)

  def schwanzbeisser(): 
    aufrichten()
    s.move(ms=500) # etwas warten
    s('C', 0.6, 3000, move='S')
    s.move()
    s('Z', 1, 1000, move='S')
    s('T', 0.6, 3000, move='S')
    s.move()
    s.move(ms=500) # etwas warten
    for angle in (0.5,0.8, 0.4, 1):
      s('Z', angle, 500)
      s.move()
      if angle < 0.5:
        lib_commands.buzzer(1)
    s.move(ms=1000) # etwas warten
    s('T', 0.0, 2000, move='S')
    s('C', 0, 3000, move='S')
    s.move()
    s('Z', 0, 200)
    s.move()
    ablegen()


  def drehen(schritte = 2, rechts=True):
    s('B,C,D,E', -0.1, 2000, move='S')
    s('F', 1, 3000, move='S')
    s('T', -1, 3000, move='S')
    s('E', -0.2, 1000, move='S')
    s.move()
    faktor = -1
    if rechts:
      faktor = 1
    for i in range(schritte):
      s('K',  1*faktor, 1000, move='S')
      s.move()
      s('A', -0.5, 1000, move='S')
      s.move()
      s('K', -1*faktor, 1000, move='S')
      s.move()
      s('A', 0, 1000, move='S')
      s.move()
    s('K', 0, 1000, move='S')
    s.move()
    end_flach()

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


  def aufrichtKopfWaggel():
    aufrichten()
    s('A', -1, 3000, move='S')
    s('K', 1, 4000, move='S') # Kopf, links -1.0 rechts 1.0
    s('B,C', -0.2, 2000, move='S')
    s.move()
    for angle in [-1, 1, -1, 0]:
      s('K', angle, 1000, move='S') # Kopf, links -1.0 rechts 1.0
      s.move()
    s('A,B,C', 0, 4000, move='S')
    s.move(ms=2000)
    ablegen()

  def kuer(): 
    winkel= 0.3
    s('A', 0.1 - 0.5, 1000, move='S')
    s.move(600) # macht Bewegung nur halb fertig
    s('B', winkel, 1000, move='S')
    s.move(500) # macht Bewegung nur halb fertig
    s('C', winkel, 1500, move='S')
    s.move(700) # macht Bewegung nur halb fertig
    s('D', winkel, 2000, move='S')
    s.move(1500) # macht Bewegung nur halb fertig
    s('T', winkel, 1000, move='S')
    s.move(600) # macht Bewegung nur halb fertig
    s('G', 0.4, 1500, move='S')
    s.move(1000) # macht Bewegung nur halb fertig
    s('F', 0.2, 2000, move='S')
    s.move(1500) # macht Bewegung nur halb fertig
    s('E', 0.2, 2000, move='S')
    s.move(1500) # macht Bewegung nur halb fertig
    s('G', 0.3, 200, move='S')
    s.move()
    s.move(1000)
    s('A,B,C,D,E,F,G,T,K,Z', 0.0, 5000, move='S')
    s.move()


  import lib_commands

  #handorgel(0.8)
  #init_flach()
  #s('T', 0)
  #s.move()
  #s('T', 0.8, 10000, move='L')
  #aufrichten()
  #s.move(ms=2000) # etwas warten
  #ablegen()

  #lib_commands.buzzer(3)
  #move(steps = 3,  wave_time_ms = 10000, foreward = True) # Vor oder zurueck bewegen: wave_time_ms minimal 4000, gemuetlich 10000
  #schwanzwackel(n=3)
  #schwanzbeisser()
  #bogenbogen()
  #aufrichtKopfWaggel()
  #drehen(schritte=5, rechts=False) # 5 Schritte entsprechend 90 Grad
  #bogenbogen()


  aufrichtKopfWaggel()

  s.move(ms=5000) # etwas warten
  end_flach()

if __name__ == '__main__':
  s = lib_servo.Servos()
  initialize(s)
  run(s)
