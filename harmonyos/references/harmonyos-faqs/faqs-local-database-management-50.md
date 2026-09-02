---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-50
title: preferences实现数据跨进程读取
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > preferences实现数据跨进程读取
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5024d6ce53b6fa096a4a7098a9188afa508e8a89fb179e9a61f852d026cebd53
---

## 问题现象

应用进程的token数据通过PersistentStorage存储，在卡片进程通过AppStorage获取，获取不到token数据。

## 背景知识

* [PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)是应用程序中的可选单例对象。此对象的作用是持久化存储选定的AppStorage属性，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。
* AppStorage是应用全局的UI状态存储，是和应用的进程绑定的。AppStorage支持应用的主线程内多个UIAbility实例间的状态共享。AppStorage是UI相关的数据，需要运行在UI线程，[无法将对象共享到其他线程](faqs-arkui-49.md)。
* [卡片数据交互](../best-practices/bpta-card-update-and-data-interaction.md)应用可以通过[formProvider.updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)函数更新指定的卡片。
* [用户首选项](../harmonyos-references/js-apis-data-preferences.md)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

## 解决方案

AppStorage不适合跨进程共享数据。此场景“应用与卡片之间数据传递”可以基于用户首选项来实现跨进程数据共享。具体实现示例如下：

1. UI进程，Index文件存储首选项值代码如下：

   ```ts
   import { preferences } from '@kit.ArkData';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     message: string = '持久化存储';

     // 创建一个使用preferences持久化的方法
     save() {
       let dataPreferences: preferences.Preferences | null = null;
       // 通过调用preferences.getPreferences()实现获取一个名为myStore的的首选项对象
       preferences.getPreferences(this.getUIContext().getHostContext(), 'myStore',
         (err: BusinessError, val: preferences.Preferences) => {
           if (err) {
             console.error('Failed to get preferences. code =', err.code, ', message =', err.message);
             return;
           }
           dataPreferences = val;
           try {
             // 通过同步处理dataPreferences.putSync方法存储一个键值对，键为token，值为'123123'
             dataPreferences.putSync('token', '123123');
             console.info('Succeeded in putting value of token.');
             // 数据持久化到存储中
             dataPreferences?.flushSync();
             console.info('Succeeded in flushing.');
           } catch (err) {
             console.error('Failed to preferences. code =', err.code, ', message =', err.message);
           }
         });
     }

     build() {
       RelativeContainer() {
         Button(this.message)
           .id('HelloWorld')
           .fontSize(18)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             // 数据持久化存储
             this.save();
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. 卡片获取首选项值，详情代码如下：

   ```ts
   import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
   import { preferences } from '@kit.ArkData';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class EntryFormAbility extends FormExtensionAbility {
     // 服务卡片生命周期的一个方法，当服务卡片被添加到前台时触发
     onAddForm() {
       let context = this.context;
       let dataPreferences: preferences.Preferences | null = null;
       // 调用getPreferences方法同步获取首选项对象
       preferences.getPreferences(context, 'myStore', (err: BusinessError, val: preferences.Preferences) => {
         if (err) {
           console.error('Failed to get preferences. code =', err.code, ', message =', err.message);
           return;
         }
         // 将获取的首选项对象赋值给dataPreferences变量
         dataPreferences = val;
         try {
           // 使用getSync方法同步获取名为token的首选项值，如果找不到该值，则使用default作为默认值。
           let promise = dataPreferences.getSync('token', 'default');
           console.info('Succeeded in getting preferences. Data: ', promise);
         } catch (err) {
           console.error('Failed to get preferences. code =' + err.code, ', message =', err.message);
         }
       });
       // 创建并返回一个表单绑定数据对象，用于将数据绑定到服务卡片的视图层
       return formBindingData.createFormBindingData('');
     }

     onAcquireFormState() {
       // Called to return a {@link FormState} object.
       return formInfo.FormState.READY;
     }
   }
   ```

   实现效果：上述代码实现token数据存入myStore文件，文件内容为token的值：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/6BPITkYKRKi3HpYuzLspkw/zh-cn_image_0000002628899082.png "点击放大")

## 常见FAQ

Q：首选项是否可以多进程并发使用？

A：不允许deletePreferences与其他接口多线程、多进程并发调用，否则可能会发生不可预期行为。详情参考官网[约束限制](../harmonyos-guides/data-persistence-by-preferences.md#约束限制)。

Q：distributedKVStore （分布式键值数据库）与首选项的区别是什么？

A：若需跨设备数据同步或单设备处理复杂业务逻辑，选择distributedKVStore，若仅需单设备轻量级存储（如配置项），优先使用Preferences。
