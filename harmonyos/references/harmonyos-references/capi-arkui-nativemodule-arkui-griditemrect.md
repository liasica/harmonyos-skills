---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemrect
title: ArkUI_GridItemRect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_GridItemRect
category: harmonyos-references
scraped_at: 2026-04-28T08:04:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3e2a7b6cf9470d085db292fdc96ec3078081266dbdf6f55d84f5606ad8e46803
---

```
1. typedef struct {...} ArkUI_GridItemRect
```

## 概述

PhonePC/2in1TabletTVWearable

定义Grid布局选项onGetRectByIndex回调返回值结构体。

**起始版本：** 22

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t rowStart | GridItem行起始位置。 |
| uint32\_t columnStart | GridItem列起始位置。 |
| uint32\_t rowSpan | GridItem占用的行数。 |
| uint32\_t columnSpan | GridItem占用的列数。 |
