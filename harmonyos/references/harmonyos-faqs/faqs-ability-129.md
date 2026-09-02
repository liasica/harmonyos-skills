---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-129
title: 应用二次侧滑退出到桌面，背景声音还在继续播放
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用二次侧滑退出到桌面，背景声音还在继续播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7ed1bc2de86a3e598678d721f231c2525a35932a2256cdd17d049eca4727611d
---

## 问题现象

应用打开，在前台时点击播放背景音乐，连续侧滑2次，中间应用提示“再按一次退出”，退至手机桌面，此时背景音乐还在继续播放。

## 背景知识

* [长时任务](../harmonyos-guides/continuous-task.md)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。
* [onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：属于自定义组件的生命周期回调函数之一，当用户点击返回按钮或侧滑返回时触发，仅@Entry装饰的自定义组件生效。

## 问题定位

根据应用运行过程中HIlog日志进行排查：

1. 应用在启动时即申请了后台长时任务，根据关键词“startBackgroundRunning”可过滤出来，如下所示：

   ```shell
   06-30 14:19:57.882   60087-61546   C01711/com.hm...NTINUOUS_TASK  [StartBackgroundRunningExecuteCB:271] RequestStartBackgroundRunning isBatch: 0, bgModeSize: 0
   06-30 14:19:57.889   60087-61546   C01711/com.hm...CKGROUND_TASK  [StartBackgroundRunning:201] BackgroundTaskMgrProxy read notificationId -1, continuousTaskId 14
   06-30 14:19:57.889   60087-61546   C01711/com.hm...NTINUOUS_TASK  [StartBackgroundRunningExecuteCB:276] notification -1, continuousTaskId 14
   ```
2. 应用通过2次侧滑退到手机桌面，通过日志中关键字“onBackPress return true”，说明重写了onBackPress的方法；关键字“app is inBackground”则表明应用是进入后台状态，并不是进程结束。

   ```shell
   06-30 14:27:36.433   60087-61785   C03900/com.hm.example/Ace            com.hm.example    I     [(-1:100000:singleton)] [com.hm.example][entry][100000]: OnBackPressed called
   06-30 14:27:36.433   60087-60087   C03922/com.hm.example/AceNavigation  com.hm.example    I     [(100000:100000:scope)] can't find destination node to process back press
   06-30 14:27:36.434   60087-60087   C03925/com.hm.example/AceRouter      com.hm.example    I     [(100000:100000:scope)] router user onBackPress return true
   06-30 14:27:36.434   60087-60087   C03900/com.hm.example/Ace            com.hm.example    I     [(100000:100000:scope)] router consumed backpressed event
   06-30 14:27:36.751   60087-61785   C03900/com.hm.example/Ace            com.hm.example    I     [(-1:100000:singleton)] [com.hm.example][entry][100000]: OnBackPressed called
   06-30 14:27:36.751   60087-60087   C03922/com.hm...AceNavigation        com.hm.example    I     [(100000:100000:scope)] can't find destination node to process back press
   06-30 14:27:36.752   60087-60087   C03900/com.hm.example/Ace            com.hm.example    E     [(100000:100000:scope)] Error calling onBackPress
   06-30 14:27:36.753   60087-60087   A03D00/com.hm.example/JSAPP          com.hm.example    I     Ability onBackPressed
   06-30 14:27:36.753   60087-60087   C04200/com.hm...neSessionImpl        com.hm.example    I     (3012)PerformBack: Transfer back event to host session needMoveToBackground 1
   06-30 14:27:36.764   60087-60087   A03D00/com.hm.example/JSAPP          com.hm.example    I     [@umeng][common][lifecycle]:AbilityLifecycleCallback onWindowStageInactive ability: ${ability} windowStage: ${windowStage}
   06-30 14:27:36.770   60087-60087   A03D00/com.hm.example/JSAPP          com.hm.example    I     Ability onBackground1:::true
   06-30 14:27:36.770   60087-60087   C01332/com.hm.example/UIAbility      com.hm.example    I     [js_ui_ability.cpp:1408]end, name: onBackground, time: 2
   06-30 14:27:36.770   60087-60087   C04202/com.hm.example/WMSMain        com.hm.example    I     [] GoBackground(170): reason: 0
   06-30 14:27:36.771   60087-60087   C03900/com.hm.example/Ace            com.hm.example    I     [(-2:100000:singleton)] [com.hm.example][entry][100000]: window background
   06-30 14:27:36.776   60087-60087   C01406/com.hm.example/OHOS::RS       com.hm.example    I     RSSurfaceNode::SetAbilityState, surfaceNodeId:[258071699914753], ability state: background
   06-30 14:27:36.777   60087-60087   A03D00/com.hm.example/JSAPP          com.hm.example    I     [@umeng][common][lifecycle]:AbilityLifecycleCallback onAbilityBackground ability: ${ability}
   06-30 14:27:36.777   60087-60087   C02D07/com.hm.example/ObserverMgr    com.hm.example    I     start to handle background
   06-30 14:27:37.559   60087-60087   C03F00/com.hm.example/ArkCompiler    com.hm.example    I     [gc] app is inBackground
   ```

## 分析结论

应用通过侧滑回到手机桌面处理逻辑并不是结束进程，而是进入后台状态。此时在长时任务的情况下，仍然可以播放背景音乐。

## 修改建议

应用在自定义侧滑退出应用时应结束应用进程，而不是进入后台。ArkTS提供了UIAbilityContext.[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)和UIAbilityContext.[terminateSelfWithResult](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)两个接口用于主动退出停止。参考代码：

```ts
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private message: string = '连续侧滑2次退出应用';
  private firstBackTimestamp: number = 0;
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  promptAction = this.getUIContext().getPromptAction();

  build() {
    Column() {
      Text(this.message)
        .fontWeight(FontWeight.Bold);
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }

  onBackPress(): boolean | void {
    let now = Date.now();
    if (now - this.firstBackTimestamp < 1000) {
      this.context.terminateSelf();
    } else {
      this.firstBackTimestamp = now;
      this.promptAction.showToast({
        message: '再侧滑一次退出应用',
        duration: 1000
      });
    }
    return true;
  }
}
```
