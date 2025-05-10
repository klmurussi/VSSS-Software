from client.receiver import VisionReceiver as vision
from controller.teste import Behaviour as controller
from firmware.sendData import sendData as act
import time

while True:
    data = vision.receive_packet()
    c = controller(data)
    strategy = c.process()
    action = act(strategy)
    action.send()
    time.sleep(0.05)