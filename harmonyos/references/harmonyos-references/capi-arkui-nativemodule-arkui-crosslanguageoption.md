---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-crosslanguageoption
title: ArkUI_CrossLanguageOption
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_CrossLanguageOption
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dac495c84d16dad9d8e66d54d5a5d3e1debdab4579cd2e78918f0129c6dad06e
---

```c
typedef struct ArkUI_CrossLanguageOption ArkUI_CrossLanguageOption
```

## 概述

定义跨语言配置项，用于配置目标节点的跨语言访问能力，例如是否允许跨语言修改属性；从API version 26.0.0开始，还可配置节点树跨语言操作状态。

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_NodeUtils\_SetCrossLanguageOption](capi-native-node-h.md#oh_arkui_nodeutils_setcrosslanguageoption) | 设置目标节点的跨语言配置项。 |
| [OH\_ArkUI\_NodeUtils\_GetCrossLanguageOption](capi-native-node-h.md#oh_arkui_nodeutils_getcrosslanguageoption) | 获取目标节点的跨语言配置项。 |
| [OH\_ArkUI\_CrossLanguageOption\_Create](capi-native-type-h.md#oh_arkui_crosslanguageoption_create) | 创建跨语言配置项实例。使用完毕后，需调用[OH\_ArkUI\_CrossLanguageOption\_Destroy](capi-native-type-h.md#oh_arkui_crosslanguageoption_destroy)销毁实例。 |
| [OH\_ArkUI\_CrossLanguageOption\_Destroy](capi-native-type-h.md#oh_arkui_crosslanguageoption_destroy) | 销毁跨语言配置项实例。 |
| [OH\_ArkUI\_CrossLanguageOption\_SetAttributeSettingStatus](capi-native-type-h.md#oh_arkui_crosslanguageoption_setattributesettingstatus) | 设置配置项中是否允许跨语言修改属性。 |
| [OH\_ArkUI\_CrossLanguageOption\_GetAttributeSettingStatus](capi-native-type-h.md#oh_arkui_crosslanguageoption_getattributesettingstatus) | 获取配置项中是否允许跨语言修改属性。 |
| [OH\_ArkUI\_CrossLanguageOption\_SetTreeOperatingStatus](capi-native-type-h.md#oh_arkui_crosslanguageoption_settreeoperatingstatus) | 设置跨语言配置项的节点树操作状态。 |
| [OH\_ArkUI\_CrossLanguageOption\_GetTreeOperatingStatus](capi-native-type-h.md#oh_arkui_crosslanguageoption_gettreeoperatingstatus) | 获取跨语言配置项的节点树操作状态。 |
