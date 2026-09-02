---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1457
title: 如何设置应用的启动图为全屏图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何设置应用的启动图为全屏图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3210542058da661a550ca1cc52bacec27e251864ce6eb39e476a33e99df1e915
---

## 问题现象

如何做到startWindowIcon设置的图片和闪屏页面使用的是同一张，现在startWindowIcon设置的图片尺寸明显超过闪屏页面所需尺寸。

## 背景知识

* [abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。其中startWindowIcon标识当前UIAbility组件启动页面图标资源文件，startWindowBackground标识当前UIAbility组件启动页面背景颜色资源文件。
* 启动页：应用启动时系统默认显示的过渡窗口，用于提升用户体验（避免白屏），通常包含应用图标、名称等元素。
* startWindowIcon：用于定义启动窗口中显示的图标，需在应用配置文件中声明，该标签不可缺省，目前startWindowIcon的显示尺寸与图片原始尺寸保持一致，一般推荐放一个icon小图（分辨率建议不超过256\*256）。startWindowIcon启动图按图片像素大小居中显示，具体可参考：[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)。
* [onWindowStageCreate](../harmonyos-guides/uiability-lifecycle.md#onwindowstagecreate)：启动窗口的显示与onWindowStageCreate生命周期相关，窗口初始化完成后会自动隐藏。
* 主题与样式：可通过startWindowBackground配置启动窗口背景色，可以与图标配合实现视觉统一。
* 设置应用启动页可参考：[启动页的分类和实现方式](../harmonyos-guides/launch-page-config.md#启动页的分类和实现方式)。

## 解决方案

startWindowIcon的大小跟随图源尺寸，一般推荐放一个icon小图。startWindowIcon启动图全屏居中，按图片像素大小居中显示。

* **方案一：** 根据屏幕宽高进行定制化设计启动图的场景。

  设置全屏图片需要图片是SVG格式，普通图片不支持，可以通过：[display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)的[Display](../harmonyos-references/js-apis-display.md#display)实例获取屏幕宽高，然后准备一张屏幕宽高尺寸的图片。（以Pura X为例，为1136\*2690像素）SVG格式的矢量图，需要您自行设计，矢量图是天然支持跟着容器缩放的。
* **方案二：** 配置透明的启动图标与背景，自定义启动页的场景。

  修改module.json5中startWindowBackground背景色和启动图一致，并设置startIcon为透明的空图片，即可隐藏默认的启动页，同时新建一个启动页Page，用于显示启动图，使用定时器，2秒后执行跳转到主页面。

  1. module.json5，配置透明的启动图标与背景。

     ```json
     {
       "module": {
         "name": "entry",
         "type": "entry",
         "description": "$string:module_desc",
         "mainElement": "EntryAbility",
         "deviceTypes": [
           "phone"
         ],
         "deliveryWithInstall": true,
         "installationFree": false,
         "pages": "$profile:main_pages",
         "abilities": [
           {
             "name": "EntryAbility",
             "srcEntry": "./ets/entryability/EntryAbility.ets",
             "description": "$string:EntryAbility_desc",
             "icon": "$media:layered_image",
             "label": "$string:EntryAbility_label",
             "startWindowIcon": "$media:custom_bg",
             "startWindowBackground": "$color:start_window_background",
             "exported": true,
             "skills": [
               {
                 "entities": [
                   "entity.system.home"
                 ],
                 "actions": [
                   "ohos.want.action.home"
                 ]
               }
             ]
           }
         ],
         "extensionAbilities": [
           {
             "name": "EntryBackupAbility",
             "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
             "type": "backup",
             "exported": false,
             "metadata": [
               {
                 "name": "ohos.extension.backup",
                 "resource": "$profile:backup_config"
               }
             ],
           }
         ]
       }
     }
     ```
  2. EntryAbility.ets，加载自定义的启动页。

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
         windowStage.loadContent('pages/Splash', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }

       onWindowStageDestroy(): void {
         // Main window is destroyed, release UI related resources
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
     };
     ```
  3. Splash.ets，启动页内容。

     ```ts
     @Entry
     @Component
     struct Splash {
       private timer: number | null = null;

       aboutToAppear(): void {
         this.setTimer();
       }

       aboutToDisappear(): void {
         this.clearTimer();
       }

       setTimer() {
         this.timer = setInterval(() => {
           //此处可自定义跳转逻辑
           this.getUIContext().getRouter().replaceUrl({
             url: 'pages/Index'
           });
           this.clearTimer();
         }, 2000);
       }

       clearTimer() {
         if (this.timer !== null) {
           clearInterval(this.timer);
           this.timer = null;
         }
       }

       build() {
         Column() {
           Image($r('app.media.splash_img')) // 启动图路径需替换成自定义的资源路径
             .width('100%')
             .height('100%')
             .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
             .syncLoad(true); // 设置图片为同步加载
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.White)
         .justifyContent(FlexAlign.Center)
         .alignItems(HorizontalAlign.Center);
       }
     }
     ```
  4. Index.ets，应用主页。

     ```ts
     @Entry
     @Component
     struct Index {
       private  message: string = '首页';

       build() {
         RelativeContainer() {
           Text(this.message)
             .id('HelloWorld')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
         }
         .height('100%')
         .width('100%');
       }
     }
     ```
* **方案三：** 适合API19+版本以上的场景。

  配置增强启动页:请参考[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)**（需要设备系统版本满足API19+，否则startWindow字段不会生效）**。

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/TYTlDg2xQ9y1AOG9e9xpwg/zh-cn_image_0000002658843535.png "点击放大")

## 常见FAQ

Q：自定义启动页跳转后是否还能返回。

A：router模块提供了两种跳转模式，分别是router.pushUrl和router.replaceUrl。router.pushUrl：目标页面不会替换当前页，而是压入页面栈。这样可以保留当前页的状态，并且可通过返回键或router.back方法返回到当前页。router.replaceUrl：目标页面会替换当前页，并销毁当前页。这样可以释放当前页的资源，并且无法返回到当前页，可以把router.pushUrl替换为router.replaceUrl实现。

Q：启动图片没有占满全屏。

A：给需要全屏显示的Image组件设置expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])来扩展组件的安全区域。

Q：使用配置增强启动页，配置了startWindow不生效，还是startWindowIcon在生效。

A：配置增强启动页需确保配置文件（如start\_window.json）中正确设置或文件路径无误。请确保startWindow字段正确指向了一个有效的json配置文件，并且该文件中包含了正确的启动页配置，另外，查看[启动页的分类和实现方式](../harmonyos-guides/launch-page-config.md#启动页的分类和实现方式)可以发现，是从API version 19开始支持startWindow字段。

Q：startWindowIcon启动图可以自适应吗？

A：目前startWindowIcon启动图是按图片实际像素大小居中显示的，如果要实现资源文件适配不同类型设备，不同分辨率，不同场景，可以根据设备一个或多个不同特征，创建限定词目录文件，在文件中存放适合场景的资源文件，可以参考[限定词目录与设备状态的匹配规则](../harmonyos-guides/resource-categories-and-access.md#限定词目录与设备状态的匹配规则)、[创建资源目录和资源文件](../harmonyos-guides/resource-categories-and-access.md#创建资源目录和资源文件)。

Q：配置了startWindow增强启动页同时在onWindowStageCreate又设置了相同的启动页（即方案二方案三同时使用），应用启动页出现闪屏现象。

A：startWindow配置增强启动页和onWindowStageCreate设置启动页两者互相独立且发生在不同的阶段，在两者过渡的时候可能会造成闪屏的现象，建议只配置其中之一。

Q：启动页的显示区域是否可以自己设置？

A：图标/插画资源区域和品牌标识资源区域不支持三方应用设置，该区域由系统侧计算。

Q：应用设置全屏启动图后，在启动时出现闪屏现象。

A：startWindow配置增强启动页和onWindowStageCreate设置启动页两者互相独立且发生在不同的阶段，在两者过渡的时候可能会造成闪屏的现象，建议只配置其中之一。

Q：增强启动页startWindowIllustration和startWindowBrandingImage的布局规则是什么？

A：规则如下：

* 插画资源在页面高度的70%内上下居中（窗口上部分）展示，如资源尺寸超出其展示区域，将由系统侧保持宽高比缩小，使得资源完全显示在其展示区域内；否则其尺寸保持不变。插画区域宽高比1:1，尺寸计算方式为当前窗口高度/2与窗口宽度比较，取短边的80%作为插画范围的高度，取短边的70%作为插画内容的高度。
* 品牌标识资源在页面高度的30%内上下居中（窗口下部分）展示。如资源尺寸超出其展示区域，将由系统侧保持宽高比缩小，使得资源完全显示在其展示区域内；否则其尺寸保持不变。品牌标识资源自动适配最大宽度or高度，最大尺寸宽度为窗口宽度-左边距（24）-右边距（24），高度为窗口高度30%-上边距（40）-下边距（40）
