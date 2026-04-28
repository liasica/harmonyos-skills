---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettilingcond
title: GetTilingCond
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetTilingCond
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58ddf07e8ae1970000557ebeef9b884bc8ae515128aa592038a9905c144e761d
---

## 函数功能

获取tiling cond。

## 函数原型

```
1. int32_t GetTilingCond() const;
```

## 参数说明

无

## 返回值

tiling cond:

若返回值大于等于0，代表此tiling cond为有效的tiling cond。

若返回值为-1，代表此tiling cond为无效的tiling cond。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto tiling_cond = context->GetTilingCond();
3. // ...
4. }
```
