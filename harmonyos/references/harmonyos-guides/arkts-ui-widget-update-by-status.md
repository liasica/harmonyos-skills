---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-update-by-status
title: 根据卡片状态刷新不同内容
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面刷新 > 根据卡片状态刷新不同内容
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:30+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:1219e62964ced7df61efdd222bd1355769c32e53a205e06d91e97f900ab7c554
---

相同的卡片可以添加到桌面上实现不同的功能，比如添加两张桌面的卡片，一张显示杭州的天气，一张显示北京的天气，设置每天早上7点触发定时刷新，卡片需要感知当前的配置是杭州还是北京，然后将对应城市的天气信息刷新到卡片上，以下示例介绍了如何根据卡片的状态动态选择需要刷新的内容。

* 卡片配置文件：配置每隔30分钟自动刷新。

  ```
  1. {
  2. "forms": [
  3. {
  4. "name": "WidgetUpdateByStatus",
  5. "description": "$string:UpdateByStatusFormAbility_desc",
  6. "src": "./ets/widgetupdatebystatus/pages/WidgetUpdateByStatusCard.ets",
  7. "uiSyntax": "arkts",
  8. "window": {
  9. "designWidth": 720,
  10. "autoDesignWidth": true
  11. },
  12. "isDefault": true,
  13. "updateEnabled": true,
  14. "scheduledUpdateTime": "10:30",
  15. "updateDuration": 1,
  16. "defaultDimension": "2*2",
  17. "supportDimensions": [
  18. "2*2"
  19. ]
  20. }
  21. ]
  22. }
  ```
* 卡片页面：卡片具备不同的状态选择，在不同的状态下需要刷新不同的内容，因此在状态发生变化时通过postCardAction通知EntryFormAbility。

  ```
  1. // entry/src/main/ets/widgetupdatebystatus/pages/WidgetUpdateByStatusCard.ets
  2. let storageUpdateByStatus = new LocalStorage();

  4. @Entry(storageUpdateByStatus)
  5. @Component
  6. struct WidgetUpdateByStatusCard {
  7. // $r('app.string.to_be_refreshed')需要替换为开发者所需的资源文件
  8. @LocalStorageProp('textA') textA: Resource = $r('app.string.to_be_refreshed');
  9. @LocalStorageProp('textB') textB: Resource = $r('app.string.to_be_refreshed');
  10. @State selectA: boolean = false;
  11. @State selectB: boolean = false;

  13. build() {
  14. Column() {
  15. Column() {
  16. Row() {
  17. Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
  18. .padding(0)
  19. .select(false)
  20. .margin({ left: 26 })
  21. .onChange((value: boolean) => {
  22. this.selectA = value;
  23. postCardAction(this, {
  24. action: 'message',
  25. params: {
  26. selectA: JSON.stringify(value)
  27. }
  28. });
  29. })
  30. // $r('app.string.status_a')需要替换为开发者所需的资源文件
  31. Text($r('app.string.status_a'))
  32. .fontColor('#000000')
  33. .opacity(0.9)
  34. .fontSize(14)
  35. .margin({ left: 8 })
  36. }
  37. .width('100%')
  38. .padding(0)
  39. .justifyContent(FlexAlign.Start)

  41. Row() {
  42. Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
  43. .padding(0)
  44. .select(false)
  45. .margin({ left: 26 })
  46. .onChange((value: boolean) => {
  47. this.selectB = value;
  48. postCardAction(this, {
  49. action: 'message',
  50. params: {
  51. selectB: JSON.stringify(value)
  52. }
  53. });
  54. })
  55. // $r('app.string.status_b')需要替换为开发者所需的资源文件
  56. Text($r('app.string.status_b'))
  57. .fontColor('#000000')
  58. .opacity(0.9)
  59. .fontSize(14)
  60. .margin({ left: 8 })
  61. }
  62. .width('100%')
  63. .position({ y: 32 })
  64. .padding(0)
  65. .justifyContent(FlexAlign.Start)
  66. }
  67. .position({ y: 12 })

  69. Column() {
  70. Row() {
  71. // 选中状态A才会进行刷新的内容
  72. Text($r('app.string.status_a'))
  73. .fontColor('#000000')
  74. .opacity(0.4)
  75. .fontSize(12)

  77. Text(this.textA)
  78. .fontColor('#000000')
  79. .opacity(0.4)
  80. .fontSize(12)
  81. }
  82. .margin({ top: '12px', left: 26, right: '26px' })

  84. Row() {
  85. // 选中状态B才会进行刷新的内容
  86. Text($r('app.string.status_b'))
  87. .fontColor('#000000')
  88. .opacity(0.4)
  89. .fontSize(12)
  90. Text(this.textB)
  91. .fontColor('#000000')
  92. .opacity(0.4)
  93. .fontSize(12)
  94. }
  95. .margin({
  96. top: '12px',
  97. bottom: '21px',
  98. left: 26,
  99. right: '26px'
  100. })
  101. }
  102. .margin({ top: 80 })
  103. .width('100%')
  104. .alignItems(HorizontalAlign.Start)
  105. }.width('100%').height('100%')
  106. // $r('app.media.CardUpdateByStatus')需要替换为开发者所需的资源文件
  107. .backgroundImage($r('app.media.CardUpdateByStatus'))
  108. .backgroundImageSize(ImageSize.Cover)
  109. }
  110. }
  ```
* EntryFormAbility：将卡片的状态存储在本地数据库中，在刷新事件回调触发时，通过formId获取当前卡片的状态，然后根据卡片的状态选择不同的刷新内容。

  ```
  1. // entry/src/main/ets/updatebystatusformability/UpdateByStatusFormAbility.ts
  2. import { Want } from '@kit.AbilityKit';
  3. import { preferences } from '@kit.ArkData';
  4. import { BusinessError } from '@kit.BasicServicesKit';
  5. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
  6. import { hilog } from '@kit.PerformanceAnalysisKit';

  8. const TAG: string = 'UpdateByStatusFormAbility';
  9. const DOMAIN_NUMBER: number = 0xFF00;

  11. export default class UpdateByStatusFormAbility extends FormExtensionAbility {
  12. onAddForm(want: Want): formBindingData.FormBindingData {
  13. let formId: string = '';
  14. if (want.parameters) {
  15. formId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
  16. let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
  17. promise.then(async (storeDB: preferences.Preferences) => {
  18. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
  19. await storeDB.put('A' + formId, 'false');
  20. await storeDB.put('B' + formId, 'false');
  21. await storeDB.flush();
  22. }).catch((err: BusinessError) => {
  23. hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
  24. });
  25. }
  26. let formData: Record<string, Object | string> = {};
  27. return formBindingData.createFormBindingData(formData);
  28. }

  30. onRemoveForm(formId: string): void {
  31. hilog.info(DOMAIN_NUMBER, TAG, 'onRemoveForm, formId:' + formId);
  32. let promise = preferences.getPreferences(this.context, 'myStore');
  33. promise.then(async (storeDB) => {
  34. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
  35. await storeDB.delete('A' + formId);
  36. await storeDB.delete('B' + formId);
  37. }).catch((err: BusinessError) => {
  38. hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
  39. });
  40. }

  42. // 当前卡片使用方不会涉及该场景，无需实现该回调函数
  43. onCastToNormalForm(formId: string): void {
  44. }

  46. onUpdateForm(formId: string): void {
  47. let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
  48. promise.then(async (storeDB: preferences.Preferences) => {
  49. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences from onUpdateForm.');
  50. let stateA = await storeDB.get('A' + formId, 'false');
  51. let stateB = await storeDB.get('B' + formId, 'false');
  52. // A状态选中则更新textA
  53. if (stateA === 'true') {
  54. let param: Record<string, string> = {
  55. 'textA': 'AAA'
  56. };
  57. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
  58. await formProvider.updateForm(formId, formInfo);
  59. }
  60. // B状态选中则更新textB
  61. if (stateB === 'true') {
  62. let param: Record<string, string> = {
  63. 'textB': 'BBB'
  64. };
  65. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
  66. await formProvider.updateForm(formId, formInfo);
  67. }
  68. hilog.info(DOMAIN_NUMBER, TAG, `Update form success stateA:${stateA} stateB:${stateB}.`);
  69. }).catch((err: BusinessError) => {
  70. hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
  71. });
  72. }

  74. onFormEvent(formId: string, message: string): void {
  75. // 存放卡片状态
  76. hilog.info(DOMAIN_NUMBER, TAG, 'onFormEvent formId:' + formId + 'msg:' + message);
  77. let promise: Promise<preferences.Preferences> = preferences.getPreferences(this.context, 'myStore');
  78. promise.then(async (storeDB: preferences.Preferences) => {
  79. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded to get preferences.');
  80. let msg: Record<string, string> = JSON.parse(message);
  81. if (msg.selectA !== undefined) {
  82. hilog.info(DOMAIN_NUMBER, TAG, 'onFormEvent selectA info:' + msg.selectA);
  83. await storeDB.put('A' + formId, msg.selectA);
  84. }
  85. if (msg.selectB !== undefined) {
  86. hilog.info(DOMAIN_NUMBER, TAG, 'onFormEvent selectB info:' + msg.selectB);
  87. await storeDB.put('B' + formId, msg.selectB);
  88. }
  89. await storeDB.flush();
  90. }).catch((err: BusinessError) => {
  91. hilog.info(DOMAIN_NUMBER, TAG, `Failed to get preferences. ${JSON.stringify(err)}`);
  92. });
  93. }
  94. }
  ```

说明

通过本地数据库进行卡片信息的持久化时，建议先在[**onAddForm**](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)生命周期进行卡片信息持久化；同时需要在卡片销毁(**[onRemoveForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonremoveform)**)时删除当前卡片存储的持久化信息，避免反复添加删除卡片导致数据库文件持续变大。
