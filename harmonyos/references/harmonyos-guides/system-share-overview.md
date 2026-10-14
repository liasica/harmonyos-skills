---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1888b7b52b6624628f2ffd9570332283b1d030c0facef83efb0d1a469ba2a2af
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/HAMkWbx0T4GTjzOsLfhzaw/zh-cn_image_0000002791739869.png)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/L0cBxS0wSHywHDU_FCGeaQ/zh-cn_image_0000002762341290.png)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/kBH_FZBLSPysL0u_0v3tkA/zh-cn_image_0000002791860087.png)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
