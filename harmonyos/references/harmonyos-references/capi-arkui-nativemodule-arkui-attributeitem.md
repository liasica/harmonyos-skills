---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem
title: ArkUI_AttributeItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AttributeItem
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f3095e7b719aa5acb887928ae6f6d61b2f6b341d86c470c97d3140991fd6ccfc
---

```c
typedef struct {...} ArkUI_AttributeItem
```

## 概述

定义[setAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#setattribute)函数的通用入参结构。各个属性设置接口可选择使用其中的成员变量来存储特定类型的参数数据。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md)\* value | 数字数组，用于存储数字类型的属性参数，数组长度由size指定。 |
| int32\_t size | value数组的长度，需配合变量value使用。 |
| const char\* string | 字符串，用于存储字符串类型的属性参数。 |
| void\* object | 对象数据，用于存储对象类型的属性参数。 |
