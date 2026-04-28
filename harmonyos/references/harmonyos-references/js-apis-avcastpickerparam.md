---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avcastpickerparam
title: @ohos.multimedia.avCastPickerParam (投播组件参数)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avCastPickerParam (投播组件参数)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:53ebc0815ab01ba20ac384632ee0ac6036cce41d95b48361f0567156b548d00c
---

avCastPickerParam提供了[@ohos.multimedia.avCastPicker](ohos-multimedia-avcastpicker.md)组件状态枚举值。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## AVCastPickerState

PhonePC/2in1TabletTV

投播组件设备列表状态参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_APPEARING | 0 | 组件显示。 |
| STATE\_DISAPPEARING | 1 | 组件消失。 |

## AVCastPickerStyle12+

PhonePC/2in1TabletTV

投播组件样式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE\_PANEL | 0 | 面板样式。 |
| STYLE\_MENU | 1 | 菜单样式。 |

## AVCastPickerColorMode12+

PhonePC/2in1TabletTV

投播组件显示模式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 跟随系统模式。 |
| DARK | 1 | 深色模式。 |
| LIGHT | 2 | 浅色模式。 |
