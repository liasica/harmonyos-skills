---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/location-kit-troubleshooting-0001
title: 应用获取定位权限问题排查与解决
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 故障排查 > 应用获取定位权限问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:29+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:5a32ac9cbf6bfe350be7c0599e241cff7b6b02e4b613e9f1a5e7bda019650340
---

## 应用后台获取定位权限

### 问题现象

应用处于后台，如何获取定位权限？

### 定位过程

1. module.json5是否配置定位权限，如果有后台任务是否配置后台定位权限。
2. 询问用户授权时，需要使用定位权限组，同时判断多个定位权限。

### 分析结论

1. 始终允许权限需要在ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION的基础上增加后台定位权限ohos.permission.LOCATION\_IN\_BACKGROUND，由于安全隐私要求，应用不能通过弹窗的形式被授予后台位置权限，应用如果需要使用后台位置权限，需要引导用户到设置界面手动授予。
2. 对于定位权限来说，模糊定位和精准定位权限要一起申请授权。LocationButton从API Version 15开始不再维护，推荐使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)。

### 修改建议

1. 应用应通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限。用户在设置界面中的选择"始终允许"应用访问位置信息权限，完成手动授予。设置路径：路径一：设置->隐私与安全->位置->具体应用。路径二：设置->应用和元服务->具体应用->位置。
2. 同时判断ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。代码参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)开发步骤第3步：动态向用户申请授权。

## LocationButton申请定位权限无弹窗

### 问题现象

判断是否有定位权限，一直是没有授权，然后用LocationButton重新申请的时候，result一直是"1"，没有弹窗提醒授权。

```ts
import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';

@Entry
@Component
export struct Test {
  build() {
  }

  async checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

    // 获取应用程序的accessTokenID
    let tokenId: number = 0;
    let bundleInfo: bundleManager.BundleInfo =
      await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    console.info('Succeeded in getting Bundle.');
    let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
    tokenId = appInfo.accessTokenId;

    // 校验应用是否被授予权限
    grantStatus = await atManager.checkAccessToken(tokenId, permission);
    console.info('Succeeded in checking access token.');
    return grantStatus;
  }

  async checkPermissions1(): Promise<boolean> {
    let grantStatus1: boolean = await this.checkPermissionGrant('ohos.permission.LOCATION') ===
    abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED; // 获取精确定位权限状态
    let grantStatus2: boolean = await this.checkPermissionGrant('ohos.permission.APPROXIMATELY_LOCATION') ===
    abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED; // 获取模糊定位权限状态

    // 根据权限状态采取相应措施
    if (grantStatus1 && grantStatus2) {
      console.info('已获得所有必要的定位权限，可以继续进行操作。');
      return true
    } else if (grantStatus1 || grantStatus2) {
      console.info('已获得部分定位权限，需要申请剩余权限。');
      return false
    } else {
      console.info('未获得任何定位权限，需要向用户申请权限。');
      return false
    }
  }
}
```

### 定位过程

1. module.json5是否配置定位权限，如果有后台任务是否配置后台定位权限。
2. 询问用户授权时，需要使用定位权限组，同时判断多个定位权限。

### 分析结论

1. 始终允许权限需要在ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION的基础上增加后台定位权限ohos.permission.LOCATION\_IN\_BACKGROUND，由于安全隐私要求，应用不能通过弹窗的形式被授予后台位置权限，应用如果需要使用后台位置权限，需要引导用户到设置界面手动授予。
2. 对于定位权限来说，模糊定位和精准定位权限要一起申请授权。LocationButton从API Version 15开始不再维护，推荐使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)。

### 修改建议

1. 应用应通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限。用户在设置界面中的选择"始终允许"应用访问位置信息权限，完成手动授予。设置路径：路径一：设置->隐私与安全->位置->具体应用。路径二：设置->应用和元服务->具体应用->位置。
2. 同时判断ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。代码参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)开发步骤第3步：动态向用户申请授权。
