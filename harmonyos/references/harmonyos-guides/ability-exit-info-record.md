---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-exit-info-record
title: 获取应用异常退出原因
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 获取应用异常退出原因
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5a83ec6e991fed1878975984ae0b98187a0e9e00225ff33f154a8b00b50bb65
---

当应用异常退出后再次启动时，开发者往往需要获取上次异常退出的具体原因和当时的应用状态信息，比如应用内存占用的rss、pss值、上次应用退出的时间等等。通过UIAbility和UIExtensionAbility的OnCreate生命周期函数中的launchParam参数，开发者可以获取到相关信息，并将其应用于应用体验的分析改进，从而调整业务逻辑、提高应用的存活率。

## 约束限制

仅[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)和[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)支持获取上次的退出原因。

## 接口说明

接口详情参见[API参考](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)。

| **接口名** | **描述** |
| --- | --- |
| [LaunchParam](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam) | 启动参数。此接口的lastExitReason、lastExitMessage、lastExitDetailInfo成员记录Ability上次异常退出的信息。 |
| [LastExitDetailInfo](../harmonyos-references/js-apis-app-ability-abilityconstant.md#lastexitdetailinfo18) | 从API version 18开始，记录Ability所在进程上次退出时的关键运行信息。 |

## 开发步骤

1. 获取UIAbility上次退出的原因。

   在UIAbility类的onCreate成员函数的launchParam参数中读取Ability上次退出的信息。

   ```
   1. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const DOMAIN_NUMBER = 0xF811;
   5. const TAG  = '[Sample_UnexpExit]';
   6. const MAX_RSS_THRESHOLD: number = 100000;
   7. const MAX_PSS_THRESHOLD: number = 100000;

   9. function doSomething() {
   10. hilog.info(DOMAIN_NUMBER, TAG, 'do Something');
   11. }

   13. function doAnotherThing() {
   14. hilog.info(DOMAIN_NUMBER, TAG, 'do Another Thing');
   15. }

   17. export default class ExitAbility extends UIAbility {
   18. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
   19. // 获取退出原因
   20. let reason: number = launchParam.lastExitReason;
   21. let subReason: number = -1;
   22. if (launchParam.lastExitDetailInfo) {
   23. subReason = launchParam.lastExitDetailInfo.exitSubReason;
   24. }
   25. let exitMsg: string = launchParam.lastExitMessage;
   26. // ···
   27. if (launchParam.lastExitDetailInfo) {
   28. // 获取Ability上次退出时所在进程的信息
   29. let pid = launchParam.lastExitDetailInfo.pid;
   30. let processName: string = launchParam.lastExitDetailInfo.processName;
   31. let rss: number = launchParam.lastExitDetailInfo.rss;
   32. let pss: number = launchParam.lastExitDetailInfo.pss;
   33. // ···
   34. // 其他信息
   35. let uid: number = launchParam.lastExitDetailInfo.uid;
   36. let timestamp: number = launchParam.lastExitDetailInfo.timestamp;
   37. // ···
   38. }
   39. }
   40. }
   ```

   [ExitAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UnexpExit/entry/src/main/ets/exitability/ExitAbility.ets#L15-L80)
2. 根据上次退出的信息做相应的业务处理。

   * 对于不同的退出原因，开发者可以增加不同的处理逻辑，例如：

   ```
   1. if (reason === AbilityConstant.LastExitReason.APP_FREEZE) {
   2. // Ability上次因无响应而退出，此处可增加处理逻辑。
   3. doSomething();
   4. } else if (reason === AbilityConstant.LastExitReason.SIGNAL && subReason === 9) {
   5. // Ability上次所在进程因kill -9信号而退出，此处可增加处理逻辑。
   6. doAnotherThing();
   7. } else if (reason === AbilityConstant.LastExitReason.RESOURCE_CONTROL) {
   8. // Ability上次因rss管控而退出，此处可实现处理逻辑，最简单的就是打印出来。
   9. hilog.info(DOMAIN_NUMBER, TAG, `The ability has exit last because the rss control，the lastExitReason is ${reason}, subReason is ${subReason}, lastExitMessage is ${exitMsg}.`);
   10. }
   ```

   [ExitAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UnexpExit/entry/src/main/ets/exitability/ExitAbility.ets#L42-L53)

   * 根据进程信息感知应用内存占用异常，例如：

   ```
   1. if (rss > MAX_RSS_THRESHOLD || pss > MAX_PSS_THRESHOLD) {
   2. // RSS或PSS值过大，说明内存使用率接近或达到上限，打印告警，或者增加处理逻辑。
   3. hilog.warn(DOMAIN_NUMBER, TAG, `Process ${processName}(${pid}) memory usage approaches or reaches the upper limit.`);
   4. }
   ```

   [ExitAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UnexpExit/entry/src/main/ets/exitability/ExitAbility.ets#L62-L67)

   * 根据异常退出时刻的时间戳，明确异常发生的时刻，便于问题定位。

   ```
   1. hilog.info(DOMAIN_NUMBER, TAG, `App ${uid} terminated at ${timestamp}.`);
   ```

   [ExitAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UnexpExit/entry/src/main/ets/exitability/ExitAbility.ets#L73-L75)
