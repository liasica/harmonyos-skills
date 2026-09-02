---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-15
title: 如何判断应用权限是否允许，以及拒绝后再次授权
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 如何判断应用权限是否允许，以及拒绝后再次授权
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:9ceff8eb9a74e7215b4fcc72580c58de3f7e7bab3d1e9b020d2b1da64422337d
---

## 问题现象

调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口申请相关权限，用户拒绝后，后续再调用requestPermissionsFromUser()接口不会弹出授权弹窗。

## 背景知识

* 应用在申请权限时，需要在项目的配置文件中逐个声明需要的权限，否则应用将无法获取授权，详情请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
* 当应用需要访问用户的隐私信息或使用系统能力时，例如获取位置信息、访问日历、使用相机拍摄照片或录制视频等，应该向用户请求授权，详情请参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。

## 解决方案

为避免过度打扰用户，系统限制频繁弹出权限请求，如果调用requestPermissionsFromUser()接口被用户拒绝授权，将无法再次弹出窗口，此时可使用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)二次拉起权限弹窗，或者引导用户跳转到系统设置的权限页进行手动开启权限，具体操作如下：

1. **权限检查：**

   申请相关权限前应使用[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)检查是否有该权限，若无权限则进行如下操作。

   使用requestPermissionsFromUser()接口请求相应的权限时，系统会拉起权限弹窗。示例代码如下：

   ```ts
   let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   atManager.requestPermissionsFromUser(context, ['ohos.permission.APPROXIMATELY_LOCATION'], (err: BusinessError, data: PermissionRequestResult) => {
     if (err) {
       console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
     } else {
       console.info(`requestPermissionsFromUser success, result: ${data}`);
       console.info('requestPermissionsFromUser data permissions:' + data.permissions);
       console.info('requestPermissionsFromUser data authResults:' + data.authResults);
       console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
     }
   });
   ```
2. **二次向用户申请授权：**

   用户已经拒绝过该权限则不会再次弹出，需要引导用户开启权限有以下两种方案。

   * **方案一**：

     调用requestPermissionOnSetting()二次拉起权限设置弹窗，示例代码如下：

     ```ts
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     atManager.requestPermissionOnSetting(context, ['ohos.permission.APPROXIMATELY_LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
       console.info(`requestPermissionOnSetting success, result: ${data}`);
     }).catch((err: BusinessError) => {
       console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
     });
     ```

     **说明** 

     应适度使用requestPermissionOnSetting()方法进行权限请求。
   * **方案二**：

     可以引导用户点击跳转到对应应用的权限页面，让用户手动授权，示例代码如下：

     ```ts
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     context?.startAbility({
       bundleName: 'com.huawei.hmos.settings',
       abilityName: 'com.huawei.hmos.settings.MainAbility',
       uri: 'systemui_notification_settings', // uri为空的时候，拉起设置主页面
       parameters: {
         pushParams: {
           bundleName: 'com.example.multishopping' // 传要跳转的对应应用的包名
         }
       }
     });
     ```

完整示例代码如下：

```ts
import { abilityAccessCtrl, Context, PermissionRequestResult, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@ComponentV2
struct GetPermission {
  build() {
    Column() {
      Button('权限检查').onClick(() => {
        let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        atManager.requestPermissionsFromUser(context, ['ohos.permission.APPROXIMATELY_LOCATION'], (err: BusinessError, data: PermissionRequestResult) => {
          if (err) {
            console.error(`requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
          } else {
            console.info(`requestPermissionsFromUser success, result: ${data}`);
            console.info('requestPermissionsFromUser data permissions:' + data.permissions);
            console.info('requestPermissionsFromUser data authResults:' + data.authResults);
            console.info('requestPermissionsFromUser data dialogShownResults:' + data.dialogShownResults);
          }
        });
      });
      Button('二次拉起权限设置弹框').onClick(() => {
        let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        atManager.requestPermissionOnSetting(context, ['ohos.permission.APPROXIMATELY_LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
          console.info(`requestPermissionOnSetting success, result: ${data}`);
        }).catch((err: BusinessError) => {
          console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
        });
      });
      Button('引导用户手动开启权限').onClick(() => {
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        context?.startAbility({
          bundleName: 'com.huawei.hmos.settings',
          abilityName: 'com.huawei.hmos.settings.MainAbility',
          uri: 'systemui_notification_settings', // uri为空的时候，拉起设置主页面
          parameters: {
            pushParams: {
              bundleName: 'com.example.multishopping' // 传要跳转的对应应用的包名
            }
          }
        });
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：调用requestPermissionOnSetting()接口无法拉起系统二次授权弹窗，报错12100001。

A：参考[错误码信息](../harmonyos-references/errorcode-access-token.md)，二次授权需要保证当次申请的所有权限在同一个[权限组](../harmonyos-guides/app-permission-group-list.md)中。

Q：在首次申请用户授权弹窗弹出时不进行选择授权方式，直接返回上一级、返回应用后台或退出应用会有什么结果？

A：首次申请用户授权弹窗弹出时不进行选择授权方式直接返回，会默认用户选择拒绝授权，在应用权限设置页面可以看到应用对应权限为关闭状态；再次调用申请用户授权接口dialogShownResults参数会返回false，表示非首次调用申请用户授权接口。

Q：可以跳转应用总权限页，如何跳转到各自的权限详情页？

A：目前不支持跳转到应用单个权限详情页。

Q：申请用户权限没有弹出对应的提示框？

A：参考权限[APP\_TRACKING\_CONSENT](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapp_tracking_consent)，部分权限在申请时，有开关去控制是否弹窗向用户请求授权。开关关闭，当应用请求权限时，系统不会弹窗，默认授予应用权限。

Q：abilityAccessCtrl.AtManager.on('selfPermissionStateChange')监听权限变化报错401。

A：[abilityAccessCtrl.AtManager.on()](../harmonyos-references/js-apis-abilityaccessctrl.md#on18)接口为API18开始启用，需要检查SDK和系统版本是否在API18及以上。

Q：申请ohos.permission.APP\_TRACKING\_CONSENT权限时，部分设备弹出授权弹窗，部分设备未弹出，哪种行为是正确的？

A：两种行为都是正确的。是否弹窗向用户请求授权，取决于"要求应用请求关联"的开关状态。如果开关关闭，当应用请求权限时，系统不会弹窗，默认授予应用权限；如果开关开启，当应用请求权限时，系统将弹窗，需要用户确认才能授予应用权限。"要求应用请求关联"的开关状态可在"设置 > 隐私与安全 > 跨应用关联"页面中查看，详情参考[ohos.permission.APP\_TRACKING\_CONSENT](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapp_tracking_consent)。

## 总结

当用户触发需要使用权限的场景时，首先使用checkAccessToken()判断当前是否已经授权，如果已经授权，则可以直接访问目标操作，否则需要向用户申请授权。调用requestPermissionsFromUser()方法可以向用户申请授权。若之前已经拒绝过该权限，可使用requestPermissionOnSetting()二次拉起权限弹窗，或者引导用户跳转到系统设置的权限页进行手动开启权限。
