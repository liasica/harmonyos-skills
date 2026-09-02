---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-5
title: 地图组件如何添加多个Marker并自定义样式
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图组件如何添加多个Marker并自定义样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:34f203043e82ddbe4c97b2b2c3d2149950bb0501a1592049160adaf05871ca0b
---

## 问题现象

如何在地图上实现多个Marker的效果，多个Marker的样式不同，需要自定义样式。

## 背景知识

* Map Kit提供的**点标记功能**（又称[Marker](../harmonyos-references/map-map-marker.md)）是地图开发的核心组件之一。它封装了大量的触发事件，例如点击事件、长按事件、拖拽事件。
* Marker的主要作用是在地图上标记任何位置，例如用户位置、车辆位置、店铺位置等一切带有位置属性的事物。
* 系统为Marker提供了默认的显示风格，同时也支持开发者进行自定义，来实现自定义标记、自定义信息窗等功能。

## 解决方案

* 添加多个Marker：可以通过调用map.MapComponentController类的[addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)方法，该方法会返回添加的Marker实例；再通过不同的[MarkerOptions](../harmonyos-references/map-common.md#markeroptions)参数调用该方法创建不同的Marker实例，即可在地图上添加多个Marker标记。
* 自定义Marker样式的实现：Marker的[icon属性](../harmonyos-references/map-common.md#markeroptions)可以自定义设置图片，可以尝试使用[组件截图](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md)的方式去构建Builder组件来实现Marker的自定义设置。

实现步骤如下：

1. 构造Marker自定义样式。
2. 通过组件截图的方式获取需要样式的图片，并添加Marker至地图上显示。

   ```ts
   import { map, mapCommon, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   import { image } from '@kit.ImageKit';

   @Entry
   @Component
   struct CustomizationMarker {
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     uiContext: UIContext = this.getUIContext();

     addMarker() {
       this.uiContext.getComponentSnapshot().createFromBuilder(() => {
         this.RandomBuilder();
       },
         async (error: Error, pixmap: image.PixelMap) => {
           if (error) {
             return;
           }
           // Marker初始化参数
           let markerOptions: mapCommon.MarkerOptions = {
             position: {
               latitude: 31.984410259206815,
               longitude: 118.76625379397866
             },
             rotation: 0,
             visible: true,
             zIndex: 0,
             alpha: 1,
             anchorU: 0.5,
             anchorV: 1,
             clickable: true,
             draggable: true,
             flat: false,
             icon: pixmap
           };
           this.mapController?.addMarker(markerOptions);
         });
     }

     aboutToAppear(): void {
       // 地图初始化参数
       this.mapOptions = {
         position: {
           target: {
             latitude: 31.984410259206815,
             longitude: 118.76625379397866
           },
           zoom: 15
         }
       };
       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           this.addMarker();
         }
       };
     }

     @Builder
     RandomBuilder() {
       Row() {
         Image($r('app.media.startIcon')).width(18).height(24)
         Column() {
           Text('200米')
             .fontSize(12)
             .fontColor('#1f2642')
             .fontWeight(FontWeight.Bold)
           Text('35分钟')
             .fontSize(12)
             .fontColor('#1f2642')
             .fontWeight(FontWeight.Bold)
             .margin({ top: 1 })
         }.margin({ left: 6 }).alignItems(HorizontalAlign.Start)

         Divider()
           .vertical(true)
           .width(1)
           .height(18)
           .backgroundColor('#c1cadd')
           .margin({ left: 8, right: 8 })

         Image($r('app.media.startIcon')).width(18).height(18)

         Text('导航')
           .fontSize(12)
           .fontColor('#1f2642')
           .fontWeight(FontWeight.Bold)
           .margin({ left: 2 })
       }
       .margin({ bottom: 3 })
       .padding({
         left: 6,
         right: 6,
         top: 8,
         bottom: 8
       })
       .backgroundColor(Color.White)
       .borderRadius(12)
       .shadow({ radius: 12, color: '#33000000' })
     }

     build() {
       Stack() {
         Column() {
           MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
         }.width('100%')
       }.height('100%')
     }
   }
   ```

## 常见FAQ

Q：地图上如何实现自定义信息窗？

A：自定义信息窗可以参考：[自定义信息窗](../harmonyos-guides/map-marker.md#自定义信息窗)。

Q：Marker中的图标可以使用远程地址吗？

A：不可以，icon参数目前只支持三种类型，分别为string、[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)和[Resource](../harmonyos-references/ts-types.md#resource)。当类型为string时，可以传入资源相对路径格式或者toDataURL格式。所以如果需要传入远程图片地址，可以下载到本地以后使用本地相对路径或者转化成Base64格式以data:image/png;Base64,<图片的Base64字节编码值>加载。

Q：地图组件怎么删除Marker？

A：可以使用[remove](../harmonyos-references/map-map-baseoverlay.md#remove)方法从地图移除覆盖物，实现删除单个Marker。或者可以使用[clear](../harmonyos-references/map-map-mapcomponentcontroller.md#clear)方法删除地图上所有标记。

Q：使用createFromBuilder自定义Marker图标时，为什么全局Builder不生效？

A：[createFromBuilder](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12)不支持全局Builder，包括通过wrapBuilder封装的全局Builder。建议使用局部Builder来构建Marker的自定义样式。

Q：删除其他Marker时，为什么当前Marker弹出的自定义信息窗会自动隐藏？

A：调用remove()方法删除Marker时会触发覆盖物列表的变更，导致当前Marker的自定义信息窗受到影响。可以使用[setVisible(false)](../harmonyos-references/map-map-baseoverlay.md#setvisible)代替remove()，这样不会触发覆盖物列表的变更，自定义信息窗不会受影响。
