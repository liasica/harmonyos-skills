---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplatforminfo
title: GetPlatformInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetPlatformInfo
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2ff549223fca305fb5571f8100347a7fed87ba7676a3d2a92c242111ef0a838f
---

## 函数功能

获取fe::PlatFormInfos指针。

## 函数原型

```
1. fe::PlatFormInfos *GetPlatformInfo() const
```

## 参数说明

无

## 返回值

fe::PlatFormInfos指针。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto platform_info = context->GetPlatformInfo();
3. // ...
4. }
```
