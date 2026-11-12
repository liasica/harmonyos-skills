---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b83a29c253e95499f1e58a82ffce88a68ce011f4ae6b70242706183bd7f05bc2
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/9eGQC2osRQWKd5CCbz9JoA/zh-cn_image_0000002815559413.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A403985315F852F93A9D3D4872E6426E47B0DE7C253EB41CA737D64F0DE8BC3)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/fxbAR_nZQEufuPw-YFuo0w/zh-cn_image_0000002815399497.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=D21498A06D458476E5ABEFBB72CEC4248694C4EC141B6CC136249BB533B50934)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/6c1r2StJQ1quxJw5gm423w/zh-cn_image_0000002786519922.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3079226D1ECDFB73F3562FE2A49441F14B2E46BE15A3FBE0CEA9F199CA88908)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Cs0WreFJQpyeA7iOC94byw/zh-cn_image_0000002786359994.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A5ECAEED645A6B11103656EAF5268317135780C605A6D8D41D9048BA2ABCC47)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
