---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/development-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-05-13
content_hash: sha256:fa4f81fdf0922ad08d26e27fab466e97145fd507dfea625eb01885684119598f
---

## 申请权限

应用在使用Ads Kit能力前，需要检查是否已经获取对应权限。如未获得授权，需要声明对应权限。

Ads Kit所需的权限有：

* ohos.permission.INTERNET：用于请求和展示广告、回传竞价结果。
* ohos.permission.APP\_TRACKING\_CONSENT：用于获取开放匿名设备标识符。

在模块的module.json5中配置所需申请的权限，其中跨应用关联权限[ohos.permission.APP\_TRACKING\_CONSENT](permissions-for-all-user.md#ohospermissionapp_tracking_consent)为user\_grant权限，reason和abilities标签必填，配置方式参见[requestPermissions标签说明](declare-permissions.md#在配置文件中声明权限)。

示例代码如下所示：

```typescript
{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.APP_TRACKING_CONSENT",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.INTERNET"
      }
    ]
  }
}
```
