---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-preparations
title: 开发准备
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1b2e7b5e696ef6590354842339a820401944fb9d8543f77dda084667ceab7a1
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

## 申请权限

开发者需要根据实际场景申请对应权限，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[声明权限](declare-permissions.md)声明对应权限。

| 权限 | 使用场景 |
| --- | --- |
| ohos.permission.GET\_WIFI\_INFO | 使用场景化API获取Wi-Fi信息需要申请该权限（使用5.0.1(13)及以上版本时不需要设置该权限）。 |
| ohos.permission.ACCESS\_BLUETOOTH | 使用场景化API获取蓝牙信息需要申请该权限（使用5.0.1(13)及以上版本时不需要设置该权限）。 |

说明

获取用户程序访问控制权限可参考[程序访问控制管理](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。
