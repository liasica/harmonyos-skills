---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:51+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0264cc5492db08af9de6e93677a8f94e1d7d259346cc59e51e72670302b9c1ed
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/HqXnpFxuSgS0miemaqHFdQ/zh-cn_image_0000002552798968.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=2D7EE34C15F4F55C8602CD6562B9CE6FA8ABDB31E47F6A4C54DB862496EEE534)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/7LRAOcCyRDmNVYMZfp4Zfw/zh-cn_image_0000002583438663.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=DDD713AD5FC6EFE5CF03DEC7C56D99BF02BA19172825548DABB7F43A2FBC1DA3)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/oOaDnTW2QnGn__zfO63vcA/zh-cn_image_0000002552958618.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=DB890521B926E13904910D02F60A041E9B436755239DEB2B4A2169784875B6B6)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/uEH9gvl1Rrmzig_XFDvPSw/zh-cn_image_0000002583478619.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=50D902CFC53A097D151D83FD427134BA5132572C3A88C5C4FE6D06FA73AF91EC)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/hgwBAX-XQtSC0aNRa7lQ6A/zh-cn_image_0000002552798970.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=DE5A066F0DF96B4774035120DFE2D8CC5C2C6A63FE27AB1B888165282739C8B9)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/ceqUioB-ScSs2nPXC-NwBw/zh-cn_image_0000002583438665.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=BFDF9F38C80C528E3BCD3BF170B6A52C69C236AC11F328A1C306239D8FA849D8)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/-dHeYnTuR5Sxbi4MciNvJw/zh-cn_image_0000002552958620.png?HW-CC-KV=V1&HW-CC-Date=20260427T234649Z&HW-CC-Expire=86400&HW-CC-Sign=AEFD8D9E64B4E1A891D8A3151605095C2795C4F807FFC4703EE622443A5F8E2F)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
