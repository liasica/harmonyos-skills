---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-call
title: 卡片拉起应用UIAbility到后台（call事件）
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > 卡片拉起应用UIAbility到后台（call事件）
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2d5d3f424c6c5e98755ffa9fdaba12619c20547bb8be39781a90dab4c6d654c
---

许多应用希望借助卡片的能力，实现和应用在前台时相同的功能。例如音乐卡片，卡片上提供播放、暂停等按钮，点击不同按钮将触发音乐应用的不同功能，进而提高用户的体验。在卡片中使用[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口的call能力，能够将卡片提供方应用的指定的UIAbility拉到后台。同时，call能力提供了调用应用指定方法、传递数据的功能，使应用在后台运行时可以通过卡片上的按钮执行不同的功能。

说明

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

## 开发步骤

1. 创建动态卡片

   新建一个名为WidgetEventCall的ArkTs动态卡片。
2. 页面布局代码实现

   在卡片页面中布局两个按钮，点击按钮A或按钮B，会调用postCardAction向指定UIAbility发送call事件，在call事件内定义了需要调用的方法。按钮A和按钮B分别对应调用funA、funB方法，其中funA携带了formID参数，funB携带了formID和num参数，开发过程中请根据实际需要传参。postCardAction中的method参数为必填参数，用于标识需要调用的方法名称，与步骤3中UIAbility监听的方法一致，其他参数为非必填。

   ```
   1. //src/main/ets/widgeteventcall/pages/WidgetEventCallCard.ets
   2. let storageEventCall = new LocalStorage();

   4. @Entry(storageEventCall)
   5. @Component
   6. struct WidgetEventCallCard {
   7. @LocalStorageProp('formId') formId: string = '12400633174999288';
   8. // $r('app.string.ButtonA_label')和$r('app.string.ButtonB_label')需要替换为开发者所需的资源文件
   9. private funA: Resource = $r('app.string.ButtonA_label');
   10. private funB: Resource = $r('app.string.ButtonB_label');

   12. build() {
   13. RelativeContainer() {
   14. Button(this.funA)
   15. .id('funA__')
   16. .fontSize(14)
   17. .fontWeight(FontWeight.Bold)
   18. .alignRules({
   19. center: { anchor: '__container__', align: VerticalAlign.Center },
   20. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   21. })
   22. .onClick(() => {
   23. postCardAction(this, {
   24. action: 'call',
   25. // 只能跳转到当前应用下的UIAbility，与module.json5中定义保持一致
   26. abilityName: 'WidgetEventCallEntryAbility',
   27. params: {
   28. formId: this.formId,
   29. // 需要调用的方法名称
   30. method: 'funA'
   31. }
   32. });
   33. })

   35. Button(this.funB)
   36. .id('funB__')
   37. .fontSize(14)
   38. .fontWeight(FontWeight.Bold)
   39. .margin({ top: 10 })
   40. .alignRules({
   41. top: { anchor: 'funA__', align: VerticalAlign.Bottom },
   42. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   43. })
   44. .onClick(() => {
   45. postCardAction(this, {
   46. action: 'call',
   47. abilityName: 'WidgetEventCallEntryAbility',
   48. params: {
   49. formId: this.formId,
   50. // 需要调用的方法名称
   51. method: 'funB',
   52. num: 1
   53. }
   54. });
   55. })
   56. }
   57. .height('100%')
   58. .width('100%')
   59. }
   60. }
   ```
3. 创建指定的UIAbility

   在UIAbility中监听call事件，根据监听到的method参数中的方法名称调用对应方法，并通过[rpc.Parcelable](../harmonyos-references/js-apis-rpc.md#parcelable9)获取参数。UIAbility中监听的方法与步骤2中调用的方法需保持一致。

   ```
   1. //src/main/ets/WidgetEventCallEntryAbility/WidgetEventCallEntryAbility.ets
   2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { rpc } from '@kit.IPCKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';

   7. const TAG: string = 'WidgetEventCallEntryAbility';
   8. const DOMAIN_NUMBER: number = 0xFF00;
   9. const CONST_NUMBER_1: number = 1;
   10. const CONST_NUMBER_2: number = 2;

   12. // ipc通信返回类型的实现，用于数据序列化和反序列化
   13. class MyParcelable implements rpc.Parcelable {
   14. private num: number;
   15. private str: string;

   17. constructor(num: number, str: string) {
   18. this.num = num;
   19. this.str = str;
   20. }

   22. marshalling(messageSequence: rpc.MessageSequence): boolean {
   23. messageSequence.writeInt(this.num);
   24. messageSequence.writeString(this.str);
   25. return true;
   26. }

   28. unmarshalling(messageSequence: rpc.MessageSequence): boolean {
   29. this.num = messageSequence.readInt();
   30. this.str = messageSequence.readString();
   31. return true;
   32. }
   33. }

   35. export default class WidgetEventCallEntryAbility extends UIAbility {
   36. // 如果UIAbility启动，在收到call事件后会触发onCreate生命周期回调
   37. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   38. try {
   39. // 监听call事件所需的方法并调用
   40. this.callee.on('funA', (data: rpc.MessageSequence) => {
   41. // 获取call事件中传递的所有参数
   42. hilog.info(DOMAIN_NUMBER, TAG, `FunACall param:  ${JSON.stringify(data.readString())}`);
   43. return new MyParcelable(CONST_NUMBER_1, 'aaa');
   44. });
   45. this.callee.on('funB', (data: rpc.MessageSequence) => {
   46. // 获取call事件中传递的所有参数
   47. hilog.info(DOMAIN_NUMBER, TAG, `FunBCall param:  ${JSON.stringify(data.readString())}`);
   48. return new MyParcelable(CONST_NUMBER_2, 'bbb');
   49. });
   50. } catch (err) {
   51. hilog.error(DOMAIN_NUMBER, TAG, `Failed to register callee on. Cause: ${JSON.stringify(err as BusinessError)}`);
   52. }
   53. }

   55. // 进程退出时，解除监听
   56. onDestroy(): void | Promise<void> {
   57. try {
   58. this.callee.off('funA');
   59. this.callee.off('funB');
   60. } catch (err) {
   61. hilog.error(DOMAIN_NUMBER, TAG, `Failed to register callee off. Cause: ${JSON.stringify(err as BusinessError)}`);
   62. }
   63. }
   64. }
   ```
4. 配置后台运行权限

   call事件存在约束限制，卡片提供方应用需要在module.json5下添加后台运行权限([ohos.permission.KEEP\_BACKGROUND\_RUNNING](permissions-for-all.md#ohospermissionkeep_background_running))。

   ```
   1. //src/main/module.json5
   2. "requestPermissions": [
   3. {
   4. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
   5. },
   6. // ···
   7. // [EndExclude jscard_extension_ability]
   8. ]
   ```
5. 配置指定的UIAbility

   在module.json5的abilities数组内添加WidgetEventCallEntryAbility对应的配置信息。

   ```
   1. //src/main/module.json5
   2. "abilities": [
   3. // ···
   4. {
   5. "name": "WidgetEventCallEntryAbility",
   6. "srcEntry": "./ets/widgeteventcallentryability/WidgetEventCallEntryAbility.ets",
   7. "description": "$string:WidgetEventCallEntryAbility_desc",
   8. "icon": "$media:icon",
   9. "label": "$string:WidgetEventCallEntryAbility_label",
   10. "startWindowIcon": "$media:icon",
   11. "startWindowBackground": "$color:start_window_background"
   12. }
   13. ],
   ```
