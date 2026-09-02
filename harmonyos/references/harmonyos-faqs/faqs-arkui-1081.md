---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1081
title: HarmonyOS如何监听窗口生命周期变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > HarmonyOS如何监听窗口生命周期变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:1003be4f3979cac5cba8f9fd2278d066540e77af9c1611789b21af7423749e85
---

## 问题现象

HarmonyOS如何监听不同情况窗口生命周期变化，比如窗口失焦/获焦、窗口前后台切换、窗口进入多任务等。

## 背景知识

* 开启WindowStage生命周期变化的监听：[windowStage.on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)。
* [WindowStageEventType](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)：WindowStage生命周期状态枚举。
* [on('windowEvent')](../harmonyos-references/arkts-apis-window-window.md#onwindowevent10)：可通过on('windowEvent')监听窗口的生命周期变化。
* [WindowEventType](../harmonyos-references/arkts-apis-window-e.md#windoweventtype10)：窗口生命周期。
* UIAbility里提供UI界面的应用组件生命周期回调：[UIAbility生命周期](../harmonyos-references/js-apis-app-ability-uiability.md)。

## 解决方案

* 监听窗口失焦与获焦的变化：
  + 可通过on('windowEvent')监听窗口的生命周期变化，其返回值WindowEventType.WINDOW\_ACTIVE为获焦状态，值为WindowEventType.WINDOW\_INACTIVE时为失焦状态。详情参考[PC或平板自由多窗模式下，如何做到主窗口获焦，子窗口隐藏](faqs-arkui-980.md)。
  + 可通过on('windowStageEvent')开启windowStage生命周期变化，其返回值WindowStageEventType.ACTIVE为获焦状态，WindowStageEventType.INACTIVE为失焦状态。
* 监听窗口前后台切换的变化：
  + 可通过on('windowEvent')监听窗口的生命周期变化，其返回值WindowEventType.WINDOW\_SHOWN为前台状态，值为WindowEventType.WINDOW\_HIDDEN时为后台状态。
  + 可通过on('windowStageEvent')开启windowStage生命周期变化，其返回值WindowStageEventType.SHOWN为前台状态，WindowStageEventType.HIDDEN为后台状态。
* 监听窗口是否进入多任务：
  + 可通过on('windowStageEvent')开启windowStage生命周期变化，当上划应用时，会触发WindowStageEventType.PAUSED，松开时会触发WindowStageEventType.RESUMED，详情参考[如何监听应用进入多任务](faqs-arkui-969.md)。

监听不同情况窗口生命周期变化示例代码参考如下：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });

    // 监听windowStage生命周期变化
    try {
      windowStage.on('windowStageEvent', (data) => {
        let stageEventType: window.WindowStageEventType = data;

        switch (stageEventType) {
          case window.WindowStageEventType.ACTIVE: // 获焦状态
            console.info(`windowStage active.`);
            break;
          case window.WindowStageEventType.INACTIVE: // 失焦状态
            console.info(`windowStage inactive.`);
            break;
          case window.WindowStageEventType.SHOWN: // 切到前台
            console.info(`windowStage foreground.`);
            break;
          case window.WindowStageEventType.HIDDEN: // 切到后台
            console.info(`windowStage background.`);
            break;
          default:
            break;
        }
      });
    } catch (exception) {
      console.info(`Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
    }

    // 监听窗口生命周期变化
    window.getLastWindow(this.context, (_, data) => {
      let windowClass = data;
      windowClass.on('windowEvent', (data) => {
        let winEventType: window.WindowEventType = data;

        switch (winEventType){
          case window.WindowEventType.WINDOW_ACTIVE: // 获焦状态
            console.info(`window active.`);
            break;
          case window.WindowEventType.WINDOW_INACTIVE: // 失焦状态
            console.info(`window inactive.`);
            break;
          case window.WindowEventType.WINDOW_SHOWN: // 切到前台
            console.info(`window foreground.`);
            break;
          case window.WindowEventType.WINDOW_HIDDEN: // 切到后台
            console.info(`window background.`);
            break;
          default:
            break;
        }
      });
    });
  }
```

## 常见FAQ

Q：使用[getLastWindow](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)获取的window，当新建的窗口还未销毁此时获取window，就会报Window is nullptr和This window stage is abnormal，请问有什么好的解决办法？

A：建议应用在窗口销毁[onWindowStageDestroy](../harmonyos-references/js-apis-app-ability-abilitylifecyclecallback.md#onwindowstagedestroy)回调中处理业务。如果只是想获取业务的Component（Entry所属的那个window），可以通过getUIContext().[getWindowName](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowname12)获取。

Q：在[onBackground](../harmonyos-guides/uiability-lifecycle.md#onbackground)中使用[windowStage.getMainWindowSync](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)获取主窗口偶现报错Cannot read property off of undefined如何解决？

A：在onBackground事件中，可能正在释放一部分资源，包括窗口资源，因此可能出现获取不到主窗。可以使用[ApplicationContext.on('abilityLifecycle')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)监听[AbilityLifecycleCallback](../harmonyos-references/js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback)的[onAbilityWillBackground](../harmonyos-references/js-apis-app-ability-abilitylifecyclecallback.md#onabilitywillbackground12)事件或者[onWindowStageInactive](../harmonyos-references/js-apis-app-ability-abilitylifecyclecallback.md#onwindowstageinactive)事件，再操作主窗。

Q：折叠屏手机锁屏时会将[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)监听注销，如何在设备解锁时恢复监听？

A：当折叠屏设备锁屏时，系统会暂停后台应用的非必要监听以节省资源。display.on('foldStatusChange')作为屏幕状态监听器，属于系统级资源敏感操作，锁屏时会被自动注销。建议在[onForeground](../harmonyos-guides/uiability-lifecycle.md#onforeground)生命周期重新注册监听器，在onBackground主动注销避免资源泄漏。

Q：多窗口场景（分屏、悬浮窗、自由多窗）下，UIAbility的onForeground和onBackground不触发，如何监听应用前后台切换？

A：onForeground和onBackground是应用进程级的前后台切换回调，多窗口场景下应用窗口仅发生失焦/获焦或显示/隐藏，并未发生进程级前后台切换，因此不会触发。可通过[windowStage.on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)监听WindowStage生命周期变化来处理前后台切换事件，也可通过[ApplicationContext.getRunningProcessInformation()](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextgetrunningprocessinformation)获取进程信息判断当前是否处于前台。若需要在页面、组件、线程等场景下响应前后台切换，可结合事件通知能力，在切换前后台时发送事件通知并在相应场景下接收处理。
