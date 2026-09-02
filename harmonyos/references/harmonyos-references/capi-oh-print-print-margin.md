---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-margin
title: Print_Margin
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_Margin
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c0ef767d712ea5370bff3ba2fd6880884241d8463966d033b035d6ac31b4f581
---

```cpp
typedef struct {...} Print_Margin
```

## 概述

Print\_Margin用于表示打印页面的边距信息，支持设置左、上、右、下四个方向的边距，控制可打印内容区域。适用于需要在打印时精确控制内容与纸张边缘距离的场景，通过合理配置边距可以避免内容溢出或被裁剪。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t leftMargin | 左边距，单位：毫米。取值原则：大于0。 |
| uint32\_t topMargin | 上边距，单位：毫米。取值原则：大于0。 |
| uint32\_t rightMargin | 右边距，单位：毫米。取值原则：大于0。 |
| uint32\_t bottomMargin | 下边距，单位：毫米。取值原则：大于0。 |
