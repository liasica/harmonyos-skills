---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-33
title: 如何解决自定义样式地图国境线不可见的问题
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何解决自定义样式地图国境线不可见的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:89440d1f708fc1afa1043e4f9b8619b965ce70fdad03704b73c5e8ade9622148
---

## 问题现象

使用Petal Maps Studio的Night模式预览时有国境线，发布后作为自定义地图在真机上运行，缩小至能见全国时，没有国境线，即肉眼不可见。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/y9bHB6zwRHWnN5r9XELzPQ/zh-cn_image_0000002658793633.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/MvrJ-UUaQ4mlTS3EBZNHKA/zh-cn_image_0000002628554266.png "点击放大")

## 解决方案

浏览器中打开[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)，进入Night模式，在左侧目录找到Administrative>Country>Geometry>stroke>color，点击色板修改颜色，建议设置明亮的颜色。发布后在真机上验证，即可看见国境线。

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/55LFRNdFSv6lUrO_WGH9nw/zh-cn_image_0000002658913587.png "点击放大")
