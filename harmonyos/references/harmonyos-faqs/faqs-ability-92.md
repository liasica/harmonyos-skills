---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-92
title: 如何在App启动时让各种权限弹窗的申请自动弹出
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在App启动时让各种权限弹窗的申请自动弹出
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c85a0d5e38aee5f4f906c8e0112ffd2a6a699ea836140398f0e75f91f6cb1dcd
---

将requestPermissionsFromUser接口放到EntryAbility.ets文件的loadContent回调中，参考代码如下：

```
1. windowStage.loadContent('pages/Index', (err) => {
2. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
3. atManager.requestPermissionsFromUser(this.context, ['ohos.permission.ACCESS_BLUETOOTH'])
4. .then((data: PermissionRequestResult) => {
5. console.info('data:' + JSON.stringify(data));
6. console.info('data permissions:' + data.permissions);
7. console.info('data authResults:' + data.authResults);
8. }).catch((err: BusinessError) => {
9. console.error('data:' + JSON.stringify(err));
10. });
11. });
```

[EntryAbilityRequest.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/entryability/EntryAbilityRequest.ets#L28-L38)

在设置文件中声明目标权限：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.ACCESS_BLUETOOTH",
4. "usedScene": {
5. "abilities": [
6. "EntryAbility"
7. ],
8. "when": "inuse"
9. },
10. "reason": "$string:app_name"
11. }
12. ],
```

[module\_request.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/module_request.json5#L10-L21)

**参考链接**

[abilityAccessCtrl.createAtManager](../harmonyos-references/js-apis-abilityaccessctrl.md#abilityaccessctrlcreateatmanager)
