---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-48
title: 如何将触摸点转换为地图经纬度坐标
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何将触摸点转换为地图经纬度坐标
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:25+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:4548e6a7d75061a3390751dbbe3f7c5f347f91a88beb8643d90051c9591635c7
---

## 问题现象

在集成地图场景的应用中，通常有这样一种场景：需要获取手指触摸点对应地图上的经纬度坐标。获取经纬度坐标后，再进行相关业务处理，譬如放置标记、逆地理编码展示详细地址、查看附近商店等。那么，如何将手指触摸点转换为对应地图上的经纬度坐标？

## 背景知识

* [层叠布局](../harmonyos-guides/arkts-layout-development-stack-layout.md) （Stack）：层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。
* [触摸事件](../harmonyos-references/ts-universal-events-touch.md)（onTouch）：手指在组件上按下、滑动或抬起时触发。
* [fromScreenLocation](../harmonyos-references/map-map-projection.md#fromscreenlocation)：将屏幕像素点坐标转换成经纬度。

## 解决方案

1. 获取手指触摸点对应于（地图可视区域的）屏幕的像素点。本例通过onTouch事件获取手指触摸点，通过LongPressGesture、PanGesture等手势也可获取手指触摸点位置。
2. 将手指触摸点位置对应的屏幕像素点通过fromScreenLocation转换为地图经纬度坐标。

   示例代码如下：

   ```ts
   import { map, mapCommon, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct FromScreenLocationDemo {
     private mapOptions?: mapCommon.MapOptions;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapController?: map.MapComponentController;
     private mapEventManager?: map.MapEventManager;

     aboutToAppear(): void {
       // 地图初始化参数，设置地图中心点坐标及层级
       this.mapOptions = {
         position: {
           target: {
             latitude: 39.9,
             longitude: 116.4
           },
           zoom: 10
         }
       };

       // 地图初始化的回调
       this.callback = async (err, mapController) => {
         if (!err) {
           // 获取地图的控制器类，用来操作地图
           this.mapController = mapController;
           this.mapEventManager = this.mapController.getEventManager();
           let callback = () => {
             console.info('on-mapLoad');
           };
           this.mapEventManager.on('mapLoad', callback);
         }
       };
     }

     build() {
       Stack() {
         Column() {
           Text('This is a Text').fontSize(40).backgroundColor(Color.Green).width('100%').height('10%');
           Stack() {
             MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
               .width('100%')
               .height('100%');
           }
           .width('100%')
           .height('100%')
           .onTouch((event) => {
             // 获取手指触摸位置对应的屏幕像素点
             let positionX = this.getUIContext().vp2px(event.touches[0].x);
             let positionY = this.getUIContext().vp2px(event.touches[0].y);
             let projection: map.Projection | undefined = this.mapController?.getProjection();
             if (projection) {
               let point: mapCommon.MapPoint = {
                 positionX: positionX,
                 positionY: positionY
               };
               // 转为地图的经纬度坐标
               let latLng: mapCommon.LatLng = projection.fromScreenLocation(point);
               this.getUIContext().getPromptAction().showToast({
                 message: 'longitude: ' + latLng.longitude + '  latitude:' + latLng.latitude,
                 duration: 3000
               });
             }
           });
         }.width('100%');
       }.height('100%');
     }
   }
   ```

   **说明** 

   * fromScreenLocation的入参为屏幕位置，是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。因此，要确保获取的屏幕位置是相对于地图可视区域计算的。
   * onTouch获取的x、y值单位为vp，fromScreenLocation的输入值单位是xp，需要通过[vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)进行转换。
   * fromScreenLocation转后的经纬度为GCJ02坐标系。
