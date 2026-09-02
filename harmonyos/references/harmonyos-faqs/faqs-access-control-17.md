---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-17
title: 使用了某些权限但是系统设置页不存在，应用内如何引导用户修改权限
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 使用了某些权限但是系统设置页不存在，应用内如何引导用户修改权限
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:38b1687270224101de4043b871af3e8a38686520a049859fae42c82c00feb0c5
---

## 问题现象

应用中使用了存储、相机、麦克风等权限，并做了跳转到系统设置-应用权限设置页的权限管理功能。但是有时候跳转到系统设置-应用权限设置页不存在上述权限，为什么？此时如何引导用户修改权限？

## 背景知识

[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)的回调函数可知应用是否已申请过该权限。

## 解决方案

1. 在API23之前，对于授权方式为用户授权的权限，系统设置-应用权限设置页不存在权限是因为应用的权限设置中只展示应用申请过的权限，该特性是系统规格，只有在调用requestPermissionsFromUser这个接口，并且用户选择是否授予权限之后，才会在应用详情页显示该权限开关。从API23开始，系统设置-应用权限设置页会展示所有权限。
2. 要在应用中的统一权限管理页引导用户管理权限，可以在进行跳转操作前，使用requestPermissionsFromUser申请该权限，此时有以下两种情况：
   * 如果用户未申请过权限，会弹出权限申请提示框，用户可以选择允许或拒绝授权权限，关闭权限弹框。
   * 如果用户已经申请过权限，可能接受或拒绝，不会弹出权限申请提示框，此时跳转到系统设置-应用权限设置页。

   **说明** 

   授权方式为用户授权的权限都需要[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

参考以下代码：

在配置文件module.json5中声明ohos.permission.MICROPHONE权限后：

```ts
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions, Want } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';

@Entry
@Component
struct PermissionManager {
  PERMISSION_LIST: Permissions[] = ["ohos.permission.MICROPHONE"];

  requestPermission(permissionList: Array<Permissions>) {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, permissionList).then((data: PermissionRequestResult) => {
      // dialogShowResults数组长度根据申请权限的数量判断，以下以单个权限申请为例
      if (data.dialogShownResults && data.dialogShownResults[0]) { // 用户首次申请，弹框
        let grantStatus: Array<number> = data.authResults;
        if (grantStatus[0] === 0) {
          // 用户授权，可以继续访问目标操作
        } else {
          // 用户拒绝授权，提示用户涉及该权限的功能无法继续使用
          return;
        }
      } else if (data.dialogShownResults && !data.dialogShownResults[0]) {
        // 非首次申请，跳转到系统设置页进行关闭或打开权限的操作
        bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT, (err, bundleInfo) => {
          if (err) {
            console.error(`Failed to getBundleInfoForSelf. Code: ${err.code}, message: ${err.message}`);
            return;
          }
          let want: Want = {
            bundleName: 'com.huawei.hmos.settings',
            abilityName: 'com.huawei.hmos.settings.MainAbility',
            uri: 'application_info_entry',
            // 传递你的应用的包名作为参数
            parameters: {
              pushParams: bundleInfo.name ?? ''
            }
          };
          context.startAbility(want)
            .then(() => {
              console.info('Success to startAbility');
            })
            .catch((err: BusinessError<Error>) => {
              console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
            });
        });
      }
    }).catch((err: BusinessError<Error>) => {
      console.error(`data: ${err}`);
    });
  }

  build() {
    Column() {
      Button('requestPermission')
        .onClick(() => {
          this.requestPermission(this.PERMISSION_LIST);
        })
    }
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%')
  }
}
```
