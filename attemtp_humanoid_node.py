class WalkNode(Node):
    def order_callback(self, msg):  # "иди к двери"
        # MoveIt2 или gait planner генерит походку
        trajectory = JointTrajectory()
        trajectory.points = [  # 20 шагов
            {'left_hip': 0.3, 'left_knee': -0.5},  # шаг левой
            {'right_hip': -0.3, 'right_knee': -0.5} # шаг правой
        ]
        self.joints_pub.publish(trajectory)  # 10Гц
