---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-data-sync-with-ui
title: UIAbility组件与UI的数据同步
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > UIAbility组件 > UIAbility组件与UI的数据同步
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1c92470bc46ffcd2782e229040d57d3504b84a0db8c6efdde902121952a9fbc
---

基于当前的应用模型，可以通过以下几种方式来实现[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件与UI之间的数据同步。

* [使用EventHub进行数据通信](uiability-data-sync-with-ui.md#使用eventhub进行数据通信)：在[基类Context](../harmonyos-references/js-apis-inner-application-context.md)中提供了[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)对象，可以通过发布订阅方式来实现事件的传递。在事件传递前，订阅者需要先进行订阅，当发布者发布事件时，订阅者将接收到事件并进行相应处理。
* [使用AppStorage/LocalStorage进行数据同步](uiability-data-sync-with-ui.md#使用appstoragelocalstorage进行数据同步)：ArkUI提供了[AppStorage](arkts-appstorage.md)和[LocalStorage](arkts-localstorage.md)两种应用级别的状态管理方案，可用于实现应用级别和UIAbility级别的数据同步。

## 使用EventHub进行数据通信

[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)为[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件提供了事件机制，使它们能够进行订阅、取消订阅和触发事件等数据通信能力。

在[基类Context](../harmonyos-references/js-apis-inner-application-context.md)中，提供了EventHub对象，可用于在UIAbility组件实例内通信。使用EventHub实现UIAbility与UI之间的数据通信需要先获取EventHub对象，本章节将以此为例进行说明。

1. 在UIAbility中调用[eventHub.on()](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhubon)方法注册一个自定义事件“event1”，eventHub.on()有如下两种调用方式，使用其中一种即可。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. // ···

   5. const DOMAIN = 0x0000;
   6. const TAG: string = '[EventAbility]';

   8. export default class EntryAbility extends UIAbility {
   9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   10. // 获取eventHub
   11. let eventhub = this.context.eventHub;
   12. // 执行订阅操作
   13. eventhub.on('event1', this.eventFunc);
   14. eventhub.on('event1', (data: string) => {
   15. // 触发事件，完成相应的业务操作
   16. });
   17. hilog.info(DOMAIN, TAG, '%{public}s', 'Ability onCreate');
   18. }

   20. eventFunc(argOne: object, argTwo: object): void {
   21. hilog.info(DOMAIN, TAG, '1. ' + `${argOne}, ${argTwo}`);
   22. return;
   23. }

   25. // ···
   26. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityDataSync/entry/src/main/ets/entryability/EntryAbility.ets#L16-L87)
2. 在UI中通过[eventHub.emit()](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhubemit)方法触发该事件，在触发事件的同时，根据需要传入参数信息。

   ```
   1. import { common } from '@kit.AbilityKit';

   3. @Entry
   4. @Component
   5. struct EventHubPage {
   6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

   8. eventHubFunc(): void {
   9. // 不带参数触发自定义“event1”事件
   10. this.context.eventHub.emit('event1');
   11. // 带1个参数触发自定义“event1”事件
   12. this.context.eventHub.emit('event1', 1);
   13. // 带2个参数触发自定义“event1”事件
   14. this.context.eventHub.emit('event1', 2, 'test');
   15. // 开发者可以根据实际的业务场景设计事件传递的参数
   16. }

   18. build() {
   19. Column() {
   20. List({ initialIndex: 0 }) {
   21. ListItem() {
   22. Row() {
   23. // ···
   24. }
   25. .onClick(() => {
   26. this.eventHubFunc();
   27. this.getUIContext().getPromptAction().showToast({
   28. message: 'EventHubFuncA'
   29. });
   30. })
   31. // ···
   32. }

   34. ListItem() {
   35. Row() {
   36. // ···
   37. }
   38. .onClick(() => {
   39. this.context.eventHub.off('event1');
   40. this.getUIContext().getPromptAction().showToast({
   41. message: 'EventHubFuncB'
   42. });
   43. })
   44. // ···
   45. }
   46. }
   47. // ···
   48. }
   49. // ···
   50. }
   51. }
   ```

   [EventHubPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityDataSync/entry/src/main/ets/pages/EventHubPage.ets#L16-L95)
3. 在UIAbility的注册事件回调中可以得到对应的触发事件结果，运行日志结果如下所示。

   ```
   1. [Example].[Entry].[EntryAbility] 1. []
   2. [Example].[Entry].[EntryAbility] 1. [1]
   3. [Example].[Entry].[EntryAbility] 1. [2,"test"]
   ```
4. 在自定义事件“event1”使用完成后，可以根据需要调用[eventHub.off()](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhuboff)方法取消该事件的订阅。

   ```
   1. // ···
   2. import { UIAbility } from '@kit.AbilityKit';
   3. // ···

   5. export default class EntryAbility extends UIAbility {
   6. // ···

   8. onDestroy(): void {
   9. this.context.eventHub.off('event1');
   10. }

   12. // ···
   13. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityDataSync/entry/src/main/ets/entryability/EntryAbility.ets#L17-L86)

## 使用AppStorage/LocalStorage进行数据同步

ArkUI提供了[AppStorage](arkts-appstorage.md)和[LocalStorage](arkts-localstorage.md)两种应用级别的状态管理方案，可用于实现应用级别和[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)级别的数据同步。使用这些方案可以方便地管理应用状态，提高应用性能和用户体验。其中，AppStorage是一个全局的状态管理器，适用于多个UIAbility共享同一状态数据的情况；而LocalStorage则是一个局部的状态管理器，适用于单个UIAbility内部使用的状态数据。通过这两种方案，开发者可以更加灵活地控制应用状态，提高应用的可维护性和可扩展性。详细请参见[应用级变量的状态管理](arkts-application-state-management-overview.md)。
