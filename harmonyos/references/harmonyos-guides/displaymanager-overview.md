---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaymanager-overview
title: 屏幕管理简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 屏幕管理 > 屏幕管理简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3c8b5abd6082de31ab81a3443cfb7d456928f437c266aff08855898d1f0179e
---

屏幕管理主要是针对设备的各种屏幕（包括物理屏、虚拟屏、折叠屏）进行管理，管理其各种属性信息，并当作广播者，将监听到的信息广播给各个需要屏幕信息的订阅服务。

屏幕管理主要包括以下几方面能力：

* 可获取屏幕当前的属性信息，包括屏幕分辨率、物理像素密度、屏幕尺寸等。
* 可监听屏幕发生的各种事件变化，包括屏幕旋转变化、屏幕分辨率变化、屏幕刷新率变化、折叠状态变化等。
* 提供虚拟屏的创建和使用，此部分能力仅对系统应用开放。

针对屏幕属性相关信息的查询和监听，可见[使用OH\_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++)](native-display-manager.md)和[使用Display实现屏幕属性查询及状态监听 (ArkTS)](screenproperty-guideline.md)。

## 约束和限制

* 需要在支持SystemCapability.Window.SessionManager能力的系统上使用Display和Screen接口，更详细的系统能力请参考[系统能力SystemCapability使用指南](../harmonyos-references/syscap.md)。
* 在多屏实现中，Screen接口仅支持系统应用使用，且部分接口需要申请ohos.permission.CAPTURE\_SCREEN权限。
