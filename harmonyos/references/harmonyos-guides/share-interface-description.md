---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-interface-description
title: 应用内处理分享内容
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 应用内处理分享内容
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:915845e9942ace0b1ca32447c8835f28f2184c521b85e7afbdc5bf10631bdb7e
---

目标应用可以通过[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)构建接收分享内容的界面，并将应用显示到分享面板应用推荐区内，以实现将分享内容传递到目标应用内进行处理。开发时需要接入方实现[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)并于module.json5中注册支持分享内容的能力。

## 接口说明

getSharedData接口用于从want中获取分享数据；getContactInfo接口用于从want中获取联系人信息（仅当用户选择联系人分享时有返回值）。具体API说明详见[接口文档](../harmonyos-references/share-system-share.md#getshareddata)。

**表1** 目标应用解析分享数据接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| [getSharedData](../harmonyos-references/share-system-share.md#getshareddata)(want: [Want](../harmonyos-references/js-apis-inner-ability-want.md)): Promise<[SharedData](../harmonyos-references/share-system-share.md#shareddata)> | 从want中获取分享数据 |
| [getContactInfo](../harmonyos-references/share-system-share.md#getcontactinfo)(want: [Want](../harmonyos-references/js-apis-inner-ability-want.md)): Promise<[ContactInfo](../harmonyos-references/share-system-share.md#contactinfo)> | 从want中获取联系人信息 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { systemShare } from '@kit.ShareKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 目标应用可实现[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)。在Ability被启动后，可以在其[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中获取传入的want参数。将want参数通过[getSharedData](../harmonyos-references/share-system-share.md#getshareddata)解析后得到分享数据。

   ```typescript
   export default class TestUIAbility extends UIAbility {
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       systemShare.getSharedData(want)
         .then((data: systemShare.SharedData) => {
           data.getRecords().forEach((record: systemShare.SharedRecord) => {
             // 处理分享数据
           });
         })
         .catch((error: BusinessError) => {
           console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
           this.context.terminateSelf();
         });
     }
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       windowStage.loadContent('pages/Index', (error) => {
         if (error.code) {
           console.error(`Failed to load the content. Code: ${error.code}, message: ${error.message}`);
           return;
         }
         console.info('Succeeded in loading the content.');
       });
     }
   }
   ```
3. 构建完UIAbility，需要在应用配置文件（src/main/module.json5）的[skills](module-configuration-file.md#skills标签)配置中注册。配置actions为ohos.want.action.sendData；uris需穷举所有支持的数据类型。

   ```json
   "abilities": [
     {
       "name": "TestUIAbility",
       "srcEntry": "./ets/entryability/TestUIAbility.ets",
       "description": "$string:EntryAbility_desc",
       "icon": "$media:layered_image",
       "label": "$string:EntryAbility_label",
       "startWindowIcon": "$media:startIcon",
       "startWindowBackground": "$color:start_window_background",
       "exported": true,
       "skills": [
         {
           "actions": [
             "ohos.want.action.sendData"
           ],
           // scheme为预留字段，在此处不生效，配置file仅为示例
           // 目标应用在配置支持接收的数据类型时，需穷举支持的UTD，比如：支持全部图片类型，可声明：general.image
           // maxFileSupported 对于归属指定类型的文件，标识一次支持接收的最大数量。默认为0，代表不支持此类文件的分享。
           // 文件类型归属关系参考：@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)
           "uris": [
             {
               "scheme": "file",
               "utd": "general.text",
               "maxFileSupported": 1
             },
             {
               "scheme": "file",
               "utd": "general.png",
               "maxFileSupported": 1
             },
             {
               "scheme": "file",
               "utd": "general.jpeg",
               "maxFileSupported": 1
             }
           ]
         }
       ]
     }
   ]
   ```
