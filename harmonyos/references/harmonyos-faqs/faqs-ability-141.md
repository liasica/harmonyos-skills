---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-141
title: 如何监听应用主动终止进程或用户主动清理
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何监听应用主动终止进程或用户主动清理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a7f01af79c9013aa99eaedb7b27a683e277c48060048e8f27ec0ec98d5fd55f4
---

## 问题现象

在统计当前APP使用时长，或者应用退出时清理应用发布的通知消息等场景下，需要关注应用何时关闭退出（应用主动终止进程或者用户主动清理两大类场景），涉及的事件有哪些，如何监听？

## 背景知识

* 应用主动终止进程：

  ArkTS的UIAbilityContext提供了两个接口用于主动退出停止：[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)、[terminateSelfWithResult](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)。需要注意的是调用这些接口后，任务中心的任务默认不会清理（即手势上划切到近期所有任务滑动界面，被终止的应用仍存在）。

  如需清理，需要在项目的module.json5中配置removeMissionAfterTerminate为true（不配置默认false）。
* UIAbility应用生命周期：

  当用户打开关闭、切换和返回到对应应用时，应用中的UIAbility实例会在其生命周期的不同状态之间转换。UIAbility类提供了一系列回调，通过这些回调可以知道当前UIAbility实例的某个状态发生改变，会经过UIAbility实例的创建和销毁，或者UIAbility实例发生了前后台的状态切换。

  相关状态可以参考：[onDestroy](../harmonyos-guides/uiability-lifecycle.md#ondestroy)、[onWindowStageWillDestroy](../harmonyos-guides/uiability-lifecycle.md#onwindowstagewilldestroy)、[onWindowStageCreate](../harmonyos-guides/uiability-lifecycle.md#onwindowstagecreate)、[onWindowStageDestroy](../harmonyos-guides/uiability-lifecycle.md#onwindowstagedestroy)。

## 解决方案

* 场景一：应用主动终止进程。

  可以通过terminateSelf和terminateSelfWithResult处理，这两个API都提供了退出事件回调，相关退出监听及业务逻辑可以直接在回调里面处理，代码示例如下：

  ```ts
  function terminateSelfTest(context: common.UIAbilityContext) {
    try {
      context.terminateSelf((err: BusinessError) => {
        if (err.code) {
          // 处理逻辑错误
          hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行监听回调处理
        hilog.info(DOMAIN, TAG, 'terminateSelf succeed');
      });
    } catch (err) {
      // 捕获同步的参数错误
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${code}, message is ${message}`);
    }
  }
  ```

  ```ts
  function terminateSelfWithResultTest(context: common.UIAbilityContext) {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let resultCode = 100;
    // 返回给接口调用方AbilityResult信息
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };
    try {
      context.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
        if (err.code) {
          // 处理逻辑错误
          hilog.error(DOMAIN, TAG, `terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行监听回调处理
        hilog.info(DOMAIN, TAG, 'terminateSelfWithResult succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN, TAG, `terminateSelfWithResult failed, code is ${code}, message is ${message}`);
    }
  }
  ```
* 场景二：用户主动清理应用。用户通过最近任务列表主动清理应用，有以下两种操作情况：
  + 用户点击底下的垃圾桶图标，一键清理所有近期应用：

    可通过[公共事件订阅](../harmonyos-guides/common-event-subscription.md)监听对应事件：[CommonEventSubscribeInfo](../harmonyos-references/js-apis-inner-commonevent-commoneventsubscribeinfo.md)中的公共事件名称event为“RECENT\_EVENT”，[CommonEventData](../harmonyos-references/js-apis-inner-commonevent-commoneventdata.md)中的公共事件数据data为“RECENT\_CLEAR\_ALL”。

    ```ts
    function subscribeMultitaskCleanup() {
      // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
      let subscriber: commonEventManager.CommonEventSubscriber;
      // 订阅者信息
      let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
        events: ['RECENT_EVENT'] // 多任务事件
      };
      // 创建订阅者
      try {
        commonEventManager.createSubscriber(subscribeInfo,
          (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
            if (err) {
              hilog.error(DOMAIN, TAG, `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
              return;
            }
            subscriber = commonEventSubscriber;
            // 订阅公共事件
            try {
              commonEventManager.subscribe(subscriber,
                (err: BusinessError, eventData: commonEventManager.CommonEventData) => {
                  if (err) {
                    hilog.error(DOMAIN, TAG, `Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                    return;
                  }
                  // 多任务点击一键清理事件
                  if (eventData.data === 'RECENT_CLEAR_ALL') {
                    // 监听多任务视图一键清理事件，进行业务处理
                    hilog.info(DOMAIN, TAG, `RECENT_CLEAR_ALL notify success`);
                  }
                });
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              hilog.error(DOMAIN, TAG, `Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
            }
          });
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        hilog.error(DOMAIN, TAG, `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
      }
    }
    ```
  + 用户选择当前应用，上划清理当前应用：

    方式一：这种情形找到上划删除应用涉及的UIAbility，其生命周期函数onWindowStageDestroy、onDestroy在销毁时会被执行，可以在onWindowStageDestroy、onDestroy回调函数中进行相关逻辑处理。

    方式二：可以在应用涉及的UIAbility生命周期函数onCreate里面注册监听应用内生命周期回调，在应用触发销毁生命周期函数里（如：onAbilityDestroy、onWindowStageDestroy、onWindowStageWillDestroy，onAbilityWillDestroy等）处理销毁业务逻辑。详细可以参考：[AbilityLifecycleCallback使用示例](../harmonyos-references/js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

  完整示例代码：

  ```ts
  import { BusinessError } from '@ohos.base';
  import { common, Want } from '@kit.AbilityKit';
  import commonEventManager from '@ohos.commonEventManager';
  import hilog from '@ohos.hilog';

  const DOMAIN: number = 0x00;
  const TAG: string = 'IndexPage';

  function terminateSelfTest(context: common.UIAbilityContext) {
    try {
      context.terminateSelf((err: BusinessError) => {
        if (err.code) {
          // 处理逻辑错误
          hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行监听回调处理
        hilog.info(DOMAIN, TAG, 'terminateSelf succeed');
      });
    } catch (err) {
      // 捕获同步的参数错误
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${code}, message is ${message}`);
    }
  }

  function terminateSelfWithResultTest(context: common.UIAbilityContext) {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let resultCode = 100;
    // 返回给接口调用方AbilityResult信息
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };
    try {
      context.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
        if (err.code) {
          // 处理逻辑错误
          hilog.error(DOMAIN, TAG, `terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行监听回调处理
        hilog.info(DOMAIN, TAG, 'terminateSelfWithResult succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(DOMAIN, TAG, `terminateSelfWithResult failed, code is ${code}, message is ${message}`);
    }
  }

  function subscribeMultitaskCleanup() {
    // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
    let subscriber: commonEventManager.CommonEventSubscriber;
    // 订阅者信息
    let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
      events: ['RECENT_EVENT'] // 多任务事件
    };
    // 创建订阅者
    try {
      commonEventManager.createSubscriber(subscribeInfo,
        (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
          if (err) {
            hilog.error(DOMAIN, TAG, `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
            return;
          }
          subscriber = commonEventSubscriber;
          // 订阅公共事件
          try {
            commonEventManager.subscribe(subscriber,
              (err: BusinessError, eventData: commonEventManager.CommonEventData) => {
                if (err) {
                  hilog.error(DOMAIN, TAG, `Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                  return;
                }
                // 多任务点击一键清理事件
                if (eventData.data === 'RECENT_CLEAR_ALL') {
                  // 监听多任务视图一键清理事件，进行业务处理
                  hilog.info(DOMAIN, TAG, `RECENT_CLEAR_ALL notify success`);
                }
              });
          } catch (error) {
            let err: BusinessError = error as BusinessError;
            hilog.error(DOMAIN, TAG, `Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
          }
        });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    }
  }

  @Entry
  @Component
  export struct Index {
    curContext: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

    build() {
      Column() {
        Button('TerminateSelf')
          .onClick(() => {
            terminateSelfTest(this.curContext);
          });
        Button('TerminateSelfWithResult')
          .onClick(() => {
            terminateSelfWithResultTest(this.curContext);
          });
        Button('clear Recent Task')
          .onClick(() => {
            subscribeMultitaskCleanup();
          });
      };
    }
  }
  ```

## 常见FAQ

Q：terminateSelf()和killAllProcesses()两个函数都能主动退出应用，这两种方式有什么区别？

A：UIAbilityContext下的[terminateSelf](../harmonyos-references/js-apis-inner-application-uiextensioncontext.md#terminateself12)是走UIAbility的正常生命周期，正常销毁；ApplicationContext下的[killAllProcesses](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses)是找出应用下面所有的进程，逐个终止，属于强制终止。

Q：为什么使用terminateSelf()后还能在最近任务列表中仍然能查看到该实例对应的任务？

A：调用terminateSelf()方法停止当前UIAbility实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应UIAbility的module.json5配置文件中，将abilities标签的removeMissionAfterTerminate字段配置为true。
