---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability
title: @ohos.app.form.FormExtensionAbility (FormExtensionAbility)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.FormExtensionAbility (FormExtensionAbility)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8317b3a37474fe767c5868e71fe547ba1b965aa9b51c7b20df8d01d3146a5477
---

FormExtensionAbility为卡片扩展模块，提供卡片创建、销毁、刷新等生命周期回调。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

FormExtensionAbility创建后10秒内无操作将会被清理。

如下模块不支持在FormExtensionAbility引用，可能会导致程序异常退出。

* @ohos.ability.particleAbility (ParticleAbility模块)
* @ohos.multimedia.audio (音频管理)
* @ohos.multimedia.camera (相机管理)
* @ohos.multimedia.media (媒体服务)
* @ohos.resourceschedule.backgroundTaskManager (后台任务管理)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FormExtensionAbility } from '@kit.FormKit';
```

## FormExtensionAbility

PhonePC/2in1TabletTVWearable

卡片扩展类。包含卡片提供方接收创建卡片、修改可见性等的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FormExtensionContext](js-apis-inner-application-formextensioncontext.md) | 否 | 否 | FormExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

### FormExtensionAbility.onAddForm

PhonePC/2in1TabletTVWearable

onAddForm(want: Want): formBindingData.FormBindingData

卡片提供方接收创建卡片的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前卡片相关的Want类型信息，其中Want中的parameters为自定义取值，取值可以包含[卡片参数枚举](js-apis-app-form-forminfo.md#formparam)中的一个或多个，如卡片ID、卡片名称、卡片样式等。这些卡片信息必须作为持久数据进行管理，以便后续更新和删除卡片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [formBindingData.FormBindingData](js-apis-app-form-formbindingdata.md#formbindingdata) | formBindingData.FormBindingData对象，卡片要显示的数据。 |

**示例：**

```
1. import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class MyFormExtensionAbility extends FormExtensionAbility {
5. onAddForm(want: Want) {
6. console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
7. let dataObj1: Record<string, string> = {
8. 'temperature': '11c',
9. 'time': '11:00'
10. };

12. let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
13. return obj1;
14. }
15. }
```

### FormExtensionAbility.onCastToNormalForm

PhonePC/2in1TabletTVWearable

onCastToNormalForm(formId: string): void

卡片提供方收到卡片使用方将临时卡片转常态卡片的通知接口。临时卡片、常态卡片是卡片使用方的概念，其中：临时卡片是短期存在的，在特定事件或用户行为后显示，完成后自动消失。常态卡片是持久存在的，在用户未进行清除或更改的情况下，会一直存在，平时开发的功能卡片属于常态卡片。当前卡片使用方不会使用临时卡片。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求转换为常态的卡片标识。 |

**示例：**

```
1. import { FormExtensionAbility } from '@kit.FormKit';

3. export default class MyFormExtensionAbility extends FormExtensionAbility {
4. onCastToNormalForm(formId: string) {
5. // 卡片提供方收到卡片使用方将临时卡片转常态卡片的通知时触发，开发者需根据实际需求做相应的处理
6. console.info(`FormExtensionAbility onCastToNormalForm, formId: ${formId}`);
7. }
8. };
```

### FormExtensionAbility.onUpdateForm

PhonePC/2in1TabletTVWearable

onUpdateForm(formId: string, wantParams?: Record<string, Object>): void

卡片提供方接收携带参数的更新卡片的通知接口。获取最新数据后调用formProvider的[updateForm](js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求更新的卡片ID。 |
| wantParams12+ | Record<string, Object> | 否 | 更新参数。 |

**示例：**

```
1. import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyFormExtensionAbility extends FormExtensionAbility {
5. onUpdateForm(formId: string, wantParams?: Record<string, Object>) {
6. console.info(`FormExtensionAbility onUpdateForm, formId: ${formId},
7. wantPara: ${wantParams?.['ohos.extra.param.key.host_bg_inverse_color']}`);
8. let param: Record<string, string> = {
9. 'temperature': '22c',
10. 'time': '22:00'
11. }
12. let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
13. formProvider.updateForm(formId, obj2).then(() => {
14. console.info(`FormExtensionAbility context updateForm`);
15. }).catch((error: BusinessError) => {
16. console.error(`FormExtensionAbility context updateForm failed, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
17. });
18. }
19. };
```

### FormExtensionAbility.onChangeFormVisibility

PhonePC/2in1TabletTVWearable

onChangeFormVisibility(newStatus: Record<string, number>): void

卡片提供方接收修改可见性的通知接口。

该接口仅对系统应用生效，且需要将formVisibleNotify配置为true。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newStatus | Record<string, number> | 是 | 请求修改的卡片标识和可见状态。 |

**示例：**

```
1. import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // ArkTS规范中ets文件无法使用Object.keys和for..in...获取Object的key值，请使用自定义函数getObjKeys代替。
5. // 使用时请将此函数单独抽离至一个ts文件中并导出，在需要用到的ets文件中导入此函数后使用。
6. function getObjKeys(obj: Object): string[] {
7. let keys = Object.keys(obj);
8. return keys;
9. }

11. export default class MyFormExtensionAbility extends FormExtensionAbility {
12. onChangeFormVisibility(newStatus: Record<string, number>) {
13. console.info(`FormExtensionAbility onChangeFormVisibility, newStatus: ${newStatus}`);
14. let param: Record<string, string> = {
15. 'temperature': '22c',
16. 'time': '22:00'
17. }
18. let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);

20. let keys: string[] = getObjKeys(newStatus);

22. for (let i: number = 0; i < keys.length; i++) {
23. console.info(`FormExtensionAbility onChangeFormVisibility, key: ${keys[i]}, value= ${newStatus[keys[i]]}`);
24. formProvider.updateForm(keys[i], obj2).then(() => {
25. console.info('FormExtensionAbility context updateForm');
26. }).catch((error: BusinessError) => {
27. console.error(`Operation updateForm failed. , code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
28. });
29. }
30. }
31. };
```

### FormExtensionAbility.onFormEvent

PhonePC/2in1TabletTVWearable

onFormEvent(formId: string, message: string): void

卡片提供方接收处理卡片事件的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求触发事件的卡片标识。 |
| message | string | 是 | 事件消息。 |

**示例：**

```
1. import { FormExtensionAbility } from '@kit.FormKit';

3. export default class MyFormExtensionAbility extends FormExtensionAbility {
4. onFormEvent(formId: string, message: string) {
5. console.info(`FormExtensionAbility onFormEvent, formId: ${formId}, message: ${message}`);
6. }
7. };
```

### FormExtensionAbility.onRemoveForm

PhonePC/2in1TabletTVWearable

onRemoveForm(formId: string): void

卡片提供方接收销毁卡片的通知接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求销毁的卡片标识。 |

**示例：**

```
1. import { FormExtensionAbility } from '@kit.FormKit';

3. export default class MyFormExtensionAbility extends FormExtensionAbility {
4. onRemoveForm(formId: string) {
5. console.info(`FormExtensionAbility onRemoveForm, formId: ${formId}`);
6. }
7. };
```

### FormExtensionAbility.onConfigurationUpdate

PhonePC/2in1TabletTVWearable

onConfigurationUpdate(newConfig: Configuration): void

当系统配置项变更时调用，仅当FormExtensionAbility存活时才会触发onConfigurationUpdate回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newConfig | [Configuration](js-apis-app-ability-configuration.md) | 是 | 表示需要更新的配置信息。 |

**示例：**

```
1. import { FormExtensionAbility } from '@kit.FormKit';
2. import { Configuration } from '@kit.AbilityKit';

4. export default class MyFormExtensionAbility extends FormExtensionAbility {
5. onConfigurationUpdate(newConfig: Configuration) {
6. // 仅当前formExtensionAbility存活时更新配置才会触发此生命周期。
7. // 需要注意：formExtensionAbility创建后10秒内无操作将会被清理。
8. console.info(`onConfigurationUpdate, config: ${newConfig?.language}`);
9. }
10. };
```

### FormExtensionAbility.onAcquireFormState

PhonePC/2in1TabletTVWearable

onAcquireFormState?(want: Want): formInfo.FormState

卡片提供方接收查询卡片状态通知接口，默认返回卡片初始状态(该方法可以选择性重写)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | want表示获取卡片状态的描述。描述包括Bundle名称、能力名称、模块名称、卡片名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [formInfo.FormState](js-apis-app-form-forminfo.md#formstate) | formInfo.FormState枚举，表示卡片当前的状态。 |

**示例：**

```
1. import { FormExtensionAbility, formInfo } from '@kit.FormKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class MyFormExtensionAbility extends FormExtensionAbility {
5. onAcquireFormState(want: Want) {
6. console.info(`FormExtensionAbility onAcquireFormState, want: ${want}`);
7. return formInfo.FormState.UNKNOWN;
8. }
9. };
```

### FormExtensionAbility.onStop12+

PhonePC/2in1TabletTVWearable

onStop?(): void

当卡片提供方的卡片进程退出时，触发该回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**示例：**

```
1. import { FormExtensionAbility } from '@kit.FormKit';

3. export default class MyFormExtensionAbility extends FormExtensionAbility {
4. onStop() {
5. console.info(`FormExtensionAbility onStop`);
6. }
7. }
```

### FormExtensionAbility.onFormLocationChanged20+

PhonePC/2in1TabletTVWearable

onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void

当卡片位置发生变化时，触发该回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 发生位置变化的卡片标识。 |
| newFormLocation | [formInfo.FormLocation](js-apis-app-form-forminfo.md#formlocation20) | 是 | 卡片最新位置的枚举值。 |

**示例：**

```
1. import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class EntryFormAbility extends FormExtensionAbility {
5. onAddForm(want: Want) {
6. let formData: Record<string, string | Object> = {
7. 'data': 'addForm'
8. };
9. return formBindingData.createFormBindingData(formData);
10. }
11. onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation) {
12. console.info("EntryFormAbility onFormLocationChanged current location: " + newFormLocation);
13. }
14. }
```

### FormExtensionAbility.onSizeChanged20+

PhonePC/2in1TabletTVWearable

onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void

卡片大小变化时，触发回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |
| newDimension | [formInfo.FormDimension](js-apis-app-form-forminfo.md#formdimension) | 是 | 卡片尺寸，例如 Dimension\_1\_2，表示 1 x 2 卡片。 |
| newRect | [formInfo.Rect](js-apis-app-form-forminfo.md#rect20) | 是 | 卡片位置信息，包括卡片左上角顶点的xy坐标和卡片的宽高。 |

**示例：**

```
1. import { FormExtensionAbility, formInfo } from '@kit.FormKit';

3. export default class MyFormExtensionAbility extends FormExtensionAbility {
4. onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect) {
5. console.info(`FormExtensionAbility onSizeChanged, formId: ${formId}, newDimension: ${newDimension}`);
6. }
7. }
```
