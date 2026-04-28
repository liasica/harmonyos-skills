---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-kit-1
title: 如何申请精确定位
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何申请精确定位
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ecb56fbef974ffa72ee9fa93f843ddc5684fdbe7cbfa21f52b1cd8c2fea56b63
---

**问题场景**

在获取定位权限的场景中，申请了模糊定位和精准定位的权限['ohos.permission.APPROXIMATELY\_LOCATION', 'ohos.permission.LOCATION']。模糊定位会弹出权限框，点击同意后，再申请精准定位时，精准定位结果grantStatus返回2表示什么？

**解决措施**

精准定位结果grantStatus返回2，表示未授权，请求无效可能原因有：未在设置文件中声明目标权限、权限名非法、部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件。其他相应请求权限，返回的错误码，可参考[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)。

```
1. import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ApplyPrecisePositioning {
7. permissions: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'];

9. aboutToAppear(): void {
10. this.reqPermissionsFromUser(this.permissions);
11. }

13. reqPermissionsFromUser(permissions: Array<Permissions>): void {
14. let context: Context = getContext(this) as common.UIAbilityContext;
15. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
16. // RequestPermissionsFromUser will determine whether to trigger a pop-up window based on the authorization status of the permission
17. atManager.requestPermissionsFromUser(context, permissions).then((data: PermissionRequestResult) => {
18. let grantStatus: Array<number> = data.authResults;
19. let length: number = grantStatus.length;
20. for (let i = 0; i < length; i++) {
21. if (grantStatus[i] === 0) {
22. // User authorization allows continued access to the target operation
23. } else {
24. // The user refuses authorization, prompting the user that authorization is required to access the functionality of the current page, and guiding the user to open the corresponding permissions in the system settings
25. this.getUIContext().getPromptAction().showToast({ message: 'User refuses authorization' });
26. return;
27. }
28. }
29. // Authorization successful
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
32. })
33. }

35. build() {
36. }
37. }
```

[ApplyPrecisePositioning.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocationKit/entry/src/main/ets/pages/ApplyPrecisePositioning.ets#L21-L57)
