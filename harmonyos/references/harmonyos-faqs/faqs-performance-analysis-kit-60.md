---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-60
title: 如何使用ErrorManager捕获异常
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何使用ErrorManager捕获异常
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fe296d17af274b20e1109a855859a1a92dfac643ec114862b9533fcd0be7c141
---

ErrorManager提供错误观察器的注册和注销。

异常监听（ErrorObserver）接口功能介绍：

| 接口名称 | 说明 |
| --- | --- |
| onUnhandledException(errMsg: string): void | 系统回调接口，应用注册后，当应用产生未捕获的异常时的回调。 |
| onException?(errObject: Error): void | 系统回调接口，应用注册后，当应用产生异常上报JS层时的回调。 |

捕获异常代码参考：

Index.ets中：

```
1. @Entry
2. @Component
3. struct ErrorManagerPage {
4. @State message: string = 'Capture exceptions';

6. build() {
7. Row() {
8. Column() {
9. Button(this.message)
10. .onClick(() => {
11. let tempList = ['0', '1'];
12. tempList[5].toString();
13. })
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

[ErrorManagerPage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/ErrorManagerPage.ets#L21-L39)

EntryAbility.ets中：

```
1. import { AbilityConstant, errorManager, UIAbility, Want } from '@kit.AbilityKit';
2. import { ConfigurationConstant } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';

6. let callback: errorManager.ErrorObserver = {
7. onUnhandledException: (errMsg) => {
8. console.log('Callback when an uncaught exception occurs,onUnhandledException:', errMsg);
9. },
10. onException: (errorObj) => {
11. console.log('The callback when an exception is reported to the JS layer,onException');
12. console.log('onException, name: ', errorObj.name);
13. console.log('onException, message: ', errorObj.message);
14. if (typeof (errorObj.stack) === 'string') {
15. console.log('onException, stack: ', errorObj.stack);
16. }
17. }
18. }

20. let abilityWant: Want;
21. let registerId = -1;
22. const DOMAIN = 0x0000;

24. export default class EntryAbility extends UIAbility {
25. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
26. try {
27. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
28. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
29. console.log('[Demo] EntryAbility onCreate');
30. registerId = errorManager.on('error', callback);
31. abilityWant = want;
32. console.log('registerId:', registerId);
33. } catch (err) {
34. hilog.error(DOMAIN, 'testTag', `setColorMode failed, code is ${err.code}, message is ${err.message}`);
35. }
36. }

38. onDestroy(): void {
39. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
40. console.log('[Demo] EntryAbility onDestroy');
41. errorManager.off('error', registerId, (result) => {
42. console.log(`[Demo] result:${result}`);
43. });
44. }

46. // ...
47. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/entryability/EntryAbility.ets#L19-L95)

**参考链接**

[@ohos.app.ability.errorManager](../harmonyos-references/js-apis-app-ability-errormanager.md)
