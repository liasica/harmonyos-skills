---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-sec-panel
title: 分享详情页处理分享内容
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 目标应用处理分享内容 > 分享详情页处理分享内容
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e915805ef86393e53c7aa8ed120a47a7131dc3664d0c277c90c340579970792d
---

分享详情页能力基于[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)界面嵌入能力。目标应用可以通过[ShareExtensionAbility](../harmonyos-references/js-apis-app-ability-shareextensionability.md)构建接收分享内容的分享详情页，并将应用显示到分享面板应用推荐区内，通过分享详情页便捷的处理分享内容。开发时需要接入方实现[ShareExtensionAbility](../harmonyos-references/js-apis-app-ability-shareextensionability.md)并于module.json5中注册支持分享内容的能力。

通过此方式注册的应用，点击时将跳转到分享详情页，也可返回分享面板。参见：[分享详情页面](../design-guides/share-0000001957076313.md#section27599419404)。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { Want, ShareExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
   import { systemShare } from '@kit.ShareKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 目标应用可以使用[ShareExtensionAbility](../harmonyos-references/js-apis-app-ability-shareextensionability.md)为基类构建分享能力Ability。在Ability被启动后，可以在其[onSessionCreate](../harmonyos-references/js-apis-app-ability-uiextensionability.md#onsessioncreate)回调中获取传入的want参数，将want参数通过[getSharedData](../harmonyos-references/share-system-share.md#getshareddata)解析后得到分享数据。

   ```typescript
   export default class TestShareAbility extends ShareExtensionAbility {
     onSessionCreate(want: Want, session: UIExtensionContentSession) {
       systemShare.getSharedData(want)
         .then((data: systemShare.SharedData) => {
           data.getRecords().forEach((record: systemShare.SharedRecord) => {
             // 处理分享数据
           });
           session.loadContent('pages/Index');
         })
         .catch((error: BusinessError) => {
           console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
           session.terminateSelf();
         });
     }
   }
   ```
3. （可选）社交类应用可通过[意图框架](intents-introduction.md)捐献联系人推荐信息。当用户在推荐区选择联系人进行内容分享时，社交应用注册的Ability可从接收的want数据中获取到联系人信息，直接分享数据到指定用户。

   ```typescript
   export default class TestShareAbility extends ShareExtensionAbility {
     onSessionCreate(want: Want, session: UIExtensionContentSession) {
       systemShare.getContactInfo(want)
         .then(async (contact: systemShare.ContactInfo) => {
           // 处理联系人信息，可通过联系人类型（如：个人，群组等），联系人ID，进行指定用户分享。
           // 获取分享数据
           let data = await systemShare.getSharedData(want);
         })
         .catch((error: BusinessError) => {
           console.error(`Failed to getContactInfo. Code: ${error.code}, message: ${error.message}`);
           // 联系人不存在或数据获取异常
           session.terminateSelf();
         });
     }
   }
   ```
4. 构建完分享能力Ability，需要在应用配置文件（src/main/module.json5）的[skills](module-configuration-file.md#skills标签)配置中注册。配置actions为ohos.want.action.sendData，并且uris需穷举所有支持的数据类型。

   ```json
   "extensionAbilities": [
     {
       "name": "TestShareAbility",
       "srcEntry": "./ets/abilities/TestShareAbility.ts",
       "type": "share", // 支持分享数据处理
       "description": "xxx",
       "exported": true,
       "label": "$string:xx_label",
       "icon": "$media:icon",
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
