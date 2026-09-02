---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-44
title: 如何设置地图深色模式、浅色模式和自定义颜色
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何设置地图深色模式、浅色模式和自定义颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:868318a60092c9d3a26195a3fa26896a88c2c26bd36716b3cde76d49d342ea62
---

## 问题现象

根据不同使用场景进行深色模式、浅色模式切换是常见地图使用场景之一，如何实现Map Kit地图的深色模式、浅色模式配置？如何自定义地图的颜色？

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* [setDayNightMode](../harmonyos-references/map-map-mapcomponentcontroller.md#setdaynightmode)：设置地图的日间夜间模式，对应配模式配置值请参见[DayNightMode](../harmonyos-references/map-map-mapcomponentcontroller.md#getdaynightmode)。
* [Petal Maps Studio](https://developer.petalmaps.com/console/studio/)：管理地图样式网站。
* [setCustomMapStyle](../harmonyos-references/map-map-mapcomponentcontroller.md#setcustommapstyle)：将地图样式修改为自定义样式。

## 解决方案

* 场景一：加载地图时，默认显示为深色模式。

  在地图初始化mapOptions参数中，配置DayNightMode为mapCommon.DayNightMode.NIGHT。

  ```ts
  this.mapOptions = {
    position: {
      target: {
        latitude: 39.9,
        longitude: 116.4
      },
      zoom: 10
    },
    myLocationControlsEnabled: true,
    // 设置地图为夜间模式
    dayNightMode: mapCommon.DayNightMode.NIGHT
  };
  ```
* 场景二：切换地图为深色模式。

  配置调用setDayNightMode接口配置DayNightMode为NIGHT。

  ```ts
  Button('切换为深色模式')
    .onClick(() => {
      this.mapController?.setDayNightMode(mapCommon.DayNightMode.NIGHT);
    })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/4sle47gyTNyIE8WKlu3shg/zh-cn_image_0000002658793653.png "点击放大")
* 场景三：切换地图为浅色模式。

  配置调用setDayNightMode接口配置DayNightMode为DAY。

  ```ts
  Button('切换为浅色模式')
    .onClick(() => {
      this.mapController?.setDayNightMode(mapCommon.DayNightMode.DAY);
    })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/vLmC_wGqTqGwD2W3yuKjXA/zh-cn_image_0000002628554286.png "点击放大")
* 场景四：地图颜色跟随系统深色模式配置。

  配置调用setDayNightMode接口配置DayNightMode为AUTO。

  ```ts
  Button('切换为跟随系统深色模式')
    .onClick(() => {
      this.mapController?.setDayNightMode(mapCommon.DayNightMode.AUTO);
    });
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/U6SbQbVLQIWKuN61D4JmmQ/zh-cn_image_0000002658913609.png "点击放大")
* 场景五：配置地图为自定义颜色。
  1. 登录[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)网站，点击首页中的“Start”按钮。
  2. 点击页面右上角的“Create map”按钮，在新页面中点击预设的“Standard”、“Simple”、“Night”三种地图样式。
  3. 在地图样式配置和预览页面，左侧选择需要配置的地图元素，依次选择“Feature type”、“Element type”、“Stylers”，通过配置Stylers中的Color来自定义对应元素的颜色。
  4. 点击页面“SAVE”按钮后，参考产品文档中显示自定义地图的[开发步骤](../harmonyos-guides/map-style.md#开发步骤)进行自定义地图加载。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/MOE7kZaEROiBymMVGXyjTA/zh-cn_image_0000002628394392.png "点击放大")

  完整代码：

  ```ts
  import { MapComponent, mapCommon, map } from '@kit.MapKit';
  import { AsyncCallback } from '@kit.BasicServicesKit';
  import { display } from '@kit.ArkUI';

  @Entry
  @Component
  struct MapDayNightMode {
    private mapOptions?: mapCommon.MapOptions;
    private callback?: AsyncCallback<map.MapComponentController>;
    private mapController?: map.MapComponentController;
    @State mapHeight: number = 0;

    aboutToAppear(): void {
      let displayClass = display.getDefaultDisplaySync();
      this.mapHeight = this.getUIContext().px2vp(displayClass.height);
      // 地图初始化参数，设置地图中心点坐标及层级
      this.mapOptions = {
        position: {
          target: {
            latitude: 39.9,
            longitude: 116.4
          },
          zoom: 10
        },
        myLocationControlsEnabled: true,
        // 设置地图为夜间模式
        dayNightMode: mapCommon.DayNightMode.NIGHT
      };

      // 地图初始化的回调
      this.callback = async (err, mapController) => {
        if (!err) {
          // 获取地图的控制器类，用来操作地图
          this.mapController = mapController;

        } else {
          console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
        }
      };
    }

    // 页面每次显示时触发一次，包括路由过程、应用进入前台等场景，仅@Entry装饰的自定义组件生效
    onPageShow(): void {
      // 将地图切换到前台
      if (this.mapController) {
        this.mapController.show();
      }
    }

    // 页面每次隐藏时触发一次，包括路由过程、应用进入后台等场景，仅@Entry装饰的自定义组件生效
    onPageHide(): void {
      // 将地图切换到后台
      if (this.mapController) {
        this.mapController.hide();
      }
    }

    build() {
      Stack({ alignContent: Alignment.Bottom }) {
        Column() {
          MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
            .height(this.mapHeight);
          // .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        }.width('100%');

        Column() {
          Button('切换为深色模式')
            .onClick(() => {
              this.mapController?.setDayNightMode(mapCommon.DayNightMode.NIGHT);
            })
            .margin({ bottom: 2 });
          Button('切换为浅色模式')
            .onClick(() => {
              this.mapController?.setDayNightMode(mapCommon.DayNightMode.DAY);
            })
            .margin({ bottom: 2 });
          Button('切换为跟随系统深色模式')
            .onClick(() => {
              this.mapController?.setDayNightMode(mapCommon.DayNightMode.AUTO);
            });
        };
      }.height('100%')
      .ignoreLayoutSafeArea();
    }
  }
  ```
