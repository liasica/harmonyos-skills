---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiletimetensordesc-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > CompileTimeTensorDesc > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:025729f35e1cc9bab041407d1ffd9410d4b53973273b1b4d4c4c6905f30d8c8d
---

## 函数功能

CompileTimeTensorDesc类用于描述编译时的Tensor描述信息，包含dtype信息以及format信息。由于编译时无法确定shape，因此不包含shape信息。该函数为CompileTimeTensorDesc类的构造函数。

## 函数原型

```cpp
CompileTimeTensorDesc()
```

## 参数说明

无

## 返回值

返回一个CompileTimeTensorDesc对象。

## 约束说明

无
