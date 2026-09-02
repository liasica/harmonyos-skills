---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-resetdata
title: ResetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > ResetData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45fc34df635fcaaea8d6cdd17062040fbcebecc6c8a4fca42ec9186fbf25328f
---

## 函数功能

释放Tensor中数据内存。

## 函数原型

```cpp
std::unique_ptr<uint8_t[], Tensor::DeleteFunc> ResetData();
```

## 参数说明

无

## 返回值

返回释放后的内存地址和删除器。

## 异常处理

无

## 约束说明

无
