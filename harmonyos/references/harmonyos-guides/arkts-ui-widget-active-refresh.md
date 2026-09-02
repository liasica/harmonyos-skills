---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-active-refresh
title: ArkTS卡片主动刷新
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面刷新 > ArkTS卡片主动刷新
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bfea973d3488d650ad23246d72ca50ba0cbcfafc25a2f3deee6706a7f0eb76bc
---

本文主要提供主动刷新的开发指导，刷新流程请参考[主动刷新概述](arkts-ui-widget-interaction-overview.md#主动刷新)。

## 卡片提供方主动刷新卡片内容

卡片提供方可以通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口进行主动刷新。推荐与卡片生命周期回调[onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent)、[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)、[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)接口搭配使用。

### 开发步骤

下面给出一个示例，实现如下功能：卡片添加至桌面后，点击卡片上的刷新按钮，刷新卡片信息。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 实现卡片布局，在卡片上添加一个刷新按钮，点击按钮后通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口，触发onFormEvent回调。

   ```typescript
   // entry/src/main/ets/updatebymessage/pages/UpdateByMessageCard.ets
   let storageUpdateByMsg = new LocalStorage();

   @Entry(storageUpdateByMsg)
   @Component
   struct UpdateByMessageCard {
     // $r('app.string.default_title')和$r('app.string.DescriptionDefault')需要替换为开发者所需的资源文件
     @LocalStorageProp('title') title: ResourceStr = $r('app.string.default_title');
     @LocalStorageProp('detail') detail: ResourceStr = $r('app.string.DescriptionDefault');

     build() {
       Column() {
         Column() {
           Text(this.title)
             .fontColor('#FFFFFF')
             .opacity(0.9)
             .fontSize(14)
             .margin({ top: '8%', left: '10%' })
           Text(this.detail)
             .fontColor('#FFFFFF')
             .opacity(0.6)
             .fontSize(12)
             .margin({ top: '5%', left: '10%' })
         }.width('100%').height('50%')
         .alignItems(HorizontalAlign.Start)

         Row() {
           // ...
           Button() {
             // $r('app.string.update')需要替换为开发者所需的资源文件
             Text($r('app.string.update'))
               .fontColor('#45A6F4')
               .fontSize(12)
           }
           .width(120)
           .height(32)
           .margin({ top: '30%', bottom: '10%' })
           .backgroundColor('#FFFFFF')
           .borderRadius(16)
           .onClick(() => {
             postCardAction(this, {
               action: 'message',
               params: { msgTest: 'messageEvent' }
             });
           })
         }.width('100%').height('40%')
         .justifyContent(FlexAlign.Center)
       }
       .width('100%')
       .height('100%')
       .alignItems(HorizontalAlign.Start)
       // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
       .backgroundImage($r('app.media.CardEvent'))
       .backgroundImageSize(ImageSize.Cover)
     }
   }
   ```
3. 在onFormEvent回调函数的实现中，通过updateForm接口刷新卡片数据。

   ```typescript
   // entry/src/main/ets/entryformability/EntryFormAbility.ts
   import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   import { Configuration, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   // entry/src/main/ets/entryformability/EntryFormAbility.ts
   const TAG: string = 'EntryFormAbility';
   const DOMAIN_NUMBER: number = 0xFF00;

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want): formBindingData.FormBindingData {
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAddForm');
       hilog.info(DOMAIN_NUMBER, TAG, want.parameters?.[formInfo.FormParam.NAME_KEY] as string);
       // 卡片使用方创建卡片时触发，卡片提供方需要返回卡片数据绑定类
       let obj: Record<string, string> = {
         'title': 'titleOnAddForm',
         'detail': 'detailOnAddForm'
       };
       let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
       return formData;
     }

     onCastToNormalForm(formId: string): void {
       // ...
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
     }

     onUpdateForm(formId: string): void {
       // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
       let obj: Record<string, string> = {
         'title': 'titleOnUpdateForm',
         'detail': 'detailOnUpdateForm'
       };
       let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
       formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
         hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
       });
     }

     onChangeFormVisibility(newStatus: Record<string, number>): void {
       // ...
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onChangeFormVisibility');
     }

     onFormEvent(formId: string, message: string): void {
       // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
       hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${message}`);
       class FormDataClass {
         title: string = 'Title Update.'; // 和卡片布局中对应
         detail: string = 'Description update success.'; // 和卡片布局中对应
       }

       // 请根据业务替换为实际刷新的卡片数据
       let formData = new FormDataClass();
       let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
       formProvider.updateForm(formId, formInfo).then(() => {
         hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
       }).catch((error: BusinessError) => {
         hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
       });
     }

     onRemoveForm(formId: string): void {
       // ...
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
       // ...
     }

     onConfigurationUpdate(config: Configuration) {
       // ...
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onConfigurationUpdate:' + JSON.stringify(config));
     }

     onAcquireFormState(want: Want): formInfo.FormState {
       // ...
       return formInfo.FormState.READY;
     }

   }
   ```
4. 资源文件如下。

   ```ts
   // entry/src/main/resources/zh_CN/element/string.json
   {
      "string": [
      // ...
        {
          "name": "default_title",
          "value": "Title default."
        },
        {
          "name": "DescriptionDefault",
          "value": "Description default."
        },
        {
          "name": "update",
          "value": "刷新"
        }
      ]
   }
   ```

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/id6_2u6QQMan5FYONXlGkA/zh-cn_image_0000002706674218.gif)

## 卡片提供方批量请求刷新卡片内容

从API version 22开始，支持卡片提供方批量请求刷新卡片内容。卡片提供方可以通过[reloadForms](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderreloadforms22)和[reloadAllForms](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderreloadallforms22)接口在应用主进程中通知FormExtension进程进行批量更新，仅支持在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)中调用。

### 开发步骤

下面给出一个示例，实现如下功能：添加应用的多张卡片至桌面后，点击应用UIAbility中的刷新按钮，批量刷新卡片信息。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 实现卡片布局，在卡片上创建两个待刷新的Text。

   ```typescript
   // entry/src/main/ets/reloadbyuiability/pages/ReloadByUIAbilityCard.ets
   let storageReloadForm = new LocalStorage();

   @Entry(storageReloadForm)
   @Component
   struct ReloadByUIAbilityCard {
     // 创建两个待刷新的Text，Text初始内容分别为'Title default'、'Description default'。资源文件定义请参见下方步骤5
     @LocalStorageProp('title') title: ResourceStr = $r('app.string.default_title');
     @LocalStorageProp('detail') detail: ResourceStr = $r('app.string.DescriptionDefault');

     build() {
       Column() {
         Column() {
           Text(this.title)
             .fontSize(14)
             .margin({ top: '8%', left: '10%' })
           Text(this.detail)
             .fontSize(12)
             .margin({ top: '5%', left: '10%' })
         }.width('100%').height('50%')
         .alignItems(HorizontalAlign.Start)
       }
       .width('100%')
       .height('100%')
       .alignItems(HorizontalAlign.Start)
     }
   }
   ```
3. 在FormExtensionAbility中实现onUpdateForm回调，通过updateForm接口定义卡片刷新逻辑。

   ```typescript
   // entry/src/main/ets/entryformability/EntryFormAbility.ets
   import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = 'EntryFormAbility';
   const DOMAIN_NUMBER: number = 0xFF00;

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       const formData = '';
       return formBindingData.createFormBindingData(formData);
     }

     onCastToNormalForm(formId: string): void {
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
     }

     onUpdateForm(formId: string) {

       class FormDataClass {
         title: string = 'Title: ' + Math.random();
         detail: string = 'Description: ' + Math.random();
       }

       let formData = new FormDataClass();
       let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
       // 更新卡片数据
       formProvider.updateForm(formId, formInfo).then(() => {
         hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
       }).catch((error: BusinessError) => {
         hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. code: ${error.code}, message: ${error.message}`);
       });
     }

     onFormEvent(formId: string, message: string) {
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
     }

     onRemoveForm(formId: string) {
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
     }

     onAcquireFormState(want: Want) {
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAcquireFormState');
       return formInfo.FormState.READY;
     }
   }
   ```
4. 在UIAbility的界面中添加两个批量刷新按钮，点击按钮后通过reloadForms或reloadAllForms接口，批量触发FormExtensionAbility中的onUpdateForm回调。

   ```typescript
   // entry/src/main/ets/pages/index.ets
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { formProvider } from '@kit.FormKit';

   @Entry
   @Component
   struct Index {
     build() {
       Column({ space: 20 }) {
         Button('reloadForms')
           .onClick(() => {
             try {
               let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let moduleName: string = 'entry';
               let abilityName: string = 'EntryFormAbility';
               let formName: string = 'ReloadByUIAbility';
               formProvider.reloadForms(context, moduleName, abilityName, formName).then((reloadNum: number) => {
                 console.info(`reloadForms success, reload number: ${reloadNum}`);
               }).catch((error: BusinessError) => {
                 console.error(`promise error, code: ${error.code}, message: ${error.message}`);
               });
             } catch (error) {
               console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
             }
           })
         Button('reloadAllForms')
           .onClick(() => {
             try {
               let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
               formProvider.reloadAllForms(context).then((reloadNum: number) => {
                 console.info(`reloadAllForms success, reload number: ${reloadNum}`);
               }).catch((error: BusinessError) => {
                 console.error(`promise error, code: ${error.code}, message: ${error.message}`);
               });
             } catch (error) {
               console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
             }
           })
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center)
     }
   }
   ```
5. 资源文件如下。

   ```json5
   // entry/src/main/resources/base/element/string.json
   {
      "string": [
      // ...
        {
          "name": "default_title",
          "value": "Title default."
        },
        {
          "name": "DescriptionDefault",
          "value": "Description default."
        }
      ]
   }
   ```

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Sepie67hTQSFaexrslwzVg/zh-cn_image_0000002736433309.gif)
