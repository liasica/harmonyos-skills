---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-active-refresh
title: ArkTS卡片主动刷新
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面刷新 > ArkTS卡片主动刷新
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6390687f4245c837b6fc26390c94fed242141783f0f25dcbf7205e6abb1e1619
---

本文主要提供主动刷新的开发指导，刷新流程请参考[主动刷新概述](arkts-ui-widget-interaction-overview.md#主动刷新)。

## 卡片提供方主动刷新卡片内容

卡片提供方可以通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口进行主动刷新。推荐与卡片生命周期回调[onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent)、[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)、[onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)接口搭配使用。

### 开发步骤

下面给出一个示例，实现如下功能：卡片添加至桌面后，点击卡片上的刷新按钮，刷新卡片信息。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 实现卡片布局，在卡片上添加一个刷新按钮，点击按钮后通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口，触发onFormEvent回调。

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
3. 在onFormEvent回调函数的实现中，通过updateForm接口刷新卡片数据。

   ```
   1. // entry/src/main/ets/entryformability/EntryFormAbility.ts
   2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   3. import { Configuration, Want } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';

   8. // entry/src/main/ets/entryformability/EntryFormAbility.ts
   9. const TAG: string = 'EntryFormAbility';
   10. const DOMAIN_NUMBER: number = 0xFF00;

   12. export default class EntryFormAbility extends FormExtensionAbility {
   13. onAddForm(want: Want): formBindingData.FormBindingData {
   14. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAddForm');
   15. hilog.info(DOMAIN_NUMBER, TAG, want.parameters?.[formInfo.FormParam.NAME_KEY] as string);
   16. // 卡片使用方创建卡片时触发，卡片提供方需要返回卡片数据绑定类
   17. let obj: Record<string, string> = {
   18. 'title': 'titleOnAddForm',
   19. 'detail': 'detailOnAddForm'
   20. };
   21. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   22. return formData;
   23. }

   25. onCastToNormalForm(formId: string): void {
   26. // ...
   27. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
   28. }

   30. onUpdateForm(formId: string): void {
   31. // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
   32. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
   33. let obj: Record<string, string> = {
   34. 'title': 'titleOnUpdateForm',
   35. 'detail': 'detailOnUpdateForm'
   36. };
   37. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   38. formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
   39. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
   40. });
   41. }

   43. onChangeFormVisibility(newStatus: Record<string, number>): void {
   44. // ...
   45. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onChangeFormVisibility');
   46. }

   48. onFormEvent(formId: string, message: string): void {
   49. // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
   50. hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${message}`);
   51. class FormDataClass {
   52. title: string = 'Title Update.'; // 和卡片布局中对应
   53. detail: string = 'Description update success.'; // 和卡片布局中对应
   54. }

   56. // 请根据业务替换为实际刷新的卡片数据
   57. let formData = new FormDataClass();
   58. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
   59. formProvider.updateForm(formId, formInfo).then(() => {
   60. hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
   61. }).catch((error: BusinessError) => {
   62. hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
   63. });
   64. }

   66. onRemoveForm(formId: string): void {
   67. // ...
   68. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
   69. // ...
   70. }

   72. onConfigurationUpdate(config: Configuration) {
   73. // ...
   74. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onConfigurationUpdate:' + JSON.stringify(config));
   75. }

   78. onAcquireFormState(want: Want): formInfo.FormState {
   79. // ...
   80. return formInfo.FormState.READY;
   81. }

   83. }
   ```
4. 资源文件如下。

   ```
   1. // entry/src/main/resources/zh_CN/element/string.json
   2. {
   3. "string": [
   4. // ...
   5. {
   6. "name": "default_title",
   7. "value": "Title default."
   8. },
   9. {
   10. "name": "DescriptionDefault",
   11. "value": "Description default."
   12. },
   13. {
   14. "name": "update",
   15. "value": "刷新"
   16. }
   17. ]
   18. }
   ```

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/e1XAKRJLS2yW6rvVzWLrsA/zh-cn_image_0000002552798646.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234128Z&HW-CC-Expire=86400&HW-CC-Sign=C0EBD93FA822DE69F7F587BDBC12448082523D1E333DD835A366138DD0917CC0)

## 卡片提供方批量请求刷新卡片内容

从API version 22开始，支持卡片提供方批量请求刷新卡片内容。卡片提供方可以通过[reloadForms](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderreloadforms22)和[reloadAllForms](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderreloadallforms22)接口在应用主进程中通知FormExtension进程进行批量更新，仅支持在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)中调用。

### 开发步骤

下面给出一个示例，实现如下功能：添加应用的多张卡片至桌面后，点击应用UIAbility中的刷新按钮，批量刷新卡片信息。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 实现卡片布局，在卡片上创建两个待刷新的Text。

   ```
   1. // entry/src/main/ets/reloadbyuiability/pages/ReloadByUIAbilityCard.ets
   2. let storageReloadForm = new LocalStorage();

   4. @Entry(storageReloadForm)
   5. @Component
   6. struct ReloadByUIAbilityCard {
   7. // 创建两个待刷新的Text，Text初始内容分别为'Title default'、'Description default'。资源文件定义请参见下方步骤5
   8. @LocalStorageProp('title') title: ResourceStr = $r('app.string.default_title');
   9. @LocalStorageProp('detail') detail: ResourceStr = $r('app.string.DescriptionDefault');

   11. build() {
   12. Column() {
   13. Column() {
   14. Text(this.title)
   15. .fontSize(14)
   16. .margin({ top: '8%', left: '10%' })
   17. Text(this.detail)
   18. .fontSize(12)
   19. .margin({ top: '5%', left: '10%' })
   20. }.width('100%').height('50%')
   21. .alignItems(HorizontalAlign.Start)
   22. }
   23. .width('100%')
   24. .height('100%')
   25. .alignItems(HorizontalAlign.Start)
   26. }
   27. }
   ```
3. 在FormExtensionAbility中实现onUpdateForm回调，通过updateForm接口定义卡片刷新逻辑。

   ```
   1. // entry/src/main/ets/entryformability/EntryFormAbility.ets
   2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   3. import { Want } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';

   7. const TAG: string = 'EntryFormAbility';
   8. const DOMAIN_NUMBER: number = 0xFF00;

   10. export default class EntryFormAbility extends FormExtensionAbility {
   11. onAddForm(want: Want) {
   12. const formData = '';
   13. return formBindingData.createFormBindingData(formData);
   14. }

   16. onCastToNormalForm(formId: string): void {
   17. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
   18. }

   20. onUpdateForm(formId: string) {

   22. class FormDataClass {
   23. title: string = 'Title: ' + Math.random();
   24. detail: string = 'Description: ' + Math.random();
   25. }

   27. let formData = new FormDataClass();
   28. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
   29. formProvider.updateForm(formId, formInfo).then(() => {
   30. hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
   31. }).catch((error: BusinessError) => {
   32. hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. code: ${error.code}, message: ${error.message}`);
   33. });
   34. }

   36. onFormEvent(formId: string, message: string) {
   37. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onFormEvent');
   38. }

   40. onRemoveForm(formId: string) {
   41. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
   42. }

   44. onAcquireFormState(want: Want) {
   45. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAcquireFormState');
   46. return formInfo.FormState.READY;
   47. }
   48. }
   ```
4. 在UIAbility的界面中添加两个批量刷新按钮，点击按钮后通过reloadForms或reloadAllForms接口，批量触发FormExtensionAbility中的onUpdateForm回调。

   ```
   1. // entry/src/main/ets/pages/index.ets
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { formProvider } from '@kit.FormKit';

   6. @Entry
   7. @Component
   8. struct Index {
   9. build() {
   10. Column({ space: 20 }) {
   11. Button('reloadForms')
   12. .onClick(() => {
   13. try {
   14. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   15. let moduleName: string = 'entry';
   16. let abilityName: string = 'EntryFormAbility';
   17. let formName: string = 'reloadByUIAbilityCard';
   18. formProvider.reloadForms(context, moduleName, abilityName, formName).then((reloadNum: number) => {
   19. console.info(`reloadForms success, reload number: ${reloadNum}`);
   20. }).catch((error: BusinessError) => {
   21. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
   22. });
   23. } catch (error) {
   24. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
   25. }
   26. })
   27. Button('reloadAllForms')
   28. .onClick(() => {
   29. try {
   30. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   31. formProvider.reloadAllForms(context).then((reloadNum: number) => {
   32. console.info(`reloadAllForms success, reload number: ${reloadNum}`);
   33. }).catch((error: BusinessError) => {
   34. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
   35. });
   36. } catch (error) {
   37. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
   38. }
   39. })
   40. }
   41. .height('100%')
   42. .width('100%')
   43. .justifyContent(FlexAlign.Center)
   44. }
   45. }
   ```
5. 资源文件如下。

   ```
   1. // entry/src/main/resources/base/element/string.json
   2. {
   3. "string": [
   4. // ...
   5. {
   6. "name": "default_title",
   7. "value": "Title default."
   8. },
   9. {
   10. "name": "DescriptionDefault",
   11. "value": "Description default."
   12. }
   13. ]
   14. }
   ```

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/A7zg9DhmSBCKcgtU3othXA/zh-cn_image_0000002583438341.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234128Z&HW-CC-Expire=86400&HW-CC-Sign=B3A6C26CC3E1D95F9682B7E93B60C4A50EA49F00739824A89FC145A1F16E5F3F)
