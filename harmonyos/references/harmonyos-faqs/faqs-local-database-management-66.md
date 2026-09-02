---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-66
title: 如何在卡片和应用间共享UI状态
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何在卡片和应用间共享UI状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:fc2ecb3ac7c37458ed55645e3ea53db8ba64e663644c3af58229137ed1e37ebf
---

## 问题现象

以计数器为例，在应用内和卡片中的计数可以同步增加或减少。如何在卡片和应用间共享UI状态？

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* [@ohos.commonEventManager (公共事件模块)](../harmonyos-references/js-apis-commoneventmanager.md)提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及退订公共事件。
* [formProvider.getPublishedRunningFormInfos](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfos20)获取设备上当前应用程序所有已经加载到桌面的卡片信息。
* [formProvider.updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)更新指定的卡片。

## 解决方案

**解决方案一：**

由于卡片与应用属于不同进程，所以选择使用commonEventManager公共事件模块，分别在主应用端和卡片端发布、订阅公共事件，实现UI状态共享。

1. 创建src/main/ets/utils/SubscriberClass.ets，将其作为工具类，提供订阅和发布公共事件方法。

   ```ts
   import commonEventManager from '@ohos.commonEventManager';

   class SubscriberClass {
     subscriber?: commonEventManager.CommonEventSubscriber;
     publishCount: number = 0;

     publish(eventType: string, data: string = '') {
       commonEventManager.publish(eventType, { data }, () => {
         console.error(`发布失败`);
       });
     }

     subscribe(eventType: string, callback: (event: string) => void) {
       // 1.创建订阅者
       commonEventManager.createSubscriber({ events: [eventType] }, (err, data) => {
         if (err) {
           return console.info('logData:', '创建订阅者失败');
         }
         // 2.data是订阅者
         this.subscriber = data;
         if (this.subscriber) {
           // 3.订阅事件
           commonEventManager.subscribe(this.subscriber, (err, data) => {
             if (err) {
               return console.info('logData:', '订阅者事件失败');
             }
             if (data.data) {
               callback(data.data);
             }
           });
         }
       });
     }
   }

   export const subscriberClass = new SubscriberClass();
   ```
2. 在主应用的aboutToAppear方法中订阅来自卡片发布的事件，同时分别在新增和减少按钮的点击事件中发布应用内数量变更事件。

   ```ts
   import { subscriberClass } from '../utils/SubscriberClass';

   @Component
   @Entry
   struct Index {
     @State count: number = 0;

     aboutToAppear(): void {
       // 订阅来自卡片发布的事件
       subscriberClass.subscribe('appUpdate', (event) => {
         this.count = Number(event);
       });
     }

     build() {

       Row({ space: 10 }) {
         Button('-')
           .width(80)
           .onClick(() => {
             // 减少计数器
             this.count--;
             // 发布事件
             subscriberClass.publish('cardUpdate', this.count.toString());
           });

         Text(this.count.toString());

         Button('+')
           .width(80)
           .onClick(() => {
             // 增加计数器
             this.count++;
             // 发布事件
             subscriberClass.publish('cardUpdate', this.count.toString());
           });
       }.width('100%').height('100%').justifyContent(FlexAlign.Center);
     }
   }
   ```
3. 在卡片生命周期EntryFormAbility的onAddForm生命周期和onFormEvent生命周期分别订阅和发布公共事件。

   ```ts
   import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';
   import { subscriberClass } from '../utils/SubscriberClass';

   interface Param {
     count: number,
     params: string,
     action: string
   }

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       // Called to return a FormBindingData object.
       let formData = '';
       let formId: string = want.parameters![formInfo.FormParam.IDENTITY_KEY] as string;
       // 订阅公共事件
       subscriberClass.subscribe('cardUpdate', (event) => {
         formProvider.updateForm(formId, formBindingData.createFormBindingData({
           count: event
         })).catch(() => {
           console.error('卡片更新失败了');
         });
       });
       return formBindingData.createFormBindingData(formData);
     }

     onCastToNormalForm(formId: string) {
       // Called when the form provider is notified that a temporary form is successfully
       // converted to a normal form.
       console.info('onCastToNormalForm', formId);
     }

     onUpdateForm(formId: string) {
       // Called to notify the form provider to update a specified form.
       console.info('onUpdateForm', formId);
     }

     onFormEvent(formId: string, message: string) {
       // Called when a specified message event defined by the form provider is triggered.
       console.info('onFormEvent', formId);
       // 发布公共事件
       let param = JSON.parse(message) as Param;
       subscriberClass.publish('appUpdate', param.count.toString());
     }

     onRemoveForm(formId: string) {
       // Called to notify the form provider that a specified form has been destroyed.
       console.info('onRemoveForm', formId);
     }

     onAcquireFormState(want: Want) {
       console.info('onAcquireFormState', want.bundleName);
       return formInfo.FormState.READY;
     }
   };
   ```
4. 在卡片页面接收来自应用的数据，并通过postCardAction事件发布计数器数据变化。

   ```ts
   const localStorage = new LocalStorage();

   @Entry(localStorage)
   @Component
   struct WidgetCard {
     @LocalStorageProp('count')
     count: number = 0;

     build() {
       Column() {
         Row({ space: 10 }) {
           Button('-')
             .width(80)
             .onClick(() => {
               this.count--;
               postCardAction(this, {
                 'action': 'message',
                 params: {
                   count: this.count
                 }
               });
             });

           Text(this.count.toString());

           Button('+')
             .width(80)
             .onClick(() => {
               this.count++;
               postCardAction(this, {
                 'action': 'message',
                 params: {
                   count: this.count
                 }
               });
             });
         };
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

**解决方案二：**

当主应用需要将数据同步至卡片时，在主应用中可通过[formProvider.getPublishedRunningFormInfos](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfos20)接口首先获取设备上当前应用程序所有已经加载到桌面的卡片信息，然后通过[formProvider.updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口对指定的卡片进行更新；

当卡片需要将数据同步至主应用时，与方案一致，通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md)的message事件触发卡片onFormEvent生命周期，然后发布公共事件。

1. 创建src/main/ets/utils/SubscriberClass.ets，并将其作为工具类。

   ```ts
   import commonEventManager from '@ohos.commonEventManager';

   class SubscriberClass {
     subscriber?: commonEventManager.CommonEventSubscriber;
     publishCount: number = 0;

     publish(eventType: string, data: string = '') {
       commonEventManager.publish(eventType, { data }, () => {
         console.error(`发布失败`);
       });
     }

     subscribe(eventType: string, callback: (event: string) => void) {
       // 1.创建订阅者
       commonEventManager.createSubscriber({ events: [eventType] }, (err, data) => {
         if (err) {
           return console.info('logData:', '创建订阅者失败');
         }
         // 2.data是订阅者
         this.subscriber = data;
         if (this.subscriber) {
           // 3.订阅事件
           commonEventManager.subscribe(this.subscriber, (err, data) => {
             if (err) {
               return console.info('logData:', '订阅者事件失败');
             }
             if (data.data) {
               callback(data.data);
             }
           });
         }
       });
     }
   }

   export const subscriberClass = new SubscriberClass();
   ```
2. 在主应用的aboutToAppear方法中订阅来自卡片发布的事件，同时获取当前设备当前应用已上桌的卡片，过滤出需要更新的卡片信息。对计数器的值使用@Watch进行监听，当发送变化时，通过updateForm方法更新卡片。

   ```ts
   import { subscriberClass } from '../utils/SubscriberClass';
   import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Component
   @Entry
   struct Index {
     @Watch('countChange') @State count: number = 0;
     updateForms: formInfo.RunningFormInfo[] = [];

     aboutToAppear(): void {
       // 订阅来自卡片发布的事件
       subscriberClass.subscribe('appUpdate', (event) => {
         this.count = Number(event);
       });

       // 获取已上桌的卡片
       formProvider.getPublishedRunningFormInfos().then((data: formInfo.RunningFormInfo[]) => {
         console.info(`formProvider getPublishedRunningFormInfos, data: ${JSON.stringify(data)}`);
         // 过滤出需要同步更新的卡片，可以根据卡片名称
         this.updateForms = data.filter((item) => item.formName === 'widget');
       }).catch((error: BusinessError) => {
         console.error(`promise error, code: ${error.code}, message: ${error.message})`);
       });

     }

     build() {
       Row({ space: 10 }) {
         Button('-')
           .width(80)
           .onClick(() => {
             // 减少计数器
             this.count--;
           });

         Text(this.count.toString());

         Button('+')
           .width(80)
           .onClick(() => {
             // 增加计数器
             this.count++;
           });
       }.width('100%').height('100%').justifyContent(FlexAlign.Center);
     }

     // 计数器变化监听
     countChange() {
       // 遍历卡片
       this.updateForms.forEach((item) => {
         // 值更新
         formProvider.updateForm(item.formId, formBindingData.createFormBindingData({
           count: this.count
         }), (error: BusinessError) => {
           if (error) {
             console.error(`formProvider updateForm callback error, code: ${error.code}, message: ${error.message})`);
             return;
           }
           console.info(`formProvider updateForm success`);
         });
       });
     }
   }
   ```
3. 在卡片生命周期EntryFormAbility的onFormEvent生命周期发布公共事件，无需像步骤一那样订阅发布事件。

   ```ts
   import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';
   import { subscriberClass } from '../utils/SubscriberClass';

   interface Param {
     count: number,
     params: string,
     action: string
   }

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       // Called to return a FormBindingData object.
       let formId: string = want.parameters![formInfo.FormParam.IDENTITY_KEY] as string;
       console.info('onAddForm', formId);
       const formData = '';
       return formBindingData.createFormBindingData(formData);
     }

     onCastToNormalForm(formId: string) {
       // Called when the form provider is notified that a temporary form is successfully
       // converted to a normal form.
       console.info('onCastToNormalForm', formId);
     }

     onUpdateForm(formId: string) {
       // Called to notify the form provider to update a specified form.
       console.info('onUpdateForm', formId);
     }

     onFormEvent(formId: string, message: string) {
       // Called when a specified message event defined by the form provider is triggered.
       let param = JSON.parse(message) as Param;
       subscriberClass.publish('appUpdate', param.count.toString());
     }

     onRemoveForm(formId: string) {
       // Called to notify the form provider that a specified form has been destroyed.
       console.info('onRemoveForm', formId);
     }

     onAcquireFormState(want: Want) {
       // Called to return a {@link FormState} object.
       console.info('onAcquireFormState', want.bundleName);
       return formInfo.FormState.READY;
     }
   };
   ```
4. 在卡片页面接收来自应用的数据，并通过postCardAction事件发布计数器数据变化。

   ```ts
   const localStorage = new LocalStorage();

   @Entry(localStorage)
   @Component
   struct WidgetCard {
     @LocalStorageProp('count')
     count: number = 0;

     build() {
       Column() {
         Row({ space: 10 }) {
           Button('-')
             .width(80)
             .onClick(() => {
               this.count--;
               postCardAction(this, {
                 'action': 'message',
                 params: {
                   count: this.count
                 }
               });
             });

           Text(this.count.toString());

           Button('+')
             .width(80)
             .onClick(() => {
               this.count++;
               postCardAction(this, {
                 'action': 'message',
                 params: {
                   count: this.count
                 }
               });
             });
         };
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

## 常见FAQ

Q：通过AppStorage为何无法在应用与卡片间共享UI状态？

A：AppStorage支持应用主线程中多个UIAbility实例之间的状态共享。AppStorage是与UI相关的数据，必须在UI线程中运行，无法与其他线程共享。卡片运行在独立进程（FormExtensionAbility），与主应用进程内存隔离，直接访问AppStorage会导致数据获取失败或同步异常。

Q：使用公共事件模块实现卡片和应用间共享UI状态有什么缺陷？

A：FormExtensionAbility创建后10秒内无操作将会被清理。如果FormExtensionAbility被清理后，从主应用更新卡片将单向失败，而卡片更新主应用仍可正常进行。

## 总结

* 解决方案一通过公共事件模块实现卡片和应用间共享UI状态，该方法在主应用和卡片间实现方式统一，方案简洁，但是当卡片进程消亡后，主应用无法再同步数据至卡片。
* 解决方案二为了对方案一进行改进，在主应用同步数据至卡片时采用调用卡片更新接口的方式进行实现。而该方案当主应用从任务列表清除再冷启动时，无法同步卡片最后更新的数据，需要考虑采用持久化方案。
