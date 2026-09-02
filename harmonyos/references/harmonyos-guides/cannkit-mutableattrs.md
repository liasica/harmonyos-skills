---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableattrs
title: MutableAttrs
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > MutableAttrs
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:b5de5488390afaf111a744e181ac4f8f95a77bc1f918a30387dca66555bcfa66
---

## 函数功能

获取算子的属性值，仅在算子IR原型定义和调用IMPL\_OP宏注册的属性值会被返回，其他属性值被丢弃。

本方法与[GetAttrs](cannkit-computenodeinfo-getattrs.md)的区别在于可以返回非const的属性对象。

## 函数原型

```cpp
RuntimeAttrs *MutableAttrs()
```

## 参数说明

无

## 返回值

所有IR原型定义过的属性值以及通过IMPL\_OP宏注册的属性值，属性值按照IR原型定义的顺序依次保存。返回对象为非const。

## 约束说明

无

## 调用示例

```cpp
auto compute_node_info = extend_kernel_context->GetComputeNodeInfo();
auto attrs = compute_node_info->MutableAttrs();
```
