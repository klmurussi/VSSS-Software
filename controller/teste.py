class Behaviour:
    def __init__(self, data):
        self.data = data
        self.robots_blue = []
        self.robots_yellow = []
        self.ball = []

    def process(self):
        for robot in self.data.robots_blue:
            self.robots_blue.append(robot)
        for robot in self.data.robots_yellow:
            self.robots_yellow.append(robot)
        for ball in self.data.balls:
            self.ball.append(ball)

        for robot in self.robots_blue:
            print (f"Azul {robot.robot_id}: ({robot.x:.2f}, {robot.y:.2f})")
        for robot in self.robots_yellow:
            print (f"Amarelo {robot.robot_id}: ({robot.x:.2f}, {robot.y:.2f})")
        for ball in self.ball:
            print (f"Bola em: ({ball.x:.2f}, {ball.y:.2f})")
        
        estrategia = {
            "robot_id": 0,
            "action": "move",
            "target": {
                "x": 0,
                "y": 0
            }
        }
        return estrategia
        
    