---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-4
title: 如何给地图组件添加含数字角标的自定义图片标记
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何给地图组件添加含数字角标的自定义图片标记
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f95cea7f354887473190fde2a9433ef33e5d4c86adc3834cdd8087cf4ef3f65e
---

## 问题现象

在显示地图Marker时，为了实现自定义图片和动态更新标记消息数，需要给地图组件添加含数字角标的自定义图片标记，该如何实现？

## 背景知识

* [自定义标记](../harmonyos-guides/map-marker.md#自定义标记)：通过在MarkerOptions中将icon属性（支持string|image.PixelMap | Resource类型）设置为自定义图标的资源，可将默认标记图标修改成自定义图标。
* [Badge](../harmonyos-references/ts-container-badge.md#badge-1)：信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。
* [组件截图](../harmonyos-references/js-apis-arkui-componentsnapshot.md)：提供获取组件截图的能力，包括已加载的组件的截图和没有加载的组件的截图。
* [OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)：使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制带数字的合成图片。

## 解决方案

* **方案一**：

  首先创建一个@Builder函数并绘制样式，其中使用Badge组件添加数字标记，再使用组件截图将@Builder函数转成PixelMap，最后使用自定义标记将PixelMap设置到Marker上。

  ```ts
  @Component
  struct MarkerDemoA {
    private mapOptions?: mapCommon.MapOptions;
    private mapController?: map.MapComponentController;
    private callback?: AsyncCallback<map.MapComponentController>;
    uiContext: UIContext = this.getUIContext();

    @Builder
    RandomBuilder() { // 创建一个@Builder函数并绘制标记样式
      Row() {
        Badge({
          count: 3,
          style: { badgeColor: Color.Red },
          position: BadgePosition.RightTop,
        }) {
          Row() {
            Text('自定义图片标记');
          }
          .padding(12)
          .backgroundColor(Color.White)
          .borderRadius(12)
          .shadow({ radius: 12, color: '#33000000' });
        };
      }
      .backgroundColor('#00000000')
      .padding(12);
    }

    addMarker() {
      // 使用组件截图将@Builder函数转成PixelMap，添加标记到地图。
      this.uiContext.getComponentSnapshot().createFromBuilder(() => {
        this.RandomBuilder();
      },
        async (error: Error, pixelMap: image.PixelMap) => {
          if (error) {
            console.error(`error:${error}`);
            return;
          }

          // Marker初始化参数
          let markerOptions: mapCommon.MarkerOptions = {
            // 填入目标经纬度
            position: {
              latitude: 39.918,
              longitude: 116.397
            },
            icon: pixelMap
          };
          this.mapController?.addMarker(markerOptions);
        });
    }

    aboutToAppear(): void {
      // 地图初始化参数
      this.mapOptions = {
        // 填入目标经纬度
        position: {
          target: {
            latitude: 39.918,
            longitude: 116.397
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

    build() {
      Stack() {
        Column() {
          MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
        }.width('100%');
      }.height('100%');
    }
  }
  ```

* **方案二：**

  使用Canvas生成带数字的标记。

  ```ts
  @Component
  struct MarkerDemoB {
    private mapOptions?: mapCommon.MapOptions;
    private mapController?: map.MapComponentController;
    private callback?: AsyncCallback<map.MapComponentController>;
    uiContext: UIContext = this.getUIContext();
    // 示例用图片，实际使用中请自行替换。
    private img?: ImageBitmap;

    // 使用Canvas动态生成带数字的标记
    async createNumberedMarker(num: number): Promise<string> {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // 示例用图片，实际使用中请自行替换。
      let fileData: Uint8Array = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
      let imageSource: image.ImageSource = image.createImageSource(fileData.buffer);
      let options: image.DecodingOptions = { editable: true, desiredPixelFormat: image.PixelMapFormat.RGBA_8888 };
      let pixelMap: image.PixelMap = imageSource.createPixelMapSync(options);
      this.img = new ImageBitmap(pixelMap);
      // 创建Canvas绘制上下文
      const canvasRenderingContext = new OffscreenCanvasRenderingContext2D(60, 60);

      // 绘制基础图标
      canvasRenderingContext.drawImage(this.img, 0, 10, 50, 50);

      // 绘制数字角标
      canvasRenderingContext.fillStyle = 'red';
      canvasRenderingContext.beginPath();
      canvasRenderingContext.arc(50, 10, 10, 0, Math.PI * 2);
      canvasRenderingContext.fill();
      canvasRenderingContext.fillStyle = 'white';
      canvasRenderingContext.font = '14vp sans-serif';
      canvasRenderingContext.textAlign = 'center';
      canvasRenderingContext.fillText(num.toString(), 50, 14);

      // 生成Base64图片数据
      return canvasRenderingContext.toDataURL();
    }

    async addMarker() {
      // 使用动态生成的图片
      const dynamicIcon = await this.createNumberedMarker(5);
      let markerOptions: mapCommon.MarkerOptions = {
        // 填入目标经纬度,
        position: {
          latitude: 39.918,
          longitude: 116.397
        },
        icon: dynamicIcon, // 使用生成的Base64图片
        anchorU: 0.5, // 设置锚点为中心
        anchorV: 0.5
      };
      this.callback = async (err, mapController) => {
        if (!err) {
          this.mapController = mapController;
          this.mapController?.addMarker(markerOptions);
        }
      };
    }

    aboutToAppear(): void {
      // 地图初始化参数
      this.mapOptions = {
        // 填入目标经纬度
        position: {
          target: {
            latitude: 39.918,
            longitude: 116.397
          },
          zoom: 15
        }
      };
      this.callback = async (err, mapController) => {
        if (!err) {
          this.mapController = mapController;
        }
      };
      this.addMarker();
    }

    build() {
      Stack() {
        Column() {
          MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
        }.width('100%');
      }.height('100%');
    }
  }
  ```

完整示例参考如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct IndexMarkerDemo {
  @State currentIndex: number = 0;

  @Builder
  tabBuilder(index: number, name: string | Resource) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? '#0A59F7' : '#E6000000')
        .fontSize(16)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 });
      Divider()
        .width(48)
        .strokeWidth(2)
        .color('#0A59F7')
        .opacity(this.currentIndex === index ? 1 : 0);
    };
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start }) {
        TabContent() {
          MarkerDemoA();
        }.tabBar(this.tabBuilder(0, '方案一'));

        TabContent() {
          MarkerDemoB();
        }.tabBar(this.tabBuilder(1, '方案二'));
      }
      .barWidth('100%')
      .barHeight(52)
      .onAnimationStart((index: number, targetIndex: number) => {
        console.info(`${index.toString()}`);
        this.currentIndex = targetIndex;
      })
      .width('100%')
      .height('100%');
    }.width('100%');
  }
}

@Component
struct MarkerDemoA {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  uiContext: UIContext = this.getUIContext();

  @Builder
  RandomBuilder() { // 创建一个@Builder函数并绘制标记样式
    Row() {
      Badge({
        count: 3,
        style: { badgeColor: Color.Red },
        position: BadgePosition.RightTop,
      }) {
        Row() {
          Text('自定义图片标记');
        }
        .padding(12)
        .backgroundColor(Color.White)
        .borderRadius(12)
        .shadow({ radius: 12, color: '#33000000' });
      };
    }
    .backgroundColor('#00000000')
    .padding(12);
  }

  addMarker() {
    // 使用组件截图将@Builder函数转成PixelMap，添加标记到地图。
    this.uiContext.getComponentSnapshot().createFromBuilder(() => {
      this.RandomBuilder();
    },
      async (error: Error, pixelMap: image.PixelMap) => {
        if (error) {
          console.error(`error:${error}`);
          return;
        }

        // Marker初始化参数
        let markerOptions: mapCommon.MarkerOptions = {
          // 填入目标经纬度
          position: {
            latitude: 39.918,
            longitude: 116.397
          },
          icon: pixelMap
        };
        this.mapController?.addMarker(markerOptions);
      });
  }

  aboutToAppear(): void {
    // 地图初始化参数
    this.mapOptions = {
      // 填入目标经纬度
      position: {
        target: {
          latitude: 39.918,
          longitude: 116.397
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

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
      }.width('100%');
    }.height('100%');
  }
}

@Component
struct MarkerDemoB {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  uiContext: UIContext = this.getUIContext();
  // 示例用图片，实际使用中请自行替换。
  private img?: ImageBitmap;

  // 使用Canvas动态生成带数字的标记
  async createNumberedMarker(num: number): Promise<string> {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 示例用图片，实际使用中请自行替换。
    let fileData: Uint8Array = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
    let imageSource: image.ImageSource = image.createImageSource(fileData.buffer);
    let options: image.DecodingOptions = { editable: true, desiredPixelFormat: image.PixelMapFormat.RGBA_8888 };
    let pixelMap: image.PixelMap = imageSource.createPixelMapSync(options);
    this.img = new ImageBitmap(pixelMap);
    // 创建Canvas绘制上下文
    const canvasRenderingContext = new OffscreenCanvasRenderingContext2D(60, 60);

    // 绘制基础图标
    canvasRenderingContext.drawImage(this.img, 0, 10, 50, 50);

    // 绘制数字角标
    canvasRenderingContext.fillStyle = 'red';
    canvasRenderingContext.beginPath();
    canvasRenderingContext.arc(50, 10, 10, 0, Math.PI * 2);
    canvasRenderingContext.fill();
    canvasRenderingContext.fillStyle = 'white';
    canvasRenderingContext.font = '14vp sans-serif';
    canvasRenderingContext.textAlign = 'center';
    canvasRenderingContext.fillText(num.toString(), 50, 14);

    // 生成Base64图片数据
    return canvasRenderingContext.toDataURL();
  }

  async addMarker() {
    // 使用动态生成的图片
    const dynamicIcon = await this.createNumberedMarker(5);
    let markerOptions: mapCommon.MarkerOptions = {
      // 填入目标经纬度,
      position: {
        latitude: 39.918,
        longitude: 116.397
      },
      icon: dynamicIcon, // 使用生成的Base64图片
      anchorU: 0.5, // 设置锚点为中心
      anchorV: 0.5
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        this.mapController?.addMarker(markerOptions);
      }
    };
  }

  aboutToAppear(): void {
    // 地图初始化参数
    this.mapOptions = {
      // 填入目标经纬度
      position: {
        target: {
          latitude: 39.918,
          longitude: 116.397
        },
        zoom: 15
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
      }
    };
    this.addMarker();
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
      }.width('100%');
    }.height('100%');
  }
}
```
