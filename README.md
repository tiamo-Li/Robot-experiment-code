# Robot-experiment-code

注意：

1. 模型文件中部分参数与老师要求不同，例如轮子厚度应为1.5cm，电机形状应为长方体~~（建模型的时候没细看，懒得改了）~~
2. 可以修改move_base包中的参数来改善导航效果
3. 不推荐按照老师的PPT实现，仅作为参数与流程参考即可，推荐参考文档：[Autolabor-ROS机器人入门课程《ROS理论与实践》零基础教程](http://www.autolabor.com.cn/book/ROSTutorials/)

在FAEP的复现过程中，使用WSL2来安装Ubuntu-18.04，需要注意的是：
在安装CUDA Toolkit时，一定要安装WSL版本的，否则CUDA会被覆盖，因为WSL2会直接将物理机中的CUDA映射到子系统中。

更新：

重写了FAEP的复现步骤，并添加了对照实验FUEL的实现方法，并改为使用Ubuntu20.04来实现。

如果不想改，可以直接跳到步骤3.3，并且不需要对Cmake配置文件做过多的修改。

另外那两个对照方法最新也只能跑在ROS Kinetic上，要想做只能上双系统了