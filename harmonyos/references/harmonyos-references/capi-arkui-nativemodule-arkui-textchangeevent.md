---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textchangeevent
title: ArkUI_TextChangeEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_TextChangeEvent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8daf1dfd5af4ae4c57fe4e3bc1916a61dfd05f63b0ac25ea029fadd43212c45a
---

```c
typedef struct {...} ArkUI_TextChangeEvent
```

## 概述

定义文本变化事件的数据结构，用于在文本输入场景中监听和处理文本变更事件。该结构体包含文本内容、扩展信息和数值参数，支持开发者实时获取文本变更数据，适用于输入框内容监听、实时搜索、字数统计等场景。

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* pStr | 文本变更事件中的文本内容字符串。 |
| const char\* pExtendStr | 文本变更事件中的扩展字符串，用于存储额外的文本信息。 |
| int32\_t number | 事件的数字参数值，用于记录文本变更事件中的数值信息。取值范围[-2147483648, 2147483647]。 |
