---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-69
title: 应用被用户主动退出/清理时如何保存数据
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 应用被用户主动退出/清理时如何保存数据
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:78cd0c637119103098e918df8af3ed37ad60a6f75c291187f8bd3fd0b1f4c164
---

## 问题现象

编辑页面内容时，如果应用被用户主动退出或者应用进程被清理时，应该如何保存当前页面未提交信息？

## 背景知识

* [短时任务(ArkTS)](../harmonyos-guides/transient-task.md)：应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用在后台仍需要执行耗时不长的任务，如状态保存等，可以通过申请短时任务，扩展应用在后台的运行时间。
* 在UIAbility实例销毁之前，系统触发[onWindowStageWillDestroy()](../harmonyos-guides/uiability-lifecycle.md#onwindowstagewilldestroy)回调。如果需要感知UIAbility生命周期变化，可以使用[ApplicationContext注册接口](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)监听UIAbility生命周期变化。详见[监听UIAbility生命周期变化](../harmonyos-guides/application-context-stage.md#监听uiability生命周期变化)。
* [公共事件模块](../harmonyos-references/js-apis-commoneventmanager.md#commoneventsubscribeinfo10)提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及退订公共事件。

## 解决方案

用户主动退出应用有以下几种场景：

| 退出方式 | 触发事件 |
| --- | --- |
| 多任务中心一键清理 | 系统会发送[公共事件](../harmonyos-guides/common-event-subscription.md)：名称event为**RECENT\_EVENT**，数据data为**RECENT\_CLEAR\_ALL**。 |
| 多任务中心上滑清理 | 系统会触发[onWindowStageWillDestroy()](../harmonyos-guides/uiability-lifecycle.md#onwindowstagewilldestroy)回调 |

* 当应用被用户通过多任务中心的一键清理销毁时，可通过[公共事件订阅](../harmonyos-guides/common-event-subscription.md)监听对应事件：[CommonEventSubscribeInfo](../harmonyos-references/js-apis-inner-commonevent-commoneventsubscribeinfo.md)中的公共事件名称event为**RECENT\_EVENT**，[CommonEventData](../harmonyos-references/js-apis-inner-commonevent-commoneventdata.md)中的公共事件数据data为**RECENT\_CLEAR\_ALL**。

  ```ts
  subscribeMultitaskCleanup() {
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
          if (!err) {
            console.info(`Succeeded in creating subscriber.`);
            subscriber = commonEventSubscriber;
            // 订阅公共事件
            try {
              commonEventManager.subscribe(subscriber,
                (err: BusinessError, eventData: commonEventManager.CommonEventData) => {
                  if (err) {
                    console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                    return;
                  }
                  // 多任务点击一键清理事件
                  if (eventData.data === 'RECENT_CLEAR_ALL') {
                    // 监听多任务视图一键清理事件，进行业务处理
                    this.saveAppData();
                  }
                  console.info(`Succeeded in subscribing, eventData is ${JSON.stringify(eventData)}`);
                });
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
            }
            return;
          }
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    }
  }
  ```
* 当应用被用户通过多任务中心上滑或其他方式销毁时，可使用[ApplicationContext注册接口](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)监听UIAbility生命周期变化，在[onWindowStageWillDestroy()](../harmonyos-guides/uiability-lifecycle.md#onwindowstagewilldestroy)回调中进行页面数据的保存。

  ```ts
  subscribeMultitaskSlipUpDelete() {
    let _this = this;
    let abilityLifecycleCallback: AbilityLifecycleCallback = {
      onWindowStageWillDestroy() {
        console.info(`AbilityLifecycleCallback onWindowStageWillDestroy.`);
        // 监听onWindowStageWillDestroy回调，进行业务处理
        _this.saveAppData();
      },
      onAbilityCreate() {
        console.info(`AbilityLifecycleCallback onAbilityCreate.`);
      },
      onWindowStageCreate() {
        console.info(`AbilityLifecycleCallback onWindowStageCreate.`);
      },
      onWindowStageActive() {
        console.info(`AbilityLifecycleCallback onWindowStageActive.`);
      },
      onWindowStageInactive() {
        console.info(`AbilityLifecycleCallback onWindowStageInactive.`);
      },
      onWindowStageDestroy() {
        console.info(`AbilityLifecycleCallback onWindowStageDestroy.`);
      },
      onAbilityDestroy() {
        console.info(`AbilityLifecycleCallback onAbilityDestroy.`);
      },
      onAbilityForeground() {
        console.info(`AbilityLifecycleCallback onAbilityForeground.`);
      },
      onAbilityBackground() {
        console.info(`AbilityLifecycleCallback onAbilityBackground.`);
      },
      onAbilityContinue() {
        console.info(`AbilityLifecycleCallback onAbilityContinue.`);
      }
    };
    try {
      // 通过applicationContext注册监听应用内生命周期
      let lifecycleId = this.appContext.on('abilityLifecycle', abilityLifecycleCallback);
      console.info(`registerAbilityLifecycleCallback lifecycleId: ${lifecycleId}`);
    } catch (paramError) {
      console.error(`registerAbilityLifecycleCallback failed,error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
  }
  ```

**须知** 

注意：无论是通过多任务中心上滑退出应用还是通过一键清理退出应用都会杀死应用进程，所以在收到onWindowStageWillDestroy回调或是公共事件回调时仅有短暂的时间(约几毫秒)可供应用保存数据，因此该方案仅适用于**保存少量数据**，**不适用于保存大数据或耗时操作**。

以下为使用首选项实现的应用退出时保存页面数据的完整示例代码:

```ts
import { AbilityLifecycleCallback, common } from '@kit.AbilityKit';
import { preferences } from '@kit.ArkData';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

@Observed
class UserInfo {
  name: string = '';
  cardId: string = '';
  phone: string = '';
  email: string = '';

  setName(value: string) {
    this.name = value;
  }

  setCardId(value: string) {
    this.cardId = value;
  }

  setPhone(value: string) {
    this.phone = value;
  }

  setEmail(value: string) {
    this.email = value;
  }
}

@Entry
@Component
struct Index {
  @State userInfo: UserInfo = new UserInfo();
  isSaving: boolean = false;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  appContext = this.context.getApplicationContext();
  dataPreferences: preferences.Preferences | null = null;

  aboutToAppear(): void {
    this.getPreferenceInfo();
    this.subscribeMultitaskCleanup();
    this.subscribeMultitaskSlipUpDelete();
  }

  subscribeMultitaskCleanup() {
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
          if (!err) {
            console.info(`Succeeded in creating subscriber.`);
            subscriber = commonEventSubscriber;
            // 订阅公共事件
            try {
              commonEventManager.subscribe(subscriber,
                (err: BusinessError, eventData: commonEventManager.CommonEventData) => {
                  if (err) {
                    console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                    return;
                  }
                  // 多任务点击一键清理事件
                  if (eventData.data === 'RECENT_CLEAR_ALL') {
                    // 监听多任务视图一键清理事件，进行业务处理
                    this.saveAppData();
                  }
                  console.info(`Succeeded in subscribing, eventData is ${JSON.stringify(eventData)}`);
                });
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
            }
            return;
          }
          console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
        });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    }
  }

  subscribeMultitaskSlipUpDelete() {
    let _this = this;
    let abilityLifecycleCallback: AbilityLifecycleCallback = {
      onWindowStageWillDestroy() {
        console.info(`AbilityLifecycleCallback onWindowStageWillDestroy.`);
        // 监听onWindowStageWillDestroy回调，进行业务处理
        _this.saveAppData();
      },
      onAbilityCreate() {
        console.info(`AbilityLifecycleCallback onAbilityCreate.`);
      },
      onWindowStageCreate() {
        console.info(`AbilityLifecycleCallback onWindowStageCreate.`);
      },
      onWindowStageActive() {
        console.info(`AbilityLifecycleCallback onWindowStageActive.`);
      },
      onWindowStageInactive() {
        console.info(`AbilityLifecycleCallback onWindowStageInactive.`);
      },
      onWindowStageDestroy() {
        console.info(`AbilityLifecycleCallback onWindowStageDestroy.`);
      },
      onAbilityDestroy() {
        console.info(`AbilityLifecycleCallback onAbilityDestroy.`);
      },
      onAbilityForeground() {
        console.info(`AbilityLifecycleCallback onAbilityForeground.`);
      },
      onAbilityBackground() {
        console.info(`AbilityLifecycleCallback onAbilityBackground.`);
      },
      onAbilityContinue() {
        console.info(`AbilityLifecycleCallback onAbilityContinue.`);
      }
    };
    try {
      // 通过applicationContext注册监听应用内生命周期
      let lifecycleId = this.appContext.on('abilityLifecycle', abilityLifecycleCallback);
      console.info(`registerAbilityLifecycleCallback lifecycleId: ${lifecycleId}`);
    } catch (paramError) {
      console.error(`registerAbilityLifecycleCallback failed,error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
  }

  saveAppData() {
    try {
      if (this.isSaving) {
        console.info('already saving, skip this time.');
        return;
      }
      this.isSaving = true;
      if (this.userInfo) {
        // 保存应用业务数据
        this.savePreferenceInfo();
      }
    } catch (error) {
      console.error(`saveAppData failed. code is ${(error as BusinessError)?.code} message is ${(error as BusinessError)?.message}`);
    }
  }

  // 初始化Preference
  initPreferences() {
    try {
      if (this.dataPreferences == null) {
        this.dataPreferences = preferences.getPreferencesSync(this.context, { name: 'appCache' });
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`getPreferencesSync failed. code is ${err.code} message is ${err.message}`);
    }
  }

  // 保存数据到Preference中并持久化
  savePreferenceInfo() {
    try {
      this.initPreferences();
      this.dataPreferences?.putSync('cacheData', JSON.stringify(this.userInfo));
      this.dataPreferences?.flushSync();
      console.info(`this.userInfo => ${JSON.stringify(this.userInfo)}`);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`savePreferenceInfo failed. code is ${err.code} message is ${err.message}`);
    }
  }

  // 从Preference中获取数据
  getPreferenceInfo() {
    try {
      this.initPreferences();
      let cacheData = this.dataPreferences?.getSync('cacheData', '') as string;
      console.info(`cacheData => ${JSON.stringify(cacheData)}`);
      if (cacheData) {
        let userInfo = JSON.parse(cacheData) as UserInfo;
        this.userInfo.setName(userInfo.name);
        this.userInfo.setCardId(userInfo.cardId);
        this.userInfo.setPhone(userInfo.phone);
        this.userInfo.setEmail(userInfo.email);
        console.info(`this.userInfo => ${JSON.stringify(this.userInfo)}`);
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`getPreferenceInfo failed. code is ${err.code} message is ${err.message}`);
    }
  }

  build() {
    Navigation() {
      Column({ space: 20 }) {
        this.InputStyle('姓名', '证件号码', this.userInfo.name, (value: string) => {
          this.userInfo.setName(value);
        });

        this.InputStyle('证件号码', '联系电话', this.userInfo.cardId, (value: string) => {
          this.userInfo.setCardId(value);
        }, InputType.Number);

        this.InputStyle('联系电话', '电子邮箱', this.userInfo.phone, (value: string) => {
          this.userInfo.setPhone(value);
        }, InputType.PhoneNumber);

        this.InputStyle('电子邮箱', '', this.userInfo.email, (value: string) => {
          this.userInfo.setEmail(value);
        }, InputType.Email);
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Start)
      .justifyContent(FlexAlign.Start)
      .padding(20);
    }
    .backgroundColor('#F1F3F5');
  }

  // Input样式子组件封装
  @Builder
  InputStyle(text: string, next: string, val: string, setValue: Function,
    type: InputType = InputType.Normal) {
    Row() {
      Text(text)
        .fontSize(16)
        .fontWeight(500);
      TextInput({ placeholder: `请输入${text}`, text: val })
        .key(text)// 定义当前填写项的key值
        .fontSize(16)
        .width('60%')
        .layoutWeight(1)
        .type(type)
        .placeholderColor('#66000000')
        .placeholderFont({ size: 16, weight: 400 })
        .backgroundColor(Color.White)
        .enterKeyType(EnterKeyType.Next)
        .onSubmit(() => {
          focusControl.requestFocus(next); // 填写跳转目标填写项的key值
        })
        .onChange((value: string) => {
          setValue(value);
        });
    }
    .width('100%')
    .height(50)
    .backgroundColor(Color.White)
    .padding({ left: 15, right: 15 })
    .borderRadius(18);
  };
}
```
