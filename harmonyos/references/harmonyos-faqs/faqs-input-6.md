---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-input-6
title: 模拟鼠标滚轮事件相关疑问
breadcrumb: FAQ > 系统开发 > 基础功能 > 多模输入（Input） > 模拟鼠标滚轮事件相关疑问
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:37a24a0dfff6cf4dd9af6c30acdbcaa33581a30fbc8fee885a6dbc7052780a9b
---

## 问题现象

1. 应用侧已申请[ohos.permission.INPUT\_MONITORING](../harmonyos-guides/restricted-permissions.md#ohospermissioninput_monitoring)权限，已实现鼠标移动、键盘按键的模拟，但是鼠标滚轮事件不生效。
2. 如何模拟鼠标双击事件？

## 解决方案

1. 需要调用[OH\_Input\_SetMouseEventAction](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_setmouseeventaction)接口，分别处理[Input\_MouseEventAction](../harmonyos-references/capi-oh-input-manager-h.md#input_mouseeventaction)中的MOUSE\_ACTION\_AXIS\_UPDATE和MOUSE\_ACTION\_AXIS\_END事件。
2. 模拟连续单击事件，时间间隔小于0.3s。
