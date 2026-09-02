---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-user-authentication-2
title: 如何检查当前应用程序是否已经被授予相关权限
breadcrumb: FAQ > 系统开发 > 安全 > 用户身份认证（User Authentication） > 如何检查当前应用程序是否已经被授予相关权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:1907b6f77112ce35f191e783af82bffc9afa100ebe05fe63abcf38a3ebe3eb6b
---

## 问题现象

如何检查当前应用程序是否已经被授予相关权限，例如：wifi权限、数据联网权限？

## 背景知识

检查用户是否已向您的应用授予特定权限，可以使用[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)函数，此方法会返回PERMISSION\_GRANTED或PERMISSION\_DENIED。

若需查询应用的网络访问策略（是否允许使用蜂窝、Wi-Fi网络上网），可以使用[policy.getNetAccessPolicy](../harmonyos-references/js-apis-net-policy.md#policygetnetaccesspolicy)接口。

## 解决方案

以检查应用是否具备wifi权限、数据联网权限为例：

1. 申请ohos.permission.GET\_WIFI\_INFO、ohos.permission.INTERNET权限。
2. 通过调用checkAccessToken()方法来校验当前是否已经授权。

参考代码如下：

```ts
import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct demo {
  @State message: string = '点击权限检查';
  @State wifiStatus: boolean = false;
  @State internetStatus: boolean = false;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('权限检查')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.checkPermissions();
          this.message = 'wifi权限' + this.wifiStatus + ",数据联网权限：" + this.internetStatus;
        })
    }
    .height('100%')
    .width('100%')
  }

  async checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;
    // 获取应用程序的accessTokenID。
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION); // 获取包含应用信息的 BundleInfo，比如应用名称、应用包名、应用组件
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;  // 获取`tokenId` ，它是 HarmonyOS 中用于应用权限管理的一个关键标识符
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to get bundle info for self. Code is ${err.code}, message is ${err.message}`);
    }

    // 校验应用是否被授予权限。
    try {
      grantStatus = await atManager.checkAccessToken(tokenId, permission);  // `checkAccessToken` 是 `atManager` 对象上的一个方法，用于验证给定的令牌ID和权限是否有效。
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to check access token. Code is ${err.code}, message is ${err.message}`);
    }
    return grantStatus;
  }

  async checkPermissions(): Promise<void> {
    let grantStatus1: boolean = await this.checkPermissionGrant('ohos.permission.GET_WIFI_INFO') ===
    abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    let grantStatus2: boolean = await this.checkPermissionGrant('ohos.permission.INTERNET') ===
    abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    console.info("wifi权限：" + grantStatus1);
    console.info("数据联网权限：" + grantStatus2);
    this.wifiStatus = grantStatus1;
    this.internetStatus = grantStatus2;
    return;
  }
}
```

若需查询应用是否允许使用蜂窝或Wi-Fi网络上网，可调用[policy.getNetAccessPolicy](../harmonyos-references/js-apis-net-policy.md#policygetnetaccesspolicy)接口查询自身应用的联网策略。
