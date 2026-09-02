---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-59
title: 如何查询和监听最高优先级输出设备信息
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何查询和监听最高优先级输出设备信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3bd3e7cd00224e7632ff5c27e92513791e78225279c35a5629b338888cfcfc51
---

## 问题现象

如何查询或监听最高优先级输出设备变化信息，例如切换扬声器听筒。

## 解决方案

[getPreferOutputDeviceForRendererInfo](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getpreferoutputdeviceforrendererinfo10)接口可查询优先级最高的输出设备。

[on('preferOutputDeviceChangeForRendererInfo')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onpreferoutputdevicechangeforrendererinfo10)回调方法，可以监听最高优先级输出设备变化事件（当最高优先级输出设备发生变化时触发）。

注意事项：

* 当设备信息是蓝牙设备，且需要获取蓝牙设备名称，MAC地址等信息时，需要[申请权限](../harmonyos-guides/declare-permissions.md)允许应用查看蓝牙的配置[ohos.permission.USE\_BLUETOOTH](../harmonyos-guides/permissions-for-all.md#ohospermissionuse_bluetooth)。
* 如果在音频流运行中切换其他设备，只会影响本次音频流，当音频流结束后，仍然会切回原默认优先级最高的设备。
* VOIP音频流不用时，需及时release释放掉，否则也会影响监听触发回调事件。
* audioSessionManager模块[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)切换默认输出设备时，不需要重复调用[activateAudioSession](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#activateaudiosession12)激活audioSessionManager，否则会被重复监听到。
