---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-intro
title: 布局说明
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 构建布局 > 布局说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d03a3b07bbfb22a8ac4b3213b88f2f3708569b8f20403bd51bb502fe10c32b66
---

设备的基准宽度为720px（px为逻辑像素，非物理像素），实际显示效果会根据实际屏幕宽度进行缩放。

其换算关系如下：

组件的width设为100px时，在宽度为720物理像素的屏幕上，实际显示为100物理像素；在宽度为1440物理像素的屏幕上，实际显示为200物理像素。

一个页面的基本元素包含标题区域、文本区域、图片区域等，每个基本元素内还可以包含多个子元素，开发者根据需求还可以添加按钮、开关、进度条等组件。在构建页面布局时，需要对每个基本元素思考以下几个问题：

* 该元素的尺寸和排列位置
* 是否有重叠的元素
* 是否需要设置对齐、内间距或者边界
* 是否包含子元素及其排列位置
* 是否需要容器组件及其类型

将页面中的元素分解之后再对每个基本元素按顺序实现，可以减少多层嵌套造成的视觉混乱和逻辑混乱，提高代码的可读性，方便对页面做后续的调整。以下图为例进行分解：

**图1** 页面布局分解

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/3gudWTHfRaClIKSH2-yMgQ/zh-cn_image_0000002558764572.png?HW-CC-KV=V1&HW-CC-Date=20260429T052842Z&HW-CC-Expire=86400&HW-CC-Sign=2C2DF5414DAD4D179C9625FCAD88DCF9EB4B2B2F99F77DF8B0B947B939B32456)

**图2** 留言区布局分解

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/FsDMapm0S0yUYY5xtX4CPw/zh-cn_image_0000002558604916.png?HW-CC-KV=V1&HW-CC-Date=20260429T052842Z&HW-CC-Expire=86400&HW-CC-Sign=BABA0F59F51255A530C2EA2E7D2BE866EB4366CC73965F188360D3E59971514E)
