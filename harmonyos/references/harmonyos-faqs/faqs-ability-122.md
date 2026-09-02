---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-122
title: 已安装的应用在文件的打开方式中找不到
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 已安装的应用在文件的打开方式中找不到
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bf26886a5dd7d15d4fa6b691b970bc46e34ac3da9eee0400261a47e4cc469a2a
---

## 问题现象

已下载多个视频播放器，但是打开方式选择项中没有这些应用。

## 背景知识

支持打开文件的应用需要在[module.json5](../harmonyos-guides/file-processing-apps-startup.md#目标方接入步骤)配置文件中声明文件打开能力。

## 问题定位

1. 确定打开的文件类型，参考[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)。
2. 确定目标应用是否声明对应文件的打开能力，检查module.json5配置文件中的module.abilities.skills.uris.type。

## 分析结论

应用未声明对应文件格式的打开能力，所以不会出现在选项中。

## 修改建议

1. 以视频文件为例，需要在module.json5文件中增加如下配置。

   ```screen
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
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home",
                 "ohos.want.action.viewData" // 必填，声明数据处理能力
               ],
               "uris": [
                 {
                   // 允许打开uri中以file://协议开头标识的本地文件
                   "scheme": "file", // 必填，声明协议类型为文件
                   "type": "general.video", // 必填，表示支持打开的文件类型
                   "linkFeature": "FileOpen" // 必填且大小写敏感，表示此URI的功能为文件打开
                 }
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
2. 声明了文件打开的应用在被拉起后，获取传入的Want参数信息，从中获取待打开文件的URI。

   ```screen
   import { ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@ohos.base';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     uiContext: UIContext | undefined = undefined;

     onCreate(want: Want): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');

       // 从want信息中获取uri字段
       let uri = want.uri;
       if (uri == null || uri == undefined) {
         console.info('uri is invalid');
         return;
       }
       // 将uri信息保存至全局变量中
       AppStorage.setOrCreate<string>("fileUri", uri);
     }

     onNewWant(want: Want): void {
       // 从want信息中获取uri字段
       let uri = want.uri;
       if (uri == null || uri == undefined) {
         console.info('uri is invalid');
         return;
       }
       // 将uri信息保存至全局变量中
       AppStorage.setOrCreate<string>("fileUri", uri);
       this.uiContext?.getRouter().pushUrl({
         url: 'pages/Index'
       }).catch((error: BusinessError) => {
         console.error(`error:${error.message}`);
       });
     }

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
         try {
           this.uiContext = windowStage.getMainWindowSync().getUIContext();
         } catch (error) {
           console.error(`error:${error.message}`);
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
       windowStage.getMainWindow((err: BusinessError, data: window.Window) => {
         if (err.code) {
           return;
         }
         data.setWindowSystemBarEnable([]);
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
   }
   ```

   ```screen
   @Entry
   @Component
   struct Index {
     private controller: VideoController = new VideoController();
     @StorageLink('fileUri') private fileUri: string = '';

     build() {
       Column() {
         Video({
           src: this.fileUri,
           controller: this.controller
         })
           .margin({bottom: 20})
           .objectFit(ImageFit.Contain)
           .autoPlay(true);
       }
       .height('100%')
       .width('100%')
       .backgroundColor(Color.Black)
     }
   }
   ```
