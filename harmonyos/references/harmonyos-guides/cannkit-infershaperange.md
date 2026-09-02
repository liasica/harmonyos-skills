---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershaperange
title: InferShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > InferShapeRange
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28f175587163096f80938b23d3ec124f3e3addcd7b6020f5a8b639b08c237cc2
---

## 函数功能

注册算子的InferShapeRange函数。

开发者需要为算子编写一个InferShapeRangeKernelFunc类型的函数，并使用该接口进行注册。

InferShapeRangeKernelFunc类型定义如下。

```cpp
using InferShapeRangeKernelFunc = UINT32 (*)(InferShapeRangeContext *);
```

## 函数原型

```cpp
OpImplRegisterV2 &InferShapeRange(InferShapeRangeKernelFunc infer_shape_range_func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| infer\_shape\_range\_func | 输入 | 要注册的自定义infer\_shape\_range\_func函数，类型为InferShapeRangeKernelFunc。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了InferShapeRange函数infer\_shape\_range\_func。

## 约束说明

无
