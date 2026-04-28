---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isscalar
title: IsScalar
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > IsScalar
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:36d7c1ec5212e3f3b35c88601248dfd4538eb5873cb659c53e2270ece4765240
---

## 函数功能

判断本shape是否为标量，所谓标量，是指GetDimNum()为0的张量。

## 函数原型

```
1. bool IsScalar() const
```

## 参数说明

无

## 返回值

true为标量，false为非标量。

## 约束说明

无

## 调用示例

```
1. Shape shape0({3, 256, 256});
2. Shape shape2;
3. shape0.IsScalar(); // false
4. shape2.IsScalar(); // true
```
