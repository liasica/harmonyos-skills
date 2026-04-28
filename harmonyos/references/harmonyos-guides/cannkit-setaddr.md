---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setaddr
title: SetAddr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > SetAddr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:089740312dd4dca3f0b8cfbb8304a5373606dea290c2306b26746e7a5329ce7d
---

## 函数功能

设置tensor地址。

## 函数原型

```
1. ge::graphStatus SetAddr(const ConstTensorAddressPtr addr, TensorAddrManager manager)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| addr | 输入 | tensor地址。  using ConstTensorAddressPtr = const void \*; |
| manager | 输入 | tensor的管理函数。 |

## 返回值

成功时返回ge::GRAPH\_SUCCESS；失败时返回manager管理函数中定义的错误码。

## 约束说明

无

## 调用示例

```
1. auto addr = reinterpret_cast<void *>(0x10);
2. TensorData td(addr, nullptr);
3. td.SetAddr(addr, HostAddrManager);
```
