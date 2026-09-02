---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-snapshotoptions
title: ArkUI_SnapshotOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_SnapshotOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7a0461253184062e447df14f4c2484fb521f94f97e182c956aa950c795a4f344
---

```c
typedef struct ArkUI_SnapshotOptions ArkUI_SnapshotOptions
```

## 概述

定义截图的可选项，用于在执行组件截图时配置截图行为，适用于需要按业务需求控制截图输出效果的场景。

使用本结构体时，应先调用[OH\_ArkUI\_CreateSnapshotOptions](capi-common-attributes-h.md#oh_arkui_createsnapshotoptions)创建截图选项对象，并通过相关配置接口设置截图参数；再将该对象作为snapshotOptions参数传入[OH\_ArkUI\_GetNodeSnapshot](capi-native-node-h.md#oh_arkui_getnodesnapshot)；不再使用时，必须调用[OH\_ArkUI\_DestroySnapshotOptions](capi-common-attributes-h.md#oh_arkui_destroysnapshotoptions)释放资源。

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [common\_attributes.h](capi-common-attributes-h.md)
