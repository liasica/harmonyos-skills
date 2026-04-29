---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-4
title: 某些特殊场景下（如附近存在磁场干扰、手机发烫或扫描到重复纹理等），出现平面漂移或者位姿数据跳变现象
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 某些特殊场景下（如附近存在磁场干扰、手机发烫或扫描到重复纹理等），出现平面漂移或者位姿数据跳变现象
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:715254ff6881f6e323d3e9361d4c91b853947998732fd440f20a808babb81bc5
---

## 现象描述

某些特殊场景下，如使用环境附近存在强磁场，手机处于高负载场景下（后台开启很多应用或长时间使用导致手机发烫），或者扫描到重复纹理（见下图）时，可能出现识别到的平面无法锚定到现实世界中，或者通过[HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose)接口获取的位姿信息出现大幅度跳变等现象。

**图1** 重复纹理的地板

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/6-DBUP2lTi2f1WvVOpIuww/zh-cn_image_0000002558605472.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053601Z&HW-CC-Expire=86400&HW-CC-Sign=26C2C72E3DB5DCD342974327D0DD1D73DE286A152FE13EE3886E242CB8D6732C)

## 可能原因

AR Engine通过获取到的加速度计传感器和磁力计传感器的信息进行平面计算和相机位姿计算，上述特殊场景下，系统传感器数据可能会存在异常，从而导致平面漂移或者位姿跳变的现象发生。

## 处理步骤

建议应用对通过[HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose)接口获取到的位姿数据，按照实际应用使用场景进行滤波，如步行导航场景，应用可以缓存多帧数据，通过多帧数据可以计算得到运动速度，如果检测到此速度明显高于步行速度，证明此时AR数据已经不可信，可以丢弃此数据或者重启AR算法。

说明

**计算运动速度**：x,y,z为在t时刻的位姿数据的位移量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/D9TAwtY-Rym7JQ_zhOhFGQ/zh-cn_image_0000002589324999.png?HW-CC-KV=V1&HW-CC-Date=20260429T053601Z&HW-CC-Expire=86400&HW-CC-Sign=453811B67F28DE3211F774B07245C5318FEA6FEAC7C1BEC5A1088ADE4A518BD1)
