---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:43+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1ee34aee86e4de1357e265ef55b478ad694b69bd99a0e87a629857778b23d0ba
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/A-SR7i6YTLagF7cmnEgq0g/zh-cn_image_0000002820525997.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C7795BD5815AEF817732421BCA7BB1905D34735539A14346FC5DB5550E426CF)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/W-pddqxCS4uO1ob1YsjpfQ/zh-cn_image_0000002820405997.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D11F32C3C944C5F4C88ABFEBF3223884BA7677A08D0405BC5DFC7970DFD9A61)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/fyUZWQZJSMe-CJeGxqIugw/zh-cn_image_0000002791726018.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=37CF12F3B341CB81B7AF69C0A5F590EF964E372F2CE835E79DA8CBB2D8A334B4)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/tO_wP1lbTGqewclctnTy9g/zh-cn_image_0000002791566046.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=572F5F70529D9C59F8DF606172DF54475ED67920FC822B70D13BE887E80AD9CF)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/oiEcvbOQQsWBZSWoI5F_rw/zh-cn_image_0000002820525999.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=A21C49B730FCA57618CECE9BF8FA82984474549DA7C632679ACF675A6485FEC8)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/UaG4XZ2cT12s9d6CViVdEg/zh-cn_image_0000002820405999.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=23F0FDB7BE5C6D0AB3124B47E7FD4891D5A28EC7664D30D186DD120E2309966D)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/xgr19Q-YSIWr9ypDvAfkfw/zh-cn_image_0000002791726020.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA430D78A0BF0570B991DB9C4314CF41C0667FD9CE45BB1747046DA22E31E752)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
