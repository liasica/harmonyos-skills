---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getplacement
title: GetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetPlacement
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c8057f6c382d17311851483324b8235752ba979fbd2294f9a50f541b3a7a52ae
---

## 函数功能

获取Tensor的placement。

## 函数原型

```cpp
ge::Placement GetPlacement() const;
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
