---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-10
title: 位置权限关闭后，如何实现在应用内一步操作重新开启
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 位置权限关闭后，如何实现在应用内一步操作重新开启
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:64b7f141451aee1e649797a46a30a341d02cb32113debfa5e46fe67baa2dd924
---

## 问题现象

位置权限被关闭后，如何引导用户开启精确位置和后台位置权限，减少操作路径，优化用户体验？

## 背景知识

位置权限说明：

| 场景 | 涉及权限 | 备注 |
| --- | --- | --- |
| 模糊位置 | [ohos.permission.APPROXIMATELY\_LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapproximately_location) | 精确度为5公里。 |
| 精确位置 | [ohos.permission.LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation) | 精确度为米级，需要与ohos.permission.APPROXIMATELY\_LOCATION同时申请。 |
| 后台位置 | [ohos.permission.LOCATION\_IN\_BACKGROUND](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation_in_background) | 先获取前台位置权限，再配合[长时任务](../harmonyos-guides/continuous-task.md)使用。 |

**说明** 

* 精确位置：关闭“精确位置”的开关后，无法通过[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)再次拉起弹框获取授权。需要用户手动在设置中开启，或者使用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口[二次向用户申请授权](../harmonyos-guides/request-user-authorization-second.md)。
* 后台位置：申请后台权限前，必须先申请前台位置权限。前台位置权限的申请有两种允许情况：
  + 申请前台模糊位置权限：ohos.permission.APPROXIMATELY\_LOCATION。
  + 申请前台精确位置权限：ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION。

## 解决方案

* **场景一****：****代码引导用户开启“精确位置”**。
  1. 使用[checkAccessTokenSync()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstokensync10)接口判断ohos.permission.LOCATION是否授权的方式，确认当前应用是否开启“精确位置”开关。

     ```screen
     checkPermissionGrant(): void {
       let hasPermission = false;
       let tokenId: number = 0;
       try {
         let bundleInfo: bundleManager.BundleInfo =
           bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
         let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
         tokenId = appInfo.accessTokenId;
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         hilog.error(0x0000, 'Index',
           `Failed to get bundle info for self. Code is ${err.code}, message is ${err.message}`);
       }

       try {
         let atManager = abilityAccessCtrl.createAtManager();
         let approximatelyLocation = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.APPROXIMATELY_LOCATION');
         // 获取精确位置权限授权状态
         let location = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.LOCATION');
         hasPermission = approximatelyLocation === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED &&
           location === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         hilog.error(0x0000, 'Index', `Failed to check access token. Code is ${err.code}, message is ${err.message}`);
       }
       if (hasPermission) {
         this.isLocationToggle();
       } else {
         this.requestPermissions();
       }
     }
     ```
  2. 在[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)申请授权回调中判断是否有授权弹窗提示。应用非首次申请授权且没有向用户展示授权弹框，应用可以调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口二次向用户申请位置授权。

     ```screen
     requestPermissions(): void {
       let atManager = abilityAccessCtrl.createAtManager();
       try {
         atManager.requestPermissionsFromUser(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
           'ohos.permission.LOCATION']).then((data) => {
           if (data.authResults[0] === -1 || data.authResults[1] === -1) {
             if (data.dialogShownResults && (data.dialogShownResults[0] || data.dialogShownResults[1])) {
               this.isShowPermissions = true;
               if (data.authResults[0] === -1) {
                 this.permissionsMessage = '需获取定位权限才能正常使用';
               } else {
                 this.permissionsMessage = '需获取精确定位权限才能获取精确位置';
               }
             } else {
               this.openPermissionsSetting();
               return;
             }
           } else {
             this.isShowPermissions = false;
           }
           if (data.authResults[0] !== 0) {
             return;
           }
           this.isLocationToggle();
         }).catch((err: Error) => {
           hilog.error(0x0000, 'Index', 'requestPermissionsFromUser err:' + JSON.stringify(err));
         });
       } catch (err) {
         hilog.error(0x0000, 'Index', 'requestPermissionsFromUser err:' + JSON.stringify(err));
       }
     }
     ```
  3. 使用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口向用户二次申请“精确位置”授权。

     ```screen
     private openPermissionsSetting(): void {
       let atManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionOnSetting(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
         'ohos.permission.LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
         if (data[0] === -1 && data[1] === -1) {
           this.isShowPermissions = true;
           this.permissionsMessage = '需获取定位权限才能正常使用';
           return;
         } else if (data[0] === 0 && data[1] === -1) {
           this.isShowPermissions = true;
           this.permissionsMessage = '需获取精确定位权限才能获取精确位置';
         } else {
           this.isShowPermissions = false;
         }
         this.isLocationToggle();
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'Index', 'data:' + JSON.stringify(err));
       });
     }
     ```

     效果预览：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/j9_HQl_ZSLWlzVccEyzOIg/zh-cn_image_0000002658793799.png "点击放大")
* **场景二：代码引导用户开启“后台位置”。**

  确认完成前台位置权限授权后，使用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)接口向用户申请后台位置授权：

  ```screen
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  atManager.requestPermissionOnSetting(this.context, ['ohos.permission.LOCATION_IN_BACKGROUND'])
    .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
      hilog.info(0x0000, 'Index', `requestPermissionOnSetting success, result: ${data}`);
    })
    .catch((err: BusinessError) => {
      hilog.error(0x0000, 'Index',
        `requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
      if (err.code == 12100011) {
        try {
          this.promptAction.showToast({
            message: '已获取权限',
            duration: 2000
          });
        } catch (error) {
          let message = (error as BusinessError).message;
          let code = (error as BusinessError).code;
          hilog.error(0x0000, 'Index', `showToast args error code is ${code}, message is ${message}`);
        }
      }
    });
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/1JHrr02dSoGWFK4iUHXzVA/zh-cn_image_0000002628394530.png "点击放大")
* **场景三：代码引导用户开启“系统位置”功能开关。**

  使用[isLocationEnabled()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)检查当前系统位置功能是否被禁用。如果位置功能被禁用则无法获取位置信息，需要调用[requestGlobalSwitch()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)拉起半模态对话框打开位置开关。

  ```screen
  isLocationToggle(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    let isLocationEnabled = geoLocationManager.isLocationEnabled();
    if (!isLocationEnabled) {
      atManager.requestGlobalSwitch(this.context, abilityAccessCtrl.SwitchType.LOCATION).then((data: boolean) => {
        if (data) {
          this.isShowLocation = false;
          this.getLocation();
        } else {
          this.isShowLocation = true;
          this.locationServiceMessage = '需打开设备位置服务才能获取当前位置';
        }
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'Index', 'data:' + JSON.stringify(err));
      });
    } else {
      this.isShowLocation = false;
      this.getLocation();
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ei8qYismTj-JF4hTyTRjEw/zh-cn_image_0000002628554424.png "点击放大")

完整代码如下，使用前请先在module.json5中声明ohos.permission.APPROXIMATELY\_LOCATION、ohos.permission.LOCATION和ohos.permission.LOCATION\_IN\_BACKGROUND权限：

```screen
import { i18n } from '@kit.LocalizationKit';
import { abilityAccessCtrl, bundleManager, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isShowPermissions: boolean = false;
  @State currentLocation: string = '';
  @State permissionsMessage: string = '需获取定位权限才能正常使用';
  @State locationServiceMessage: string = '需获取定位权限才能正常使用';
  @State isShowLocation: boolean = false;
  @Watch('locale') @StorageLink('language') systemLanguages: string = i18n.System.getAppPreferredLanguage();
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private promptAction: PromptAction = this.getUIContext().getPromptAction();
  latitude: number = 0;
  longitude: number = 0;

  locale(): void {
    this.getLocation();
  }

  build() {
    Column({ space: 10 }) {
      Column() {
        Row() {
          Text('当前位置：')
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
            .textAlign(TextAlign.Start)
        }
        .width('100%')
        .padding({
          left: 12,
          right: 16
        })
        .margin({
          top: 16,
          bottom: 16
        })

        Row() {
          Text(this.currentLocation)
        }
        .width('100%')
        .padding({
          left: 16,
          right: 16
        })
      }

      Column() {
        if (this.isShowPermissions) {
          Text() {
            Span(this.permissionsMessage)
              .fontColor('#99000000')
            Span('开启权限')
              .fontColor('#0A59F7')
              .onClick(() => {
                this.checkPermissionGrant();
              })
          }
          .width('100%')
          .padding({
            left: 16,
            right: 16
          })
          .margin({
            bottom: 16
          })
        }
        if (this.isShowLocation) {
          Text() {
            Span(this.locationServiceMessage)
              .fontColor('#99000000')
            Span('开启位置服务')
              .fontColor('#0A59F7')
              .onClick(() => {
                this.isLocationToggle();
              })
          }
          .width('100%')
          .padding({
            left: 16,
            right: 16
          })
          .margin({
            bottom: 16
          })
        }

        Button('获取当前位置')
          .onClick(() => {
            this.currentLocation = '';
            this.checkPermissionGrant();
          })
          .backgroundColor('#0A59F7')
          .width(288)
          .margin({
            bottom: 16
          })

        if (this.isShowPermissions) {
          Button('开启后台位置权限')
            .onClick(() => {
              let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
              atManager.requestPermissionOnSetting(this.context, ['ohos.permission.LOCATION_IN_BACKGROUND'])
                .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
                  hilog.info(0x0000, 'Index', `requestPermissionOnSetting success, result: ${data}`);
                })
                .catch((err: BusinessError) => {
                  hilog.error(0x0000, 'Index',
                    `requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
                  if (err.code == 12100011) {
                    try {
                      this.promptAction.showToast({
                        message: '已获取权限',
                        duration: 2000
                      });
                    } catch (error) {
                      let message = (error as BusinessError).message;
                      let code = (error as BusinessError).code;
                      hilog.error(0x0000, 'Index', `showToast args error code is ${code}, message is ${message}`);
                    }
                  }
                });
            })
            .backgroundColor('#0A59F7')
            .width(288)
            .margin({
              bottom: 16
            })
        }

      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .width('100%')
    .height('100%')
  }

  // [Start open_permissions_setting]
  // The permission setting dialog box is displayed.
  private openPermissionsSetting(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionOnSetting(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
      'ohos.permission.LOCATION']).then((data: Array<abilityAccessCtrl.GrantStatus>) => {
      if (data[0] === -1 && data[1] === -1) {
        this.isShowPermissions = true;
        this.permissionsMessage = '需获取定位权限才能正常使用';
        return;
      } else if (data[0] === 0 && data[1] === -1) {
        this.isShowPermissions = true;
        this.permissionsMessage = '需获取精确定位权限才能获取精确位置';
      } else {
        this.isShowPermissions = false;
      }
      this.isLocationToggle();
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'Index', 'data:' + JSON.stringify(err));
    });
  }

  // [End open_permissions_setting]

  // [Start check_permission_grant]
  // Verify if the application has been granted permission.
  checkPermissionGrant(): void {
    let hasPermission = false;
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(0x0000, 'Index',
        `Failed to get bundle info for self. Code is ${err.code}, message is ${err.message}`);
    }

    try {
      let atManager = abilityAccessCtrl.createAtManager();
      let approximatelyLocation = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.APPROXIMATELY_LOCATION');
      // 获取精确位置权限授权状态
      let location = atManager.checkAccessTokenSync(tokenId, 'ohos.permission.LOCATION');
      hasPermission = approximatelyLocation === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED &&
        location === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(0x0000, 'Index', `Failed to check access token. Code is ${err.code}, message is ${err.message}`);
    }
    if (hasPermission) {
      this.isLocationToggle();
    } else {
      this.requestPermissions();
    }
  }

  // [End check_permission_grant]

  // [Start request_permissions]
  // Requests location permissions from the user.
  requestPermissions(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    try {
      atManager.requestPermissionsFromUser(this.context, ['ohos.permission.APPROXIMATELY_LOCATION',
        'ohos.permission.LOCATION']).then((data) => {
        if (data.authResults[0] === -1 || data.authResults[1] === -1) {
          if (data.dialogShownResults && (data.dialogShownResults[0] || data.dialogShownResults[1])) {
            this.isShowPermissions = true;
            if (data.authResults[0] === -1) {
              this.permissionsMessage = '需获取定位权限才能正常使用';
            } else {
              this.permissionsMessage = '需获取精确定位权限才能获取精确位置';
            }
          } else {
            this.openPermissionsSetting();
            return;
          }
        } else {
          this.isShowPermissions = false;
        }
        if (data.authResults[0] !== 0) {
          return;
        }
        this.isLocationToggle();
      }).catch((err: Error) => {
        hilog.error(0x0000, 'Index', 'requestPermissionsFromUser err:' + JSON.stringify(err));
      });
    } catch (err) {
      hilog.error(0x0000, 'Index', 'requestPermissionsFromUser err:' + JSON.stringify(err));
    }
  }

  // [End request_permissions]

  // [Start is_location_toggle]
  // Obtain current location switch status and pull up the global switch to set the pop-up box.
  isLocationToggle(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    let isLocationEnabled = geoLocationManager.isLocationEnabled();
    if (!isLocationEnabled) {
      atManager.requestGlobalSwitch(this.context, abilityAccessCtrl.SwitchType.LOCATION).then((data: boolean) => {
        if (data) {
          this.isShowLocation = false;
          this.getLocation();
        } else {
          this.isShowLocation = true;
          this.locationServiceMessage = '需打开设备位置服务才能获取当前位置';
        }
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'Index', 'data:' + JSON.stringify(err));
      });
    } else {
      this.isShowLocation = false;
      this.getLocation();
    }
  }

  getLocation(): void {
    let request: geoLocationManager.SingleLocationRequest = {
      'locatingTimeoutMs': 10000,
      'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED
    };
    // Get current location.
    geoLocationManager.getCurrentLocation(request).then((location) => {
      this.latitude = location.latitude;
      this.longitude = location.longitude;
      let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
        'locale': this.systemLanguages.toString().includes('zh') ? 'zh' : 'en',
        'latitude': this.latitude,
        'longitude': this.longitude,
        'maxItems': 1
      };
      // Call the inverse geocoding service to convert coordinates into geographic descriptions.
      geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest).then((data) => {
        if (data[0].placeName) {
          this.currentLocation = data[0].placeName;
        }
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'Index', 'GetAddressesFromLocation err:' + JSON.stringify(err));
      });
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'Index', 'Promise getCurrentLocation err:' + JSON.stringify(err));
    });
  }

  // [End is_location_toggle]
}
```

## 常见FAQ

Q：申请ohos.permission.LOCATION精确位置无弹窗提示。

A：ohos.permission.LOCATION不可以单独申请，需要与模糊位置权限ohos.permission.APPROXIMATELY\_LOCATION同时申请。

Q：位置授权弹窗三种选择对应的效果是什么。

A：位置授权弹窗提示分为以下三种情况：

* 不允许：后续不再弹窗，如需要权限，需要提醒用户前往设置页面手动开启；
* 本次使用允许：赋予临时权限，后续再次调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)向用户索取权限时，还会继续弹窗；
* 仅在使用期间允许：应用在前台使用位置权限不再弹窗提醒。

Q：是否可以区分用户选择了位置授权弹框的“不允许”、“本次允许”还是“仅在使用期间允许”？

A：[checkAccessTokenSync](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstokensync10)接口仅返回是否授权两个枚举状态[GrantStatus](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)，不会进一步说明选择的是哪种授权类型。

Q：如何取消位置权限的授权？

A：参考上述场景二，代码引导用户关闭“后台位置”。

Q：精确位置默认能否开启？

A：精确位置权限默认是关闭的，开发者必须显式声明和申请权限。
