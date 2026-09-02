---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tiling
title: Tiling
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > Tiling
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:989563a6818da128cbb55596bca77e9a9ec4ec54ecd891f2bed6f1a45771af5a
---

## 函数功能

注册算子的Tiling函数。

开发者需要为算子编写一个TilingKernelFunc类型的函数，并使用该接口进行注册。同时可以指定tiling数据的最大长度，缺省值为2048Bytes。

TilingKernelFunc类型定义如下。

```cpp
using TilingKernelFunc = UINT32 (*)(TilingContext *);
```

## 函数原型

```cpp
OpImplRegisterV2 &Tiling(TilingKernelFunc tiling_func, size_t max_tiling_data_size = 2048);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| tiling\_func | 输入 | 待注册的自定义Tiling函数，类型为TilingKernelFunc。 |
| max\_tiling\_data\_size | 输入 | tiling数据的最大长度，默认值为2048Bytes。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了Tiling函数tiling\_func。

## 约束说明

无
