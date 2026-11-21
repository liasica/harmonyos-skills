---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2506869933ac0a20476757378560e8be69f8b606d32c5990548acbebb0a216ac
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/fIbTWxz-RwCh0lIszBLTaQ/zh-cn_image_0000002821758217.png?HW-CC-KV=V1&HW-CC-Date=20261121T011239Z&HW-CC-Expire=31536000000&HW-CC-Sign=77C615CDEAE54E26711FE82501BA614CF9EE950FD584250FBB8E6FCDEA24437F)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/f4f4cOWeTB6oubwfLWrZYg/zh-cn_image_0000002793038280.png?HW-CC-KV=V1&HW-CC-Date=20261121T011239Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A0EAC11CAC8366E0A7622D9DF0C3FD65AC32876E517A5B1ABAFF6767890055B)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/FDMf2njaTsGaH5oJ1fjbcA/zh-cn_image_0000002792878310.png?HW-CC-KV=V1&HW-CC-Date=20261121T011239Z&HW-CC-Expire=31536000000&HW-CC-Sign=92D82C1F1866ECF2EE289EB244BEF8DDB1FF05335981C66C175E460BC42301B7)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
