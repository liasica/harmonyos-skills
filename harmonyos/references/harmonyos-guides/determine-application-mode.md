---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/determine-application-mode
title: 选择申请权限的方式
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 选择申请权限的方式
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:85be939b472f32edc4a0f7aa8d8f00f25097ecee3e213363bbdb6ee25a7d06c6
---

应用访问数据或执行操作时，需评估是否需要相关权限。如需权限，应在应用安装包中申请。

每个权限的等级和[授权方式](app-permission-mgmt-overview.md#授权方式)不同，因此申请权限的方式也不同。申请权限前，开发者需要：

1. 根据API接口中的“需要权限”或“@permission”字段，确认权限名称，通过[权限列表](app-permissions.md)页面检索确认权限类型。
2. 参考操作路径，申请相应的权限。

根据目标权限的开放范围和授权方式，开发者可以参考以下操作路径申请权限。

## 应用申请权限的方式

| 权限类型 | 授权方式 | 操作路径 |
| --- | --- | --- |
| [开放权限（系统授权）](permissions-for-all.md) | system\_grant | [声明权限](declare-permissions.md) > 访问接口 |
| [开放权限（用户授权）](permissions-for-all-user.md) | user\_grant | [声明权限](declare-permissions.md) > [向用户申请授权](request-user-authorization.md) > 访问接口 |
| [受限开放权限（系统授权）](restricted-permissions.md) | system\_grant | [申请使用受限权限](declare-permissions-in-acl.md) > [声明权限](declare-permissions.md) > 访问接口 |
| [受限开放权限（用户授权）](restricted-permissions.md) | user\_grant | [申请使用受限权限](declare-permissions-in-acl.md) > [声明权限](declare-permissions.md) > [向用户申请授权](request-user-authorization.md) > 访问接口 |
