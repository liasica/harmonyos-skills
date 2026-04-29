---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:704372b1e71c3f5a6df1b007cba457ca410211b924556537055d6a1e0e29b4ed
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/2O0zaZq0SjOVgNP6QNdOsQ/zh-cn_image_0000002558605470.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053600Z&HW-CC-Expire=86400&HW-CC-Sign=3499A2D2FA21E825905A77FE642330E81001F58E684906EE466DEFA487C3A77E)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/I79CR9CPRHm0Do35HzISQQ/zh-cn_image_0000002589324997.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053600Z&HW-CC-Expire=86400&HW-CC-Sign=2ABF0532B8B79970032599396FB3CDEF398A411BE5914EF030C06044E752CB46)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/d5OX5br4TnisKmWmez6Gew/zh-cn_image_0000002589244933.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053600Z&HW-CC-Expire=86400&HW-CC-Sign=3F87D466BCCEE5B3F37006ACB1B4D78C745C2D564A242B8F3AAE04B0B0D457E6)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/gc_BEpfMSoiC8a-sZycq5Q/zh-cn_image_0000002558765128.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053600Z&HW-CC-Expire=86400&HW-CC-Sign=59BD990EDD6037DD4E9384D5E2AB1505A05053F94A010CB377D716A27BA2A569)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
