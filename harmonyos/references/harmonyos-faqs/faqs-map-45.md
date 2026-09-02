---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-45
title: Map Kit如何添加自定义信息窗并实现点击响应
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit如何添加自定义信息窗并实现点击响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:f8042ff8919cfd2d78b87a6513287bf42ebc9b57d634ccd4bff00e63ca960a0a
---

## 问题现象

Map Kit中Marker标记仅能实现简单图标的显示，如何实现标记点更多信息的展示，自定义设计展示的样式，并实现信息窗的点击响应交互。

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* [customInfoWindow](../harmonyos-references/map-mapcomponent.md#mapcomponent)：自定义信息窗。在[customInfoWindowCallback](../harmonyos-references/map-mapcomponent.md#custominfowindowcallback)中绘制自定义UI样式。

## 解决方案

1. 添加Marker，在[MarkerOptions](../harmonyos-references/map-common.md#markeroptions)中设置clickable为true，设置信息窗title。如果需在信息窗中展示副标题信息，也可以设置snippet信息。

   ```ts
   let markerOptions: mapCommon.MarkerOptions = {
     position: {
       latitude: 32.120750,
       longitude: 118.788765
     },
     clickable: true,
     // 设置信息窗标题，点击标记后可展示信息窗
     title: '☆点击收藏'
   };
   await this.mapController?.addMarker(markerOptions);
   ```
2. 设置自定义信息窗UI样式，通过[getTitle](../harmonyos-references/map-map-marker.md#gettitle)和[setTitle](../harmonyos-references/map-map-marker.md#settitle)可以获取和设置当前Marker信息窗的标题。在UI中添加onClick点击事件，进行相关点击的响应和操作。

   ```ts
   // 自定义信息窗BuilderParam
   @BuilderParam customInfoWindow: ($$: map.MarkerDelegate) => void = this.customInfoWindowBuilder;

   // 自定义信息窗Builder
   @Builder
   customInfoWindowBuilder($$: map.MarkerDelegate) {
     if ($$.marker) {
       Text($$.marker.getTitle())
         .width(120)
         .height(30)
         .margin({ bottom: 3 })
         .backgroundColor(Color.White)
         .textAlign(TextAlign.Center)
         .fontColor(Color.Black)
         .font({ size: 18, weight: 10 })
         .border({ width: 1, color: Color.Black, radius: 8 })
         .onClick(() => {
           $$.marker?.setTitle('★已收藏');
         });

     }
   }
   ```
3. 在初始化地图时，设置customInfoWindow。

   ```ts
   build() {
     Stack() {
       Column() {
         MapComponent({
           mapOptions: this.mapOptions,
           mapCallback: this.callback,
           // 自定义信息窗
           customInfoWindow: this.customInfoWindow
         })
           .height(this.mapHeight);
       }.width('100%');
     }.ignoreLayoutSafeArea();
   }
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/fh81r9QITiiD7VkMUu22JQ/zh-cn_image_0000002658793655.png "点击放大")

   完整代码：

   ```ts
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   import { display } from '@kit.ArkUI';

   @Entry
   @Component
   struct MarkerDemo {
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     @State mapHeight: number = 0;

     aboutToAppear(): void {
       let displayClass = display.getDefaultDisplaySync();
       this.mapHeight = this.getUIContext().px2vp(displayClass.height);
       this.mapOptions = {
         position: {
           target: {
             latitude: 32.120750,
             longitude: 118.788765
           },
           zoom: 15
         }
       };

       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           let markerOptions: mapCommon.MarkerOptions = {
             position: {
               latitude: 32.120750,
               longitude: 118.788765
             },
             clickable: true,
             // 设置信息窗标题，点击标记后可展示信息窗
             title: '☆点击收藏'
           };
           await this.mapController?.addMarker(markerOptions);
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     build() {
       Stack() {
         Column() {
           MapComponent({
             mapOptions: this.mapOptions,
             mapCallback: this.callback,
             // 自定义信息窗
             customInfoWindow: this.customInfoWindow
           })
             .height(this.mapHeight);
         }.width('100%');
       }.ignoreLayoutSafeArea();
     }

     // 自定义信息窗BuilderParam
     @BuilderParam customInfoWindow: ($$: map.MarkerDelegate) => void = this.customInfoWindowBuilder;

     // 自定义信息窗Builder
     @Builder
     customInfoWindowBuilder($$: map.MarkerDelegate) {
       if ($$.marker) {
         Text($$.marker.getTitle())
           .width(120)
           .height(30)
           .margin({ bottom: 3 })
           .backgroundColor(Color.White)
           .textAlign(TextAlign.Center)
           .fontColor(Color.Black)
           .font({ size: 18, weight: 10 })
           .border({ width: 1, color: Color.Black, radius: 8 })
           .onClick(() => {
             $$.marker?.setTitle('★已收藏');
           });

       }
     }

   }
   ```

## 常见FAQ

Q：如何默认显示信息窗？

A：在初始化地图时，添加Marker后，设置[setInfoWindowVisible](../harmonyos-references/map-map-marker.md#setinfowindowvisible)为true。
