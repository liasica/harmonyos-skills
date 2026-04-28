---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pasteboard
title: @ohos.pasteboard (剪贴板)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.pasteboard (剪贴板)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4ac4f0b1407454032925fdda8c6300835981c3e4a5a4a89aab930ce56e2e61b1
---

本模块提供管理系统剪贴板的能力，支持系统复制、粘贴功能。系统剪贴板支持对文本、HTML、URI、Want、PixelMap等内容的操作。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { pasteboard } from '@kit.BasicServicesKit';
```

## 常量

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| MAX\_RECORD\_NUM7+ | number | - | API version 10之前，此常量值为512，表示单个PasteData中所能包含的最大条目数为512。当剪贴板内容中添加的条目达到数量上限512后，后续的添加操作无效。  从API version 10开始，不再限制单个PasteData中所能包含的最大条目数。 |
| MIMETYPE\_TEXT\_HTML7+ | string | 'text/html' | HTML内容的MIME类型定义。 |
| MIMETYPE\_TEXT\_WANT7+ | string | 'text/want' | Want内容的MIME类型定义。 |
| MIMETYPE\_TEXT\_PLAIN7+ | string | 'text/plain' | 纯文本内容的MIME类型定义。 |
| MIMETYPE\_TEXT\_URI7+ | string | 'text/uri' | URI内容的MIME类型定义。 |
| MIMETYPE\_PIXELMAP9+ | string | 'pixelMap' | PixelMap内容的MIME类型定义。 |

## ValueType9+

PhonePC/2in1TabletTVWearable

type ValueType = string | image.PixelMap | Want | ArrayBuffer

用于表示允许的数据字段类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 类型 | 说明 |
| --- | --- |
| string | 表示string的类型。 |
| image.PixelMap | 表示[image.PixelMap](arkts-apis-image-pixelmap.md)的类型。 |
| Want | 表示[Want](js-apis-app-ability-want.md)的类型。 |
| ArrayBuffer | 表示ArrayBuffer的类型。 |

## pasteboard.createData9+

PhonePC/2in1TabletTVWearable

createData(mimeType: string, value: ValueType): PasteData

构建一个指定类型的剪贴板内容对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 剪贴板数据对应的MIME类型，可以是[常量](js-apis-pasteboard.md#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值, mimeType长度不能超过1024字节。 |
| value | [ValueType](js-apis-pasteboard.md#valuetype9) | 是 | 自定义数据内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 剪贴板内容对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例1：**

```
1. let dataXml = new ArrayBuffer(256);
2. let pasteData: pasteboard.PasteData = pasteboard.createData('app/xml', dataXml);
```

**示例2：**

```
1. let dataText = 'hello';
2. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, dataText);
```

## pasteboard.createData14+

PhonePC/2in1TabletTVWearable

createData(data: Record<string, ValueType>): PasteData

构建一个包含多个类型数据的剪贴板内容对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [Record](../harmonyos-guides/introduction-to-arkts.md#对象字面量)<string, [ValueType](js-apis-pasteboard.md#valuetype9)> | 是 | Record的key为剪贴板数据对应的MIME类型。可以是[常量](js-apis-pasteboard.md#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型。也可以是自定义的MIME类型，可自定义此参数值，mimeType长度不能超过1024字节。  Record的value为key中指定MIME类型对应的数据。  Record中的首个key-value指定的MIME类型，会作为剪贴板内容对象中首个PasteDataRecord的默认MIME类型，非默认类型的数据在粘贴时只能使用[getData](js-apis-pasteboard.md#getdata14)接口读取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 剪贴板内容对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例1：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData({
2. 'text/plain': 'hello',
3. 'app/xml': new ArrayBuffer(256),
4. });
```

**示例2：**

```
1. let record: Record<string, pasteboard.ValueType> = {};
2. record[pasteboard.MIMETYPE_TEXT_PLAIN] = 'hello';
3. record[pasteboard.MIMETYPE_TEXT_URI] = 'dataability:///com.example.myapplication1/user.txt';
4. let pasteData: pasteboard.PasteData = pasteboard.createData(record);
```

## pasteboard.createRecord9+

PhonePC/2in1TabletTVWearable

createRecord(mimeType: string, value: ValueType): PasteDataRecord

创建一条指定类型的数据内容条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 剪贴板数据对应的MIME类型，可以是[常量](js-apis-pasteboard.md#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。 |
| value | [ValueType](js-apis-pasteboard.md#valuetype9) | 是 | 指定类型对应的数据内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 一条新建的指定类型的数据内容条目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例1：**

```
1. let dataXml = new ArrayBuffer(256);
2. let pasteDataRecord: pasteboard.PasteDataRecord = pasteboard.createRecord('app/xml', dataXml);
```

**示例2：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
3. pasteData.replaceRecord(0, record);
```

## pasteboard.getSystemPasteboard

PhonePC/2in1TabletTVWearable

getSystemPasteboard(): SystemPasteboard

获取系统剪贴板对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SystemPasteboard](js-apis-pasteboard.md#systempasteboard) | 系统剪贴板对象。 |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

## ShareOption9+

PhonePC/2in1TabletTVWearable

可粘贴数据的范围类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INAPP | 0 | 表示仅允许同应用内粘贴。 |
| LOCALDEVICE | 1 | 表示允许在任何应用内粘贴。用户在“设置-多设备协同-跨设备剪贴板开关”选项中控制允许跨设备粘贴，表示允许跨设备在任何应用内粘贴。 |
| CROSSDEVICE(deprecated) | 2 | 表示允许跨设备在任何应用内粘贴。  从API version 12开始废弃，无替代接口和替代方法，后续由用户在“设置-多设备协同-跨设备剪贴板开关”选项中控制是否允许跨设备粘贴。 |

## pasteboard.createHtmlData(deprecated)

PhonePC/2in1TabletTVWearable

createHtmlData(htmlText: string): PasteData

构建一个HTML剪贴板内容对象。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](js-apis-pasteboard.md#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| htmlText | string | 是 | HTML内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 剪贴板内容对象。 |

**示例：**

```
1. let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
2. let pasteData: pasteboard.PasteData = pasteboard.createHtmlData(html);
```

## pasteboard.createWantData(deprecated)

PhonePC/2in1TabletTVWearable

createWantData(want: Want): PasteData

构建一个Want剪贴板内容对象。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](js-apis-pasteboard.md#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 剪贴板内容对象。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';

3. let object: Want = {
4. bundleName: "com.example.aafwk.test",
5. abilityName: "com.example.aafwk.test.TwoAbility"
6. };
7. let pasteData: pasteboard.PasteData = pasteboard.createWantData(object);
```

## pasteboard.createPlainTextData(deprecated)

PhonePC/2in1TabletTVWearable

createPlainTextData(text: string): PasteData

构建一个纯文本剪贴板内容对象。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](js-apis-pasteboard.md#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 纯文本内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 剪贴板内容对象。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
```

## pasteboard.createUriData(deprecated)

PhonePC/2in1TabletTVWearable

createUriData(uri: string): PasteData

构建一个URI剪贴板内容对象。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createData](js-apis-pasteboard.md#pasteboardcreatedata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | URI内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 剪贴板内容对象。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createUriData('dataability:///com.example.myapplication1/user.txt');
```

## pasteboard.createHtmlTextRecord(deprecated)

PhonePC/2in1TabletTVWearable

createHtmlTextRecord(htmlText: string): PasteDataRecord

创建一条HTML内容的条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](js-apis-pasteboard.md#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| htmlText | string | 是 | HTML内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 一条新建的HTML内容条目。 |

**示例：**

```
1. let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
2. let record: pasteboard.PasteDataRecord = pasteboard.createHtmlTextRecord(html);
```

## pasteboard.createWantRecord(deprecated)

PhonePC/2in1TabletTVWearable

createWantRecord(want: Want): PasteDataRecord

创建一条Want内容条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](js-apis-pasteboard.md#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 一条新建的Want内容条目。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';

3. let object: Want = {
4. bundleName: "com.example.aafwk.test",
5. abilityName: "com.example.aafwk.test.TwoAbility"
6. };
7. let record: pasteboard.PasteDataRecord = pasteboard.createWantRecord(object);
```

## pasteboard.createPlainTextRecord(deprecated)

PhonePC/2in1TabletTVWearable

createPlainTextRecord(text: string): PasteDataRecord

创建一条纯文本内容条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](js-apis-pasteboard.md#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 纯文本内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 一条新建的纯文本内容条目。 |

**示例：**

```
1. let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');
```

## pasteboard.createUriRecord(deprecated)

PhonePC/2in1TabletTVWearable

createUriRecord(uri: string): PasteDataRecord

创建一条URI内容的条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.createRecord](js-apis-pasteboard.md#pasteboardcreaterecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | URI内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 一条新建的URI内容条目。 |

**示例：**

```
1. let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
```

## PasteDataProperty7+

PhonePC/2in1TabletTVWearable

定义剪贴板中所有内容条目的属性，包含时间戳、数据类型、粘贴范围以及一些附加数据等，该属性必须通过[setProperty](js-apis-pasteboard.md#setproperty9)方法，才能设置到剪贴板中。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| additions | Record<string, object> | 否 | 否 | 设置其他附加属性数据。不支持动态追加属性，只能通过重新赋值的方式修改附加值，具体见相关示例setProperty， 默认为空。 |
| mimeTypes | Array<string> | 是 | 否 | 剪贴板内容条目的数据类型，非重复的类型列表。 |
| tag | string | 否 | 否 | 用户自定义标签，默认为空。 |
| timestamp | number | 是 | 否 | 剪贴板数据的写入时间戳（单位：已开机时间的ns数）。 |
| localOnly | boolean | 否 | 否 | 配置剪贴板内容是否为“仅在本地”，默认值为false。其值会被shareOption属性覆盖，推荐使用[ShareOption](js-apis-pasteboard.md#shareoption9)属性。 |
| shareOption9+ | [ShareOption](js-apis-pasteboard.md#shareoption9) | 否 | 否 | 指示剪贴板数据可以粘贴到的范围，默认值为CROSSDEVICE。 |

## FileConflictOptions15+

PhonePC/2in1TabletTVWearable

定义文件拷贝冲突时的选项。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERWRITE | 0 | 目标路径存在同文件名时覆盖。 |
| SKIP | 1 | 目标路径存在同文件名时跳过，若设置SKIP，应用获取到的粘贴数据不包含跳过文件。 |

## ProgressIndicator15+

PhonePC/2in1TabletTVWearable

定义进度条指示选项，可选择是否采用系统默认进度显示。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不采用系统默认进度显示。 |
| DEFAULT | 1 | 采用系统默认进度显示。 |

## ProgressInfo15+

PhonePC/2in1TabletTVWearable

定义进度上报的数据结构，且仅当进度指示选项[ProgressIndicator](js-apis-pasteboard.md#progressindicator15)设置为NONE时才会上报此信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 不使用系统提供的进度条时，系统上报拷贝粘贴任务进度百分比。 |

## ProgressListener15+

PhonePC/2in1TabletTVWearable

type ProgressListener = (progress: ProgressInfo) => void

定义进度数据变化的订阅函数，当选择不使用系统默认进度显示时，可设置该项获取粘贴过程的进度。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | [ProgressInfo](js-apis-pasteboard.md#progressinfo15) | 是 | 定义进度上报的数据结构，且仅当进度指示选项[ProgressIndicator](js-apis-pasteboard.md#progressindicator15)设置为NONE时才会上报此信息。 |

## ProgressSignal15+

PhonePC/2in1TabletTVWearable

定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](js-apis-pasteboard.md#progressindicator15)设置为NONE时此参数才有意义。

**系统能力：** SystemCapability.MiscServices.Pasteboard

### cancel15+

PhonePC/2in1TabletTVWearable

cancel(): void

取消正在进行的拷贝粘贴任务。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```
1. import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';
3. @Entry
4. @Component
5. struct PasteboardTest {
6. build() {
7. RelativeContainer() {
8. Column() {
9. Column() {
10. Button("Copy txt")
11. .onClick(async ()=>{
12. let text = "test";
13. let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
14. let systemPasteboard = pasteboard.getSystemPasteboard();
15. await systemPasteboard.setData(pasteData);
16. let signal = new pasteboard.ProgressSignal;
17. let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
18. console.info('progressListener success, progress:' + progress.progress);
19. signal.cancel();
20. };
21. let destPath: string = '/data/storage/el2/base/files/';
22. let destUri : string = fileUri.getUriFromPath(destPath);
23. let params: pasteboard.GetDataParams = {
24. destUri: destUri,
25. fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
26. progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
27. progressListener: progressListenerInfo,
28. };
29. systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
30. console.info('getDataWithProgress success');
31. }).catch((err: BusinessError) => {
32. console.error('Failed to get PasteData. Cause: ' + err.message);
33. })
34. })
35. }
36. }
37. }
38. }
39. }
```

## GetDataParams15+

PhonePC/2in1TabletTVWearable

应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| destUri | string | 否 | 是 | 拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理，默认为空。 |
| fileConflictOptions | [FileConflictOptions](js-apis-pasteboard.md#fileconflictoptions15) | 否 | 是 | 定义文件拷贝冲突时的选项，默认为OVERWRITE。 |
| progressIndicator | [ProgressIndicator](js-apis-pasteboard.md#progressindicator15) | 否 | 否 | 定义进度条指示选项，可选择是否采用系统默认进度显示。 |
| progressListener | [ProgressListener](js-apis-pasteboard.md#progresslistener15) | 否 | 是 | 定义进度数据变化的订阅函数，当选择不使用系统默认进度显示时，可设置该项获取粘贴过程的进度，默认为空。 |
| progressSignal | [ProgressSignal](js-apis-pasteboard.md#progresssignal15) | 否 | 是 | 定义进度取消的函数，在粘贴过程中可选择取消任务，且仅当进度指示选项[ProgressIndicator](js-apis-pasteboard.md#progressindicator15)设置为NONE时此参数才有意义，默认为空。 |

## PasteDataRecord7+

PhonePC/2in1TabletTVWearable

对于剪贴板中内容记录的抽象定义，称之为条目。剪贴板内容部分由一个或者多个条目构成，例如一条文本内容、一份HTML、一个URI或者一个Want。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| htmlText | string | 是 | 否 | HTML内容。 |
| want | [Want](js-apis-app-ability-want.md) | 是 | 否 | Want内容。 |
| mimeType | string | 是 | 否 | 默认数据类型。 |
| plainText | string | 是 | 否 | 纯文本内容。 |
| uri | string | 是 | 否 | URI内容。 |
| pixelMap9+ | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | PixelMap内容。 |
| data9+ | Record<string, ArrayBuffer> | 是 | 否 | 自定义数据内容。 |

### toPlainText9+

PhonePC/2in1TabletTVWearable

toPlainText(): string

将一个PasteDataRecord中的html、plain、uri内容强制转换为文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 纯文本内容。 |

**示例：**

```
1. let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, '<html>hello</html>');
2. let text: string = record.toPlainText();
3. console.info(`Succeeded in converting to text. Text: ${text}`);
```

### addEntry14+

PhonePC/2in1TabletTVWearable

addEntry(type: string, value: ValueType): void

往一个PasteDataRecord中额外添加一种样式的自定义数据。此方式添加的MIME类型都不是Record的默认类型，粘贴时只能使用[getData](js-apis-pasteboard.md#getdata14)接口读取对应数据。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 剪贴板数据对应的MIME类型，可以是[常量](js-apis-pasteboard.md#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型，开发者可自定义此参数值，mimeType长度不能超过1024字节。 |
| value | [ValueType](js-apis-pasteboard.md#valuetype9) | 是 | 自定义数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
2. let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
3. record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
4. record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
```

### getValidTypes14+

PhonePC/2in1TabletTVWearable

getValidTypes(types: Array<string>): Array<string>

根据传入的MIME类型，返回传入的MIME类型和剪贴板中数据的MIME类型的交集。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array<string> | 是 | MIME类型列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 传入的MIME类型和剪贴板中数据的MIME类型的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
2. let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
3. record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
4. record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
5. let types: string[] = record.getValidTypes([
6. pasteboard.MIMETYPE_TEXT_PLAIN,
7. pasteboard.MIMETYPE_TEXT_HTML,
8. pasteboard.MIMETYPE_TEXT_URI,
9. pasteboard.MIMETYPE_TEXT_WANT,
10. pasteboard.MIMETYPE_PIXELMAP
11. ]);
```

### getData14+

PhonePC/2in1TabletTVWearable

getData(type: string): Promise<ValueType>

从PasteDataRecord中获取指定MIME类型的自定义数据。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | MIME类型，其长度不能超过1024字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ValueType](js-apis-pasteboard.md#valuetype9)> | Promise对象，返回PasteDataRecord中指定MIME类型的自定义数据。  PasteDataRecord中包含多个MIME类型数据时，非PasteDataRecord的默认MIME类型的数据只能通过本接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let html = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
4. let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
5. record.addEntry(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
6. record.addEntry(pasteboard.MIMETYPE_TEXT_HTML, html);
7. record.getData(pasteboard.MIMETYPE_TEXT_PLAIN).then((value: pasteboard.ValueType) => {
8. let textPlainContent = value as string;
9. console.info('Success to get text/plain value. value is: ' + textPlainContent);
10. }).catch((err: BusinessError) => {
11. console.error('Failed to get text/plain value. Cause: ' + err.message);
12. });
13. record.getData(pasteboard.MIMETYPE_TEXT_URI).then((value: pasteboard.ValueType) => {
14. let uri = value as string;
15. console.info('Success to get text/uri value. value is: ' + uri);
16. }).catch((err: BusinessError) => {
17. console.error('Failed to get text/uri value. Cause: ' + err.message);
18. });
```

### convertToText(deprecated)

PhonePC/2in1TabletTVWearable

convertToText(callback: AsyncCallback<string>): void

将一个PasteData中的内容强制转换为文本内容，使用callback异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[toPlainText](js-apis-pasteboard.md#toplaintext9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，当转换成功，err为undefined，data为强制转换的文本内容；否则返回错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
4. record.convertToText((err: BusinessError, data: string) => {
5. if (err) {
6. console.error(`Failed to convert to text. Cause: ${err.message}`);
7. return;
8. }
9. console.info(`Succeeded in converting to text. Data: ${data}`);
10. });
```

### convertToText(deprecated)

PhonePC/2in1TabletTVWearable

convertToText(): Promise<string>

将一个PasteData中的内容强制转换为文本内容，使用Promise异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[toPlainText](js-apis-pasteboard.md#toplaintext9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回强制转换的文本内容。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
4. record.convertToText().then((data: string) => {
5. console.info(`Succeeded in converting to text. Data: ${data}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to convert to text. Cause: ${err.message}`);
8. });
```

## PasteData

PhonePC/2in1TabletTVWearable

剪贴板内容对象。剪贴板内容包含一个或者多个内容条目（[PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7)）以及属性描述对象（[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)）。

在调用PasteData的接口前，需要先通过[createData()](js-apis-pasteboard.md#pasteboardcreatedata9)或[getData()](js-apis-pasteboard.md#getdata9)获取一个PasteData对象。

**系统能力：** SystemCapability.MiscServices.Pasteboard

### getPrimaryText

PhonePC/2in1TabletTVWearable

getPrimaryText(): string

获取第一条纯文本内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 纯文本内容。剪贴板内容对象中没有纯文本内容时，默认返回为undefined。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
5. let text: string = pasteData.getPrimaryText();
6. }).catch((err: BusinessError) => {
7. console.error('Failed to get PasteData. Cause: ' + err.message);
8. });
```

### getPrimaryHtml7+

PhonePC/2in1TabletTVWearable

getPrimaryHtml(): string

获取第一条的HTML内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | HTML内容。剪贴板内容对象中没有HTML内容时，默认返回为undefined。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
5. let htmlText: string = pasteData.getPrimaryHtml();
6. }).catch((err: BusinessError) => {
7. console.error('Failed to get PasteData. Cause: ' + err.message);
8. });
```

### getPrimaryWant7+

PhonePC/2in1TabletTVWearable

getPrimaryWant(): Want

获取第一条的Want对象内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Want](js-apis-app-ability-want.md) | Want对象内容。剪贴板内容对象中没有Want内容时，默认返回为undefined。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
5. systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
6. let want: Want = pasteData.getPrimaryWant();
7. }).catch((err: BusinessError) => {
8. console.error('Failed to get PasteData. Cause: ' + err.message);
9. });
```

### getPrimaryUri7+

PhonePC/2in1TabletTVWearable

getPrimaryUri(): string

获取第一条的URI内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | URI内容。剪贴板内容对象中没有URI内容时，默认返回为undefined。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
5. let uri: string = pasteData.getPrimaryUri();
6. }).catch((err: BusinessError) => {
7. console.error('Failed to get PasteData. Cause: ' + err.message);
8. });
```

### getPrimaryPixelMap9+

PhonePC/2in1TabletTVWearable

getPrimaryPixelMap(): image.PixelMap

获取第一条的PixelMap内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [image.PixelMap](arkts-apis-image-pixelmap.md) | PixelMap内容。剪贴板内容对象中没有PixelMap内容时，默认返回为undefined。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. let buffer = new ArrayBuffer(128);
4. let realSize: image.Size = { height: 3, width: 5 };
5. let opt: image.InitializationOptions = {
6. size: realSize,
7. pixelFormat: 3,
8. editable: true,
9. alphaType: 1,
10. scaleMode: 1
11. };
12. image.createPixelMap(buffer, opt).then((pixelMap: image.PixelMap) => {
13. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_PIXELMAP, pixelMap);
14. let PixelMap: image.PixelMap = pasteData.getPrimaryPixelMap();
15. });
```

### addRecord7+

PhonePC/2in1TabletTVWearable

addRecord(record: PasteDataRecord): void

向当前剪贴板内容中添加一条条目，同时也会将条目类型添加到[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 是 | 待添加的条目。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
2. let textRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
3. let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
4. let htmlRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_HTML, html);
5. pasteData.addRecord(textRecord);
6. pasteData.addRecord(htmlRecord);
```

### addRecord9+

PhonePC/2in1TabletTVWearable

addRecord(mimeType: string, value: ValueType): void

向当前剪贴板内容中添加一条数据内容条目，同时也会将数据类型添加到[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 数据的MIME类型， 其长度不能超过1024字节。 |
| value | [ValueType](js-apis-pasteboard.md#valuetype9) | 是 | 数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'dataability:///com.example.myapplication1/user.txt');
2. let dataXml = new ArrayBuffer(256);
3. pasteData.addRecord('app/xml', dataXml);
```

### getMimeTypes7+

PhonePC/2in1TabletTVWearable

getMimeTypes(): Array<string>

获取剪贴板中[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes列表，接口调用异常时返回undefined。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 剪贴板内容条目的数据类型，非重复的类型列表。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let types: string[] = pasteData.getMimeTypes();
```

### getPrimaryMimeType7+

PhonePC/2in1TabletTVWearable

getPrimaryMimeType(): string

获取剪贴板内容中首个条目的数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 首个条目的数据类型。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let type: string = pasteData.getPrimaryMimeType();
```

### getProperty7+

PhonePC/2in1TabletTVWearable

getProperty(): PasteDataProperty

获取剪贴板内容的属性描述对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7) | 属性描述对象。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let property: pasteboard.PasteDataProperty = pasteData.getProperty();
```

### setProperty9+

PhonePC/2in1TabletTVWearable

setProperty(property: PasteDataProperty): void

设置剪贴板内容的属性描述对象[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7) | 是 | 属性描述对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. type AdditionType = Record<string, Record<string, Object>>;

3. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_HTML, 'application/xml');
4. let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
5. prop.shareOption = pasteboard.ShareOption.INAPP;
6. // 需要注意，不支持对addition进行追加属性的操作，只能通过重新赋值的方式达到追加属性的目的。
7. prop.additions = { 'TestOne': { 'Test': 123 }, 'TestTwo': { 'Test': 'additions' } } as AdditionType;
8. prop.tag = 'TestTag';
9. pasteData.setProperty(prop);
```

[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的localOnly与shareOption属性互斥，最终结果以shareOption为准，shareOption会影响localOnly的值。

```
1. (async () => {
2. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
3. let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
4. prop.shareOption = pasteboard.ShareOption.INAPP;
5. prop.localOnly = false;
6. pasteData.setProperty(prop);
7. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

9. await systemPasteboard.setData(pasteData).then(async () => {
10. console.info('Succeeded in setting PasteData.');
11. await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
12. let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
13. prop.localOnly; // true
14. });
15. });

17. prop.shareOption = pasteboard.ShareOption.LOCALDEVICE;
18. prop.localOnly = false;
19. pasteData.setProperty(prop);

21. await systemPasteboard.setData(pasteData).then(async () => {
22. console.info('Succeeded in setting PasteData.');
23. await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
24. let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
25. prop.localOnly; // true
26. });
27. });
28. })
```

### getRecord9+

PhonePC/2in1TabletTVWearable

getRecord(index: number): PasteDataRecord

获取剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定条目的下标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 指定下标的条目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900001 | The index is out of the record. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);
```

### getRecordCount7+

PhonePC/2in1TabletTVWearable

getRecordCount(): number

获取剪贴板内容中条目的个数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 条目的个数。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let count: number = pasteData.getRecordCount();
```

### getTag7+

PhonePC/2in1TabletTVWearable

getTag(): string

获取剪贴板内容中用户自定义的标签内容，如果没有设置用户自定义的标签内容将返回空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回用户自定义的标签内容，如果没有设置用户自定义的标签内容，将返回空。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let tag: string = pasteData.getTag();
```

### hasType9+

PhonePC/2in1TabletTVWearable

hasType(mimeType: string): boolean

检查剪贴板内容中是否有指定的MIME数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 待查询的数据类型。可以是[常量](js-apis-pasteboard.md#常量)中已定义的类型，包括HTML类型，WANT类型，纯文本类型，URI类型，PIXELMAP类型；也可以是自定义的MIME类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let hasType: boolean = pasteData.hasType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

### removeRecord9+

PhonePC/2in1TabletTVWearable

removeRecord(index: number): void

移除剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定的下标。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900001 | The index is out of the record. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. pasteData.removeRecord(0);
```

### replaceRecord9+

PhonePC/2in1TabletTVWearable

replaceRecord(index: number, record: PasteDataRecord): void

替换剪贴板内容中指定下标的条目。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定的下标。 |
| record | [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 是 | 被替换后的条目数据内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900001 | The index is out of the record. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE_TEXT_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
3. pasteData.replaceRecord(0, record);
```

### pasteStart12+

PhonePC/2in1TabletTVWearable

pasteStart(): void

读取剪贴板数据前，通知剪贴板服务保留跨设备通道。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
5. if (err) {
6. console.error('Failed to get PasteData. Cause: ' + err.message);
7. return;
8. }
9. pasteData.pasteStart();
10. console.info(`using data: ${pasteData.getPrimaryText()}`);
11. pasteData.pasteComplete();
12. });
```

### pasteComplete12+

PhonePC/2in1TabletTVWearable

pasteComplete(): void

通知剪贴板服务数据使用已完成。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
5. if (err) {
6. console.error('Failed to get PasteData. Cause: ' + err.message);
7. return;
8. }
9. pasteData.pasteStart();
10. console.info(`using data: ${pasteData.getPrimaryText()}`);
11. pasteData.pasteComplete();
12. });
```

### addHtmlRecord(deprecated)

PhonePC/2in1TabletTVWearable

addHtmlRecord(htmlText: string): void

向当前剪贴板内容中添加一条HTML内容条目，并将MIMETYPE\_TEXT\_HTML添加到[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](js-apis-pasteboard.md#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| htmlText | string | 是 | HTML内容。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. let html: string = "<!DOCTYPE html>\n" + "<html>\n" + "<head>\n" + "<meta charset=\"utf-8\">\n" + "<title>HTML-PASTEBOARD_HTML</title>\n" + "</head>\n" + "<body>\n" + "    <h1>HEAD</h1>\n" + "    <p></p>\n" + "</body>\n" + "</html>";
3. pasteData.addHtmlRecord(html);
```

### addWantRecord(deprecated)

PhonePC/2in1TabletTVWearable

addWantRecord(want: Want): void

向当前剪贴板内容中添加一条Want条目，并将MIMETYPE\_TEXT\_WANT添加到[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](js-apis-pasteboard.md#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want对象内容。 |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';

3. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
4. let object: Want = {
5. bundleName: "com.example.aafwk.test",
6. abilityName: "com.example.aafwk.test.TwoAbility"
7. };
8. pasteData.addWantRecord(object);
```

### addTextRecord(deprecated)

PhonePC/2in1TabletTVWearable

addTextRecord(text: string): void

向当前剪贴板内容中添加一条纯文本条目，并将MIMETYPE\_TEXT\_PLAIN添加到[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](js-apis-pasteboard.md#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 纯文本内容。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. pasteData.addTextRecord('good');
```

### addUriRecord(deprecated)

PhonePC/2in1TabletTVWearable

addUriRecord(uri: string): void

向当前剪贴板内容中添加一条URI条目，并将MIMETYPE\_TEXT\_URI添加到[PasteDataProperty](js-apis-pasteboard.md#pastedataproperty7)的mimeTypes中。入参均不能为空，否则添加失败。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[addRecord](js-apis-pasteboard.md#addrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | URI内容。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. pasteData.addUriRecord('dataability:///com.example.myapplication1/user.txt');
```

### getRecordAt(deprecated)

PhonePC/2in1TabletTVWearable

getRecordAt(index: number): PasteDataRecord

获取剪贴板内容中指定下标的条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[getRecord](js-apis-pasteboard.md#getrecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定条目的下标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 指定下标的条目。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. let record: pasteboard.PasteDataRecord = pasteData.getRecordAt(0);
```

### hasMimeType(deprecated)

PhonePC/2in1TabletTVWearable

hasMimeType(mimeType: string): boolean

检查剪贴板内容中是否有指定的数据类型。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasType](js-apis-pasteboard.md#hastype9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 待查询的数据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. let hasType: boolean = pasteData.hasMimeType(pasteboard.MIMETYPE_TEXT_PLAIN);
```

### removeRecordAt(deprecated)

PhonePC/2in1TabletTVWearable

removeRecordAt(index: number): boolean

移除剪贴板内容中指定下标的条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[removeRecord](js-apis-pasteboard.md#removerecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定的下标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功移除返回true，失败返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. let isRemove: boolean = pasteData.removeRecordAt(0);
```

### replaceRecordAt(deprecated)

PhonePC/2in1TabletTVWearable

replaceRecordAt(index: number, record: PasteDataRecord): boolean

替换剪贴板内容中指定下标的条目。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[replaceRecord](js-apis-pasteboard.md#replacerecord9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定的下标。 |
| record | [PasteDataRecord](js-apis-pasteboard.md#pastedatarecord7) | 是 | 替换后的条目。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功替换返回true，失败返回false。 |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
2. let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
3. let isReplace: boolean = pasteData.replaceRecordAt(0, record);
```

## SystemPasteboard

PhonePC/2in1TabletTVWearable

系统剪贴板对象。

在调用SystemPasteboard的接口前，需要先通过[getSystemPasteboard](js-apis-pasteboard.md#pasteboardgetsystempasteboard)获取系统剪贴板。

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

### on('update')7+

PhonePC/2in1TabletTVWearable

on(type: 'update', callback: () =>void): void

订阅系统剪贴板内容变化事件，当系统剪贴板中内容变化时触发用户程序的回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取值为'update'，表示系统剪贴板内容变化事件。 |
| callback | function | 是 | 剪贴板中内容变化时触发的用户程序的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. let listener = () => {
3. console.info('The system pasteboard has changed.');
4. };
5. systemPasteboard.on('update', listener);
```

### off('update')7+

PhonePC/2in1TabletTVWearable

off(type: 'update', callback?: () =>void): void

取消订阅系统剪贴板内容变化事件。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取值为'update'，表示系统剪贴板内容变化事件。 |
| callback | function | 否 | 剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有监听回调，否则表示清除指定监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. let listener = () => {
3. console.info('The system pasteboard has changed.');
4. };
5. systemPasteboard.off('update', listener);
```

### clearData9+

PhonePC/2in1TabletTVWearable

clearData(callback: AsyncCallback<void>): void

清空系统剪贴板内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功清空时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. systemPasteboard.clearData((err, data) => {
3. if (err) {
4. console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
5. return;
6. }
7. console.info('Succeeded in clearing the pasteboard.');
8. });
```

### clearData9+

PhonePC/2in1TabletTVWearable

clearData(): Promise<void>

清空系统剪贴板内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.clearData().then((data: void) => {
5. console.info('Succeeded in clearing the pasteboard.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to clear the pasteboard. Cause: ${err.message}`);
8. });
```

### setData9+

PhonePC/2in1TabletTVWearable

setData(data: PasteData, callback: AsyncCallback<void>): void

将数据写入系统剪贴板，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PasteData](js-apis-pasteboard.md#pastedata) | 是 | PasteData对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
2. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
3. systemPasteboard.setData(pasteData, (err, data) => {
4. if (err) {
5. console.error('Failed to set PasteData. Cause: ' + err.message);
6. return;
7. }
8. console.info('Succeeded in setting PasteData.');
9. });
```

### setData9+

PhonePC/2in1TabletTVWearable

setData(data: PasteData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PasteData](js-apis-pasteboard.md#pastedata) | 是 | PasteData对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'content');
4. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
5. systemPasteboard.setData(pasteData).then((data: void) => {
6. console.info('Succeeded in setting PasteData.');
7. }).catch((err: BusinessError) => {
8. console.error('Failed to set PasteData. Cause: ' + err.message);
9. });
```

### getData9+

PhonePC/2in1TabletTVWearable

getData(callback: AsyncCallback<PasteData>): void

读取系统剪贴板内容，使用callback异步回调。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PasteData](js-apis-pasteboard.md#pastedata)> | 是 | 回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
5. if (err) {
6. console.error('Failed to get PasteData. Cause: ' + err.message);
7. return;
8. }
9. let text: string = pasteData.getPrimaryText();
10. });
```

### getData9+

PhonePC/2in1TabletTVWearable

getData(): Promise<PasteData>

读取系统剪贴板内容，使用Promise异步回调。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PasteData](js-apis-pasteboard.md#pastedata)> | Promise对象，返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
5. let text: string = pasteData.getPrimaryText();
6. }).catch((err: BusinessError) => {
7. console.error('Failed to get PasteData. Cause: ' + err.message);
8. });
```

### hasData9+

PhonePC/2in1TabletTVWearable

hasData(callback: AsyncCallback<boolean>): void

判断系统剪贴板中是否有内容，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.hasData((err: BusinessError, data: boolean) => {
5. if (err) {
6. console.error(`Failed to check the PasteData. Cause: ${err.message}`);
7. return;
8. }
9. console.info(`Succeeded in checking the PasteData. Data: ${data}`);
10. });
```

### hasData9+

PhonePC/2in1TabletTVWearable

hasData(): Promise<boolean>

判断系统剪贴板中是否有内容，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.hasData().then((data: boolean) => {
5. console.info(`Succeeded in checking the PasteData. Data: ${data}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to check the PasteData. Cause: ${err.message}`);
8. });
```

### clear(deprecated)

PhonePC/2in1TabletTVWearable

clear(callback: AsyncCallback<void>): void

清空系统剪贴板内容，使用callback异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.clearData](js-apis-pasteboard.md#cleardata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功清空时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. systemPasteboard.clear((err, data) => {
3. if (err) {
4. console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
5. return;
6. }
7. console.info('Succeeded in clearing the PasteData.');
8. });
```

### clear(deprecated)

PhonePC/2in1TabletTVWearable

clear(): Promise<void>

清空系统剪贴板内容，使用Promise异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[pasteboard.clearData](js-apis-pasteboard.md#cleardata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.clear().then((data) => {
5. console.info('Succeeded in clearing the PasteData.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to clear the PasteData. Cause: ${err.message}`);
8. });
```

### getPasteData(deprecated)

PhonePC/2in1TabletTVWearable

getPasteData(callback: AsyncCallback<PasteData>): void

读取系统剪贴板内容，使用callback异步回调。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[getData](js-apis-pasteboard.md#getdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PasteData](js-apis-pasteboard.md#pastedata)> | 是 | 回调函数。当读取成功，err为undefined，data为返回的系统剪贴板数据；否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
5. if (err) {
6. console.error('Failed to get PasteData. Cause: ' + err.message);
7. return;
8. }
9. let text: string = pasteData.getPrimaryText();
10. });
```

### getPasteData(deprecated)

PhonePC/2in1TabletTVWearable

getPasteData(): Promise<PasteData>

读取系统剪贴板内容，使用Promise异步回调。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[getData](js-apis-pasteboard.md#getdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PasteData](js-apis-pasteboard.md#pastedata)> | Promise对象，返回系统剪贴板数据。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
5. let text: string = pasteData.getPrimaryText();
6. }).catch((err: BusinessError) => {
7. console.error('Failed to get PasteData. Cause: ' + err.message);
8. });
```

### hasPasteData(deprecated)

PhonePC/2in1TabletTVWearable

hasPasteData(callback: AsyncCallback<boolean>): void

判断系统剪贴板中是否有内容，使用callback异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasData](js-apis-pasteboard.md#hasdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.hasPasteData((err: BusinessError, data: boolean) => {
5. if (err) {
6. console.error(`Failed to check the PasteData. Cause: ${err.message}`);
7. return;
8. }
9. console.info(`Succeeded in checking the PasteData. Data: ${data}`);
10. });
```

### hasPasteData(deprecated)

PhonePC/2in1TabletTVWearable

hasPasteData(): Promise<boolean>

判断系统剪贴板中是否有内容，使用Promise异步回调。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[hasData](js-apis-pasteboard.md#hasdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.hasPasteData().then((data: boolean) => {
5. console.info(`Succeeded in checking the PasteData. Data: ${data}`);
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to check the PasteData. Cause: ${err.message}`);
8. });
```

### setPasteData(deprecated)

PhonePC/2in1TabletTVWearable

setPasteData(data: PasteData, callback: AsyncCallback<void>): void

将数据写入系统剪贴板，使用callback异步回调。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[setData](js-apis-pasteboard.md#setdata9)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PasteData](js-apis-pasteboard.md#pastedata) | 是 | PasteData对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
2. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
3. systemPasteboard.setPasteData(pasteData, (err, data) => {
4. if (err) {
5. console.error('Failed to set PasteData. Cause: ' + err.message);
6. return;
7. }
8. console.info('Succeeded in setting PasteData.');
9. });
```

### setPasteData(deprecated)

PhonePC/2in1TabletTVWearable

setPasteData(data: PasteData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

说明

从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[setData](js-apis-pasteboard.md#setdata9-1)替代。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PasteData](js-apis-pasteboard.md#pastedata) | 是 | PasteData对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
4. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
5. systemPasteboard.setPasteData(pasteData).then((data: void) => {
6. console.info('Succeeded in setting PasteData.');
7. }).catch((err: BusinessError) => {
8. console.error('Failed to set PasteData. Cause: ' + err.message);
9. });
```

### isRemoteData11+

PhonePC/2in1TabletTVWearable

isRemoteData(): boolean

判断剪贴板中的数据是否来自其他设备。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是来自其他设备返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. let result: boolean = systemPasteboard.isRemoteData();
4. console.info(`Succeeded in checking the RemoteData. Result: ${result}`);
5. } catch (err) {
6. console.error('Failed to check the RemoteData. Cause:' + err.message);
7. };
```

### getDataSource11+

PhonePC/2in1TabletTVWearable

getDataSource(): string

获取数据来源的应用名称。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 数据来源的应用名称。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. let result: string = systemPasteboard.getDataSource();
4. console.info(`Succeeded in getting DataSource. Result: ${result}`);
5. } catch (err) {
6. console.error('Failed to get DataSource. Cause:' + err.message);
7. };
```

### hasDataType11+

PhonePC/2in1TabletTVWearable

hasDataType(mimeType: string): boolean

检查剪贴板内容中是否有指定类型的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 数据类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 有指定类型的数据返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE_TEXT_PLAIN);
4. console.info(`Succeeded in checking the DataType. Result: ${result}`);
5. } catch (err) {
6. console.error('Failed to check the DataType. Cause:' + err.message);
7. };
```

### clearDataSync11+

PhonePC/2in1TabletTVWearable

clearDataSync(): void

清空系统剪贴板内容, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. systemPasteboard.clearDataSync();
4. console.info('Succeeded in clearing the pasteboard.');
5. } catch (err) {
6. console.error('Failed to clear the pasteboard. Cause:' + err.message);
7. };
```

### getDataSync11+

PhonePC/2in1TabletTVWearable

getDataSync(): PasteData

读取系统剪贴板内容, 此接口为同步接口。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasteData](js-apis-pasteboard.md#pastedata) | 返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. let result: pasteboard.PasteData = systemPasteboard.getDataSync();
4. console.info('Succeeded in getting PasteData.');
5. } catch (err) {
6. console.error('Failed to get PasteData. Cause:' + err.message);
7. };
```

### setDataSync11+

PhonePC/2in1TabletTVWearable

setDataSync(data: PasteData): void

将数据写入系统剪贴板, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PasteData](js-apis-pasteboard.md#pastedata) | 是 | 需要写入剪贴板中的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, 'hello');
2. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
3. try {
4. systemPasteboard.setDataSync(pasteData);
5. console.info('Succeeded in setting PasteData.');
6. } catch (err) {
7. console.error('Failed to set PasteData. Cause:' + err.message);
8. };
```

### hasDataSync11+

PhonePC/2in1TabletTVWearable

hasDataSync(): boolean

判断系统剪贴板中是否有内容, 此接口为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示系统剪贴板中有内容，返回false表示系统剪贴板中没有内容。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. let result: boolean = systemPasteboard.hasDataSync();
4. console.info(`Succeeded in checking the PasteData. Result: ${result}`);
5. } catch (err) {
6. console.error('Failed to check the PasteData. Cause:' + err.message);
7. };
```

### getUnifiedData12+

PhonePC/2in1TabletTVWearable

getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>

读取系统剪贴板内容，使用Promise异步回调。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[unifiedDataChannel.UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)> | Promise对象，返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 27787277 | Another copy or paste operation is in progress. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

4. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
5. systemPasteboard.getUnifiedData().then((data) => {
6. let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
7. for (let j = 0; j < records.length; j++) {
8. if (records[j].getType() === uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
9. let text = records[j].getValue() as uniformDataStruct.PlainText;
10. console.info(`${j + 1}.${text.textContent}`);
11. }
12. }
13. }).catch((err: BusinessError) => {
14. console.error('Failed to get UnifiedData. Cause: ' + err.message);
15. });
```

### getUnifiedDataSync12+

PhonePC/2in1TabletTVWearable

getUnifiedDataSync(): unifiedDataChannel.UnifiedData

读取系统剪贴板内容, 此接口为同步接口。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [unifiedDataChannel.UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. try {
5. let result: unifiedDataChannel.UnifiedData = systemPasteboard.getUnifiedDataSync();
6. console.info('Succeeded in getting UnifiedData.');
7. } catch (err) {
8. console.error('Failed to get UnifiedData. Cause:' + err.message);
9. };
```

### setUnifiedData12+

PhonePC/2in1TabletTVWearable

setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>

将数据写入系统剪贴板，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [unifiedDataChannel.UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 需要写入剪贴板中的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

4. let plainText : uniformDataStruct.PlainText = {
5. uniformDataType: uniformTypeDescriptor.UniformDataType.PLAIN_TEXT,
6. textContent : 'PLAINTEXT_CONTENT',
7. abstract : 'PLAINTEXT_ABSTRACT',
8. }
9. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
10. let data = new unifiedDataChannel.UnifiedData();
11. data.addRecord(record);

13. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
14. systemPasteboard.setUnifiedData(data).then((data: void) => {
15. console.info('Succeeded in setting UnifiedData.');
16. }).catch((err: BusinessError) => {
17. console.error('Failed to setUnifiedData. Cause: ' + err.message);
18. });
```

### setUnifiedDataSync12+

PhonePC/2in1TabletTVWearable

setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void

将数据写入系统剪贴板, 此接口为同步接口。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [unifiedDataChannel.UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 需要写入剪贴板中的数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';

3. let plainTextData = new unifiedDataChannel.UnifiedData();
4. let plainText = new unifiedDataChannel.PlainText();
5. plainText.details = {
6. Key: 'delayPlaintext',
7. Value: 'delayPlaintext',
8. };
9. plainText.textContent = 'delayTextContent';
10. plainText.abstract = 'delayTextContent';
11. plainTextData.addRecord(plainText);

13. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
14. try {
15. systemPasteboard.setUnifiedDataSync(plainTextData);
16. console.info('Succeeded in setting UnifiedData.');
17. } catch (err) {
18. console.error('Failed to set UnifiedData. Cause:' + err.message);
19. };
```

### setAppShareOptions14+

PhonePC/2in1TabletTVWearable

setAppShareOptions(shareOptions: ShareOption): void

应用设置本应用剪贴板数据的可粘贴范围。

**需要权限**：ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shareOptions | [ShareOption](js-apis-pasteboard.md#shareoption9) | 是 | 可粘贴的范围，参数只允许pasteboard.ShareOption.INAPP。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12900006 | Settings already exist. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
4. console.info('Set app share options success.');
5. } catch (error) {
6. console.error(`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
7. }
```

### removeAppShareOptions14+

PhonePC/2in1TabletTVWearable

removeAppShareOptions(): void

删除应用全局的可粘贴的范围。

**需要权限**：ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

**系统能力：** SystemCapability.MiscServices.Pasteboard

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. try {
3. systemPasteboard.removeAppShareOptions();
4. console.info('Remove app share options success.');
5. } catch (error) {
6. console.error(`Remove app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.`);
7. }
```

### Pattern13+

PhonePC/2in1TabletTVWearable

剪贴板支持检测的模式类型。

**系统能力：** SystemCapability.MiscServices.Pasteboard

| 名称 | 值 | 说明 |
| --- | --- | --- |
| URL | 0 | URL类型。 |
| NUMBER | 1 | 数字类型。 |
| EMAIL\_ADDRESS | 2 | 邮箱地址类型。 |

### detectPatterns13+

PhonePC/2in1TabletTVWearable

detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>

检测**本地**剪贴板中存在的[Pattern](js-apis-pasteboard.md#pattern13)模式，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| patterns | [Array<Pattern>](js-apis-pasteboard.md#pattern13) | 是 | 需要在剪贴板中检测的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Pattern>> | Promise对象，返回检测到的模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. import { pasteboard } from '@kit.BasicServicesKit'

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL_ADDRESS];

6. systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
7. if (patterns.sort().join('')==data.sort().join('')) {
8. console.info('All needed patterns detected, next get data');
9. try {
10. let result: pasteboard.PasteData = systemPasteboard.getDataSync();
11. console.info('Succeeded in getting PasteData.');
12. } catch (err) {
13. console.error('Failed to get PasteData. Cause:' + err.message);
14. };
15. } else {
16. console.info("Not all needed patterns detected, no need to get data.");
17. }
18. });
```

### getMimeTypes14+

PhonePC/2in1TabletTVWearable

getMimeTypes(): Promise<Array<string>>

读取剪贴板中存在的MIME类型，使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回读取到的MIME类型。 |

**示例：**

```
1. import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. systemPasteboard.getMimeTypes().then((data: Array<string>) => {
5. console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
6. }).catch((err: BusinessError) => {
7. console.error('Failed to get mimeTypes. Cause:' + err.message);
8. });
```

### getDataWithProgress15+

PhonePC/2in1TabletTVWearable

getDataWithProgress(params: GetDataParams): Promise<PasteData>

获取剪贴板的内容和进度，使用Promise异步回调，不支持对文件夹的拷贝。

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [GetDataParams](js-apis-pasteboard.md#getdataparams15) | 是 | 应用在使用剪贴板提供的文件拷贝能力的情况下需要的参数，包含目标路径、文件冲突选项、进度条类型等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PasteData](js-apis-pasteboard.md#pastedata)> | Promise对象，返回系统剪贴板数据。 |

**错误码：**

以下错误码的详细介绍请参见[剪贴板错误码](errorcode-pasteboard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. |
| 12900003 | Another copy or paste operation is in progress. |
| 12900007 | Invalid destUri or file system error. |
| 12900008 | Failed to start progress. |
| 12900009 | Progress exits abnormally. |
| 12900010 | System error occurred during paste execution. |

**示例：**

```
1. import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
2. import { fileUri } from '@kit.CoreFileKit';
3. @Entry
4. @Component
5. struct PasteboardTest {
6. build() {
7. RelativeContainer() {
8. Column() {
9. Column() {
10. Button("Copy txt")
11. .onClick(async ()=>{
12. let text = "test";
13. let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
14. let systemPasteboard = pasteboard.getSystemPasteboard();
15. await systemPasteboard.setData(pasteData);
16. let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
17. console.info('progressListener success, progress:' + progress.progress);
18. };
19. let destPath: string = '/data/storage/el2/base/files/';
20. let destUri : string = fileUri.getUriFromPath(destPath);
21. let params: pasteboard.GetDataParams = {
22. destUri: destUri,
23. fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
24. progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
25. progressListener: progressListenerInfo,
26. };
27. systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
28. console.info('getDataWithProgress success');
29. }).catch((err: BusinessError) => {
30. console.error('Failed to get PasteData. Cause: ' + err.message);
31. })
32. })
33. }
34. }
35. }
36. }
37. }
```

### getChangeCount18+

PhonePC/2in1TabletTVWearable

getChangeCount(): number

获取剪贴板内容的变化次数。

执行成功时返回剪贴板内容的变化次数，否则返回0。

当剪贴板内容过期或调用[clearDataSync](js-apis-pasteboard.md#cleardatasync11)等接口导致剪贴板内容为空时，内容变化次数不会因此改变。

系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被视作多次更改，每次复制均会导致内容变化次数增加。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回读取到的剪贴板内容变化次数。 |

**示例：**

```
1. import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

3. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
4. try {
5. let result : number = systemPasteboard.getChangeCount();
6. console.info(`Succeeded in getting the ChangeCount. Result: ${result}`);
7. } catch (err) {
8. console.error(`Failed to get the ChangeCount. Cause: ${err.message}`);
9. };
```

### UpdateCallback 22+

PhonePC/2in1TabletTVWearable

type UpdateCallback = () => void

表示剪贴板内容变更的回调

**系统能力：** SystemCapability.MiscServices.Pasteboard

### onRemoteUpdate(callback: UpdateCallback)22+

PhonePC/2in1TabletTVWearable

onRemoteUpdate(callback: UpdateCallback): void

订阅跨设备剪贴板内容变化事件，当远端设备系统剪贴板中内容变化时触发用户程序的回调。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [UpdateCallback](js-apis-pasteboard.md#updatecallback-22) | 是 | 剪贴板中内容变化时触发的用户程序的回调。 |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. let listener = () => {
3. console.info('The remote pasteboard has changed.');
4. };
5. systemPasteboard.onRemoteUpdate(listener);
```

### offRemoteUpdate22+

PhonePC/2in1TabletTVWearable

offRemoteUpdate(callback?: UpdateCallback): void

取消订阅跨设备剪贴板内容变化事件。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [UpdateCallback](js-apis-pasteboard.md#updatecallback-22) | 否 | 远端设备剪贴板中内容变化时触发的用户程序的回调。如果此参数未填，表明清除本应用的所有远端监听回调，否则表示清除指定远端监听回调。 |

**示例：**

```
1. const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
2. let listener = () => {
3. console.info('The remote pasteboard has changed.');
4. };
5. systemPasteboard.offRemoteUpdate(listener);
```
