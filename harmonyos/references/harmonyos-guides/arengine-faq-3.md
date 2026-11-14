---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:297a918099647f923332b80c9be4c304323a9b052a6fa43c3283b6359151bf0c
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/WRzDlmC2Qi-61PO_ECAvCQ/zh-cn_image_0000002788467668.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004622Z&HW-CC-Expire=31536000000&HW-CC-Sign=977CD685855829EECE3B2ABF88D8C427031528CF1930DE3AB6207433A1A0180E)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/MDQyZebkTferlYI0GQRAWA/zh-cn_image_0000002817507157.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004622Z&HW-CC-Expire=31536000000&HW-CC-Sign=A78DFF20D2BF0218590333193EBC9AFBBC5282919E4E5F4FAA23C4C1FCE80379)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/No6zp8NfSgCe85X8BaDjqQ/zh-cn_image_0000002788307726.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004622Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8A4272CCCA5B874B150D8F2B0D0C2EDE555DF8CFF758687FE3C124DCC628D31)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/47MsuNn1TL63u0Sj0ZRbqw/zh-cn_image_0000002817427089.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004622Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ED8426D3D81FE266BA0560CC752E36B00C71CD3829E8CABCEEF1CA070BECC56)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
