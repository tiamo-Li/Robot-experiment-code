#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

ros::Publisher pub;
double scale_linear;
double scale_angular;

void velocityCallback(const geometry_msgs::Twist::ConstPtr& msg)
{
    // 输出接收到的原始消息
    ROS_INFO("接收: linear velocity [%.2f], angular velocity [%.2f]", msg->linear.x, msg->angular.z);

    // 进行按比例缩小转换
    geometry_msgs::Twist scaled_msg;
    scaled_msg.linear.x = msg->linear.x * scale_linear;
    scaled_msg.angular.z = msg->angular.z * scale_angular;

    // 输出转换后的消息
    ROS_INFO("转换: linear velocity [%.2f], angular velocity [%.2f]", scaled_msg.linear.x, scaled_msg.angular.z);

    // 发布转换后的消息
    pub.publish(scaled_msg);
}

int main(int argc, char** argv)
{
    setlocale(LC_ALL, "");
    ros::init(argc, argv, "converter");

    ros::NodeHandle nh;

    // 设置缩放比例
    scale_linear = 0.5;
    scale_angular = 0.5;

    // 定义发布者和订阅者
    pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel_cov", 10);
    ros::Subscriber sub = nh.subscribe("/cmd_vel", 10, velocityCallback);

    ros::spin();
    return 0;
}