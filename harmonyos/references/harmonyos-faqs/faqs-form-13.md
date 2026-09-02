---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-13
title: 主应用如何获取卡片列表中某个卡片添加/移除
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 主应用如何获取卡片列表中某个卡片添加/移除
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2fe1aca6c8e01b63f166163bb1176a402c83cb2858ca5c40ff818641ad5d09ad
---

## 问题现象

如何记录真正添加到桌面的卡片，卡片被添加/移除时如何通知主应用？

## 背景知识

* [FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)为卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调；由于服务卡片和主应用是两个不同进程，所以需要借助持久化、进程间通信等方法来通知主应用卡片添加/移除。
  + [FormExtensionAbility.onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform)：卡片提供方接收创建卡片的通知接口。
  + [FormExtensionAbility.onRemoveForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonremoveform)：卡片提供方接收销毁卡片的通知接口。
  + [FormExtensionAbility.onCastToNormalForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityoncasttonormalform)：卡片提供方接收临时卡片转常态卡片的通知接口。
* [用户首选项（Preferences）](../harmonyos-guides/data-persistence-by-preferences.md)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。当用户希望有一个全局唯一存储的地方，可以采用用户首选项来进行存储。
* [commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber)支持用户自定义的公共事件，可用于实现跨进程的事件通信能力。

## 解决方案

**一、卡片添加/移除的场景以及相关卡片生命周期：**

目前卡片添加/移除至桌面没有直接的回调响应，可以通过onAddForm和onRemoveForm相结合记录保存到桌面的卡片。

onAddForm/onRemoveForm添加至桌面的生命周期触发流程如下：

1. 长按应用图标->服务卡片->打开卡片列表，触发onAddForm（卡片列表中有几张卡片生命周期就会回调onAddForm几次）

   例如：打开下面的卡片列表，卡片列表中有3张卡片，可以看到日志中onAddForm回调了3次。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/BC361PdyRZONjxGWASSSeQ/zh-cn_image_0000002628631646.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/fs4u2TqWRzS9qCT1Fl83tQ/zh-cn_image_0000002658870921.png "点击放大")
2. 长按应用图标->服务卡片->打开卡片列表->服务卡片列表取消，触发onRemoveForm（卡片列表中有几张卡片生命周期就会回调触发onRemoveForm几次）

   例如：点击x号取消了服务卡片列表，则会触发onRemoveForm回调3次。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/gVFlX-eoSxelxHZdM4cOoA/zh-cn_image_0000002628791552.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/wFyJoDy_Tg-p8vhkSXG_1w/zh-cn_image_0000002658990861.png "点击放大")
3. 长按应用图标->服务卡片->打开卡片列表->选择一张卡片添加到桌面（选中卡片将回调onUpdateForm，其余卡片回调onRemoveForm）

   例如：添加一张卡片至桌面，则会onUpdateForm选中的卡片，onRemoveForm另外两张卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/LeEp6ZfrTFuCyB-sQIIunA/zh-cn_image_0000002628631648.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/_FOElj4fSQ-0ET8DmlhguQ/zh-cn_image_0000002658870923.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Ef9R009YTMu7Qd0Xbjwteg/zh-cn_image_0000002628791554.png "点击放大")
4. 桌面上移除某一张卡片（选中移除卡片将回调onRemoveForm）

   例如：在桌面移除一张卡片，会onRemoveForm当前移除的卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/mmitB8nvS7WoHyYVffyN3w/zh-cn_image_0000002658990863.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/kjlJ5AZ5QzuNTrdHNsMi0w/zh-cn_image_0000002628631652.png "点击放大")

综上，将卡片添加至桌面的流程中，生命周期回调onAddForm/onRemoveForm会执行多次，但是最终卡片新增还是移除是确定的。

**二、实现卡片添加/移除管理以及主应用获取卡片id：**

本方案使用首选项通过在服务卡片中onAddForm/onRemoveForm回调函数中，对formId进行持久化缓存，并在主应用中进行跨进程读取。以下是实现步骤：

前置步骤[创建服务卡片](../harmonyos-guides/ide-service-widget.md#section111689357301)请参考官网，不再赘述。

1. 实现一个公共的单例首选项类以供服务卡片/主应用共同使用，需要注意的是，这里首选项对于跨进程的场景下，需要使用同一个context上下文对象，后面在调用处均使用了this.context.getApplicationContext()保持统一。src\main\ets\common\PreferencesHelper.ets：

   ```ts
   import { preferences } from '@kit.ArkData';

   // 公共模块PreferencesHelper.ets用于存取formId
   export class PreferencesHelper {
     private static instance: PreferencesHelper | null = null;

     private constructor() {}

     public static getInstance() {
       if (PreferencesHelper.instance === null) {
         PreferencesHelper.instance = new PreferencesHelper();
       }
       return PreferencesHelper.instance;
     }

     public get(context: Context, key: string, defaultValue: preferences.ValueType) {
       preferences.removePreferencesFromCacheSync(context, 'preferences');
       let preference = preferences.getPreferencesSync(context, { name: 'preferences' });
       return preference.getSync(key, defaultValue);
     }

     public put(context: Context, key: string, defaultValue: preferences.ValueType) {
       preferences.removePreferencesFromCacheSync(context, 'preferences');
       let preference = preferences.getPreferencesSync(context, { name: 'preferences' });
       preference.putSync(key, defaultValue);
       preference.flushSync();
     }
   }
   ```
2. 在EntryAbility中的onCreate中进行存储applicationContext用于UI页面使用：

   src\main\ets\entryability\EntryAbility.ets：

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       AppStorage.setOrCreate('AppContext', this.context.getApplicationContext());
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   }
   ```
3. 当长按应用图标拉起应用卡片列表时以及在卡片列表中选择一张服务卡片时，会触发onAddForm回调，此时将卡片id保存下来；服务卡片列表取消时或者在桌面移除卡片时，会触发onRemoveForm，此时将记录里对应的数据删除，首选项中剩余的即是添加到桌面的卡片。（注意：formlist需要做去重）src\main\ets\entryformability\EntryFormAbility.ets：

   ```ts
   import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
   import { Want } from '@kit.AbilityKit';
   import { commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { PreferencesHelper } from '../common/PreferencesHelper';

   const DOMAIN = 0x0000;

   export default class EntryFormAbility extends FormExtensionAbility {
     // 服务卡片FormExtensionAbility.ets，添加formId
     onAddForm(want: Want) {
       let formList: Array<string> =
         PreferencesHelper.getInstance().get(this.context.getApplicationContext(), 'formList', []) as Array<string>;
       if (want.parameters) {
         let formId = (want.parameters['ohos.extra.param.key.form_identity']) as string;
         hilog.info(DOMAIN, 'testTag', `add formId: ${formId}`);
         if (!formList.includes(formId)) {
           formList.push(formId);
         }
         PreferencesHelper.getInstance().put(this.context.getApplicationContext(), 'formList', formList);
       }
       const formData = '';
       return formBindingData.createFormBindingData(formData);
     }

     onCastToNormalForm() {
       // Called when the form provider is notified that a temporary form is successfully
       // converted to a normal form.
     }

     onUpdateForm() {
       // Called to notify the form provider to update a specified form.
       hilog.info(DOMAIN, 'testTag', `onUpdateForm`);
     }

     onFormEvent() {
       // Called when a specified message event defined by the form provider is triggered.
     }

     // 服务卡片FormExtensionAbility.ets，移除formId
     onRemoveForm(formId: string) {
       // Called to notify the form provider that a specified form has been destroyed.
       let formList: Array<string> =
         PreferencesHelper.getInstance().get(this.context.getApplicationContext(), 'formList', []) as Array<string>;
       formList = formList.filter(item => item !== formId);
       hilog.info(DOMAIN, 'testTag', `del formId: ${formId}`);
       PreferencesHelper.getInstance().put(this.context.getApplicationContext(), 'formList', formList);
       commonEventManager.publish('delCard', { data: formId, bundleName: 'com.example.formKit_preferences' }, err => {
         if (err) {
           hilog.info(DOMAIN, 'testTag', `onRemoveForm publish fail, errCode: ${err.code}, errMsg: ${err.message}`);
         }
         hilog.info(DOMAIN, 'testTag', 'onRemoveForm publish success');
       });
     }

     onAcquireFormState() {
       // Called to return a {@link FormState} object.
       return formInfo.FormState.READY;
     }
   };
   ```
4. 在主应用中通过PreferencesHelper.getInstance().get('formList', [])对formId进行查询（注意：主应用需要和卡片使用同一个context）。

   src\main\ets\pages\Index.ets：

   ```ts
   import { commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { PreferencesHelper } from '../common/PreferencesHelper';

   const DOMAIN = 0x0000;

   @Entry
   @Component
   struct Index {
     private subscriber: commonEventManager.CommonEventSubscriber | null = null;
     private subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
       events: ['delCard'],
     };

     aboutToAppear(): void {
       this.subscriber = commonEventManager.createSubscriberSync(this.subscribeInfo);
       if (this.subscriber) {
         commonEventManager.subscribe(this.subscriber, (err, data) => {
           if (err) {
             hilog.info(DOMAIN, 'testTag', `delCard err: ${err}`);
           }
           hilog.info(DOMAIN, 'testTag', `delCard 传递的数据: ${data.data}`);
         });
       }
     }

     build() {
       RelativeContainer() {
         Text('Hello World')
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             // 主应用Index.ets，在主应用中对formId进行读取
             let formList: Array<string> = PreferencesHelper.getInstance().get(AppStorage.get('AppContext') as Context,
               'formList', []) as Array<string>;
             hilog.info(DOMAIN, 'testTag', `formList size ${formList.length}`);
             for (let index = 0; index < formList.length; index++) {
               const element = formList[index];
               hilog.info(DOMAIN, 'testTag', `formId ${element}`);
             }
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

## 常见FAQ

Q：跨进程读取首选项（以主应用读取服务卡片写入的首选项为例）为何读取不到？

A：由于context不同，跨模块、多页面场景下可能无法获取数据。建议在EntryAbility中使用单例类存储全局context，或使用应用级context。

Q：是否可以使用commonEventManager来进行跨进程监听服务卡片的卡片列表中某个卡片添加/移除？

A：该方案可以监听到服务卡片变化，但是在主应用未启动或者重启等场景下，因为主应用进程不存在，导致无法实时监听变化，所以不推荐该方案。

Q：是否可以使用PersistentStorage和AppStorage在应用和卡片之间进行状态数据共享？

A：卡片和应用的主进程不是一个进程，而AppStorage是和进程绑定的，仅支持应用的主线程内多个UIAbility实例间的UI状态数据共享，所以卡片和应用主进程之间无法使用PersistentStorage和AppStorage进行状态数据共享。

Q：服务卡片生命周期里的onCastToNormalForm方法，在什么时候执行？

A：[onCastToNormalForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityoncasttonormalform)在[卡片使用方](../harmonyos-guides/formkit-overview.md#服务卡片架构)将临时卡片转换为常态卡片时触发，可能涉及数据固化、权限申请或状态同步至服务端。参考[管理ArkTS卡片生命周期](../harmonyos-guides/arkts-ui-widget-lifecycle.md)，onCastToNormalForm事件是否能触发，取决于是否有卡片使用方使用，当前主要卡片使用方就是桌面；由于当前桌面不会使用临时卡片，所以真机上暂时没有场景触发卡片提供方的onCastToNormalForm。

Q：删除form\_config.json中的卡片配置并重新安装应用后，原卡片仍显示在桌面？

A：可以修改AppScope/app.json5文件下的versionCode版本号。

Q：为什么在添加卡片时，onUpdateForm函数有时会被触发，有时无法触发？

A：onUpdateForm函数是卡片提供方接收更新参数通知的接口。该函数的触发行为与系统版本相关：在API 20之前的版本中添加卡片时，该函数不会被触发；而在API 20及后续版本添加卡片时会正常触发。为确保兼容性，建议开发者在onAddForm函数及onUpdateForm函数中同时处理初始化（如初始化首选项）及卡片更新逻辑，这样可保证在不同系统版本下卡片功能的稳定性。

Q：卡片的formId是不是固定的？

A：卡片的formId在创建以后是固定的。在HarmonyOS的服务卡片开发中，formId作为卡片的唯一标识符，用于标识不同的服务卡片。这样设计确保了卡片的身份在整个生命周期中的一致性和可识别性。

Q：服务卡片进程里面读取应用进程的首选项数据，只读取不写入会有文件损坏的风险吗？

A：服务卡片进程里面读取应用进程的首选项数据，只读取不写入不会损坏文件。

Q：能否根据卡片的formName更新卡片信息？

A：对于当前应用程序相同moduleName、abilityName、formName的卡片，多次加桌后会每张卡片会有不同的卡片id。卡片提供方可以通过[formProvider.reloadForms接口](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderreloadforms22)批量更新不同的卡片id但moduleName、abilityName、formName相同的卡片。

Q：应用卡片内部组件能使用装饰器吗？如@State、@Provide、@Prop等传递数据。

A：卡片内通过@State等修饰的数据是可以改变的。

## 总结

主应用获取服务卡片的卡片列表中某个卡片添加/移除的场景下，首先要注意卡片的onAddForm/onRemoveForm事件的系统回调的触发时机；其次由于卡片和主应用是跨进程的所以需要借助首选项进行跨进程读取。
