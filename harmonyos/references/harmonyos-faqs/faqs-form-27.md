---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-27
title: 卡片数据更新时应用内数据不会自动更新
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 卡片数据更新时应用内数据不会自动更新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:9c7898d4f394aa160bfbcb9daf7e3ba429fe161beb20dae517f8cc27ab791880
---

## 问题现象

点击桌面卡片的待办事项，更新为已完成，然后进入应用内发现该待办事项还是未完成状态，需要下拉刷新一下页面才显示已完成。

## 背景知识

* [卡片拉起应用UIAbility到后台（call事件）](../harmonyos-guides/arkts-ui-widget-event-call.md)：在卡片中使用postCardAction接口的call能力，能够将卡片提供方应用的指定的UIAbility拉到后台。同时，call能力提供了调用应用指定方法、传递数据的功能，使应用在后台运行时可以通过卡片上的按钮执行不同的功能。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)是应用程序中的一个特殊的单例LocalStorage对象，是应用级的数据库，和进程绑定，通过@StorageProp和@StorageLink装饰器可以和组件联动。

## 问题定位

1. 检测应用是否在卡片中使用了postCardAction接口的call能力，可以在hilog日志中搜索'Callee onRemoteMessageRequest'进行判断。

   ```txt
   09-12 14:03:06.561   52704-52704   A03D00/com.exa...ication/JSAPP  com.examp...lication  I     Ability::onCallRequest callee is object [object Object]
   09-12 14:03:06.567   52704-52704   A03D00/com.exa...ication/JSAPP  com.examp...lication  I     Callee onRemoteMessageRequest code [number 1]
   09-12 14:03:06.568   52704-52704   A03D00/com.exa...ication/JSAPP  com.examp...lication  I     Callee onRemoteMessageRequest code proc
   09-12 14:03:06.568   52704-52704   A03D00/com.exa...ication/JSAPP  com.examp...lication  I     Callee onRemoteMessageRequest method [funA]
   09-12 14:03:06.575   52704-52704   A03D00/com.exa...ication/JSAPP  com.examp...lication  I     Callee onRemoteMessageRequest code proc Packed data
   09-12 14:03:06.575   52704-52704   A03D00/com.exa...ication/JSAPP  com.examp...lication  I     Callee onRemoteMessageRequest code proc success
   ```
2. 检查应用代码逻辑，在call事件的回调函数中，是否对卡片更新的数据使用AppStorage进行全局的UI状态存储。并且检查应用内的页面中是否使用@StorageLink或@StorageProp对AppStorage中对应的属性建立数据同步。

## 分析结论

1. 应用没有在卡片中使用postCardAction接口的call能力，所以卡片进程的数据变化无法同步给主进程。
2. 应用页面中展示的数据没有使用全局UI状态存储，并进行双向绑定，导致页面数据无法实时更新。

## 修改建议

1. 首先参考[创建ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)在工程中创建动态卡片。
2. 配置后台运行权限。call事件存在约束限制，卡片提供方应用需要在module.json5下添加后台运行权限。

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
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
           "name": "EntryFormAbility",
           "srcEntry": "./ets/entryformability/EntryFormAbility.ets",
           "label": "$string:EntryFormAbility_label",
           "description": "$string:EntryFormAbility_desc",
           "type": "form",
           "metadata": [
             {
               "name": "ohos.extension.form",
               "resource": "$profile:form_config"
             }
           ]
         }
       ],
       "requestPermissions":[
         {
           "name": "ohos.permission.KEEP_BACKGROUND_RUNNING"
         }
       ]
     }
   }
   ```
3. 添加卡片到桌面，EntryFormAbility实现如下：

   ```ts
   import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       if (!want || !want.parameters) {
         return formBindingData.createFormBindingData('');
       }
       let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
       let formData: Record<string, string> = {
         'formId': formId
       };
       return formBindingData.createFormBindingData(formData);
     }
   };
   ```
4. 点击卡片更新数据时，在卡片页面调用postCardAction向指定UIAbility发送call事件，并根据实际的业务需求进行传参。

   ```ts
   let storageUpdateCall = new LocalStorage();

   @Entry(storageUpdateCall)
   @Component
   struct WidgetExampleCard {
     @LocalStorageProp('title') title: string = 'title';
     @LocalStorageProp('detail') detail: string = '未更新.';
     @LocalStorageProp('formId') formId: string = '';

     build() {
       Row() {
         Column() {
           Text(this.title)
             .fontSize(14)
             .fontWeight(FontWeight.Medium)
             .fontColor($r('sys.color.font'));
           Text(this.detail)
             .fontSize(14)
             .fontWeight(FontWeight.Medium)
             .fontColor($r('sys.color.font'));
           // 卡片按钮点击事件
           Button('更新数据')
             .onClick(() => {
               postCardAction(this, {
                 action: 'call',
                 // 只能跳转到当前应用下的UIAbility，与module.json5中定义保持一致
                 abilityName: 'EntryAbility',
                 params: {
                   formId: this.formId,
                   // 需要调用的方法名称
                   method: 'funA',
                   newData: 'new title', // 修改后的数据
                   detail: '已更新',
                   formEvent: 'DATA_CHANGE' // 自定义事件类型
                 }
               });
             });
         }
         .width('100%');
       }
       .height('100%')
       .backgroundColor($r('sys.color.comp_background_primary'));
     }
   }
   ```
5. 在指定的UIAbility中监听call事件，根据监听到的method参数中的方法名称调用对应方法，并通过rpc.Parcelable获取参数，使用AppStorage进行全局的UI状态存储。

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { rpc } from '@kit.IPCKit';
   import { formBindingData, formProvider } from '@kit.FormKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;
   // ipc通信返回类型的实现，用于数据序列化和反序列化
   class MyParcelable implements rpc.Parcelable {
     num: number;
     str: string;

     constructor(num: number, str: string) {
       this.num = num;
       this.str = str;
     }

     marshalling(messageSequence: rpc.MessageSequence): boolean {
       messageSequence.writeInt(this.num);
       messageSequence.writeString(this.str);
       return true;
     }

     unmarshalling(messageSequence: rpc.MessageSequence): boolean {
       this.num = messageSequence.readInt();
       this.str = messageSequence.readString();
       return true;
     }
   }

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       // 监听call事件所需的方法并调用
       this.callee.on('funA', this.callUpdateFunc);
     }

     private callUpdateFunc = (data: rpc.MessageSequence): MyParcelable => {
       let params: Record<string, string> = JSON.parse(data.readString());
       if (params.formEvent === 'DATA_CHANGE') {
         AppStorage.setOrCreate('title', params.newData);
         AppStorage.setOrCreate('detail', params.detail);
         if (params.formId !== undefined) {
           // 更新卡片显示
           const bindData = formBindingData.createFormBindingData({
             'title': params.newData,
             'detail': params.detail
           });
           formProvider.updateForm(params.formId, bindData).catch((err: BusinessError) => {
             console.error(`更新卡片失败: ${params.formId}, ${err.code}, ${err.message}`);
           });
         }
       }
       return new MyParcelable(1, 'aaa');
     };

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
       try {
         this.callee.off('funA');
       } catch (err) {
         hilog.info(DOMAIN, 'testTag', '%{public}s', JSON.stringify(err));
       }
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         AppStorage.setOrCreate('title', 'title');
         AppStorage.setOrCreate('detail', '未更新');
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }
   }
   ```
6. 在应用页面内使用@StorageLink对AppStorage中对应的属性建立数据同步，使页面数据同步更新。

   ```ts
   @Entry
   @Component
   struct Index {
     @StorageLink('title') title: string = '';
     @StorageLink('detail') detail: string = '';

     build() {
       Column({space: 20}) {
         Text(`卡片内容：${this.title}`)
           .fontSize(20)
           .margin(10)
         Text(`描述：${this.detail}`)
           .fontSize(20)
           .margin(10)
       }
       .height('100%')
       .width('100%')
       .padding(20)
     }
   }
   ```
