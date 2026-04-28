---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdimnum
title: GetDimNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > GetDimNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dde3885f283aabcbe5df78f1c42b67df62fb851e49aa4b60937639e5bedbedb0
---

## 函数功能

获取dim\_num。

## 函数原型

```
1. size_t GetDimNum() const
```

## 参数说明

无

## 返回值

获取dim\_num，即Shape的长度。

## 约束说明

无

## 调用示例

```
1. Shape shape0({3, 256, 256});
2. auto dim_num = shape0.GetDimNum(); // 3
```
