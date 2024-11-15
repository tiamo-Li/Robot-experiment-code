# Robot-experiment-code

注意：

1. 模型文件中部分参数与老师要求不同，例如轮子厚度应为1.5cm，电机形状应为长方体~~（建模型的时候没细看，懒得改了）~~
2. 可以修改move_base包中的参数来改善导航效果
3. 不推荐按照老师的PPT实现，仅作为参数与流程参考即可，推荐参考文档：[Autolabor-ROS机器人入门课程《ROS理论与实践》零基础教程](http://www.autolabor.com.cn/book/ROSTutorials/)

在FAEP的复现过程中，使用WSL2来安装Ubuntu-18.04，需要注意的是：
在安装CUDA Toolkit时，一定要安装WSL版本的，否则CUDA会被覆盖，因为WSL2会直接将物理机中的CUDA映射到子系统中。