---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-operatora
title: operator==
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f099920e086bd35cd7a4c8e3192b600442606c23ee04ce0cee4ae70a7e6cbe5b
---

## 函数功能

判断格式是否相等。

## 函数原型

```
1. bool operator==(const StorageFormat &other) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一种格式。 |

## 返回值

true代表相等。

false代表不等。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. StorageFormat another_format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_NC, dim_type);
4. bool is_same_fmt = format == another_format; // false
```
