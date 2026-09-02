---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customproperty
title: ArkUI_CustomProperty
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_CustomProperty
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5c15c47119674eaef73da4387dc6ae3820c8ea4ced30386ea51f404f1e6ab694
---

```c
typedef struct ArkUI_CustomProperty ArkUI_CustomProperty
```

## 概述

定义表示组件自定义属性的 ArkUI\_CustomProperty 结构体。通过相关接口，可以为 ArkUI 组件添加、移除和获取自定义属性，以及获取自定义属性的字符串值。

**起始版本：** 14

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_NodeUtils\_AddCustomProperty](capi-native-node-h.md#oh_arkui_nodeutils_addcustomproperty) | 添加组件的自定义属性。 |
| [OH\_ArkUI\_NodeUtils\_RemoveCustomProperty](capi-native-node-h.md#oh_arkui_nodeutils_removecustomproperty) | 移除组件已设置的自定义属性。 |
| [OH\_ArkUI\_NodeUtils\_GetCustomProperty](capi-native-node-h.md#oh_arkui_nodeutils_getcustomproperty) | 获取组件的自定义属性，并通过handle返回ArkUI\_CustomProperty实例。 |
| [OH\_ArkUI\_CustomProperty\_Destroy](capi-native-type-h.md#oh_arkui_customproperty_destroy) | 销毁 ArkUI\_CustomProperty 实例。 |
| [OH\_ArkUI\_CustomProperty\_GetStringValue](capi-native-type-h.md#oh_arkui_customproperty_getstringvalue) | 获取自定义属性的字符串值。 |
