---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/immersive-window-feature
title: 窗口沉浸式
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口基础能力 > 窗口沉浸式
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:22+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:8862b4b98f857092aa88077664002040227c375a788c39576908109dbc7770a7
---

## 场景介绍

窗口沉浸式指通过优化应用界面，使内容成为视觉焦点，以最大限度排除无关元素的干扰，实现沉浸式效果。其实现需针对不同设备的屏幕特性、交互逻辑及系统规范进行差异化适配。

## 沉浸式效果

通常情况下，影音类、游戏类、办公类等应用为了尽可能全屏显示，减少其他无关界面元素的干扰，会主动调整系统界面元素的显隐状态或样式来聚焦更多应用界面内容。

开发应用沉浸式效果主要通过调整状态栏、应用界面和底部导航区域的显示效果来减少状态栏和导航区域等系统界面的突兀感，从而使用户获得最佳的UI体验。

开发者可以通过三种方式实现应用界面内的沉浸式效果：

* [隐藏系统界面元素](immersive-window-feature.md#隐藏系统界面元素实现沉浸式效果)，使应用内容布满整个窗口显示区域。
* 设置窗口为[沉浸式布局](immersive-window-feature.md#沉浸式布局)，将应用内容拓展到整个窗口显示区域，通过[布局避让](immersive-window-feature.md#布局避让)避免重要组件与系统界面元素重叠。
* 使用组件[安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)能力，将部分组件拓展到安全区域外部。该方案下，界面元素仅做绘制延伸，无法单独布局到状态栏和导航区域，针对需要单独布局UI元素到系统界面元素区域的场景，建议使用上述两种方案。

### 界面元素构成

典型全屏应用窗口包括系统界面元素和应用界面。其中系统界面元素包含状态栏和导航区域，通常在[沉浸式布局](immersive-window-feature.md#沉浸式布局)下称为避让区域，避让区域之外的区域称为安全区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/KCU_yHZcTvKJ86Ds4CNomg/zh-cn_image_0000002736433191.png)

### 沉浸式布局

沉浸式布局是一种让应用可布局区域拓展至整个窗口显示区域的状态。

* 非沉浸式布局下，应用界面内容默认会避开系统UI的显示区域，包括状态栏、导航区域。
* 沉浸式布局下，应用内的可用布局区域延伸到整个窗口大小，此时应用界面的布局内容可与系统UI界面重叠显示，但系统界面元素层级始终高于应用界面内容。

  可以通过[isImmersiveLayout()](../harmonyos-references/arkts-apis-window-window.md#isimmersivelayout20)接口判断当前窗口是否为沉浸式布局。

多设备场景下不同窗口形态的沉浸式开发与实现可以参考[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)最佳实践。

**说明** 

沉浸式布局是窗口内元素的布局方式，进入或退出沉浸式布局不会改变窗口尺寸和位置，仅会影响应用界面内元素的布局。

[自由窗口](freeform-window-overview.md#自由窗口)状态和非[自由窗口](freeform-window-overview.md#自由窗口)状态下实现沉浸式布局的方式不同。

* 非自由窗口状态下，可通过使用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)或[setImmersiveModeEnabledState()](../harmonyos-references/arkts-apis-window-window.md#setimmersivemodeenabledstate12)接口设置当前窗口进入/退出窗口沉浸式布局。

  **说明** 

  非自由窗口状态下，除应用子窗外的其他类型窗口在创建时默认为非沉浸式布局，子窗口创建后默认为沉浸式布局。

  ```typescript
  import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    // ...

    onWindowStageCreate(windowStage: window.WindowStage): void {
      windowStage.loadContent('pages/Index', async (err) => {
        if (err.code) {
          return;
        }

        try {
          const mainWindow: window.Window = windowStage.getMainWindowSync();  // 获取应用主窗口
          await mainWindow.setWindowLayoutFullScreen(true); // 进入窗口沉浸式布局（非自由窗口状态）
          mainWindow.setWindowDecorVisible(false);  // 隐藏窗口标题栏，进入沉浸式布局（自由窗口状态）
        } catch (e) {
          console.error(`Failed to set status bar to invisible`);
        }
      });
    }
  // ...
  }
  ```

  | 非自由窗口的非沉浸式布局示意 | 非自由窗口的沉浸式布局示意 |
  | --- | --- |
  |  |  |
* 自由窗口状态下，可通过[setWindowDecorVisible()](../harmonyos-references/arkts-apis-window-window.md#setwindowdecorvisible11)接口控制窗口标题栏显隐，当标题栏隐藏时，窗口处于沉浸式布局。

  | 自由窗口的非沉浸式布局示意 | 自由窗口的沉浸式布局示意 |
  | --- | --- |
  |  |  |

### 布局避让

沉浸式布局状态下，窗口可布局区域与系统界面元素的显示区域可以重叠，此时为了避免状态栏、导航区域等系统界面元素交叉导致应用界面显示被遮挡，需要在组件布局时做额外的布局避让。

窗口与系统界面元素显示的交叉区域称为**避让区域**，应用内通过布局避让，将关键显示组件避开避让区域显示，从而达到沉浸式效果。

系统支持的避让区域类型通过枚举[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)表示。

### 避让区域AvoidArea的计算方式

避让区域[AvoidArea](../harmonyos-references/arkts-apis-window-i.md#avoidarea7)的数据结构如下所示：

```txt
interface AvoidArea {
  visible: boolean;
  leftRect: Rect;
  topRect: Rect;
  rightRect: Rect;
  bottomRect: Rect;
}

interface Rect {
  left: number;
  top: number;
  width: number;
  height: number;
}
```

* 其中包含四组Rect信息，表示此类型的避让区域在相对于窗口中心点的方向和具体矩形区域位置。
* visible属性不代表任何系统UI的可见性，没有实际含义，**请避免使用此属性**。

在避让区域的计算中，将窗口按照对角线分为四个三角形区域，当对应系统界面元素的位置（矩形中心点）落于某个方向上的三角形区域时，提供的避让区域将在对应的Rect中。如下图所示整个矩形为窗口区域，以窗口左上角为原点，水平向右为X轴正方向，垂直向下为Y轴正方向，窗口矩形的两条对角线将整个矩形划分为四个方向上的Rect区域，用以表示避让区域相对窗口的几何位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/nFmsDgTpQSCmePG5Cdnnwg/zh-cn_image_0000002706834038.png)

其中每个Rect为(X, Y, Width, Height)构成的四元组，表示以**窗口左上角为原点**的唯一矩形区域。

如下图，挖孔区域表示为 **[topRect, (x1, y1, w1, h1)]** ，底部导航区域表示为 **[bottomRect, (0, H-h2, W, h2)]** 。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/CleQ0nU4QtKzTnAGO4NSiw/zh-cn_image_0000002736313147.png)

## 隐藏系统界面元素实现沉浸式效果

可通过隐藏系统界面元素实现沉浸式效果，适用于游戏、电影等应用场景。例如，在相机大图页面隐藏状态栏以获得沉浸式的图片查看效果。

**说明** 

[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)、[setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)等控制系统界面元素显示的接口仅非[自由窗口](freeform-window-overview.md#自由窗口)状态下的主窗口支持调用，在[辅助窗口](window-type-overview.md#辅助窗口)中调用或[自由窗口](freeform-window-overview.md#自由窗口)状态下调用不生效。在主窗口非全屏/非最大化模式时调用不会立即生效，应用在进入全屏/最大化模式后配置生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/7LKunt8gTeyNvUmQ8UMLeg/zh-cn_image_0000002706674104.png)

1. 调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口进入沉浸式布局。
2. 调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)隐藏状态栏。

```typescript
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
    // ...

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', async (err) => {
      if (err.code) {
        return;
      }

      try {
        const mainWindow: window.Window = windowStage.getMainWindowSync();  // 获取应用主窗口
        await mainWindow.setWindowLayoutFullScreen(true);  // 设置窗口进入沉浸式
        await mainWindow.setSpecificSystemBarEnabled('status', false);  // 设置状态栏隐藏
      } catch (e) {
        console.error(`Failed to set status bar to invisible`);
      }
    });
  }
  // ...
```

## 适配沉浸式布局实现沉浸式效果

**说明** 

全局悬浮窗、模态窗口和系统窗口本身不具备获取避让区域的能力，如果需要在这些窗口中适配布局避让，需要使用[setSystemAvoidAreaEnabled()](../harmonyos-references/arkts-apis-window-window.md#setsystemavoidareaenabled18)接口使能避让区域能力后再进行布局避让。

1. 调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口进入沉浸式布局。
2. 获取并监听窗口避让区域，在避让区域更新时同时更新应用内布局。

   此处以获取并监听状态栏、底部导航区域、挖孔区为例。

   * 可以通过使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口获取当前窗口避让区域。使用[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)接口监听避让区域的动态变化。

     常见的触发避让区域回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；多折叠设备在屏幕折叠态和展开态之间的切换；应用窗口在多设备之间的流转。

     ```typescript
     import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { window } from '@kit.ArkUI';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       // ...

       private async initializeMainWindow(windowStage: window.WindowStage): Promise<void> {
         try {
           this.mainWindow = windowStage.getMainWindowSync();
           AppStorage.setOrCreate('mainWindow', this.mainWindow);
           await this.mainWindow.setWindowLayoutFullScreen(true);
           this.initSafeArea(this.mainWindow);
           this.mainWindow.on('avoidAreaChange', (option) => {
             switch (option.type) {
               // 监听状态栏避让区域
               case window.AvoidAreaType.TYPE_SYSTEM: {
                 const topHeight = Math.max(option.area.topRect.height, AppStorage.get<number>('topAvoidHeight') ?? 0);
                 AppStorage.setOrCreate('topAvoidHeight', topHeight);
                 break;
               }
               // 监听挖孔区避让区域
               case window.AvoidAreaType.TYPE_CUTOUT: {
                 this.handleCutoutAvoidArea(option.area);
                 break;
               }
               // 监听底部导航区避让区域
               case window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR: {
                 const bottomHeight = Math.max(option.area.bottomRect.height, AppStorage.get<number>('bottomAvoidHeight') ?? 0);
                 AppStorage.setOrCreate('bottomAvoidHeight', bottomHeight);
                 break;
               }
               default: {
                 break;
               }
             }
           });
         } catch (err) {
           hilog.error(DOMAIN, 'testTag', 'Failed to initialize avoid area listener. Cause: %{public}s', JSON.stringify(err));
         }
       }

       private initSafeArea(win: window.Window): void {
         try {
           // 获取状态栏避让区域
           const systemAvoidArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
           // 获取底部导航区避让区域
           const navigationAvoidArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
           // 获取挖孔区避让区域
           const cutoutAvoidArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_CUTOUT);

           AppStorage.setOrCreate('topAvoidHeight', systemAvoidArea.topRect.height);
           AppStorage.setOrCreate('bottomAvoidHeight', navigationAvoidArea.bottomRect.height);
           AppStorage.setOrCreate('leftAvoidWidth', 0);
           AppStorage.setOrCreate('rightAvoidWidth', 0);
           this.handleCutoutAvoidArea(cutoutAvoidArea);
         } catch (err) {
           hilog.error(DOMAIN, 'testTag', 'Failed to init safe area. Cause: %{public}s', JSON.stringify(err));
         }
       }

       private handleCutoutAvoidArea(cutoutAvoidArea: window.AvoidArea): void {
         if (cutoutAvoidArea.topRect.height > 0) {
           const topHeight = Math.max(AppStorage.get<number>('topAvoidHeight') ?? 0, cutoutAvoidArea.topRect.height);
           AppStorage.setOrCreate('topAvoidHeight', topHeight);
         }
         if (cutoutAvoidArea.bottomRect.height > 0) {
           const bottomHeight = Math.max(AppStorage.get<number>('bottomAvoidHeight') ?? 0, cutoutAvoidArea.bottomRect.height);
           AppStorage.setOrCreate('bottomAvoidHeight', bottomHeight);
         }
         if (cutoutAvoidArea.leftRect.width > 0) {
           AppStorage.setOrCreate('leftAvoidWidth', cutoutAvoidArea.leftRect.width);
         }
         if (cutoutAvoidArea.rightRect.width > 0) {
           AppStorage.setOrCreate('rightAvoidWidth', cutoutAvoidArea.rightRect.width);
         }
       }
     }
     ```
   * 还可以使用响应式环境变量装饰器[@Env](../harmonyos-references/ts-env-system-property.md)来实现避让区域的获取和监听。

     可通过响应式环境变量装饰器@Env(@Env(SystemProperties.WINDOW\_AVOID\_AREA)或@Env(SystemProperties.WINDOW\_AVOID\_AREA\_PX))获取并监听当前窗口的避让区域信息。

     当避让区域因横竖屏切换、系统栏显隐、窗口形态变化等发生变化时，@Env变量会自动更新，并触发相关组件刷新，从而实现沉浸式布局的动态适配。示例代码如下：

     ```typescript
     import { window } from '@kit.ArkUI';
     import { hilog } from '@kit.PerformanceAnalysisKit';

     const DOMAIN = 0x0000;

     @Entry
     @Component
     struct Index {
       @Env(SystemProperties.WINDOW_AVOID_AREA) avoidAreasVp: window.UIEnvWindowAvoidAreaInfoVP;
       @StorageProp('topAvoidHeight')
       topAvoidHeight: number = 0;
       @StorageProp('bottomAvoidHeight')
       bottomAvoidHeight: number = 0;
       @StorageProp('leftAvoidWidth')
       leftAvoidWidth: number = 0;
       @StorageProp('rightAvoidWidth')
       rightAvoidWidth: number = 0;
       @StorageLink('mainWindow')
       mainWindow: window.Window | undefined = undefined;
       // ...
     }
     ```
3. 布局中的系统界面元素需要避让状态栏和导航区域，否则可能产生UI元素重叠等情况。

   **说明** 

   避让区域存在大小为0的情况，当获取到的避让区域为0时，开发者需注意针对性适配此时的页面区域和布局，避免贴边、内容裁剪等问题，以确保应用界面正常显示且具有良好的美观性。

   开发者可以通过添加padding或添加占位组件的方式避让系统界面元素，此处以添加padding为例（具体数值为避让高度+10vp，防止在系统界面元素隐藏时布局内容贴边，开发者可以根据实际需求更改）。对控件顶部设置padding，实现对状态栏的避让；对底部设置padding，实现对底部导航区域的避让；对左右两侧设置padding，实现对挖孔区域的避让。

   * 避让使用getWindowAvoidArea接口获取到的避让区域的示例代码如下：

     ```typescript
     import { window } from '@kit.ArkUI';
     import { hilog } from '@kit.PerformanceAnalysisKit';

     const DOMAIN = 0x0000;

     @Entry
     @Component
     struct Index {
       // ...
       build() {
         Column() {
           // 避让顶部和挖孔区域
           Row() {
             Text('Top Container')
               .fontSize(40)
               .textAlign(TextAlign.Center)
               .width('100%')
           }
           .backgroundColor('#2786d9')
           .padding({
             top: this.getUIContext().px2vp(this.topAvoidHeight) + 10,
             bottom: 10,
             // 避让挖孔区域
             left: this.getUIContext().px2vp(this.leftAvoidWidth),
             right: this.getUIContext().px2vp(this.rightAvoidWidth)
           })

           Scroll() {
             Column({ space: 12 }) {
               Row() {
                 Text(this.text)
                   .fontSize(20)
               }

               Divider()

               Text(`topAvoidHeight: ${this.topAvoidHeight}`)
               Text(`bottomAvoidHeight: ${this.bottomAvoidHeight}`)
               Text(`leftAvoidWidth: ${this.leftAvoidWidth}`)
               Text(`rightAvoidWidth: ${this.rightAvoidWidth}`)
               Text(`preferredOrientation: ${this.orientationText}`)
               Text(this.statusText)
                 .fontColor('#666666')

               Row({ space: 8 }) {
                 Button('Auto Rotation')
                   .layoutWeight(1)
                   .onClick(() => {
                     void this.setOrientation(window.Orientation.AUTO_ROTATION, 'AUTO_ROTATION');
                   })

                 Button('Portrait')
                   .layoutWeight(1)
                   .backgroundColor('#0A7A5A')
                   .onClick(() => {
                     void this.setOrientation(window.Orientation.PORTRAIT, 'PORTRAIT');
                   })

                 Button('Landscape')
                   .layoutWeight(1)
                   .backgroundColor('#AD5C00')
                   .onClick(() => {
                     void this.setOrientation(window.Orientation.LANDSCAPE, 'LANDSCAPE');
                   })
               }
               .width('100%')

               Text('Cutout test: rotate the app and observe whether leftAvoidWidth / rightAvoidWidth change on a cutout device.')
                 .fontColor('#666666')
             }
             .width('100%')
           }
           .backgroundColor(Color.White)
           .padding(20)
           .borderRadius(15)
           .width('80%')
           .margin({
             left: this.getUIContext().px2vp(this.leftAvoidWidth),
             right: this.getUIContext().px2vp(this.rightAvoidWidth)
           })
           .layoutWeight(1)
           // 避让底部和挖孔区域
           Row() {
             Text('Bottom Container')
               .fontSize(40)
               .textAlign(TextAlign.Center)
               .width('100%')
           }
           .backgroundColor('#96dffa')
           .padding({
             top: 10,
             bottom: this.getUIContext().px2vp(this.bottomAvoidHeight) + 10,
             // 避让挖孔区域
             left: this.getUIContext().px2vp(this.leftAvoidWidth),
             right: this.getUIContext().px2vp(this.rightAvoidWidth)
           })
         }
         .width('100%')
         .height('100%')
         .padding({
           left: this.getUIContext().px2vp(this.leftAvoidWidth),
           right: this.getUIContext().px2vp(this.rightAvoidWidth)
         })
         .alignItems(HorizontalAlign.Center)
         .backgroundColor('#d5d5d5')
         .justifyContent(FlexAlign.SpaceBetween)
       }
     }
     ```
   * 避让使用@Env(SystemProperties.WINDOW\_AVOID\_AREA)获取到的避让区域的示例代码如下：

     ```typescript
      // ...
       build() {
         Column() {
           Row() {
             Text('Top Container')
               .fontSize(40)
               .textAlign(TextAlign.Center)
               .width('100%')
           }
           .backgroundColor('#2786d9')
           .padding({
             top: this.avoidAreasVp.statusBar.topRect.height + 10,
             bottom: 10,
             left: this.avoidAreasVp.cutout.leftRect.width,
             right: this.avoidAreasVp.cutout.rightRect.width
           })

           Scroll() {
             Column({ space: 12 }) {
               Row() {
                 Text(this.text)
                   .fontSize(20)
               }

               Divider()

               Text(`topAvoidHeight: ${this.topAvoidHeight}`)
               Text(`bottomAvoidHeight: ${this.bottomAvoidHeight}`)
               Text(`leftAvoidWidth: ${this.leftAvoidWidth}`)
               Text(`rightAvoidWidth: ${this.rightAvoidWidth}`)
               Text(`preferredOrientation: ${this.orientationText}`)
               Text(this.statusText)
                 .fontColor('#666666')

               Row({ space: 8 }) {
                 Button('Auto Rotation')
                   .layoutWeight(1)
                   .onClick(() => {
                     void this.setOrientation(window.Orientation.AUTO_ROTATION, 'AUTO_ROTATION');
                   })

                 Button('Portrait')
                   .layoutWeight(1)
                   .backgroundColor('#0A7A5A')
                   .onClick(() => {
                     void this.setOrientation(window.Orientation.PORTRAIT, 'PORTRAIT');
                   })

                 Button('Landscape')
                   .layoutWeight(1)
                   .backgroundColor('#AD5C00')
                   .onClick(() => {
                     void this.setOrientation(window.Orientation.LANDSCAPE, 'LANDSCAPE');
                   })
               }
               .width('100%')

               Text('Cutout test: rotate the app and observe whether leftAvoidWidth / rightAvoidWidth change on a cutout device.')
                 .fontColor('#666666')
             }
             .width('100%')
           }
           .backgroundColor(Color.White)
           .padding(20)
           .borderRadius(15)
           .width('80%')
           .margin({
             left: this.avoidAreasVp.cutout.leftRect.width,
             right: this.avoidAreasVp.cutout.rightRect.width
           })
           .layoutWeight(1)

           Row() {
             Text('Bottom Container')
               .fontSize(40)
               .textAlign(TextAlign.Center)
               .width('100%')
           }
           .backgroundColor('#96dffa')
           .padding({
             top: 10,
             bottom: this.avoidAreasVp.navigationIndicator.bottomRect.height + 10,
             left: this.avoidAreasVp.cutout.leftRect.width,
             right: this.avoidAreasVp.cutout.rightRect.width
           })
         }
         .width('100%')
         .height('100%')
         .padding({
           left: this.avoidAreasVp.cutout.leftRect.width,
           right: this.avoidAreasVp.cutout.rightRect.width
         })
         .alignItems(HorizontalAlign.Center)
         .backgroundColor('#d5d5d5')
         .justifyContent(FlexAlign.SpaceBetween)
       }
     }
     ```
4. 根据实际的UI界面显示或相关UI元素背景颜色等，还可以按需设置状态栏的文字颜色、背景色或设置导航区域的显示或隐藏，以使UI界面效果呈现和谐。状态栏和导航区域默认是透明的，透传的是应用界面的背景色。

   此例中UI颜色比较简单，故未对状态栏文字颜色、背景色进行设置，未对导航区域进行隐藏。

| 未适配沉浸式布局与避让区 | 适配沉浸式布局与避让区 |
| --- | --- |
|  |  |
