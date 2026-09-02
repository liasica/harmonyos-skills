---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecomponentevent
title: ArkUI_NodeComponentEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NodeComponentEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b431bf49c04eae08934b00cf7d5766d28d1031fc3bef8910b62f2d95c15d8471
---

```c
typedef struct {...} ArkUI_NodeComponentEvent
```

## 概述

定义组件回调事件的参数类型，用于在组件回调触发时传递事件相关数据，便于应用获取回调事件参数。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NumberValue](capi-arkui-nativemodule-arkui-numbervalue.md) data[[MAX\_COMPONENT\_EVENT\_ARG\_NUM](capi-native-node-h.md#宏定义)] | 用于存储组件回调事件的参数数据，数组元素按照回调事件定义的参数顺序排列；各事件类型的参数定义详见[native\_node.h](capi-native-node-h.md)相关说明。 |
