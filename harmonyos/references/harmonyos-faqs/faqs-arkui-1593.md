---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1593
title: 从侧边栏启动应用，切换全屏后底部未避让导航栏问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 从侧边栏启动应用，切换全屏后底部未避让导航栏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c1ed953cec9353931ba544bf1e584e807732e875ec18b27a90f836b16dc8a744
---

## 问题现象

从屏幕两侧侧滑屏幕，打开侧边栏。从侧边栏中启动应用，然后切换为全屏，底部组件被导航栏遮挡。

应用从桌面全屏启动时显示正常，底部组件未被遮挡。

## 背景知识

导航栏避让常规方法：

1. 在EntryAbility的onWindowStageCreate()中使用[window.getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)、[window.createWindow()](../harmonyos-references/arkts-apis-window-f.md#windowcreatewindow9)、[window.findWindow()](../harmonyos-references/arkts-apis-window-f.md#windowfindwindow9)中的任一方法获取到Window实例(windowClass)，以getLastWindow()为例。

   ```ts
   let windowClass: window.Window | undefined = undefined;
     window.getLastWindow(this.context, (err: BusinessError, data) => {
     windowClass = data;
   })
   ```
2. 使用[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)方法动态获取避让区域尺寸。

   ```ts
   windowClass.on('avoidAreaChange', (data: window.AvoidAreaOptions) => {
     AppStorage.setOrCreate('avoidArea', data.area);
   });
   ```
3. 据此设置应用页面内容下方的[padding](../harmonyos-references/ts-universal-attributes-size.md#padding)实现避让导航栏。

   ```ts
   @StorageLink('avoidArea') avoidArea: window.AvoidArea = {
     // 具体参数
   };

   Text('title')
     .padding({ bottom: this.avoidArea.bottomRect.height })
   ```

## 问题定位

* 分析思路：通过不同方式启动应用，现象不一致（即应用从桌面全屏打开时未遮挡，侧边栏启动后切换全屏有遮挡）。初步判断，可能是通过不同方式启动时，获取的避让区域高度不同导致出现此问题。
* 定位过程：
  1. 在EntryAbility中查看是否有使用getWindowAvoidArea()获取避让高度。
  2. 增加日志打印，查看切换全屏前后避让区域高度的变化情况。导航栏需要查看[AvoidArea](../harmonyos-references/arkts-apis-window-i.md#avoidarea7)中bottomRect的height数值。

     切换全屏前：

     ```shell
     "bottomRect":{"left":0,"top":0,"width":0,"height":0}
     ```

     由日志可知，切换全屏前避让区域的高度为0。

     切换全屏后：

     ```shell
     "bottomRect":{"left":0,"top":0,"width":0,"height":0}
     ```

     切换全屏后避让区域的高度依然为0。

## 分析结论

窗口尺寸变化后，未重新获取导航栏避让高度，导致底部被导航条遮挡。

## 修改建议

1. 在EntryAbility的onWindowStageCreate()中添加[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听，动态获取系统避让区尺寸，并存储在AppStorage中。

   示例代码如下：

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

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
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         let windowClass: window.Window | undefined = undefined;
         window.getLastWindow(this.context, (err: BusinessError, data: window.Window) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to create the system window. Cause code: ${err.code}, message: ${err.message}`);
             return;
           }
           windowClass = data;
           windowClass.setWindowLayoutFullScreen(true).then(() => {
             console.info('Succeeded in setting the window layout to full-screen mode.');
           }).catch((err: BusinessError) => {
             console.error(`Failed to set the window layout to full-screen mode. Cause code: ${err.code}, message: ${err.message}`);
           });
           try {
             // 首次启动应用时避让导航栏
             let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
             let avoidArea = windowClass.getWindowAvoidArea(type);
             AppStorage.setOrCreate('avoidArea', avoidArea);
             // 通过监听系统规避区尺寸动态避让导航栏
             windowClass.on('avoidAreaChange', (data: window.AvoidAreaOptions) => {
               AppStorage.setOrCreate('avoidArea', data.area);
             });
           } catch (exception) {
             console.error(`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
           }
         });
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     onWindowStageDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   }
   ```
2. 使用@StorageLink获取导航栏尺寸，在tabBar的padding中的bottom参数设置为导航栏高度，对导航栏进行避让。

   示例代码如下：

   ```ts
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     // 获取导航栏尺寸
     @StorageLink('avoidArea') avoidArea: window.AvoidArea = {
       visible: true,
       topRect: {
         top: 0,
         left: 0,
         width: 0,
         height: 0
       },
       bottomRect: {
         top: 0,
         left: 0,
         width: 0,
         height: 0
       },
       leftRect: {
         top: 0,
         left: 0,
         width: 0,
         height: 0
       },
       rightRect: {
         top: 0,
         left: 0,
         width: 0,
         height: 0
       }
     };

     @Builder
     tabBuilder(content: string, img: Resource) {
       Column({ space: 5 }) {
         Image(img)
           .height(20)
         Text(content)
           .fontSize(15)
       }
     }

     build() {
       Tabs({ barPosition: BarPosition.End }) {
         TabContent() {
           Text('页签1')
             .fontSize(50)
         }
         .tabBar(this.tabBuilder('页签1', $r('app.media.startIcon')))
         .backgroundColor(Color.Red)

         TabContent() {
           Text('页签2')
             .fontSize(50)
         }
         .tabBar(this.tabBuilder('页签2', $r('app.media.startIcon')))
         .backgroundColor(Color.Yellow)

         TabContent() {
           Text('页签3')
             .fontSize(50)
         }
         .tabBar(this.tabBuilder('页签3', $r('app.media.startIcon')))
         .backgroundColor(Color.Blue)

         TabContent() {
           Text('页签4')
             .fontSize(50)
         }
         .tabBar(this.tabBuilder('页签4', $r('app.media.startIcon')))
         .backgroundColor(Color.Green)
       }
       .padding({ bottom: this.avoidArea.bottomRect.height + 'px' }) // 在padding中设置，避让导航栏
     }
   }
   ```
