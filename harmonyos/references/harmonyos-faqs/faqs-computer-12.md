---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-12
title: PC端设置窗口大小不生效
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > PC端设置窗口大小不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9fdf451eb8660645521eaadbd1bb921aab516f7dacc2fb2c5ac911c1c09470a0
---

## 问题现象

通过配置module.json5文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的maxWindowWidth、maxWindowHeight两个属性，设置窗口设置宽高为500\*1000，实际运行过程中未生效，日志监听窗口大小为950 \* 1394。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/vwkxkBQwTMKsdYKnNgaXmg/zh-cn_image_0000002658791751.png "点击放大")

## 背景知识

* 使用[getGlobalRect](../harmonyos-references/arkts-apis-window-window.md#getglobalrect13)方法可以获取窗口在屏幕上的真实位置和大小。
* 通过配置[module.json5](../harmonyos-guides/module-configuration-file.md)文件中的[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)可以实现对应用图标、窗口等内容的自定义。

## 问题定位

1. 根据宽高都比设置数值偏大，推测是单位不一致导致。查阅[窗口大小限制](../harmonyos-guides/window-overview.md#约束与限制)，module.json5中数值单位为vp。而getGlobalRect方法返回类型为[Rect](../harmonyos-references/arkts-apis-window-i.md#rect7)，宽高单位是px。
2. 使用[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)方法转换单位后，重新打印日志，高度值仍不正确。查看maxWindowWidth和maxWindowHeight属性的描述，两者是用于设置窗口的最大宽高，如果需要指定窗口为某一数值，则需要同时设置minWindowHeight以及minWindowWidth。

## 分析结论

1. 单位不同：module.json5里的数值单位是vp，通过getGlobalRect获取的宽高单位是px。
2. maxWindowHeight、minWindowHeight、maxWindowWidth、minWindowWidth是一个区间范围，同时设置才能固定数值。

## 修改建议

1. 同时设置maxWindowHeight、minWindowHeight、maxWindowWidth、minWindowWidth四个属性固定初始窗口大小。
2. 日志打印通过getGlobalRect方法获取的宽高时使用px2vp()进行单位转换。

示例代码：

1. Index.ets文件：

   ```ts
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     @State screenWidth: number = 0;
     @State screenHeight: number = 0;
     context: Context | undefined = undefined;

     getScreenInfo() {
       let windowClass: window.Window | undefined = undefined;
       try {
         let promise = window.getLastWindow(this.context);
         promise.then((data) => {
           windowClass = data;
           this.screenWidth = windowClass.getGlobalRect().width; // 获取窗口宽度
           this.screenHeight = windowClass.getGlobalRect().height; // 获取窗口高度
         }).catch((err: BusinessError) => {
           console.error('getLastWindow error', err);
         });
       } catch (e) {
         console.error('setScreenOrientation error');
       }
     }

     aboutToAppear(): void {
       this.context = this.getUIContext().getHostContext() as common.Context;
       this.getScreenInfo();
     }

     build() {
       Column() {
         Text(`宽度是：${this.getUIContext().px2vp(this.screenWidth)}，高度是：${this.getUIContext()
           .px2vp(this.screenHeight)}`)
       }
     }
   }
   ```
2. 在module.json5文件中abilities标签配置宽高：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone",
         "2in1"
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
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "maxWindowHeight": 1000, // 设置最大高度
           "minWindowHeight": 1000, // 设置最小高度
           "maxWindowWidth": 500, // 设置最大宽度
           "minWindowWidth": 500, // 设置最小宽度
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

## 常见FAQ

Q：PC端应用如何设置窗口大小？

A：PC/2in1设备上的应用可以支持全屏或自由窗口、自定义窗口标题栏以及沉浸式体验，满足用户的多样化体验。

* 可以在module.json5中配置参数设置窗口大小，参考[如何限制自由窗窗口尺寸](../best-practices/bpta-multi-device-window-mode.md#section6754152523715)。
* 应用窗口化适配：应用从桌面启动时，默认以非全屏窗口显示，窗口大小支持自由拖动。更多详情请参考[自由窗口模式适配](../best-practices/bpta-multi-device-window-mode.md#section151195853214)。
* 应用窗口化标题栏适配：应用窗口标题栏支持沉浸式和自定义。更多详情请参考[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)。
* 自由窗口的全屏沉浸式适配：视频类应用支持自由窗口与全屏沉浸式体验。更多详情请参考[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)。
