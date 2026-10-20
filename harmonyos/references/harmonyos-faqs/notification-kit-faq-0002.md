---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/notification-kit-faq-0002
title: 用户通知服务常见问题
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 常见问题 > 用户通知服务常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:35+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:da2c03d932dcbb99a9f5a45b3326e6c84c493400b34976b229fb2d7855d652ef
---

**Q：配置了用户通知服务后，横幅通知没有显示，如何配置应用以启用横幅通知？**

**A**：完整流程如下：

1. 可通过[requestEnableNotification](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerrequestenablenotification10)的错误码判断用户是否授权。若返回的错误码为1600004，即为拒绝授权。

   ```ts
   notificationManager.isNotificationEnabled().then((data: boolean) => {
         hilog.info(DOMAIN_NUMBER, TAG, 'isNotificationEnabled success, data: ' + JSON.stringify(data));
         if (!data) {
           notificationManager.requestEnableNotification(this.context).then(() => {
             hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
           }).catch((err: BusinessError) => {
             if (1600004 === err.code) {
               hilog.error(DOMAIN_NUMBER, TAG,
                 `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
             } else {
               hilog.error(DOMAIN_NUMBER, TAG,
                 `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
             }
           });
         }
       }).catch((err: BusinessError) => {
         hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
       });
   ```
2. 拉起应用的通知设置界面，引导用户打开横幅通知。

   ```ts
   notificationManager.openNotificationSettings(this.context).then(() => {
         hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
       }).catch((err: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
       });
   ```

   补充说明，从HarmonyOS 7.0 beta版本开始，支持通过[notificationManager.getNotificationSetting()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagergetnotificationsetting20)获取当前应用通知设置状态，返回的NotificationSetting中bannerEnabled表示横幅通知开启状态。如未开启横幅通知，可调用[notificationManager.openNotificationSettingsWithResult()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettingswithresult)拉起应用通知设置页面，用户完成设置后会返回NotificationSetting，根据bannerEnabled判断是否开启了横幅通知。

   ```ts
   notificationManager.getNotificationSetting().then((data: notificationManager.NotificationSetting) => {
     hilog.info(DOMAIN_NUMBER, TAG, `getNotificationSetting success, data: ${JSON.stringify(data)}`);
     if (!data.bannerEnabled) {
       const context = this.getUIContext().getHostContext();
       if (context) {
         let uiAbilityContext: common.UIAbilityContext = context as common.UIAbilityContext;
         notificationManager.openNotificationSettingsWithResult(uiAbilityContext)
           .then((result: notificationManager.NotificationSetting) => {
             hilog.info(DOMAIN_NUMBER, TAG,
               `[ANS] openNotificationSettingsWithResult success, result: ${JSON.stringify(result)}`);
           }).catch((err: BusinessError) => {
             hilog.error(DOMAIN_NUMBER, TAG,
               `[ANS] openNotificationSettingsWithResult failed, code is ${err.code}, message is ${err.message}`);
           });
       }
     }
   }).catch((err: BusinessError) => {
     hilog.error(DOMAIN_NUMBER, TAG, `getNotificationSetting failed, code is ${err.code}, message is ${err.message}`);
   });
   ```
3. 构造SlotType为SOCIAL\_COMMUNICATION或SERVICE\_INFORMATION类型的NotificationRequest对象，并发布通知。

   ```ts
   let notificationRequest: notificationManager.NotificationRequest = {
         id: 1,
         content: {
           notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT, // 普通文本类型通知
           normal: {
             title: 'test_title',
             text: 'Notification published',
             additionalText: 'test_additionalText',
           },
         },
         // 设置通知渠道类型为社交通信SOCIAL_COMMUNICATION或者SERVICE_INFORMATION
         notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
       };
       notificationManager.publish(notificationRequest, (err: BusinessError) => {
         if (err) {
           hilog.error(DOMAIN_NUMBER, TAG,
             `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
           return;
         }
         hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
       });
   ```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/UbQ6GmDnSrCbHiP6Jo3CKg/zh-cn_image_0000002765215712.png "点击放大")

完整代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { notificationManager } from '@kit.NotificationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  checkNotificationPermission() {
    notificationManager.isNotificationEnabled().then((data: boolean) => {
      hilog.info(DOMAIN_NUMBER, TAG, 'isNotificationEnabled success, data: ' + JSON.stringify(data));
      if (!data) {
        notificationManager.requestEnableNotification(this.context).then(() => {
          hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
        }).catch((err: BusinessError) => {
          if (1600004 === err.code) {
            hilog.error(DOMAIN_NUMBER, TAG,
              `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
          } else {
            hilog.error(DOMAIN_NUMBER, TAG,
              `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
          }
        });
      }
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
    });
  }

  openNotificationSetting() {
    notificationManager.openNotificationSettings(this.context).then(() => {
      hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag',
        `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
    });
  }

  publishNotification() {
    let notificationRequest: notificationManager.NotificationRequest = {
      id: 1,
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT, // 普通文本类型通知
        normal: {
          title: 'test_title',
          text: 'Notification published',
          additionalText: 'test_additionalText',
        },
      },
      // 设置通知渠道类型为社交通信SOCIAL_COMMUNICATION或者SERVICE_INFORMATION
      notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
    };
    notificationManager.publish(notificationRequest, (err: BusinessError) => {
      if (err) {
        hilog.error(DOMAIN_NUMBER, TAG,
          `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
        return;
      }
      hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
    });
  }

  aboutToAppear(): void {
    this.checkNotificationPermission();
  }

  build() {
    Column({ space: 10 }) {
      Button('publish')
        .onClick(() => {
          this.publishNotification();
        })
      Button('点击拉起应用设置页面')
        .onClick(() => {
          this.openNotificationSetting();
        })
    }
    .padding({ right: '16px', left: '16px' })
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

**Q：APP处于前台时，三方推送通知会横幅展示，如何不进行展示？**

**A**：推送通知扩展消息需要申请场景化消息权益，申请该权益存在限制该场景化消息仅为有商家新订单提醒、商家收款场景的应用开放，其他场景不支持该能力。若您的应用进程在前台，则不弹出通知提醒，您可以在应用进程中获取通知扩展消息内容并自行完成业务处理，具体参考：[发送通知扩展消息](../harmonyos-guides/push-send-extend-noti.md)。

**Q：横幅通知上划后，再次调用不会弹出横幅通知，是什么原因？**

**A**：用户有横幅通知的上划动作，从不过于打扰用户的方面考虑，一分钟内不再弹出横幅，但是通知的响铃提示音在此期间是可以正常提示的；一分钟之后，如果有新消息通知的话，才会继续弹出横幅。

**Q：应用是否可以主动关闭推送通知扩展消息的横幅通知？**

**A**：在用户同意应用横幅通知情况下，当前应用服务端推送通知扩展消息给应用时，应用无法主动关闭横幅通知。如果应用想实现某些特殊使用场景下，不进行推送，可以将应用状态传递给服务端，服务端过滤掉这些设备，不进行推送。

**Q：如何在代码中判断横幅通知是否已开启？**

**A**：从HarmonyOS 7.0 beta版本开始，可调用[notificationManager.getNotificationSetting()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagergetnotificationsetting20)获取当前应用通知设置状态，返回的NotificationSetting中bannerEnabled字段表示横幅通知开启状态。如未开启，可调用[notificationManager.openNotificationSettingsWithResult()](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettingswithresult)拉起应用通知设置页面，用户完成设置后会返回更新后的NotificationSetting，根据bannerEnabled判断是否已开启横幅通知。

**Q：使用Notification Kit发送消息如何为通知添加行为意图并实现跳转到应用指定页面？**

A：实现跳转应用指定页面的方案如下：

1. 代码中申请通知权限：

   ```ts
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
2. [为通知添加行为意图](../harmonyos-guides/notification-with-wantagent.md)并填写需要拉起的应用bundleName和abilityName（应用只能设置自己应用的bundleName和abilityName），然后构造NotificationRequest对象并发布通知：

   ```ts
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
   * 热启动代码，在应用已启动的情况下实现点击消息通知后会从应用当前所在页面跳转到指定页面：

     ```ts
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
   * 冷启动代码，实现点击消息通知会启动应用并直接跳转指定页面：

     ```ts
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

完整代码如下：

* Index.ets代码：

  ```ts
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

    aboutToAppear(): void {
      this.enableNotifications()
    }

    build() {
      Column({ space: 10 }) {
        Text('页面一')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
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
* EntryAbility.ets代码：

  ```ts
  import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { window } from '@kit.ArkUI';

  export default class EntryAbility extends UIAbility {
    funcAbilityWant: Want | undefined = undefined;
    uiContext: UIContext | undefined = undefined;

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

    onDestroy(): void {
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    }

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

**Q：wantAgentInfo中的deviceId有什么作用？**

**A**：deviceId表示运行指定Ability的设备ID。如果未设置该字段，则表明指定本设备。

**Q：为什么调用方法[notificationManager.publish](../harmonyos-references/js-apis-notificationmanager.md#notificationmanagerpublish)时，通知栏没有通知显示？在notificationManager.publish方法下通过catch获取到报错信息401：Invalid parameter。**

**A**：方法notificationManager.[NotificationRequest](../harmonyos-references/js-apis-inner-notification-notificationrequest.md)中参数wantAgent类型为[WantAgent](../harmonyos-references/js-apis-app-ability-wantagent.md)，而当传递的参数类型为[WantAgentInfo](../harmonyos-references/js-apis-inner-wantagent-wantagentinfo.md)时，则会导致通知栏没有通知显示。

**Q：点击消息通知，在EntryAbility中如何使用Navigation进行路由跳转？**

**A**：Navigation作为组件，子页面想要做路由需要拿到Navigation持有的导航控制器对象NavPathStack，首先通过全局的AppStorage接口设置获取NavPathStack。

```ts
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

热启动：此时Navigation已存在并且AppStorage已存储，在EntryAbility中可以直接获取并跳转。

冷启动：首先执行EntryAbility中的onCreate，使用AppStorage存储下需要跳转的Url和参数信息，

当执行到Navigation根页面pathStack存在时，在aboutToAppear中获取到Url和参数进行跳转。
