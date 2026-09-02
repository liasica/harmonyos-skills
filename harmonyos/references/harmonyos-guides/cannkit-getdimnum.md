---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdimnum
title: GetDimNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > GetDimNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f0d6197ea0ce98a9d073a87284012ac5d6f3a81a65ec5690eee7fc0f12be4af
---

## 函数功能

获取dim\_num。

## 函数原型

```cpp
size_t GetDimNum() const
```

## 参数说明

无

## 返回值

获取dim\_num，即Shape的长度。

## 约束说明

无

## 调用示例

```cpp
Shape shape0({3, 256, 256});
auto dim_num = shape0.GetDimNum(); // 3
```
