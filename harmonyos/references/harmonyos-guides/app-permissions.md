---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-permissions
title: 应用权限列表
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 应用权限列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b69a7cfcce8bc0c23299aa01953f4c22ed36e79bdaaa2e57d0bb5a3b298a2651
---

根据权限的开放范围和授权方式不同，申请对应权限的方式也不同。

系统当前存在以下权限列表，开发者可根据实际需求进行检索，并确定对应权限的申请方式。

* [开放权限（系统授权）](permissions-for-all.md)

  所有应用可申请。应用申请了此类权限后，系统将在用户安装应用时，自动把相应权限授予给应用。
* [开放权限（用户授权）](permissions-for-all-user.md)

  所有应用可申请。应用申请了此类权限后，还需要在应用动态运行时，通过发送弹窗的方式请求用户授权。
* [受限开放权限](restricted-permissions.md)

  面向普通应用开放的system\_basic权限。
* [企业类应用可用权限](permissions-for-enterprise-apps.md)

  仅面向企业普通应用、MDM应用开放。分发类型（app-distribution-type）为enterprise\_normal（企业普通应用）、enterprise\_mdm（MDM应用）的应用可申请。应用在申请时，需确认其授权方式，按照合适的方式申请。
* [MDM应用可用权限](permissions-for-mdm-apps.md)

  仅[MDM](mdm-kit-intro.md)应用可申请。应用在申请时，需确认其授权方式，按照合适的方式申请。

* **[开放权限（系统授权）](permissions-for-all.md)**
* **[开放权限（用户授权）](permissions-for-all-user.md)**
* **[受限开放权限](restricted-permissions.md)**
* **[企业类应用可用权限](permissions-for-enterprise-apps.md)**
* **[仅MDM应用可用权限](permissions-for-mdm-apps.md)**
