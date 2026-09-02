---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativecolorspacemanager-whitepointarray
title: WhitePointArray
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > WhitePointArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fde7d70ecdc61c24ae9e225b73febfae2cc595c433d67a740a67cceb18d815d4
---

```c
typedef struct {...} WhitePointArray
```

## 概述

提供白点数组结构体，白点是在当前色域中表示白色的坐标。

**起始版本：** 13

**相关模块：** [NativeColorSpaceManager](capi-nativecolorspacemanager.md)

**所在头文件：** [native\_color\_space\_manager.h](capi-native-color-space-manager-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float arr[2] | 表示白点坐标数组。arr[0]表示x坐标，arr[1]表示y坐标，用于在色域空间中精确定义白色基准点，影响色域的显示效果和颜色准确性。 |
