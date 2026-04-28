---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customproperty
title: ArkUI_CustomProperty
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_CustomProperty
category: harmonyos-references
scraped_at: 2026-04-28T08:04:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1752a2d06a245e7084a85056ba9792e268455bf1dee0dcf8850b3c2bc97d9a6e
---

```
1. typedef struct ArkUI_CustomProperty ArkUI_CustomProperty
```

## 概述

PhonePC/2in1TabletTVWearable

定义自定义属性的CustomProperty类信息。

**起始版本：** 14

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_NodeUtils\_AddCustomProperty](capi-native-node-h.md#oh_arkui_nodeutils_addcustomproperty) | 设置组件的自定义属性。 |
| [OH\_ArkUI\_NodeUtils\_RemoveCustomProperty](capi-native-node-h.md#oh_arkui_nodeutils_removecustomproperty) | 移除组件已设置的自定义属性。 |
| [OH\_ArkUI\_NodeUtils\_GetCustomProperty](capi-native-node-h.md#oh_arkui_nodeutils_getcustomproperty) | 获取组件的自定义属性的值。 |
| [OH\_ArkUI\_CustomProperty\_Destroy](capi-native-type-h.md#oh_arkui_customproperty_destroy) | 销毁CustomProperty实例。 |
| [OH\_ArkUI\_CustomProperty\_GetStringValue](capi-native-type-h.md#oh_arkui_customproperty_getstringvalue) | 获取自定义属性value信息。 |
