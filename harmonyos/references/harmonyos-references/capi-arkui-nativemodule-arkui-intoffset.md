---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intoffset
title: ArkUI_IntOffset
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_IntOffset
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e89c4fcb4a56b1284cc83028b1f0a5c2b7c6d3b612546a2d964aab66d21dd2d7
---

```c
typedef struct {...} ArkUI_IntOffset
```

## 概述

偏移量，用于描述当前组件相对于父组件的位置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 水平方向的偏移量，单位为px。x为正数时组件向右偏移，为负数时向左偏移。 |
| int32\_t y | 竖直方向的偏移量，单位为px。y为正数时组件向下偏移，为负数时向上偏移。 |
