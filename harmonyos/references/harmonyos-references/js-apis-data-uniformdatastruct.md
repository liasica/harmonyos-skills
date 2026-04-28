---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformdatastruct
title: @ohos.data.uniformDataStruct (标准化数据结构)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.uniformDataStruct (标准化数据结构)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1ef7a9fef8680e6c3c8ad99f0fce765ae632b818c0a49242c3e54ea06002fc2c
---

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了部分标准化数据类型[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)对应的数据结构，方便不同应用间进行数据交互，减少数据类型适配的工作量。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { uniformDataStruct } from '@kit.ArkData';
```

## PlainText

PhonePC/2in1TabletTV

纯文本类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.plain-text' | 是 | 否 | 统一数据类型标识，标识为纯文本类型数据，固定为“general.plain-text”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| textContent | string | 否 | 否 | 纯文本内容。 |
| abstract | string | 否 | 是 | 纯文本摘要，非必填字段，默认值为空字符串。 |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述文本内容详细属性。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象，用于描述一篇文章的详细属性。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let plainTextDetails : Record<string, string> = {
3. 'attr1': 'value1',
4. 'attr2': 'value2'
5. }
6. let plainText : uniformDataStruct.PlainText = {
7. uniformDataType: 'general.plain-text',
8. textContent : 'This is plainText textContent example',
9. abstract : 'this is abstract',
10. details : plainTextDetails
11. }
12. console.info('plainText.uniformDataType: ' + plainText.uniformDataType);
13. if(plainText.details != undefined){
14. let plainTextDetailsObj : Record<string, string> = plainText.details;
15. for(let kv of Object.entries(plainTextDetailsObj)) {
16. console.info('plainText.details.attr: ' + kv[0] + ', value:' + kv[1]);
17. }
18. }
19. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
```

## Hyperlink

PhonePC/2in1TabletTV

超链接类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.hyperlink' | 是 | 否 | 统一数据类型标识为超链接类型数据，固定为“general.hyperlink”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| url | string | 否 | 否 | 链接url。 |
| description | string | 否 | 是 | 链接内容描述，非必填字段，默认值为空字符串。 |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述Hyperlink的详细属性内容。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let hyperlinkDetails : Record<string, string> = {
3. 'attr1': 'value1',
4. 'attr2': 'value2'
5. }
6. let hyperlink : uniformDataStruct.Hyperlink = {
7. uniformDataType:'general.hyperlink',
8. url : 'www.XXX.com',
9. description : 'This is the description of this hyperlink',
10. details : hyperlinkDetails
11. }
12. console.info('hyperlink.uniformDataType: ' + hyperlink.uniformDataType);
13. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
```

## HTML

PhonePC/2in1TabletTV

HTML类型数据，用于描述超文本标记语言数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.html' | 是 | 否 | 统一数据类型标识为html类型数据，固定为“general.html”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| htmlContent | string | 否 | 否 | html格式内容。 |
| plainContent | string | 否 | 是 | 去除html标签后的纯文本内容，非必填字段，默认值为空字符串。 |
| details | Record<string, string> | 否 | 是 | 是一个字典类型对象，key和value都是string类型，用于描述HTML的详细属性内容。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let htmlObjDetails : Record<string, string> = {
3. 'attr1': 'value1',
4. 'attr2': 'value2'
5. }
6. let htmlObj : uniformDataStruct.HTML = {
7. uniformDataType :'general.html',
8. htmlContent : '<div><p>标题</p></div>',
9. plainContent : 'this is plainContent',
10. details : htmlObjDetails
11. }
12. console.info('htmlObj.uniformDataType: ' + htmlObj.uniformDataType);
13. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HTML, htmlObj);
```

## OpenHarmonyAppItem

PhonePC/2in1TabletTV

系统定义的桌面图标类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'openharmony.app-item' | 是 | 否 | 统一数据类型标识为桌面图标类型数据，固定为“openharmony.app-item”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| appId | string | 否 | 否 | 图标对应的应用id。 |
| appName | string | 否 | 否 | 图标对应的应用名。 |
| appIconId | string | 否 | 否 | 图标的图片id。 |
| appLabelId | string | 否 | 否 | 图标名称对应的标签id。 |
| bundleName | string | 否 | 否 | 图标对应的应用bundle名。 |
| abilityName | string | 否 | 否 | 图标对应的应用ability名。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
3. let appItemDetails : Record<string, number | string | Uint8Array> = {
4. 'appItemKey1': 123,
5. 'appItemKey2': 'appItemValue',
6. 'appItemKey3': u8Array
7. }
8. let appItem : uniformDataStruct.OpenHarmonyAppItem = {
9. uniformDataType:'openharmony.app-item',
10. appId : 'MyAppId',
11. appName : 'MyAppName',
12. appIconId : 'MyAppIconId',
13. appLabelId : 'MyAppLabelId',
14. bundleName : 'MyBundleName',
15. abilityName : 'MyAbilityName',
16. details : appItemDetails
17. }
18. console.info('appItem.uniformDataType: ' + appItem.uniformDataType);
19. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_APP_ITEM, appItem);
```

## ContentForm14+

PhonePC/2in1TabletTV

内容卡片类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.content-form' | 是 | 否 | 统一数据类型标识为内容卡片类型数据，固定为“general.content-form”。 |
| title | string | 否 | 否 | 内容卡片的标题。 |
| thumbData | Uint8Array | 否 | 是 | 内容卡片对应的图片数据。 |
| description | string | 否 | 是 | 内容卡片中的描述信息。 |
| appIcon | Uint8Array | 否 | 是 | 内容卡片中的应用图标数据。 |
| appName | string | 否 | 是 | 内容卡片中应用的应用名。 |
| linkUri | string | 否 | 是 | 内容卡片对应的跳转超链接。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let thumbDataU8Array = new Uint8Array([1, 2, 3, 4, 5]);
3. let appIconU8Array = new Uint8Array([6, 7, 8, 9, 10]);
4. let contentForm : uniformDataStruct.ContentForm = {
5. uniformDataType : 'general.content-form',
6. title : 'MyTitle',
7. thumbData : thumbDataU8Array,
8. description : 'MyDescription',
9. appName : 'MyAppName',
10. linkUri : 'MyLinkUri',
11. appIcon : appIconU8Array
12. }
13. console.info('contentForm.uniformDataType: ' + contentForm.uniformDataType);
14. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.CONTENT_FORM, contentForm);
```

## Form15+

PhonePC/2in1TabletTV

系统定义的卡片类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'openharmony.form' | 是 | 否 | 统一数据类型标识为卡片类型数据，固定为“openharmony.form”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| formId | number | 否 | 否 | 卡片id。 |
| formName | string | 否 | 否 | 卡片名。 |
| bundleName | string | 否 | 否 | 卡片所属的bundle名。 |
| abilityName | string | 否 | 否 | 卡片对应的ability名。 |
| module | string | 否 | 否 | 卡片所属的module名。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
3. let formDetails : Record<string, number | string | Uint8Array> = {
4. 'formKey1': 123,
5. 'formKey2': 'formValue',
6. 'formKey3': u8Array
7. }
8. let form : uniformDataStruct.Form = {
9. uniformDataType : 'openharmony.form',
10. formId : 1,
11. formName : 'formName',
12. bundleName : 'com.xx.app',
13. abilityName : 'abilityName',
14. module : 'module',
15. details : formDetails
16. }
17. console.info('form.uniformDataType: ' + form.uniformDataType);
18. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
```

## FileUri15+

PhonePC/2in1TabletTV

文件地址类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.file-uri' | 是 | 否 | 统一数据类型标识为文件地址类型数据，固定为“general.file-uri”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| oriUri | string | 否 | 否 | 文件路径。 |
| fileType | string | 否 | 否 | 文件类型（必须是UTD类型，详情参考[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)）。fileType最大长度限制为1024个字节。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
3. let fileUriDetails : Record<string, number | string | Uint8Array> = {
4. 'fileUriKey1': 123,
5. 'fileUriKey2': 'fileUriValue',
6. 'fileUriKey3': u8Array
7. }
8. let fileUri : uniformDataStruct.FileUri = {
9. uniformDataType : 'general.file-uri',
10. oriUri : 'www.xx.com',
11. fileType : 'general.image',
12. details : fileUriDetails
13. }
14. console.info('fileUri.uniformDataType: ' + fileUri.uniformDataType);
15. // 当使用FileUri类型的标准化数据结构构造record时，推荐入参中的type值设为uniformTypeDescriptor.UniformDataType.FILE_URI
16. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
```

## PixelMap15+

PhonePC/2in1TabletTV

系统定义的像素图类型数据。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'openharmony.pixel-map' | 是 | 否 | 统一数据类型标识为像素图类型数据，固定为“openharmony.pixel-map”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| pixelMap | image.PixelMap | 否 | 否 | 像素图二进制数据。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```
1. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
2. import { image } from '@kit.ImageKit';

4. let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
5. let arrayBuffer = new ArrayBuffer(4*200*200);
6. let opt : image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 }, alphaType: 3 };
7. let pixelMapDetails : Record<string, number | string | Uint8Array> = {
8. 'pixelMapKey1': 123,
9. 'pixelMapKey2': 'pixelMapValue',
10. 'pixelMapKey3': u8Array
11. }
12. let pixelMap : uniformDataStruct.PixelMap = {
13. uniformDataType : 'openharmony.pixel-map',
14. pixelMap : image.createPixelMapSync(arrayBuffer, opt),
15. details : pixelMapDetails
16. }
17. console.info('pixelMap.uniformDataType: ' + pixelMap.uniformDataType);
18. let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```
