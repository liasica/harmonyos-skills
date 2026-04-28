---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formbindingdata
title: @ohos.app.form.formBindingData (卡片数据绑定类)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.formBindingData (卡片数据绑定类)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f6c89f06eabe41f3bf0d8ec69875fb0b7a7e5f01cb032cd9926f1c1cbd6c57a3
---

卡片数据绑定模块提供卡片数据绑定的能力。包括FormBindingData对象的创建、相关信息的描述。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formBindingData } from '@kit.FormKit';
```

## ProxyData10+

PhonePC/2in1TabletTVWearable

卡片代理刷新订阅数据信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key10+ | string | 否 | 否 | 卡片代理刷新的订阅标识，与数据发布者保持一致。 |
| subscriberId10+ | string | 否 | 是 | 卡片代理刷新的订阅条件，默认值为当前卡片的formId。 |

## FormBindingData

PhonePC/2in1TabletTVWearable

FormBindingData相关描述。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Object | 否 | 否 | 卡片要展示的数据。可以是包含若干键值对的Object或者 json 格式的字符串。 |
| proxies10+ | Array<[ProxyData](js-apis-app-form-formbindingdata.md#proxydata10)> | 否 | 是 | 卡片代理刷新的订阅信息，默认为空数组。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## formBindingData.createFormBindingData

PhonePC/2in1TabletTVWearable

createFormBindingData(obj?: Object | string): FormBindingData

创建一个FormBindingData对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object | string | 否 | 卡片要展示的数据。可以是包含若干键值对的Object或者 json 格式的字符串。其中图片数据以'formImages'作为标识，内容为图片标识与图片文件描述符的键值对{'formImages': {'key1': fd1, 'key2': fd2}}。  **说明：** 在[卡片刷新](../harmonyos-guides/arkts-ui-widget-interaction-overview.md)过程中，卡片UI通过@LocalStorageProp接收卡片数据时，FormBindingData对象会序列化，即卡片数据会转换成string类型。从API version 20开始，如果卡片刷新的数据通过共享内存更新，刷新数据总大小不超过10MB，刷新图片数量不超过20张，API version 19及之前的版本，图片文件数量上限为5张，每张限制内存2MB，超出限制的图片会显示异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FormBindingData](js-apis-app-form-formbindingdata.md#formbindingdata) | 根据传入数据创建的FormBindingData对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**示例：**

```
1. import { formBindingData } from '@kit.FormKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';

5. @Entry
6. @Component
7. struct Index {
8. content = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. pathDir: string = this.content.filesDir;

11. createFormBindingData() {
12. try {
13. let filePath = this.pathDir + "/form.png";
14. let file = fileIo.openSync(filePath);
15. let formImagesParam: Record<string, number> = {
16. 'image': file.fd
17. };
18. let createFormBindingDataParam: Record<string, string | Record<string, number>> = {
19. 'name': '21°',
20. 'imgSrc': 'image',
21. 'formImages': formImagesParam
22. };
23. formBindingData.createFormBindingData(createFormBindingDataParam);
24. } catch (error) {
25. console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
26. }
27. }

29. build() {
30. Button('createFormBindingData')
31. .onClick((event: ClickEvent) => {
32. this.createFormBindingData();
33. })
34. }
35. }
```
