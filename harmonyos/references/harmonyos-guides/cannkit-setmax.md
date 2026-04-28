---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmax
title: SetMax
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > SetMax
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5cba7531cc9d465e6acf4a91426bb9da75f573a4189a2518c5dc3ca5bda9bb15
---

## 函数功能

设置最大的T对象指针。

## 函数原型

```
1. void SetMax(T *max)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| max | 输入 | 最大的T对象指针。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. Range<int> range;
2. int max = 1024;
3. range.SetMax(&max);
```
