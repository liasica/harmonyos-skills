---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/location-kit-troubleshooting-0001
title: 定位与地图权限申请问题排查与解决
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 故障排查 > 定位与地图权限申请问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:44+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:2d95ed5913e4583cbe958ab266f4d8979e33141779b7cd4918487be1f1a45918
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

1. 应用应通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限。

   用户在设置界面中的选择"始终允许"应用访问位置信息权限，完成手动授予。

   设置路径：

   路径一：设置->隐私与安全->位置->具体应用。

   路径二：设置->应用和元服务->具体应用->位置。
2. 同时判断ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。

   代码参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)开发步骤第3步：动态向用户申请授权。

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

1. 应用应通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限。

   用户在设置界面中的选择"始终允许"应用访问位置信息权限，完成手动授予。

   设置路径：

   路径一：设置->隐私与安全->位置->具体应用。

   路径二：设置->应用和元服务->具体应用->位置。
2. 同时判断ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。代码参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)开发步骤第3步：动态向用户申请授权。

## 定位权限未配置未申请导致不弹窗

### 问题现象

应用在启用定位功能时，未弹出请求授权的提示，导致定位未能成功。

应用在启用定位功能时，未弹出请求授权的提示，导致定位未能成功。

### 定位过程

1. 查看[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件中是否已经申请了ohos.permission.LOCATION定位权限。也可以通过查看对应时间点的hilog日志，在用户提供的日志中搜索权限ohos.permission.LOCATION，返回结果flag=0表示权限请求的结果为未授权或权限不存在。

   ```txt
   [GetPermissionFlag:386]GetPermissionFlag called, tokenID: xxxxxxxxx, permissionName: ohos.permission.LOCATION
   [GetPermissionFlag:312]Result from server()error=0, flag=0)
   ```
2. 申请了权限之后需要查看[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法中是否向用户申请授权。

### 分析结论

1. 未配置定位权限。
2. 未向用户申请授权，如果没有授权用户收不到定位授权的弹窗无法获取定位信息。

### 修改建议

1. 在module.json5中配置ohos.permission.LOCATION定位权限，可参考：[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
2. 使用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法向用户申请授权。

## 定位与地图权限申请被驳回

### 问题现象

申请定位与地图功能被驳回，且部分申请选项存在捆绑关系，不选择某些选项无法继续申请。

申请定位与地图功能被驳回，且部分申请选项存在捆绑关系，不选择某些选项无法继续申请。

### 定位过程

系统提供的位置权限无需通过申请获取，只需在module.json5中声明即可。地图服务需要在AppGallery Connect上单独开通，不属于权限申请范畴。

### 分析结论

定位与地图功能被驳回的原因是将系统位置权限与高精度定位权限混淆。系统提供的位置权限无需申请，只需在module.json5中声明即可。地图服务需在AppGallery Connect上开通，而非通过权限申请获取。

### 修改建议

无需申请高精度定位权限，系统提供的位置权限只需在module.json5中声明即可。如需使用地图功能，还需在AppGallery Connect上开通[地图服务](../harmonyos-guides/map-config-agc.md)。

## 定位权限无法重复拉起如何解决

### 问题现象

应用安装完成，首次申请位置权限弹窗被用户点击拒绝后，无论退出后台还是杀死应用后再唤起应用，都无法再次拉起系统权限弹窗。

当首次弹窗选择"仅本次允许"后，调用requestPermissionOnSetting无法再次拉起权限弹窗。首次弹窗选择"不允许"后，通过requestPermissionOnSetting拉起二次弹窗，若用户在该弹窗中选择"仅使用期间允许"，后续也无法再通过requestPermissionOnSetting拉起弹窗。

### 定位过程

[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)用于UIAbility/UIExtensionAbility拉起弹框请求用户授权。如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用"设置"的界面中，手动授予权限，或是调用[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，拉起权限设置弹框，引导用户授权。

requestPermissionOnSetting接口仅在权限处于拒绝状态时才会拉起弹窗。当用户选择"仅本次允许"时，权限处于临时授权状态（视为已授权），系统认为权限已授予，因此不再拉起弹窗。当用户选择"仅使用期间允许"时，权限处于持久授权状态（视为已授权），后续使用中不再拉起弹窗。

### 分析结论

该现象属于系统权限管理机制的正常设计行为。requestPermissionOnSetting接口的设计初衷是在权限被用户明确拒绝后，提供二次引导授权的途径，因此仅在权限处于"拒绝"状态时才会拉起弹窗。

需要在代码中加入二次申请权限逻辑：

1、页面加载时校验应用是否被授予位置权限，并用变量标识校验结果。若结果为true，则获取并展示位置信息；若结果为false，则展示授权按钮。

2、使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)拉起弹框请求用户授权，根据授权结果回调，如果权限被授予，则执行获取位置的业务逻辑。如果权限未被授予，则进入引导用户二次授权位置权限的逻辑。

### 修改建议

定义变量hasPermissions用来表示是否获取到位置权限。在页面初始化时校验应用是否被授予位置权限，若已授权，则获取位置信息。

```ts
aboutToAppear(): void {
    this.checkPermissions(this.permissions).then((isGranted: boolean) => {
      if (isGranted) {
        this.hasPermissions = true;
        this.getLocation();
      }
    });
  }

  getLocation() {
    try {
      geoLocationManager.getCurrentLocation(
        (err: BusinessError, location: geoLocationManager.Location) => {
          if (err) {
            this.hasPermissions = false;
            console.error(`Failed to get current location. Code is ${err.code}, message is ${err.message}`);
          }
          if (location) {
            this.hasPermissions = true;
            this.latitude = location.latitude;
            this.longitude = location.longitude;
            this.getAddress();
          } else {
            this.hasPermissions = false;
          }
        });
    } catch (err) {
      console.error(`Failed to get current location. Code is ${err.code}, message is ${err.message}`);
    }
  }
```

申请位置权限的逻辑：

```ts
async requestPermission() {
    this.checkPermissions(this.permissions).then((isGranted: boolean) => {
      if (isGranted) {
        this.getLocation();
        return;
      }

      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      atManager.requestPermissionsFromUser(this.context, this.permissions)
        .then((data: PermissionRequestResult) => {
          if (data.authResults.every(item => item === 0)) { // 已授权
            this.getLocation();
            this.hasPermissions = true;
          } else {
            switch (this.solution) {
              case Solution.requestPermissionOnSetting:
                this.requestPermissionOnSetting();
                break;
              case Solution.goToPermissionSettings:
                this.goToPermissionSettings();
                break;
              case Solution.showDialogToUser:
                this.showDialogToUser();
                break;
            }
          }
        })
        .catch((err: BusinessError) => {
          console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
        });
    });
  }
```

首次申请权限弹窗被用户点击拒绝后，二次申请权限有三种方案可以选择：

1. 拉起申请权限半模态面板：

   ```ts
   async requestPermissionOnSetting() {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionOnSetting(this.context, this.permissions)
         .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
           if (data.every(item => item === 0)) {
             this.getLocation();
             this.hasPermissions = true;
           }
         })
         .catch((err: BusinessError) => {
           console.error(`Failed to request permission on setting. Code is ${err.code}, message is ${err.message}`);
         });
     }
   ```
2. 跳转到系统设置界面，让用户自行打开权限。需要将settingsParamBundleName字段修改为对应应用包名：

   ```ts
   goToPermissionSettings() {
       this.uiContext.showAlertDialog({
         title: '定位失败',
         message: '获取我的位置需要开启精确位置',
         confirm: {
           value: '去开启',
           action: () => {
             let want: Want = {
               bundleName: 'com.huawei.hmos.settings',
               abilityName: 'com.huawei.hmos.settings.MainAbility',
               uri: 'application_info_entry',
               parameters: {
                 settingsParamBundleName: 'com.example.requestPermissionDemo'
               }
             };
             (this.context as common.UIAbilityContext).startAbility(
               want, (err: BusinessError) => {
               if (err) {
                 console.error(`Failed to start Ability. Code is ${err.code}, message is ${err.message}`);
                 return;
               }
             });
           }
         }
       });
     }
   ```
3. 提示用户去设置打开位置权限：

   ```ts
   showDialogToUser() {
       this.uiContext.showAlertDialog({
         title: '定位失败',
         message: '请前往设置打开定位权限：设置 > 隐私和安全 > 位置信息 > 位置测试'
       });
     }
   ```

完整代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import {
  abilityAccessCtrl,
  bundleManager,
  common,
  Context,
  Permissions,
  PermissionRequestResult,
  Want
} from '@kit.AbilityKit';
import { geoLocationManager } from '@kit.LocationKit';
HarmonyOS生态对于权限申请有一定规范，当用户拒绝首次权限申请后，后续重新申请该权限时并不会重新弹窗，为了用户的体验，此时需要开发者做相应的适配，引导客户授权。本文给出了3种适配方式（重新拉起半模态面板、跳转到系统设置页面、信息提示），除了位置以外，麦克风、相机等权限申请也可参考本文实现。

enum Solution {
  requestPermissionOnSetting,
  goToPermissionSettings,
  showDialogToUser,
}

@Entry
@Component
struct RequestLocationPermission {
  @State hasPermissions: boolean = false; // 是否获取到定位权限
  @State address: string = '';
  longitude: number = 0;
  latitude: number = 0;
  solution: Solution = Solution.requestPermissionOnSetting;
  uiContext: UIContext = this.getUIContext();
  context: Context = this.uiContext.getHostContext() as Context;
  permissions: Permissions[] = ['ohos.permission.APPROXIMATELY_LOCATION'];

  @Styles
  locationButtonStyles() {
    .backgroundColor(0x317aff)
    .margin({ bottom: 20 })
    .borderRadius(8)
    .height(50)
    .width(200);
  }

  aboutToAppear(): void {
    this.checkPermissions(this.permissions).then((isGranted: boolean) => {
      if (isGranted) {
        this.hasPermissions = true;
        this.getLocation();
      }
    });
  }

  getLocation() {
    try {
      geoLocationManager.getCurrentLocation(
        (err: BusinessError, location: geoLocationManager.Location) => {
          if (err) {
            this.hasPermissions = false;
            console.error(`Failed to get current location. Code is ${err.code}, message is ${err.message}`);
          }
          if (location) {
            this.hasPermissions = true;
            this.latitude = location.latitude;
            this.longitude = location.longitude;
            this.getAddress();
          } else {
            this.hasPermissions = false;
          }
        });
    } catch (err) {
      console.error(`Failed to get current location. Code is ${err.code}, message is ${err.message}`);
    }
  }

  async requestPermissionOnSetting() {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionOnSetting(this.context, this.permissions)
      .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
        if (data.every(item => item === 0)) {
          this.getLocation();
          this.hasPermissions = true;
        }
      })
      .catch((err: BusinessError) => {
        console.error(`Failed to request permission on setting. Code is ${err.code}, message is ${err.message}`);
      });
  }

  goToPermissionSettings() {
    this.uiContext.showAlertDialog({
      title: '定位失败',
      message: '获取我的位置需要开启精确位置',
      confirm: {
        value: '去开启',
        action: () => {
          let want: Want = {
            bundleName: 'com.huawei.hmos.settings',
            abilityName: 'com.huawei.hmos.settings.MainAbility',
            uri: 'application_info_entry',
            parameters: {
              settingsParamBundleName: 'com.example.requestPermissionDemo'
            }
          };
          (this.context as common.UIAbilityContext).startAbility(
            want, (err: BusinessError) => {
            if (err) {
              console.error(`Failed to start Ability. Code is ${err.code}, message is ${err.message}`);
              return;
            }
          });
        }
      }
    });
  }

  showDialogToUser() {
    this.uiContext.showAlertDialog({
      title: '定位失败',
      message: '请前往设置打开定位权限：设置 > 隐私和安全 > 位置信息 > 位置测试'
    });
  }

  async checkPermissions(permissions: Permissions[]): Promise<boolean> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;
      // 校验列表中的权限是否都被授权
      const authResults = permissions.map(item => atManager.checkAccessTokenSync(tokenId, item) ===
      abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED);
      return authResults.every(item => item === true);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to get bundle info for self. Code is ${err.code}, message is ${err.message}`);
    }
    return false;
  }

  async requestPermission() {
    this.checkPermissions(this.permissions).then((isGranted: boolean) => {
      if (isGranted) {
        this.getLocation();
        return;
      }

      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      atManager.requestPermissionsFromUser(this.context, this.permissions)
        .then((data: PermissionRequestResult) => {
          if (data.authResults.every(item => item === 0)) { // 已授权
            this.getLocation();
            this.hasPermissions = true;
          } else {
            switch (this.solution) {
              case Solution.requestPermissionOnSetting:
                this.requestPermissionOnSetting();
                break;
              case Solution.goToPermissionSettings:
                this.goToPermissionSettings();
                break;
              case Solution.showDialogToUser:
                this.showDialogToUser();
                break;
            }
          }
        })
        .catch((err: BusinessError) => {
          console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
        });
    });
  }

  getAddress() {
    let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
      'latitude': this.latitude,
      'longitude': this.longitude,
      'maxItems': 1
    };
    try {
      geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
        if (err) {
          console.error(`Failed to get addresses from location. Code is ${err.code}, message is ${err.message}`);
        }
        this.address = data[0].placeName as string;
      });
    } catch (err) {
      console.error(`Failed to get addresses from location. Code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {
    Column() {
      if (!this.hasPermissions) {
        Column() {
          Button('我的位置(拉起半模态权限弹窗)')
            .locationButtonStyles()
            .onClick(async () => {
              this.solution = Solution.requestPermissionOnSetting;
              this.requestPermission();
            });
          Button('我的位置(跳转到设置的权限页)')
            .locationButtonStyles()
            .onClick(async () => {
              this.solution = Solution.goToPermissionSettings;
              this.requestPermission();
            });
          Button('我的位置(弹窗提示去开启权限)')
            .locationButtonStyles()
            .onClick(async () => {
              this.solution = Solution.showDialogToUser;
              this.requestPermission();
            });
        }
        .justifyContent(FlexAlign.Center)
        .height('100%');
      } else {
        Text(this.address)
          .fontSize(20)
          .fontWeight(800)
          .width(280)
          .textAlign(TextAlign.Center);
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
