---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmin
title: SetMin
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > SetMin
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5c4e947ce796725a72681c244b97192b02ed87f84cd8925ce9103b7240ad22a
---

## 函数功能

设置最小的T对象指针。

## 函数原型

```cpp
void SetMin(T *min)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| min | 输入 | 最小的T对象指针。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
Range<int> range;
int min = -1;
range.SetMin(&min);
```
