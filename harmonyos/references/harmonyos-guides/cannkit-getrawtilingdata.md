---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrawtilingdata
title: GetRawTilingData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetRawTilingData
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1986523ca32b23d4ccfdaf5a443bc58402a4e7542a5e1ac7aa459e85828d5ebf
---

## 函数功能

获取无类型的tiling data指针。

## 函数原型

```
1. TilingData *GetRawTilingData();
```

## 参数说明

无

## 返回值

tiling data指针，失败时返回空指针。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto tiling_data = context->GetRawTilingData();
3. // ...
4. }
```
