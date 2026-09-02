---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-formextensionability
title: 卡片传递消息给应用（message事件）
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > 卡片传递消息给应用（message事件）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c698210971133b982c7068ed78a8ac42ac4870115ecb3a8cc5bbad932b4cc0cd
---

在卡片页面中可以通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口触发message事件拉起[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)，通过[onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent)接口回调通知，以完成点击卡片控件后传递消息给应用的功能，然后由FormExtensionAbility刷新卡片内容，下面是这种刷新方式的简单示例。

**说明** 

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

* 在卡片页面通过注册Button的onClick点击事件回调，并在回调中调用postCardAction接口触发message事件拉起FormExtensionAbility。卡片页面中使用[LocalStorageProp](arkts-localstorage.md#localstorageprop)装饰需要刷新的卡片数据。

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
* 在EntryFormAbility.ets中，导入相关模块

  ```typescript
  // entry/src/main/ets/entryformability/EntryFormAbility.ts
  import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
  import { Configuration, Want } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  ```
* 在FormExtensionAbility的onFormEvent生命周期中调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片。

  ```typescript
  // entry/src/main/ets/entryformability/EntryFormAbility.ts
  const TAG: string = 'EntryFormAbility';
  const DOMAIN_NUMBER: number = 0xFF00;

  export default class EntryFormAbility extends FormExtensionAbility {
    // ...
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

    // ...
  }
  ```

  运行效果如下图所示。

  | 初始状态 | 点击刷新 |
  | --- | --- |
  |  |  |
