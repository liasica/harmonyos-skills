---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-17
title: 定位权限无法重复拉起如何解决
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 定位权限无法重复拉起如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5f078d3c475d4c9dee328dfe8cca14c0dca1ad15bfe7087e026d1bfaca96f77a
---

## 问题现象

应用安装完成，首次申请位置权限弹窗被用户点击拒绝后，无论是退出后台还是杀死应用后再唤起应用，都无法再次拉起系统权限弹窗。

## 背景知识

应用使用位置权限，必须在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)的requestPermissions标签中声明权限。本文以[ohos.permission.APPROXIMATELY\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapproximately_location)权限为例，允许应用获取设备模糊位置信息。

应用在首次打开或运行中，在用户未主动点击权限对应的相关功能或服务时，提前向用户弹窗申请开启位置权限，属于[权限索取违规行为](../app/faq-05.md)，所以需要用户主动点击触发后弹起权限弹窗。若首次弹窗未被用户授权同意，应用应给出提示去设置打开权限开关或者能够重复拉起权限窗口。

## 问题定位

[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)用于UIAbility/UIExtensionAbility拉起弹框请求用户授权。如果用户拒绝授权，将无法再次拉起弹框，需要用户在系统应用“设置”的界面中，手动授予权限，或是调用[requestPermissionOnSetting](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，拉起权限设置弹框，引导用户授权。

## 分析结论

需要在代码中加入二次申请权限逻辑：

1. 页面加载时校验应用是否被授予位置权限，并用变量标识校验结果。若结果为true，则获取并展示位置信息；若结果为false，则展示授权按钮。
2. 使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)拉起弹框请求用户授权，根据授权结果回调，如果权限被授予，则执行获取位置的业务逻辑。如果权限未被授予，则进入引导用户二次授权位置权限的逻辑。

## 修改建议

定义变量hasPermissions用来表示是否获取到位置权限。在页面初始化时校验应用是否被授予位置权限，若已授权，则获取位置信息。

```screen
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

```screen
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

   ```screen
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

   ```screen
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

   ```screen
   showDialogToUser() {
     this.uiContext.showAlertDialog({
       title: '定位失败',
       message: '请前往设置打开定位权限：设置 > 隐私和安全 > 位置信息 > 位置测试'
     });
   }
   ```

完整示例参考如下：

```screen
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

## 总结

HarmonyOS生态对于权限申请有一定规范，当用户拒绝首次权限申请后，后续重新申请该权限时并不会重新弹窗，为了用户的体验，此时需要开发者做相应的适配，引导客户授权。本文给出了3种适配方式（重新拉起半模态面板、跳转到系统设置页面、信息提示），除了位置以外，麦克风、相机等权限申请也可参考本文实现。
