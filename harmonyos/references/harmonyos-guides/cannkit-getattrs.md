---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattrs
title: GetAttrs
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetAttrs
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3814382df85064bed77cabd059ba6b1b3fc6817af8dbb6e089fd5b569aec91ba
---

## 函数功能

获取算子的属性值，仅在算子IR原型定义中的属性值会被返回，其他属性值被丢弃。

## 函数原型

```
1. const RuntimeAttrs *GetAttrs() const
```

## 参数说明

无

## 返回值

所有IR原型定义的属性值，为const类型的对象，属性值按照IR原型定义的顺序依次保存。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto rt_attrs = extend_context->GetAttrs();
```
