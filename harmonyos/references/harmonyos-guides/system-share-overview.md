---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-share-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8de7b8a52ffbf08eadcfa322699bcde434769c180eb75307739b374af069d4e9
---

## 场景介绍

在手机设备中，分享框通过模态弹窗方式被拉起，效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/kFOg8VmbRZ6H5VwVGZJtMA/zh-cn_image_0000002583439223.png?HW-CC-KV=V1&HW-CC-Date=20260427T235057Z&HW-CC-Expire=86400&HW-CC-Sign=D4063BB87524CF9AFA4D2252E036A81BC1F53EE16D0C2EE29447E727CF14D710)

在2in1设备上分享框通过Popup形式展示，效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/gCB8OoKATNuF9h2VFsZzYw/zh-cn_image_0000002552959178.png?HW-CC-KV=V1&HW-CC-Date=20260427T235057Z&HW-CC-Expire=86400&HW-CC-Sign=4D9ABC02DD4337726AC9EC9EB13D53BDDB7A287071F824540E3A37B14BFAF937)

1. 宿主应用可以分享一段文本、一个文件或一条备忘录到其他应用。
2. 宿主应用可以分享多个内容，如文本、图片等到其他应用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/VPSepnJRQBezhLadAg-JBg/zh-cn_image_0000002583479179.png?HW-CC-KV=V1&HW-CC-Date=20260427T235057Z&HW-CC-Expire=86400&HW-CC-Sign=7A5CD9071FA5922E84E6D8100D67D68636AE507D712D6BD28E4DD8FB85DE484D)

流程说明：

1、宿主应用构造分享数据、构造ShareController以及注册分享面板状态监听（可选）。

2、宿主应用拉起系统分享面板。

3、用户可选择目标设备或者应用。

4、目标应用处理分享数据，并关闭系统分享面板。

## 设计规范

宿主应用接入系统分享时，根据不同的内容类型，应选择恰当的分享方式。详细参见：[系统分享设计指南](../design-guides/share-0000001957076313.md)。
