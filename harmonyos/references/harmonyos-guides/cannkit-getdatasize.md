---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdatasize
title: GetDataSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > GetDataSize
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00ea2003b5963b10c2a4a2be44ae802b4f7326222822e7600f3b3b70745cbc5d
---

## 函数功能

获取tiling data长度。

## 函数原型

```
1. size_t GetDataSize() const;
```

## 参数说明

无

## 返回值

tiling data长度。

## 约束说明

无

## 调用示例

```
1. auto td_buf = TilingData::CreateCap(100U);
2. auto td = reinterpret_cast<TilingData *>(td_buf.get());
3. size_t data_size = td->GetDataSize(); // 0

5. td->SetDataSize(100U);
6. data_size = td->GetDataSize(); // 100
```
