---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1555
title: 如何解决Scroll嵌套地图组件时的滚动冲突问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Scroll嵌套地图组件时的滚动冲突问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:59827d7389616128c6ad508709eecf84bfe9c9e3a1df05383488cbd28cc2eb21
---

## 问题现象

将地图组件，内嵌到了Scroll里面，会出现上下滑动时同时滚动的问题，如何控制滑动地图时Scroll不响应？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/iAEYrLD3RAaFgnLFq-zyog/zh-cn_image_0000002658848495.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Xu2a8_hETw2cCdf-njcxiA/zh-cn_image_0000002628609232.gif "点击放大")

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动，若子组件尺寸不超过父组件则Scroll不提供滚动能力。
* [滚动组件通用接口](../harmonyos-references/ts-container-scrollable-common.md)滚动组件通用属性和事件目前只支持List、Grid、Scroll和WaterFlow组件。提供了诸如滚动条、摩擦系数、滚动到组件最后触发的回调注册等。
* 在使用地图服务之前，需要先通过DevEco Studio或AppGallery Connect网站开通地图服务，详情可见官网指南[开发准备](../harmonyos-guides/map-config-agc.md)。

## 解决方案

Scroll中嵌套地图组件的情况，可以在MapComponent的onTouch事件中确认父组件Scroll的滑动状态，若点击到地图则Scroll不响应滑动，松开时恢复。

在onTouch回调函数中，使用switch语句根据触摸事件的类型来更新地图组件的滚动方向：

* 当触摸事件类型为TouchType.Down时，表示开始触摸，此时设置this.scrollable为ScrollDirection.None，表示停止滚动。
* 当触摸事件类型为TouchType.Up或TouchType.Cancel时，表示停止触摸或取消操作，此时设置this.scrollable为ScrollDirection.Vertical，表示允许垂直滚动。

**说明** 

地图组件在[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)后才可以正常加载地图信息。

在EntryAbility中配置沉浸式，示例代码如下：

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    window.getLastWindow(this.context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
    });

    windowStage.loadContent('pages/MapDemo', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

完整示例参考如下：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MapDemo {
  @State scrollable: ScrollDirection = ScrollDirection.Vertical;
  private mapEventManager?: map.MapEventManager;
  private TAG = 'HuaweiMapDemo';
  private mapOption?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOption = {
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
          console.info(this.TAG, `on-mapLoad`);
        };
        this.mapEventManager.on('mapLoad', callback);
      }
    };
  }

  build() {
    Stack() {
      Scroll() {
        Column() {
          // 调用MapComponent组件初始化地图
          MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
            .width('100%')
            .height('60%')
            .onTouch((event) => {
              switch (event.type) {
                case TouchType.Down:
                  this.scrollable = ScrollDirection.None;
                  break;
                case TouchType.Up:
                  this.scrollable = ScrollDirection.Vertical;
                  break;
                case TouchType.Cancel:
                  this.scrollable = ScrollDirection.Vertical;
                  break;
              }
            });
          // 用于观测是否跟随滑动
          Text('测试是否可以滑动').width('100%').height('50%').textAlign(TextAlign.Center);
        }
        .width('100%');
      }
      .scrollable(this.scrollable)
      .scrollBar(BarState.Off)
      .width('100%')
      .height('100%');
    }.height('100%');
  }
}
```
