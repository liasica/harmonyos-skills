---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getaddr
title: GetAddr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > GetAddr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e3c9acdc73387449ee9ecd4c2029ec5e0fd8f1c30178e7149edab02c7e8ace3a
---

## 函数功能

获取tensor数据地址。若存在manager函数，则由manager函数给出地址。

## 函数原型

```
1. TensorAddress GetAddr() const
```

## 参数说明

无

## 返回值

tensor地址。

## 约束说明

无

## 调用示例

```
1. auto addr0 = reinterpret_cast<void *>(0x10);
2. TensorData td(addr, nullptr);
3. auto addr1 = td.GetAddr(); // 0x10
```
