---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dce366b1e6d0fa05919348dc06dc6108f1af18ff48435ec4eab150da3379a650
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/UpDFi_5JSASlI1ttXOGpYA/zh-cn_image_0000002815560013.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DD16D921ED226FEBD0798469A2969AB7D619DE130A20D2494BEAF005B262F36)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/4x3J1UvyR8-buLY9nsKGBA/zh-cn_image_0000002815400097.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=39934C93F1494ED98FE3AF52C632559D1DD1451DE0BE9342DC5F55B128F608CB)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/9Aj4JZ9VROCziAUj0ERe6w/zh-cn_image_0000002786520522.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=57DE4B112CA9127E1BD63B637A81F3FF73403BBC05F5D4E913F17279AE219133)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
