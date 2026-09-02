---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-15
title: 如何判断卫星是否参与定位
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何判断卫星是否参与定位
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:bcde89ae1e20512e778790c8b075313ff3870f6bd3948f96a1a6caa4375e8ae2
---

## 问题现象

通过[satelliteStatusChange](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronsatellitestatuschange)订阅GNSS卫星状态信息上报事件，如何从返回的GNSS卫星状态信息中判断卫星是否参与了定位？

## 背景知识

* [SatelliteStatusInfo](../harmonyos-references/js-apis-geolocationmanager.md#satellitestatusinfo)：卫星状态信息，通过订阅GNSS卫星状态信息上报事件获取。
* [SatelliteAdditionalInfo](../harmonyos-references/js-apis-geolocationmanager.md#satelliteadditionalinfo12)：卫星附加信息类型，在卫星状态信息中，可用于判断本卫星是否具有星历数据、本卫星是否具有年历数据、是否使用了本卫星和本卫星是否具有载波频率。

## 解决方案

订阅GNSS卫星状态信息上报事件，打印卫星状态信息里的卫星附加信息。

**说明** 

地图组件在[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)后才可以正常加载地图信息。

```screen
import abilityAccessCtrl, { Permissions } from '@ohos.abilityAccessCtrl';
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
import { geoLocationManager } from '@kit.LocationKit';
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct locationTest {
  private permissions: Array<Permissions> = [
    'ohos.permission.APPROXIMATELY_LOCATION',
    'ohos.permission.LOCATION'
  ];
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;

  @State hasPermission: boolean = false;

  reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
    const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
    atManager.requestPermissionsFromUser(context, permissions).then((data) => {
      // 启用我的位置图层
      this.mapController?.setMyLocationEnabled(true);
      let grantStatus: Array<number> = data.authResults;
      let length: number = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus[i] === 0) {
          // 用户授权，可以继续访问目标操作
          this.hasPermission = true;
          // 订阅GNSS卫星状态信息上报事件
          geoLocationManager.on('satelliteStatusChange',
            (satelliteStatusInfo: geoLocationManager.SatelliteStatusInfo): void => {
              console.info(`satelliteStatusInfo.satelliteAdditionalInfo->${
              satelliteStatusInfo.satelliteAdditionalInfo?.toString()})`);
            });
        } else {
          // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
          return;
        }
      }
      // 授权成功
    }).catch((err: BusinessError) => {
      console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
    });
  }

  onPageShow() {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    this.reqPermissionsFromUser(this.permissions, context);
  }

  aboutToAppear() {
    this.mapOption = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      },
      tiltGesturesEnabled: true,
      myLocationControlsEnabled: true
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // 启用我的位置图层
        this.mapController.setMyLocationEnabled(true);
        // 启用我的位置按钮
        this.mapController.setMyLocationControlsEnabled(true);
      }
    };
  }

  build() {
    Column() {
      if (this.hasPermission) {
        MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
          .width('100%')
          .height('100%');
      }
    }.width('100%')
  }
}
```

打印卫星附加信息，信息会不断刷新，举例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_211csGZTdekK4wR3qzkpg/zh-cn_image_0000002628394534.png "点击放大")

SatelliteAdditionalInfo每一项表示一个卫星的附加信息，返回的是十进制数字“15,15,14,15,15,15...”，需要先转换为二进制数字再判断各个比特位，对应比特位上为1表示有对应的信息，每个比特位的含义见下图。比如返回卫星附加信息为15，转换成二进制是1111，表示使用了本卫星，且具有星历数据、年历数据和载波频率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/pQs9_IiVQRmHlYelyn4tTg/zh-cn_image_0000002628554428.png "点击放大")

要判断这些卫星是否参与定位，只需要判断转换后的二进制数字从右向左数第三位是否为1，上述十进制数字中“15、14、13”满足要求，这些数字对应的卫星参与了定位。
