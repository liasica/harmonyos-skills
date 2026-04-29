---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-card-update-and-data-interaction
title: 卡片更新与数据交互
breadcrumb: 最佳实践 > 应用框架 > 服务卡片 > 卡片更新与数据交互
category: best-practices
scraped_at: 2026-04-29T14:10:55+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5d9dd6e16a87a097220d3868696eb430bc819b965da7426bf459fa8d0701f9ef
---

## 概述

服务卡片给用户提供一目了然的信息内容，具有易用可见、智能可选和多端可变的特点，提供给用户简洁、高效的体验。系统通过[卡片开发服务](../harmonyos-guides/form-kit.md)（Form Kit），提供了丰富的服务卡片开发能力，涵盖了卡片的创建、交互、更新与管理等多个方面，使开发者能够高效完成个性化服务卡片的开发。

**图1** 天气卡片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/QYODolzKRMKoJQGnCuijIg/zh-cn_image_0000002427681508.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=732863AA9290A2F9989342C3FFAE1E52E376EC8A8EA77CD25CC321ECF80D62B0 "点击放大")

### 卡片更新场景

服务卡片通常用于展示最新的信息或数据。通过卡片更新机制，开发者可以确保卡片上展示的内容是最新的，从而满足用户对实时信息的需求。例如，新闻应用可以通过更新卡片来展示最新的新闻标题和摘要，天气应用可以通过更新卡片来提供最新的天气信息。

卡片更新的频率和策略直接影响用户体验。如果卡片内容长时间不更新，用户可能会认为应用不活跃或不可靠，从而降低对应用的信任度和使用频率。相反，通过合理的卡片更新机制，可以保持卡片内容的新鲜感和吸引力，提升用户的使用体验和满意度。

通常需要进行卡片数据加载或卡片更新的场景有以下几种类型：

**表1** 卡片更新场景

| 场景类型 | 场景描述 | | |
| --- | --- | --- | --- |
| 主动刷新 | * 添加卡片时，初始化卡片数据。 例如，从桌面添加卡片，弹出卡片预览弹窗时，进行卡片数据初始化加载。 | * 卡片UI交互时，进行卡片更新。 例如，点击卡片刷新按钮，更新卡片推荐内容；音乐类卡片点击播放按钮，拉起应用至后台播放音乐，更新播放按钮状态。 | * 应用侧交互引起变化，更新数据到卡片。 例如，在应用侧点击收藏按钮改变文章的收藏状态时，同步更新卡片的收藏状态。 |
| 被动刷新 | * 定时更新、定点更新以及指定下次刷新时间间隔更新。例如，定时更新新闻卡片的推荐内容。 | | |

本文将以[实现卡片更新与数据交互功能](https://gitcode.com/harmonyos_samples/CardInfoRefresh)示例应用为例，介绍卡片数据交互流程、如何实现常见的卡片更新场景以及卡片更新开发过程中的常见问题和注意事项。

## 实现原理

### 卡片运行机制简介

**图2** 卡片提供方和使用方  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/gMvbVHa9TwOLnNO-8QoaEw/zh-cn_image_0000002461241349.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=D6A98B3EC38C820AB3E6A5CC53FD0F9863F1D5646817234AC35AAA309DBDA605 "点击放大")

以天气卡片为例，天气应用作为[卡片提供方](../harmonyos-guides/formkit-overview.md#服务卡片架构)，提供天气卡片的显示内容、控件布局和卡片交互处理逻辑。例如，天气卡片显示地点、温度和天气情况，点击卡片跳转至天气应用等。此时，桌面作为[卡片使用方](../harmonyos-guides/formkit-overview.md#服务卡片架构)，即卡片的宿主应用，控制天气卡片在桌面中展示的位置并展示卡片内容。ArkTS服务卡片的实现依赖ArkTS卡片框架的能力，卡片框架管理卡片生命周期和刷新机制，负责卡片页面的渲染。如下图所示，卡片提供方和使用方都依赖于卡片框架，天气应用提供的天气卡片，其添加、删除和刷新依赖框架的卡片管理服务，桌面展示天气卡片内容依赖框架的卡片渲染服务。关于卡片提供方、使用方和卡片框架的详细内容可参考[ArkTS卡片实现原理](../harmonyos-guides/arkts-form-overview.md#实现原理)。

**图3** 卡片运行机制示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/vZpaFUUqRGCk6KhvxLAGIQ/zh-cn_image_0000002461241901.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=C4ACA69226C8579ECEEBFF6C26AF97AF2EF8E9A8A1DDE29ADC42536D0940064D "点击放大")

### 卡片数据交互

卡片更新场景的实现，依赖于[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)生命周期、[formProvider模块](../harmonyos-references/js-apis-app-form-formprovider.md)提供的[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口和卡片框架提供的卡片刷新机制。如下图所示，应用主进程和应用的卡片进程是两个独立的进程，应用主进程持有[UIAbility](../harmonyos-guides/uiability.md)，应用的卡片进程持有[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)。卡片的UI页面由系统服务统一进行渲染，由卡片使用方（例如桌面）进行呈现。如果卡片数据不依赖于应用主进程，在卡片进程中使用卡片框架能力就能实现卡片更新。如果卡片数据依赖于应用主进程，应用主进程使用[FormProvider模块](../harmonyos-references/js-apis-app-form-formprovider.md)提供的[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口更新卡片时，需要明确卡片ID，所以卡片ID在添加卡片时需要进行存储，此类场景下需要借助卡片框架和数据存储等系统能力，保证应用主进程和卡片进程的卡片ID数据一致性。

**图4** 应用主进程与卡片进程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/HDEyUqabTJWhxb6CSNdGcA/zh-cn_image_0000002427844140.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=1D2EC0E7456C8237B3CB2F5D73A1FFD789019C878533E93144755D5C184AE920 "点击放大")

本文主要介绍由卡片或应用UI交互引起的、由系统刷新机制定时或定点触发的[卡片更新场景](bpta-card-update-and-data-interaction.md#section430210710274)。一般情况下，卡片实现这几种常见场景就可以满足用户对卡片信息更新的诉求。还有一类是需要实时更新信息的应用卡片，例如出行打车类卡片，用户对信息的实时性要求很高，这类场景可以通过[Push Kit（推送服务）](../harmonyos-guides/push-kit-guide.md)的能力来实现，详细可参考[推送卡片刷新消息](../harmonyos-guides/push-form-update.md)。

## 卡片数据初始化

### 场景描述

添加卡片时需要对卡片进行数据初始化，卡片创建及卡片配置参考[ArkTS卡片开发指导](../harmonyos-guides/arkts-ui.md)，本章节将对卡片数据初始化的流程进行介绍。

**图5** 卡片预览页  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/XbsZvjRwSqqezlA7yyFGgg/zh-cn_image_0000002194011496.png?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=53BCA7B3C05FE88DA46C59009CC63E0BC84B204DCCC6D132857609ECB0652AF0 "点击放大")

### 开发流程

添加卡片时，卡片数据初始化流程：

**图6** 卡片数据初始化流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/mBwHEZunTAGE9yPxAPkuZw/zh-cn_image_0000002461363873.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=E6A4E5E594D7EB857E6AF73FF6339C1279AC09421F3AFB5D1B6814A54A75E44D "点击放大")

桌面长按应用图标待展示卡片列表时，首先触发[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)生命周期接口onAddForm()。使用卡片参数枚举[FormParam](../harmonyos-references/js-apis-app-form-forminfo.md#formparam)可以从生命周期接口onAddForm()的入参[want](../harmonyos-references/js-apis-app-ability-want.md)中取出卡片的相关信息如卡片标识、卡片名称、卡片宽高等。针对必要的信息可以进行判断或者保存等操作。

```
1. import { Want } from '@kit.AbilityKit';
2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. // ...
5. const TAG: string = 'EntryFormAbility';

7. export default class EntryFormAbility extends FormExtensionAbility {
8. onAddForm(want: Want): formBindingData.FormBindingData {
9. if (!want || !want.parameters) {
10. hilog.error(0x0000, TAG, `FormAbility onAddForm want or want.parameters is undefined`);
11. return formBindingData.createFormBindingData('');
12. }
13. do {
14. let formName: string = want.parameters[formInfo.FormParam.NAME_KEY] as string;
15. let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
16. // ...
17. } while (0);
18. return formBindingData.createFormBindingData('');
19. }

21. // ...
22. }
```

[EntryFormAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L19-L173)

创建需要返回卡片的数据类，可以是包含若干键值对的Object或JSON格式的字符串。使用卡片数据绑定模块[formBindingData](../harmonyos-references/js-apis-app-form-formbindingdata.md#formbindingdata)的createFormBindingData()接口封装卡片需要使用的数据类，作为生命周期接口onAddForm()的返回值并传递给卡片。

说明：若onAddForm()接口中无法直接构建数据类作为接口返回值初始化卡片，例如依赖数据库查询结果或等待网络数据等使用异步的场景，可以使用[formProvider模块](../harmonyos-references/js-apis-app-form-formprovider.md)提供的[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口将异步获取的数据推送至卡片。

```
1. export class FormData {
2. formId: string = '';
3. formTime: string = '';
4. isFavor?: boolean = false;
5. index?: number = 0;
6. cardList: Array<CardListItemData> = [];

8. constructor(formId: string) {
9. this.formId = formId;
10. }
11. }
```

[CommonData.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/common/CommonData.ets#L42-L52)

```
1. import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
2. import { Want } from '@kit.AbilityKit';
3. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { CardListItemData, CommonData, FormData } from '../common/CommonData';
6. // ...
7. export default class EntryFormAbility extends FormExtensionAbility {
8. onAddForm(want: Want): formBindingData.FormBindingData {
9. if (!want || !want.parameters) {
10. hilog.error(0x0000, TAG, `FormAbility onAddForm want or want.parameters is undefined`);
11. return formBindingData.createFormBindingData('');
12. }
13. do {
14. let formName: string = want.parameters[formInfo.FormParam.NAME_KEY] as string;
15. let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
16. // ...
17. if (formName === 'card_info_refresh') {
18. let formData = new FormData(formId);
19. formData.formTime = systemDateTime.getTime().toString();
20. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
21. return formInfo;
22. }

24. let key: string = `${formId}_show_index`;
25. let data = util.getFormInitData(key, preferences);
26. if (formName === 'card_info_update') {
27. // Save the index of the data items currently displayed on the card.
28. util.preferencesPut(preferences, key, data.id);
29. let formData = new FormData(formId);
30. formData.cardList.push(data);
31. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
32. return formInfo;
33. }
34. } while (0);
35. return formBindingData.createFormBindingData('');
36. }

38. // ...
39. }
```

[EntryFormAbility.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L17-L174)

卡片页面使用页面级的UI状态存储[LocalStorage](../harmonyos-guides/arkts-localstorage.md)接收onAddForm()接口传递的数据。使用装饰器@LocalStorageProp装饰的状态变量接收数据类的详细信息，装饰器@LocalStorageProp(key)中的key值需与数据类的键值一一对应。使用获取的数据初始化卡片页面。

```
1. let storageLocal = new LocalStorage();

3. @Entry(storageLocal)
4. @Component
5. struct WidgetCard {
6. // ...
7. @LocalStorageProp('formTime') @Watch('onFormTimeChange') formTime: string = '';
8. @LocalStorageProp('formId') formId: string = '';
9. // ...
10. onFormTimeChange() {
11. // ...
12. }
13. // ...
14. build() {
15. // ...
16. }
17. }
```

[WidgetCard.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L20-L212)

## 卡片UI交互引起卡片更新

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/l95FfP-gS3CbmKQrS3xSTw/zh-cn_image_0000002229451777.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=73C3AFF886A5802736D4A2C3AE24C419674736D352314CACF5E400089CAB39B6 "点击放大")

一般情况下，简单的卡片UI交互会引起卡片更新。例如，智能家电控制类卡片，通过卡片控制家电开关时，卡片上的开关状态会随设备状态而改变；点击新闻类卡片刷新按钮，从网络获取最新数据更新推荐内容列表。这类更新场景可以[通过message事件](../harmonyos-guides/arkts-ui-widget-event-formextensionability.md)实现，仅在卡片进程就可以完成卡片更新。

### 开发流程

**图7** 卡片UI交互引起更新  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/w9yZF2sjRyiyqvCrlZq1Fg/zh-cn_image_0000002427845712.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=7D51B839EEC71F7F50A47D1EDCD83D91DEA3599CA40BFEA92A4CCDFC429FA3E5 "点击放大")

在卡片页面注册onClick()点击事件，动态卡片使用postCardAction()接口，静态卡片使用FormLink组件触发事件。本文以动态卡片为例，在点击事件回调中调用postCardAction()接口，action参数选择message触发message事件。message事件未设置abilityName参数时，默认拉起FormExtensionAbility。

```
1. Row() {
2. this.buttonBuilder($r('app.string.message'))
3. }
4. .onClick(() => {
5. postCardAction(this, {
6. action: 'message',
7. params: {
8. message: 'Message refresh card.'
9. }
10. });
11. })
```

[WidgetCard.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L172-L182)

message事件拉起FormExtensionAbility后触发onFormEvent()生命周期，构建卡片需要更新的数据类，调用[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口推送数据至卡片。卡片页面中使用[LocalStorageProp](../harmonyos-guides/arkts-localstorage.md#localstorageprop)装饰的状态变量更新后触发卡片更新。

```
1. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { CardListItemData, CommonData, FormData } from '../common/CommonData';
4. // ...
5. const TAG: string = 'EntryFormAbility';

7. export default class EntryFormAbility extends FormExtensionAbility {
8. // ...
9. onFormEvent(formId: string, message: string) {
10. // ...
11. let formData = new FormData(formId);
12. // ...
13. let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
14. formProvider.updateForm(formId, formMsg).then(() => {
15. hilog.info(0x0000, TAG, 'updateForm success.');
16. }).catch((error: Error) => {
17. let err = error as BusinessError;
18. hilog.error(0x0000, TAG, `updateForm failed. error code=${err.code}, message=${err.message}`);
19. });
20. } catch (error) {
21. let err = error as BusinessError;
22. hilog.error(0x0000, TAG, `getSync failed, error code=${err.code}, message=${err.message}`);
23. }
24. }

26. // ...
27. }
```

[EntryFormAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L22-L175)

## 拉起应用至后台时更新卡片

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/xYH74XqaT7WkC4yh6LZ8Tg/zh-cn_image_0000002193851912.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=48334DB14B539CF878323A9ECD29F88A86E47C40F9B841AF1E3CE17B75351E73 "点击放大")

卡片UI交互引起卡片更新，实现和应用在前台时相同的功能。例如，音乐类卡片，点击播放或切换按钮，拉起后台播放音乐，同时更新卡片上的播放状态。这类更新场景可以[通过call事件](../harmonyos-guides/arkts-ui-widget-event-call.md)实现，需要在卡片进程拉起应用主进程至后台时更新卡片。

### 开发流程

**图8** 拉起应用至后台时更新卡片  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/hrO4e-ieSlirH0ZS_YcGQw/zh-cn_image_0000002461364589.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=15978758F115FA5B037FD788ED5B50EDC77064995EFB363207280E8D5F173862 "点击放大")

在卡片页面注册onClick()点击事件，本文以动态卡片为例，在回调中调用postCardAction()接口（静态卡片使用静态用的FormLink），action参数选择call并配置需要调用的方法和传递的数据，触发call事件后台拉起指定UIAbility。配置参数注意以下限制：

* abilityName参数仅支持配置当前应用下的UIAbility，即配置在module.json5文件中的UIAbility。
* method为必选参数，且类型为string类型，用于触发UIAbility中对应的方法。
* 在当前call事件触发指定卡片刷新场景中，需设置formId参数，用于UIAbility接收后更新当前卡片。

```
1. Row() {
2. this.buttonBuilder($r('app.string.call'))
3. }
4. .onClick(() => {
5. postCardAction(this, {
6. action: 'call',
7. abilityName: 'EntryAbility',
8. params: {
9. formId: this.formId,
10. method: 'updateCardInfo',
11. params: {
12. message: 'Call refresh card.'
13. }
14. }
15. });
16. })
```

[WidgetCard.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L153-L168)

在被拉起的UIAbility的onCreate()生命周期中，需要配置监听call事件所需的方法，监听的方法名与call事件配置的method保持一致。通过[readString()](../harmonyos-references/js-apis-rpc.md#readstring9)方法读取传递的字符串值后，使用JSON.parse()解析传递的参数。使用传递的formId并构建更新卡片需要的数据类型，调用[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口推送数据至卡片。

注意，进程退出时需在onDestroy()生命周期中解除监听；监听配置的方法需返回实现rpc.Parcelable()接口的数据类。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
4. import { rpc } from '@kit.IPCKit';
5. import { CardListItemData, CommonData, FormData } from '../common/CommonData';
6. // ...
7. const TAG: string = 'EntryAbility';

9. export default class EntryAbility extends UIAbility {
10. private callFunc = (data: rpc.MessageSequence): MyParcelable => {
11. try {
12. let params: Record<string, string> = JSON.parse(data.readString());
13. if (params.formId !== undefined) {
14. let formId: string = params.formId;
15. let formData = new FormData(formId);
16. let util = PreferencesUtil.getInstance();
17. let preferences = util.getPreferences(this.context);
18. if (!preferences) {
19. return new MyParcelable(1);
20. }
21. let index: number = preferences.getSync(CommonConstants.DATA_INDEX, 0) as number;
22. formData.cardList = CommonData.getData(index);
23. util.preferencesPut(preferences, CommonConstants.DATA_INDEX, index + 1);
24. let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
25. formProvider.updateForm(formId, formMsg).then((data) => {
26. hilog.info(0x0000, TAG, 'updateForm success.', JSON.stringify(data));
27. }).catch((error: Error) => {
28. let err = error as BusinessError;
29. hilog.error(0x0000, TAG, `updateForm failed. error code=${err.code}, message=${err.message}`);
30. });
31. }
32. } catch (error) {
33. let err = error as BusinessError;
34. hilog.error(0x0000, TAG, `callFunc failed, error code=${err.code}, message=${err.message}`);
35. }
36. return new MyParcelable(1);
37. };
38. // ...
39. onCreate(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
40. // ...
41. try {
42. this.callee.on('updateCardInfo', this.callFunc);
43. } catch (error) {
44. let err = error as BusinessError;
45. hilog.error(0x0000, TAG, `on updateCardInfo failed, error code=${err.code}, message=${err.message}`);
46. }
47. // ...
48. }

50. // ...
51. onDestroy(): void {
52. // ...
53. try {
54. this.callee.off('updateCardInfo');
55. // ...
56. } catch (error) {
57. let err = error as BusinessError;
58. hilog.error(0x0000, TAG, `Failed to disconnect callee. Cause: error code=${err.code}, message=${err.message}`);
59. }
60. }

62. // ...
63. }

66. class MyParcelable implements rpc.Parcelable {
67. num: number;

69. constructor(num: number) {
70. this.num = num;
71. }

73. marshalling(dataOut: rpc.MessageSequence): boolean {
74. try {
75. dataOut.writeInt(this.num);
76. } catch (error) {
77. let err = error as BusinessError;
78. hilog.error(0x0000, 'MyParcelable', `marshalling failed, error code=${err.code}, message=${err.message}`);
79. }
80. return true;
81. }

83. unmarshalling(dataIn: rpc.MessageSequence): boolean {
84. try {
85. this.num = dataIn.readInt();
86. } catch (error) {
87. let err = error as BusinessError;
88. hilog.error(0x0000, 'MyParcelable', `unmarshalling failed, error code=${err.code}, message=${err.message}`);
89. }
90. return true;
91. }
92. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L17-L327)

说明

提供方应用需要具备后台运行权限（[ohos.permission.KEEP\_BACKGROUND\_RUNNING](../harmonyos-guides/permissions-for-all.md#ohospermissionkeep_background_running)）。

## 从卡片跳转到应用后更新卡片

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Qsi4aHn7QXe2fhhqbks4uQ/zh-cn_image_0000002193851920.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=3D0383402BEAE7B808E04A20B5D819DAEBEDC1CD867F44AB13758FECC396EAB5 "点击放大")

卡片UI交互跳转至应用后，引起卡片更新。用于定时更新类卡片手动触发卡片更新。例如，天气类卡片，点击卡片跳转至应用，应用实时刷新天气，同时更新卡片展示的天气数据。这类更新场景可以[通过router事件](../harmonyos-guides/arkts-ui-widget-event-router.md)实现，需要从卡片进程跳转至应用主进程后进行卡片更新。

### 开发流程

**图9** 跳转到应用后更新卡片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ihtJ9IkIRuSVV6zlw27H8Q/zh-cn_image_0000002427849920.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=FDFED0510CA657ED2AB093314D461EAB26C6A44B92F4AEC76D84BB9806F6C8E1 "点击放大")

在卡片页面注册onClick()点击事件，在回调中调用postCardAction()接口，action参数选择router触发router事件。router事件拉起指定的UIAbility，使用abilityName进行配置。

```
1. Row(){
2. this.buttonBuilder($r('app.string.router'))
3. }
4. .onClick(() => {
5. postCardAction(this, {
6. action: 'router',
7. abilityName: 'EntryAbility',
8. params: {
9. message: 'Router refresh card.'
10. }
11. });
12. })
```

[WidgetCard.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/widget/pages/WidgetCard.ets#L138-L149)

在UIAbility中接收router事件并获取参数。若UIAbility未在后台运行，触发onCreate生命周期回调。若UIAbility已在后台运行，会触发onNewWant()生命周期回调。生命周期参数want包含卡片相关信息，执行卡片相关操作。判断params中包含的参数，构建卡片更新需要的数据类，调用[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口推送数据至卡片。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
4. import { rpc } from '@kit.IPCKit';
5. import { CardListItemData, CommonData, FormData } from '../common/CommonData';
6. // ...
7. const TAG: string = 'EntryAbility';

9. export default class EntryAbility extends UIAbility {
10. // ...
11. onCreate(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
12. // ...
13. this.updateInfo(want);
14. // ...
15. }

17. // ...
18. onNewWant(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
19. this.updateInfo(want);
20. }

22. private updateInfo(want: Want) {
23. if (!want || !want.parameters || want.parameters[formInfo.FormParam.IDENTITY_KEY] === undefined) {
24. return;
25. }
26. let message: string = (JSON.parse(want.parameters?.params as string))?.message;
27. if (message === 'Router refresh card.') {
28. let formId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
29. let formData = new FormData(formId);
30. // ...
31. let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
32. formProvider.updateForm(formId, formMsg)
33. .then((data) => {
34. hilog.info(0x0000, TAG, 'updateForm success.', JSON.stringify(data));
35. })
36. .catch((error: Error) => {
37. let err = error as BusinessError;
38. hilog.error(0x0000, TAG, `updateForm failed, error code=${err.code}, message=${err.message}`);
39. });
40. } catch (error) {
41. let err = error as BusinessError;
42. hilog.error(0x0000, TAG, `updateInfo failed, error code=${err.code}, message=${err.message}`);
43. }
44. }
45. }

47. // ...
48. }
```

[EntryAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L16-L297)

## 从应用更新数据到卡片

### 场景描述

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/eVeoU1irQ4GnEDMz6ap0WQ/zh-cn_image_0000002193851888.png?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=4679B769667F4047475220D0682AA44DDF5749CD66ACB0E191DE2B8E92857ADE "点击放大")

以应用点击收藏场景为例。卡片展示内容在应用内数据列表中，当点击应用内收藏按钮，收藏状态应同步至卡片。

### 开发流程

应用侧UI交互引起卡片数据变化时：

**图10** 从应用更新数据到卡片流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/flqaSAO2SUWG38mvpAG98A/zh-cn_image_0000002461368797.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061049Z&HW-CC-Expire=86400&HW-CC-Sign=44A2A794778F521EB3DC2CDD42A378D07234F1946FD4952EF18A8E6B4E9A8434 "点击放大")

图片展示卡片创建时，在onAddForm()生命周期中使用首选项保存卡片ID至卡片ID列表及卡片当前状态。

```
1. import { Want } from '@kit.AbilityKit';
2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { CardListItemData, CommonData, FormData } from '../common/CommonData';
5. import { CommonConstants } from '../common/CommonConstants';
6. import { PreferencesUtil } from '../common/utils/PreferencesUtil';

8. const TAG: string = 'EntryFormAbility';

10. export default class EntryFormAbility extends FormExtensionAbility {
11. onAddForm(want: Want): formBindingData.FormBindingData {
12. if (!want || !want.parameters) {
13. hilog.error(0x0000, TAG, `FormAbility onAddForm want or want.parameters is undefined`);
14. return formBindingData.createFormBindingData('');
15. }
16. do {
17. let formName: string = want.parameters[formInfo.FormParam.NAME_KEY] as string;
18. let formId: string = want.parameters[formInfo.FormParam.IDENTITY_KEY] as string;
19. let util = PreferencesUtil.getInstance();
20. let preferences = util.getPreferences(this.context);
21. if (!preferences) {
22. break;
23. }
24. // Save form id using preferences.
25. util.addFormId(preferences, formId);

27. // ...
28. let key: string = `${formId}_show_index`;
29. let data = util.getFormInitData(key, preferences);
30. if (formName === 'card_info_update') {
31. // Save the index of the data items currently displayed on the card.
32. util.preferencesPut(preferences, key, data.id);
33. let formData = new FormData(formId);
34. formData.cardList.push(data);
35. let tempFormInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
36. return tempFormInfo;
37. }
38. } while (0);
39. return formBindingData.createFormBindingData('');
40. }

42. // ...
43. }
```

[EntryFormAbility.ets](https://gitcode.com/HarmonyOS_Samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L20-L176)

应用侧收藏按钮注册onClick()事件，事件回调触发时，使用首选项更新收藏状态，查询当前正在展示该收藏状态变化的数据的卡片，更新收藏状态到对应卡片。

```
1. Row() {
2. // ...
3. }
4. .onClick(() => {
5. let util = PreferencesUtil.getInstance();
6. let preferences = util.getPreferences(this.getUIContext().getHostContext()!);
7. if(!preferences) {
8. return;
9. }
10. this.statusArr[this.itemData.id] = !this.statusArr[this.itemData.id];
11. this.itemData.favour = this.statusArr[this.itemData.id!];
12. util.preferencesPut(preferences, 'statusArr', this.statusArr)

14. // Update page display data.
15. AppStorage.set('statusArr', [...this.statusArr]);

17. let idArr = PreferencesUtil.getInstance().getFormIds(preferences);
18. if (idArr.length > 0) {
19. idArr.forEach((formId: string) => {
20. if (!preferences) {
21. return;
22. }
23. try {
24. if (preferences.getSync(`${formId}_show_index`, -1) as number === this.itemData.id) {
25. let formData = new FormData(formId);
26. formData.cardList = [this.itemData];
27. let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
28. formProvider.updateForm(formId, formMsg).then(() => {
29. hilog.info(0x0000, TAG, `updateForm success.`);
30. }).catch((error: Error) => {
31. let err = error as BusinessError;
32. hilog.error(0x0000, TAG, `updateForm failed: error code=${err.code}, message=${err.message}`);
33. });
34. }
35. } catch (error) {
36. let err = error as BusinessError;
37. hilog.error(0x0000, TAG, `getSync failed, error code=${err.code}, message=${err.message}`);
38. }
39. })
40. }
41. })
```

[Index.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/pages/Index.ets#L91-L142)

## 定时、定点更新卡片

### 场景描述

使用天气类或日历类应用时，卡片需要每日更新当日最新数据，方便用户获取最及时的信息。新闻阅读类卡片展示热点文章列表时，需要随时间变化进行定时更新。

服务卡片支持通过定时刷新及定点刷新的方式实现以上场景。

在使用定时和定点刷新功能之前，需要在form\_config.json配置文件中设置updateEnabled字段为true，以启用周期性刷新功能。出于安全及性能考虑，每张卡片每天最多通过定时方式触发刷新50次，定时刷新包含[卡片配置项updateDuration](../harmonyos-guides/arkts-ui-widget-configuration.md)和调用setFormNextRefreshTime方法两种方式，当达到50次配额后，无法通过定时方式再次触发刷新，刷新次数会在每天的0点重置。

### 开发流程

**定时刷新**

定时刷新表示在指定的时间间隔后自动刷新卡片内容。可以在[form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md)配置文件的updateDuration字段中进行设置。卡片定时刷新的更新周期updateDuration字段的单位为30分钟，即最短为半小时（1 \* 30min）刷新一次。当取值为0时，表示该参数不生效，当取值为正整数N时，表示刷新周期为30\*N分钟。

定时刷新触发后，系统调用onUpdateForm()的生命周期回调函数，使用[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)方法更新卡片内容。

```
1. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { CardListItemData, CommonData, FormData } from '../common/CommonData';
4. // ...
5. export default class EntryFormAbility extends FormExtensionAbility {
6. // ...
7. onUpdateForm(formId: string) {
8. // ...
9. let formData = new FormData(formId);
10. // ...
11. let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
12. formProvider.updateForm(formId, formMsg).catch((err: BusinessError) => {
13. hilog.error(0x0000, TAG, `updateForm failed, error code=${err.code}, message=${err.message}`);
14. });
15. }

17. // ...
18. }
```

[EntryFormAbility.ets](https://gitcode.com/harmonyos_samples/CardInfoRefresh/blob/master/entry/src/main/ets/entryformability/EntryFormAbility.ets#L23-L177)

**定点刷新**

定点刷新表示在每天的某个指定的时间点自动刷新卡片内容。通过在form\_config.json文件中配置scheduledUpdateTime字段实现，例如配置为14:00。定点刷新触发后，系统调用FormExtensionAbility的[onUpdateForm()](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)生命周期回调，相关操作参考定时刷新。

注意，当同时配置了定时刷新updateDuration和定点刷新scheduledUpdateTime时，定时刷新的优先级更高。为实现定点刷新updateDuration需要配置为0，配置大于0的数字时会导致定点刷新不生效。

```
1. {
2. "forms": [
3. {
4. "name": "card_info_refresh",
5. "displayName": "$string:widget_display_name",
6. "description": "$string:widget_desc",
7. "src": "./ets/widget/pages/WidgetCard.ets",
8. "uiSyntax": "arkts",
9. "window": {
10. "designWidth": 720,
11. "autoDesignWidth": true
12. },
13. "colorMode": "auto",
14. "isDynamic": true,
15. "isDefault": true,
16. "updateEnabled": true,
17. "scheduledUpdateTime": "14:00",
18. "updateDuration": 0,
19. "defaultDimension": "4*4",
20. "supportDimensions": [
21. "4*4"
22. ]
23. },
24. // ...
25. ]
26. }
```

更多注意事项参考[卡片定时刷新和定点刷新](../harmonyos-guides/arkts-ui-widget-interaction-overview.md#被动刷新)。

## 常见问题

### 如何刷新指定类型的多个卡片

刷新所有同类卡片首先需要保存同类卡片的formId。在onAddForm()生命周期中，通过判断卡片名称，卡片宽高等信息，识别同类型卡片，将formId分类并持久化，如使用首选项或RDB。

应用侧更新状态需同步卡片时，从持久化的数据中获取该类型的formId数组，遍历数组调用formProvider.updateForm()推送卡片更新需要的数据。当卡片移除时，需要在onRemoveForm()生命周期中判断formId是否在该类型数组中，若存在需删除该数据项并更新持久化数据。

### 如何管理当前已加桌的所有卡片ID

长按App图标，弹出下拉菜单点击卡片，或者长按某张卡片，选择更多卡片，弹出“卡片加桌弹窗”时，所有的卡片都会触发onAddForm()生命周期回调。手动关闭卡片加桌弹窗或息屏，退出“卡片加桌弹窗”时，会触发所有卡片的onRemoveForm()生命周期回调。点击“添加至桌面”添加卡片时，退出“卡片加桌弹窗”，会触发除当前加桌卡片之外的其他卡片的onRemoveForm()生命周期回调。

当触发onAddForm()生命周期回调时，将卡片ID存储到数据库。当触发onRemoveForm()生命周期回调时，将卡片ID从数据库删除。数据库中未被删除的卡片ID，即是当前已加桌的所有卡片ID。

## 示例代码

* [实现卡片更新与数据交互功能](https://gitcode.com/harmonyos_samples/CardInfoRefresh)
