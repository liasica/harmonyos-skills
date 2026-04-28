---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getplacement
title: GetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetPlacement
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c86d67993de29176b71ca3e9199ba7c555ffb31dd3377d2665cfe1c2015a7ed2
---

## 函数功能

获取Tensor的placement。

## 函数原型

```
1. ge::Placement GetPlacement() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| ge::Placement | 返回tensor的Placement值，默认值为kPlacementEnd。 |

## 异常处理

无

## 约束说明

无
