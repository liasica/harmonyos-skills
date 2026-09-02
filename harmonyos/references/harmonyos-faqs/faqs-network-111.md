---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-111
title: 使用权限申请，没有拉起弹窗，可能原因是什么
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 使用权限申请，没有拉起弹窗，可能原因是什么
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f410b4cbdc69f8831526f3e70a523c7e9b3ddeeb8f20c166c382079729d9f560
---

## 问题现象

使用权限申请，没有拉起弹窗，可能原因是什么？

```ts
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let context = this.getUIContext().getHostContext() as common.UIAbilityContext
let needPermissions:Permissions[] = ['ohos.permission.ACCESS_BLUETOOTH','ohos.permission.USE_BLUETOOTH'];
atManager.requestPermissionsFromUser(context, needPermissions, (err: BusinessError, data: PermissionRequestResult) => {
  if (err) {
    Logger.p(`requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
  } else {
    Logger.p('data:' + JSON.stringify(data));
    Logger.p('data permissions:' + data.permissions);
    Logger.p('data authResults:' + data.authResults);
    Logger.p('data dialogShownResults:' + data.dialogShownResults);
  }
});
```

## 解决方案

当前申请的ACCESS\_BLUETOOTH和USE\_BLUETOOTH权限，只有ACCESS\_BLUETOOTH是需要用户授权的，[USE\_BLUETOOTH](../harmonyos-guides/permissions-for-all.md#ohospermissionuse_bluetooth)是通过系统授权。

需确认module.json5中是否已配置这两个权限。若是权限申请后没有弹窗提醒，可能是您已经成功授权过，或者已经默认拒绝了该权限，需检查应用是否已经授权。还可以通过拉起设置页面手动进行授权设置。
