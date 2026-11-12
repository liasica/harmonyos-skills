---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization-second
title: 再次向用户申请授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 再次向用户申请授权
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2d5838b7dcdf7ba8911e5603f9b63d2896ec61cae1a8f3f2efb1903a5bbb7e99
---

当应用通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)拉起弹框[请求用户授权](request-user-authorization.md)时，如果用户拒绝授权，应用将无法再次通过requestPermissionsFromUser()拉起弹框。用户需要在系统设置中手动授权。

在“设置”应用中的路径如下：

* 路径一：设置 > 隐私与安全 > 权限类型（如位置信息） > 具体应用
* 路径二：设置 > 应用和元服务 > 某个应用

应用也可以通过调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，直接拉起权限设置弹框，引导用户授权。

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/6Y0f6yoWTpCNVtlCZooE7g/zh-cn_image_0000002815399131.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB9B32A9402E961CC845876E6FF1015C1BC0357A0B03A2928D8AA18BA3E9D7D6)

以下示例代码展示了如何再次拉起弹框申请ohos.permission.APPROXIMATELY\_LOCATION权限。

```typescript
import { abilityAccessCtrl, Context, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// ···
          let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
          let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          atManager.requestPermissionOnSetting(context, ['ohos.permission.APPROXIMATELY_LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
            console.info(`requestPermissionOnSetting success, result: ${data}`);
          }).catch((err: BusinessError) => {
            console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
          });
```
