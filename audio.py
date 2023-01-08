import time #unused [implement if needed delays, add "time.sleep(0.1)"]
from sense_hat import SenseHat
from pygame import mixer

sense = SenseHat()

#pulling audio file [works sometimes :( ]
mixer.init()
mixer.music.load('filename.mp3')
mixer.music.play(-1)

sense.clear(0, 0, 0)

while True:
  spectrum = mixer.music.get_volume() #multiply by ~7 to zoom in or zoom out audio spectrum
  
  sense.clear(0, 0, 0)

  for i in range(8):
    sense.set_pixel(i, 7, (spectrum, 0, 0))
    
#bhagwan ke naame pe kaam karna, nariyal chadhaunga
