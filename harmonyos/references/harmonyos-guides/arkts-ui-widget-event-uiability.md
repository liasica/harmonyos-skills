---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-uiability
title: 通过router或call事件刷新卡片内容
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > 通过router或call事件刷新卡片内容
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5f91bf097ffead0cb022903ebd61c16293c1ce59a3032c19c353b0180ce79315
---

使用router事件，点击卡片可拉起对应应用的UIAbility至前台，并刷新卡片。使用call事件，点击卡片可拉起对应应用的UIAbility至后台，并刷新卡片。在卡片页面中可以通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口触发router事件或者call事件拉起UIAbility，然后由UIAbility刷新卡片内容，下面是这种刷新方式的简单示例。

说明

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

## 通过router事件刷新卡片内容

* 在卡片页面代码文件中，通过注册Button的onClick点击事件回调并在回调中调用postCardAction接口，触发router事件拉起UIAbility至前台。

  ```
  1. // entry/src/main/ets/widgetupdaterouter/pages/WidgetUpdateRouterCard.ets
  2. let storageUpdateRouter = new LocalStorage();

  4. @Entry(storageUpdateRouter)
  5. @Component
  6. struct WidgetUpdateRouterCard {
  7. // $r('app.string.init')需要替换为开发者所需的资源文件
  8. @LocalStorageProp('routerDetail') routerDetail: ResourceStr = $r('app.string.init');

  10. build() {
  11. Column() {
  12. Column() {
  13. Text(this.routerDetail)
  14. .fontColor('#FFFFFF')
  15. .opacity(0.9)
  16. .fontSize(14)
  17. .margin({ top: '8%', left: '10%', right: '10%' })
  18. .textOverflow({ overflow: TextOverflow.Ellipsis })
  19. .maxLines(2)
  20. }.width('100%').height('50%')
  21. .alignItems(HorizontalAlign.Start)

  23. Row() {
  24. Button() {
  25. // $r('app.string.JumpLabel')需要替换为开发者所需的资源文件
  26. Text($r('app.string.JumpLabel'))
  27. .fontColor('#45A6F4')
  28. .fontSize(12)
  29. }
  30. .width(120)
  31. .height(32)
  32. .margin({ top: '30%', bottom: '10%' })
  33. .backgroundColor('#FFFFFF')
  34. .borderRadius(16)
  35. .onClick(() => {
  36. postCardAction(this, {
  37. action: 'router',
  38. abilityName: 'WidgetEventRouterEntryAbility', // 只能跳转到当前应用下的UIAbility
  39. params: {
  40. routerDetail: 'RouterFromCard',
  41. }
  42. });
  43. })
  44. }.width('100%').height('40%')
  45. .justifyContent(FlexAlign.Center)
  46. }
  47. .width('100%')
  48. .height('100%')
  49. .alignItems(HorizontalAlign.Start)
  50. // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
  51. .backgroundImage($r('app.media.CardEvent'))
  52. .backgroundImageSize(ImageSize.Cover)
  53. }
  54. }
  ```
* 在UIAbility的onCreate或者onNewWant生命周期中可以通过入参want获取卡片的formID和传递过来的参数信息，然后调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片。

  ```
  1. // entry/src/main/ets/widgetevententryability/WidgetEventRouterEntryAbility.ts
  2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  3. import { window } from '@kit.ArkUI';
  4. import { BusinessError } from '@kit.BasicServicesKit';
  5. import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
  6. import { hilog } from '@kit.PerformanceAnalysisKit';

  8. const TAG: string = 'WidgetEventRouterEntryAbility';
  9. const DOMAIN_NUMBER: number = 0xFF00;

  11. export default class WidgetEventRouterEntryAbility extends UIAbility {
  12. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  13. this.handleFormRouterEvent(want, 'onCreate');
  14. }

  16. handleFormRouterEvent(want: Want, source: string): void {
  17. hilog.info(DOMAIN_NUMBER, TAG, `handleFormRouterEvent ${source}, Want: ${JSON.stringify(want)}`);
  18. if (want.parameters && want.parameters[formInfo.FormParam.IDENTITY_KEY] !== undefined) {
  19. let curFormId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
  20. // want.parameters.params 对应 postCardAction() 中 params 内容
  21. let message: string = (JSON.parse(want.parameters?.params as string))?.routerDetail;
  22. hilog.info(DOMAIN_NUMBER, TAG, `UpdateForm formId: ${curFormId}, message: ${message}`);
  23. let formData: Record<string, string> = {
  24. 'routerDetail': message + ' ' + source + ' UIAbility', // 和卡片布局中对应
  25. };
  26. let formMsg = formBindingData.createFormBindingData(formData);
  27. formProvider.updateForm(curFormId, formMsg).then((data) => {
  28. hilog.info(DOMAIN_NUMBER, TAG, 'updateForm success.', JSON.stringify(data));
  29. }).catch((error: BusinessError) => {
  30. hilog.info(DOMAIN_NUMBER, TAG, 'updateForm failed.', JSON.stringify(error));
  31. });
  32. }
  33. }

  35. // 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
  36. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  37. hilog.info(DOMAIN_NUMBER, TAG, 'onNewWant Want:', JSON.stringify(want));
  38. this.handleFormRouterEvent(want, 'onNewWant');
  39. }

  41. onWindowStageCreate(windowStage: window.WindowStage): void {

  43. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');

  45. windowStage.loadContent('pages/Index', (err, data) => {
  46. if (err.code) {
  47. hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
  48. return;
  49. }
  50. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  51. });
  52. }
  53. }
  ```

## 通过call事件刷新卡片内容

* 在卡片页面代码文件中，通过注册Button的onClick点击事件回调并在回调中调用postCardAction接口，触发call事件拉起UIAbility至后台。

  ```
  1. // entry/src/main/ets/widgetupdatecall/pages/WidgetUpdateCallCard.ets
  2. let storageUpdateCall = new LocalStorage();

  4. @Entry(storageUpdateCall)
  5. @Component
  6. struct WidgetUpdateCallCard {
  7. @LocalStorageProp('formId') formId: string = '12400633174999288';
  8. // $r('app.string.init')需要替换为开发者所需的资源文件
  9. @LocalStorageProp('calleeDetail') calleeDetail: ResourceStr = $r('app.string.init');

  11. build() {
  12. Column() {
  13. Column() {
  14. Text(this.calleeDetail)
  15. .fontColor('#FFFFFF')
  16. .opacity(0.9)
  17. .fontSize(14)
  18. .margin({ top: '8%', left: '10%' })
  19. }.width('100%').height('50%')
  20. .alignItems(HorizontalAlign.Start)

  22. Row() {
  23. Button() {
  24. // $r('app.string.CalleeJumpLabel')需要替换为开发者所需的资源文件
  25. Text($r('app.string.CalleeJumpLabel'))
  26. .fontColor('#45A6F4')
  27. .fontSize(12)
  28. }
  29. .width(120)
  30. .height(32)
  31. .margin({ top: '30%', bottom: '10%' })
  32. .backgroundColor('#FFFFFF')
  33. .borderRadius(16)
  34. .onClick(() => {
  35. postCardAction(this, {
  36. action: 'call',
  37. abilityName: 'WidgetCalleeEntryAbility', // 只能拉起当前应用下的UIAbility
  38. params: {
  39. method: 'funA',
  40. formId: this.formId,
  41. calleeDetail: 'CallFrom'
  42. }
  43. });
  44. })
  45. }.width('100%').height('40%')
  46. .justifyContent(FlexAlign.Center)
  47. }
  48. .width('100%')
  49. .height('100%')
  50. .alignItems(HorizontalAlign.Start)
  51. // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
  52. .backgroundImage($r('app.media.CardEvent'))
  53. .backgroundImageSize(ImageSize.Cover)
  54. }
  55. }
  ```
* 在UIAbility的onCreate生命周期中监听call事件所需的方法，然后在对应方法中调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片。

  ```
  1. // entry/src/main/ets/widgetcalleeentryability/WidgetCalleeEntryAbility.ts
  2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  3. import { window } from '@kit.ArkUI';
  4. import { BusinessError } from '@kit.BasicServicesKit';
  5. import { formBindingData, formProvider } from '@kit.FormKit';
  6. import { rpc } from '@kit.IPCKit';
  7. import { hilog } from '@kit.PerformanceAnalysisKit';

  9. const TAG: string = 'WidgetCalleeEntryAbility';
  10. const DOMAIN_NUMBER: number = 0xFF00;
  11. const MSG_SEND_METHOD: string = 'funA';
  12. const CONST_NUMBER_1: number = 1;

  14. class MyParcelable implements rpc.Parcelable {
  15. num: number;
  16. str: string;

  18. constructor(num: number, str: string) {
  19. this.num = num;
  20. this.str = str;
  21. };

  23. marshalling(messageSequence: rpc.MessageSequence): boolean {
  24. messageSequence.writeInt(this.num);
  25. messageSequence.writeString(this.str);
  26. return true;
  27. };

  29. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
  30. this.num = messageSequence.readInt();
  31. this.str = messageSequence.readString();
  32. return true;
  33. };
  34. }

  36. // 在收到call事件后会触发callee监听的方法
  37. let funACall = (data: rpc.MessageSequence): MyParcelable => {
  38. // 获取call事件中传递的所有参数
  39. let params: Record<string, string> = JSON.parse(data.readString());
  40. if (params.formId !== undefined) {
  41. let curFormId: string = params.formId;
  42. let message: string = params.calleeDetail;
  43. hilog.info(DOMAIN_NUMBER, TAG, `UpdateForm formId: ${curFormId}, message: ${message}`);
  44. let formData: Record<string, string> = {
  45. 'calleeDetail': message
  46. };
  47. let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
  48. formProvider.updateForm(curFormId, formMsg).then((data) => {
  49. hilog.info(DOMAIN_NUMBER, TAG, `updateForm success. ${JSON.stringify(data)}`);
  50. }).catch((error: BusinessError) => {
  51. hilog.error(DOMAIN_NUMBER, TAG, `updateForm failed: ${JSON.stringify(error)}`);
  52. });
  53. }
  54. return new MyParcelable(CONST_NUMBER_1, 'aaa');
  55. };

  57. export default class WidgetCalleeEntryAbility extends UIAbility {
  58. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  59. try {
  60. // 监听call事件所需的方法
  61. this.callee.on(MSG_SEND_METHOD, funACall);
  62. } catch (error) {
  63. hilog.error(DOMAIN_NUMBER, TAG, `${MSG_SEND_METHOD} register failed with error ${JSON.stringify(error)}`);
  64. }
  65. }

  67. onWindowStageCreate(windowStage: window.WindowStage): void {
  68. // Main window is created, set main page for this ability
  69. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');

  71. windowStage.loadContent('pages/Index', (err, data) => {
  72. if (err.code) {
  73. hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
  74. return;
  75. }
  76. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  77. });
  78. }
  79. }
  ```

  要拉起UIAbility至后台，需要在module.json5配置文件中，配置ohos.permission.KEEP\_BACKGROUND\_RUNNING权限。

  ```
  1. //src/main/module.json5
  2. "requestPermissions": [
  3. {
  4. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
  5. },
  6. // ···
  7. ]
  ```
