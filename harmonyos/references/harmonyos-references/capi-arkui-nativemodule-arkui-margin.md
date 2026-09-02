---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-margin
title: ArkUI_Margin
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_Margin
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b7b44f863f8e23b05e2fbc5a5b5ba546c08c8ecbce4e16433eb50c1efbea0841
---

```c
typedef struct {...} ArkUI_Margin
```

## 概述

外边距属性，定义组件边界与父容器或相邻组件之间的空白区域，影响组件在布局中的实际占用空间和位置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [water\_flow.h](capi-water-flow-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float top | 上外边距，单位为vp。 |
| float right | 右外边距，单位为vp。 |
| float bottom | 下外边距，单位为vp。 |
| float left | 左外边距，单位为vp。 |
