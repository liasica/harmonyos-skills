---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-18
title: 初始化地图全屏蓝色如何解决
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 初始化地图全屏蓝色如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c32213f1d043b1b74bc3de6f48e35a460f9132812b5e7741276d10413bf5853
---

## 问题现象

使用MapComponent开发地图服务中，加载地图后，表现为全屏蓝色，可能被误认为无法加载地图。

问题代码示例参考如下：

```ts
// 获取定位
Location() {
  let request: geoLocationManager.SingleLocationRequest = {
    locatingPriority: 0x501,
    locatingTimeoutMs: 1000
  };

  geoLocationManager.getCurrentLocation(request).then((location: geoLocationManager.Location) => {
    this.point = MapUtil.convertToGcj02(location.latitude, location.longitude);
    logger.debug(`getCurrentLocationPosition latitude: ${this.point.latitude}, longitude: ${this.point.longitude}`);
  }).catch((err: BusinessError) => {
    logger.error(`getCurrentLocationPosition failed, code: ${err.code}, message: ${err.message}`);
  });
}

aboutToAppear(): void {
  this.Location()
  // 初始化地图参数
  this.mapOptions = {
    position: {
      target: this.point,
      zoom: 17
    }
  }
}

build() {
  NavDestination() {
    Stack() {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback,
        })
      }
    }
  }
}
```

## 背景知识

* [开发准备](../harmonyos-guides/map-config-agc.md)：请优先开通地图服务后，再继续进行以下开发活动。
* [位置服务](../harmonyos-references/js-apis-geolocationmanager.md)：提供GNSS定位、网络定位（蜂窝基站、WLAN、蓝牙定位技术）、地理编码、逆地理编码、国家码和地理围栏等基本功能。

## 问题定位

根据Mapkit开发地图，先获取定位，然后再用获取到的定位作为mapOptions的position参数来初始化地图；此时我们预期的展示是当前定位处，但是打开地图页面过后直接蓝屏，左右滑动也是毫无反应。经过日志分析：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/fmgwhJwNRTab9jUupJskow/zh-cn_image_0000002628554260.png "点击放大")

发现定位并没有偏差。

通过对代码的Debug运行，发现获取定位是一个异步过程，获取到定位前已初始化地图结束，导致地图position取了默认值(0,0)定位在海洋中，所以显示为海洋蓝色，左右滑动也是因为地图层级太大，导致依旧处于海洋当中，所以毫无变化。

## 分析结论

获取定位是异步操作，导致地图position取了默认值(0,0)定位在海洋中，地图显示为蓝色，并且地图层级太大，导致滑动无变化。

## 修改建议

1. 为了初始化地图，所以先给定地图一个接近当前定位的初始值，如日志中的地址：@State point: mapCommon.LatLng = { latitude: 22.892205166694172, longitude: 113.89977867120956 }。

   同时，再获取地址后，再次进行定位修正：

   ```ts
   // 再次修正定位，此处为解决问题的代码。
   let cameraUpdate = map.newLatLng(this.point);
   this.mapController?.animateCamera(cameraUpdate);
   ```
2. 建议开发地图过程中相机缩放级别取较小值，没有问题后再根据实际需求设定zoom，其中zoom取值【2，20】：

   ```ts
   position: {
     target: this.point,
     zoom: 17
   }
   ```

完整示例参考如下：

```ts
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { geoLocationManager } from '@kit.LocationKit';

function convertToGcj02(latitude: number, longitude: number) {
  let wgs84Position: mapCommon.LatLng = {
    latitude: latitude,
    longitude: longitude
  };

  // Convert latitude and longitude coordinates
  let gcj02Position: mapCommon.LatLng =
    map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);
  return gcj02Position;
}

@Entry
@Component
struct LocationDemo {
  point: mapCommon.LatLng = { latitude: 22, longitude: 113 };
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOptions = {
      position: {
        target: this.point,
        zoom: 17
      }
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;

        await this.Location();

        this.mapController?.setMyLocationEnabled(true);
        let style: mapCommon.MyLocationStyle = {
          icon: $r('app.media.startIcon'), // Replace this with your own icon resource.
          radiusFillColor: 0
        };
        await this.mapController.setMyLocationStyle(style);
        // 启用我的位置图层
        this.mapController?.setMyLocationEnabled(true);
        // 启用我的位置按钮
        this.mapController?.setMyLocationControlsEnabled(true);
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  // 获取定位
  async Location() {
    let permission = await this.checkPermissions();
    if (!permission) {
      await this.requestPermissions();
    }

    let request: geoLocationManager.SingleLocationRequest = {
      locatingPriority: 0x501,
      locatingTimeoutMs: 1000
    };

    geoLocationManager.getCurrentLocation(request).then((location: geoLocationManager.Location) => {
      this.point = convertToGcj02(location.latitude, location.longitude);

      // 再次修正定位，此处为解决问题的代码。
      let cameraUpdate = map.newLatLng(this.point);
      this.mapController?.animateCamera(cameraUpdate);

      console.info(`getCurrentLocationPosition latitude: ${this.point.latitude}, longitude: ${this.point.longitude}`);
    }).catch((err: BusinessError) => {
      console.error(`getCurrentLocationPosition failed, code: ${err.code}, message: ${err.message}`);
    });
  }

  // 校验应用是否被授予定位权限，可以通过调用checkAccessToken()方法来校验当前是否已经授权。
  async checkPermissions(): Promise<boolean> {
    const permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
    for (let permission of permissions) {
      let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
      if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        // 启用我的位置图层，mapController为地图操作类对象
        this.mapController?.setMyLocationEnabled(true);
        // 启用我的位置按钮
        this.mapController?.setMyLocationControlsEnabled(true);
        return true;
      }
    }
    return false;
  }

  // 如果没有被授予定位权限，动态向用户申请授权
  async requestPermissions(): Promise<void> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    await atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
      ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION']);

  }

  async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
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

  build() {
    Stack() {
      // 调用MapComponent组件初始化地图
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%');
    }.height('100%');
  }
}
```
