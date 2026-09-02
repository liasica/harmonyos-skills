---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opexecutefunc
title: OpExecuteFunc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > OpExecuteFunc
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f28272a7cbf115b4bc8ce7327cb1be052ec0877e558188b0c8a45615e6c0b46
---

## 函数功能

单个算子包含多kernel组合执行逻辑的场景下，算子可以通过该接口设置算子级的回调函数，回调函数内实现多kernel的下发。该功能为预留特性，暂不支持。

## 函数原型

```cpp
OpImplRegisterV2 &OpExecuteFunc(OpExecFunc op_execute_func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_execute\_func | 输入 | 注册的自定义OpExecuteFunc函数，类型为OpExecFunc。  OpExecFunc类型定义如下。  using OpExecFunc = UINT32 (\*)(OpExecuteContext \*); |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了算子级的回调函数。

## 约束说明

无
