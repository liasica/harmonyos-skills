---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-39
title: 录制音频时，如何指定蓝牙为音频输入设备
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 录制音频时，如何指定蓝牙为音频输入设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9f96e8df15d248467104c2ad5c14e3ec979649be3c38e52ba108ac43d2b1784e
---

## 问题现象

音频录制时，如何在连接蓝牙耳机之后指定蓝牙作为音频输入设备？

## 背景知识

* [AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md)是录音设备选择组件，可用于切换音频输入设备，仅在PC/2in1设备可用。
* 应用音频输入时，系统会根据音频流类型选择对应的输入设备，如果默认音频输入设备不满足应用需求，应用可通过[setBluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)或[selectMediaInputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)实现音频输入设备切换。

## 解决方案

1. API 20后，在PC/2in1设备上，在需要切换设备的通话界面创建AVInputCastPicker组件，实现音频输入设备的选择。具体实现可参考：[切换通话输入设备](../harmonyos-guides/using-switch-call-devices.md#切换通话输入设备)。
2. API 21后，应用可使用[AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)的[setBluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)设置应用程序的输入设备选择偏好，当蓝牙或星闪设备上线时生效。
3. API 21后，应用可使用[AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)的[selectMediaInputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)选择音频输入设备。
