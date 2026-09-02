---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-14
title: 点击消息通知跳转应用页面的方案
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 点击消息通知跳转应用页面的方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0bce41f286c3fe2099dedaaba517cea884ba862538acf0bd630b6846d031d401
---

## 问题现象

使用Notification Kit发送消息如何为通知添加行为意图并实现跳转到应用指定页面？

## 背景知识

当发布通知时，如果期望用户可以通过点击通知栏拉起目标应用组件或发布公共事件，可以通过Ability Kit申请[WantAgent](../harmonyos-guides/notification-with-wantagent.md)封装至通知消息中。

## 解决方案

1. 代码中申请通知权限。

   ```screen
   enableNotifications() {
     let requestEnableNotificationCallback = (err: BusinessError): void => {
       if (err) {
         hilog.error(0x0000, 'testTag',
           `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
       } else {
         hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
       }
     };
     notificationManager.requestEnableNotification(this.context, requestEnableNotificationCallback);
   }
   ```
2. [创建WantAgentInfo信息](../harmonyos-guides/notification-with-wantagent.md#开发步骤)并填写需要拉起的应用bundleName和abilityName（应用只能设置自己应用的bundleName和abilityName），然后构造NotificationRequest对象并发布通知。

   ```screen
   Button('点击发送通知消息').onClick(() => {
     let wantAgentObj: WantAgent;
     let wantAgentInfo: wantAgent.WantAgentInfo = {
       wants: [
         {
           deviceId: '',
           bundleName: 'com.example.s_20250401090433411329', // 自己项目的包名
           abilityName: 'EntryAbility',
           action: '',
           entities: [],
           uri: '',
           parameters: {
             targetPage: 'Index2' // 添加目标页面参数
           }
         }
       ],
       actionType: wantAgent.OperationType.START_ABILITY,
       requestCode: 0,
       wantAgentFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
     };
     wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
       if (err) {
         hilog.error(DOMAIN_NUMBER, TAG, `Failed to get want agent. Code is ${err.code}, message is ${err.message}`);
         return;
       }
       hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in getting want agent.');
       wantAgentObj = data;
       // 构造NotificationRequest对象
       let notificationRequest: notificationManager.NotificationRequest = {
         content: {
           notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
           normal: {
             title: 'Test_Title',
             text: 'Test_Text',
             additionalText: 'Test_AdditionalText',
           },
         },
         id: 6,
         label: 'TEST',
         wantAgent: wantAgentObj,
       }
       notificationManager.publish(notificationRequest, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN_NUMBER, TAG,
             `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
           return;
         }
         hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
         try {
           this.getUIContext().getPromptAction().showToast({ message: '消息已发送' })
         } catch (error) {
           console.error(`error:${error.message}`)
         }
       });
     });
   })
   ```

3. 在EntryAbility.ets文件中添加方法实现[目标UIAbility热启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability热启动)和[目标UIAbility冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)用来获取点击消息通知后的WantAgentInfo信息并实现跳转指定页面。
   * 热启动代码，在应用已启动的情况下实现点击消息通知后会从应用当前所在页面跳转到指定页面。

     ```screen
     // 热启动
     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       // 通过want.parameters获取参数
       const targetPage = want.parameters?.targetPage;
       console.info(`onNewWant Received parameter: ${targetPage}`)
     // 根据参数执行逻辑（例如跳转页面）
     if (targetPage === 'Index2') {
       // 跳转到Index2页面
       this.uiContext?.getRouter().pushUrl({
         url: 'pages/Index2'
       }).catch((error: BusinessError) => {
         console.error(`error:${error.message}`)
       });
     }
     }
     ```
   * 冷启动代码，实现点击消息通知会启动应用并直接跳转指定页面。

     ```screen
     // 冷启动
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (error) {
         console.error(`error:${error.message}`)
       }
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
       this.funcAbilityWant = want;
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       let url = 'pages/Index';
       if (this.funcAbilityWant?.parameters?.targetPage === 'Index2') {
         url = 'pages/Index2';
       }
       console.info(`url:${url}`)
       windowStage.loadContent(url, (err) => {
         if (err.code) {
           hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
           return;
         }
         try {
           this.uiContext = windowStage.getMainWindowSync().getUIContext();
         } catch (error) {
           console.error(`error:${error.message}`)
         }
         hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
       });
     }
     ```

4. 新增Index2页面的步骤：右键工程中的Pages文件夹，然后选择New，接着点击Page最后点击New Page，输入Index2即可创建Page页面文件Index2.ets。
5. 模拟点击消息跳转页面步骤：
   * 冷启动：发送消息后，在多任务页面终止应用，再点击消息实现跳转应用指定页面Index2。
   * 热启动：发送消息后，将应用返回后台，再点击消息实现跳转应用指定页面Index2。

Index.ets代码。

```screen
import { common, wantAgent, WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { notificationManager } from '@kit.NotificationKit';

const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  // Start solution1
  enableNotifications() {
    let requestEnableNotificationCallback = (err: BusinessError): void => {
      if (err) {
        hilog.error(0x0000, 'testTag',
          `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
      } else {
        hilog.info(0x0000, 'testTag', `[ANS] requestEnableNotification success`);
      }
    };
    notificationManager.requestEnableNotification(this.context, requestEnableNotificationCallback);
  }

  // End solution1
  aboutToAppear(): void {
    this.enableNotifications()
  }

  build() {
    Column({ space: 10 }) {
      Text('页面一')
        .fontSize(40)
        .fontWeight(FontWeight.Bold)
      // Start solution2
      Button('点击发送通知消息').onClick(() => {
        let wantAgentObj: WantAgent;
        let wantAgentInfo: wantAgent.WantAgentInfo = {
          wants: [
            {
              deviceId: '',
              bundleName: 'com.example.s_20250401090433411329', // 自己项目的包名
              abilityName: 'EntryAbility',
              action: '',
              entities: [],
              uri: '',
              parameters: {
                targetPage: 'Index2' // 添加目标页面参数
              }
            }
          ],
          actionType: wantAgent.OperationType.START_ABILITY,
          requestCode: 0,
          wantAgentFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
        };
        wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
          if (err) {
            hilog.error(DOMAIN_NUMBER, TAG, `Failed to get want agent. Code is ${err.code}, message is ${err.message}`);
            return;
          }
          hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in getting want agent.');
          wantAgentObj = data;
          // 构造NotificationRequest对象
          let notificationRequest: notificationManager.NotificationRequest = {
            content: {
              notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
              normal: {
                title: 'Test_Title',
                text: 'Test_Text',
                additionalText: 'Test_AdditionalText',
              },
            },
            id: 6,
            label: 'TEST',
            wantAgent: wantAgentObj,
          }
          notificationManager.publish(notificationRequest, (err: BusinessError) => {
            if (err) {
              hilog.error(DOMAIN_NUMBER, TAG,
                `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
              return;
            }
            hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
            try {
              this.getUIContext().getPromptAction().showToast({ message: '消息已发送' })
            } catch (error) {
              console.error(`error:${error.message}`)
            }
          });
        });
      })
      // End solution2
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 页面间转场动画，在热启动场景下点击通知消息跳转到目标页面时，使用该动画可优化跳转体验
  pageTransition() {
    PageTransitionExit({ type: RouteType.Push, duration: 200 })
      .slide(SlideEffect.Left)
  }
}
```

EntryAbility.ets代码。

```screen
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  funcAbilityWant: Want | undefined = undefined;
  uiContext: UIContext | undefined = undefined;

  // Start solution3
  // 热启动
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 通过want.parameters获取参数
    const targetPage = want.parameters?.targetPage;
    console.info(`onNewWant Received parameter: ${targetPage}`)
    // 根据参数执行逻辑（例如跳转页面）
    if (targetPage === 'Index2') {
      // 跳转到Index2页面
      this.uiContext?.getRouter().pushUrl({
        url: 'pages/Index2'
      }).catch((error: BusinessError) => {
        console.error(`error:${error.message}`)
      });
    }
  }

  // End solution3
  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  // Start solution4
  // 冷启动
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (error) {
      console.error(`error:${error.message}`)
    }
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    this.funcAbilityWant = want;
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    let url = 'pages/Index';
    if (this.funcAbilityWant?.parameters?.targetPage === 'Index2') {
      url = 'pages/Index2';
    }
    console.info(`url:${url}`)
    windowStage.loadContent(url, (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      try {
        this.uiContext = windowStage.getMainWindowSync().getUIContext();
      } catch (error) {
        console.error(`error:${error.message}`)
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  // End solution4
  onWindowStageDestroy(): void {
    // Main window is destroyed,release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

## 常见FAQ

Q：wantAgentInfo中的deviceId有什么作用？

A：deviceId表示运行指定Ability的设备ID。如果未设置该字段，则表明指定本设备。

Q：点击消息通知，在EntryAbility中如何使用Navigation进行路由跳转？

A：Navigation作为组件，子页面想要做路由需要拿到Navigation持有的导航控制器对象NavPathStack，首先通过全局的AppStorage接口设置获取NavPathStack。

```screen
struct Index {
  pathStack: NavPathStack = new NavPathStack();
  // 全局设置一个NavPathStack
  aboutToAppear(): void {
    AppStorage.setOrCreate('PathStack', this.pathStack);
  }
  build() {
    Navigation(this.pathStack) {
      // ...
    }.title('Navigation')
    .mode(NavigationMode.Stack)
  }
}

// Navigation子页面
export struct PageOne {
  // 子页面中获取全局的NavPathStack
  pathStack: NavPathStack = AppStorage.get('PathStack') as NavPathStack;
  build() {
    NavDestination() {
      // ...
    }
    .title('PageOne')
  }
}
```

在EntryAbility中，点击消息通知，使用Navigation跳转页面，分以下情况：

* 热启动：此时Navigation已存在并且AppStorage已存储，在EntryAbility中可以直接获取并跳转。
* 冷启动：首先执行EntryAbility中的onCreate，使用AppStorage存储下需要跳转的Url和参数信息。

  当执行到Navigation根页面pathStack存在时，在aboutToAppear中获取到Url和参数进行跳转。
