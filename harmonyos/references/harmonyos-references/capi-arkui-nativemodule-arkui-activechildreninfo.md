---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo
title: ArkUI_ActiveChildrenInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ActiveChildrenInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1de8806601f02cdad533ea191a24e6ca91b9e8296acc1468facb42bb9c6e9b12
---

```c
typedef struct ArkUI_ActiveChildrenInfo ArkUI_ActiveChildrenInfo
```

## 概述

定义ArkUI\_ActiveChildrenInfo结构体，用于保存内部活跃状态为true的FrameNode子节点信息，支持查询子节点数量和按下标获取子节点。该结构体实例由OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo生成，使用完毕后必须调用OH\_ArkUI\_ActiveChildrenInfo\_Destroy销毁。

**起始版本：** 14

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_NodeUtils\_GetActiveChildrenInfo](capi-native-node-h.md#oh_arkui_nodeutils_getactivechildreninfo) | 获取内部活跃状态为true的FrameNode子节点，并生成ArkUI\_ActiveChildrenInfo实例。Span不会被计入子节点统计。获取成功后，可查询子节点数量并按下标读取子节点；实例使用完毕后必须调用OH\_ArkUI\_ActiveChildrenInfo\_Destroy销毁。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_GetNodeByIndex](capi-native-type-h.md#oh_arkui_activechildreninfo_getnodebyindex) | 获取ArkUI\_ActiveChildrenInfo结构体中下标为index的子节点，适用于按下标遍历活跃子节点。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_GetCount](capi-native-type-h.md#oh_arkui_activechildreninfo_getcount) | 获取ArkUI\_ActiveChildrenInfo结构体内的子节点数量，适用于遍历活跃子节点前确定数量。 |
| [OH\_ArkUI\_ActiveChildrenInfo\_Destroy](capi-native-type-h.md#oh_arkui_activechildreninfo_destroy) | 销毁ArkUI\_ActiveChildrenInfo实例，释放获取活跃子节点信息时分配的资源。 |
