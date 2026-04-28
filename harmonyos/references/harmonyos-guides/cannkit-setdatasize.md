---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdatasize
title: SetDataSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > SetDataSize
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b19f6b6001dde8c2c992fdfcd469a02e7d1ec5c8c8a85cf92d0698385014dab0
---

## 函数功能

设置tiling data长度。

## 函数原型

```
1. void SetDataSize(const size_t size);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| size | 输入 | tiling data长度。 |

## 返回值

无

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
