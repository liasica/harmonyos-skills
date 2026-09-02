---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-operatorb
title: operator!=
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > operator!=
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:68c2beb22ed0737054da731008fbfced7efebc6da4049c1a2812ad69ec486ef5
---

## 函数功能

判断格式是否不相等。

## 函数原型

```cpp
bool operator!=(const StorageFormat &other) const
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

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
StorageFormat another_format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_NC, dim_type);
bool is_diff_fmt = format != another_format; // true
```
