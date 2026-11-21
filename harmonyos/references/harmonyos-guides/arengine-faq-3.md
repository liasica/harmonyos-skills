---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb07d22add769fde2ec6fec33f7e17a183e718131ea058520ee6fe6820392510
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/_WcOTUNETR2FMb4P4hLSHw/zh-cn_image_0000002821757615.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011043Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3C070896F7E51411DC2720F4E9EEC4577F4C11F70B68F4E1305C118DA09FD6E)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/5orCTFCHTD6I7y1dWC8-Lw/zh-cn_image_0000002793037678.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011043Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8900F18BFE32236C45DFE9AAD85DAF0FF93C22BB827C48902D2283C9F22CF2A)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/of3A402sTWyLd8ic4hk5PA/zh-cn_image_0000002792877708.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011043Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFA193E86C5A98A1C96495E19A12A341747A5E3B33FB2D23A10DBF7EC082D891)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/_9kRmwDITR2LBIyvTfBjXw/zh-cn_image_0000002821837615.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011043Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDB9E9E09AD0AD2FEFB4831202DF56DB21B9DADFE80732BB8342DB9EC45F3CBA)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
