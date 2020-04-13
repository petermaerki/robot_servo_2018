import lib_servo
import lib_commands

# Initialize the hardware
objServos = lib_servo.Servos()
lib_commands.objServos = objServos

# Select a choreo
import choreo_peter as current_choreo
# import choreo_hans as current_choreo

# Register the commands - they may be called from 'repl'
start = lib_commands.Start()
stop = lib_commands.Stop()
status = lib_commands.Status()
c = choreo = lib_commands.Choreo(current_choreo)
servo = lib_commands.Servo()
s = lib_commands.Servo()
servos = lib_commands.Servos()
h = lib_commands.Help()

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
t = 't'
z = 'z'
k = 'k'

# example used fom repl, shows examples:
# h

# Start the choreo
if True:
  current_choreo.initialize(objServos)
  current_choreo.run(objServos)

