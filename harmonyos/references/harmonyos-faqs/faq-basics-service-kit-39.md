---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-39
title: 应用在后台如何接收公共事件
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 应用在后台如何接收公共事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9a9e873f944449b6a8ba103bf24fd5691d66e65d2aa6d0ee1be555b0de6f7dfe
---

## 问题现象

应用订阅灭屏公共事件后，为什么按电源键灭屏未接收到灭屏事件，反而在亮屏后接收到灭屏事件？

灭屏公共事件：

```screen
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ["usual.event.SCREEN_OFF"], // 订阅灭屏公共事件
};
```

## 背景知识

* [动态订阅公共事件](../harmonyos-guides/common-event-subscription.md)：动态订阅的公共事件回调受应用状态影响。当应用处于后台时，无法接收到动态订阅公共事件。当应用从后台切换到前台时，最多可以回调切回前30s内监听的公共事件。
* [长时任务](../harmonyos-guides/continuous-task.md)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。

## 解决方案

按电源键灭屏，应用处于后台，无法接收到灭屏事件，点亮并解锁屏幕，应用切换到前台，会回调30s内监听到的灭屏事件。

通过申请长时任务，可以让应用处于后台时也能监听到灭屏事件。参考长时任务[开发步骤](../harmonyos-guides/continuous-task.md#开发步骤)，需要先在module.json5中配置ohos.permission.KEEP\_BACKGROUND\_RUNNING权限并声明后台模式类型，然后使用[backgroundTaskManager.startBackgroundRunning()](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning)API申请长时任务。可以参考如下代码：

```screen
import { commonEventManager } from '@kit.BasicServicesKit';
import { ApplicationStateChangeCallback, common, WantAgent, wantAgent } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

@Component
@Entry
struct EventPage {
  longTaskEnable: boolean = false;

  build() {
    Column({ space: 50 }) {
      Text('test SCREEN_OFF event')
    }
    .width('100%')
    .height('100%')
  }

  private settingSubscriber: commonEventManager.CommonEventSubscriber | null = null;
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    this.subscribeStateChange();
    let settingSubscriberInfo: commonEventManager.CommonEventSubscribeInfo = {
      events: [
        // 灭屏事件
        commonEventManager.Support.COMMON_EVENT_SCREEN_OFF
      ]
    };
    commonEventManager.createSubscriber(settingSubscriberInfo).then((subscriber) => {
      this.settingSubscriber = subscriber;
      commonEventManager.subscribe(subscriber, () => {
        hilog.info(0x0000, '', 'My app received COMMON_EVENT_SCREEN_OFF');
      });
    });
  }

  aboutToDisappear(): void {
    commonEventManager.unsubscribe(this.settingSubscriber, () => {
      this.settingSubscriber = null;
    });
    this.stopLongTask();
  }

  subscribeStateChange() {
    let that = this;
    let applicationContext = this.context.getApplicationContext();
    let applicationStateChangeCallback: ApplicationStateChangeCallback = {
      onApplicationForeground() {
        hilog.info(0x0000, '', 'applicationStateChangeCallback onApplicationForeground');
      },
      onApplicationBackground() {
        hilog.info(0x0000, '', 'applicationStateChangeCallback onApplicationBackground');
        // 应用切到后台时启动长时任务
        if (!this.longTaskEnable) {
          that.startLongTask();
        }
      }
    };
    try {
      // 监听应用前后台状态变化
      applicationContext.on('applicationStateChange', applicationStateChangeCallback);
    } catch (paramError) {
      hilog.error(0x0000, '',
        `error: ${(paramError as BusinessError<string>).code}, ${(paramError as BusinessError<string>).message}`);
    }
  }

  startLongTask(): void {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: this.context.abilityInfo.bundleName,
          abilityName: this.context.abilityInfo.name
        }
      ],
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    try {
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        backgroundTaskManager.startBackgroundRunning(this.context, backgroundTaskManager.BackgroundMode.LOCATION,
          wantAgentObj)
          .then(() => {
            hilog.info(0x0000, '', `Operation startBackgroundRunning succeeded`);
          })
          .catch((error: BusinessError<string>) => {
            hilog.error(0x0000, '',
              `Operation startBackgroundRunning failed. code is ${error.code} message is ${error.message}`);
          });
      });
    } catch (error) {
      hilog.error(0x0000, '', `Operation getWantAgent failed. error is ${JSON.stringify(error)} `);
    }
  }

  // 停止长时任务
  stopLongTask(): void {
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      hilog.info(0x0000, '', 'Operation stopBackgroundRunning succeeded');
      this.longTaskEnable = false;
    }).catch((error: BusinessError<string>) => {
      hilog.error(0x0000, '', `Operation stopBackgroundRunning failed. error is ${JSON.stringify(error)} `);
    });
  }
}
```

## 常见FAQ

Q：如何判断设备是否熄屏？

A：可以订阅系统公共事件[COMMON\_EVENT\_SCREEN\_OFF](../harmonyos-references/commoneventmanager-definitions.md#common_event_screen_off)监听熄屏。

## 总结

应用退至后台一小段时间后，应用进程会被挂起，无法使用软件资源（如公共事件、定时器等）和硬件资源（CPU、网络、GPS、蓝牙等）。应用可以合理使用后台任务，以满足应用退至后台后继续运行的需求。
