import pyb
import micropython
import time
import lib_servo

STATE_STOPPED = 'stopped'
STATE_RUNNING = 'running'
STATE_ERROR = 'error'

class State:
  def __init__(self):
    self.strState = STATE_STOPPED
    self.listErrorMessages = []

  def status(self):
    print('state=%s' % self.strState)
    print('error messages:')
    for strErrorMessage in self.listErrorMessages:
      print('  ' + strErrorMessage)

objState = State()

timer1 = pyb.Timer(1)
button1 = pyb.Switch()

objServos = lib_servo.Servos()

buzzer_pin = pyb.Pin('Y1', pyb.Pin.OUT_PP)
def buzzer(n=1):
  for i in range(2*n):
    buzzer_pin.value(not(i%2))
    time.sleep(0.1)

#buzzer(1)

def schedule_timer1(iDummy4712):
  pyb.LED(1).toggle()

def schedule_button(iDummy4712):
  pyb.LED(2).toggle()
  objState.listErrorMessages.append('Fehler!')
  if len(objState.listErrorMessages) > 5:
    print('Hallo')

class Servo:
  def __repr__(self):
    return 'servo(strName, fPosition) fPosition: -1.0 ... 1.0'

  def __call__(self, strName, fPosition):
    objServos.setPosition(strName, fPosition)
    print('done')

class Servos:
  def __repr__(self):
    return objServos.getNamen()

  def __call__(self, strName, fPosition):
    return self.__repr__()

class Choreo:
  def __repr__(self):
    objServos.resetTime()
    import choreo_a
    choreo_a.run(objServos)
    return ''

  def __call__(self, strName, fPosition):
    return self.__repr__()

class Start:
  def __repr__(self):
    # See: 
    micropython.alloc_emergency_exception_buf(100)
    objState.strState = STATE_RUNNING
    objState.listErrorMessages = []
    timer1.init(freq=0.5)  # 0.5 Hz
    timer1.callback(lambda objTimer: micropython.schedule(schedule_timer1, 4712))
    button1.callback(lambda: micropython.schedule(schedule_button, 4712))
    return ''

  def __call__(self):
    return self.__repr__()

class Stop:
  def __repr__(self):
    objState.strState = STATE_STOPPED
    timer1.deinit()
    timer1.callback(None)
    button1.callback(None)
    status()
    return ''

  def __call__(self):
    return self.__repr__()

class Status:
  def __repr__(self):
    return objState.status()

  def __call__(self):
    return self.__repr__()

class Help:
  def __repr__(self):
    print('Commands:')
    print('  start')
    print('  stop')
    print('  status')
    print('  choreo')
    print('  servo(strName, fPosition) fPosition: -1.0 ... 1.0')
    print('  servos  Listet die vorhandenen Servos auf.')
    print('  h()')
    return ''

  def __call__(self):
    return self.__repr__()

class X:
  def __repr__(self):
    return

  def __call__(self):
    return self.__repr__()


start = Start()
stop = Stop()
status = Status()
choreo = Choreo()
c = choreo
servo = Servo()
servos = Servos()
h = Help()
s=objServos

import choreo_peter as choooreo
choooreo.initialize_servos(objServos)
choooreo.run(objServos)
print('loaded...')
#print(choreo)

