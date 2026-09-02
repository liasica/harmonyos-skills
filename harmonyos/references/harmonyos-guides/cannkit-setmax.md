---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmax
title: SetMax
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > SetMax
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e35dff7dd4d13cf4a137bf5f41afbc10bd351a3a283c39e8156b74db0131a201
---

## 函数功能

设置最大的T对象指针。

## 函数原型

```cpp
void SetMax(T *max)
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

```cpp
Range<int> range;
int max = 1024;
range.SetMax(&max);
```
