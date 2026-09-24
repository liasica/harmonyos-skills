---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intoffset
title: ArkUI_IntOffset
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_IntOffset
category: harmonyos-references
scraped_at: 2026-09-25T07:10:48+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:cc6903ebe6fee473782122d2e1d858912b17f43b4e8522f9494a84583b739237
---

```c
typedef struct {...} ArkUI_IntOffset
```

## 概述

偏移量，用于描述当前组件相对于父组件的位置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [common\_type.h](capi-common-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 水平方向的偏移量，单位为px。x为正数时组件向右偏移，为负数时向左偏移。 |
| int32\_t y | 竖直方向的偏移量，单位为px。y为正数时组件向下偏移，为负数时向上偏移。 |
