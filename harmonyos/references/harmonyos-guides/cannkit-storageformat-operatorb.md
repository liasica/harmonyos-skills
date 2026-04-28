---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-operatorb
title: operator!=
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > operator!=
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:575b26c69d11b1b14c6254fb324e1515446f6a20352a1610ed76fca2772c8a26
---

## 函数功能

判断格式是否不相等。

## 函数原型

```
1. bool operator!=(const StorageFormat &other) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一种格式。 |

## 返回值

true表示格式不同。

false表示格式相同。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. StorageFormat another_format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_NC, dim_type);
4. bool is_diff_fmt = format != another_format; // true
```
