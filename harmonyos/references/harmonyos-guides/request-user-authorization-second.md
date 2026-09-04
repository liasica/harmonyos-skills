---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization-second
title: 再次向用户申请授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 再次向用户申请授权
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50f0a0c616a0c05acee6e202369332da03e08ee6d05d71e00bebdcbd50b76681
---

当应用通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)拉起弹框[请求用户授权](request-user-authorization.md)时，如果用户拒绝授权，应用将无法再次通过requestPermissionsFromUser()拉起弹框。用户需要在系统设置中手动授权。

在“设置”应用中的路径如下：

* 路径一：设置 > 隐私与安全 > 权限类型（如位置信息） > 具体应用
* 路径二：设置 > 应用和元服务 > 某个应用

应用也可以通过调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，直接拉起权限设置弹框，引导用户授权。

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ihMyNlHwQsmVTfaC2q1yrg/zh-cn_image_0000002712404454.png)

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
