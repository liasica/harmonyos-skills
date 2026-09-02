---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-appenddim
title: AppendDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > AppendDim
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3236d430c3a30a42b504e17b6f3ae60be84f435995fbb7648f0f1732c53be5c
---

## 函数功能

向后扩展一个dim值，如果扩展的dim数量超出Shape的最大限制，那么本函数不做任何事情。

## 函数原型

```cpp
Shape& AppendDim(const int64_t value)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| value | 输入 | 扩展的dim值。 |

## 返回值

this引用。

## 约束说明

无

## 调用示例

```cpp
Shape shape0({3, 256, 256});
shape0.AppendDim(1024); // 3,256,256,1024
```
