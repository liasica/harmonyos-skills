---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-formeditextensioncontext
title: FormEditExtensionContext
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > application > FormEditExtensionContext
category: harmonyos-references
scraped_at: 2026-04-28T08:06:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:383ebe24ca525c3725c2b6311bb1ae42c6daf5bd97157914cf4c1187534bb036
---

FormEditExtensionContext是[FormEditExtensionAbility](js-apis-app-form-formeditextensionability.md)的上下文，继承自[UIExtensionContext](js-apis-inner-application-uiextensioncontext.md)。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FormEditExtensionAbility } from '@kit.FormKit';
```

## FormEditExtensionContext

PhonePC/2in1TabletTVWearable

FormEditExtensionContext提供允许访问特定于FormEditExtensionAbility资源的能力。

### startSecondPage

PhonePC/2in1TabletTVWearable

startSecondPage(want: Want): Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)>

拉起需要被编辑的卡片提供方页面。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 第三方应用需要被桌面拉起的编辑页面信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | Promise对象，返回AbilityResult。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | The application is not a system application. |
| 16500050 | An IPC connection error happened. |
| 16501000 | An internal functional error occurred. |
| 16500100 | Failed to obtain the configuration information. |

**示例：**

```
1. import { FormEditExtensionAbility } from '@kit.FormKit';
2. import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

4. const TAG: string = '[testTag] ExampleFormEditExtensionAbility'

6. export default class ExampleFormEditAbility extends FormEditExtensionAbility {
7. abilityName: string = 'FormEditSecPageAbility'

9. onSessionCreate(want: Want, session: UIExtensionContentSession) {
10. try {
11. this.context.startSecondPage({
12. bundleName: 'com.example.formEditDemo',
13. parameters: {
14. "secPageAbilityName": this.abilityName
15. }

17. }).then(data => {
18. console.info(TAG, `startSecondPage result want: ${data.resultCode}`)
19. });
20. } catch (e) {
21. console.error(TAG, `startSecondPage failed, code: ${e.code}, message: ${e.message}`)
22. return
23. }
24. }
25. }
```

### startUIAbility23+

PhonePC/2in1TabletTVWearable

startUIAbility(want: Want): Promise<void>

拉起卡片所属应用的UIAbility。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md#want) | 是 | 应用自身UIAbility的ability信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回void。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | An IPC connection error happened. |
| 16500100 | Failed to obtain the configuration information. |
| 16000130 | The target UIAbility does not belong to the caller. |
| 16501014 | The form edit page is not in the foreground. The current operation is not supported. |
| 16000121 | The target component type is not a UIAbility. |

**示例：**

```
1. import { FormEditExtensionAbility } from '@kit.FormKit'
2. import { Want, UIExtensionContentSession } from '@kit.AbilityKit';

4. const TAG: string = '[testTag] ExampleFormEditExtensionAbility'

6. export default class ExampleFormEditAbility extends FormEditExtensionAbility {
7. abilityName: string = 'FormEditSecPageAbility'

9. onSessionCreate(want: Want, session: UIExtensionContentSession) {
10. try {
11. this.context.startUIAbility({
12. abilityName: 'EntryAbility1',
13. }).then(() => {
14. console.info(TAG, `startUIAbility success`);
15. });
16. } catch (e) {
17. console.error(TAG, `startUIAbility failed, code: ${e.code}, message: ${e.message}`);
18. return
19. }
20. }
21. }
```
