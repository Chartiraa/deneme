import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class PublisherNode(Node):

    def __init__(self):
        super().__init__('Life_Sensor_Publisher')
        self.publisher_temperature = self.create_publisher(String, 'temperature', 10)
        self.publisher_humidity = self.create_publisher(String, 'humidity', 10)
        self.publisher_battery = self.create_publisher(String, 'battery', 10)
        timer_period = 1  # saniye
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        temperature = random.randint(0, 100)
        humidity = random.randint(0, 100)
        battery = random.randint(0, 100)

        # Publish temperature
        msg_temperature = String()
        msg_temperature.data = str(temperature)
        self.publisher_temperature.publish(msg_temperature)
        self.get_logger().info('Temperature: "%s"' % msg_temperature.data)

        # Publish humidity
        msg_humidity = String()
        msg_humidity.data = str(humidity)
        self.publisher_humidity.publish(msg_humidity)
        self.get_logger().info('Humidity: "%s"' % msg_humidity.data)

        # Publish battery
        msg_battery = String()
        msg_battery.data = str(battery)
        self.publisher_battery.publish(msg_battery)
        self.get_logger().info('Battery: "%s"' % msg_battery.data)

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
