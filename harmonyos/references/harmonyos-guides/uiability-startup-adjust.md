---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-startup-adjust
title: 显式Want跳转切换应用链接跳转适配指导
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定应用 > 显式Want跳转切换应用链接跳转适配指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:384188d309339fbb169f2636f49f19c240ab0aad9bc0d9bf373f8dcce61aaf13
---

从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定[应用链接](app-startup-overview.md#应用链接)的方式来实现。

本章节介绍如何从显式Want跳转切换到应用链接跳转。

## 启动其他应用的UIAbility

1. 将待跳转的应用安装到设备，在其对应UIAbility的[module.json5配置文件](module-configuration-file.md)中配置skills标签的entities字段、actions字段和uri字段：

   * "actions"列表中包含"ohos.want.action.viewData"。
   * "entities"列表中包含"entity.system.browsable"。
   * "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。uri的匹配规则参考[uri匹配](explicit-implicit-want-mappings.md#uri匹配规则)，domainVerify为true代表开启域名检查，通过App Linking匹配该应用时需经过配置的域名校验后才能匹配到。

   ```
   1. {
   2. "module": {
   3. // ···
   4. "abilities": [
   5. // ···
   6. {
   7. // ···
   8. "skills": [
   9. {
   10. "entities": [
   11. "entity.system.browsable"
   12. ],
   13. "actions": [
   14. "ohos.want.action.viewData"
   15. ],
   16. "uris": [
   17. {
   18. "scheme": "https",
   19. "host": "www.example.com"
   20. }
   21. ],
   22. "domainVerify": true
   23. }
   24. ]
   25. },
   26. // ···
   27. ],
   28. // ···
   29. }
   30. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/module.json5#L16-L354)
2. 调用方通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口执行跳转，需要传入link和[options](../harmonyos-references/js-apis-app-ability-openlinkoptions.md)，不再需要传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skills配置的应用。

   * 当options中的appLinkingOnly为true时，匹配到的应用会经过应用市场域名检查（需联网）返回域名校验检查的唯一匹配项或未匹配结果。
   * 当options中的appLinkingOnly为false时，会优先尝试以App Linking的方式拉起，如果没有匹配的应用则跳转默认浏览器打开网页。

   ```
   1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[UIAbilityComponentsOpenLink]';
   6. const DOMAIN_NUMBER: number = 0xFF00;

   8. @Entry
   9. @Component
   10. struct WantAbilityPage1 {
   11. build() {
   12. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
   13. .width('87%')
   14. .height('5%')
   15. .margin({ bottom: '12vp' })
   16. .onClick(() => {
   17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   18. /*
   19. * 通过startAbility接口显式启动其他UIAbility，推荐使用openLink接口。
   20. * let want: Want = {
   21. *   bundleName: "com.test.example",
   22. *   moduleName: "entry",
   23. *   abilityName: "EntryAbility"
   24. * };
   25. * try {
   26. *   context.startAbility(want)
   27. *     .then(() => {
   28. *       hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
   29. *     }).catch((err: BusinessError) => {
   30. *       hilog.error(DOMAIN_NUMBER, TAG, `startAbility failed. Code is ${err.code}, message is ${err.message}`);
   31. *     })
   32. * } catch (paramError) {
   33. *   hilog.error(DOMAIN_NUMBER, TAG, `Failed to startAbility. Code is ${paramError.code},\
   34. *   message is ${paramError.message}`);
   35. * }
   36. */
   37. let link: string = 'https://www.example.com';
   38. let openLinkOptions: OpenLinkOptions = {
   39. // 匹配的abilities选项是否需要通过App Linking域名校验，匹配到唯一配置过的应用ability
   40. appLinkingOnly: true,
   41. // 同want中的parameter，用于传递的参数
   42. parameters: {demo_key: 'demo_value'}
   43. };

   45. try {
   46. context.openLink(link, openLinkOptions)
   47. .then(() => {
   48. hilog.info(DOMAIN_NUMBER, TAG, 'open link success.');
   49. }).catch((err: BusinessError) => {
   50. hilog.error(DOMAIN_NUMBER, TAG, `open link failed. Code is ${err.code}, message is ${err.message}`);
   51. })
   52. } catch (paramError) {
   53. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
   54. }
   55. })
   56. }
   57. }
   ```

   [WantAbilityPage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/ets/pages/WantAbilityPage1.ets#L15-L71)

## 启动其他应用的UIAbility并获取返回结果

1. 将待跳转的应用安装到设备，在其对应UIAbility的[module.json5配置文件](module-configuration-file.md)中配置skills标签的entities字段、actions字段和uri字段：

   * "actions"列表中包含"ohos.want.action.viewData"。
   * "entities"列表中包含"entity.system.browsable"。
   * "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。uri的匹配规则参考[uri匹配](explicit-implicit-want-mappings.md#uri匹配规则)，domainVerify为true代表开启域名检查，通过App Linking匹配该应用时需经过配置的域名校验后才能匹配到。

   ```
   1. {
   2. "module": {
   3. // ···
   4. "abilities": [
   5. // ···
   6. {
   7. // ···
   8. "skills": [
   9. {
   10. "entities": [
   11. "entity.system.browsable"
   12. ],
   13. "actions": [
   14. "ohos.want.action.viewData"
   15. ],
   16. "uris": [
   17. {
   18. "scheme": "https",
   19. "host": "www.example.com"
   20. }
   21. ],
   22. "domainVerify": true
   23. }
   24. ]
   25. },
   26. // ···
   27. ],
   28. // ···
   29. }
   30. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/module.json5#L17-L353)
2. 调用方通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口执行跳转，需要传入link和[options](../harmonyos-references/js-apis-app-ability-openlinkoptions.md)，不再需要传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skills配置的应用。AbilityResult回调结果通过入参传入回调函数，在被启动的UIAbility停止自身后返回给调用方。启动成功和失败结果仍通过Promise返回。

   * 当options中的appLinkingOnly为true时，匹配到的应用会经过应用市场域名检查（需联网）返回域名校验检查的唯一匹配项或未匹配结果。
   * 当options中的appLinkingOnly为false时，会优先尝试以App Linking的方式拉起，如果没有匹配的应用则跳转默认浏览器打开网页。

   ```
   1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const TAG: string = '[UIAbilityComponentsOpenLink]';
   6. const DOMAIN_NUMBER: number = 0xFF00;

   8. @Entry
   9. @Component
   10. struct WantAbilityPage2 {
   11. build() {
   12. Button('start link', { type: ButtonType.Capsule, stateEffect: true })
   13. .width('87%')
   14. .height('5%')
   15. .margin({ bottom: '12vp' })
   16. .onClick(() => {
   17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   18. /*
   19. * 通过startAbility接口显式启动其他UIAbility，推荐使用openLink接口。
   20. * let want: Want = {
   21. *   bundleName: "com.test.example",
   22. *   moduleName: "entry",
   23. *   abilityName: "EntryAbility"
   24. * };
   25. * try {
   26. *   context.startAbilityForResult(want)
   27. *     .then((data) => {
   28. *       hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success. data: ' + JSON.stringify(data));
   29. *     }).catch((err: BusinessError) => {
   30. *       hilog.error(DOMAIN_NUMBER, TAG, `startAbility failed. Code is ${err.code}, message is ${err.message}`);
   31. *     })
   32. * } catch (paramError) {
   33. *   hilog.error(DOMAIN_NUMBER, TAG, `Failed to startAbility. Code is ${paramError.code}, \
   34. *   message is ${paramError.message}`);
   35. * }
   36. */
   37. let link: string = 'https://www.example.com';
   38. let openLinkOptions: OpenLinkOptions = {
   39. // 匹配的abilities选项是否需要通过App Linking域名校验，匹配到唯一配置过的应用ability
   40. appLinkingOnly: true,
   41. // 同want中的parameter，用于传递的参数
   42. parameters: {demo_key: 'demo_value'}
   43. };

   45. try {
   46. context.openLink(link, openLinkOptions, (err, data) => {
   47. // AbilityResult回调函数，仅在被启动的UIAbility终止时触发
   48. hilog.info(DOMAIN_NUMBER, TAG, 'open link success. Callback result: ' + JSON.stringify(data));
   49. }).then(() => {
   50. hilog.info(DOMAIN_NUMBER, TAG, 'open link success.');
   51. }).catch((err: BusinessError) => {
   52. hilog.error(DOMAIN_NUMBER, TAG, `open link failed. Code is ${err.code}, message is ${err.message}`);
   53. })
   54. } catch (paramError) {
   55. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
   56. }
   57. })
   58. }
   59. }
   ```

   [WantAbilityPage2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/PullLinking/entry/src/main/ets/pages/WantAbilityPage2.ets#L15-L73)
