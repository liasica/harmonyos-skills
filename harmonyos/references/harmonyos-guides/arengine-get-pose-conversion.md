---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:11fbaec910f31f7520cc221637d8ae34298eda580b92ea630713ccc8b3ff2d6a
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/xsIbkeSXRW2ejENXaGRBzw/zh-cn_image_0000002817507147.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5DCB4F45B54BFBEA037EFEDEE7476176D12465DDA8F923098B9C67A0C03623A)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/dU2RQ07NSDmwM8umSAbWVA/zh-cn_image_0000002788307716.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAD3C2033AEC38307E0D36D27B755C17B3612DD34436790F4E4A4B6C2FA9A1A4)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Kimdl3ofQD2COG4rnT2Icg/zh-cn_image_0000002817427079.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=9462648BAEC040A5D2C0D9D005B594F283A0230F453FAB1A9D737318F17B3814)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/db0GSvf9Sx-0islprvOayA/zh-cn_image_0000002788467660.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFD6D0CE854BB417ADB935C2CFCA12EB517DF19A753ECD4BEF48034FDE4BF07D)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/v0Cp7md7SMGe7eyI_MGJdQ/zh-cn_image_0000002817507149.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BD8A63866B2CDBECAB203D232BB9A26A6468D99735E6C5F20F730E2E2A29DDE)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/jhp3YUuYTi6mjLXffpN9mA/zh-cn_image_0000002788307718.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=D196D2E2C0A441289A0987027DCE6B772B67E1F57251E1DDEF06C380B10A2F71)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/OeNLJqlVSgCqIV2VzSUJqA/zh-cn_image_0000002817427081.png?HW-CC-KV=V1&HW-CC-Date=20261114T004803Z&HW-CC-Expire=31536000000&HW-CC-Sign=D58F9B8C791BF5A912EFD3906121C00B315807E515FE6C333BC9D96785D1B488)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
