---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tilingparse
title: TilingParse
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > TilingParse
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20af9d49e3154d81059ed4cfd7b642c4fe3773f6e344c91ecbf16d63d8cc909e
---

## 函数功能

注册算子的TilingParse函数，用于解析算子编译阶段生成的算子信息json文件，在注册时需要注册算子自行指定数据类型T，该数据类型用于保存解析后的算子信息。

开发者需要为算子编写一个KernelFunc类型或者TilingParseFunc类型的函数，并使用下列对应的接口进行注册。

KernelFunc类型定义如下。

```cpp
using KernelFunc = UINT32 (*)(KernelContext *context);
```

TilingParseFunc类型定义如下。

```cpp
using TilingParseFunc = UINT32 (*)(TilingParseContext *context);
```

## 函数原型

```cpp
template<typename T>
OpImplRegisterV2 &TilingParse(KernelFunc const tiling_parse_func);
template<typename T>
OpImplRegisterV2 &TilingParse(TilingParseFunc const tiling_parse_func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| tiling\_parse\_func | 输入 | 待注册的TilingParse函数，类型支持2种：KernelFunc、TilingParseFunc。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了TilingParse函数。

## 约束说明

无
