---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-3
title: 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > AR Engine常见问题 > 反光、光线暗或者弱纹理场景（输入图像颜色变化小）下无法识别平面
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6d84a28f54f958487c679925a42def21a9775b04e30352852959790bcb139f6
---

## 现象描述

使用环境跟踪能力时，如果输入图像中有反光、光线暗、有弱纹理（输入图像颜色变化小），识别到的点云数量会变少甚至没有，出平面时间也会变长或无法生成平面。

1. 反光：镜面，光滑的大理石地板等

   **图1** 镜面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/nVlLTsdpTyuxme-yKC1oow/zh-cn_image_0000002791566054.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014751Z&HW-CC-Expire=31536000000&HW-CC-Sign=256A82D3EF560DE62DB3DEF7E0B65D2AF8F539A9C0558E58A7680DD25F8019FD)
2. 光线暗：夜晚的路面或摄像头遮挡等。

   **图2** 夜晚的路面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/g9os6R5WRlOvrJsIeou30w/zh-cn_image_0000002820526007.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014751Z&HW-CC-Expire=31536000000&HW-CC-Sign=693846F56DF9127E001853446FDB9EFE2D79641D1127E2F13299C9B19B2B2227)
3. 弱纹理：如单色柜子、单色桌面和墙面等。

   **图3** 墙面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/aFQxPVTdQ9iadUPkn5EDgQ/zh-cn_image_0000002820406007.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014751Z&HW-CC-Expire=31536000000&HW-CC-Sign=A82B6B6D67ADE6853B0730F7AF07D015EAEE62433C6C14E35ACEB28D5B2618B6)

   **图4** 纯色的桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/rF9YqA4IR3e5qA0K9LXT-w/zh-cn_image_0000002791726028.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014751Z&HW-CC-Expire=31536000000&HW-CC-Sign=C79DE653782F97A20170E5F02FA293C915BE6420344D60EEE712BC9630A42EF0)

## 可能原因

AR Engine通过输入的图像数据进行平面上特征点的计算，如果输入图像数据中存在反光、光线暗和弱纹理，AR Engine计算后只能得到很少的点，而平面根据识别到的点云生成，因此会导致平面出现缓慢或无法出现的现象。

## 处理步骤

建议应用在持续无法获取点云或平面数据时，提示用户移动相机，避免画面中持续出现反光、光线暗或弱纹理。
