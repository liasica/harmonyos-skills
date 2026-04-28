---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-resetdata
title: ResetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > ResetData
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb2cb9343ab8bb7154d2f80b42187a4cc9f7b103b85f9873dff82198a1b06f5c
---

## 函数功能

释放Tensor中数据内存。

## 函数原型

```
1. std::unique_ptr<uint8_t[], Tensor::DeleteFunc> ResetData();
```

## 参数说明

无

## 返回值

返回释放后的内存地址和删除器。

## 异常处理

无

## 约束说明

无
