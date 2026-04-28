---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-formextensionability
title: 卡片传递消息给应用（message事件）
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > 卡片传递消息给应用（message事件）
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b1dc30e2d07dec0da49f1fad78aa247a7502be1c345604ee36ac7a83e3901865
---

在卡片页面中可以通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口触发message事件拉起[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)，通过[onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent)接口回调通知，以完成点击卡片控件后传递消息给应用的功能，然后由FormExtensionAbility刷新卡片内容，下面是这种刷新方式的简单示例。

说明

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

* 在卡片页面通过注册Button的onClick点击事件回调，并在回调中调用postCardAction接口触发message事件拉起FormExtensionAbility。卡片页面中使用[LocalStorageProp](arkts-localstorage.md#localstorageprop)装饰需要刷新的卡片数据。

  ```
  1. // entry/src/main/ets/updatebymessage/pages/UpdateByMessageCard.ets
  2. let storageUpdateByMsg = new LocalStorage();

  4. @Entry(storageUpdateByMsg)
  5. @Component
  6. struct UpdateByMessageCard {
  7. // $r('app.string.default_title')和$r('app.string.DescriptionDefault')需要替换为开发者所需的资源文件
  8. @LocalStorageProp('title') title: ResourceStr = $r('app.string.default_title');
  9. @LocalStorageProp('detail') detail: ResourceStr = $r('app.string.DescriptionDefault');

  11. build() {
  12. Column() {
  13. Column() {
  14. Text(this.title)
  15. .fontColor('#FFFFFF')
  16. .opacity(0.9)
  17. .fontSize(14)
  18. .margin({ top: '8%', left: '10%' })
  19. Text(this.detail)
  20. .fontColor('#FFFFFF')
  21. .opacity(0.6)
  22. .fontSize(12)
  23. .margin({ top: '5%', left: '10%' })
  24. }.width('100%').height('50%')
  25. .alignItems(HorizontalAlign.Start)

  27. Row() {
  28. // ...
  29. Button() {
  30. // $r('app.string.update')需要替换为开发者所需的资源文件
  31. Text($r('app.string.update'))
  32. .fontColor('#45A6F4')
  33. .fontSize(12)
  34. }
  35. .width(120)
  36. .height(32)
  37. .margin({ top: '30%', bottom: '10%' })
  38. .backgroundColor('#FFFFFF')
  39. .borderRadius(16)
  40. .onClick(() => {
  41. postCardAction(this, {
  42. action: 'message',
  43. params: { msgTest: 'messageEvent' }
  44. });
  45. })
  46. }.width('100%').height('40%')
  47. .justifyContent(FlexAlign.Center)
  48. }
  49. .width('100%')
  50. .height('100%')
  51. .alignItems(HorizontalAlign.Start)
  52. // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
  53. .backgroundImage($r('app.media.CardEvent'))
  54. .backgroundImageSize(ImageSize.Cover)
  55. }
  56. }
  ```
* 在EntryFormAbility.ets中，导入相关模块

  ```
  1. // entry/src/main/ets/entryformability/EntryFormAbility.ts
  2. import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
  3. import { Configuration, Want } from '@kit.AbilityKit';
  4. import { BusinessError } from '@kit.BasicServicesKit';
  5. import { hilog } from '@kit.PerformanceAnalysisKit';
  ```
* 在FormExtensionAbility的onFormEvent生命周期中调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片。

  ```
  1. // entry/src/main/ets/entryformability/EntryFormAbility.ts
  2. const TAG: string = 'EntryFormAbility';
  3. const DOMAIN_NUMBER: number = 0xFF00;

  5. export default class EntryFormAbility extends FormExtensionAbility {
  6. // ...
  7. onFormEvent(formId: string, message: string): void {
  8. // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
  9. hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${message}`);

  11. class FormDataClass {
  12. title: string = 'Title Update.'; // 和卡片布局中对应
  13. detail: string = 'Description update success.'; // 和卡片布局中对应
  14. }

  16. // 请根据业务替换为实际刷新的卡片数据
  17. let formData = new FormDataClass();
  18. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
  19. formProvider.updateForm(formId, formInfo).then(() => {
  20. hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
  21. }).catch((error: BusinessError) => {
  22. hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
  23. });
  24. }

  26. // ...
  27. }
  ```

  运行效果如下图所示。

  | 初始状态 | 点击刷新 |
  | --- | --- |
  |  |  |
