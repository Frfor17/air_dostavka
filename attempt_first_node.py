# attempt for first node for dron

import rclpy # connecting ros 2 stuff
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped # geometry stuff for 3D positions
from std_msgs.msg import String # simple string, for "orders" from shop, like for text

class DeliveryNode(Node):
    def __init__(self):
        super().__init__('delivery')
        self.order_sub = self.create_subscription(String, '/order', self.order_callback, 10)
        self.target_pub = self.create_publisher(PoseStamped, '/mavros/setpoint_position/local', 10)

    def order_callback(self, msg):
        # Парси заказ в pose (x,y,z к окну)
        pose = PoseStamped()
        pose.pose.position.x = 10.0  # пример
        self.target_pub.publish(pose)

rclpy.init()
node = DeliveryNode()
rclpy.spin(node)
