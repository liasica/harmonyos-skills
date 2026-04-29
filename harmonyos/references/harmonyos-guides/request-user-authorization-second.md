---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization-second
title: 再次向用户申请授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 再次向用户申请授权
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:062fa7711aa5405229958c7ff79b1788767c6afa2d9abbcb93940dc5a4f14b4f
---

当应用通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)拉起弹框[请求用户授权](request-user-authorization.md)时，如果用户拒绝授权，应用将无法再次通过requestPermissionsFromUser()拉起弹框。用户需要在系统设置中手动授权。

在“设置”应用中的路径如下：

* 路径一：设置 > 隐私与安全 > 权限类型（如位置信息） > 具体应用
* 路径二：设置 > 应用和元服务 > 某个应用

应用也可以通过调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，直接拉起权限设置弹框，引导用户授权。

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/nhTkeNwAR7ego7BQhG-HGQ/zh-cn_image_0000002558764854.png?HW-CC-KV=V1&HW-CC-Date=20260429T053033Z&HW-CC-Expire=86400&HW-CC-Sign=A03D67B61C51C7E8C7F0C1D25DB41E3FE893344407CDC81578196D150E38326E)

以下示例代码展示了如何再次拉起弹框申请ohos.permission.APPROXIMATELY\_LOCATION权限。

```
1. import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // ···
5. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
6. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. atManager.requestPermissionOnSetting(context, ['ohos.permission.APPROXIMATELY_LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
8. console.info(`requestPermissionOnSetting success, result: ${data}`);
9. }).catch((err: BusinessError) => {
10. console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
11. });
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/RequestUserAuthorization/entry/src/main/ets/secondpages/Index.ets#L18-L39)
