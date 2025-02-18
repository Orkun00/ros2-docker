#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoyCalculatorNode(Node):
    def __init__(self):
        super().__init__('rover_movement_calculation_node')
        # Subscribe to /joy topic
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10
        )
        self.get_logger().info("RoverMovementCalculation started. Subscribed to '/joy'.")

    def joy_callback(self, joy_msg):
        """
        Called every time a Joy message is received on /joy.
        Perform any calculations you want with axis/buttons here.
        """
        axes = joy_msg.axes     # e.g. left stick, right stick, triggers, etc.
        buttons = joy_msg.buttons  # button states (0 or 1)

        # Example: sum of all axis values
        axes_sum = sum(axes)

        # Example: which buttons are pressed?
        pressed_buttons = [i for i, val in enumerate(buttons) if val == 1]

        # Log or do further logic
        self.get_logger().info(f"Axes: {axes} (sum = {axes_sum})")
        self.get_logger().info(f"Buttons pressed: {pressed_buttons}")

def main(args=None):
    rclpy.init(args=args)
    node = JoyCalculatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
