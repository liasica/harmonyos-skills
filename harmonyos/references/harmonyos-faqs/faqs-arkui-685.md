---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-685
title: 多级Tabs感知当前屏幕显示的TabContent
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 多级Tabs感知当前屏幕显示的TabContent
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e08d1be0ce5ebe772f77c41da8c44a46b6df517fb959f3402466273701065e2
---

## 问题现象

目前多级Tabs嵌套后，当外层Tabs切换时，无法触发内层Tabs的onWillShow和onWillHide，无法感知内层Tabs当前是哪个TabContent显示在页面上。

例如：A是一个Tabs，里面有两个TabContent分别是B和C，C本身是一个Tabs里面有D和F两个TabContent，当从B切换至C时，无法触发D和F的onWillShow，因此无法感知目前显示在页面上的是D还是F。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/EFidD09tQE-secUKTTw-qw/zh-cn_image_0000002658914071.gif "点击放大")

## 背景知识

* [onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)：组件可见区域变化时触发该回调。当前从B切换至C时，会有D或者F的可见区域由无到有，触发该回调。
* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

## 解决方案

使用onVisibleAreaChange监控所需感知内部的TabContent。

* 一级Tabs代码实现：

  ```screen
  @Entry
  @Component
  struct FirstTabs {
    controller: TabsController = new TabsController();

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End, index: 0, controller: this.controller }) {
          TabContent() {
            SecondTabs(); // 二级Tabs
          }.tabBar({ icon: $r('app.media.startIcon'), text: '首页' });

          TabContent() {
            Column() {
              Text('消息');
            }
            .width('100%').height('100%');
          }.tabBar({ icon: $r('app.media.startIcon'), text: '消息' });

          TabContent() {
            Column() {
              Text('我的');
            }.width('100%').height('100%');
          }.tabBar({ icon: $r('app.media.startIcon'), text: '我的' });
        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barWidth(360)
        .barHeight(56)
        .width('100%')
        .height('100%')
        .backgroundColor('#F1F3F5');
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 二级Tabs代码实现：

  ```screen
  // 二级Tabs
  @Component
  struct SecondTabs {
    controller: TabsController = new TabsController();

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.controller }) {
          TabContent() {
            ThirdTabs(); // 三级Tabs
          }.tabBar('北京');

          TabContent() {
            Column() {
              Text('上海');
            }.width('100%').height('100%');
          }.tabBar('上海');

          TabContent() {
            Column() {
              Text('深圳');
            }
            .width('100%').height('100%');
          }.tabBar('深圳');
        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barWidth(360)
        .barHeight(56)
        .width('100%')
        .height('100%')
        .backgroundColor('#F1F3F5');
      }.width('100%').height('100%');
    }
  }
  ```
* 三级Tabs代码实现：

  ```screen
  // 三级Tabs
  @Component
  struct ThirdTabs {
    controller: TabsController = new TabsController();

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.controller }) {
          TabContent() {
            Column() {
              Text('天安门');
            }.width('100%').height('100%');
          }.tabBar('天安门')
          .onWillShow(() => {
            console.info('天安门：onWillShow');
          })
          .onWillHide(() => {
            console.info('天安门：onWillHide');
          })
          .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
            // 组件可见区域变化时触发该回调
            if (isExpanding && currentRatio >= 0) {
              console.info('天安门：开始显示');
            }
            if (!isExpanding && currentRatio <= 1.0) {
              console.info('天安门：开始消失');
            }
          });

          TabContent() {
            Column() {
              Text('长城');
            }.width('100%').height('100%');
          }.tabBar('长城')
          .onWillShow(() => {
            console.info('长城：onWillShow');
          })
          .onWillHide(() => {
            console.info('长城：onWillHide');
          });

          TabContent() {
            Column() {
              Text('后海');
            }.width('100%').height('100%');
          }.tabBar('后海');
        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barWidth(360)
        .barHeight(56)
        .width('100%')
        .height('100%')
        .backgroundColor('#F1F3F5');
      }.width('100%').height('100%');
    }
  }
  ```
