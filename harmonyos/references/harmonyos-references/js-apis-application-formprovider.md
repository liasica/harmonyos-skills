---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formprovider
title: @ohos.application.formProvider (formProvider)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > 已停止维护的接口 > @ohos.application.formProvider (formProvider)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cab4a5aeb16edad1400f14d65d54eaeeb1d3b45792f16e22bd542b1e9de058c1
---

FormProvider模块提供了卡片提供方相关接口的能力，开发者在开发卡片时，可通过该模块提供接口实现更新卡片，设置卡片更新时间，获取卡片信息，请求发布卡片等。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9 开始废弃，建议使用[formProvider](js-apis-app-form-formprovider.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formProvider } from '@kit.FormKit';
```

## formProvider.setFormNextRefreshTime

PhonePC/2in1TabletTVWearable

setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void

设置指定卡片的下一次更新时间，使用callback异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |
| minute | number | 是 | 指定多久之后更新。单位分钟，大于等于5。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { formProvider } from '@kit.FormKit';
3. // 使用时需要用已经存在formId
4. let formId: string = '12400633174999288';
5. formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
6. if (error.code) {
7. console.error(`formProvider setFormNextRefreshTime, errorCode: ${error.code}, errorMessage: ${error.message}`);
8. }
9. });
```

## formProvider.setFormNextRefreshTime

PhonePC/2in1TabletTVWearable

setFormNextRefreshTime(formId: string, minute: number): Promise<void>

设置指定卡片的下一次更新时间，使用Promise异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |
| minute | number | 是 | 指定多久之后更新。单位分钟，大于等于5。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { formProvider } from '@kit.FormKit';
3. // 使用时需要用已经存在formId
4. let formId: string = '12400633174999288';
5. formProvider.setFormNextRefreshTime(formId, 5).then(() => {
6. console.info('formProvider setFormNextRefreshTime success');
7. }).catch((error: BusinessError) => {
8. console.error(`formProvider setFormNextRefreshTime, errorCode: ${error.code}, errorMessage: ${error.message}`);
9. });
```

## formProvider.updateForm

PhonePC/2in1TabletTVWearable

updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void

更新指定的卡片，使用callback异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求更新的卡片标识。 |
| formBindingData | [formBindingData.FormBindingData](js-apis-application-formbindingdata.md#formbindingdata) | 是 | 用于更新的数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { formProvider, formBindingData } from '@kit.FormKit';

4. // 使用时需要用已经存在formId
5. let formId: string = '12400633174999288';
6. let param: Record<string, string> = {
7. 'temperature': '22c',
8. 'time': '22:00'
9. }
10. let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
11. formProvider.updateForm(formId, obj, (error: BusinessError) => {
12. if (error.code) {
13. console.error(`formProvider updateForm, errorCode: ${error.code}, errorMessage: ${error.message}`);
14. }
15. });
```

## formProvider.updateForm

PhonePC/2in1TabletTVWearable

updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>

更新指定的卡片，使用Promise异步回调。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求更新的卡片标识。 |
| formBindingData | [formBindingData.FormBindingData](js-apis-application-formbindingdata.md#formbindingdata) | 是 | 用于更新的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { formProvider, formBindingData } from '@kit.FormKit';

4. // 使用时需要用已经存在formId
5. let formId: string = '12400633174999288';
6. let param: Record<string, string> = {
7. 'temperature': '22c',
8. 'time': '22:00'
9. }
10. let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
11. formProvider.updateForm(formId, obj).then(() => {
12. console.info('formProvider updateForm success');
13. }).catch((error: BusinessError) => {
14. console.error(`formProvider updateForm, errorCode: ${error.code}, errorMessage: ${error.message}`);
15. });
```
