---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-9
title: OpenID和UnionID的格式说明
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > OpenID和UnionID的格式说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:78845243a0dcd759b51070dead254650379467eb8dc96593610d051fb54def4b
---

## 长度

为减少开发者接入和迁移成本，Account Kit在2023年09月21日对OpenID、UnionID的长度做出了如下调整：

* OpenID

  + 应用创建时间晚于（含）2023年09月21日 23:00:00，OpenID固定28位。
  + 应用创建时间早于2023年09月21日 23:00:00，OpenID长度不固定，限制在1-256位。
* UnionID

  + 开发者账号注册时间晚于（含）2023年09月21日 23:00:00，UnionID固定29位。
  + 开发者账号注册时间早于2023年09月21日 23:00:00，UnionID长度不固定，限制在1-92位。

## 唯一性标识

1. 开发者账号下管理了多个应用时，针对同一个华为账号，不同的应用返回的OpenID值不同，但返回的UnionID相同。
2. 如果开发者账号下管理了多个应用，并且这些应用需要共享同一个华为账号的用户信息，可以使用UnionID作为用户标识。

## 数据类型

OpenID和UnionID均是字符串类型的数据。

## 大小写敏感

OpenID和UnionID严格区分大小写。

## 实际应用中的注意事项

在存储、查询、比较OpenID或UnionID时，请务必保持其原始的大小写格式。
