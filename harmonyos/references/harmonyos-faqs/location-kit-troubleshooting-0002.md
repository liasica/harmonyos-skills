---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/location-kit-troubleshooting-0002
title: 应用获取设备定位信息问题定位
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 故障排查 > 应用获取设备定位信息问题定位
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:43+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:f9add2f4b6fef9feceb962d9254ac6396923cce1867124aa21bc0a22c2748707
---

## 获取位置信息出现闪退

### 问题现象

在设备关闭定位的情况下，应用获取位置信息会出现闪退。

### 定位过程

1. 从faultlogger目录下获取故障日志。
2. 打开对应日志查看内容，确定故障原因是Error。异常信息是“BusinessError 3301100: The location switch is off.”，该错误码表示位置功能的开关未开启导致功能失败。

   ```txt
   Error name:Error
   Error message:BusinessError 3301100: The location switch is off.
   Error code:3301100
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
   at locationinfo (entry|entry|1.0.0|src/main/ets/model/coordinates.ts:22:1)
   at aboutToAppear (entry|entry|1.0.0|src/main/ets/pages/mapPage/mapPage.ts:95:1)
   ```
3. 排查堆栈中的代码在使用定位服务时，是否先判断位置开关已打开，是否捕获了异常并处理。

### 分析结论

应用在获取当前位置信息前，未判断位置开关状态，且未捕获异常，导致应用闪退。

### 修改建议

建议参考文档[获取设备的位置信息开发指导](../harmonyos-guides/location-guidelines.md)，应用调用位置服务接口前，应当先判断位置开关状态是否开启，如果位置开关未开启，可以使用[requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)接口拉起全局开关设置弹框提醒用户开启，代码示例参考[开发步骤](../harmonyos-guides/location-guidelines.md#开发步骤)。

## 已开启位置权限仍提示未开启

### 问题现象

已开启应用的位置权限，但实际无法获取当前位置且仍然提示未开启位置权限，跳转系统设置页后应用位置权限也都是开启的。

### 定位过程

1. 排查应用是否被授权了位置权限：在日志中全局搜索关键字“ohos.permission.LOCATION”、“ohos.permission.APPROXIMATELY\_LOCATION”，state为0，表示此应用已被授予ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION这2个位置权限。

   ```txt
   07-22 12:00:48.108   3766-21737    C05A01/com.hm.example/ATM  com.hm.example  I     [IsDynamicRequest:440]Permission: ohos.permission.APPROXIMATELY_LOCATION: state: 0, errorReason: 0
   07-22 12:00:48.108   3766-21737    C05A01/com.hm.example/ATM  com.hm.example  I     [IsDynamicRequest:440]Permission: ohos.permission.LOCATION: state: 0, errorReason: 0
   ```
2. 排查设备是否开启了位置服务：在日志中全局搜索关键字“location switch”，可以看到以下相关日志，表明设备的位置服务未开启。

   ```txt
   07-22 15:52:56.840   35263-35311   C02300/locationhub/Locator      locationhub           E     [(ReportLocationStatus:1217)]ReportLocationStatus line:1217 location switch is off
   07-22 15:52:56.861   35263-50703   C02300/locationhub/Locator      locationhub           E     [(AddRequestToWorkRecord:508)]AddRequestToWorkRecord line:508 the location switch is off
   ```

### 分析结论

设备的位置服务未开启，导致应用虽然被授权了位置权限，但仍然获取不到位置信息。

### 修改建议

1. 在获取到位置权限后，实际定位前，调用[geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)查询系统位置服务开关状态。
2. 若系统位置服务开关未开启，调用[requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)接口向用户请求开启位置服务。

全量代码如下：

**说明** 

参考[声明权限](../harmonyos-guides/declare-permissions.md)文档，需要先在module.json5文件中声明ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION权限。

```ts
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
