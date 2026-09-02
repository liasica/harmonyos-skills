---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-multi-device-deployment-7
title: 如何实现横屏页面返回切换竖屏/单页面横竖屏
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 常见问题 > 如何实现横屏页面返回切换竖屏/单页面横竖屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:29fb94e8058585e3d7a59e2451f24a6c277e2f1de2f35d726d2726cf4ce17855
---

## 问题现象

在视频播放、股票K线分析、AR模型预览等应用中，详情页通常采用竖屏布局以适配常规操作。为提供更沉浸、更专业的交互体验，目前提供了以下三种场景：

* 用户可通过界面上的全屏按钮一键切换至横屏全屏状态。
* 在沉浸式模式下实现单页面内横竖屏切换。
* 区分手机和PAD，根据实际设备类型限制页面以竖屏或者横屏展示。

横屏模式下，内容展示区域更大、细节更清晰，尤其适合视频全屏播放、K线图表横向展开以及AR模型的全景预览，从而显著提升视觉体验与操作效率。

## 背景知识

* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)：在创建自定义组件的新实例后，在其build()函数执行前调用。
* [aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)：在自定义组件析构销毁时执行。不允许在aboutToDisappear函数中改变状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定。
* [window.getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)：获取当前应用内层级最高的子窗口，使用callback异步回调。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置窗口的显示方向属性，使用callback异步回调。
* [AppStorage](../harmonyos-references/ts-state-management.md#appstorage)：AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。
* [getMainWindowSync](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)：获取该WindowStage实例下的主窗口，该接口为同步调用。
* [display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)：返回应用所在屏幕的Display对象。若应用内多个Ability在不同屏幕，返回主屏的Display对象，若应用内多个Ability在同一屏幕，返回所在屏幕的Display对象。
* [deviceInfo.getDeviceInfo](../harmonyos-references/js-apis-enterprise-deviceinfo.md#deviceinfogetdeviceinfo)：获取设备信息。
* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置应用主窗口或应用子窗口的布局是否为沉浸式布局，使用Promise异步回调。其余窗口调用不生效也不报错。
* [Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)：窗口显示方向类型枚举。

## 解决方案

场景一：从列表进入视频播放页面，提供一个按钮通过setPreferredOrientation(window.Orientation.LANDSCAPE)设置横屏来控制屏幕的显示方向为横屏，点击后进入横屏，退出页面后通过setPreferredOrientation(window.Orientation.PORTRAIT)恢复到竖屏。

1. 新建Index.ets文件模拟视频列表，代码如下：

   ```ts
   @Entry
   @Component
   struct MainPage {
     // 单页面设置横屏（页面之间设置横竖屏切换）
     private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

     build() {
       Column() {
         List({ space: 20, initialIndex: 0 }) {
           ForEach(this.arr, (item: number) => {
             ListItem() {
               Text('' + item)
                 .width('100%')
                 .height(100)
                 .fontSize(16)
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .backgroundColor(0xFFFFFF);
             }
             .onClick(() => {
               this.getUIContext().getRouter().pushUrl({ url: 'pages/OrientationTest' });
             });
           }, (item: number) => item.toString());
         }
         .listDirection(Axis.Vertical) // 排列方向
         .scrollBar(BarState.Off)
         .friction(0.6)
         .divider({
           strokeWidth: 2,
           color: 0xFFFFFF,
           startMargin: 20,
           endMargin: 20
         }) // 每行之间的分界线
         .edgeEffect(EdgeEffect.Spring); // 边缘效果设置为Spring
       }
       .justifyContent(FlexAlign.Center)
       .width('100%')
       .backgroundColor('#f1f3f5')
       .height('100%');
     }
   }
   ```
2. 新建OrientationTest.ets文件，点击按钮后通过setPreferredOrientation(window.Orientation.LANDSCAPE)设置横屏，在aboutToDisappear回调内通过setPreferredOrientation(window.Orientation.PORTRAIT)在退出页面后重置方向，设置为竖屏，代码如下：

   ```ts
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct OrientationTest {
     aboutToDisappear(): void {
       window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
         // 退出页面后重置方向，设置为竖屏
         win.setPreferredOrientation(window.Orientation.PORTRAIT);
       });
     }

     build() {
       Column() {
         Button('退出播放页面')
           .backgroundColor('#0a59f7')
           .onClick(() => {
             this.getUIContext().getRouter().back();
           })
           .margin({ top: 50 });
         // 点击按钮后通过setPreferredOrientation设置页面横屏
         Button('横屏播放')
           .backgroundColor('#0a59f7')
           .margin({ top: 50 })
           .onClick(() => {
             window.getLastWindow(this.getUIContext().getHostContext()).then((win: window.Window) => {
               win.setPreferredOrientation(window.Orientation.LANDSCAPE);
             });
           });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

   效果如下：

   | 播放页面竖屏 | 播放页面横屏 |
   | --- | --- |
   |  |  |

场景二：在沉浸式模式下实现单页面内横竖屏切换，在aboutToAppear回调内通过setWindowLayoutFullScreen(true)设置页面为沉浸式并通过布尔值的变化，通过以下三元表达式win.setPreferredOrientation(this.isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT)来实现横竖屏的切换。

1. 在aboutToAppear回调内通过setWindowLayoutFullScreen(true)设置页面为沉浸式，代码如下：

   ```ts
   // 沉浸式模式下实现页面内横竖屏切换
     aboutToAppear(): void {
       // 开启沉浸式
       window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
         win.setWindowLayoutFullScreen(true);
       });
     }
   ```
2. 自定义onFullChange方法，通过setPreferredOrientation设置页面的横竖屏，代码如下：

   ```ts
   onFullChange() {
       window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
         this.isLandscape = !this.isLandscape;
         win.setPreferredOrientation(this.isLandscape ? window.Orientation.LANDSCAPE :
           window.Orientation.PORTRAIT);
       });
   ```

完整代码如下：

```ts
import { window } from '@kit.ArkUI';
@Entry
@Component
export struct Page {
  @State isLandscape: boolean = false;
  // 沉浸式模式下实现页面内横竖屏切换
  aboutToAppear(): void {
    // 开启沉浸式
    window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
      win.setWindowLayoutFullScreen(true);
    });
  }
  build() {
    Stack() {
      Stack() {
        // 实际使用时替换为真实的图片
        Image($r('app.media.img'))
          .width('100%')
          .aspectRatio(16 / 9)
          .constraintSize({
            maxWidth: '100%',
            maxHeight: '100%'
          });
        if (this.isLandscape) {
          Row({ space: 10 }) {
            Blank()
            Image($r('app.media.arrow_down_right_and_arrow_up_left'))
              .width(24)
              .height(24)
              .onClick(() => {
                this.onFullChange();
              });
          }
          .width('100%')
          .alignItems(VerticalAlign.Center)
          .padding({
            left: 44, right: 44, bottom: 20
          });
        } else {
          Text('全屏切换')
            .borderWidth(1)
            .borderRadius('50%')
            .borderColor(Color.White)
            .fontColor(Color.White)
            .fontSize(14)
            .padding({
              left: 10,
              right: 10,
              top: 5,
              bottom: 5
            })
            .onClick(() => {
              this.onFullChange();
            })
            .offset({
              y: 50
            });
        }
      }
      .alignContent(Alignment.Bottom);
    }
    .backgroundColor('#000')
    .width('100%')
    .height('100%');
  }
  onFullChange() {
    window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
      this.isLandscape = !this.isLandscape;
      win.setPreferredOrientation(this.isLandscape ? window.Orientation.LANDSCAPE :
        window.Orientation.PORTRAIT);
    });
  }
}
```

效果如下：

| 播放页面竖屏 | 播放页面横屏 |
| --- | --- |
|  |  |

场景三：设置指定页面在手机上只允许竖屏显示，在PAD上只允许横屏显示。

1. 在EntryAbility.ets中通过AppStorage保存WindowStage，代码如下：

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         AppStorage.setOrCreate('windowStage', windowStage);
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
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
2. 在aboutToAppear回调内通过getMainWindow获取当前主窗口，并通过deviceInfo.deviceType获取当前设备类型，并根据设备类型指定当前的屏幕方向，代码如下：

   ```ts
   import { window } from '@kit.ArkUI';
   import { deviceInfo } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct PadAndPhonePage {
     @State message: string = 'Hello World';

     // 在手机上竖屏显示，在pad上横屏显示
     aboutToAppear(): void {
       window.getLastWindow(this.getUIContext().getHostContext()).then(win => {
         win.setWindowLayoutFullScreen(true);
       });
       let windowStage = AppStorage.get('windowStage') as window.WindowStage;
       let windowClass: window.Window | undefined = undefined;
       windowStage.getMainWindow((err: BusinessError, data) => {
         const errCode: number = err.code;
         if (errCode) {
           console.error(`Failed to obtain the main window. Cause code: ${err.code}, message: ${err.message}`);
           return;
         }
         windowClass = data;
         // 获取设备类型
         let deviceTypeInfo: string = deviceInfo.deviceType;
         console.info(`the value of the deviceType is:${deviceTypeInfo}`);
         let orientation = window.Orientation.AUTO_ROTATION;
         // 判断设备是手机or平板，来设置窗口显示方向
         if (deviceTypeInfo == 'phone') {
           orientation = window.Orientation.PORTRAIT;
           this.message = '当前的设备是:phone';
         } else if (deviceTypeInfo == 'tablet') {
           orientation = window.Orientation.LANDSCAPE;
           this.message = '当前的设备是:tablet';
         }
         try {
           windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
             const errCode: number = err.code;
             if (errCode) {
               console.error(`Failed to set window orientation. Cause code: ${err.code}, message: ${err.message}`);
               return;
             }
             console.info('Succeeded in setting window orientation.');
           });
         } catch (exception) {
           console.error(`Failed to set window orientation. Cause code: ${exception.code}, message: ${exception.message}`);
         }
       });
     }

     build() {
       RelativeContainer() {
         Text(this.message)
           .fontSize(25)
           .fontColor(Color.White)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });
       }
       // 实际使用时替换为真实的图片
       .backgroundImage($r('app.media.img'))
       .height('100%')
       .width('100%');
     }
   }
   ```

   效果如下：

   | 手机上竖屏 | 平板上横屏 |
   | --- | --- |
   |  |  |

## 常见FAQ

Q：横竖屏切换的时候，底部安全区域怎么适配。

A：可以设置[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性，动态改变edges的值，在横屏时配置为[SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]，设置当前页面横屏状态。

Q：应用在前台设置LANDSCAPE后，再将window锁定状态为LOCKED。应用进入后台后，再返回前台，设置的LOCKED状态被取消且变成竖屏。

A：LOCKED旋转策略，会跟随当前屏幕朝向启动。应用退出到后台后，桌面会旋转到竖屏，再次打开应用，应用也会跟随桌面旋转到竖屏，这是规格。维持原来的旋转策略(LANDSCAPE)就可以，不需要更改成LOCKED。

Q：横竖屏旋转适配Orientation设置UNSPECIFIED和AUTO\_ROTATION有什么区别。

A:1.UNSPECIFIED由系统判定，在桌面时是否可旋转，所以手机上不会发生旋转，PAD会旋转。2.AUTO\_ROTATION是跟随传感器自动旋转，手机和PAD上都会旋转。

Q：在平板上调用[getPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#getpreferredorientation12)获取窗口显示方向返回0，如何获取当前屏幕实际的横竖屏状态？

A：返回值0对应window.Orientation.UNSPECIFIED，表示未定义方向模式，由系统判定。若需获取当前屏幕实际的横竖屏状态，可通过[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)().orientation属性来判断屏幕当前所处的横竖屏状态。
