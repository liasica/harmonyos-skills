---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformdatastruct
title: "@ohos.data.uniformDataStruct (标准化数据结构)"
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.uniformDataStruct (标准化数据结构)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:908ca68522cdb935b9e86fa6c07253d26dff237a07b95e32de5b2788c98893de
---

本模块为统一数据管理框架（Unified Data Management Framework，UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景提供了部分标准化数据类型[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)对应的数据结构，方便不同应用间进行数据交互，减少数据类型适配的工作量。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```js
import { uniformDataStruct } from '@kit.ArkData';
```

## PlainText

纯文本类型数据，用于描述和管理纯文本内容。创建PlainText对象后，可用于拖拽、复制粘贴等数据共享场景，实现跨应用的纯文本数据交互。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.plain-text' | 是 | 否 | 统一数据类型标识为纯文本类型数据，固定为“general.plain-text”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| textContent | string | 否 | 否 | 纯文本内容。长度限制为20MB。 |
| abstract | string | 否 | 是 | 纯文本摘要，非必填字段。当需要为文本提供简短摘要时传入此参数（如用于预览、搜索结果展示等场景），不传入时默认值为空字符串，不提供摘要信息。 |
| details | Record<string, string> | 否 | 是 | 字典类型对象，key和value均为string类型，用于描述文本内容详细属性。非必填字段，默认值为空字典对象。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象。当需要存储额外的文本属性信息时传入此参数，不传入时默认值为空字典对象，不提供额外属性。 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let plainTextDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let plainText: uniformDataStruct.PlainText = {
  uniformDataType: 'general.plain-text',
  textContent: 'This is plainText textContent example',
  abstract: 'this is abstract',
  details: plainTextDetails
};
console.info('plainText.uniformDataType: ' + plainText.uniformDataType);
if (plainText.details != undefined) {
  let plainTextDetailsObj: Record<string, string> = plainText.details;
  for (let kv of Object.entries(plainTextDetailsObj)) {
    console.info('plainText.details.attr: ' + kv[0] + ', value:' + kv[1]);
  }
}
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN_TEXT, plainText);
```

## Hyperlink

超链接类型数据，用于描述和管理超链接信息。创建Hyperlink对象后，可用于拖拽、分享等场景，实现跨应用的超链接数据传递和跳转。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.hyperlink' | 是 | 否 | 统一数据类型标识为超链接类型数据，固定为“general.hyperlink”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| url | string | 否 | 否 | 链接URL地址，支持http、https等协议，需符合标准URL格式。例如：https://www.example.com或file:///path/to/file。 |
| description | string | 否 | 是 | 链接内容描述，非必填字段。当需要为超链接提供文字描述时传入此参数（如用于可访问性、链接预览等场景），不传入时默认值为空字符串，不提供描述信息。 |
| details | Record<string, string> | 否 | 是 | 字典类型对象，key和value均为string类型，用于描述Hyperlink的详细属性内容。非必填字段，默认值为空字典对象。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象。当需要存储额外的超链接属性信息时传入此参数，不传入时默认值为空字典对象，不提供额外属性。 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let hyperlinkDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let hyperlink: uniformDataStruct.Hyperlink = {
  uniformDataType: 'general.hyperlink',
  url: 'www.XXX.com',
  description: 'This is the description of this hyperlink',
  details: hyperlinkDetails
};
console.info('hyperlink.uniformDataType: ' + hyperlink.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HYPERLINK, hyperlink);
```

## HTML

HTML类型数据，用于描述超文本标记语言数据。创建HTML对象后，可在拖拽、复制粘贴等场景中传递富文本内容，支持跨应用的HTML格式数据交互，并可通过uriAuthorizationPolicies控制URI授权策略。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.html' | 是 | 否 | 统一数据类型标识为html类型数据，固定为“general.html”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| htmlContent | string | 否 | 否 | HTML格式的内容文本，支持标准HTML标签。可以是完整的HTML文档或HTML片段。长度限制为20MB。建议使用UTF-8编码。例如：<div><p>标题</p></div>。 |
| plainContent | string | 否 | 是 | 去除HTML标签后的纯文本内容，非必填字段。当需要提供HTML内容的纯文本版本时传入此参数（如用于文本搜索、无HTML渲染环境的展示等场景），不传入时默认值为空字符串，不提供纯文本版本。 |
| details | Record<string, string> | 否 | 是 | 字典类型对象，key和value均为string类型，用于描述HTML的详细属性内容。非必填字段，默认值为空字典对象。例如，可生成一个details内容为  {  "title":"标题",  "content":"内容"  }  的数据对象。 |
| uriAuthorizationPolicies | Array<number> | 否 | 是 | 用于拖拽场景的URI授权策略。默认值为READ（仅读授权），仅在img标签等场景下生效。只针对单个record使用，优先级最高，具体策略见[UriPermission](js-apis-data-unifieddatachannel.md#uripermission)。  **起始版本**：26.0.0 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let htmlObjDetails: Record<string, string> = {
  'attr1': 'value1',
  'attr2': 'value2'
};
let htmlObj: uniformDataStruct.HTML = {
  uniformDataType: 'general.html',
  htmlContent: '<div><p>标题</p></div>',
  plainContent: 'this is plainContent',
  details: htmlObjDetails,
  // 从API 26.0.0版本开始，支持uri授权策略
  uriAuthorizationPolicies: [
    unifiedDataChannel.UriPermission.WRITE
  ]
};
console.info('htmlObj.uniformDataType: ' + htmlObj.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.HTML, htmlObj);
```

## OpenHarmonyAppItem

系统定义的桌面图标类型数据，用于跨应用共享桌面图标信息。典型使用场景包括：桌面启动器拖拽图标、应用商店分享应用图标或创建快捷方式等。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'openharmony.app-item' | 是 | 否 | 统一数据类型标识为桌面图标类型数据，固定为“openharmony.app-item”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| appId | string | 否 | 否 | 图标对应的应用id。 |
| appName | string | 否 | 否 | 图标对应的应用名。 |
| appIconId | string | 否 | 否 | 图标的图片id。 |
| appLabelId | string | 否 | 否 | 图标名称对应的标签id。 |
| bundleName | string | 否 | 否 | 图标对应的应用bundle名，格式需符合应用包名规范。 |
| abilityName | string | 否 | 否 | 图标对应的应用ability名。建议遵循Ability组件命名规范：取值为长度不超过127字节的字符串，以字母开头，可包含字母、数字、下划线（\_）或点号（.）；确保该名称在整个应用中唯一。推荐使用"包名.Ability名"格式（如"com.example.myapplication.MainAbility"）。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 字典类型对象，key为string类型，value可包含number（数值类型）、string（字符串类型）或Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let appItemDetails: Record<string, number | string | Uint8Array> = {
  'appItemKey1': 123,
  'appItemKey2': 'appItemValue',
  'appItemKey3': u8Array
};
let appItem: uniformDataStruct.OpenHarmonyAppItem = {
  uniformDataType: 'openharmony.app-item',
  appId: 'MyAppId',
  appName: 'MyAppName',
  appIconId: 'MyAppIconId',
  appLabelId: 'MyAppLabelId',
  bundleName: 'MyBundleName',
  abilityName: 'MyAbilityName',
  details: appItemDetails
};
console.info('appItem.uniformDataType: ' + appItem.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_APP_ITEM, appItem);
```

## ContentForm14+

内容卡片类型数据，用于跨应用共享内容卡片信息。典型使用场景包括：资讯应用分享文章卡片、电商应用分享商品卡片、社交应用分享内容预览等。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.content-form' | 是 | 否 | 统一数据类型标识为内容卡片类型数据，固定为“general.content-form”。 |
| title | string | 否 | 否 | 内容卡片的标题。 |
| thumbData | Uint8Array | 否 | 是 | 内容卡片对应的图片数据。默认值为空。 |
| description | string | 否 | 是 | 内容卡片中的描述信息。默认值为空字符串。 |
| appIcon | Uint8Array | 否 | 是 | 内容卡片中的应用图标数据。默认值为空。 |
| appName | string | 否 | 是 | 内容卡片中应用的应用名。默认值为空字符串。 |
| linkUri | string | 否 | 是 | 内容卡片对应的跳转超链接，需符合URI格式规范。默认值为空字符串。 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let thumbDataU8Array = new Uint8Array([1, 2, 3, 4, 5]);
let appIconU8Array = new Uint8Array([6, 7, 8, 9, 10]);
let contentForm: uniformDataStruct.ContentForm = {
  uniformDataType: 'general.content-form',
  title: 'MyTitle',
  thumbData: thumbDataU8Array,
  description: 'MyDescription',
  appName: 'MyAppName',
  linkUri: 'MyLinkUri',
  appIcon: appIconU8Array
};
console.info('contentForm.uniformDataType: ' + contentForm.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.CONTENT_FORM, contentForm);
```

## Form15+

系统定义的卡片类型数据，用于跨应用共享卡片信息。典型使用场景包括：卡片拖拽分享、卡片内容跨应用传输、桌面小组件数据共享等。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'openharmony.form' | 是 | 否 | 统一数据类型标识为卡片类型数据，固定为“openharmony.form”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| formId | number | 否 | 否 | 卡片id。 |
| formName | string | 否 | 否 | 卡片名。 |
| bundleName | string | 否 | 否 | 卡片所属的bundle名，格式需符合应用包名规范。 |
| abilityName | string | 否 | 否 | 卡片对应的ability名。建议遵循Ability组件命名规范：取值为长度不超过127字节的字符串，以字母开头，可包含字母、数字、下划线（\_）或点号（.）；确保该名称在整个应用中唯一。推荐使用"包名.Ability名"格式（如"com.example.myapplication.MainAbility"）。 |
| module | string | 否 | 否 | 卡片所属的module名。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 字典类型对象，key为string类型，value可包含number（数值类型）、string（字符串类型）或Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let formDetails: Record<string, number | string | Uint8Array> = {
  'formKey1': 123,
  'formKey2': 'formValue',
  'formKey3': u8Array
};
let form: uniformDataStruct.Form = {
  uniformDataType: 'openharmony.form',
  formId: 1,
  formName: 'formName',
  bundleName: 'com.xx.app',
  abilityName: 'abilityName',
  module: 'module',
  details: formDetails
};
console.info('form.uniformDataType: ' + form.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_FORM, form);
```

## FileUri15+

文件地址类型数据，用于描述文件的URI地址信息。创建FileUri对象后，可用于文件拖拽、文件共享等场景，支持通过uriAuthorizationPolicies控制文件访问权限，实现跨应用的文件数据传递和权限管理。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'general.file-uri' | 是 | 否 | 统一数据类型标识为文件地址类型数据，固定为“general.file-uri”，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| oriUri | string | 否 | 否 | 文件的原始URI路径。支持本地文件绝对路径、file://协议和http/https网络URL格式。长度限制为4096字节。例如：/data/local/tmp/test.txt、file:///data/local/tmp/test.txt或http://example.com/file.txt。 |
| fileType | string | 否 | 否 | 文件类型必须是标准化数据类型（即[UTD预置列表](../harmonyos-guides/uniform-data-type-list.md)中各类型对应的UTD-ID或自定义UTD-ID）。fileType最大长度限制为1024个字节，超出限制时抛出异常。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 字典类型对象，key为string类型，value可包含number（数值类型）、string（字符串类型）或Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |
| uriAuthorizationPolicies | Array<number> | 否 | 是 | 用于拖拽场景的URI授权策略。默认值为READ+WRITE+PERSIST（读+写+持久化授权）。只针对单个record使用，优先级最高，具体策略见[UriPermission](js-apis-data-unifieddatachannel.md#uripermission)。  **起始版本**：26.0.0 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let fileUriDetails: Record<string, number | string | Uint8Array> = {
  'fileUriKey1': 123,
  'fileUriKey2': 'fileUriValue',
  'fileUriKey3': u8Array
};
let fileUri: uniformDataStruct.FileUri = {
  uniformDataType: 'general.file-uri',
  oriUri: 'www.xx.com',
  fileType: 'general.image',
  details: fileUriDetails,
  // 从API 26.0.0版本开始，支持uri授权策略
  uriAuthorizationPolicies: [
    unifiedDataChannel.UriPermission.WRITE
  ]
};
console.info('fileUri.uniformDataType: ' + fileUri.uniformDataType);
// 当使用FileUri类型的标准化数据结构构造record时，推荐入参中的type值设为uniformTypeDescriptor.UniformDataType.FILE_URI
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.FILE_URI, fileUri);
```

## PixelMap15+

系统定义的像素图类型数据，用于描述图像像素数据。创建PixelMap对象后，可用于图像拖拽、图像共享等场景，实现跨应用的图像数据传递。

**系统能力**：SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniformDataType | 'openharmony.pixel-map' | 是 | 否 | 统一数据类型标识为像素图类型数据，固定为"openharmony.pixel-map"，数据类型描述信息见[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 像素图对象。 |
| details | Record<string, number | string | Uint8Array> | 否 | 是 | 字典类型对象，key为string类型，value可包含number（数值类型）、string（字符串类型）或Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。 |

**示例：**

```ts
import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';
import { image } from '@kit.ImageKit';

let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
let arrayBuffer = new ArrayBuffer(4 * 200 * 200);
let opt: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: { height: 200, width: 200 },
  alphaType: 3
};
let pixelMapDetails: Record<string, number | string | Uint8Array> = {
  'pixelMapKey1': 123,
  'pixelMapKey2': 'pixelMapValue',
  'pixelMapKey3': u8Array
};
let pixelMap: uniformDataStruct.PixelMap = {
  uniformDataType: 'openharmony.pixel-map',
  pixelMap: image.createPixelMapSync(arrayBuffer, opt),
  details: pixelMapDetails
};
console.info('pixelMap.uniformDataType: ' + pixelMap.uniformDataType);
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP, pixelMap);
```
