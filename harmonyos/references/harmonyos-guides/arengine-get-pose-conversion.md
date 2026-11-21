---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:09+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:70fce15bf2eaa3e1210406a4e745afb92b34947ca6f25a1238e2473145c6abb1
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/rzi4JFkUTUiyD0mVvMVCYA/zh-cn_image_0000002793037668.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E6DC55ECF65543199EC42DE05392AE344A3076F977DA2E746545D639660206C)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/ojXipghcSSOryYm5OW1kAw/zh-cn_image_0000002792877698.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=35036D398BFF90A962AB41C90A70614D892EA91D8603FA2015208B38A7D44957)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/wpMaKfTaT-aEe8rEdc67Vg/zh-cn_image_0000002821837605.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D41837C39BEE0CF8877822E221BD6071024BDE8DE529DB475C489C0ADD9B3BE)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/7qkCRui6QHmlGls0uoEtsA/zh-cn_image_0000002821757607.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=06B8720305607B10A9BFA491C13D09247440BB88D45FD355DB1B49330818F504)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/RMbOXhd2QOKiYcOPa9Ta2Q/zh-cn_image_0000002793037670.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=FED346E160B2EA967E5404A943364B1C90D731B91A5CD8F2B9004BE38FD7007D)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/0xU3Yv2gR9GXxDIUyof0ZA/zh-cn_image_0000002792877700.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=66DF865E95B34AE85E10B72E2CB25618466BBA5616B705CFEED07FC2EB30DE50)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/6UVWc_H4RNe3-3V-zRAa-g/zh-cn_image_0000002821837607.png?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=F98FAAD63382A6D3656102F31B5F072EAAA1029C07B0C922AC4E6943C37B80E0)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
