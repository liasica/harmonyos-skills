---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0025
title: 状态栏颜色设置与适配常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 状态栏颜色设置与适配常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:bd39baf1b333aa6d9bdb8ebff53697e2c4b02ccf57bc6bd825ddecc6dcc4314f
---

**Q：在应用开发过程中，如何通过调整状态栏、导航栏的颜色及文字颜色，以适应不同界面的设计需求？**

**A**：若想设置状态栏、导航栏颜色，相关的属性有如下四个：statusBarColor、statusBarContentColor、navigationBarColor、navigationBarContentColor。下文将以设置状态栏背景颜色与状态栏字体颜色举例说明用法。

方案一：直接在UI组件中调用setWindowSystemBarProperties方法设置状态栏颜色和状态栏字体颜色。

```ts
import window from '@ohos.window';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Solution1 {
  build() {
    RelativeContainer() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext()!, (err: BusinessError, windowClass) => {
            if (err.code) {
              console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
              return;
            }
            let systemBarProperties: window.SystemBarProperties = {
              statusBarColor: '#F1F3F5', // 状态栏背景色
              statusBarContentColor: '#0A59F7' // 状态栏文字颜色
            };
            windowClass.setWindowSystemBarProperties(systemBarProperties).then(() => {
              console.info('Succeeded in setting the system bar properties.');
            }).catch((err: BusinessError) => {
              console.error(`Failed to set systemBar properties. Cause code: ${err.code}, message: ${err.message}`);
            });
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

方案二：封装修改状态栏颜色的工具类StatusBarManager，在UI组件中调用工具类改变状态栏颜色。

1. 通过传入Context，进而能够获取到Window实例来执行setWindowSystemBarProperties方法。
2. 传入包含状态栏属性的JSON字符串，工具类解析字符串后使用。

   ```ts
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   export class StatusBarManager {
     static handleStatusBarAction(context: common.BaseContext, p: string): void {
       try {
         interface ParamsType {
           action: string;
           args: Array<string>;
         }

         // 解析入参，用于设置状态栏的颜色
         const params: ParamsType = JSON.parse(p);
         const action: string = params.action;
         const args: Array<string> = params.args;
         let statusBarColor = '#FFFFFF'; // 默认白色
         let statusBarContentColor = '#000000'; // 默认黑色
         if (action === 'backgroundColorByHexString') {
           statusBarColor = args[0] || statusBarColor;
           statusBarContentColor = args[1] || statusBarContentColor;
         }
         // 创建SystemBarProperties对象
         const systemBarProperties: window.SystemBarProperties = {
           statusBarColor: statusBarColor,
           statusBarContentColor: statusBarContentColor,
         };
         StatusBarManager.setStatusBarBgColor(context, systemBarProperties);
       } catch (error) {
         console.error('Failed to parse or handle status bar action. Error:');
       }
     }

     private static setStatusBarBgColor(context: common.BaseContext,
       systemBarProperties: window.SystemBarProperties): void {
       window.getLastWindow(context).then((windowClass: window.Window) => {
         try {
           windowClass.setWindowSystemBarProperties(systemBarProperties);
           console.info('Status bar color updated successfully.');
         } catch (exception) {
           console.error(`Failed to set the system bar properties. Cause: ${JSON.stringify(exception)}`);
         }
       }).catch((error: BusinessError) => {
         console.error(`Failed to get last window. Error: ${JSON.stringify(error)}`);
       });
     }
   }
   ```

   在UI组件中调用：

   ```ts
   import { StatusBarManager } from './StatusBarManager';
   import { JSON } from '@kit.ArkTS';

   @Entry
   @Component
   struct Solution2 {
     build() {
       RelativeContainer() {
         Text('Hello World')
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             // 调用封装的StatusBarManager类设置状态栏颜色
             StatusBarManager.handleStatusBarAction(this.getUIContext().getHostContext()!,
               JSON.stringify({ 'action': 'backgroundColorByHexString', 'args': ['#F1F3F5', '#0A59F7'] }));
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

需要注意的是：设置状态栏与导航栏颜色的重要前提是获取Context，getLastWindow方法会在获取Context后确定操作的对象是哪一个窗口实例。在封装成工具类时，可以在类中获取Context，也可以将UI组件中获取的Context作为参数传给类中方法，为保证Context的一致性和准确性，更推荐在UI组件中获取Context并传给类中方法。

两种方案的实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/FyxUuG97Qaiw32fEKWWPvw/zh-cn_image_0000002802039479.png "点击放大")

若是想要设置导航栏，则需要在SystemBarProperties中给navigationBarColor、navigationBarContentColor赋值。

**Q：为什么设置了navigationBarColor，但是导航栏颜色没生效？**

**A**：navigationBarColor是设置导航栏的背景颜色，也就是传统的三键导航，如果设备没有该底部导航栏，则设置不会生效。

**Q：如何设置底部导航条区域背景色和导航条的颜色？**

**A**：目前无相关API，即底部导航条颜色不可设置，底部导航条区域背景色设置可以通过扩展布局，全屏显示，不隐藏避让区实现，去掉顶部和底部的padding设置，即不避让状态栏和导航条，UI元素就会发生重叠。状态栏和导航区域默认是透明的，透传的是应用界面的背景色。

参考文档：[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。

**Q：如何只针对某一个页面设置状态栏颜色？**

**A**：可以在该页面的aboutToAppear设置状态栏颜色，并在设置前使用getWindowSystemBarProperties获取状态栏颜色，在aboutToDisappear中设置为保存的状态栏颜色，以此达到针对一个页面修改颜色的效果。

**Q：设置了沉浸式，如何修改导航栏颜色？**

**A**：可以在最外层嵌套一层容器，使用padding空出底部位置，设置背景色即可。

**Q：PC端应用如何设置顶部状态栏的背景色？**

**A**：[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)该接口在2in1(PC)设备上调用不生效，暂不支持在PC端应用设置顶部状态栏的背景色。

**Q：深色模式后状态栏看不到状态信息（时间、电量等）？**

**A**：需要做页面[状态栏深色模式的适配](https://developer.huawei.com/consumer/cn/forum/topic/0208153170088597816?fid=0109140870620153026)。

**Q：如何实现状态栏透明背景颜色？**

**A**：在需要改变的页面直接调用setWindowSystemBarProperties方法，如果要设置状态栏整体透明度，可以使用RGBA对状态栏每部分设置相同透明度实现。

**Q：在深色模式下，状态栏颜色与背景色对比度不足，导致内容难以辨认。**

**A**：解决措施如下：

1. base/element/color.json中定义浅色模式的状态栏背景色。
2. 在dark/element/color.json中定义深色模式的状态栏背景色。
3. 监听深浅色模式的切换。
4. 监听到颜色切换后，手动使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)设置状态栏字体颜色。

关于深色模式适配，请参考[深色模式适配](../best-practices/bpta-dark-mode-adaptation.md#section128661451172714)。

参考代码如下：

1. 定义深浅色模式下的颜色资源。

   ```json
   // resources/dark/element/color.json
   {
     "color": [
       {
         "name": "status_bar",
         "value": "#000000"
       }
     ]
   }
   ```

   ```json
   // resources/base/element/color.json
   {
     "color": [
       {
         "name": "status_bar",
         "value": "#FFFFFF"
       }
     ]
   }
   ```
2. 缓存窗口对象和当前颜色模式，便于后续使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)接口设置状态栏属性。

   ```ts
   // EntryAbility.ets

   onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     // Cache the color mode of the current device
     AppStorage.setOrCreate('currentColorMode', this.context.config.colorMode);
   }

   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main application window
       // 1. Set the window to full screen
       let isLayoutFullScreen = true;
       windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
       // 2. Cache window object
       AppStorage.setOrCreate('windowClass', windowClass);
     });
   }
   ```
3. 颜色模式变更时，更新缓存中的颜色模式。

   ```screen
   // EntryAbility.ets

   // 监听系统配置变更
   onConfigurationUpdate(newConfig: Configuration): void {
     let newColorMode = newConfig.colorMode;
     let currentColorMode = AppStorage.get<ConfigurationConstant.ColorMode>('currentColorMode');
     if (newColorMode === currentColorMode) {
       return;
     }
     // 更新缓存中的颜色模式
     AppStorage.setOrCreate('currentColorMode', newConfig.colorMode);
   }
   ```
4. 页面监听颜色模式，模式变更时更新状态栏字体颜色。

   ```ts
   import { window } from '@kit.ArkUI';
   import { ConfigurationConstant } from '@kit.AbilityKit';

   @Entry
   @Component
   struct SysDarkMode {
     @State message: string = 'page layout';
     @StorageProp('currentColorMode') @Watch('onColorModeChange') currentColorMode: number =
       ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT;

     aboutToAppear(): void {
       this.onColorModeChange();
     }

     onColorModeChange(): void {
       // Get the current application window
       let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;

       if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT) {
         // Currently in light color mode
         //Set the font to black
         windowClass.setWindowSystemBarProperties({
           // Status bar text color
           statusBarContentColor: '#000000'
         });
       } else if (this.currentColorMode === ConfigurationConstant.ColorMode.COLOR_MODE_DARK) {
         // Currently in dark mode
         //Set the font to white
         windowClass.setWindowSystemBarProperties({
           // Status bar text color
           statusBarContentColor: '#FFFFFF'
         });
       } else {
         console.warn("Unsupported color mode")
       }
     }

     build() {
       Column() {
         Row()
           .width('100%')
           .height(100)
           .backgroundColor($r('app.color.status_bar'))
         // page layout
         Text(this.message)
           .fontSize(50)
           .fontColor(Color.Red)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: {
               anchor: '__container__',
               align: VerticalAlign.Center
             },
             middle: {
               anchor: '__container__',
               align: HorizontalAlign.Center
             }
           })
           .layoutWeight(1)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

**Q：如何修改状态栏字体颜色？**

**A**：[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)可以用于设置窗口内导航栏和状态栏的属性，包括状态栏背景颜色和状态栏文字颜色等。

在EntryAbility.ets的onWindowStageCreate方法中设置WindowStage的AppStorage。参考代码如下：

```ts
AppStorage.setOrCreate('windowStage',windowStage);
```

通过setWindowSystemBarProperties可以设置状态栏样式。

```screen
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
struct ChangeStatusBar {
  windowStage: window.WindowStage = AppStorage.get("windowStage") as window.WindowStage;
  // How to get the main window
  mainWin: window.Window = this.windowStage.getMainWindowSync();

  aboutToAppear(): void {
    let sysBarProps: window.SystemBarProperties = {
      statusBarColor: '#000000',
      statusBarContentColor: '#ffffff'
    };
    this.mainWin.setWindowSystemBarProperties(sysBarProps).then(() => {
      console.info('[StaticUtils] Succeeded in setting the system bar properties.');
    }).catch((err: BusinessError) => {
      console.error(`setting system bar properties failed, code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text('Demo of modifying the status bar')
          .fontSize(25)
          .margin(20)
          .fontColor(0x3399FF)
      }.width('100%')
    }.height('100%').backgroundColor(Color.White)
  }
}
```

**Q：为了避免状态栏颜色与背景重合，如何根据状态栏和内容区域的颜色进行沉浸式效果适配？**

**A**：方式一：设置窗口的背景色来实现沉浸式效果，参考代码如下：

```screen
// EntryAbility.ets

onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.loadContent('pages/Example', (err, data) => {
    if (err?.code) {
      return;
    }
    // Set the full window color to match the color of the application elements
    windowStage.getMainWindowSync().setWindowBackgroundColor('#008000');
  });
}
```

方式二：对顶部组件使用[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性扩展安全区域属性，实现状态栏沉浸。

```screen
@Entry
@Component
struct Example {
  build() {
    Column() {
      Row() {
        Text('Top Row')
          .fontSize(40)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .backgroundColor('#F08080')
      // Set the top drawing to extend to the status bar
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

      Row() {
        Text('ROW2')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW3')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW4')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('ROW5')
          .fontSize(40)
      }
      .backgroundColor(Color.Orange)
      .padding(20)

      Row() {
        Text('Bottom Row')
          .fontSize(40)
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .backgroundColor(Color.Orange)
      // Set the bottom drawing to extend to the navigation bar
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .backgroundColor('#008000')
    .justifyContent(FlexAlign.SpaceBetween)
  }
}
```

方式三：手动设置状态栏的颜色：

实现步骤：

1. 获取并缓存窗口对象，可参考：[Interface (Window)](../harmonyos-references/arkts-apis-window-window.md)。
2. 在打开目标页面时，使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)接口设置状态栏属性。

   获取窗口对象并缓存。

   ```ts
   // EntryAbility.ets

   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main window of the application
       // 1. Set the window to full screen
       let isLayoutFullScreen = true;
       windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
       // 2. Cache window object
       AppStorage.setOrCreate('windowClass', windowClass);
     });
   }
   ```

   打开页面时，设置状态栏属性，选择所需的沉浸式颜色。

   ```ts
   import { window } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct CommonTopBar {
     @State message: string = 'Hello World';

     aboutToAppear() {
       // Get the current application window
       let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;
       try {
         // Set the background color of the status bar and navigation bar to the same color as the application window
         windowClass.setWindowSystemBarProperties({
           // The color attribute is ARGB, set the dust cover to 0% to make it transparent
           // Navigation bar color
           navigationBarColor: '#fd121de5',
           // Status bar color
           statusBarColor: '#ff0ad9c2',
           // Status bar text color
           statusBarContentColor: '#fff1e50a'
         })
       } catch (error) {
         let err = error as BusinessError;
         hilog.error(0x0000, 'CommonTopBar', `error code:${err.code},message:${err.message}`);
       }
     }

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('PageHelloWorld')
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: {
               anchor: '__container__',
               align: VerticalAlign.Center
             },
             middle: {
               anchor: '__container__',
               align: HorizontalAlign.Center
             }
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
