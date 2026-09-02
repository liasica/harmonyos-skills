---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1491
title: 关于在Navigation的子页面使用bindSheet导致侧滑无响应的问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 关于在Navigation的子页面使用bindSheet导致侧滑无响应的问题定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7f4944052ece863b61b98ea64b801b2f8244217831c30628c9c7e8eb37b7e800
---

## 问题现象

在开发地图组件时，需要半模态的bindSheet显示一些内容，同时保持与地图的交互。

问题代码示例参考如下：

```screen
build() {
  NavDestination() {
    Stack() {
      Column() {
        MapComponent({})
          .bindSheet($$this.isShow, this.SheetBuilder(), {
            enableOutsideInteractive: true,
          })
      }
    }
  }
  .height('100%')
  .width('100%')
  .hideTitleBar(true)
  .onBackPressed(() => {
    // 自己需要做出的动作，比如弹窗拦截等，以function举例。
    this.function();
    console.info('onBackPressed')
    return true;
  })
  .onReady((context: NavDestinationContext) => {
    this.navPathStack = context.pathStack;
  })
}
```

侧滑返回时，onBackPressed函数未触发。

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)为推荐的路由导航组件，使用示例参考[使用导航控制器方法](../harmonyos-references/ts-basic-components-navigation.md#示例2使用导航控制器方法)。
* [绑定半模态页面](../harmonyos-guides/arkts-sheet-page.md)默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见。
  + [SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)参数中可以配置onWillDismiss属性，用于设置半模态页面的交互式关闭回调函数。

## 问题定位

根据对日志进行分析，侧滑时onBackPressed函数未被调用，若注册了onWillDismiss函数，则onWillDismiss函数会被触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/07IpLXXjTkyEBuCns1eyqA/zh-cn_image_0000002628765706.png "点击放大")

## 分析结论

模态弹窗层级较高，会优先响应侧滑事件。当用户执行侧滑操作时，正常关闭半模态，不论是否注册onWillDismiss函数，NavDestination页面的onBackPressed均不会被触发。若注册了onWillDismiss函数，则会触发onWillDismiss回调。

## 修改建议

将该子页面onBackPressed中的处理逻辑放到半模态的onWillDismiss函数中。

```screen
import { MapComponent } from '@kit.MapKit';

@Entry
@Component
struct BindSheetPage {
  pathStack: NavPathStack = new NavPathStack();

  @Builder
  pageMap() {
    NavDestination1();
  }

  build() {
    Navigation(this.pathStack) {
      Column() {
        Button('跳转子页')
          .onClick(() => {
            this.pathStack.pushPathByName('NavDestination1', null, true);
          });
      }.width('100%').height('100%')
      .justifyContent(FlexAlign.Center);
    }
    .width('100%')
    .height('100%')
    .navDestination(this.pageMap)
    .hideToolBar(true)
    .hideTitleBar(true);
  }
}

@Component
struct NavDestination1 {
  @State isShow: boolean = true;
  navPathStack: NavPathStack = new NavPathStack();

  @Builder
  SheetBuilder() {
    Column() {
      Button('Button');
    };
  }

  function() {
    console.info('function');
  }

  build() {
    NavDestination() {
      Column() {
        Button('打开弹窗')
          .margin({ top: 16 })
          .onClick(() => {
            this.isShow = true;
          });
        MapComponent({})
          .bindSheet($$this.isShow, this.SheetBuilder(), {
            enableOutsideInteractive: true,
            onWillDismiss: ((dismissSheetAction: DismissSheetAction) => {
              if (dismissSheetAction.reason === DismissReason.PRESS_BACK) {
                // 自己需要做出的动作，比如弹窗拦截等
                this.function();
              }
              dismissSheetAction.dismiss();
            })
          });
      }.height('100%').width('100%')
      .justifyContent(FlexAlign.Center);
    }.hideTitleBar(true)
    .onReady((context: NavDestinationContext) => {
      this.navPathStack = context.pathStack;
    });
  }
}
```
