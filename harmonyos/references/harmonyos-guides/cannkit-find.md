---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-find
title: Find
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AscendString > Find
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:883e57adc3b0137e72af7f0ff055ddda0777b7b192eaace9f5d501411fb36079
---

## 函数功能

查找子串在当前字符串中的位置。

## 函数原型

```
1. size_t Find(const AscendString &ascend_string) const;
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
