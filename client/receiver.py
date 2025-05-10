import sys
import os
PROTOBUF_PATH = os.path.abspath("../../titans-vision/client/python")
sys.path.append(PROTOBUF_PATH)
import socket
import struct
import wrapper_pb2 as wr

class VisionReceiver:
    def __init__(self, group='224.5.23.2', port=10006, buffer_size=2048):
        self.group = group
        self.port = port
        self.buffer_size = buffer_size
        self.sock = self._setup_socket()

    def _setup_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', self.port))  
        mreq = struct.pack('4sl', socket.inet_aton(self.group), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        print(f"VisionReceiver :: Escutando {self.group}:{self.port}")
        return sock

    def receive_packet(self):
        data, addr = self.sock.recvfrom(self.buffer_size)
        msg = wr.SSL_WrapperPacket()
        msg.ParseFromString(data)
        return msg

    def run(self):
        while True:
            msg = self.receive_packet()
            if msg.HasField("detection"):
                print(f"Frame #{msg.detection.frame_number}")
                for ball in msg.detection.balls:
                    print(f"Bola em: ({ball.x:.2f}, {ball.y:.2f})")
                for robot in msg.detection.robots_blue:
                    print(f"Azul {robot.robot_id}: ({robot.x:.2f}, {robot.y:.2f})")
                for robot in msg.detection.robots_yellow:
                    print(f"Amarelo {robot.robot_id}: ({robot.x:.2f}, {robot.y:.2f})")