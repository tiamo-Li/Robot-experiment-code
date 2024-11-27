#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from std_srvs.srv import Empty
import subprocess

def explore():
    rospy.loginfo("Starting exploration...")
    explore_client = rospy.ServiceProxy('/explore/start', Empty)
    explore_client()
    rospy.loginfo("Exploration started.")

def return_to_initial_pose():
    rospy.loginfo("Returning to initial pose...")
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = 0.0  # 初始位姿的 x 坐标
    goal.target_pose.pose.position.y = 0.0  # 初始位姿的 y 坐标
    goal.target_pose.pose.orientation.w = 1.0  # 初始位姿的朝向

    client.send_goal(goal)
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo("Returned to initial pose successfully")
    else:
        rospy.loginfo("Failed to return to initial pose")

def save_map():
    rospy.loginfo("Saving map...")
    map_save_path = "/path/to/your/map_directory/map_name"  # 指定保存路径和文件名
    try:
        # 使用 map_server 的 map_saver 节点保存地图
        subprocess.call(['rosrun', 'map_server', 'map_saver', '-f', map_save_path])
        rospy.loginfo("Map saved successfully to %s" % map_save_path)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def main():
    rospy.init_node('main_controller', anonymous=True)
    explore()
    return_to_initial_pose()
    save_map()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass