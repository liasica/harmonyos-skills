---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-sidebar-alignment-substyle
title: 设置侧边栏半屏居中对齐样式
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 底部页签 > 设置侧边栏半屏居中对齐样式
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d5481b5851ec9ce1418360d20f0d1da3895b3c8dd2013e5ee9d3a2d8d68a65f8
---

## 场景介绍

从6.0.0(20)版本开始，新增支持设置侧边栏半屏居中对齐样式。

[HdsTabs (底部页签)](../harmonyos-references/ui-design-hdstabs.md)容器组件侧边栏支持半屏居中对齐布局。横向Tabs时，若没有主动设置TabBar高度，则TabBar默认高度为48vp，纵向TabBar默认宽度为96vp，barHeight设成固定值后，TabBar无法扩展底部安全区。当safeAreaPadding不设置bottom或者bottom设置为0时，可以实现扩展安全区。

* 半屏居中对齐布局

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/vKkepvlrQIyyT5rrlMN5-A/zh-cn_image_0000002736433393.png)
* 默认横向和纵向布局

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/RpOttnFtSA-6QfnBks_Qeg/zh-cn_image_0000002706834238.png)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/RlNDcsZVT2umKCyk7hDemg/zh-cn_image_0000002736313347.png)

## 约束条件

1. 依赖页签位于侧边栏，vertical设置为true。
2. 页签使用BottomTabBarStyle样式。

## 开发步骤

1. 导入相关模块。

   ```typescript
   // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
   import { HdsTabs, ExtendBarMode, HdsTabsAttribute, HdsBarMode } from '@kit.UIDesignKit';
   ```
2. 创建Hds一级容器组件，设置HdsTabs组件的barMode样式为ExtendBarMode.HALF\_SCREEN\_FIXED，所有页签总高度之和为HdsTabs组件高度的四分之一，且处在二分之一屏的居中位置。

   ```typescript
    @Entry
    @Component
    struct Index {
      @State isVertical: boolean = false;
      @State barMode: HdsBarMode = ExtendBarMode.HALF_SCREEN_FIXED

      build() {
        Column() {
          Column() {
            Row() {
              Button('verticalChange')
                .onClick(() => {
                  this.isVertical = !this.isVertical;
                })
            }
            Row() {
              Button('HALF_SCREEN_FIXED')
                .onClick(() => {
                  this.barMode = ExtendBarMode.HALF_SCREEN_FIXED
                })
              Button('Fixed')
                .onClick(() => {
                  this.barMode = BarMode.Fixed
                })
              Button('Scrollable')
                .onClick(() => {
                  this.barMode = BarMode.Scrollable
                })
            }
          }
          .margin({ top: 20 })
          .width('100%')
          .height('20%')
          HdsTabs({ barPosition: BarPosition.End }) {
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Yellow)
            }
            .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Yellow'))
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Blue)
            }
            .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))
            TabContent() {
              Column().width('100%').height('100%').backgroundColor(Color.Pink)
            }
            .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Pink'))
          }
          .vertical(this.isVertical)
          .barMode(this.barMode)
          .width('100%')
          .height('80%')
        }
        .width('100%')
        .height('100%')
      }
    }
   ```
