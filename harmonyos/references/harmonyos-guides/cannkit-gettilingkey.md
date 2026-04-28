---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingkey
title: GetTilingKey
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetTilingKey
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60aad4e12f6268ca94c6d8fd15e8b413dad9f61a3750bf79178de785f2cb0d03
---

## 函数功能

获取tiling key。

## 函数原型

```
1. uint64_t GetTilingKey() const;
```

## 参数说明

无

## 返回值

返回tiling key。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto tiling_key = context->GetTilingKey();
3. // ...
4. }
```
