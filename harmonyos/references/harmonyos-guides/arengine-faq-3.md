---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:397cac97293ee9d4214242e85ae1b81af4b6d98a24825922bcf0d60c01945a4b
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ifCZUttvRGSN_gluZHhj2g/zh-cn_image_0000002583478627.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234658Z&HW-CC-Expire=86400&HW-CC-Sign=DEDFE91E272D0389D3C77A183012B895235BBDC74E95D2F3EB82B36A0DDA7D74)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/f5jQLEUSTb2kM0mv3dxAQg/zh-cn_image_0000002552798978.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234658Z&HW-CC-Expire=86400&HW-CC-Sign=8F4E8BC819E0545CBC5650561FB48173F7CE6B00FA6E7D8309DCD1140B0B4482)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/RkB3U0gSRBe3Wif2o27u-Q/zh-cn_image_0000002583438673.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234658Z&HW-CC-Expire=86400&HW-CC-Sign=A35516D1A1A116A9BCA00B7A50E06EB09D956261744C826AF3FEDE317D3BCEAA)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/NyIr29woTma2CdMK0IY3VA/zh-cn_image_0000002552958628.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234658Z&HW-CC-Expire=86400&HW-CC-Sign=6E091785D6B4ABBE911E6E8AC7EAE23BFD89CC84860B2423F853881DBB466D89)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
