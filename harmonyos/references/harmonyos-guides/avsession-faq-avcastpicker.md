---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-faq-avcastpicker
title: 使用AVCastPicker组件常见问题
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > AVSession Kit常见问题 > 使用AVCastPicker组件常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:81444da39712096c61583a43b79a1a7b44ef48ccb27ef4d1acb3abfa3d41ab64
---

本文汇总音视频应用在使用投播组件[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md)过程中遇到的典型问题及其定位与解决方法。开发者可结合[媒体会话管理错误码](../harmonyos-references/errorcode-avsession.md)和HiLog日志进一步定位问题。

## 组件拉起后设备列表为空

**问题现象**

点击AVCastPicker组件后，弹出的设备选择界面为空。

**可能原因**

* 未创建对应类型的AVSession：以通话场景为例，需要创建voice\_call类型的AVSession，否则将显示空列表。
* 当前设备无可用投播设备：周围不存在可投播的远端设备。

**解决措施**

1. 创建对应类型的AVSession。以通话场景为例，请参考[切换通话输出设备](using-switch-call-devices.md#切换通话输出设备)完成voice\_call类型会话的创建。
2. 确认周围存在可投播的远端设备。远端设备包括：HarmonyOS 5.0.0及以上版本的PC/2in1设备、HarmonyOS 3.1及以上的TV设备，或其他支持标准DLNA协议的设备。

## 自定义样式不随设备切换刷新

**问题现象**

使用customPicker自定义了组件样式，但设备切换后样式未更新。

**可能原因**

自定义样式不会随设备切换自动刷新，需要应用自行根据设备变化刷新。

**解决措施**

监听音频设备的切换事件[on('preferOutputDeviceChangeForRendererInfo')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onpreferoutputdevicechangeforrendererinfo10)，在回调中调用[getPreferredOutputDeviceForRendererInfoSync](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getpreferredoutputdeviceforrendererinfosync10)获取当前设备并刷新自定义样式。具体实现请参考[自定义样式实现](using-switch-call-devices.md#自定义样式实现)。
