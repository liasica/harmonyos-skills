---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tilingdata-getdata
title: GetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingData > GetData
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:849f51049b7da5447953df1209a461514ab23854ba5dd0f66eee1bd7dd2a071c
---

## 函数功能

获取TilingData的数据指针。

## 函数原型

```
1. void *GetData();
2. const void *GetData() const;
```

## 参数说明

无

## 返回值

data指针。

## 约束说明

无

## 调用示例

```
1. auto td_buf = TilingData::CreateCap(100U);
2. auto td = reinterpret_cast<TilingData *>(td_buf.get());
3. auto tiling_data_ptr = td->GetData(); // td_buf.get() + sizeof(TilingData)
```
