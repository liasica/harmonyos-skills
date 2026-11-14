---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:201fcea366259aaef3c235d6b87e8fc9f3b36b3a831a2a5ac40cba5cc7740584
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ElqOSvm9S2WaEOgoPpC2Hg/zh-cn_image_0000002788308326.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=600DA12EDAD36CA4A96FBF01ABD78B2517F8650B71BD2D89E695D2EB3B30C20F)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/dpOUGj-cQlCPY-w-FIUUtg/zh-cn_image_0000002817427689.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=392A4096C62EC146E49EEB5F167809BE5C6ACEBD74F10F750915B96404339F7E)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/D0L_4ArRSUKTiRLQn0cuWA/zh-cn_image_0000002788468270.png?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5F2EF5A8763EF24AA77F21136C57C4EEF6218BB96A87BF8AE3BC54A0F9EC9B5)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
