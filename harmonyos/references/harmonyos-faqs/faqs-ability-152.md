---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-152
title: 如何监听并响应应用切换前后台事件
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何监听并响应应用切换前后台事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:14cbebc08fe580752d5a45fd5f341900531ac77500ea12b6afbcb1e5c04daaf6
---

## 问题现象

如何监听并响应应用切换前后台事件并作出相应的处理？

## 背景知识

* [UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)是包含UI界面的应用组件，当应用首次启动到前台或者从后台转入到前台时，系统触发[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)回调；当应用从前台转入到后台时，系统触发[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)回调。
* [on('windowStageEvent')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageevent9)可以开启WindowStage生命周期变化的监听。当返回的WindowStage生命周期状态类型值为SHOWN和HIDDEN时，分别代表应用切到前台和切到后台状态，详情可参考[WindowStageEventType](../harmonyos-references/arkts-apis-window-e.md#windowstageeventtype9)。
* ApplicationContext中提供了[ApplicationContext.getRunningProcessInformation](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextgetrunningprocessinformation)方法用于获取有关运行进程的信息。
* HarmonyOS提供了EventHub、Emitter和commonEventManager三种事件通知，用于发布和监听相关事件。
  + [Emitter](../harmonyos-references/js-apis-emitter.md)模块提供了在同一进程不同线程间，或同一进程同一线程内，发送和处理事件的能力，包括持续订阅事件、单次订阅事件、取消订阅事件，以及发送事件到事件队列的能力。
  + [EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)模块提供订阅、取消订阅、触发事件的能力。但不是全局事件中心，不能用于虚拟机间或者进程间的事件传递。
  + [commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md)模块提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及退订公共事件。

## 解决方案

1. 监听应用切换前后台事件。
   * 方案一：在EntryAbility中onForeground和onBackground方法中处理应用切换前后台事件。代码示例：

     ```ts
     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
     ```
   * 方案二：通过窗口的on('windowStageEvent')接口，开启WindowStage生命周期变化的监听，处理应用切换前后台事件。代码示例：

     ```ts
     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       // 设置WindowStage的事件订阅（切到前台/切到后台）
       try {
         windowStage.on('windowStageEvent', (data) => {
           let stageEventType: window.WindowStageEventType = data;
           switch (stageEventType) {
             // 切到前台
             case window.WindowStageEventType.SHOWN:
               console.log(`windowStage foreground.`);
               // ...
               break;
             // 切到后台
             case window.WindowStageEventType.HIDDEN:
               console.log(`windowStage background.`);
               // ...
               break;
             default:
               break;
           }
         });
       } catch (exception) {
         console.log(`Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}`);
       }
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }
     ```
   * 方案三：通过ApplicationContext的getRunningProcessInformation()方法获取进程信息，其中包含当前进程运行状态，可以判断是否处于前台。代码示例：

     ```ts
     build() {
       RelativeContainer() {
         Button('获取信息').onClick(() => {
           let applicationContext = this.getUIContext().getHostContext()?.getApplicationContext();
           applicationContext?.getRunningProcessInformation().then((data) => {
             console.log(`The process running information is: ${JSON.stringify(data)}`);
           });
         })
       }
       .height('100%')
       .width('100%')
     }
     ```
2. 如果需要实现在页面、组件、线程等场景下响应前后台切换事件，可结合事件通知能力来实现。在切换前后台时，发送合适的事件通知，并在相应的场景下进行接收处理。

   使用EventHub发送通知this.context.eventHub.emit('onForeground');。

   使用EventHub接收通知。示例代码：

   ```ts
   eventFunc() {
     // 响应进入前台方法
     // ...
   }

   aboutToAppear(): void {
     // 以eventHub为例，订阅事件
     this.getUIContext().getHostContext()?.eventHub.on('onForeground', this.eventFunc);
   }

   aboutToDisappear(): void {
     this.getUIContext().getHostContext()?.eventHub.off('onForeground', this.eventFunc);
   }
   ```

## 常见FAQ

Q：如何在依赖的Har模块包中监听前后台切换事件？

A：在Hap包的EntryAbility.ets文件的onWindowStageCreate生命周期中，通过调用Har暴露的接口，将WindowStage传递给Har包。在Har包中对传递的window.WindowStage进行监听，判断应用是否退到后台。
