---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-formbindingdata
title: @ohos.application.formBindingData (卡片数据绑定类)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > 已停止维护的接口 > @ohos.application.formBindingData (卡片数据绑定类)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3804c8763c07a1a91cbfe1f2b31d2c0cb44fc25ffbbf77957d2d20c72d037d7
---

卡片数据绑定模块提供卡片数据绑定的能力。包括FormBindingData对象的创建、相关信息的描述。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始废弃，建议使用[formBindingData](js-apis-app-form-formbindingdata.md)替代。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { formBindingData } from '@kit.FormKit';
```

## FormBindingData

PhonePC/2in1TabletTVWearable

FormBindingData相关描述。

**系统能力：** SystemCapability.Ability.Form

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Object | 否 | 否 | js卡片要展示的数据。可以是包含若干键值对的Object或者 json 格式的字符串。 |

## formBindingData.createFormBindingData

PhonePC/2in1TabletTVWearable

createFormBindingData(obj?: Object | string): FormBindingData

创建一个FormBindingData对象。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object|string | 否 | JS卡片要展示的数据。可以是包含若干键值对的Object或者 json 格式的字符串。其中图片数据以'formImages'作为标识，内容为图片标识与图片文件描述符的键值对{'formImages': {'key1': fd1, 'key2': fd2}}。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FormBindingData](js-apis-application-formbindingdata.md#formbindingdata) | 根据传入数据创建的FormBindingData对象。 |

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
25. console.error(`catch error, error: ${JSON.stringify(error)}`);
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
