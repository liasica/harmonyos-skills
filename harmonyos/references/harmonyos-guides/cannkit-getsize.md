---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsize
title: GetSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > GetSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e73b34a99cc12afd220112fdc0118a6164ae4c9269fb3dcfcc1f631d2b41e27c
---

## 函数功能

获取tensor数据的内存大小。

## 函数原型

```cpp
size_t GetSize() const
```

## 参数说明

无

## 返回值

tensor所占内存大小，单位为字节。

## 约束说明

无

## 调用示例

```cpp
auto addr = reinterpret_cast<void *>(0x10);
TensorData td(addr, HostAddrManager, 100U, kOnHost);
auto td_size = td.GetSize(); // 100U
```
