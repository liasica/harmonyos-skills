---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-getattrs
title: GetAttrs
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetAttrs
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b2d37ba66d0530e258ccfa3aa0b957f0925acbf702b686f2a039cece58365c1
---

## 函数功能

获取算子的属性值，仅在算子IR原型定义和调用IMPL\_OP宏注册的属性值会被返回，其他属性值被丢弃。

## 函数原型

```cpp
const RuntimeAttrs *GetAttrs() const
```

## 参数说明

无

## 返回值

所有IR原型定义的属性值以及通过IMPL\_OP宏注册的属性值，为const类型的对象，属性值按照IR原型定义的顺序依次保存。

## 约束说明

无

## 调用示例

```cpp
auto ret = bg::CreateComputeNodeInfo(node, buffer_pool);
ASSERT_NE(ret, nullptr);
auto compute_node_info = reinterpret_cast<ComputeNodeInfo *>(ret.get());
auto attrs = compute_node_info->GetAttrs();
```
