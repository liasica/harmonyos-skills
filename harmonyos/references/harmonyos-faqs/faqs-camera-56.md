---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-56
title: 相机对焦模式设置
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 相机对焦模式设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:be1f6c71be425ad56e1a22e57c45d47fd21d769ed5e02762e54781e0b6852048
---

## 问题现象

如何在拍照时设置对焦模式？

## 背景知识

相机框架提供对焦设置的能力，应用可以根据使用场景进行对焦模式和对焦点的设置，具体开发步骤可参考[对焦(ArkTS)](../harmonyos-guides/camera-focus.md)和[对焦(C/C++)](../harmonyos-guides/camera-focus-native.md)。

## 解决方案

以自动对焦模式为例，可以使用以下方式设置对焦模式为自动对焦：

1. 在设置对焦模式前，需要先调用[isFocusModeSupported](../harmonyos-references/arkts-apis-camera-focusquery.md#isfocusmodesupported11)检查设备是否支持指定的焦距模式，需要在Session调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)完成配流之后调用。
2. 调用[setFocusMode](../harmonyos-references/arkts-apis-camera-focus.md#setfocusmode11)设置对焦模式为camera.FocusMode.FOCUS\_MODE\_AUTO，支持调用[setFocusPoint](../harmonyos-references/arkts-apis-camera-focus.md#setfocuspoint11)设置对焦点，根据对焦点执行一次自动对焦。具体对焦模式可参考下表：

   | 名称 | 值 | 说明 | 适用场景 |
   | --- | --- | --- | --- |
   | FOCUS\_MODE\_MANUAL | 0 | 手动对焦。通过手动修改相机焦距来改变对焦位置，不支持对焦点设置。 | 当相机和拍摄主体距离，已经近到超过了镜头的最近对焦距离，或在弱光环境下，需要使用手动对焦。 |
   | FOCUS\_MODE\_CONTINUOUS\_AUTO | 1 | 连续自动对焦。不支持对焦点设置。 | 适合用于拍摄移动的主体或者在拍摄过程中需要不断调整焦距的情况。画面会根据预览的内容自动调整，切换焦距或者画面预览都不会模糊。 |
   | FOCUS\_MODE\_AUTO | 2 | 自动对焦。支持对焦点设置，可以使用[setFocusPoint](../harmonyos-references/arkts-apis-camera-focus.md#setfocuspoint11)设置对焦点，根据对焦点执行一次自动对焦。 | 系统默认能力，大多数情况下可以成功对焦，适合绝大部分场景。 |
   | FOCUS\_MODE\_LOCKED | 3 | 对焦锁定。不支持对焦点设置。 | 完成自动对焦后，固定对焦距离，不需要相机再自行改变焦点时使用。 |

在相机应用开发过程中，可以随时监听相机聚焦的状态变化，通过注册[focusStateChange](../harmonyos-references/arkts-apis-camera-securesession.md#onfocusstatechange12)的回调函数获取监听结果，仅当对焦模式为自动对焦模式，且相机对焦状态发生改变时触发该事件，具体代码可参考[对焦-状态监听](../harmonyos-guides/camera-focus.md#状态监听)。

## 常见FAQ

Q：在进行拍照时，相机对焦发生改变，焦距突然变化。

A：相机框架默认自动对焦能力，可以使用以下方式设置对焦模式为手动对焦：在[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)之后执行[photoSession.setFocusMode(camera.FocusMode.FOCUS\_MODE\_MANUAL)](../harmonyos-references/arkts-apis-camera-focus.md#setfocusmode11)。

Q：自定义相机进入相机页面时，页面没有聚焦或对焦不明显，拍照会模糊，如何解决？

A：可以将模式设置为this.session.setFocusMode(camera.FocusMode.FOCUS\_MODE\_AUTO)，每次点击后用[setFocusPoint](../harmonyos-references/arkts-apis-camera-focus.md#setfocuspoint11)对焦点进行设置可以实现。

Q：相机设置连续自动对焦模式后和没设置有什么区别？

A：设置连续自动对焦后画面会根据预览的内容自动调整，在切换焦距或者画面时都不会模糊。
