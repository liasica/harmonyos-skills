---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-595
title: 监听导航条安全区域高度处理不当导致布局异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 监听导航条安全区域高度处理不当导致布局异常
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:001a7dd3a14c82382b42d63abb924178b6861326077a1d4ce1539c39def71848
---

## 问题现象

拉起相机功能，拍摄后返回，并使用windowClass.on('avoidAreaChange')监听安全避让区域的变化，此时监听到的底部导航栏安全避让区域高度变大，导致整体页面布局上抬。

问题代码示例参考如下：

```screen
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
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
    let windowClass = windowStage.getMainWindowSync()
    // 1.初始化获取布局避让遮挡的区域
    let type = window.AvoidAreaType.TYPE_SYSTEM
    let avoidArea = windowClass.getWindowAvoidArea(type)
    let topHeight = avoidArea.topRect.height
    let vpTopHeight = windowClass.getUIContext().px2vp(topHeight)
    console.info('avoidAreaChange init topHeight:', `${topHeight}`)
    AppStorage.setOrCreate('topRectHeight', vpTopHeight)
    let bottomHeight = avoidArea.bottomRect.height
    let vpBotHeight = windowClass.getUIContext().px2vp(bottomHeight)
    console.info('avoidAreaChange init bottomHeight:', `${bottomHeight}`)
    AppStorage.setOrCreate('bottomRectHeight', vpBotHeight)
    // 2.注册监听函数，动态获取避让区域数据
    windowClass.on('avoidAreaChange', (data) => {
      if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
        let topRectHeight = data.area.topRect.height;
        console.info('avoidAreaChange topRectHeight:', `${topRectHeight}`)
        AppStorage.setOrCreate('topRectHeight', topRectHeight);
      } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
        let bottomRectHeight = data.area.bottomRect.height;
        console.info('avoidAreaChange bottomRectHeight:', `${bottomRectHeight}`)
        AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
      } else {
        console.info('avoidAreaChange other:')
      }
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed,release UI related resources
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
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/SyMD4mi6S8iEf3hNj_V-NA/zh-cn_image_0000002628392532.png "点击放大")

## 背景知识

* 安全区域是指页面的显示区域，默认不与系统设置的非安全区域比如状态栏、导航栏区域重叠，默认情况下开发者开发的界面都被布局在安全区域内。
* 在应用启用沉浸式模式时，页面元素可能会出现与状态栏或导航栏重叠的问题。这时需要通过接口[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)和[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)获取并动态监听避让区域的变更信息，页面布局根据避让区域信息进行动态调整。
* 一般是对控件顶部设置padding（具体数值与状态栏高度一致），实现对状态栏的避让；对底部设置padding（具体数值与底部导航条区域高度一致），实现对底部导航条的避让。

## 问题定位

1. 查看日志打印，确认底部导航条避让区域高度变化。

   初始化日志。

   ```screen
   I     avoidAreaChange init topHeight:123
   I     avoidAreaChange init bottomHeight:0
   ```
2. 拉起相机后返回监听的日志。

   ```screen
   I     avoidAreaChange bottomRectHeight:0
   I     avoidAreaChange bottomRectHeight:91
   ```
3. 通过ArkUI Inspector确认页面布局变化，可以看到页面初始化时，最外层Column的padding-bottom=0px，在拉起相机并返回后，最外层Column的padding-bottom=91px，通过日志也可以证明底部导航条避让区域高度的确有变化。

   | 初始化页面布局 | 拉起相机后返回的页面布局 |
   | --- | --- |
   |  |  |
4. 通过确认发现padding-bottom=0px是因为getWindowAvoidArea()传入的类型为Type=window.AvoidAreaType.TYPE\_SYSTEM，此时获取的不是底部导航条避让区域高度而是顶部状态栏的高度，因此需要传入Type=window.AvoidAreaType.TYPE\_NAVIGATION\_INDICATOR来获取底部导航条避让区域高度。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/-ND0KpDTTu6G20msxXe1Yw/zh-cn_image_0000002628552428.png "点击放大")
5. 根据上一步修改后发现页面初始化后最外层Column的padding-bottom=28px，还是存在页面布局上抬的情况，再次排查发现监听避让区域变化后获取的高度单位是px，而初始化时进行了单位转换，使用的是vp，所以需要全局统一单位。

## 分析结论

ArkUI为开发者提供4种像素单位，采用vp为基准数据单位。因此为了UI组件布局统一，最好统一使用vp作为数据单位，而getWindowAvoidArea()和on('avoidAreaChange')获取到的窗口矩形区域[Rect](../harmonyos-references/arkts-apis-window-i.md#rect7)是以px为单位的，需要进行px2vp的单位转换。

## 修改建议

1. 在EntryAbility.ets中获取顶部状态栏和底部导航条高度，进行单位转换后使用[AppStorage](../harmonyos-references/ts-state-management.md#appstorage)保存。

   获取避让区示例代码如下：

   ```screen
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { UIAbility } from '@kit.AbilityKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onWindowStageCreate(windowStage: window.WindowStage): void {
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         let windowClass = windowStage.getMainWindowSync();
         // 1.初始化获取布局避让遮挡的区域
         let type = window.AvoidAreaType.TYPE_SYSTEM;
         let avoidArea = windowClass.getWindowAvoidArea(type);
         let topHeight = avoidArea.topRect.height;
         let vpTopHeight = windowClass.getUIContext().px2vp(topHeight);
         console.info('avoidAreaChange init topHeight:', `${topHeight}`);
         AppStorage.setOrCreate('topRectHeight', vpTopHeight);
         let bottomHeight = avoidArea.bottomRect.height;
         let vpBotHeight = windowClass.getUIContext().px2vp(bottomHeight);
         console.info('avoidAreaChange init bottomHeight:', `${bottomHeight}`);
         AppStorage.setOrCreate('bottomRectHeight', vpBotHeight);
         // 2.注册监听函数，动态获取避让区域数据
         windowClass.on('avoidAreaChange', (data) => {
           if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
             let topRectHeight = windowClass.getUIContext().px2vp(data.area.topRect.height); // UI全局单位统一，添加px2vp的单位转换操作
             console.info('avoidAreaChange topRectHeight:', `${topRectHeight}`);
             AppStorage.setOrCreate('topRectHeight', topRectHeight);
           } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
             let bottomRectHeight =
               windowClass.getUIContext().px2vp(data.area.bottomRect.height); // UI全局单位统一，添加px2vp的单位转换操作
             console.info('avoidAreaChange bottomRectHeight:', `${bottomRectHeight}`);
             AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
           } else {
             console.info('avoidAreaChange other:');
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
   };
   ```

   **说明** 

   新版[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)需要在获取UIContext之后使用，getUIContext需在windowStage.loadContent之后调用。因此可以在自定义组件的生命周期函数中再调用px2vp。
2. 调用方法：通过设置页面最外层容器组件的padding来解决页面重叠的问题，具体使用方法请参考以下代码：

   ```screen
   import { camera, cameraPicker as picker } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   async function openCamera(context: Context) {
     try {
       let pickerProfile: picker.PickerProfile = {
         cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
       };
       await picker.pick(context, [picker.PickerMediaType.PHOTO, picker.PickerMediaType.VIDEO], pickerProfile);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`the pick call failed. error code: ${err.code}`);
     }
   }

   @Entry
   @Component
   struct HomePage {
     message: string = 'Hello World';
     @State topHeight: number = 0;
     @State bottomHeight: number = 0;

     aboutToAppear(): void {
       this.topHeight = AppStorage.get('topRectHeight') as number;
       this.bottomHeight = AppStorage.get('bottomRectHeight') as number;
     }

     build() {
       Column() {
         Text(this.message)
           .id('HomePageHelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             let context = this.getUIContext().getHostContext() as Context as common.UIAbilityContext;
             // 调用系统相机
             openCamera(context);
           });
         Image($r('app.media.background'))
           .height('100%')
           .width('100%');
       }
       .padding({ bottom: this.bottomHeight, top: this.topHeight })
       .height('100%')
       .width('100%');
     }
   }
   ```
