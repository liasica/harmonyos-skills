---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-10
title: 在系统设置修改了应用权限，应用能否监听到权限变化
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 在系统设置修改了应用权限，应用能否监听到权限变化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bf6ca40915a66c5c5ed3054794fa050ed453afe99a22ee414decbcd1c14766b6
---

使用[on](../harmonyos-references/js-apis-abilityaccessctrl.md#on18)可以监听应用权限变化，示例代码中监听的是ohos.permission.APPROXIMATELY\_LOCATION权限变化，需要在module.json5进行相应的权限声明，参考代码如下：

```
1. import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct Index {
6. aboutToAppear(): void {
7. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
8. let permissionList: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION'];
9. try {
10. atManager.on('selfPermissionStateChange', permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
11. console.info('receive permission state change, data:' + JSON.stringify(data));
12. });
13. } catch (err) {
14. console.error(`catch err->${JSON.stringify(err)}`);
15. }
16. }

18. build() {
19. // ...
20. }
21. }
```

[MonitorChangesInPermissions.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/MonitorChangesInPermissions.ets#L21-L41)
