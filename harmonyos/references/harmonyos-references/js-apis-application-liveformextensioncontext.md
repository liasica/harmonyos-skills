---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-liveformextensioncontext
title: LiveFormExtensionContext
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > application > LiveFormExtensionContext
category: harmonyos-references
scraped_at: 2026-04-28T08:06:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5a3beb8f06d127781aefa34d120d6b5d03388fd9fc9f77f3801986aed2fd7e0c
---

LiveFormExtensionContext是[LiveFormExtensionAbility](js-apis-app-form-liveformextensionability.md)的上下文，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

说明

* 在API version 22以前，需要通过import LiveFormExtensionContext from 'application/LiveFormExtensionContext'; 导入LiveFormExtensionContext。该导入方式在DevEco Studio中标红，但不影响编译运行，可以直接使用LiveFormExtensionContext。
* 在API version 22及以后，支持通过import { common } from '@kit.AbilityKit'; 导入LiveFormExtensionContext，并通过common.LiveFormExtensionContext的方式使用。

## LiveFormExtensionContext

PhonePC/2in1TabletTVWearable

LiveFormExtensionContext提供允许访问特定于LiveFormExtensionAbility资源的能力，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

### startAbilityByLiveForm

PhonePC/2in1TabletTVWearable

startAbilityByLiveForm(want: Want): Promise<void>

拉起互动卡片提供方（应用）的页面，使用Promise异步回调。

该接口仅支持拉起互动卡片提供方（应用）的页面，不支持拉起其他应用的页面，否则会抛出错误码16501011。

该接口仅限在点击事件回调中调用，且需要直接调用，不支持延时后调用，否则会抛出错误码16501011。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 需要被拉起的应用页面信息。[仅支持使用显式want。](../harmonyos-guides/ability-startup-with-explicit-want.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported due to limited device capabilities. |
| 16500050 | An IPC connection error happened. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501011 | The form can not support this operation. |

**示例：**

```
1. // MyLiveFormExtensionAbility.ets
2. import { formInfo, LiveFormInfo, LiveFormExtensionAbility } from '@kit.FormKit';
3. import { UIExtensionContentSession } from '@kit.AbilityKit';

5. export default class MyLiveFormExtensionAbility extends LiveFormExtensionAbility {
6. onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
7. // 1.将LiveFormExtensionContext传给互动卡片的页面组件
8. let storage: LocalStorage = new LocalStorage();
9. storage.setOrCreate('context', this.context);
10. session.loadContent('pages/MyLiveFormPage', storage);
11. }
12. };
```

```
1. // pages/MyLiveFormPage.ets
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct MyLiveFormPage {
8. private storageForMyLiveFormPage: LocalStorage | undefined = undefined;
9. private liveFormContext: common.LiveFormExtensionContext | undefined = undefined;

11. aboutToAppear(): void {
12. // 2.获取LiveFormExtensionContext
13. this.storageForMyLiveFormPage = this.getUIContext().getSharedLocalStorage();
14. this.liveFormContext = this.storageForMyLiveFormPage?.get<common.LiveFormExtensionContext>('context');
15. }

17. private startAbilityByLiveForm(): void {
18. try {
19. // 请开发者替换为实际的want信息
20. this.liveFormContext?.startAbilityByLiveForm({
21. bundleName: 'com.example.liveformdemo',
22. abilityName: 'EntryAbility',
23. })
24. .then(() => {
25. console.info('startAbilityByLiveForm succeed');
26. })
27. .catch((err: BusinessError) => {
28. console.error(`startAbilityByLiveForm failed, code is ${err?.code}, message is ${err?.message}`);
29. });
30. } catch (e) {
31. console.error(`startAbilityByLiveForm failed, code is ${e?.code}, message is ${e?.message}`);
32. }
33. }

35. build() {
36. // 请开发者替换为实际的页面
37. Stack() {
38. Column()
39. .width('50%')
40. .height('50%')
41. .backgroundColor('#2875F5')
42. }
43. .width('100%')
44. .height('100%')
45. .onClick(() => {
46. // 3.在点击事件回调中直接使用该接口
47. console.info('MyLiveFormPage click to start ability');
48. if (!this.liveFormContext) {
49. console.info('MyLiveFormPage liveFormContext is empty');
50. return;
51. }
52. this.startAbilityByLiveForm();
53. })
54. }
55. }
```
