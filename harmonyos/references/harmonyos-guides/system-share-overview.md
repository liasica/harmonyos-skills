---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c0d7048232c6ce6099d53c278ba3163f3f5725024ce7a8dd49838f8a4a22aaf7
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/_JG9kYcnTS-jzhs6PlTR5A/zh-cn_image_0000002820406607.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=D027B26ECBEE876A2EB26C3277BFBD868B770FA4EAD716F152C2137F8550BEC8)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/aaAYMcKrQ1aiWq8CJz-IAg/zh-cn_image_0000002791726628.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC3B83AF273FB8C3449A929D9DE14504129F76F1078B51B5461BDD582D975319)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/2NQNuj58S8W3kC4m6ih4Xw/zh-cn_image_0000002791566656.png?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=67DFAA3F83E387FCCDAB5E9C57116721E849F6F879233EA35760FAD964B9CE2D)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
