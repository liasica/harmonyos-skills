---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattrnum
title: GetAttrNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > RuntimeAttrs > GetAttrNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:350e04898b7a3da01fb33557f69e621d5d3f0595fc2fdd3e3bb2ddb52fed26ae
---

## 函数功能

获取属性的数量。

## 函数原型

```cpp
size_t GetAttrNum() const
```

## 参数说明

无

## 返回值

属性的数量。

## 约束说明

无

## 调用示例

```cpp
const RuntimeAttrs * runtime_attrs = kernel_context->GetAttrs();
size_t attr_num = runtime_attrs->GetAttrNum();
```
