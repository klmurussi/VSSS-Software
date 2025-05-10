from client.receiver import VisionReceiver
from controller.teste import Behaviour 
from firmware.sendData import SendData
import time

while True:
    vision = VisionReceiver() 
    data = vision.receive_packet()
    controller = Behaviour(data)
    strategy = controller.process()
    action = SendData(strategy)
    action.send()
    time.sleep(0.05)