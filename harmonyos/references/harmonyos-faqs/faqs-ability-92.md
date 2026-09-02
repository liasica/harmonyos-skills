---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-92
title: 如何在App启动时让各种权限弹窗的申请自动弹出
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在App启动时让各种权限弹窗的申请自动弹出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb4b7ed005010349f8990774ed4bc8d6ae8b0ad0d6a64317ba62a4b81f8bf0b7
---

将requestPermissionsFromUser接口放到EntryAbility.ets文件的loadContent回调中，参考代码如下：

```typescript
windowStage.loadContent('pages/Index', (err) => {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionsFromUser(this.context, ['ohos.permission.ACCESS_BLUETOOTH'])
    .then((data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    }).catch((err: BusinessError) => {
    console.error('data:' + JSON.stringify(err));
  });
});
```

在设置文件中声明目标权限：

```json
"requestPermissions": [
  {
    "name": "ohos.permission.ACCESS_BLUETOOTH",
    "usedScene": {
      "abilities": [
        "EntryAbility"
      ],
      "when": "inuse"
    },
    "reason": "$string:app_name"
  }
],
```

**参考链接**

[abilityAccessCtrl.createAtManager](../harmonyos-references/js-apis-abilityaccessctrl.md#abilityaccessctrlcreateatmanager)
