---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-font-settings
title: 自定义字体设置
breadcrumb: 最佳实践 > 主题与样式 > 自定义字体设置
category: best-practices
scraped_at: 2026-09-02T15:03:16+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:088399f89afc43c11493e2bdf9c51e334b99f286c720ad2fe005d769468d7d3c
---

## 概述

在应用开发中，字体是用户界面的核心视觉元素之一，也是构建良好用户体验的关键要素之一，直接影响应用界面的美观性、可读性和用户体验。

ArkUI提供了全面的字体控制能力，如自定义设置字体大小和字重；支持通过[registerFont()](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)方法注册TTF和OTF自定义字体文件，或下载字体文件到沙箱内注册使用，实现字体的动态切换；支持省略号、自动缩放和换行控制等多种文本内容溢出处理策略，使开发者能够精细调整应用中的字体表现，满足应用多样化的设计需求。

本文将介绍以下字体设置场景的实现：

* [使用自定义字体显示文本](bpta-custom-font-settings.md#section148766114477)
* [从自定义字体恢复为系统字体](bpta-custom-font-settings.md#section994084874710)
* [使字体大小跟随系统设置](bpta-custom-font-settings.md#section1635772719497)
* [使字体大小不跟随系统设置](bpta-custom-font-settings.md#section161251820115015)

## 使用自定义字体显示文本

**场景描述**

在字体设置中，点击选择字体列表中的某个字体后，页面的字体样式会发生变化。在退出应用重新进入后，默认显示退出前选择的字体样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/5hv9zxhKR5awTzdnnS7T1A/zh-cn_image_0000002361481894.gif "点击放大")

**实现原理**

registerFont()方法可以在字体管理器中注册自定义字体，支持注册TTF格式和OTF格式的字体文件。

[preferences (用户首选项)](../harmonyos-references/js-apis-data-preferences.md)则为应用提供了处理Key-Value键值型数据的能力，支持应用持久化轻量级数据，以及数据的修改和查询。

**开发步骤**

1. 创建首选项工具类PreferenceUtils，在类中定义如下方法：
   * getTextFontPreference()方法：在其中通过[getPreferencesSync()](../harmonyos-references/js-apis-data-preferences.md#preferencesgetpreferencessync10)方法获取首选项实例。
   * saveModifyFont()方法：在其中通过[putSync()](../harmonyos-references/js-apis-data-preferences.md#putsync10)方法将传入的字体信息数据写入首选项实例中，再使用[flush()](../harmonyos-references/js-apis-data-preferences.md#flush)方法将数据持久化存储。
   * getFont()方法：在其中通过[getSync()](../harmonyos-references/js-apis-data-preferences.md#getsync10)方法从首选项实例中获取存储的数据。

   ```typescript
   export class PreferenceUtils {
     preference?: preferences.Preferences;

     // Get Preferences instance
     getTextFontPreference(context: Context) {
       try {
         this.preference = preferences.getPreferencesSync(context, { name: 'TextFontPreference' });
         hilog.info(0x0000, TAG, 'create preference success');
       } catch (err) {
         let error = err as BusinessError;
         hilog.error(0x0000, TAG, `create preference failed. code: ${error.code}, message:${err.message}`);
       }
     }

     // ...

     // Save Font
     saveModifyFont(textFont: string) {
       try {
         this.preference?.putSync(TEXT_FONT, textFont);
         this.preference?.flush((err: BusinessError) => {
           if (err) {
             hilog.error(0x0000, TAG, `Failed to flush. code:${err.code}, message:${err.message}`);
             return;
           }
           hilog.info(0x0000, TAG, 'Succeeded in flushing.');
         })
       } catch (err) {
         let error = err as BusinessError;
         hilog.error(0x0000, TAG,
           `putSync or flush font preference data failed. code: ${error.code}, message:${err.message}`);
       }
     }

     // Get Font
     getFont(): string {
       let textFont: string = '';
       try {
         textFont = this.preference?.getSync(TEXT_FONT, '') as string;
       } catch (err) {
         let error = err as BusinessError;
         hilog.error(0x0000, TAG, `getSync font preference data failed. code: ${error.code}, message:${err.message}`);
       }
       return textFont;
     }
   }

   export default new PreferenceUtils();
   ```
2. 在EntryAbility的onCreate()生命周期中，调用getTextFontPreference()方法获取首选项实例。

   ```typescript
   export default class EntryAbility extends UIAbility {
     onCreate(_want: Want, _launchParam: AbilityConstant.LaunchParam): void {
       // Get preference instance
       PreferenceUtils.getTextFontPreference(this.context);
       // ...
     }

     // ...
   }
   ```
3. 定义registerMyFont()方法注册自定义字体。

   在使用时，需要通过UIContext中的[getFont()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的Font对象，再通过该对象调用registerFont()方法注册字体。

   ```typescript
   // Register font
   export function registerMyFont(uiContext: UIContext) {
     try {
       // Register HarmonyOS Italic font through registrant Font
       uiContext.getFont().registerFont({
         familyName: $r('app.string.HarmonyOS_Italic'),
         familySrc: $rawfile('HarmonyOS_SansItalic.ttf')
       });
       // Register HarmonyOS Condensed font through registrant Font
       uiContext.getFont().registerFont({
         familyName: $r('app.string.HarmonyOS_Condensed'),
         familySrc: $rawfile('HarmonyOS_Condensed.ttf')
       });
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(0x0000, TAG, `registerFont failed. code: ${error.code}, message:${err.message}`);
     }
   }
   ```
4. 通过@StorageLink装饰变量fontOffset，标识当前选择的字体。在页面aboutToAppear()生命周期中，调用registerMyFont()方法并传入UIContext，注册自定义字体，并通过PreferenceUtils类调用getFont()方法，获取首选项中存储的数据，赋值给fontOffset，实现退出重新进入应用后显示退出前选择的字体。

   ```typescript
   @StorageLink('fontOffset') fontOffset: string = '';
   // ...

   aboutToAppear() {
     // ...
     // Get font data from preferences
     this.fontOffset = PreferenceUtils.getFont();
     // Register font
     registerMyFont(this.getUIContext());
   }
   ```
5. 在MenuItem的onChange()事件中修改fontOffset的值，并通过saveModifyFont()方法，将选择的字体数据写入首选项并持久化存储。

   ```typescript
   MenuItem({
     content: item === '' ? $r('app.string.system_default') : item,
     endIcon: this.fontOffset === item ? $r('app.media.checkmark') : ''
   })
     .onChange(() => {
       this.fontOffset = item;
       PreferenceUtils.saveModifyFont(item);
     })
   ```
6. 通过fontFamily属性传入变量fontOffset，使用注册的自定义字体改变字体样式。

   ```typescript
   // Example Text Content
   Column() {
     Text($r('app.string.preview_text'))
       // ...
       .fontFamily(this.fontOffset)
   }
   .width('100%')
   .padding(12)
   .margin({ top: 35 })
   .backgroundColor('#FFF')
   .borderRadius(16)
   ```

## 从自定义字体恢复为系统字体

**场景描述**

在应用设置页面的字体设置中，点击选择系统默认字体，首页和设置页顶部的字体样式变为系统默认。退出并重新进入应用后，仍会显示系统默认字体。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/cISqLw-qRQyHdGQ7NPnidw/zh-cn_image_0000002395161853.gif "点击放大")

**实现原理**

系统默认字体为无衬线字体HarmonyOS Sans，当fontFamily属性被显式设置为空字符串时，实际生效字体与不设置fontFamily时的效果一致，会回退到默认字体，字体样式、字重等其它属性可正常应用。

**开发步骤**

1. 方法定义参考：[使用自定义字体显示文本](bpta-custom-font-settings.md#li1099532613615)。
2. 在MenuItem的onChange()事件中修改fontOffset的值，并调用saveModifyFont()方法修改首选项的值。

   ```typescript
   Menu() {
     ForEach(this.menuItemArr, (item: string) => {
       MenuItem({
         content: item === '' ? $r('app.string.system_default') : item,
         endIcon: this.fontOffset === item ? $r('app.media.checkmark') : ''
       })
         .onChange(() => {
           this.fontOffset = item;
           PreferenceUtils.saveModifyFont(item);
         })
     }, (item: string) => item)
   }
   // ...
   ```
3. 通过fontFamily属性传入变量fontOffset，使用注册的自定义字体改变字体样式。

   ```typescript
   Text($r('app.string.preview_text'))
     // ...
     .fontFamily(this.fontOffset)
   ```

## 使字体大小跟随系统设置

**场景描述**

在设置页面中，点击打开Toggle按钮，使页面字体大小跟随系统设置发生变化。此时，自定义字体大小和字重的Slider将被禁用，无法滑动或点击。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/_wFs7B1xQ-CSRc7p7aOBgw/zh-cn_image_0000002361641798.gif "点击放大")

**实现原理**

在应用的[app.json5](../harmonyos-guides/app-configuration-file.md)配置文件中，configuration标签是用于标识应用字体大小跟随系统变更的配置文件。当configuration的fontSizeScale属性取值为followSystem，且字体大小fontSize属性使用fp为像素单位时，在改变系统设置中的字体大小缩放比例后，应用中的字体也会相应变化。

**开发步骤**

1. 在AppScope/resources/base/profile下面定义配置文件xxx.json。

   fontSizeScale属性取值（默认为nonFollowSystem不跟随系统）：

   * followSystem：跟随系统。
   * nonFollowSystem：不跟随系统。

   fontSizeMaxScale属性：用于设置应用字体大小在选择跟随系统后，相比系统字体的最大比例。

   ```screen
   {
     "configuration": {
       "fontSizeScale": "followSystem",
       "fontSizeMaxScale": "2"
     }
   }
   ```
2. 在app.json5配置文件中通过configuration字段，标识当前应用字体大小是否跟随系统配置。

   ```json
   {
     "app": {
       "bundleName": "com.example.textdisplayfont",
       "vendor": "example",
       "versionCode": 1000000,
       "versionName": "1.0.0",
       "icon": "$media:layered_image",
       "label": "$string:app_name",
       "configuration": "$profile:configuration"
     }
   }
   ```
3. 配置完成后应用字体大小和字重即可随系统设置发生变化。
4. 在Toggle组件的onChange()方法中，修改变量toggleState的值。

   ```typescript
   Toggle({ type: ToggleType.Switch, isOn: this.toggleState })
     .onChange((isOn: boolean) => {
       this.toggleState = isOn;
     })
   ```
5. 根据toggleState的值，控制Slider组件是否可交互。

   当toggleState为true时，表示跟随系统，Slider不可点击或滑动；为false时，表示不跟随系统，Slider可以点击或滑动。

   ```typescript
   Slider({
     min: -4,
     max: 4,
     value: this.fontSizeOffset,
     style: SliderStyle.InSet
   })
     .width('90%')
     .margin({ top: 12 })
     .enabled(!this.toggleState)
   ```

## 使字体大小不跟随系统设置

**场景描述**

在设置页中点击关闭Toggle按钮，通过Slider组件可以调整页面字体大小。在系统设置中调整字体大小，页面字体不会发生变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/h5r-jRPrQOiXz6yf_ym3fg/zh-cn_image_0000002395321741.gif "点击放大")

**实现原理**

在应用的[app.json5](../harmonyos-guides/app-configuration-file.md)配置文件中，通过configuration标签标识了应用字体跟随系统设置，当字体大小fontSize属性使用屏幕物理像素单位px时，页面字体大小将不再受系统设置的影响。

**开发步骤**

1. 使用[getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取display屏幕实例对象，然后通过该display对象获取设备的物理像素密度[densityDPI](../harmonyos-references/js-apis-display.md#display)。将字体大小fp为单位的数值传入fp2pxUtil()方法，将其转换为对应的px数值。

   ```typescript
   // Convert fp to px
   export function fp2pxUtil(fp: number): string {
     const pxStr: string = 'px';
     let pxVal: number = 0;
     let displayClass: display.Display | null = null;
     try {
       displayClass = display.getDefaultDisplaySync();
       pxVal = fp * (displayClass.densityDPI / 160);
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(0x0000, TAG, `get densityDPI failed. code: ${error.code}, message:${err.message}`);
     }
     return pxVal + pxStr;
   }
   ```
2. 在页面中通过判断toggleState变量的值，控制字体单位的切换，实现页面字体是否跟随系统设置。
   * 当toggleState为true时：使用number类型的值，以fp为像素单位，页面字体跟随系统设置。
   * 当toggleState为false时：调用fp2pxUtil()方法，传入具体数值转为以px为单位的值，使页面字体不跟随系统设置。

   ```typescript
   Text($r('app.string.setting'))
     .width('100%')
     .fontWeight(700)
     .fontSize(this.toggleState ? 26 : fp2pxUtil(26))
   ```

## 常见问题

### 如何获取系统缩放比例系数来修改应用内字体大小

1. 在app.json5中不配置configuration标签，或者在configuration标签指定的文件中，将fontSizeScale属性取值为nonFollowSystem不跟随系统，使应用字体大小不随系统设置发生变化。
2. 通过[onConfigurationUpdated()](../harmonyos-references/js-apis-app-ability-environmentcallback.md#onconfigurationupdated)获取系统设置中字体大小缩放比例fontSizeScale、字体粗细缩放比例fontWeightScale等变化的信息，再通过ApplicationContext.on('environment')对系统环境变化进行监听，可参考如下示例：

   ```typescript
   // System environment change information
   let envCallback: EnvironmentCallback = {
     onConfigurationUpdated(config) {
       envFont.fontSizeScale = config.fontSizeScale; // Font size scaling ratio
       envFont.fontWeightScale = config.fontWeightScale; // Font thickness scaling ratio
     },
     onMemoryLevel(level) {
       hilog.info(DOMAIN, TAG, `onMemoryLevel level: ${level}`);
     }
   }
   let appContext = this.context.getApplicationContext();
   // Register to monitor changes in the system environment
   callbackId = appContext.on('environment', envCallback);
   ```
3. 在需要修改字体大小的位置，将基础字体大小 \* 字体大小缩放系数的值，传入fontSize()属性即可。

## 示例代码

* [实现字体设置功能](https://gitcode.com/harmonyos_samples/text-display-font)
