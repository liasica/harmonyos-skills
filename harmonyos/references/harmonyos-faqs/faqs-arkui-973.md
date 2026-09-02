---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-973
title: 如何实现EmbeddedComponent和EmbeddedUIExtensionAbility之间的双向通信
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现EmbeddedComponent和EmbeddedUIExtensionAbility之间的双向通信
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:80c043625a6a59a846d7b9904fbd9810746aa488cddadfb23c6bc4b9f3590e21
---

## 问题现象

EmbeddedComponent和EmbeddedUIExtensionAbility之间进程隔离，目前官网[场景示例](../harmonyos-guides/arkts-embedded-components.md#场景示例)只提供了[terminateSelfWithResult](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)方法，没有提供更多资料参考，如何实现EmbeddedComponent和EmbeddedUIExtensionAbility之间的双向通信？

## 背景知识

* [EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)：EmbeddedComponent组件用于在当前页面嵌入本应用内其他EmbeddedUIExtensionAbility提供的UI。
* [EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)：提供方应用中定义使用，用于实现跨进程界面嵌入功能，仅能被同应用的UIAbility拉起，并需在多进程权限的场景下使用。
* [@ohos.commonEventManager (公共事件模块)](../harmonyos-references/js-apis-commoneventmanager.md)：提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及退订公共事件，可用于实现跨进程的事件通信能力。

## 解决方案

EmbeddedComponent和EmbeddedUIExtensionAbility属于两个进程，可以利用commonEventManager进行双向通信，详细步骤如下：

1. 在项目的ets/extensionAbility（extensionAbility目录需要手动创建）目录下新建EmbeddedUIExtensionAbility，代码如下：

   ```ts
   import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

   const TAG: string = '[ExampleEmbeddedAbility]';

   export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
     onCreate() {
       console.info(TAG, `onCreate`);
     }

     onForeground() {
       console.info(TAG, `onForeground`);
     }

     onBackground() {
       console.info(TAG, `onBackground`);
     }

     onDestroy() {
       console.info(TAG, `onDestroy`);
     }

     onSessionCreate(want: Want, session: UIExtensionContentSession) {
       try {
         console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
       } catch (error) {
         console.info(TAG, `error`);
       }
       let param: Record<string, UIExtensionContentSession> = {
         'session': session
       };
       let storage: LocalStorage = new LocalStorage(param);
       // 加载pages/extension.ets页面内容
       session.loadContent('pages/Extension', storage);
     }

     onSessionDestroy() {
       console.info(TAG, `onSessionDestroy`);
     }
   };
   ```
2. 在项目main\_pages.json中增加声明Extension：

   ```json
   {
     "src": [
       "pages/Index",
       "pages/Extension"
     ]
   }
   ```
3. 在module.json5配置文件的"extensionAbilities"标签下增加ExampleEmbeddedAbility配置：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "tablet",
         "2in1"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         }
       ],
       "extensionAbilities": [
         {
           "name": "EntryBackupAbility",
           "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         },
         {
           "name": "ExampleEmbeddedAbility",
           "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
           "type": "embeddedUI"
         }
       ]
     }
   }
   ```
4. 在Index页面中实现主页面UI布局并且接收来自EmbeddedUIExtensionAbility的信息：

   ```ts
   import { Want } from '@kit.AbilityKit';
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

   let options: commonEventManager.CommonEventPublishData = {
     code: 0,
     data: 'Hello',
     isOrdered: true // 有序公共事件
   };

   @Entry
   @Component
   struct Index {
     @State message: string = 'Message from ExampleEmbeddedAbility: ';
     private want: Want = {
       bundleName: 'com.example.mycommon',
       abilityName: 'ExampleEmbeddedAbility',
     };

     aboutToAppear(): void {
       // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
       let subscriber: commonEventManager.CommonEventSubscriber;
       // 订阅者信息
       let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
         events: ['event']
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
                   (err: BusinessError, data: commonEventManager.CommonEventData) => {
                     if (err) {
                       console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                       return;
                     }
                     let receiveData = JSON.parse(JSON.stringify(data)) as commonEventManager.CommonEventPublishData;
                     this.message += receiveData.data;
                     console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
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

     build() {
       Row() {
         Column() {
           Text(this.message).fontSize(20);
           Button('发送数据')
             .width('80%')
             .onClick(() => {
               try {
                 commonEventManager.publish('event2', options, (err: BusinessError) => {
                   if (err) {
                     console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
                     return;
                   }
                   console.info(`Succeeded in publishing common event.`);
                 });
               } catch (error) {
                 let err: BusinessError = error as BusinessError;
                 console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
               }
             });
           Text('EmbeddedComponent').fontSize(20);
         }
         .width('50%')
         .height(300)
         .justifyContent(FlexAlign.SpaceBetween)
         .borderColor(Color.Orange)
         .borderWidth(2);

         Column() {
           EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
             .width('100%')
             .height('100%')
             .onError((error) => {
               // 失败或异常触发onError回调，文本框显示如下报错内容
               this.message = 'Error: code = ' + error.code;
             });
         }
         .width('50%')
         .height(300)
         .borderColor(Color.Blue)
         .borderWidth(2)
         .margin({ left: 5 });

       }
       .height('100%')
       .width('100%');

     }
   }
   ```

   注意：bundleName需要和项目的包名一致。
5. 在Extension页面中实现EmbeddedComponent的UI布局并且发送事件信息：

   ```ts
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

   // 公共事件相关信息，以发布有序公共事件为例
   let options: commonEventManager.CommonEventPublishData = {
     code: 0,
     data: 'Good',
     isOrdered: true // 有序公共事件
   };

   @Entry
   @Component
   struct Extension {
     @State message: string = 'Message from EmbeddedComponent: ';

     aboutToAppear(): void {
       // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
       let subscriber: commonEventManager.CommonEventSubscriber;
       // 订阅者信息
       let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
         events: ['event2']
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
                   (err: BusinessError, data: commonEventManager.CommonEventData) => {
                     if (err) {
                       console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
                       return;
                     }
                     let receiveData = JSON.parse(JSON.stringify(data)) as commonEventManager.CommonEventPublishData;
                     this.message += receiveData.data;
                     console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
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

     build() {
       Column() {
         Text(this.message).fontSize(20);
         Button('发送数据')
           .width('80%')
           .onClick(() => {
             // 发布公共事件
             try {
               commonEventManager.publish('event', options, (err: BusinessError) => {
                 if (err) {
                   console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
                   return;
                 }
                 console.info(`Succeeded in publishing common event.`);
               });
             } catch (error) {
               let err: BusinessError = error as BusinessError;
               console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
             }
           });
         Text('ExampleEmbeddedAbility').fontSize(20);
       }.width('100%').height('100%').justifyContent(FlexAlign.SpaceBetween);
     }
   }
   ```
