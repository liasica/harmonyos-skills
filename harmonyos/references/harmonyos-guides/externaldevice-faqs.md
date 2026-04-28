---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/externaldevice-faqs
title: 常见问题
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1eec2d929b4c0f96aba9b1d20670ac54c9f91b5067ffe7cc37355cff5ac7a224
---

## 编译或运行时无法找到头文件

### 问题现象

编译或运行时提示“usb/usb\_ddk\_api.h not found”、“hid/hid\_ddk\_api.h not found” 等。

### 解决措施

* 编译时报错：请确认HarmonyOS版本，是否为最新版本。
* 运行时报错：请确认设备SDK版本为API11及以上。

## 安装HAP时提示版本不匹配

### 问题现象

安装HAP时提示 “compileSdkVersion and releaseType of the app do not match the apiVersion and releaseType on the device”。

### 解决措施

请根据[参考信息](externaldevice-faqs.md#参考信息)提供的对应关系，检查设备SDK的API版本是否匹配。

### 参考信息

| 接口类型 | 支持的最小API |
| --- | --- |
| 应用开发接口（ArkTS接口） | API10 |
| USB DDK接口 | API10 |
| HID DDK接口 | API11 |

## 安装HAP时提示解析本地so文件失败

### 问题现象

安装HAP时提示"code:9568347 error: install parse native so failed"。

### 解决措施

根据应用调试中[安装HAP时提示“code:9568347 error: install parse native so failed”错误，或者运行时候提示“TypeError：Cannot read property xxx of undefined”错误](../harmonyos-faqs-V5/faqs-app-debugging-14-V5.md)提供的解决方法，在build-profile.json5中的buildOption/externalNativeOptions内手动配置abiFilters的值。
