---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-7
title: 怎么在地图中确定某一段路线的方向
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 怎么在地图中确定某一段路线的方向
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:2ad75d8597e619b4e7ddebe05e27e00e50f1b676fd842663cc093c413738209e
---

## 问题现象

在地图绘制路线过程中需要确定某一段路线的方向，以便控制汽车图片旋转一定角度，使车头正对路线方向。

## 背景知识

* [MarkerOptions](../harmonyos-references/map-common.md#markeroptions)：在地图上设置标记，可以通过rotation参数设置旋转角度。
* [addPolyline](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)：在地图上添加一条折线作为模拟路线。

## 解决方案

路线起点和终点两端的经纬度坐标相减，通过反正切函数得到弧度值，然后再转角度，这就是路线和正北的夹角度数；然后将图片从正北方向旋转该度数，使得车头正对路线方向。

完整示例参考如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { UIContext, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct MarkerDemo {
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapPolyline?: map.MapPolyline;
  private mapEventManager?: map.MapEventManager;
  positions: mapCommon.LatLng[] = [{ longitude: 118.78, latitude: 31.965 }, { longitude: 118.79, latitude: 31.975 },
    { longitude: 118.79, latitude: 31.982 }];

  // 显示页面时设置沉浸式效果
  onPageShow(): void {
    window.getLastWindow(new UIContext().getHostContext() as common.UIAbilityContext, (err, win) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      win.setWindowLayoutFullScreen(true);
    });
  }

  // 隐藏页面时解除沉浸式效果
  onPageHide(): void {
    window.getLastWindow(new UIContext().getHostContext() as common.UIAbilityContext, (err, win) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      win.setWindowLayoutFullScreen(false);
    });
  }

  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: this.positions[0],
        zoom: 15
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // polyline初始化参数
        let polylineOption: mapCommon.MapPolylineOptions = {
          points: this.positions,
          clickable: true,
          startCap: mapCommon.CapStyle.ROUND,
          endCap: mapCommon.CapStyle.ROUND,
          geodesic: false,
          jointType: mapCommon.JointType.ROUND,
          patterns: [{ type: 0, length: 100 }],
          visible: true,
          width: 50,
          zIndex: 10,
          gradient: false,
          colors: [0xff000ff00, 0xff000ff00],
          customTexture: $r('app.media.icon'),
        };
        // 创建polyline
        this.mapPolyline = await this.mapController.addPolyline(polylineOption);

        this.mapEventManager = this.mapController.getEventManager();

        this.mapEventManager.on('polylineClick', (polyline: map.MapPolyline) => {
          console.info('polylineClick', `callback polyline = ${polyline.getId()}`);
        });
        // 第一段路线起点和终点两端的经纬度坐标相减
        let startY = this.positions[1].longitude - this.positions[0].longitude;
        let startX = this.positions[1].latitude - this.positions[0].latitude;
        // 通过反正切函数得到的弧度值再转角度
        const angle: number = Math.atan2(startY, startX) * 180 / Math.PI;
        console.info('angle: ' + angle + '');
        // 地图标记
        let markerOptions: mapCommon.MarkerOptions = {
          position: this.positions[0],
          icon: $r('app.media.Car'),
          // 设置图片旋转角度
          rotation: angle,
          clickable: true,
        };
        await this.mapController?.addMarker(markerOptions);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({
          mapOptions: this.mapOption,
          mapCallback: this.callback,
        });
      }.width('100%');
    }.height('100%');
  }
}
```
