---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/map-kit-faq-0003
title: 地图显示样式配置常见问题
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 常见问题 > 地图显示样式配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:37+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3108801aecff5809d08934a4884d9ccd043aa52ac5f85423b63da0df55264001
---

**Q：如何实现在地图上去掉地铁路线的显示？**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/Qk8jwVcrSFexGRndccWBjA/zh-cn_image_0000002773149730.png "点击放大")

**A**：地铁路线使用transit.metro-line属性控制，配置如下：

```ts
// 自定义样式参数
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: `[{\n            "mapFeature": "transit.metro-line",\n            "options": "all",\n            "visibility": false\n          }]`
        };
```

具体实现代码如下：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct CustomMapStyleDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  mapHeight: number = 0;

  aboutToAppear(): void {
    try {
      let displayClass = display.getDefaultDisplaySync();
      this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    } catch (error) {
      console.error(`getDefaultDisplaySync error. Code is ${error.code}, message is ${error.message}.`);
    }

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
        // 自定义样式参数
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: `[{\n            "mapFeature": "transit.metro-line",\n            "options": "all",\n            "visibility": false\n          }]`
        };
        // 设置自定义样式
        try {
          await this.mapController.setCustomMapStyle(param);
        } catch (error) {
          console.error(`setCustomMapStyle fail, code is：${error.code}, message is ${error.message}`);
        }
      } else {
        console.error(`init map fail, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Column() {
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
        .height(this.mapHeight)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .width('100%')
    .height('100%')
    .ignoreLayoutSafeArea();
  }
}
```

运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/968jH_x8RYO_LhlFFTeo5w/zh-cn_image_0000002802350339.png "点击放大")

**Q：地图缩放到全国的场景下，如何实现不显示各省份名称？**

**A**：配置地图自定义JSON的administrative.province为不显示。代码示例如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State mapHeight: number = 0;

  aboutToAppear(): void {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 4
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // 自定义样式参数
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: `[\n                            {\n                                "mapFeature": "administrative.province",\n                                "options": "all",\n                                "visibility": false\n                            }\n                        ]`
        };
        // 设置自定义样式
        await this.mapController.setCustomMapStyle(param);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight);
      }.width('100%');
    }.height('100%')
    .ignoreLayoutSafeArea();
  }
}
```

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/uA_jqFZxRE6y07xCiwY5Cg/zh-cn_image_0000002772990922.png "点击放大")
