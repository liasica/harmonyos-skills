---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0012
title: 如何获取安全区域（状态栏、导航条、三键导航等）的高度并实现沉浸式下的避让
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 如何获取安全区域（状态栏、导航条、三键导航等）的高度并实现沉浸式下的避让
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:09+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:b3c61376d406cdef577ab9acc9cc2d61daa2b6b36a428d949cfd4b5faf4bcb98
---

**Q：如何获取状态栏和导航栏高度？**

**A**：获取系统状态栏和导航栏等规避区域。使用系统提供的 getWindowAvoidArea 获取系统规避区域。返回值中的 topRect.height 即为系统状态栏的高度，单位为 px。参考代码如下：

```ts
// MainAbility.ets
import { common, UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

/**
 * Get the height of the system status bar and navigation bar
 * @param context
 * @returns
 */
async function getWindowAvoidArea(context: common.UIAbilityContext): Promise<window.AvoidArea | null> {
  try {
    // The default area of the system includes the status bar and navigation bar
    const mainWindow = await window.getLastWindow(context);
    const avoidAreaType = window.AvoidAreaType.TYPE_SYSTEM;
    const avoidArea = mainWindow.getWindowAvoidArea(avoidAreaType);
    const avoidAreaTypeNavigationBar = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
    const avoidAreaNavigationBar = mainWindow.getWindowAvoidArea(avoidAreaTypeNavigationBar);
    const height = avoidArea.topRect.height;
    const heightNavigationBar = avoidAreaNavigationBar.bottomRect.height;
    return avoidArea
  } catch (e) {
    console.log('getWindowAvoidArea fail');
    return null
  }
}

export default class MainAbility extends UIAbility {
  // do something
  async onWindowStageCreate(windowStage: window.WindowStage) {
    getWindowAvoidArea(this.context);
    windowStage.loadContent('pages/index');
  }

  // do something
}
```

参考链接：[getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)。

**Q：如何实现三键导航的监听与避让？**

**A**：解决措施：

1. 通过[settings.registerKeyObserver](../harmonyos-references/js-apis-settings.md#settingsregisterkeyobserver11)监听三键导航的开启。

   ```ts
   settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float_navigation_info',
     settings.domainName.USER_PROPERTY, () => {
       this.adaptLayout();
     });
   ```
2. 通过[setting.getValue](../harmonyos-references/js-apis-settings.md#settingsgetvalue11)获取导航的信息。

   ```ts
   settings.getValue(this.getUIContext().getHostContext(), 'float_navigation_info',
     settings.domainName.USER_PROPERTY).then((data: string) => {
     if (data) {
       let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
       this.adaptValue = navigationInfo.getAdaptValue();
     }
   })
   ```
3. 定义三键导航信息。

   ```ts
   class NavigationButtonInfo {
     // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
     private showType: number = -1;
     // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
     private region: number[] = [0, 0, 0, 0];

     // Obtain the adaptation area and implement this function as required
     public getAdaptValue(): number {
       // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
       // this.region[2] < this.region[3] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
       if (this.showType === 0 && this.region[2] < this.region[3]) {
         return this.region[2];
       } else {
         return 0;
       }
     }
   }
   ```
4. 根据region中的布局信息进行适配。

   ```ts
   .padding({ right: this.getUIContext().px2vp(this.adaptValue) })
   ```

示例代码参考如下：

```ts
import settings from '@ohos.settings';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import window from '@ohos.window';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  @State adaptValue: number = 0;

  aboutToAppear(): void {
    this.watchNavigationButtonChange();
    window.getLastWindow(this.getUIContext().getHostContext(), ((err: BusinessError, data) => {
      data.setWindowLayoutFullScreen(true);
    }));
  }

  // Monitor the changes of three-key navigation information
  private watchNavigationButtonChange(): void {
    this.adaptLayout();

    settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float_navigation_info',
      settings.domainName.USER_PROPERTY, () => {
        this.adaptLayout();
      });
  }

  // Adapt the app layout based on the Three Key Navigation information
  private adaptLayout(): void {
    try {
      settings.getValue(this.getUIContext().getHostContext(), 'float_navigation_info',
        settings.domainName.USER_PROPERTY).then((data: string) => {
        if (data) {
          let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
          this.adaptValue = navigationInfo.getAdaptValue();
        }
      })
    } catch (e) {
      this.adaptValue = 0;
      hilog.warn(0, 'tag', 'adaptMargin err:' + e);
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Row() {
          Text(this.message)
            .id('HelloWorld')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .onClick(() => {
              this.message = 'Welcome';
            })
        }
        .backgroundColor(Color.Red)
        .height('100%')
        .width('100%')
      }
      .backgroundColor(Color.Yellow)
      .padding({ right: this.getUIContext().px2vp(this.adaptValue) })
    }
    .height('100%')
    .width('100%')
  }
}

class NavigationButtonInfo {
  // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
  private showType: number = -1;
  // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
  private region: number[] = [0, 0, 0, 0];

  // Obtain the adaptation area and implement this function as required
  public getAdaptValue(): number {
    // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
    // this.region[2] < this.region[3] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
    if (this.showType === 0 && this.region[2] < this.region[3]) {
      return this.region[2];
    } else {
      return 0;
    }
  }
}
```

导航条、状态栏、挖孔区沉浸式方案参考链接：[实现沉浸式效果](../best-practices/bpta-multi-device-window-immersive.md#section180431120426)。

**Q：如何获取屏幕顶部状态栏、底部导航栏和导航条的高度？**

A：可以使用window的[getWindowAvoidArea](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)方法获取，示例代码如下：

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetAvoidAreaHeight {
  context = this.getUIContext();

  build() {
    Column() {
      Button('GetAvoidAreaHeight')
        .onClick(() => {
          let systemAvoidAreaType = window.AvoidAreaType.TYPE_SYSTEM; // system
          let navigationIndicatorType = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // navigation
          if (this.context) {
            window.getLastWindow(this.context.getHostContext()).then((data) => {
              // Get the system default area, usually including the status bar and navigation bar
              let avoidArea1 = data.getWindowAvoidArea(systemAvoidAreaType);
              // Top status bar height
              let statusBarHeight = avoidArea1.topRect.height;
              // Bottom navigation bar height
              let bottomNavHeight = avoidArea1.bottomRect.height;
              // Get the navigation bar area
              let avoidArea2 = data.getWindowAvoidArea(navigationIndicatorType);
              // Get the height of the navigation bar area
              let indicatorHeight = avoidArea2.bottomRect.height;
              console.info(`statusBarHeight is ${statusBarHeight}`);
              console.info(`bottomNavHeight is ${bottomNavHeight}`);
              console.info(`indicatorHeight is ${indicatorHeight}`);
            }).catch((err: BusinessError) => {
              console.error(`Failed to obtain the window. Cause: ${JSON.stringify(err)}`);
            });
          }
        })
    }
  }
}
```

**Q：如何实现沉浸式页面（包括沉浸式状态栏、沉浸式导航条）？**

**A**：沉浸式页面开发分为以下两步：

1. 实现沉浸式效果：
   * 方案一：使用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法设置窗口为全屏模式。

     ```ts
     import { UIAbility } from '@kit.AbilityKit';
     import { window } from '@kit.ArkUI';
     import { BusinessError } from '@kit.BasicServicesKit';

     export default class EntryAbility extends UIAbility {
       onWindowStageCreate(windowStage: window.WindowStage) {
         // 1.Get the main window of the application.
         let windowClass: window.Window | undefined = undefined;
         windowStage.getMainWindow().then(windowClass => {
           console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(windowClass));
           // 2.Set the window to full screen to achieve immersive effects.
           windowClass.setWindowLayoutFullScreen(true).then(() => {
             console.info('Succeeded in setting the window layout to full-screen mode.');
           }).catch((e: BusinessError) => {
             console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(e));
           })
         }).catch((err: BusinessError) => {
           console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
         })
         // 3.Load the corresponding target page for the immersive window.
         windowStage.loadContent("pages/Index", (err) => {
           if (err.code) {
             console.error('Failed to load the content. Cause:' + JSON.stringify(err));
             return;
           }
           console.info('Succeeded in loading the content.');
         });
       }
     };
     ```
   * 方案二：设置组件的[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性，扩展组件的安全区域到状态栏和导航栏，从而实现沉浸式。

     ```ts
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
2. 处理避让区域与页面内容的适配问题：避让区包含状态栏中的电量、时间等系统信息，或手势交互如导航栏点击或上滑。实现应用页面沉浸式效果后，可能会与避让区产生UI元素遮挡、视觉违和或交互冲突等问题。开发者可针对不同场景选择以下方式对避让区和应用页面进行适配。
   * 使用[setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)方法或[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)方法设置状态栏和导航栏的显隐。
   * 使用[setWindowSystemBarProperties()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)方法设置状态栏和导航栏的样式。
   * 使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)方法获取避让区域的高度，据此设置应用页面内容的上下padding实现避让状态栏和导航栏。
   * 使用[getCutoutInfo()](../harmonyos-references/js-apis-display.md#getcutoutinfo9-1)方法获取挖孔区域宽高和位置信息，设置对应避让元素的margin实现挖孔区避让。
   * 对于需要动态调整的场景推荐使用getWindowAvoidArea()方法。

   参考链接：[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)。

**Q：如何设置沉浸式状态栏？**

**A**：设置沉浸式状态栏的步骤如下：

1. 获取应用主窗口。通过getMainWindow接口获取应用主窗口。
2. 实现沉浸式效果。有以下两种方式：
   * 方式一：调用setWindowSystemBarEnable接口，设置导航栏、状态栏不显示，从而达到沉浸式效果。
   * 方式二：调用setWindowLayoutFullScreen接口，设置应用主窗口为全屏布局；然后调用setWindowSystemBarProperties接口，设置导航栏、状态栏的透明度、背景/文字颜色以及高亮图标等属性，使之保持与主窗口显示协调一致，从而达到沉浸式效果。
3. 加载显示沉浸式窗口的具体内容。通过loadContent接口加载沉浸式窗口的具体内容。

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class EntryAbility extends UIAbility {
     onWindowStageCreate(windowStage: window.WindowStage) {
       // 1.Get the main window of the application.
       let windowClass: window.Window | undefined = undefined;
       windowStage.getMainWindow((err: BusinessError, data) => {
         if (err.code) {
           console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
           return;
         }
         windowClass = data;
         console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));

         // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
         let names = [];
         windowClass.setWindowSystemBarEnable(names).then(() => {
           console.info('Succeeded in setting the system bar to be visible.');
         }).catch((err: BusinessError) => {
           console.error('Failed to setting the system bar to be visible. Cause: ' + JSON.stringify(err));
         });
         // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
         let isLayoutFullScreen = true;
         windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
           console.info('Succeeded in setting the window layout to full-screen mode.');
         }).catch((err: BusinessError) => {
           console.error('Failed to setting the window layout. Cause: ' + JSON.stringify(err));
         });
         let sysBarProps: window.SystemBarProperties = {
           statusBarColor: '#ff00ff',
           navigationBarColor: '#00ff00',
           // The following two attributes are supported starting from API Version 8
           statusBarContentColor: '#ffffff',
           navigationBarContentColor: '#ffffff'
         };
         windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
           console.info('Succeeded in setting the system bar properties.');
         }).catch((err: BusinessError) => {
           console.error('Failed to setting the system bar properties. Cause: ' + JSON.stringify(err));
         });
       })
       // 3.Load the corresponding target page for the immersive window.
       windowStage.loadContent("pages/page2", (err) => {
         if (err.code) {
           console.error('Failed to load the content. Cause:' + JSON.stringify(err));
           return;
         }
         console.info('Succeeded in loading the content.');
       });
     }
   };
   ```
