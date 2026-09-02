---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdatasize
title: SetDataSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > SetDataSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f949f9c3be0e601c79513e3ae4281f4728e77c50de035b5a489cdd97271c4db
---

## 函数功能

设置tiling data长度。

## 函数原型

```cpp
void SetDataSize(const size_t size);
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

```cpp
auto td_buf = TilingData::CreateCap(100U);
auto td = reinterpret_cast<TilingData *>(td_buf.get());
size_t data_size = td->GetDataSize(); // 0
 
td->SetDataSize(100U);
data_size = td->GetDataSize(); // 100
```
