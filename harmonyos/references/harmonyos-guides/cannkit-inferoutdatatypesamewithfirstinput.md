---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferoutdatatypesamewithfirstinput
title: InferOutDataTypeSameWithFirstInput
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > InferOutDataTypeSameWithFirstInput
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34591195f972f2b19c86f89329a1aae53bef36b590e19326212c49881c454dbb
---

## 函数功能

注册一种datatype推导规则，该规则将算子第一个输入的datatype作为所有输出的datatype。

## 函数原型

```cpp
OpImplRegisterV2 &InferOutDataTypeSameWithFirstInput();
```

## 参数说明

无

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了算子datatype推导规则。

## 约束说明

* 注册此规则，可以不用再注册自定义推导规则。若同时注册了InferDataType和InferOutDataTypeByFirstInput，将使能最后注册的规则。
* 若算子无输入或第一个输入datatype为未定义（DT\_UNDEFINED），推导将报错。
