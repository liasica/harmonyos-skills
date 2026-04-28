---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-appenddim
title: AppendDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > AppendDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:43d5cbc07a49e547f50f90bd20c2a2e9de60ccb2967dae8247392ac88c5ce71e
---

## 函数功能

向后扩展一个dim值，如果扩展的dim数量超出Shape的最大限制，那么本函数不做任何事情。

## 函数原型

```
1. Shape& AppendDim(const int64_t value)
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

```
1. Shape shape0({3, 256, 256});
2. shape0.AppendDim(1024); // 3,256,256,1024
```
