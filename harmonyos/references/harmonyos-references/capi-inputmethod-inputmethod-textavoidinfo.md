---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-inputmethod-inputmethod-textavoidinfo
title: InputMethod_TextAvoidInfo
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > C API > 结构体 > InputMethod_TextAvoidInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:52:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8e35014647c8bcf7ef6920172591d1ec2f5e4f69aedf6ab6ef4d34e6a57c347c
---

```c
typedef struct InputMethod_TextAvoidInfo InputMethod_TextAvoidInfo
```

## 概述

输入框避让信息结构体，描述编辑框在物理屏幕上的位置和高度信息。输入法框架根据TextAvoidInfo中的positionY和height计算避让区域，使编辑框在软键盘弹起时能够自动上移或调整布局，确保输入区域不被键盘遮挡，保证用户可见并可操作输入内容。

用途：作为编辑框避让键盘区域的参数载体，向输入法框架传递编辑框的垂直位置和高度信息。输入法框架根据positionY（编辑框顶部Y坐标，取值原则：大于等于0的有效屏幕Y坐标）和height（编辑框高度，取值原则：大于0的有效高度值）确定编辑框在屏幕上的完整垂直范围（positionY到positionY+height），并与键盘占据的屏幕区域进行比较，计算是否需要避让以及避让的偏移量。

使用场景：在编辑框与输入法服务绑定后（通过OH\_InputMethodController\_Attach），编辑框客户端通过InputMethod\_TextConfig将TextAvoidInfo传递给输入法框架。输入法框架在键盘弹起时读取避让信息，判断编辑框是否处于键盘遮挡区域，并触发相应的避让调整。该结构体也可由输入法应用读取，用于了解编辑框的屏幕位置以优化键盘布局。

**起始版本：** 12

**相关模块：** [InputMethod](capi-inputmethod.md)

**所在头文件：** [inputmethod\_text\_avoid\_info\_capi.h](capi-inputmethod-text-avoid-info-capi-h.md)

相关函数：

| 函数 | 说明 |
| --- | --- |
| [OH\_TextAvoidInfo\_Create](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_create) | 创建InputMethod\_TextAvoidInfo实例 |
| [OH\_TextAvoidInfo\_Destroy](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_destroy) | 销毁InputMethod\_TextAvoidInfo实例 |
| [OH\_TextAvoidInfo\_SetPositionY](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_setpositiony) | 设置Y坐标值 |
| [OH\_TextAvoidInfo\_SetHeight](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_setheight) | 设置高度值 |
| [OH\_TextAvoidInfo\_GetPositionY](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_getpositiony) | 获取Y坐标值 |
| [OH\_TextAvoidInfo\_GetHeight](capi-inputmethod-text-avoid-info-capi-h.md#oh_textavoidinfo_getheight) | 获取高度值 |
| [OH\_TextConfig\_GetTextAvoidInfo](capi-inputmethod-text-config-capi-h.md#oh_textconfig_gettextavoidinfo) | 从TextConfig中获取TextAvoidInfo |

相关结构体：

| 结构体 | 说明 |
| --- | --- |
| [InputMethod\_TextConfig](capi-inputmethod-inputmethod-textconfig.md) | 文本输入框配置结构体，TextAvoidInfo作为其子属性被包含 |
