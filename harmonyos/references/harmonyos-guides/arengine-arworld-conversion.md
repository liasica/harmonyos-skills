---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arworld-conversion
title: 命中检测介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 命中检测 > 命中检测介绍
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:09+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:eed764630f5a45be88c93cbed0466e83f33e988365f33b190b716e705645892d
---

AR Engine通过命中检测（Hit Testing）技术，将终端设备屏幕上的兴趣点映射为现实环境中的兴趣点。命中检测以现实环境中的兴趣点为源，发出一条射线连接到摄像头所在位置，返回射线与平面、稀疏点云、Mesh的交点。

用户可以在平面上放置虚拟物体，实现虚拟和现实的融合。

通过命中检测能力，用户可以点击终端设备屏幕，在现实世界中放置虚拟物体，用于虚拟家具试用等，实现虚拟与现实世界融合。

**图1** 命中检测示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/nBHJks8rTP6_qMU439-_3Q/zh-cn_image_0000002793037672.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011208Z&HW-CC-Expire=31536000000&HW-CC-Sign=A54000DC7CCD76D33541E921AC3CC3B8D6EF477F2EAF1580ECF25C2901CBDE23)
