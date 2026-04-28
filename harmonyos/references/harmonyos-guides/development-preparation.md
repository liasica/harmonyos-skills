---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/development-preparation
title: 开发准备
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b90e1e7fde95516d4758747d220096be52e3166c0c66b20e5f61bda534e8e27
---

## 申请权限

应用在使用Ads Kit能力前，需要检查是否已经获取对应权限。如未获得授权，需要声明对应权限。

Ads Kit所需的权限有：

* ohos.permission.INTERNET：用于请求和展示广告、回传竞价结果。
* ohos.permission.APP\_TRACKING\_CONSENT：用于获取开放匿名设备标识符。

在模块的module.json5中配置所需申请的权限，其中跨应用关联权限[ohos.permission.APP\_TRACKING\_CONSENT](permissions-for-all-user.md#ohospermissionapp_tracking_consent)为user\_grant权限，reason和abilities标签必填，配置方式参见[requestPermissions标签说明](declare-permissions.md#在配置文件中声明权限)。

示例代码如下所示：

```
1. {
2. "module": {
3. "requestPermissions": [
4. {
5. "name": "ohos.permission.APP_TRACKING_CONSENT",
6. "reason": "$string:reason",
7. "usedScene": {
8. "abilities": [
9. "EntryAbility"
10. ],
11. "when": "inuse"
12. }
13. },
14. {
15. "name": "ohos.permission.INTERNET"
16. }
17. ]
18. }
19. }
```
