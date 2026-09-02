---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-9
title: 已开启应用的位置权限，但仍然提示未开启位置权限
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 已开启应用的位置权限，但仍然提示未开启位置权限
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4cf160fdf5fae9ce8d49fd6ff14742e62e74f832d264058df9c6fe4f88ad8341
---

## 问题现象

已开启应用的位置权限，但实际无法获取当前位置且仍然提示未开启位置权限，跳转系统设置页后应用位置权限也都是开启的。

## 背景知识

* [Location Kit](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，如GNSS定位、基站定位、WLAN/蓝牙定位（基站定位、WLAN/蓝牙定位后续统称“网络定位技术”）；通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置。
* [向用户申请授权](../harmonyos-guides/request-user-authorization.md)：当应用需要访问用户的隐私信息或使用系统能力时，例如获取位置信息、访问日历、使用相机拍摄照片或录制视频等，应该向用户请求授权，这部分权限是user\_grant权限。
* [geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)：判断位置服务是否已经开启。可以通过此接口获取手机是否开启了位置服务。
* [requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)：部分情况下，录音、拍照等功能禁用，应用可拉起此弹框请求用户同意开启对应功能。如果当前全局开关的状态为开启，则不拉起弹框。

## 问题定位

1. 排查应用是否被授权了位置权限：在日志中全局搜索关键字“ohos.permission.LOCATION”、“ohos.permission.APPROXIMATELY\_LOCATION”，state为0，表示此应用已被授予ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION这2个位置权限。

   ```screen
   07-22 12:00:48.108   3766-21737    C05A01/com.hm.example/ATM  com.hm.example  I     [IsDynamicRequest:440]Permission: ohos.permission.APPROXIMATELY_LOCATION: state: 0, errorReason: 0
   07-22 12:00:48.108   3766-21737    C05A01/com.hm.example/ATM  com.hm.example  I     [IsDynamicRequest:440]Permission: ohos.permission.LOCATION: state: 0, errorReason: 0
   ```
2. 排查设备是否开启了位置服务：在日志中全局搜索关键字“location switch”，可以看到以下相关日志，表明设备的位置服务未开启。

   ```screen
   07-22 15:52:56.840   35263-35311   C02300/locationhub/Locator      locationhub           E     [(ReportLocationStatus:1217)]ReportLocationStatus line:1217 location switch is off
   07-22 15:52:56.861   35263-50703   C02300/locationhub/Locator      locationhub           E     [(AddRequestToWorkRecord:508)]AddRequestToWorkRecord line:508 the location switch is off
   ```

## 分析结论

设备的位置服务未开启，导致应用虽然被授权了位置权限，但仍然获取不到位置信息。

## 修改建议

1. 在获取到位置权限后，实际定位前，调用[geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)查询系统位置服务开关状态。
2. 若系统位置服务开关未开启，调用[requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)接口向用户请求开启位置服务。

全量代码如下：

**须知** 

参考[声明权限](../harmonyos-guides/declare-permissions.md)文档，需要先在module.json5文件中声明ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION权限。

```screen
import { geoLocationManager } from '@kit.LocationKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  requestPermission() {
    try {
      // 1、查询是否开启位置服务
      let locationEnabled = geoLocationManager.isLocationEnabled();
      if (locationEnabled) {
        // 2.1、位置服务开启则申请位置相关授权
        let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        let permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
        // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗。
        atManager.requestPermissionsFromUser(this.context, permissions).then((data) => {
          let grantStatus: Array<number> = data.authResults;
          let length: number = grantStatus.length;
          for (let i = 0; i < length; i++) {
            if (grantStatus[i] === 0) {
              // 用户授权，可以继续访问目标操作。
            } else {
              // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限。
              return;
            }
          }
          // 授权成功。
        }).catch((err: BusinessError) => {
          console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
        });
      } else {
        // 2.2、位置服务未开启则弹窗请求用户开启位置服务
        let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

        atManager.requestGlobalSwitch(this.context, abilityAccessCtrl.SwitchType.LOCATION)
          .then((data: Boolean) => {
            console.info(`requestGlobalSwitch data: ${data}`);
            // 返回false表示位置服务未开启，系统会自动弹窗请求用户开启位置服务
          })
          .catch((err: BusinessError) => {
            console.error(`requestGlobalSwitch err.code: ${err.code}, err.message: ${err.message}`);
          });
      }
    } catch (err) {
      console.error(`geoLocationManager.isLocationEnabled failed err.code: ${err.code}, err.message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Button('开启定位')
        .type(ButtonType.ROUNDED_RECTANGLE)
        .backgroundColor('#0a59f7')
        .onClick(() => {
          this.requestPermission();
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
