---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose-conversion
title: 运动跟踪介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 运动跟踪介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:59d2acbd7d9317d70be1c50fa07dff5c3eca17eb80dbc3cddace47e8b6644bdd
---

AR Engine通过获取终端设备摄像头数据，结合图像特征和惯性传感器（IMU），计算设备位置（沿x、y、z轴方向位移）和姿态（绕x、y、z轴旋转），实现6自由度（6DoF）运动跟踪能力。

设备位姿描述了物体在真实世界中的位置和朝向。通过AR Engine，开发者可以实时获取设备在空间中任意时刻的位姿。

**图1** 6DoF运动跟踪能力示意图（红色线代表设备运动方向）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/J85Mcl0KRKSYaFCrB3bF6w/zh-cn_image_0000002589324987.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=3C010B02AF1FDF60E282745E0D1B31CC137A858920DE50661D8DE1121B05A45D)

## 世界坐标系与位姿示意

设备位姿一般在世界坐标系下进行表示。世界坐标系描述了真实物理空间中物体的绝对位置，其正方向如图2所示。

**图2** 世界坐标系示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/9FB2MEEoQI-PEHDeVPYj7Q/zh-cn_image_0000002589244923.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=18C7742BEB0A438782BC29FE24F3FC9314BA7FDF988B3E266E1C561A560ED636)

AR Engine会自动完成世界坐标系初始化。

在AR Engine中，设备位姿由一个7维向量描述，包括旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Oy8KQOExQvOUybv3NxmsZg/zh-cn_image_0000002558765118.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=35BBACF2FDCA1989829AB903A9B977D29CE5B76C16067B29F3D281D4809CABBC)和位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/2QcXABYcTqitZnt6yfz66A/zh-cn_image_0000002558605462.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=619B06E09C9A631E1FA509AAF925216E06158BEA1C82FE297BC66E8D991AE555)。其中旋转量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/z0Dd3Wc6TciEfSoGvTDyfA/zh-cn_image_0000002589324989.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=5BA55D50A7F85E6C6E72C472042D061AAB668218770B29620A8A5FD229A1A107)是一组四元数，描述了设备相对于坐标原点的旋转状态；位移量![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/KJLAOaRrS8OXPLMnEvHL4g/zh-cn_image_0000002589244925.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=0848C83DA2866653841013ECEC38CFB5294DFAAD8AE341767066260A7FE37044)是一组三维向量，描述了设备相对于坐标原点的平移状态，如下图所示。

**图3** 设备位姿的旋转和平移变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/XhOAanGZRletDCSXusXhuQ/zh-cn_image_0000002558765120.png?HW-CC-KV=V1&HW-CC-Date=20260429T053549Z&HW-CC-Expire=86400&HW-CC-Sign=37B15B1B982DB4E540599F24F2D572D0AED0A5A536FD1BFCF4BAF6BB87C0AA45)

通过旋转分量和平移分量，可以描述设备在空间中任意时刻的位姿状态。
