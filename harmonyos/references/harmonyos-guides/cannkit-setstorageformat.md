---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setstorageformat
title: SetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > SetStorageFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:29975721c8dcb6dd8a5a44591144553c40bd9cafba0a866cd453634cd97d6b56
---

## 函数功能

设置运行时format。

## 函数原型

```
1. void SetStorageFormat(const ge::Format storage_format)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| storage\_format | 输入 | 运行时format。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. format.SetStorageFormat(ge::Format::FORMAT_NC);
```
