---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/map-kit-faq-0001
title: 地图组件Marker标记与样式自定义常见问题
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 常见问题 > 地图组件Marker标记与样式自定义常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:23+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:df7bd4ea2339da87fb9c30e386516f12a44fd61b726faaf9e3b35ef0716e5752
---

**Q：如何在地图上实现多个Marker的效果，多个Marker的样式不同，需要自定义样式？**

**A**：添加多个Marker和自定义Marker样式的实现方式如下：

* 添加多个Marker：可以通过调用map.MapComponentController类的[addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#section0810361284)方法，该方法会返回添加的Marker实例；再通过不同的[MarkerOptions](../harmonyos-references/map-common.md#section559041743210)参数调用该方法创建不同的Marker实例，即可在地图上添加多个Marker标记。
* 自定义Marker样式的实现：Marker的[icon属性](../harmonyos-references/map-common.md#section559041743210)可以自定义设置图片，可以尝试使用[组件截图](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md)的方式去构建Builder组件来实现Marker的自定义设置。

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

**Q：地图上如何实现自定义信息窗？**

**A**：自定义信息窗可以参考：[自定义信息窗](../harmonyos-guides/map-marker.md#section1930164112317)。

**Q：Marker中的图标可以使用远程地址吗？**

**A**：不可以，icon参数目前只支持三种类型，分别为string、[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)和[Resource](../harmonyos-references/ts-types.md#resource)。当类型为string时，可以传入资源相对路径格式或者toDataURL格式。所以如果需要传入远程图片地址，可以下载到本地以后使用本地相对路径或者转化成Base64格式以data:image/png;Base64,<图片的Base64字节编码值>加载。

**Q：地图组件怎么删除Marker？**

**A**：可以使用[remove](../harmonyos-references/map-map-baseoverlay.md#section39155506439)方法从地图移除覆盖物，实现删除单个Marker。或者可以使用[clear](../harmonyos-references/map-map-mapcomponentcontroller.md#section121439349711)方法删除地图上所有标记。

**Q：使用createFromBuilder自定义Marker图标时，为什么全局Builder不生效？**

**A**：[createFromBuilder](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12)不支持全局Builder，包括通过wrapBuilder封装的全局Builder。建议使用局部Builder来构建Marker的自定义样式。

**Q：删除其他Marker时，为什么当前Marker弹出的自定义信息窗会自动隐藏？**

**A**：调用remove()方法删除Marker时会触发覆盖物列表的变更，导致当前Marker的自定义信息窗受到影响。可以使用[setVisible(false)](../harmonyos-references/map-map-baseoverlay.md#setvisible)代替remove()，这样不会触发覆盖物列表的变更，自定义信息窗不会受影响。

**Q：在显示地图Marker时，为了实现自定义图片和动态更新标记消息数，需要给地图组件添加含数字角标的自定义图片标记，该如何实现？**

**A**：方案一：

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

方案二：

使用Canvas生成带数字的标记，示例代码如下：

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

完整实例代码：

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

**Q：Map Kit使用GCJ02坐标系，当使用WGS84坐标图源时，使用Map Kit自带的setMyLocation设置我的位置时，我的位置图标是GCJ02坐标系，在WGS84坐标地图上会产生偏移，所以无法使用自带的我的位置相关能力。使用WGS84坐标图源时，如何通过Marker实现MyLocationDisplayType.FOLLOW\_ROTATE相同效果，即连续定位，且将相机移动到地图中心点，定位蓝点依照设备方向旋转，并且会跟随设备移动？**

**A**：前提条件：需申请ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION、ohos.permission.ACCELEROMETER权限。

1. 创建Marker标记：

   ```ts
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
             anchorV: 0.5,
             clickable: true,
             draggable: true,
             flat: false
           };
           this.marker = await this.mapController.addMarker(markerOptions);
   ```
2. 通过sensor.on(sensor.SensorId.ORIENTATION)监听设备方向，通过setRotation设置Marker标记的旋转角度为设备方向角度：

   ```ts
   try {
             sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
               let direction = Math.round(data.alpha);
               let nowOrientation = display.getDefaultDisplaySync().orientation;
               if (nowOrientation !== 0) {
                 direction = direction - 90 * nowOrientation;
                 if (direction < 0) {
                   direction = direction + 360;
                 }
               }
               this.marker?.setRotation(direction);
             }, { interval: 100000000 });
           } catch (error) {
             console.error(`Failed to invoke on. Code: ${error.code}, message: ${error.message}`);
           }
   ```
3. 通过geoLocationManager.on('locationChange')监听位置变化，使用setPosition设置标记的位置为监听返回的坐标。注意位置监听返回的坐标是WGS84坐标系，在WGS84图源上直接使用该坐标设置Marker位置即可，无需转换为GCJ02坐标系。同时配置moveCamera接口将相机移动至marker为屏幕中心点：

   ```ts
   let requestInfo: geoLocationManager.LocationRequest = {
             'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
             'scenario': geoLocationManager.LocationRequestScenario.UNSET,
             'timeInterval': 1,
             'distanceInterval': 0,
             'maxAccuracy': 0
           };
           let locationChange = (location: geoLocationManager.Location): void => {
             console.info('locationChange: data: ' + JSON.stringify(location));
             // 添加WGS84坐标Marker
             this.marker?.setPosition(location);
             // 并将相机移动到地图中心点
             let cameraUpdate = map.newLatLng(location);
             this.mapController?.moveCamera(cameraUpdate);
           };
   ```

完整代码：

Index.ets：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';
import { sensor } from '@kit.SensorServiceKit';
import { display } from '@kit.ArkUI';
import { Permissions } from '@kit.AbilityKit';
import PermissionsRequest from '../utils/PermissionsRequest';

@Entry
@Component
struct Index {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private marker?: map.Marker;

  async aboutToAppear() {
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
        let permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
        await PermissionsRequest.commonRequestPermissions(this.getUIContext(), permissions);
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
          anchorV: 0.5,
          clickable: true,
          draggable: true,
          flat: false
        };
        this.marker = await this.mapController.addMarker(markerOptions);
        // 监听设备方向，设置Marker的旋转角度
        try {
          sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
            let direction = Math.round(data.alpha);
            let nowOrientation = display.getDefaultDisplaySync().orientation;
            if (nowOrientation !== 0) {
              direction = direction - 90 * nowOrientation;
              if (direction < 0) {
                direction = direction + 360;
              }
            }
            this.marker?.setRotation(direction);
          }, { interval: 100000000 });
        } catch (error) {
          console.error(`Failed to invoke on. Code: ${error.code}, message: ${error.message}`);
        }

        // 持续监听设备位置，更新Marker点的位置
        let requestInfo: geoLocationManager.LocationRequest = {
          'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
          'scenario': geoLocationManager.LocationRequestScenario.UNSET,
          'timeInterval': 1,
          'distanceInterval': 0,
          'maxAccuracy': 0
        };
        let locationChange = (location: geoLocationManager.Location): void => {
          console.info('locationChange: data: ' + JSON.stringify(location));
          // 添加WGS84坐标Marker
          this.marker?.setPosition(location);
          // 并将相机移动到地图中心点
          let cameraUpdate = map.newLatLng(location);
          this.mapController?.moveCamera(cameraUpdate);
        };
        try {
          geoLocationManager.on('locationChange', requestInfo, locationChange);
        } catch (err) {
          console.error(`监听位置失败, code is: ${err.code}, message is: ${err.message}`);
        }
      } else {
        console.error(`地图初始化失败, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack({ alignContent: Alignment.End }) {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback,
        })
          .width('100%')
          .height('100%');
      }.width('100%');
    }.height('100%');
  }
}
```

utils/PermissionsRequest.ets：

```ts
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { preferences } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

class PermissionsRequest {
  /**
   * 通用申请权限
   */
  async commonRequestPermissions(context: UIContext, permissions: Array<Permissions>) {
    let isPermission: boolean = await this.checkPermissions(permissions);
    if (!isPermission) {
      //一次授权
      let isDialogShown = await this.requestPermissions(context, permissions);
      if (isDialogShown !== true) {
        //二次授权
        this.requestPermissionsOnSetting(context, permissions);
      }
    }
  }

  /**
   * 校验应用是否被授权
   */
  async checkPermissions(permissions: Array<Permissions>) {
    for (let permission of permissions) {
      let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
      if (grantStatus !== abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }

  async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

    // 获取应用程序的accessTokenID
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;
      grantStatus = await atManager.checkAccessToken(tokenId, permission);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      hilog.error(0x000, 'testTag', `Failed to check access token  ${err.code}, message is ${err.message}`);
    }
    return grantStatus;
  }

  /**
   * 申请用户授权
   */
  async requestPermissions(context: UIContext, permissions: Array<Permissions>): Promise<boolean | undefined> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    try {
      let data =
        await atManager.requestPermissionsFromUser(context.getHostContext() as common.UIAbilityContext, permissions);
      hilog.info(0x000, 'testTag', 'requestPermissions1 success', JSON.stringify(data));
      return data.dialogShownResults ? data.dialogShownResults[0] : undefined; // 返回请求是否有弹窗
    } catch (e) {
      hilog.error(0x000, 'testTag', `requestPermissions1 err Code is ${e.code}, message is ${e.message}`);
      return undefined;
    }
  }

  /**
   * 2次申请用户授权
   */
  requestPermissionsOnSetting(context: UIContext, permissions: Array<Permissions>) {
    let keyPerms = JSON.stringify(permissions);
    let store = preferences.getPreferencesSync(context.getHostContext(), { name: 'permsHasOnSetting' });
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionOnSetting(context.getHostContext(), permissions)
      .then((res: Array<abilityAccessCtrl.GrantStatus>) => {
        hilog.info(0x000, 'testTag', 'requestPermissions2 success', JSON.stringify(res));
        store.putSync(keyPerms, 1);
        store.flush();
      })
      .catch((err: BusinessError) => {
        hilog.info(0x000, 'testTag', 'requestPermissions2 err', JSON.stringify(err));
      });
  }
}

export default new PermissionsRequest();
```
