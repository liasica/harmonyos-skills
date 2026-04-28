---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getworkspacesizes
title: GetWorkspaceSizes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetWorkspaceSizes
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c4b83d6dd52552f3e313c94f66453b82ef3469203a874e7201412ae9df2c4c0
---

## 函数功能

获取workspace sizes指针。

## 函数原型

```
1. size_t *GetWorkspaceSizes(const size_t workspace_count);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| workspace\_count | 输入 | workspace的个数，传入的workspace个数不可以超过编译时指定的最大workspace个数。 |

## 返回值

workspace sizes指针。

## 约束说明

传入的workspace个数不可以超过编译时指定的最大workspace个数。

当前Kirin9020支持的最大的workspace是8个。

当前KirinX90支持的最大的workspace是8个。

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto ws = context->GetWorkspaceSizes(5);
3. // ...
4. }
```
