---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:48+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2b6404cbf4faa93413a29aca4f5d91994b9629a7048d8699a244ce23101b31fc
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/bXnqxCCGTgGYvmUs0iVRyQ/zh-cn_image_0000002776749576.png)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/g2UEdt_7T6WY6i7Y7Xl5oA/zh-cn_image_0000002806029293.png)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Zkny7O-wSgqpck6SrM6pxg/zh-cn_image_0000002806109183.png)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/p9fXzHjrR5-xuqEstahVLg/zh-cn_image_0000002776909564.png)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/-_mQxrljRBmyZxCAPTX2PQ/zh-cn_image_0000002776749578.png)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/E4I3CLDnQeyhS0SuL1eWQA/zh-cn_image_0000002806029295.png)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Qi0VQMfhQXy1nkBnTPc0KQ/zh-cn_image_0000002806109185.png)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
