---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a039d8cdd34115af6f16b24c6b22c0878c9517d8bc1885195f5479ff092b58e1
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/AzOpAQxIRASd6KC07wC_MQ/zh-cn_image_0000002589325549.png?HW-CC-KV=V1&HW-CC-Date=20260429T054031Z&HW-CC-Expire=86400&HW-CC-Sign=A669540EB14CC10EAC1AFCF4A68B127C85A15B448E0F4CED7DC411BAFEE696A4)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/gPxz_p4hSIaUvo-pz4KdqQ/zh-cn_image_0000002589245487.png?HW-CC-KV=V1&HW-CC-Date=20260429T054031Z&HW-CC-Expire=86400&HW-CC-Sign=0275C265720D0DBFB6DC1FA88FA55B451C2A30E49B350AF13A6AEC216A306E75)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/aXA83XVoRBeN3acqnmHTKw/zh-cn_image_0000002558765680.png?HW-CC-KV=V1&HW-CC-Date=20260429T054031Z&HW-CC-Expire=86400&HW-CC-Sign=6053268C679327D9879009534188F58FD0564C8BDBD9EBF4CC31A149735B5D2E)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
