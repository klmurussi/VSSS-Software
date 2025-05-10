class Behaviour:
    def __init__(self, data):
        self.data = data
        self.robots_blue = []
        self.robots_yellow = []
        self.ball = []

    def process(self):
        for robot in self.data['robots_blue']:
            self.robots_blue.append(robot)
        for robot in self.data['robots_yellow']:
            self.robots_yellow.append(robot)
        for ball in self.data['balls']:
            self.ball.append(ball)

        for robot in self.robots_blue:
            print(f"Azul {robot[0]}: ({robot[1]:.2f}, {robot[2]:.2f})")
        for robot in self.robots_yellow:
            print(f"Amarelo {robot[0]}: ({robot[1]:.2f}, {robot[2]:.2f})")
        for ball in self.ball:
            print(f"Bola em: ({ball[0]:.2f}, {ball[1]:.2f})")
        
        estrategia = {
            "robot_id": 0,
            "action": "move",
            "target": {
                "x": 0,
                "y": 0
            }
        }
        return estrategia