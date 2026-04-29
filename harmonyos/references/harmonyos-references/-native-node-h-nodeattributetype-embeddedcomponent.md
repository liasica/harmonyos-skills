---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-native-node-h-nodeattributetype-embeddedcomponent
title: ArkUI_NodeAttributeType（EmbeddedComponent组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（EmbeddedComponent组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:16+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c27900998ec228948474a315085b2bda7745b67d442a5f4c24fe85e17e596fab
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的EmbeddedComponent组件相关属性样式集合。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_EMBEDDED\_COMPONENT\_WANT

```
1. NODE_EMBEDDED_COMPONENT_WANT = MAX_NODE_SCOPE_NUM * ARKUI_NODE_EMBEDDED_COMPONENT = 1016000
```

定义用于启动EmbeddedAbility的want。支持属性设置。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | EmbeddedComponent的want参数。参数类型为[AbilityBase\_Want](capi-arkui-nativemodule-abilitybase-want.md)。默认值为nullptr。 |

## NODE\_EMBEDDED\_COMPONENT\_OPTION

```
1. NODE_EMBEDDED_COMPONENT_OPTION = 1016001
```

EmbeddedComponent的选项。支持属性设置。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | EmbeddedComponent的选项列表，参数类型为[ArkUI\_EmbeddedComponentOption](i-arkui-nativemodule-arkui-embeddedcomponentoption.md)。 |
