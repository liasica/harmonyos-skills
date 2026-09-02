---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avcastpickerparam
title: "@ohos.multimedia.avCastPickerParam (投播组件参数)"
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avCastPickerParam (投播组件参数)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4987aaac4c1fb89af0c1bec3f8d6b27a7832680728b3efd321f587fde244640c
---

avCastPickerParam提供了[@ohos.multimedia.avCastPicker](ohos-multimedia-avcastpicker.md)组件相关的枚举参数。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## AVCastPickerState

投播组件设备列表状态参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_APPEARING | 0 | 组件显示。 |
| STATE\_DISAPPEARING | 1 | 组件消失。 |

## AVCastPickerStyle12+

投播组件样式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE\_PANEL | 0 | 面板样式。 |
| STYLE\_MENU | 1 | 菜单样式。 |

## AVCastPickerColorMode12+

投播组件显示模式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 跟随系统模式。 |
| DARK | 1 | 深色模式。 |
| LIGHT | 2 | 浅色模式。 |
