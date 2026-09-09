---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:5c221edeba2af1adec19ba98cc6d1882edc574f588184a4254f391554615f6cf
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/iV5Wba5mSp--XsyBYou_jw/zh-cn_image_0000002717611470.png)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/deH4ELZlTFuKeFu-lQXiCQ/zh-cn_image_0000002747291421.png)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/vDxt5fTORsG_gXF47jqRfA/zh-cn_image_0000002747211339.png)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/4wcn7HbNTvOQ_84eIFbfEg/zh-cn_image_0000002717771404.png)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/BYAkNpBiTBS4RqghOTxZVg/zh-cn_image_0000002717611472.png)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/gYKqnf_kTbuV-YrDA76vsQ/zh-cn_image_0000002747291423.png)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/geKR3J4pT9OjZMYtEPDMZg/zh-cn_image_0000002747211341.png)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
