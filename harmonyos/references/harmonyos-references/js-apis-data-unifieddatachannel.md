---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel
title: @ohos.data.unifiedDataChannel (标准化数据通路)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.unifiedDataChannel (标准化数据通路)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e1792c9b30fc1298615525f1b84bc2d08b4fea4c729f2e4dda77b74f2a095e1
---

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了标准化的数据通路，提供了标准化的数据接入与读取接口。同时对文本、图片等数据类型提供了标准化定义，方便不同应用间进行数据交互，减少数据类型适配的工作量。UDMF处理数据时，不会解析用户数据的内容，存储路径安全性较低，不建议传输个人敏感数据和隐私数据。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { unifiedDataChannel } from '@kit.ArkData';
```

## ShareOptions12+

PhonePC/2in1TabletTV

UDMF支持的设备内使用范围类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IN\_APP | 0 | 表示允许在本设备同应用内使用。 |
| CROSS\_APP | 1 | 表示允许在本设备内跨应用使用。 |

## GetDelayData12+

PhonePC/2in1TabletTV

type GetDelayData = (type: string) => UnifiedData

对UnifiedData的延迟封装，支持延迟获取数据。当前只支持同设备剪贴板场景，后续场景待开发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 作为延迟数据类型的标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 当延迟回调触发时，返回一个UnifiedData对象。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let getDelayData: unifiedDataChannel.GetDelayData = ((type: string) => {
4. if (type == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
5. let plainTextDetails : Record<string, string> = {
6. 'attr1': 'value1',
7. 'attr2': 'value2'
8. }
9. let plainText : uniformDataStruct.PlainText = {
10. uniformDataType: 'general.plain-text',
11. textContent : 'This is a plain text example',
12. abstract : 'This is abstract',
13. details : plainTextDetails
14. }
15. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
16. let textData = new unifiedDataChannel.UnifiedData(text);
17. return textData;
18. }
19. return new unifiedDataChannel.UnifiedData();
20. });
```

## ValueType12+

PhonePC/2in1TabletTV

type ValueType = number | string | boolean | image.PixelMap | Want | ArrayBuffer | object | null | undefined

用于表示统一数据记录允许的数据字段类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示number的类型。 |
| string | 表示string的类型。 |
| boolean | 表示boolean的类型。 |
| image.PixelMap | 表示[image.PixelMap](arkts-apis-image-pixelmap.md)的类型。 |
| Want | 表示[Want](js-apis-app-ability-want.md)的类型。 |
| ArrayBuffer | 表示ArrayBuffer的类型。 |
| object | 表示object的类型。 |
| null | 表示null。 |
| undefined | 表示undefined。 |

## UnifiedDataProperties12+

PhonePC/2in1TabletTV

定义统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| extras | Record<string, object> | 否 | 是 | 是一个字典类型对象，用于设置其他附加属性数据。非必填字段，默认值为空字典对象。 |
| tag | string | 否 | 是 | 用户自定义标签。非必填字段，默认值为空字符串。 |
| timestamp | Date | 是 | 是 | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)的生成时间戳。默认值为1970年1月1日（UTC）。 |
| shareOptions | [ShareOptions](js-apis-data-unifieddatachannel.md#shareoptions12) | 否 | 是 | 指示[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)支持的设备内使用范围，非必填字段，默认值为CROSS\_APP。 |
| getDelayData | [GetDelayData](js-apis-data-unifieddatachannel.md#getdelaydata12) | 否 | 是 | 延迟获取数据回调。当前只支持同设备剪贴板场景，后续场景待开发。非必填字段，默认值为undefined。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let properties = new unifiedDataChannel.UnifiedDataProperties();
4. properties.extras = {
5. key: {
6. title: 'MyTitle',
7. content: 'MyContent'
8. }
9. };
10. properties.tag = "This is a tag of properties";
11. properties.shareOptions = unifiedDataChannel.ShareOptions.CROSS_APP;
12. properties.getDelayData = ((type: string) => {
13. if (type == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
14. let plainTextDetails : Record<string, string> = {
15. 'attr1': 'value1',
16. 'attr2': 'value2'
17. }
18. let plainText : uniformDataStruct.PlainText = {
19. uniformDataType: 'general.plain-text',
20. textContent : 'This is a plain text example',
21. abstract : 'This is abstract',
22. details : plainTextDetails
23. }
24. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
25. let textData = new unifiedDataChannel.UnifiedData(text);
26. return textData;
27. }
28. return new unifiedDataChannel.UnifiedData();
29. });
```

## UnifiedData

PhonePC/2in1TabletTV

表示UDMF统一数据对象，提供封装一组数据记录的方法。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| properties12+ | [UnifiedDataProperties](js-apis-data-unifieddatachannel.md#unifieddataproperties12) | 否 | 否 | 当前统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

### constructor12+

PhonePC/2in1TabletTV

constructor()

用于创建统一数据对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**示例：**

```
1. let unifiedData = new unifiedDataChannel.UnifiedData();
```

### constructor

PhonePC/2in1TabletTV

constructor(record: UnifiedRecord)

用于创建带有一条数据记录的统一数据对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | [UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord) | 是 | 要添加到统一数据对象中的数据记录，该记录为UnifiedRecord或其子类对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. let plainText : uniformDataStruct.PlainText = {
3. uniformDataType: 'general.plain-text',
4. textContent : 'This is a plain text example',
5. abstract : 'This is abstract'
6. }
7. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
8. let unifiedData = new unifiedDataChannel.UnifiedData(text);
```

### addRecord

PhonePC/2in1TabletTV

addRecord(record: UnifiedRecord): void

在当前统一数据对象中添加一条数据记录。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | [UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord) | 是 | 要添加到统一数据对象中的数据记录，该记录为UnifiedRecord子类对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. let plainText : uniformDataStruct.PlainText = {
3. uniformDataType: 'general.plain-text',
4. textContent : 'This is a plain text example',
5. abstract : 'This is abstract'
6. }
7. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
8. let unifiedData = new unifiedDataChannel.UnifiedData(text);

10. let hyperlink : uniformDataStruct.Hyperlink = {
11. uniformDataType:'general.hyperlink',
12. url : 'www.XXX.com',
13. description : 'This is the description of the hyperlink'
14. }
15. let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
16. unifiedData.addRecord(link);
```

### getRecords

getRecords(): Array<UnifiedRecord>

将当前统一数据对象中的所有数据记录取出。通过本接口取出的数据为UnifiedRecord类型，需通过[getType](js-apis-data-unifieddatachannel.md#gettype)获取数据类型后转为子类再使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord)> | 当前统一数据对象内所添加的记录。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let plainText : uniformDataStruct.PlainText = {
4. uniformDataType: 'general.plain-text',
5. textContent : 'This is a plain text example',
6. abstract : 'This is abstract'
7. }
8. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
9. let unifiedData = new unifiedDataChannel.UnifiedData(text);

11. let hyperlink : uniformDataStruct.Hyperlink = {
12. uniformDataType:'general.hyperlink',
13. url : 'www.XXX.com',
14. description : 'This is the description of the hyperlink'
15. }
16. let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
17. unifiedData.addRecord(link);

19. let records = unifiedData.getRecords();
20. for (let i = 0; i < records.length; i++) {
21. let record = records[i];
22. let types = record.getTypes();
23. if (types.includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
24. let plainText = record.getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as unifiedDataChannel.PlainText;
25. console.info(`textContent: ${plainText.textContent}`);
26. } else if (types.includes(uniformTypeDescriptor.UniformDataType.HYPERLINK)) {
27. let hyperlink = record.getEntry(uniformTypeDescriptor.UniformDataType.HYPERLINK) as unifiedDataChannel.Hyperlink;
28. console.info(`linkUrl: ${hyperlink.url}`);
29. }
30. }
```

### hasType12+

hasType(type: string): boolean

检查当前统一数据对象中是否有指定的数据类型，检查范围包括使用[addEntry](js-apis-data-unifieddatachannel.md#addentry15)函数添加的数据类型。

针对文件类型，若UnifiedData的类型集合中包含"general.jpeg"，在调用hasType接口判断是否包括"general.image"类型时，结果返回true（类型"general.jpeg"归属于类型"general.image"）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要查询的数据类型，见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 有指定的数据类型返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let plainText : uniformDataStruct.PlainText = {
4. uniformDataType: 'general.plain-text',
5. textContent : 'This is a plain text example',
6. abstract : 'This is abstract'
7. }
8. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
9. let unifiedData = new unifiedDataChannel.UnifiedData(text);

11. let hyperlink : uniformDataStruct.Hyperlink = {
12. uniformDataType:'general.hyperlink',
13. url : 'www.XXX.com',
14. description : 'This is the description of the hyperlink'
15. }
16. let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
17. unifiedData.addRecord(link);

19. let hasPlainText = unifiedData.hasType(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT);
20. let hasLink = unifiedData.hasType(uniformTypeDescriptor.UniformDataType.HYPERLINK);
```

### getTypes12+

getTypes(): Array<string>

获取当前统一数据对象所有数据记录的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | [UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)类型的数组，表示当前统一数据对象所有数据记录对应的数据类型。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let plainText : uniformDataStruct.PlainText = {
4. uniformDataType: 'general.plain-text',
5. textContent : 'This is a plain text example',
6. abstract : 'This is abstract'
7. }
8. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
9. let unifiedData = new unifiedDataChannel.UnifiedData(text);

11. let hyperlink : uniformDataStruct.Hyperlink = {
12. uniformDataType:'general.hyperlink',
13. url : 'www.XXX.com',
14. description : 'This is the description of the hyperlink'
15. }
16. let link = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
17. unifiedData.addRecord(link);

19. let types = unifiedData.getTypes();
```

## Summary

PhonePC/2in1TabletTV

描述统一数据对象的数据摘要，包括数据类型和大小。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| summary | Record<string, number> | 否 | 否 | 是一个字典类型对象，key表示数据类型（见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)），value为统一数据对象中该类型记录大小总和（单位：Byte）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| totalSize | number | 否 | 否 | 统一数据对象内记录总大小（单位：Byte）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| overview22+ | Record<string, number> | 是 | 否 | 统一数据对象中所有类型与该类型数据记录大小的映射关系，其中数据大小单位为Byte。当获取到的统一数据对象为空时，此overview属性值为空。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

**示例：**

```
1. function parseSummary(summary : unifiedDataChannel.Summary) {
2. let summaryRecord = summary.summary as Record<string, number>;
3. if (summaryRecord) {
4. for (let item of Object.entries(summaryRecord)) {
5. if (item && item.length <= 1) {
6. continue;
7. }
8. let summaryStr : string = String(item[1]);
9. let info : string[] = summaryStr.split(",");
10. if (info.length <= 1) {
11. continue;
12. }
13. let key : string = info[0];
14. let value : string = info[1];
15. }
16. }
17. let overviewRecord = summary.overview as Record<string, number>;
18. let totalSize = summary.totalSize;
19. }
```

## UnifiedRecord

PhonePC/2in1TabletTV

对UDMF支持的数据内容的抽象定义，称为数据记录。一个统一数据对象内包含一条或多条数据记录，例如一条文本记录、一条图片记录、一条HTML记录等。从API version 15开始，支持往数据记录中增加同一内容的不同表现样式，数据使用方根据业务需要获取对应的样式。

### constructor12+

PhonePC/2in1TabletTV

constructor()

用于创建数据记录。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**示例：**

```
1. let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
```

### constructor12+

PhonePC/2in1TabletTV

constructor(type: string, value: ValueType)

用于创建指定类型和值的数据记录。

当参数value为[image.PixelMap](arkts-apis-image-pixelmap.md)类型时，参数type必须对应为[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)中OPENHARMONY\_PIXEL\_MAP的值；

当参数value为[Want](js-apis-app-ability-want.md)类型时，参数type必须对应为[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)中OPENHARMONY\_WANT的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要创建的数据记录的类型。 |
| value | [ValueType](js-apis-data-unifieddatachannel.md#valuetype12) | 是 | 要创建的数据记录的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';

4. let hyperlink : uniformDataStruct.Hyperlink = {
5. uniformDataType:'general.hyperlink',
6. url : 'www.XXX.com',
7. description : 'This is the description of the hyperlink'
8. }
9. let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);

11. let plainText : uniformDataStruct.PlainText = {
12. uniformDataType: 'general.plain-text',
13. textContent : 'This is a plain text example',
14. abstract : 'This is abstract'
15. }
16. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);

18. let arrayBuffer = new ArrayBuffer(4 * 200 * 200);
19. let opt : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 }, alphaType: 3 };
20. let pixelMap : uniformDataStruct.PixelMap = {
21. uniformDataType : 'openharmony.pixel-map',
22. pixelMap : image.createPixelMapSync(arrayBuffer, opt)
23. }
24. let pixelMapRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```

### getType

getType(): string

获取当前数据记录的类型。由于从统一数据对象中调用[getRecords](js-apis-data-unifieddatachannel.md#getrecords)所取出的数据是UnifiedRecord对象，因此需要通过本接口查询此记录的具体类型，再将该UnifiedRecord对象转换为其子类，调用子类接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前数据记录对应的具体数据类型，见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let plainText : uniformDataStruct.PlainText = {
4. uniformDataType: 'general.plain-text',
5. textContent : 'This is a plain text example',
6. abstract : 'This is abstract'
7. }
8. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
9. let unifiedData = new unifiedDataChannel.UnifiedData(text);

11. let records = unifiedData.getRecords();
12. if (records[0].getType() == uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) {
13. let plainText = records[0] as unifiedDataChannel.PlainText;
14. console.info(`textContent: ${plainText.textContent}`);
15. }
```

### getValue12+

getValue(): ValueType

获取当前数据记录的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValueType](js-apis-data-unifieddatachannel.md#valuetype12) | 当前数据记录对应的值。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, 'this is value of text');
4. let value = text.getValue();

6. let hyperlinkDetails : Record<string, string> = {
7. 'attr1': 'value1',
8. 'attr2': 'value2'
9. }
10. let hyperlink : uniformDataStruct.Hyperlink = {
11. uniformDataType:'general.hyperlink',
12. url : 'www.XXX.com',
13. description : 'This is the description of the hyperlink',
14. details : hyperlinkDetails
15. }
16. let hyperlinkRecord = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
17. let hyperlinkValue = hyperlinkRecord.getValue();
```

### addEntry15+

PhonePC/2in1TabletTV

addEntry(type: string, value: ValueType): void

在当前数据记录中添加一条指定数据类型和内容的数据，通过该方法增加的数据类型和内容为同一内容的不同表现样式.

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要创建的数据类型，见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| value | [ValueType](js-apis-data-unifieddatachannel.md#valuetype12) | 是 | 要创建的数据的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let fileUriDetails : Record<string, string> = {
4. 'attr1': 'value1',
5. 'attr2': 'value2'
6. }
7. let fileUri : uniformDataStruct.FileUri = {
8. uniformDataType : 'general.file-uri',
9. oriUri : 'file://data/image/1.png',
10. fileType : 'general.image',
11. details : fileUriDetails
12. }
13. let hyperlink : uniformDataStruct.Hyperlink = {
14. uniformDataType:'general.hyperlink',
15. url : 'file://data/image/1.png',
16. description : 'This is the description of the hyperlink'
17. }

19. let unifiedData = new unifiedDataChannel.UnifiedData();
20. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
21. record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
22. unifiedData.addRecord(record);
```

### getEntry15+

PhonePC/2in1TabletTV

getEntry(type: string): ValueType

通过数据类型获取数据记录中的数据内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要获取数据的类型，见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ValueType](js-apis-data-unifieddatachannel.md#valuetype12) | 当前数据记录对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let fileUriDetails : Record<string, string> = {
4. 'attr1': 'value1',
5. 'attr2': 'value2'
6. }
7. let fileUri : uniformDataStruct.FileUri = {
8. uniformDataType : 'general.file-uri',
9. oriUri : 'file://data/image/1.png',
10. fileType : 'general.image',
11. details : fileUriDetails
12. }
13. let formDetails : Record<string, string> = {
14. 'attr1': 'value1',
15. 'attr2': 'value2'
16. }
17. let form : uniformDataStruct.Form = {
18. uniformDataType : 'openharmony.form',
19. formId : 1,
20. formName : 'form',
21. bundleName : 'com.xx.app',
22. abilityName : 'ability',
23. module : 'module',
24. details : formDetails
25. }

27. let unifiedData = new unifiedDataChannel.UnifiedData();
28. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
29. record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
30. unifiedData.addRecord(record);

32. let records = unifiedData.getRecords();
33. for (let i = 0; i < records.length; i++) {
34. let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
35. let fileUriRead : uniformDataStruct.FileUri = unifiedDataRecord.getEntry(uniformTypeDescriptor.UniformDataType.FILE_URI) as uniformDataStruct.FileUri;
36. if (fileUriRead != undefined) {
37. console.info(`oriUri: ${fileUriRead.oriUri}`);
38. }
39. let formRead = unifiedDataRecord.getEntry(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM) as uniformDataStruct.Form;
40. if (formRead != undefined) {
41. console.info(`formName: ${formRead.formName}`);
42. }
43. }
```

### getEntries15+

PhonePC/2in1TabletTV

getEntries(): Record<string, ValueType>

获取当前数据记录中所有数据的类型和内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [ValueType](js-apis-data-unifieddatachannel.md#valuetype12)> | 当前数据记录对应的类型和内容。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let fileUriDetails : Record<string, string> = {
4. 'attr1': 'value1',
5. 'attr2': 'value2'
6. }
7. let fileUri : uniformDataStruct.FileUri = {
8. uniformDataType : 'general.file-uri',
9. oriUri : 'file://data/image/1.png',
10. fileType : 'general.image',
11. details : fileUriDetails
12. }
13. let formDetails : Record<string, string> = {
14. 'attr1': 'value1',
15. 'attr2': 'value2'
16. }
17. let form : uniformDataStruct.Form = {
18. uniformDataType : 'openharmony.form',
19. formId : 1,
20. formName : 'form',
21. bundleName : 'com.xx.app',
22. abilityName : 'ability',
23. module : 'module',
24. details : formDetails
25. }

27. let unifiedData = new unifiedDataChannel.UnifiedData();
28. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
29. record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
30. unifiedData.addRecord(record);

32. let records = unifiedData.getRecords();
33. for (let i = 0; i < records.length; i++) {
34. let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
35. let entries : Record<string, unifiedDataChannel.ValueType> = unifiedDataRecord.getEntries();
36. let formRead : uniformDataStruct.Form = entries[uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM] as uniformDataStruct.Form;
37. if (formRead != undefined) {
38. console.info(`formName: ${formRead.formName}`);
39. }
40. let fileUriRead : uniformDataStruct.FileUri = entries[uniformTypeDescriptor.UniformDataType.FILE_URI] as uniformDataStruct.FileUri;
41. if (fileUriRead != undefined) {
42. console.info(`oriUri: ${fileUriRead.oriUri}`);
43. }
44. }
```

### getTypes15+

getTypes(): Array<string>

获取数据记录中数据的所有类型集合。可通过UnifiedRecord数据记录对象调用本接口，查询出此记录中数据的所有类型集合，包括使用[addEntry](js-apis-data-unifieddatachannel.md#addentry15)函数添加的数据类型。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力** ：SystemCapability.DistributedDataManager.UDMF.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | [UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)类型的数组，表示当前记录的数据类型集合。 |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

3. let fileUriDetails : Record<string, string> = {
4. 'attr1': 'value1',
5. 'attr2': 'value2'
6. }
7. let fileUri : uniformDataStruct.FileUri = {
8. uniformDataType : 'general.file-uri',
9. oriUri : 'file://data/image/1.png',
10. fileType : 'general.image',
11. details : fileUriDetails
12. }
13. let formDetails : Record<string, string> = {
14. 'attr1': 'value1',
15. 'attr2': 'value2'
16. }
17. let form : uniformDataStruct.Form = {
18. uniformDataType : 'openharmony.form',
19. formId : 1,
20. formName : 'form',
21. bundleName : 'com.xx.app',
22. abilityName : 'ability',
23. module : 'module',
24. details : formDetails
25. }

27. let unifiedData = new unifiedDataChannel.UnifiedData();
28. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
29. record.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
30. unifiedData.addRecord(record);

32. let records = unifiedData.getRecords();
33. for (let i = 0; i < records.length; i++) {
34. let unifiedDataRecord = records[i] as unifiedDataChannel.UnifiedRecord;
35. let types : Array<string> = unifiedDataRecord.getTypes();
36. if (types.includes(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM)) {
37. console.info(`Types include: ${uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM}`);
38. }
39. }
```

## Text

PhonePC/2in1TabletTV

文本类型数据，是[UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord)的子类，也是文本类型数据的基类，用于描述文本类数据，推荐开发者优先使用Text的子类描述数据，如[PlainText](js-apis-data-unifieddatachannel.md#plaintext)、[Hyperlink](js-apis-data-unifieddatachannel.md#hyperlink)、[HTML](js-apis-data-unifieddatachannel.md#html)等具体子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述文本内容。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象，用于描述一篇文章。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. let text = new unifiedDataChannel.Text();
2. text.details = {
3. title: 'MyTitle',
4. content: 'This is content'
5. };
6. let unifiedData = new unifiedDataChannel.UnifiedData(text);
```

## PlainText

PhonePC/2in1TabletTV

[Text](js-apis-data-unifieddatachannel.md#text)的子类，用于描述纯文本类数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textContent | string | 否 | 否 | 纯文本内容。 |
| abstract | string | 否 | 是 | 纯文本摘要，非必填字段，默认值为空字符串。 |

**示例：**

```
1. let text = new unifiedDataChannel.PlainText();
2. text.textContent = 'this is textContent';
3. text.abstract = 'This is abstract';
```

## Hyperlink

PhonePC/2in1TabletTV

[Text](js-apis-data-unifieddatachannel.md#text)的子类，用于描述超链接类型数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 链接url。 |
| description | string | 否 | 是 | 链接内容描述，非必填字段，默认值为空字符串。 |

**示例：**

```
1. let link = new unifiedDataChannel.Hyperlink();
2. link.url = 'www.XXX.com';
3. link.description = 'This is description';
```

## HTML

PhonePC/2in1TabletTV

HTML类型数据，是[Text](js-apis-data-unifieddatachannel.md#text)的子类，用于描述超文本标记语言数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| htmlContent | string | 否 | 否 | html格式内容。 |
| plainContent | string | 否 | 是 | 去除html标签后的纯文本内容，非必填字段，默认值为空字符串。 |

**示例：**

```
1. let html = new unifiedDataChannel.HTML();
2. html.htmlContent = '<div><p>标题</p></div>';
3. html.plainContent = 'This is plainContent';
```

## File

PhonePC/2in1TabletTV

File类型数据，是[UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord)的子类，也是文件类型数据的基类，用于描述文件类型数据，推荐开发者优先使用File的子类描述数据，如[Image](js-apis-data-unifieddatachannel.md#image)、[Video](js-apis-data-unifieddatachannel.md#video)、[Folder](js-apis-data-unifieddatachannel.md#folder)等具体子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述文件相关信息。例如，可生成一个details内容为  {  "name":"文件名",  "type":"文件类型"  }  的数据对象，用于描述一个文件。非必填字段，默认值为空字典对象。 |
| uri | string | 否 | 否 | 本地文件数据uri或网络文件uri，本地文件数据uri可通过[getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)函数获取。 |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';
2. import { fileUri } from '@kit.CoreFileKit'
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let context = this.context;
9. let pathDir = context.filesDir;
10. let file = new unifiedDataChannel.File();
11. file.details = {
12. name: 'test',
13. type: 'txt'
14. };
15. let filePath = pathDir + '/test.txt';
16. file.uri = fileUri.getUriFromPath(filePath);
17. }
18. }
```

## Image

PhonePC/2in1TabletTV

图片类型数据，是[File](js-apis-data-unifieddatachannel.md#file)的子类，用于描述图片文件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imageUri | string | 否 | 否 | 本地图片数据uri或网络图片uri，本地图片数据uri可通过[getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)函数获取。 |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';
2. import { fileUri } from '@kit.CoreFileKit'
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let context = this.context;
9. let pathDir = context.filesDir;
10. let image = new unifiedDataChannel.Image();
11. let filePath = pathDir + '/test.jpg';
12. image.imageUri = fileUri.getUriFromPath(filePath);
13. }
14. }
```

## Video

PhonePC/2in1TabletTV

视频类型数据，是[File](js-apis-data-unifieddatachannel.md#file)的子类，用于描述视频文件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| videoUri | string | 否 | 否 | 本地视频数据uri或网络视频uri，本地视频数据uri可通过[getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)函数获取。 |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';
2. import { fileUri } from '@kit.CoreFileKit'
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let context = this.context;
9. let pathDir = context.filesDir;
10. let video = new unifiedDataChannel.Video();
11. let filePath = pathDir + '/test.mp4';
12. video.videoUri =fileUri.getUriFromPath(filePath);
13. }
14. }
```

## Audio

PhonePC/2in1TabletTV

音频类型数据，是[File](js-apis-data-unifieddatachannel.md#file)的子类，用于描述音频文件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| audioUri | string | 否 | 否 | 本地音频数据uri或网络音频uri，本地音频数据uri可通过[getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)函数获取。 |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';
2. import { fileUri } from '@kit.CoreFileKit'
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let context = this.context;
9. let pathDir = context.filesDir;
10. let audio = new unifiedDataChannel.Audio();
11. let filePath = pathDir + '/test.mp3';
12. audio.audioUri = fileUri.getUriFromPath(filePath);
13. }
14. }
```

## Folder

PhonePC/2in1TabletTV

文件夹类型数据，是[File](js-apis-data-unifieddatachannel.md#file)的子类，用于描述文件夹。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| folderUri | string | 否 | 否 | 本地文件夹数据uri或网络文件夹uri，本地文件夹数据uri可通过[getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)函数获取。 |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';
2. import { fileUri } from '@kit.CoreFileKit'
3. import { UIAbility } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. let context = this.context;
9. let pathDir = context.filesDir;
10. let folder = new unifiedDataChannel.Folder();
11. let filePath = pathDir + '/folder';
12. folder.folderUri = fileUri.getUriFromPath(filePath);
13. }
14. }
```

## SystemDefinedRecord

PhonePC/2in1TabletTV

SystemDefinedRecord是[UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord)的子类，也是HarmonyOS系统特有数据类型的基类，用于描述仅在HarmonyOS系统范围内流通的特有数据类型，推荐开发者优先使用SystemDefinedRecord的子类描述数据，如[SystemDefinedForm](js-apis-data-unifieddatachannel.md#systemdefinedform)、[SystemDefinedAppItem](js-apis-data-unifieddatachannel.md#systemdefinedappitem)、[SystemDefinedPixelMap](js-apis-data-unifieddatachannel.md#systemdefinedpixelmap)等具体子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. let sdr = new unifiedDataChannel.SystemDefinedRecord();
2. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
3. sdr.details = {
4. title: 'recordTitle',
5. version: 1,
6. content: u8Array
7. };
8. let unifiedData = new unifiedDataChannel.UnifiedData(sdr);
```

## SystemDefinedForm

PhonePC/2in1TabletTV

系统定义的桌面卡片类型数据，是[SystemDefinedRecord](js-apis-data-unifieddatachannel.md#systemdefinedrecord)的子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | number | 否 | 否 | 卡片id。 |
| formName | string | 否 | 否 | 卡片名称。 |
| bundleName | string | 否 | 否 | 卡片所属的bundle名。 |
| abilityName | string | 否 | 否 | 卡片对应的ability名。 |
| module | string | 否 | 否 | 卡片所属的module名。 |

**示例：**

```
1. let form = new unifiedDataChannel.SystemDefinedForm();
2. form.formId = 123456;
3. form.formName = 'MyFormName';
4. form.bundleName = 'MyBundleName';
5. form.abilityName = 'MyAbilityName';
6. form.module = 'MyModule';
7. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
8. form.details = {
9. formKey1: 123,
10. formKey2: 'formValue',
11. formKey3: u8Array
12. };
13. let unifiedData = new unifiedDataChannel.UnifiedData(form);
```

## SystemDefinedAppItem

PhonePC/2in1TabletTV

系统定义的桌面图标类型数据，是[SystemDefinedRecord](js-apis-data-unifieddatachannel.md#systemdefinedrecord)的子类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appId | string | 否 | 否 | 图标对应的应用id。 |
| appName | string | 否 | 否 | 图标对应的应用名。 |
| appIconId | string | 否 | 否 | 图标的图片id。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| appLabelId | string | 否 | 否 | 图标名称对应的标签id。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| bundleName | string | 否 | 否 | 图标对应的应用bundle名。 |
| abilityName | string | 否 | 否 | 图标对应的应用ability名。 |

**示例：**

```
1. let appItem = new unifiedDataChannel.SystemDefinedAppItem();
2. appItem.appId = 'MyAppId';
3. appItem.appName = 'MyAppName';
4. appItem.appIconId = 'MyAppIconId';
5. appItem.appLabelId = 'MyAppLabelId';
6. appItem.bundleName = 'MyBundleName';
7. appItem.abilityName = 'MyAbilityName';
8. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
9. appItem.details = {
10. appItemKey1: 123,
11. appItemKey2: 'appItemValue',
12. appItemKey3: u8Array
13. };
14. let unifiedData = new unifiedDataChannel.UnifiedData(appItem);
```

## SystemDefinedPixelMap

PhonePC/2in1TabletTV

与系统侧定义的[PixelMap](arkts-apis-image-pixelmap.md)数据类型对应的图片数据类型，是[SystemDefinedRecord](js-apis-data-unifieddatachannel.md#systemdefinedrecord)的子类，仅保存PixelMap的二进制数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rawData | Uint8Array | 否 | 否 | PixelMap对象的二进制数据。 |

**示例：**

```
1. import { image } from '@kit.ImageKit'; // PixelMap类定义所在模块
2. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const color = new ArrayBuffer(96); // 创建pixelMap对象
6. let opts: image.InitializationOptions = {
7. editable: true, pixelFormat: 3, size: {
8. height: 4, width: 6
9. }
10. }
11. image.createPixelMap(color, opts, (error, pixelMap) => {
12. if (error) {
13. console.error('Failed to create pixelMap.');
14. } else {
15. console.info('Succeeded in creating pixelMap.');
16. let arrayBuf = new ArrayBuffer(pixelMap.getPixelBytesNumber());
17. pixelMap.readPixelsToBuffer(arrayBuf);
18. let u8Array = new Uint8Array(arrayBuf);
19. let sdPixel = new unifiedDataChannel.SystemDefinedPixelMap();
20. sdPixel.rawData = u8Array;
21. let unifiedData = new unifiedDataChannel.UnifiedData(sdPixel);

23. // 从unifiedData中读取pixelMap类型的record
24. let records = unifiedData.getRecords();
25. for (let i = 0; i < records.length; i++) {
26. if (records[i].getType() === uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) {
27. let pixelMapRecord = records[i] as unifiedDataChannel.SystemDefinedPixelMap;
28. let newArrayBuf = pixelMapRecord.rawData.buffer;
29. pixelMap.writeBufferToPixels(newArrayBuf).then(() => {
30. console.info('Succeeded in writing data from buffer to a pixelMap');
31. }).catch((error: BusinessError) => {
32. console.error(`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}`);
33. })
34. }
35. }
36. }
37. })
```

## ApplicationDefinedRecord

PhonePC/2in1TabletTV

ApplicationDefinedRecord是[UnifiedRecord](js-apis-data-unifieddatachannel.md#unifiedrecord)的子类，也是应用自定义数据类型的基类，用于描述仅在应用生态内部流通的自定义数据类型，应用可基于此类进行自定义数据类型的扩展。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| applicationDefinedType | string | 否 | 否 | 应用自定义类型标识符，必须以'ApplicationDefined'开头。 |
| rawData | Uint8Array | 否 | 否 | 应用自定义数据类型的二进制数据。 |

**示例：**

```
1. let record = new unifiedDataChannel.ApplicationDefinedRecord();
2. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
3. record.applicationDefinedType = 'ApplicationDefinedType';
4. record.rawData = u8Array;
5. let unifiedData = new unifiedDataChannel.UnifiedData(record);
```

## Intention

PhonePC/2in1TabletTV

UDMF已经支持的数据通路枚举类型。其主要用途是标识各种UDMF数据通路所面向的不同业务场景。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_HUB | 'DataHub' | 公共数据通路。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DRAG14+ | 'Drag' | 拖拽类型数据通道。  **模型约束：** 此接口仅可在Stage模型下使用。  **适用场景：** 适用于在拖拽场景下使用UDMF来跨应用数据共享。 |
| SYSTEM\_SHARE20+ | 'SystemShare' | 系统分享类型数据通道。  **模型约束：** 此接口仅可在Stage模型下使用。  **适用场景：** 适用于在系统分享场景下使用UDMF来跨应用数据共享。 |
| PICKER20+ | 'Picker' | Picker类型数据通道。  **模型约束：** 此接口仅可在Stage模型下使用。  **适用场景：** 适用于在Picker选择器场景下使用UDMF来跨应用数据共享。 |
| MENU20+ | 'Menu' | 菜单类型数据通道。  **模型约束：** 此接口仅可在Stage模型下使用。  **适用场景：** 适用于在右键菜单场景下使用UDMF来跨应用数据共享。 |

## Visibility20+

PhonePC/2in1TabletTV

表示数据的可见性等级枚举。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 可见性等级，所有应用可见。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| OWN\_PROCESS | 1 | 可见性等级，仅数据提供者可见。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## Options

PhonePC/2in1TabletTV

UDMF提供的数据操作接口包含三个可选参数：intention、key和visibility。如果接口不需要这些参数，可以不填，具体要求请参阅该接口的参数说明。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intention | [Intention](js-apis-data-unifieddatachannel.md#intention) | 否 | 是 | 表示数据操作相关的数据通路类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| key | string | 否 | 是 | UDMF中数据对象的唯一标识符，可通过[insertData](js-apis-data-unifieddatachannel.md#unifieddatachannelinsertdata)接口的返回值获取。  由udmf:/、intention、bundleName和groupId四部分组成，以'/'连接，比如：udmf://DataHub/com.ohos.test/0123456789。  其中udmf:/固定，DataHub为对应枚举的取值，com.ohos.test为包名，0123456789为随机生成的groupId。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| visibility20+ | [Visibility](js-apis-data-unifieddatachannel.md#visibility20) | 否 | 是 | 表示数据的可见性等级。只在写入数据的时候填写才生效，若不填写默认是Visibility.ALL。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## FileConflictOptions15+

PhonePC/2in1TabletTV

表示文件拷贝冲突时的可选策略的枚举。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERWRITE | 0 | 目标路径存在同文件名时覆盖。 |
| SKIP | 1 | 目标路径存在同文件名时跳过。 |

## ProgressIndicator15+

PhonePC/2in1TabletTV

表示进度条指示选项的枚举，可选择是否采用系统默认进度显示。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不采用系统默认进度显示。 |
| DEFAULT | 1 | 采用系统默认进度显示，500ms内获取数据完成将不会拉起默认进度条。 |

## ListenerStatus15+

PhonePC/2in1TabletTV

表示从UDMF获取数据时的状态码的枚举。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FINISHED | 0 | 表示已完成。 |
| PROCESSING | 1 | 表示正在处理中。 |
| CANCELED | 2 | 表明本次处理已被取消。 |
| INNER\_ERROR | 200 | 表明发生了内部错误。 |
| INVALID\_PARAMETERS | 201 | 表示 [GetDataParams](js-apis-data-unifieddatachannel.md#getdataparams15) 包含无效参数。 |
| DATA\_NOT\_FOUND | 202 | 表示没有获取到数据。 |
| SYNC\_FAILED | 203 | 表示同步过程中出现错误。 |
| COPY\_FILE\_FAILED | 204 | 表示文件拷贝过程中出现错误。 |

## ProgressInfo15+

PhonePC/2in1TabletTV

定义进度上报的数据。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 系统上报拖拽任务进度百分比。取值范围为[-1-100]的整数，其中-1时代表本次获取数据失败，100时表示本次获取数据完成。 |
| status | [ListenerStatus](js-apis-data-unifieddatachannel.md#listenerstatus15) | 否 | 否 | 系统上报拖拽任务的状态码。 |

## DataProgressListener15+

PhonePC/2in1TabletTV

type DataProgressListener = (progressInfo: ProgressInfo, data: UnifiedData | null) => void

定义获取进度信息和数据的监听回调函数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progressInfo | [ProgressInfo](js-apis-data-unifieddatachannel.md#progressinfo15) | 是 | 定义进度上报的进度信息。 |
| data | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | null | 是 | 进度达到100时获取的数据，进度未到100时返回null。 |

## GetDataParams15+

PhonePC/2in1TabletTV

表示从UDMF获取数据时的参数，包含目标路径、文件冲突选项、进度条类型等。

具体使用示例可见[拖拽异步获取数据](ts-universal-events-drag-drop.md#示例3拖拽异步获取数据)。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressIndicator | [ProgressIndicator](js-apis-data-unifieddatachannel.md#progressindicator15) | 否 | 否 | 定义进度条指示选项，可选择是否采用系统默认进度显示。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| dataProgressListener | [DataProgressListener](js-apis-data-unifieddatachannel.md#dataprogresslistener15) | 否 | 否 | 表示获取统一数据时的进度和数据监听器。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| destUri | string | 否 | 是 | 拷贝文件的目标路径。若不支持文件处理，则不需要设置此参数，默认为空；若支持文件处理，须设置一个已经存在的目录。若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。不填写时获取到的uri为源端路径URI，填写后获取到的uri为目标路径uri。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| fileConflictOptions | [FileConflictOptions](js-apis-data-unifieddatachannel.md#fileconflictoptions15) | 否 | 是 | 定义文件拷贝冲突时的选项，默认为OVERWRITE。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| acceptableInfo20+ | [DataLoadInfo](js-apis-data-unifieddatachannel.md#dataloadinfo20) | 否 | 是 | 定义接收方对数据类型和数据记录数量的接收能力。延迟加载场景下，发送方可根据此信息生成并返回更合适的数据内容。默认为空，不提供接收方数据接收能力。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## DataLoadInfo20+

PhonePC/2in1TabletTV

用于描述被加载数据的类型与数量。

* 在**数据发送方**中使用，表示实际可提供的数据范围，必须设置该字段。
* 在**数据接收方**中使用，表示期望加载的数据类型与数量，可根据需要设置该字段。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| types | Set<string> | 否 | 是 | 表示数据类型集合，默认为空集合。 |
| recordCount | number | 否 | 是 | 表示期望或可提供的最大数据记录数，默认值为0，取值范围为[0, 232-1]。超过取值范围时会按默认值处理。设置为浮点数时，仅使用整数部分。当用于拖拽时，会作为角标数量显示，最大支持231-1，超过此数值时不显示角标。作为角标数量时，优先级低于[DragPreviewOptions](ts-universal-attributes-drag-drop.md#dragpreviewoptions11)中的numberBadge方法。 |

## DataLoadHandler20+

PhonePC/2in1TabletTV

type DataLoadHandler = (acceptableInfo?: DataLoadInfo) => UnifiedData | null

用于延迟加载数据的处理函数。支持数据发送方根据接收方传入的信息，动态生成数据，实现更灵活、精准的数据交互策略。

该处理函数为同步函数，适用于处理简单业务逻辑，若函数业务逻辑较复杂、执行时间较长（3s以上），推荐使用异步处理函数[DelayedDataLoadHandler](js-apis-data-unifieddatachannel.md#delayeddataloadhandler22)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| acceptableInfo | [DataLoadInfo](js-apis-data-unifieddatachannel.md#dataloadinfo20) | 否 | 表示数据接收方可以接收的数据类型和数量，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | null | 当延迟处理函数触发时，返回UnifiedData或null。 |

## DelayedDataLoadHandler22+

PhonePC/2in1TabletTV

type DelayedDataLoadHandler = (acceptableInfo?: DataLoadInfo) => Promise<UnifiedData | null>

用于延迟加载数据的处理函数。支持数据发送方根据接收方传入的信息，动态生成数据，实现更灵活、精准的数据交互策略。

该处理函数为异步函数，返回Promise对象，不阻塞主线程，可处理复杂业务逻辑、执行长耗时任务。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| acceptableInfo | [DataLoadInfo](js-apis-data-unifieddatachannel.md#dataloadinfo20) | 否 | 表示数据接收方可以接收的数据类型和数量，默认为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | null> | 当延迟处理函数触发时，返回Promise对象。 |

## DataLoadParams20+

PhonePC/2in1TabletTV

用于在延迟加载场景下描述发送方的数据加载策略。

当同时传入loadHandler和delayedDataLoadHandler时，优先使用delayedDataLoadHandler，loadHandler不生效。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| loadHandler | [DataLoadHandler](js-apis-data-unifieddatachannel.md#dataloadhandler20) | 否 | 否 | 表示用于延迟加载数据的处理函数。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| delayedDataLoadHandler22+ | [DelayedDataLoadHandler](js-apis-data-unifieddatachannel.md#delayeddataloadhandler22) | 否 | 是 | 表示用于延迟加载数据的异步处理函数。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用.  **模型约束：** 此接口仅可在Stage模型下使用。 |
| dataLoadInfo | [DataLoadInfo](js-apis-data-unifieddatachannel.md#dataloadinfo20) | 否 | 否 | 用于描述当前发送方可生成的数据类型及数量信息。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## unifiedDataChannel.insertData

PhonePC/2in1TabletTV

insertData(options: Options, data: UnifiedData, callback: AsyncCallback<string>): void

将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，参数中intention字段必填，且不支持DRAG，不填时会返回401错误码；其他字段是否填写均不影响接口的使用。 |
| data | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 目标数据。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回写入UDMF的数据的唯一标识符key的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let plainText : uniformDataStruct.PlainText = {
5. uniformDataType: 'general.plain-text',
6. textContent : 'This is a plain text example',
7. abstract : 'This is abstract'
8. }
9. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
10. let unifiedData = new unifiedDataChannel.UnifiedData(text);

12. let options: unifiedDataChannel.Options = {
13. intention: unifiedDataChannel.Intention.DATA_HUB
14. }
15. try {
16. unifiedDataChannel.insertData(options, unifiedData, (err, key) => {
17. if (err === undefined) {
18. console.info(`Succeeded in inserting data. key = ${key}`);
19. } else {
20. console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
21. }
22. });
23. } catch (e) {
24. let error: BusinessError = e as BusinessError;
25. console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
26. }
```

## unifiedDataChannel.insertData

PhonePC/2in1TabletTV

insertData(options: Options, data: UnifiedData): Promise<string>

将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，参数中intention字段必填，且不支持DRAG，不填时会返回401错误码；其他字段是否填写均不影响接口的使用。 |
| data | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 目标数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回写入UDMF的数据的唯一标识符key的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let plainText : uniformDataStruct.PlainText = {
5. uniformDataType: 'general.plain-text',
6. textContent : 'This is a plain text example',
7. abstract : 'This is abstract'
8. }
9. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
10. let unifiedData = new unifiedDataChannel.UnifiedData(text);

12. let options: unifiedDataChannel.Options = {
13. intention: unifiedDataChannel.Intention.DATA_HUB
14. }
15. try {
16. unifiedDataChannel.insertData(options, unifiedData).then((key) => {
17. console.info(`Succeeded in inserting data. key = ${key}`);
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
20. });
21. } catch (e) {
22. let error: BusinessError = e as BusinessError;
23. console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
24. }
```

## unifiedDataChannel.updateData

PhonePC/2in1TabletTV

updateData(options: Options, data: UnifiedData, callback: AsyncCallback<void>): void

更新已写入UDMF的公共数据通路的数据，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，参数中key字段必填，不填时会返回401错误码；intention参数仅支持DATA\_HUB；其他字段是否填写均不影响接口的使用。 |
| data | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 目标数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当更新数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let plainText : uniformDataStruct.PlainText = {
5. uniformDataType: 'general.plain-text',
6. textContent : 'This is a plain text example',
7. abstract : 'This is abstract'
8. }
9. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
10. let unifiedData = new unifiedDataChannel.UnifiedData(text);
11. let options: unifiedDataChannel.Options = {
12. intention: unifiedDataChannel.Intention.DATA_HUB
13. }
14. try {
15. unifiedDataChannel.insertData(options, unifiedData).then((key) => {
16. console.info(`Succeeded in inserting data. key = ${key}`);
17. let updateOptions: unifiedDataChannel.Options = {
18. intention: unifiedDataChannel.Intention.DATA_HUB,
19. key: key
20. }
21. let plainTextUpdate : uniformDataStruct.PlainText = {
22. uniformDataType: 'general.plain-text',
23. textContent : 'This is plainText textContent for update',
24. abstract : 'This is abstract for update'
25. }
26. let textUpdate = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextUpdate);
27. let unifiedDataUpdate = new unifiedDataChannel.UnifiedData(textUpdate);
28. try {
29. unifiedDataChannel.updateData(updateOptions, unifiedDataUpdate, (err) => {
30. if (err === undefined) {
31. console.info('Succeeded in updating data.');
32. } else {
33. console.error(`Failed to update data. code is ${err.code}, message is ${err.message} `);
34. }
35. });
36. } catch (e) {
37. let error: BusinessError = e as BusinessError;
38. console.error(`Update data throws an exception. code is ${error.code}, message is ${error.message} `);
39. }
40. }).catch((err: BusinessError) => {
41. console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
42. });
43. } catch (e) {
44. let error: BusinessError = e as BusinessError;
45. console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
46. }
```

## unifiedDataChannel.updateData

PhonePC/2in1TabletTV

updateData(options: Options, data: UnifiedData): Promise<void>

更新已写入UDMF的公共数据通路的数据，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，参数中key字段必填，不填时会返回401错误码；intention参数仅支持DATA\_HUB；其他字段是否填写均不影响接口的使用。 |
| data | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 目标数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let plainText : uniformDataStruct.PlainText = {
5. uniformDataType: 'general.plain-text',
6. textContent : 'This is a plain text example',
7. abstract : 'This is abstract'
8. }
9. let text = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
10. let unifiedData = new unifiedDataChannel.UnifiedData(text);
11. let options: unifiedDataChannel.Options = {
12. intention: unifiedDataChannel.Intention.DATA_HUB
13. }
14. try {
15. unifiedDataChannel.insertData(options, unifiedData).then((key) => {
16. console.info(`Succeeded in inserting data. key = ${key}`);
17. let updateOptions: unifiedDataChannel.Options = {
18. intention: unifiedDataChannel.Intention.DATA_HUB,
19. key: key
20. }
21. let plainTextUpdate : uniformDataStruct.PlainText = {
22. uniformDataType: 'general.plain-text',
23. textContent : 'This is plainText textContent for update',
24. abstract : 'This is abstract for update'
25. }
26. let textUpdate = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextUpdate);
27. let unifiedDataUpdate = new unifiedDataChannel.UnifiedData(textUpdate);
28. try {
29. unifiedDataChannel.updateData(updateOptions, unifiedDataUpdate).then(() => {
30. console.info('Succeeded in updating data.');
31. }).catch((err: BusinessError) => {
32. console.error(`Failed to update data. code is ${err.code}, message is ${err.message} `);
33. });
34. } catch (e) {
35. let error: BusinessError = e as BusinessError;
36. console.error(`Update data throws an exception. code is ${error.code}, message is ${error.message} `);
37. }
38. }).catch((err: BusinessError) => {
39. console.error(`Failed to insert data. code is ${err.code}, message is ${err.message} `);
40. });
41. } catch (e) {
42. let error: BusinessError = e as BusinessError;
43. console.error(`Insert data throws an exception. code is ${error.code}, message is ${error.message} `);
44. }
```

## unifiedDataChannel.queryData

PhonePC/2in1TabletTV

queryData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void

查询UDMF公共数据通路的数据，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，key和intention均为可选，且intention参数不支持DRAG，根据传入的参数做相应的校验以返回不同的值。 |
| callback | AsyncCallback<Array<[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)>> | 是 | 回调函数，返回查询到的所有数据。  如果options中填入的是key，则返回key对应的数据；  如果options中填入的是intention，则返回intention下所有数据。  如intention和key均填写了，取两者查询数据的交集，与options只填入key的获取结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let options: unifiedDataChannel.Options = {
5. intention: unifiedDataChannel.Intention.DATA_HUB
6. };

8. try {
9. unifiedDataChannel.queryData(options, (err, data) => {
10. if (err === undefined) {
11. console.info(`Succeeded in querying data. size = ${data.length}`);
12. for (let i = 0; i < data.length; i++) {
13. let records = data[i].getRecords();
14. for (let j = 0; j < records.length; j++) {
15. if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
16. let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
17. console.info(`${i + 1}.${text.textContent}`);
18. }
19. }
20. }
21. } else {
22. console.error(`Failed to query data. code is ${err.code}, message is ${err.message} `);
23. }
24. });
25. } catch (e) {
26. let error: BusinessError = e as BusinessError;
27. console.error(`Query data throws an exception. code is ${error.code}, message is ${error.message} `);
28. }
```

## unifiedDataChannel.queryData

PhonePC/2in1TabletTV

queryData(options: Options): Promise<Array<UnifiedData>>

查询UDMF公共数据通路的数据，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，key和intention均为可选，且intention参数不支持DRAG，根据传入的参数做相应的校验以返回不同的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)>> | Promise对象，返回查询到的所有数据。  如果options中填入的是key，则返回key对应的数据。  如果options中填入的是intention，则返回intention下所有数据。  如intention和key均填写了，取两者查询数据的交集，与options只填入key的获取结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let options: unifiedDataChannel.Options = {
5. key: 'udmf://DataHub/com.ohos.test/0123456789'
6. };

8. try {
9. unifiedDataChannel.queryData(options).then((data) => {
10. console.info(`Succeeded in querying data. size = ${data.length}`);
11. for (let i = 0; i < data.length; i++) {
12. let records = data[i].getRecords();
13. for (let j = 0; j < records.length; j++) {
14. if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
15. let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
16. console.info(`${i + 1}.${text.textContent}`);
17. }
18. }
19. }
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to query data. code is ${err.code}, message is ${err.message} `);
22. });
23. } catch (e) {
24. let error: BusinessError = e as BusinessError;
25. console.error(`Query data throws an exception. code is ${error.code}, message is ${error.message} `);
26. }
```

## unifiedDataChannel.deleteData

PhonePC/2in1TabletTV

deleteData(options: Options, callback: AsyncCallback<Array<UnifiedData>>): void

删除UDMF公共数据通路的数据，返回删除的数据集，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，key和intention均为可选，且intention参数仅支持DATA\_HUB，根据传入的参数做相应的校验以返回不同的值。 |
| callback | AsyncCallback<Array<[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)>> | 是 | 回调函数，返回删除的所有数据。  如果options中填入的是key，则删除key对应的数据并返回该数据。  如果options中填入的是intention，则删除intention下所有数据并返回删除的数据。  如intention和key均填写了，取两者数据的交集进行删除，并返回删除的数据，与options只填入key的结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let options: unifiedDataChannel.Options = {
5. intention: unifiedDataChannel.Intention.DATA_HUB
6. };

8. try {
9. unifiedDataChannel.deleteData(options, (err, data) => {
10. if (err === undefined) {
11. console.info(`Succeeded in deleting data. size = ${data.length}`);
12. for (let i = 0; i < data.length; i++) {
13. let records = data[i].getRecords();
14. for (let j = 0; j < records.length; j++) {
15. if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
16. let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
17. console.info(`${i + 1}.${text.textContent}`);
18. }
19. }
20. }
21. } else {
22. console.error(`Failed to delete data. code is ${err.code}, message is ${err.message} `);
23. }
24. });
25. } catch (e) {
26. let error: BusinessError = e as BusinessError;
27. console.error(`Delete data throws an exception. code is ${error.code}, message is ${error.message} `);
28. }
```

## unifiedDataChannel.deleteData

PhonePC/2in1TabletTV

deleteData(options: Options): Promise<Array<UnifiedData>>

删除UDMF公共数据通路的数据，返回删除的数据集，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Options](js-apis-data-unifieddatachannel.md#options) | 是 | 配置项参数，key和intention均为可选，且intention参数仅支持DATA\_HUB，根据传入的参数做相应的校验以返回不同的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)>> | Promise对象，返回删除的所有数据。  如果options中填入的是key，则删除key对应的数据并返回该数据。  如果options中填入的是intention，则删除intention下所有数据并返回删除的数据。  如intention和key均填写了，取两者数据的交集进行删除，并返回删除的数据，与options只填入key的结果一致；如没有交集报错。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let options: unifiedDataChannel.Options = {
5. key: 'udmf://DataHub/com.ohos.test/0123456789'
6. };

8. try {
9. unifiedDataChannel.deleteData(options).then((data) => {
10. console.info(`Succeeded in deleting data. size = ${data.length}`);
11. for (let i = 0; i < data.length; i++) {
12. let records = data[i].getRecords();
13. for (let j = 0; j < records.length; j++) {
14. if (records[j].getTypes().includes(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT)) {
15. let text = records[j].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
16. console.info(`${i + 1}.${text.textContent}`);
17. }
18. }
19. }
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to delete data. code is ${err.code}, message is ${err.message} `);
22. });
23. } catch (e) {
24. let error: BusinessError = e as BusinessError;
25. console.error(`Query data throws an exception. code is ${error.code}, message is ${error.message} `);
26. }
```

## unifiedDataChannel.setAppShareOptions14+

PhonePC/2in1TabletTV

setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void

设置应用内拖拽通道数据可使用的范围[ShareOptions](js-apis-data-unifieddatachannel.md#shareoptions12)，目前仅支持DRAG类型数据通道的管控设置。

**需要权限:** ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intention | [Intention](js-apis-data-unifieddatachannel.md#intention) | 是 | 表示数据操作相关的数据通路类型，目前仅支持DRAG类型数据通道。 |
| shareOptions | [ShareOptions](js-apis-data-unifieddatachannel.md#shareoptions12) | 是 | 指示[UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata)支持的设备内使用范围。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[统一数据管理框架错误码](errorcode-udmf.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION". |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 20400001 | Settings already exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. unifiedDataChannel.setAppShareOptions(unifiedDataChannel.Intention.DRAG, unifiedDataChannel.ShareOptions.IN_APP);
4. console.info(`[UDMF]setAppShareOptions success. `);
5. }catch (e){
6. let error: BusinessError = e as BusinessError;
7. console.error(`[UDMF]setAppShareOptions throws an exception. code is ${error.code}, message is ${error.message} `);
8. }
```

## unifiedDataChannel.removeAppShareOptions14+

PhonePC/2in1TabletTV

removeAppShareOptions(intention: Intention): void

清除[setAppShareOptions](js-apis-data-unifieddatachannel.md#unifieddatachannelsetappshareoptions14)设置的管控信息。

**需要权限:** ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intention | [Intention](js-apis-data-unifieddatachannel.md#intention) | 是 | 表示数据操作相关的数据通路类型，目前仅支持DRAG类型数据通道。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION". |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. unifiedDataChannel.removeAppShareOptions(unifiedDataChannel.Intention.DRAG);
4. console.info(`[UDMF]removeAppShareOptions success. `);
5. }catch (e){
6. let error: BusinessError = e as BusinessError;
7. console.error(`[UDMF]removeAppShareOptions throws an exception. code is ${error.code}, message is ${error.message} `);
8. }
```

## unifiedDataChannel.convertRecordsToEntries17+

PhonePC/2in1TabletTV

convertRecordsToEntries(data: UnifiedData): void

本接口用于将传入的data转换成多样式数据结构。若原data使用多个record去承载同一份数据的不同样式，则可以使用此接口将原data转换为多样式数据结构。

当满足以下规则时进行转换，传入的data经转换后变为多样式数据结构：

1. data中的record数量大于1;
2. data中的properties中的tag值为"records\_to\_entries\_data\_format"。

否则不会产生任何行为。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 是 | 目标数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { unifiedDataChannel } from '@kit.ArkData';
2. import { uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let details : Record<string, string> = {
6. 'attr1': 'value1',
7. 'attr2': 'value2'
8. }
9. let plainTextObj : uniformDataStruct.PlainText = {
10. uniformDataType: 'general.plain-text',
11. textContent : 'The weather is very good today',
12. abstract : 'The weather is very good today',
13. details : details
14. }
15. let htmlObj : uniformDataStruct.HTML = {
16. uniformDataType :'general.html',
17. htmlContent : '<div><p>The weather is very good today</p></div>',
18. plainContent : 'The weather is very good today',
19. details : details
20. }
21. let plainText = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainTextObj);
22. let html = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HTML, htmlObj);
23. let unifiedData = new unifiedDataChannel.UnifiedData(plainText);
24. unifiedData.addRecord(html);
25. unifiedData.properties.tag = 'records_to_entries_data_format';

27. try {
28. unifiedDataChannel.convertRecordsToEntries(unifiedData);
29. let records: Array<unifiedDataChannel.UnifiedRecord> = unifiedData.getRecords();
30. console.info(`Records size is ${records.length}`); // After conversion, its length must be less than 1
31. if (records.length == 1) {
32. let plainTextObjRead: uniformDataStruct.PlainText = records[0].getEntry(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT) as uniformDataStruct.PlainText;
33. console.info(`TextContent is ${plainTextObjRead.textContent}`);
34. let htmlObjRead: uniformDataStruct.HTML = records[0].getEntry(uniformTypeDescriptor.UniformDataType.HTML) as uniformDataStruct.HTML;
35. console.info(`HtmlContent is ${htmlObjRead.htmlContent}`);
36. }
37. } catch (e) {
38. let error: BusinessError = e as BusinessError;
39. console.error(`Convert data throws an exception. code is ${error.code}, message is ${error.message} `);
40. }
```
