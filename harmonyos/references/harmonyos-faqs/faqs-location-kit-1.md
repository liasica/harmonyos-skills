---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-kit-1
title: 如何申请精确定位
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何申请精确定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:0218209dd4e0d880e70f18965c6677635044ab7f6a363b4511d45cd5be1ac650
---

## 问题场景

在获取定位权限的场景中，申请了模糊定位和精准定位的权限['ohos.permission.APPROXIMATELY\_LOCATION', 'ohos.permission.LOCATION']。模糊定位会弹出权限框，点击同意后，再申请精准定位时，精准定位结果grantStatus返回2表示什么？

## 解决措施

精准定位结果grantStatus返回2，表示未授权，请求无效可能原因有：未在设置文件中声明目标权限、权限名非法、部分权限存在特殊申请条件，在申请对应权限时未满足其指定的条件。其他相应请求权限，返回的错误码，可参考[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)。

```ts
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ApplyPrecisePositioning {
  permissions: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'];

  aboutToAppear(): void {
    this.reqPermissionsFromUser(this.permissions);
  }

  reqPermissionsFromUser(permissions: Array<Permissions>): void {
    let context: Context = getContext(this) as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    // RequestPermissionsFromUser will determine whether to trigger a pop-up window based on the authorization status of the permission
    atManager.requestPermissionsFromUser(context, permissions).then((data: PermissionRequestResult) => {
      let grantStatus: Array<number> = data.authResults;
      let length: number = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus[i] === 0) {
          // User authorization allows continued access to the target operation
        } else {
          // The user refuses authorization, prompting the user that authorization is required to access the functionality of the current page, and guiding the user to open the corresponding permissions in the system settings
          this.getUIContext().getPromptAction().showToast({ message: 'User refuses authorization' });
          return;
        }
      }
      // Authorization successful
    }).catch((err: BusinessError) => {
      console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
    })
  }

  build() {
  }
}
```
