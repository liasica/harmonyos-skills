---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-find
title: Find
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AscendString > Find
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf5882aed7dcb5f00a2c7a58978c9f064168976a7b8ff1e5702b660e1a2c8234
---

## 函数功能

查找子串在当前字符串中的位置。

## 函数原型

```cpp
size_t Find(const AscendString &ascend_string) const;
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| ascend\_string | 输入 | 要查找的子串。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| size\_t | 子串的起始位置。 |
