---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formprovider
title: @ohos.app.form.formProvider (formProvider)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.formProvider (formProvider)
category: harmonyos-references
scraped_at: 2026-04-29T13:56:31+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3aae45c1f7150103e832890823dda646d91ac8ca3aaf5bbdfe27eb662bac5044
---

formProvider模块提供了获取卡片信息、更新卡片、设置卡片更新时间等能力。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formProvider } from '@kit.FormKit';
```

## formProvider.setFormNextRefreshTime

PhonePC/2in1TabletTVWearable

setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void

设置指定卡片的下一次更新时间，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |
| minute | number | 是 | 指定卡片多久之后更新，取值范围：大于等于5，单位：min。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501002 | The number of forms exceeds the maximum allowed. |
| 16501003 | The form cannot be operated by the current application. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
5. try {
6. formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
7. if (error) {
8. console.error(`callback error, code: ${error.code}, message: ${error.message})`);
9. return;
10. }
11. console.info(`formProvider setFormNextRefreshTime success`);
12. });
13. } catch (error) {
14. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
15. }
```

## formProvider.setFormNextRefreshTime

PhonePC/2in1TabletTVWearable

setFormNextRefreshTime(formId: string, minute: number): Promise<void>

设置指定卡片的下一次更新时间，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |
| minute | number | 是 | 指定卡片多久之后更新，取值范围：大于等于5，单位：min。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501002 | The number of forms exceeds the maximum allowed. |
| 16501003 | The form cannot be operated by the current application. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
5. try {
6. formProvider.setFormNextRefreshTime(formId, 5).then(() => {
7. console.info(`formProvider setFormNextRefreshTime success`);
8. }).catch((error: BusinessError) => {
9. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
10. });
11. } catch (error) {
12. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
13. }
```

## formProvider.updateForm

PhonePC/2in1TabletTVWearable

updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void

更新指定的卡片，使用callback异步回调。

说明

从API version 20开始，如果卡片刷新的数据通过共享内存更新，刷新数据总大小不超过10MB，刷新图片数量不超过20张。API version 19及之前的版本，图片文件数量上限为5张，每张限制内存2MB，超出限制的图片会显示异常。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求更新的卡片标识。 |
| formBindingData | [formBindingData.FormBindingData](js-apis-app-form-formbindingdata.md#formbindingdata) | 是 | 用于更新的数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**示例：**

```
1. import { formBindingData, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
5. try {
6. let param: Record<string, string> = {
7. 'temperature': '22c',
8. 'time': '22:00'
9. }
10. let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
11. formProvider.updateForm(formId, obj, (error: BusinessError) => {
12. if (error) {
13. console.error(`callback error, code: ${error.code}, message: ${error.message})`);
14. return;
15. }
16. console.info(`formProvider updateForm success`);
17. });
18. } catch (error) {
19. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
20. }
```

## formProvider.updateForm

PhonePC/2in1TabletTVWearable

updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>

更新指定的卡片，使用Promise异步回调。

说明

从API version 20开始，如果卡片刷新的数据通过共享内存更新，刷新数据总大小不超过10MB，刷新图片数量不超过20张。API version 19及之前的版本，图片文件数量上限为5张，每张限制内存2MB，超出限制的图片会显示异常。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 请求更新的卡片标识。 |
| formBindingData | [formBindingData.FormBindingData](js-apis-app-form-formbindingdata.md#formbindingdata) | 是 | 用于更新的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**示例：**

```
1. import { formBindingData, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
5. let param: Record<string, string> = {
6. 'temperature': '22c',
7. 'time': '22:00'
8. }
9. let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
10. try {
11. formProvider.updateForm(formId, obj).then(() => {
12. console.info(`formProvider updateForm success`);
13. }).catch((error: BusinessError) => {
14. console.error(`promise error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
15. });
16. } catch (error) {
17. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
18. }
```

## formProvider.getFormsInfo

PhonePC/2in1TabletTVWearable

getFormsInfo(callback: AsyncCallback<Array<formInfo.FormInfo>>): void

获取设备上当前应用程序的卡片信息，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[formInfo.FormInfo](js-apis-app-form-forminfo.md)>> | 是 | 回调函数。返回查询到的卡片信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. formProvider.getFormsInfo((error, data) => {
6. if (error) {
7. console.error(`callback error, code: ${error.code}, message: ${error.message})`);
8. return;
9. }
10. console.info(`formProvider getFormsInfo, data: ${JSON.stringify(data)}`);
11. });
12. } catch (error) {
13. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
14. }
```

## formProvider.getFormsInfo

PhonePC/2in1TabletTVWearable

getFormsInfo(filter: formInfo.FormInfoFilter, callback: AsyncCallback<Array<formInfo.FormInfo>>): void

获取设备上当前应用程序的卡片信息，并筛选符合条件的信息，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [formInfo.FormInfoFilter](js-apis-app-form-forminfo.md#forminfofilter) | 是 | 卡片信息过滤器。 |
| callback | AsyncCallback<Array<[formInfo.FormInfo](js-apis-app-form-forminfo.md)>> | 是 | 回调函数。返回查询到符合条件的卡片信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const filter: formInfo.FormInfoFilter = {
5. // 获取指定module的卡片信息
6. moduleName: 'entry'
7. };
8. try {
9. formProvider.getFormsInfo(filter, (error, data) => {
10. if (error) {
11. console.error(`callback error, code: ${error.code}, message: ${error.message})`);
12. return;
13. }
14. console.info(`formProvider getFormsInfo, data: ${JSON.stringify(data)}`);
15. });
16. } catch (error) {
17. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
18. }
```

## formProvider.getFormsInfo

PhonePC/2in1TabletTVWearable

getFormsInfo(filter?: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>

获取设备上当前应用符合条件的卡片信息，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [formInfo.FormInfoFilter](js-apis-app-form-forminfo.md#forminfofilter) | 否 | 卡片信息过滤器, 默认为空，不进行过滤。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[formInfo.FormInfo](js-apis-app-form-forminfo.md)>> | Promise对象。返回查询到符合条件的卡片信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const filter: formInfo.FormInfoFilter = {
5. // get info of forms belong to module entry.
6. moduleName: 'entry'
7. };
8. try {
9. formProvider.getFormsInfo(filter).then((data: formInfo.FormInfo[]) => {
10. console.info(`formProvider getFormsInfo, data: ${JSON.stringify(data)}`);
11. }).catch((error: BusinessError) => {
12. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
13. });
14. } catch (error) {
15. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
16. }
```

## formProvider.openFormEditAbility18+

PhonePC/2in1TabletTVWearable

openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void

打开卡片编辑页。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityName | string | 是 | 编辑页的ability名称。 |
| formId | string | 是 | 卡片标识。 |
| isMainPage | boolean | 否 | 是否为主编辑页。  - true：表示是主编辑页。  - false：表示不是主编辑页。  默认值：true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function openFormEditAbility can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501003 | The form cannot be operated by the current application. |
| 16501007 | Form is not trust. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';

3. const TAG: string = 'FormEditDemo-Page] -->';

5. @Entry
6. @Component
7. struct Page {
8. @State message: string = 'Hello World';

10. aboutToAppear(): void {
11. console.info(`${TAG} aboutToAppear.....`);
12. }

14. build() {
15. RelativeContainer() {
16. Text(this.message)
17. .id('PageHelloWorld')
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. .alignRules({
21. center: { anchor: '__container__', align: VerticalAlign.Top },
22. middle: { anchor: '__container__', align: HorizontalAlign.Center }
23. })
24. .onClick(() => {
25. console.info(`${TAG} onClick.....`);
26. formProvider.openFormEditAbility('ability://EntryFormEditAbility', '1386529921');
27. })
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```

## formProvider.closeFormEditAbility23+

PhonePC/2in1TabletTVWearable

closeFormEditAbility(isMainPage?: boolean): void

关闭卡片编辑页。

**系统能力：** SystemCapability.Ability.Form

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isMainPage | boolean | 否 | 是否关闭一级卡片编辑页，true表示关闭一级编辑页，false表示关闭非一级编辑页。  默认值：true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16501015 | Cannot close the widget editing page opened by other apps. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';

3. const TAG: string = 'FormEditDemo-Page] -->';

5. @Entry
6. @Component
7. struct Page {
8. @State message: string = 'Hello World';

10. aboutToAppear(): void {
11. console.info(`${TAG} aboutToAppear.....`);
12. }

14. build() {
15. RelativeContainer() {
16. Text(this.message)
17. .id('PageHelloWorld')
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. .alignRules({
21. center: { anchor: '__container__', align: VerticalAlign.Top },
22. middle: { anchor: '__container__', align: HorizontalAlign.Center }
23. })
24. .onClick(() => {
25. console.info(`${TAG} onClick.....`);
26. try {
27. formProvider.closeFormEditAbility();
28. console.info(`${TAG} close FormEditAbility success.`);
29. } catch (error) {
30. console.error(`${TAG} close FormEditAbility faild, code: ${error.code}, message: ${error.message}`);
31. }
32. })
33. }
34. .height('100%')
35. .width('100%')
36. }
37. }
```

## formProvider.openFormManager18+

PhonePC/2in1TabletTVWearable

openFormManager(want: Want): void

打开当前应用的卡片管理页面。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 打开卡片管理页面的请求中的want参数，需包含以下字段。  bundleName: 卡片所属应用的包名。  abilityName: 卡片所属的ability名称。  parameters:  - ohos.extra.param.key.form\_dimension: [卡片尺寸](js-apis-app-form-forminfo.md#formdimension)。  - ohos.extra.param.key.form\_name: 卡片名称。  - ohos.extra.param.key.module\_name: 卡片所属的模块名称。 |

说明

如果parameters参数没有填完整或者指定的卡片不存在，就会默认展示[form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#卡片配置)中配置的默认卡片。

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Want } from '@kit.AbilityKit';

5. const want: Want = {
6. bundleName: 'com.example.formbutton',
7. abilityName: 'EntryFormAbility',
8. parameters: {
9. 'ohos.extra.param.key.form_dimension': 2,
10. 'ohos.extra.param.key.form_name': 'widget',
11. 'ohos.extra.param.key.module_name': 'entry'
12. },
13. };
14. try {
15. formProvider.openFormManager(want);
16. } catch (error) {
17. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
18. }
```

## formProvider.getPublishedFormInfoById(deprecated)

PhonePC/2in1TabletTVWearable

getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>

获取设备上当前应用程序已经加桌的指定卡片信息，使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

说明

该字段从API version 18开始支持，从API version 20开始废弃，建议使用[getPublishedRunningFormInfoById](js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfobyid20)替代。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[formInfo.FormInfo](js-apis-app-form-forminfo.md#forminfo)> | Promise对象。返回查询到符合条件的卡片信息。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const formId: string = '388344236';
5. try {
6. formProvider.getPublishedFormInfoById(formId).then((data: formInfo.FormInfo) => {
7. console.info(`formProvider getPublishedFormInfoById, data: ${JSON.stringify(data)}`);
8. }).catch((error: BusinessError) => {
9. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
10. });
11. } catch (error) {
12. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
13. }
```

## formProvider.getPublishedFormInfos(deprecated)

PhonePC/2in1TabletTVWearable

getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>

获取设备上当前应用程序所有已经加桌的卡片信息，使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

说明

该字段从API version 18开始支持，从API version 20开始废弃，建议使用[getPublishedRunningFormInfos](js-apis-app-form-formprovider.md#formprovidergetpublishedrunningforminfos20)替代。

**系统能力：** SystemCapability.Ability.Form

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[formInfo.FormInfo](js-apis-app-form-forminfo.md)>> | Promise对象。返回查询到符合条件的卡片信息。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. formProvider.getPublishedFormInfos().then((data: formInfo.FormInfo[]) => {
6. console.info(`formProvider getPublishedFormInfos, data: ${JSON.stringify(data)}`);
7. }).catch((error: BusinessError) => {
8. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
9. });
10. } catch (error) {
11. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
12. }
```

## formProvider.requestOverflow20+

PhonePC/2in1TabletTVWearable

requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>

卡片提供方发起互动卡片动效请求，只针对[场景动效类型互动卡片](../harmonyos-guides/arkts-ui-widget-configuration.md#sceneanimationparams标签)生效，使用Promise异步回调。

说明

1. 该接口在省电模式场景下不可使用，会报16501000错误码。
2. 当设备热档位进入HOT场景并且没有点击事件的场景下，该接口会报16501000错误码；当热档位进入OVERHEATED时，任何情况下都会报16501000错误码。热档位信息具体可参考[热档位信息](js-apis-thermal.md#thermallevel)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片id标识。 |
| overflowInfo | [formInfo.OverflowInfo](js-apis-app-form-forminfo.md#overflowinfo20) | 是 | 动效请求参数信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function requestOverflow can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |
| 16501011 | The form can not support this operation. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整
5. let overflowInfo: formInfo.OverflowInfo = {
6. area: {
7. left: -10,
8. top: -10,
9. width: 180,
10. height: 180
11. },
12. duration: 1000,
13. useDefaultAnimation: false,
14. };

16. try {
17. formProvider.requestOverflow(formId, overflowInfo).then(() => {
18. console.info('requestOverflow succeed.');
19. }).catch((error: BusinessError) => {
20. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
21. });
22. } catch (error) {
23. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
24. }
```

## formProvider.cancelOverflow20+

PhonePC/2in1TabletTVWearable

cancelOverflow(formId: string): Promise<void>

卡片提供方发起取消互动卡片动效请求，只针对[场景动效类型互动卡片](../harmonyos-guides/arkts-ui-widget-configuration.md#sceneanimationparams标签)生效，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function cancelOverflow can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |
| 16501011 | The form can not support this operation. |

**示例：**

```
1. import { formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整

6. try {
7. formProvider.cancelOverflow(formId).then(() => {
8. console.info('cancelOverflow succeed.');
9. }).catch((error: BusinessError) => {
10. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
11. });
12. } catch (error) {
13. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
14. }
```

## formProvider.getFormRect20+

PhonePC/2in1TabletTVWearable

getFormRect(formId: string): Promise<formInfo.Rect>

查询卡片位置、尺寸，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片id标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[formInfo.Rect](js-apis-app-form-forminfo.md#rect20)> | Promise对象，返回卡片相对屏幕左上角的位置信息和卡片尺寸信息，单位vp。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported.function getFormRect can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let formId: string = '12400633174999288'; // 表示卡片formId，根据实际formId调整

6. try {
7. formProvider.getFormRect(formId).then((data: formInfo.Rect) => {
8. console.info(`getFormRect succeed, data: ${JSON.stringify(data)}`);
9. });
10. } catch (error) {
11. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
12. }
```

## formProvider.getPublishedRunningFormInfoById20+

PhonePC/2in1TabletTVWearable

getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>

获取当前应用已加桌卡片中指定的卡片信息，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | 卡片标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[formInfo.RunningFormInfo](js-apis-app-form-forminfo.md#runningforminfo20)> | Promise对象。返回符合条件的卡片信息，包括卡片名称、尺寸等。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const formId: string = '388344236';

6. try {
7. formProvider.getPublishedRunningFormInfoById(formId).then((data: formInfo.RunningFormInfo) => {
8. console.info(`formProvider getPublishedRunningFormInfoById, data: ${JSON.stringify(data)}`);
9. }).catch((error: BusinessError) => {
10. console.error(`promise error, code: ${error.code}, message: ${error.message}`);
11. });
12. } catch (error) {
13. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
14. }
```

## formProvider.getPublishedRunningFormInfos20+

PhonePC/2in1TabletTVWearable

getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>

获取所有已加桌的卡片信息，使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[formInfo.RunningFormInfo](js-apis-app-form-forminfo.md#runningforminfo20)>> | Promise对象。返回符合条件的卡片信息。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { formInfo, formProvider } from '@kit.FormKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. formProvider.getPublishedRunningFormInfos().then((data: formInfo.RunningFormInfo[]) => {
6. console.info(`formProvider getPublishedRunningFormInfos, data: ${JSON.stringify(data)}`);
7. }).catch((error: BusinessError) => {
8. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
9. });
10. } catch (error) {
11. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
12. }
```

## formProvider.reloadForms22+

PhonePC/2in1TabletTVWearable

reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<number>

对于当前应用程序相同moduleName、abilityName、formName的卡片，多次加桌后会每张卡片会有不同的卡片id。卡片提供方可以通过本接口批量更新不同的卡片id但moduleName、abilityName、formName相同的卡片。在应用主进程通过本接口通知FormExtension进程进行批量更新，仅支持在[UIAbility](js-apis-app-ability-uiability.md)中调用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)的上下文，做校验使用。 |
| moduleName | string | 是 | 指定卡片的moduleName。 |
| abilityName | string | 是 | 指定卡片的abilityName。 |
| formName | string | 是 | 指定卡片在[form\_config.json](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)中配置的卡片名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回请求更新卡片的数量。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { formProvider } from '@kit.FormKit';

5. try {
6. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
7. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. // 请开发者替换为实际请求更新的卡片信息
9. let moduleName: string = 'entry';
10. let abilityName: string = 'EntryFormAbility';
11. let formName: string = 'formName';
12. formProvider.reloadForms(context, moduleName, abilityName, formName).then((reloadNum: number) => {
13. console.info(`reloadForms success, reload number: ${reloadNum}`);
14. }).catch((error: BusinessError) => {
15. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
16. });
17. } catch (error) {
18. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
19. }
```

## formProvider.reloadAllForms22+

PhonePC/2in1TabletTVWearable

reloadAllForms(context: UIAbilityContext): Promise<number>

在应用主进程通过本接口可以通知FormExtension进程批量更新当前应用程序下已经加桌的所有卡片，仅支持在[UIAbility](js-apis-app-ability-uiability.md)中调用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)的上下文，做校验使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回请求更新卡片的数量。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](errorcode-form.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { formProvider } from '@kit.FormKit';

5. try {
6. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
7. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
8. formProvider.reloadAllForms(context).then((reloadNum: number) => {
9. console.info(`reloadAllForms success, reload number: ${reloadNum}`);
10. }).catch((error: BusinessError) => {
11. console.error(`promise error, code: ${error.code}, message: ${error.message})`);
12. });
13. } catch (error) {
14. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
15. }
```
