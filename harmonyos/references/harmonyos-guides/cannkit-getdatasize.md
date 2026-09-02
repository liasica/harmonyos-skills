---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdatasize
title: GetDataSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > GetDataSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc4bb5afc494925f8c06d81791cb737aeee03a76b2fb01ab7555bc470d4d1a1b
---

## 函数功能

获取tiling data长度。

## 函数原型

```cpp
size_t GetDataSize() const;
```

## 参数说明

无

## 返回值

tiling data长度。

## 约束说明

无

## 调用示例

```cpp
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
size_t data_size = td->GetDataSize(); // 0
 
td->SetDataSize(100U);
data_size = td->GetDataSize(); // 100
```
