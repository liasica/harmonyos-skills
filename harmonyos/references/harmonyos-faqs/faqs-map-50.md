---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-50
title: 如何自定义Marker样式
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何自定义Marker样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:525b8c9ef7a9f20bf5b55b7ca40f7f37acb48b17d11844d959eb4521bb0d8522
---

## 问题现象

使用Map Kit添加Marker标记时，默认为固定样式，如何根据不同的业务场景，添加自定义的Marker样式？

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* [getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)：以当前canvas指定区域内的像素创建PixelMap对象。
* [createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)：通过图片解码参数创建PixelMap对象。

## 解决方案

* 方式一：替换Marker标记为本地图片。

  配置[mapCommon.MarkerOptions](../harmonyos-references/map-common.md#markeroptions)中icon参数为本地图片，图片文件存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径。

  ```ts
  // 替换icon为图片类型
  let markerOptions1: mapCommon.MarkerOptions = {
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
    // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
    icon: 'test.png'
  };
  try {
    this.marker1 = await this.mapController.addMarker(markerOptions1);
    console.info(`Add Markers success, ${this.marker1}`);
  } catch (e) {
    console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
  }
  ```
* 方式二：替换Marker标记为自定义Builder内容。

  通过@Builder设计自定义Marker的UI组件样式，然后配置[mapCommon.MarkerOptions](../harmonyos-references/map-common.md#markeroptions)中iconBuilder为@Builder装饰的组件。参见[自定义组件实现Marker图标](../harmonyos-guides/map-marker.md#自定义组件实现marker图标)。

  ```ts
  // 替换Marker为Builder样式
  let markerOptions2: mapCommon.MarkerOptions = {
    position: {
      latitude: 31.994410259206815,
      longitude: 118.77625379397866
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
    iconBuilder: () => {
      this.renderBuilder();
    }
  };
  try {
    this.marker2 = await this.mapController.addMarker(markerOptions2);
    console.info(`Add Markers success, ${this.marker2}`);
  } catch (e) {
    console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
  }
  ```
* 方式三：替换Marker标记为自定义画布内容。

  通过[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)绘制自定义画布内容，使用[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)接口转换为PixelMap格式图片，配置[mapCommon.MarkerOptions](../harmonyos-references/map-common.md#markeroptions)中icon参数为转换后的PixelMap图片。

  ```ts
  // 替换Marker为Canvas样式
  let canvas: image.PixelMap = await this.CanvasIcon();
  let markerOptions3: mapCommon.MarkerOptions = {
    position: {
      latitude: 31.984410259206815,
      longitude: 118.77625379397866
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
    icon: canvas
  };
  try {
    this.marker3 = await this.mapController.addMarker(markerOptions3);
    console.info(`Add Markers success, ${this.marker3}`);
  } catch (e) {
    console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
  }
  ```
* 方式四：替换Marker标记为网络图片。
  1. 通过[request](../harmonyos-references/js-apis-http.md#request)访问网络图片。
  2. 通过[image.createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9-2)将获取的网络图片buffer创建图片源实例。
  3. 通过[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)将图片转换为PixelMap格式图片。
  4. 配置mapCommon.MarkerOptions中icon参数为转换后的PixelMap图片。

  ```ts
  // 替换Marker为网络图片样式
  try {
    this.imageMap = await this.getPicture();
  } catch (e) {
    console.error(`Failed to getPicture, code is：${e.code}, message is ${e.message}`);
  }

  let markerOptions4: mapCommon.MarkerOptions = {
    position: {
      latitude: 31.994410259206815,
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
    icon: this.imageMap
  };
  try {
    this.marker4 = await this.mapController.addMarker(markerOptions4);
    console.info(`Add Markers success, ${this.marker4}`);
  } catch (e) {
    console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
  }
  ```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/PvlQ3r2FR3WKilS6mU4e6g/zh-cn_image_0000002628394396.png "点击放大")

完整代码：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import image from '@ohos.multimedia.image';
import { http } from '@kit.NetworkKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct CustomMarker {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private marker1?: map.Marker;
  private marker2?: map.Marker;
  private marker3?: map.Marker;
  private marker4?: map.Marker;
  private imageMap: image.PixelMap | Resource = $r('app.media.startIcon');
  decodingOptions: image.DecodingOptions = {
    editable: true,
    desiredPixelFormat: 3,
    desiredSize: { height: 150, width: 150 }
  };
  @State mapHeight: number = 0;

  async aboutToAppear() {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
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
        // 替换icon为图片类型
        let markerOptions1: mapCommon.MarkerOptions = {
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
          // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
          icon: 'test.png'
        };
        try {
          this.marker1 = await this.mapController.addMarker(markerOptions1);
          console.info(`Add Markers success, ${this.marker1}`);
        } catch (e) {
          console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
        }

        // 替换Marker为Builder样式
        let markerOptions2: mapCommon.MarkerOptions = {
          position: {
            latitude: 31.994410259206815,
            longitude: 118.77625379397866
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
          iconBuilder: () => {
            this.renderBuilder();
          }
        };
        try {
          this.marker2 = await this.mapController.addMarker(markerOptions2);
          console.info(`Add Markers success, ${this.marker2}`);
        } catch (e) {
          console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
        }

        // 替换Marker为Canvas样式
        let canvas: image.PixelMap = await this.CanvasIcon();
        let markerOptions3: mapCommon.MarkerOptions = {
          position: {
            latitude: 31.984410259206815,
            longitude: 118.77625379397866
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
          icon: canvas
        };
        try {
          this.marker3 = await this.mapController.addMarker(markerOptions3);
          console.info(`Add Markers success, ${this.marker3}`);
        } catch (e) {
          console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
        }

        // 替换Marker为网络图片样式
        try {
          this.imageMap = await this.getPicture();
        } catch (e) {
          console.error(`Failed to getPicture, code is：${e.code}, message is ${e.message}`);
        }

        let markerOptions4: mapCommon.MarkerOptions = {
          position: {
            latitude: 31.994410259206815,
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
          icon: this.imageMap
        };
        try {
          this.marker4 = await this.mapController.addMarker(markerOptions4);
          console.info(`Add Markers success, ${this.marker4}`);
        } catch (e) {
          console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  // 获取网络图片
  async getPicture(): Promise<image.PixelMap> {
    // 请填写一个具体的网络图片地址
    return new Promise(async (resolve, reject) => {
      http.createHttp().request('xxx.xxx.xxx',
        async (error: BusinessError, data: http.HttpResponse) => {
          if (error) {
            console.error('get network picture error:' + error.message);
            reject((new Error(error.message)));
          }
          if (200 === data.responseCode) {
            console.info('get network picture success:');
            const imageData: ArrayBuffer = data.result as ArrayBuffer;
            // 通过ArrayBuffer创建图片源实例
            const imageSource: image.ImageSource = image.createImageSource(imageData);
            // 通过属性创建PixelMap
            let imageMap = await imageSource.createPixelMap(this.decodingOptions);
            resolve(imageMap);
          } else {
            reject((new Error('get network picture failed')));
          }
        });
    });
  }

  // 绘制Canvas图形
  async CanvasIcon(): Promise<image.PixelMap> {
    let offCanvas: OffscreenCanvas = new OffscreenCanvas(60, 60);
    let settings: RenderingContextSettings = new RenderingContextSettings(true);
    let offContext = offCanvas.getContext('2d', settings);
    // 绘制圆形
    offContext.fillStyle = 0xff990000;
    offContext.beginPath();
    offContext.arc(30, 30, 30, 0, 6.28);
    offContext.stroke();
    offContext.fill();
    offContext.save();

    // 在圆形内绘制文本，文本信息为clusterItems的第一个聚合点的经度
    offContext.font = '16vp sans-serif';
    offContext.textAlign = 'center';
    offContext.textBaseline = 'middle';
    offContext.fillStyle = 0xffffffff;
    offContext.fillText('Canvas', 30, 30);
    offContext.restore();
    let iconPixelMap = offContext.getPixelMap(0, 0, 60, 60);
    return iconPixelMap;
  }

  // 创建自定义组件
  @Builder
  renderBuilder() {
    Stack({ alignContent: Alignment.Center }) {
      Column() {
        Text('自定义')
          .fontColor(Color.White);
        Text('Builder')
          .fontColor(Color.White);
      }
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.Blue)
      .borderRadius(10)
      .padding(2);
    }
    .height(50)
    .width(200);
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight);
      }.width('100%');
    }
    .ignoreLayoutSafeArea();
  }
}
```
