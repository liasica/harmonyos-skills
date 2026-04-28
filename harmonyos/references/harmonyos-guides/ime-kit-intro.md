---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ime-kit-intro
title: IME Kit简介
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > IME Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:36+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3dbb246e53a1fe9df46d9ce833fed3fa25f73a69823d66ec0808d30985bee5e5
---

IME Kit 负责建立编辑框所在应用与输入法应用之间的通信通道，确保两者可以共同协作提供文本输入功能，也为系统应用提供管理输入法应用的能力。

## Kit使用场景

IME Kit提供输入法框架和输入法服务两类API。用于实现输入法应用，也可以用于实现自绘编辑框以及实现对输入法应用的控制。

## 框架原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/rqKKF61yRiqIMRP2tERfQQ/zh-cn_image_0000002552798666.png?HW-CC-KV=V1&HW-CC-Date=20260427T234135Z&HW-CC-Expire=86400&HW-CC-Sign=862C8C21CF47C754445C3F6BFD6CF7B1682DC7C49A9C2EE8AC8394724BAAD125)

## 功能特点

* 输入法应用：

  支持创建固定态、悬浮态、状态栏三种类型的Panel，可支持开发一个输入法应用同时部署在手机、平板等多设备中。
* 自定义编辑框：

  支持开发者自定义编辑框，实现绑定输入法应用，并实现输入法应用的文字输入、删除、选中、光标移动等操作。

## 能力范围

* 提供输入法服务相关API，用于输入法应用，包括：创建软键盘窗口、插入/删除字符、选中文本、监听物理键盘按键事件等。
* 提供输入法框架相关API，可用于自绘编辑框，包括绑定输入法，实现输入、删除、选中、光标移动等。
* 提供系统应用管理输入法应用能力，实现对输入法应用的控制，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表。

## 与相关Kit的关系

ArkUI: IME Kit在输入法软键盘和自绘编辑框时使用ArkUI提供的部分组件、事件、动效、状态管理等能力，例如Text、Button组件，onClick点击事件。

## 约束限制

针对切换输入法应用的系统API，需要申请系统权限，部分API仅支持当前输入法应用调用。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。

## IME Kit API参考

* [inputMethodEngine](../harmonyos-references/js-apis-inputmethodengine.md)
* [inputMethod](../harmonyos-references/js-apis-inputmethod.md)
* [InputMethodExtensionAbility](../harmonyos-references/js-apis-inputmethod-extension-ability.md)
* [InputMethodExtensionContext](../harmonyos-references/js-apis-inputmethod-extension-context.md)
* [inputMethodList](../harmonyos-references/js-apis-inputmethodlist.md)
* [InputMethodSubtype](../harmonyos-references/js-apis-inputmethod-subtype.md)
* [inputMethod.Panel](../harmonyos-references/js-apis-inputmethod-panel.md)
