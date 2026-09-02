---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-864
title: 图片缩放后翻转180度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 图片缩放后翻转180度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3660265c4091cfa3dc1bf8b6e2239020f986a09f687a4df237d13798b1a20ceb
---

## 问题现象

对图片进行缩放，缩放过程中图片翻转180度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/xe8Z3QtsTBq1LcMW9lI5ZQ/zh-cn_image_0000002658918111.png "点击放大")

## 背景知识

* 通过[scale](../harmonyos-references/ts-universal-attributes-transformation.md#scale)可设置组件缩放。可以分别设置X轴、Y轴、Z轴的缩放比例，默认值为1，值小于0时倒转。
* [PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)用于触发捏合手势，触发捏合手势的最少手指为2指，最大为5指，最小识别距离为5vp。

## 问题定位

1. 使用DevEco Testing查看问题组件，问题组件为Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/y3kIN5m2RaiJcJPAO1zhhw/zh-cn_image_0000002628398896.png "点击放大")
2. 查看该问题组件的设置，该组件使用PinchGesture和scale进行图片缩放，且未对缩放的值进行限定，缩放时scale中的参数值小于0。

   ```ts
   @Component
   export struct Dialog {
     pageInfos: NavPathStack = new NavPathStack();
     @State offsetX: number = 1;
     @State offsetY: number = 1;
     private lastX: number = 0;
     private lastY: number = 0;

     build() {
       NavDestination() {
         Stack() {
           Image($r('app.media.product003')) // $r('app.media.product003')需要替换为开发者需要的图片资源文件
             .width('80%')
             .objectFit(ImageFit.Contain)
             .backgroundColor(Color.White)
             .scale({ x: this.offsetX, y: this.offsetY });
         }
         .height('100%')
         .width('100%')
         .gesture(
           PinchGesture({ fingers: 2 })
             .onActionUpdate((event: GestureEvent) => {
               console.info('event.scale', event.scale);
               this.offsetX = this.lastX + (event.scale - 1) * 3;
               this.offsetY = this.lastY + (event.scale - 1) * 3;
               // 未对缩放的值进行限定，缩放时scale中的参数值可能会小于0
             })
             .onActionEnd(() => {
               // 保存缩放倍数
               this.lastX = this.offsetX;
               this.lastY = this.offsetY;
             })
         )
       }
     }
   }
   ```

## 分析结论

未对scale缩放的值进行限定，图片缩放后参数为负数，导致图片翻转180度。

## 修改建议

合理限定scale参数的值的范围，防止出现负数造成图片翻转180度。

关键部分：

```ts
PinchGesture({ fingers: 2 })
  .onActionUpdate((event: GestureEvent) => {
    console.info('event.scale', event.scale);
    this.offsetX = this.lastX + (event.scale - 1) * 3;
    this.offsetY = this.lastY + (event.scale - 1) * 3;
    // 对缩放的值进行限定，保证缩放时scale中的参数值不会小于0
    if (this.offsetY < 0.7) {
      this.offsetY = 0.7;
    }
    if (this.offsetX < 0.7) {
      this.offsetX = 0.7;
    }
  })
```

完整示例：

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct NavigationDialog {
  pageInfos: NavPathStack = new NavPathStack();

  aboutToAppear() {
    this.pageInfos.pushPath({ name: 'PageMain' }, false);
  }

  build() {
    Stack() {
      Navigation(this.pageInfos)
        .hideNavBar(true)
        .width('100%')
        .height('100%');
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}

@Builder
export function PageMainBuilder() {
  PageMain();
}

@Builder
export function DialogBuilder() {
  Dialog();
}

// 通过弹窗全屏显示图片
@Component
export struct Dialog {
  pageInfos: NavPathStack = new NavPathStack();
  @State offsetX: number = 1;
  @State offsetY: number = 1;
  private lastX: number = 0;
  private lastY: number = 0;

  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#ffffff'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  aboutToDisappear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(false);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#000000'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  build() {
    NavDestination() {
      Stack() {
        Image($r('app.media.beauty')) // $r('app.media.beauty')需要替换为开发者需要的图片资源文件
          .width('80%')
          .objectFit(ImageFit.Contain)
          .backgroundColor(Color.White)
          .scale({ x: this.offsetX, y: this.offsetY }); // 缩放图片
      }
      .height('100%')
      .width('100%')
      .gesture(
        PinchGesture({ fingers: 2 })
          .onActionUpdate((event: GestureEvent) => {
            console.info('event.scale', event.scale);
            this.offsetX = this.lastX + (event.scale - 1) * 3;
            this.offsetY = this.lastY + (event.scale - 1) * 3;
            // 对缩放的值进行限定，保证缩放时scale中的参数值不会小于0
            if (this.offsetY < 0.7) {
              this.offsetY = 0.7;
            }
            if (this.offsetX < 0.7) {
              this.offsetX = 0.7;
            }
          })
          .onActionEnd(() => {
            // 保存缩放倍数
            this.lastX = this.offsetX;
            this.lastY = this.offsetY;
          })
      )
      .onClick(() => {
        this.pageInfos.pop();
      })
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
    .hideTitleBar(true)
    .systemTransition(NavigationSystemTransitionType.NONE)
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black)
    .mode(NavDestinationMode.DIALOG)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}

@Component
export struct PageMain {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Stack() {
        Image($r('app.media.beauty')) // $r('app.media.beauty')需要替换为开发者需要的图片资源文件
          .width(200)
          .height(200)
          .objectFit(ImageFit.Contain)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'Dialog' });
          });
      }
      .width('100%')
      .height('100%');
    }
    .hideTitleBar(true)
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .height('100%')
    .width('100%')
    .mode(NavDestinationMode.STANDARD);
  }
}
```

src/main/resources/base/profile/router\_map.json:

```ts
{
  "routerMap": [
    {
      "name": "PageMain",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "PageMainBuilder"
    },
    {
      "name": "Dialog",
      "pageSourceFile": "src/main/ets/pages/Index.ets",
      "buildFunction": "DialogBuilder"
    }
  ]
}
```

src/main/module.json5中添加配置："routerMap": "$profile:router\_map"。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/dqNhb9O2TVyoBbkmzuXNOA/zh-cn_image_0000002658798171.png "点击放大")
