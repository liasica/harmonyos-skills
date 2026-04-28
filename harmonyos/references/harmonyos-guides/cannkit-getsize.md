---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsize
title: GetSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > GetSize
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56d099e1625c6653c17738ebc9c1e88dcdb7fb2bf821ff5dfd325b1353e33740
---

## 函数功能

获取tensor数据的内存大小。

## 函数原型

```
1. size_t GetSize() const
```

## 参数说明

无

## 返回值

tensor所占内存大小，单位为字节。

## 约束说明

无

## 调用示例

```
1. auto addr = reinterpret_cast<void *>(0x10);
2. TensorData td(addr, HostAddrManager, 100U, kOnHost);
3. auto td_size = td.GetSize(); // 100U
```
