---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-19
title: 地图服务覆盖物image如何添加网络图片url
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图服务覆盖物image如何添加网络图片url
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7e4dcb02bee6a061eef6c06aab874ded2c1cadef3e9ccaea7b54c0d19d6da2d8
---

## 问题现象

Map Kit地图服务开发需要添加覆盖物，ImageOverlayParams参数中image只支持ResourceStr和image.PixelMap两种格式，如何将网络图片url添加到image中？

## 背景知识

* [Map Kit](../harmonyos-guides/map-introduction.md)：Map Kit（地图服务）为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。
* [覆盖物](../harmonyos-guides/map-coverings.md)：覆盖物是一种位于底图和底图标注层之间的特殊Overlay，该图层不会遮挡地图标注信息。通过[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类来设置，开发者可以通过[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类设置一张图片，该图片可随地图的平移、缩放、旋转等操作做相应的变换。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)创建一个PixelMap实例。

## 解决方案

[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)类中image参数只支持ResourceStr和image.PixelMap，无法直接添加网络图片url，可以把网络图片的url转换成[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)类型显示。

1. 通过http的request下载网络图片资源，并把网络图片url下载的ArrayBuffer类型的图片转换为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)类型数据。

   ```ts
   // 通过http的request方法从网络下载图片资源
   async getPicture() {
     // 请填写一个具体的网络图片地址
     http.createHttp().request('xx.xx.xx.xx.png',
       async (error: BusinessError, data: http.HttpResponse) => {
         if (error) {
           console.error('get network picture error:' + error.message);
           return;
         }
         if (200 === data.responseCode) {
           const imageData: ArrayBuffer = data.result as ArrayBuffer;
           // 通过ArrayBuffer创建图片源实例
           const imageSource: image.ImageSource = image.createImageSource(imageData);
           const options: image.InitializationOptions = {
             'alphaType': 0,
             'editable': false,
             'pixelFormat': 3,
             'scaleMode': 1,
             'size': { height: 50, width: 50 }
           };
           // 通过属性创建PixelMap
           this.imageMap = await imageSource.createPixelMap(options);
         }
       });
   }
   ```

2. 将转换后的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)图片添加到[ImageOverlayParams](../harmonyos-references/map-common.md#imageoverlayparams)的image参数中。

   ```screen
   Button('添加网络图片覆盖物').onClick(async () => {
     let imageOverlayParams: mapCommon.ImageOverlayParams = {
       // 覆盖物范围
       bounds: {
         southwest: { latitude: 32, longitude: 118 },
         northeast: { latitude: 32.4, longitude: 118.4 }
       },
       // 转换过后的PixelMap图片
       image: this.imageMap,
       transparency: 0.3,
       zIndex: 101,
       anchorU: 0.5,
       anchorV: 0.5,
       clickable: true,
       visible: true,
       bearing: 0
     };
     // 添加覆盖物
     await this.mapController?.addImageOverlay(imageOverlayParams);
   })
   ```

完整示例参考如下：

```screen
import { http } from '@kit.NetworkKit';
import { image } from '@kit.ImageKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { map, mapCommon, MapComponent } from '@kit.MapKit';

@Component
@Entry
struct Index {
  @State imageMap: image.PixelMap | Resource = $r('app.media.startIcon');
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapEventManager?: map.MapEventManager;

  // 通过http的request方法从网络下载图片资源
  async getPicture() {
    // 请填写一个具体的网络图片地址
    http.createHttp().request('xx.xx.xx.xx.png',
      async (error: BusinessError, data: http.HttpResponse) => {
        if (error) {
          console.error('get network picture error:' + error.message);
          return;
        }
        if (200 === data.responseCode) {
          const imageData: ArrayBuffer = data.result as ArrayBuffer;
          // 通过ArrayBuffer创建图片源实例
          const imageSource: image.ImageSource = image.createImageSource(imageData);
          const options: image.InitializationOptions = {
            'alphaType': 0,
            'editable': false,
            'pixelFormat': 3,
            'scaleMode': 1,
            'size': { height: 50, width: 50 }
          };
          // 通过属性创建PixelMap
          this.imageMap = await imageSource.createPixelMap(options);
        }
      });
  }

  async aboutToAppear() {
    // 设置地图属性模型
    this.mapOptions = {
      position: {
        target: {
          latitude: 32.2,
          longitude: 118.2
        },
        zoom: 10
      }
    };
    // 地图回调
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        await this.getPicture();
      } else {
        console.error(`地图初始化失败, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        Button('添加网络图片覆盖物').onClick(async () => {
          let imageOverlayParams: mapCommon.ImageOverlayParams = {
            // 覆盖物范围
            bounds: {
              southwest: { latitude: 32, longitude: 118 },
              northeast: { latitude: 32.4, longitude: 118.4 }
            },
            // 转换过后的PixelMap图片
            image: this.imageMap,
            transparency: 0.3,
            zIndex: 101,
            anchorU: 0.5,
            anchorV: 0.5,
            clickable: true,
            visible: true,
            bearing: 0
          };
          // 添加覆盖物
          await this.mapController?.addImageOverlay(imageOverlayParams);
        })
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback,
        })
          .width('100%')
          .height('90%');

      }.width('100%')
    }.height('100%')
  }
}
```

## 常见FAQ

Q：MapKit绘制中是否支持自定义覆盖物，比如图文覆盖和自定义排版？

A：当前地图覆盖物仅支持图片，不支持图文覆盖和自定义排版。
