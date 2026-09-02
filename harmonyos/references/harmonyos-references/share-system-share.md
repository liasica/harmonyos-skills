---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/share-system-share
title: systemShare（分享）
breadcrumb: API参考 > 应用服务 > Share Kit（分享服务） > ArkTS API > systemShare（分享）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf16c62f7a8a1e4856eb14432e0e566542ee4cf064b21156f1ff30c67175b54e
---

本模块提供分享数据创建及分享面板拉起的功能，提供多种系统标准分享服务，例如分享数据给其他应用、复制、打印等。

* 分享接入应用需要配置、呈现和关闭分享面板。
* 分享面板的配置包括数据对象、呈现视图的方式、预览模式等。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { systemShare } from '@kit.ShareKit';
```

## SharedRecord

用于构造一条分享数据记录。包含数据类型、数据内容及描述等信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| utd | string | 否 | 否 | 统一数据类型，参考[@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)](js-apis-data-uniformtypedescriptor.md)  建议开发者传入精准的数据类型，有助于匹配到精确的目标应用，参见：[Share Kit体验规范](../harmonyos-guides/share-access-utd.md) 。 |
| title | string | 否 | 是 | 如果是文本、链接等内容，建议填入title标识其标题。缺省时，若分享内容为文本类型，则文本内容作为title字段；若分享内容为文件类型，则文件名作为title字段。 |
| label | string | 否 | 是 | 标识当前数据记录类型的标签，在单选模式时生效。缺省为[UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype)类型相应的标签。具体如下：HYPERLINK显示为链接；HTML显示为网页；TEXT显示为文本；VIDEO显示为视频；AUDIO显示为音乐；IMAGE显示为图片；FILE显示为文件。 |
| description | string | 否 | 是 | 数据记录的描述。缺省为空字符串。 |
| thumbnail | Uint8Array | 否 | 是 | 数据记录缩略图。缺省时使用与分享内容类型匹配的图标作为缩略图。  建议开发者传入符合数据记录的缩略图，如无，可传入应用图标。  **说明：** 限制图片大小：32KB以下。过大的图片可能导致want数据超限无法拉起分享，可使用[ImagePacker.packToData](arkts-apis-image-imagepacker.md#packtodata13)压缩图片质量。 |
| thumbnailUri | string | 否 | 是 | 数据记录缩略图的uri。缺省时使用与分享内容类型匹配的图标作为缩略图。支持的uri类型：  应用文件URI，参见：[应用文件分享](../harmonyos-guides/share-app-file.md)  用户文件URI，参见：[用户文件URI介绍](../harmonyos-guides/user-file-uri-intro.md)  **起始版本：** 5.0.0(12)。  **说明：** 与thumbnail字段同时存在时，优先使用thumbnail字段。 |
| uri | string | 否 | 是 | 数据记录的uri。支持的uri类型：  应用文件URI，参见：[应用文件分享](../harmonyos-guides/share-app-file.md)  用户文件URI，参见：[用户文件URI介绍](../harmonyos-guides/user-file-uri-intro.md)  **说明：** 沙箱路径可通过[fileUri.getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)方法获取文件URI。content和uri二者至少有一个不为空，否则会导致分享失败。 |
| content | string | 否 | 是 | 数据记录内容。链接（包含App Linking）、文本类型的内容通过该字段传递。  **说明：** content和uri二者至少有一个不为空，否则会导致分享失败。 |
| extraData | Record<string, string | number | boolean | Array<string | number | boolean>> | 否 | 是 | 扩展数据，用于向目标应用/设备分享自定义的扩展内容。 |
| revisitShareRecordData | [RevisitShareRecordData](share-system-share.md#revisitsharerecorddata) | 否 | 是 | 通过该字段生成二维码复访分享图。支持类型见[RevisitShareRecordType](share-system-share.md#revisitsharerecordtype)。  **起始版本：** 6.1.0(23)。 |

## ShareControllerOptions

分享控制器配置项。用于配置分享预览模式，选择模式等，决定了分享面板的显示样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**需要权限：** 如需使用appLaunchTrustInfo字段时，需申请权限ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST，该能力受限开放，仅支持企业应用限制内部数据分享到企业集团信任的应用。权限申请方式请参考[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| anchor | [ShareControllerAnchor](share-system-share.md#sharecontrolleranchor) | string | 否 | 是 | 类型为string时，表示分享面板关联的控件ID（[ArkUI组件常规属性的id值](js-components-common-attributes.md#常规属性)）。  类型为ShareControllerAnchor时，表示锚点位置。  不传此参数时，面板会显示在默认位置（居中）。 |
| previewMode | [SharePreviewMode](share-system-share.md#sharepreviewmode) | 否 | 是 | 预览的模式，缺省为卡片模式。 |
| selectionMode | [SelectionMode](share-system-share.md#selectionmode) | 否 | 是 | 选择的模式，缺省为单选模式。 |
| excludedAbilities | Array<[ShareAbilityType](share-system-share.md#shareabilitytype)> | 否 | 是 | 操作区不需要显示的能力列表。  **起始版本：** 5.0.0(12)。 |
| appLaunchTrustInfo | Array<string> | 否 | 是 | 通过配置[应用唯一标识符](js-apis-bundlemanager-bundleinfo.md#signatureinfo)（appIdentifier字段）列表，指定可分享的目标应用名单，系统仅读取前50个配置项，超出部分将不生效。调用此功能需申请ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST权限。该能力属于受限开放范围，仅限企业应用用于限制内部数据分享至集团信任的应用列表。  **起始版本：** 6.0.1(21)。 |

## ShareControllerAnchor

分享悬浮窗视图依附锚点，分享面板会根据屏幕大小选择是否在指定的位置显示悬浮窗。

**说明** 

设备屏幕宽度较小时，不会以悬浮形态展示，而是以模态形式/弹窗形式显示。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowOffset | [Offset](share-system-share.md#offset) | 否 | 否 | 表示共享控制器的窗口偏移量，推荐设置组件左上角顶点的坐标。 |
| size | [Size](share-system-share.md#size) | 否 | 是 | 锚点矩形的尺寸，缺省时，锚点是一个点，即宽高都为0。 |

## Offset

可以设置的相对锚点的窗口偏移值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | x点的坐标。单位：像素。 |
| y | number | 否 | 否 | y点的坐标。单位：像素。 |

## Size

锚点矩形的尺寸，缺省时，锚点是一个点，即宽高都为0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 组件宽度，单位：像素。负数按0处理。 |
| height | number | 否 | 否 | 组件高度，单位：像素。负数按0处理。 |

## ShareOperationResult

shareCompleted事件的返回值，用于获知用户分享渠道信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| targetAbilityInfo | [ShareAbilityInfo](share-system-share.md#shareabilityinfo) | 否 | 否 | 用户分享渠道的信息。 |

## ShareAbilityInfo

用户分享渠道的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 分享渠道的名称。  - 系统操作有固定名称。请参见：[ShareAbilityName](share-system-share.md#shareabilityname)枚举值。  - 非系统操作采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。 |

## ContactInfo

意图框架推荐联系人的信息。当分享到推荐联系人时，携带此参数用于区分。

数据捐献参考：[共享联系人信息到分享推荐区](../harmonyos-guides/share-intents-share.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| contactType | string | 否 | 否 | 联系人类型：取值来源应用向意图捐赠数据中的entityName字段，例如"Contact"、"ChatGroup"。 |
| contactId | string | 否 | 否 | 联系人ID：取值来源应用向意图捐赠数据中的entityId字段。 |

## RevisitShareRecordData

复访分享数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| revisitShareRecordType | [RevisitShareRecordType](share-system-share.md#revisitsharerecordtype) | 否 | 否 | 复访分享数据类型。 |
| generatedImageUri | string | 否 | 否 | 生成的分享图uri路径 (应用文件URI)，用于写入绘图结果或预览。开发者需要在该路径下创建一个空的图片文件，支持的图片文件类型包括PNG、JPG。  应用文件URI，参见：[应用文件分享](../harmonyos-guides/share-app-file.md)  **说明：** 沙箱路径可通过[fileUri.getUriFromPath](js-apis-file-fileuri.md#fileurigeturifrompath)方法获取文件URI。 |

## ReadingExtendedShareRecordData

阅读分享拓展数据记录，ReadingExtendedShareRecordData继承自RevisitShareRecordData。

当utd为utd.UniformDataType.TEXT, 且revisitShareRecordType为RevisitShareRecordType.READING\_SHARE条件下生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 6.1.0(23)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sourceTitle | string | 否 | 否 | 来源标题（原文章/书名），用于生成共享镜像的标题。  长度限制：  当readingShareStyle为STYLE\_HIGHLIGHT\_CONTENT时，最大显示行数为2行。默认字号为16vp，超出部分显示省略号（...）  当readingShareStyle为STYLE\_HIGHLIGHT\_TITLE时，最大显示行数为2行。默认字号为24vp，若空间不足，则按阶梯逐级缩小至18vp。若在18vp字号下仍无法完全显示，则对末尾超出部分进行省略号（...）。 |
| appLink | string | 否 | 否 | 文章appLink（https链接格式）。  当ReadingExtendedData不为空时，此值必填。  长度限制：appLink与appLinkExtraInfo拼接后的总长度不得超过512个字符。 |
| readingShareStyle | [ReadingShareRecordStyle](share-system-share.md#readingsharerecordstyle) | 否 | 是 | 阅读分享模版数据类型， 默认STYLE\_HIGHLIGHT\_CONTENT。 |
| subtitle | string | 否 | 是 | 副标题（如：书籍章节信息、段落信息）。readingShareStyle为STYLE\_HIGHLIGHT\_TITLE生效。  长度限制：单行显示，超出部分显示省略号（...）。 |
| appLinkExtraInfo | string | 否 | 是 | appLink补充信息，拼接到appLink后参与二维码生成。  web文本选中分享场景，建议携带textFragement信息(#:~:text=[prefix-,]textStart[,textEnd][,-suffix])，以便支持高亮突出显示；  其他场景，应用可携带自定义参数，用于应用直达后的内部逻辑处理。 |
| coverImageUri | string | 否 | 是 | 封面图uri路径（应用文件URI）（如：书籍封面图路径）。readingShareStyle为STYLE\_HIGHLIGHT\_TITLE生效。  应用文件URI，参见：[应用文件分享](../harmonyos-guides/share-app-file.md)。 |
| prefixText | string | 否 | 是 | 所选文本的前缀文本。  长度限制：最大显示行数为1行，超出时使用前置省略。 |
| suffixText | string | 否 | 是 | 所选文本的后缀文本。  长度限制：最大显示行数为2行，超出时使用后置省略。 |
| author | string | 否 | 是 | 文章作者的姓名，用于生成作者分享的图片中显示的信息。  长度限制：最大显示行数为1行，超出部分显示省略号（...）。 |
| publishDate | Date | 否 | 是 | 文章发表日期。readingShareStyle为STYLE\_HIGHLIGHT\_CONTENT生效。 |
| sharerName | string | 否 | 是 | 分享者名字。  长度限制：最大显示行数为1行，超出部分显示省略号（...）。 |
| appSlogan | string | 否 | 是 | 应用的口号。  长度限制：最大显示行数为1行。超出部分显示省略号（...）。 |

## SharePreviewMode

分享预览模式。图片、视频等格式推荐使用详细预览图模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认模式（缩略图卡片）。推荐文本、链接等数据使用此模式。 |
| DETAIL | 1 | 详细预览图模式。推荐图片、视频等数据使用此模式。 |

## SelectionMode

分享面板选择模式。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SINGLE | 0 | 单选模式，当传入多条分享数据记录（SharedRecord）时，需要用户多选一进行分享。 |
| BATCH | 1 | 批量模式，分享全部数据记录。 |

## ShareAbilityType

系统能力类型定义。用于排除操作区的系统能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COPY\_TO\_PASTEBOARD | 0 | 复制 |
| SAVE\_TO\_MEDIA\_ASSET | 1 | 保存至图库 |
| SAVE\_AS\_FILE | 2 | 另存为 |
| PRINT | 3 | 打印 |
| SAVE\_TO\_SUPERHUB | 4 | 添加至中转站 |

## ShareAbilityResultCode

从UIExtensionAbility返回的Code值。可控制分享面板的行为。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR | -1 | 发生错误。如果同时传递message参数，将弹出toast提示。 |
| BACK | 0 | 用户点击返回按钮。返回分享面板。 |
| CLOSE | 1 | 用户点击关闭按钮。关闭分享面板。 |

## ShareAbilityName

系统操作的名称，用于返回分享结果数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COPY\_TO\_PASTEBOARD | 'SystemShare\_CopyToPasteboard' | 复制 |
| SAVE\_TO\_MEDIA\_ASSET | 'SystemShare\_SaveToMediaAsset' | 保存至图库 |
| SAVE\_AS\_FILE | 'SystemShare\_SaveAsFile' | 另存为 |
| PRINT | 'SystemShare\_Print' | 打印 |
| SAVE\_TO\_SUPERHUB | 'SystemShare\_Superhub' | 添加至中转站 |
| COLLECTION | 'SystemShare\_Collection' | 小艺知识空间 |
| HARMONYSHARE | 'SystemShare\_HarmonyShare' | 华为分享 |
| ENCRYPT | 'SystemShare\_Encrypt' | 加密分享 |

## RevisitShareRecordType

定义复访分享的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READING\_SHARE | 1 | 阅读分享数据类型。 |

## ReadingShareRecordStyle

阅读分享场景显示模版类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE\_HIGHLIGHT\_CONTENT | 0 | 选定文本高亮显示，默认。 |
| STYLE\_HIGHLIGHT\_TITLE | 1 | 标题突出显示。 |

## SharedData

表示分享数据对象，提供封装一组数据记录的方法。

一个分享数据对象至少存在一条记录，开发者需要在SharedData实例化过程中，通过构造器第一个参数传入；当分享数据包含多条数据记录时，则需要使用addRecord(record: SharedRecord)方法追加记录。

**说明** 

数据记录当前最大可支持500条，且需同时满足数据总大小不超过[IPC](../harmonyos-guides/ipc-rpc-overview.md#基本概念)传输上限200KB。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

### constructor

constructor(record: SharedRecord)

用于构造分享数据对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | [SharedRecord](share-system-share.md#sharedrecord) | 是 | 分享数据记录对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});
```

### addRecord

addRecord(record: SharedRecord): void

在当前分享数据中添加一条分享数据记录。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| record | [SharedRecord](share-system-share.md#sharedrecord) | 是 | 要添加到分享数据对象中的数据记录，该记录为SharedRecord对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[分享服务错误码](share-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1003700001](share-error-code.md#section1003700001-数据记录超过上限) | The number of records exceeds the maximum. |

**示例：**

```typescript
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.IMAGE,
  // ...
  title: 'Picture Title',
  description: 'Picture Description',
  label: 'Poster'
});

try {
  shareData.addRecord({
    utd: utd.UniformDataType.HYPERLINK,
    content: 'https://www.vmall.com/index.html?cid=128688',
    title: 'Huawei Vmall',
    description: 'Phone',
    label: 'Huawei Vmall',
    // ...
  });
} catch (error) {
  hilog.error(DOMAIN, 'testTag', `addRecord error. Code: ${error?.code}, message: ${error?.message}`);
}
```

### getRecords

getRecords(): Array<SharedRecord>

获取当前分享数据中的所有数据记录。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SharedRecord](share-system-share.md#sharedrecord)> | 当前分享数据对象内所包含的记录。 |

**示例：**

```typescript
aboutToAppear(): void {
  systemShare.getSharedData(this.want).then((data: systemShare.SharedData) => {
    let records: systemShare.SharedRecord[] = data.getRecords();
    records.forEach(async (record: systemShare.SharedRecord) => {
      // ...
    });
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, 'testTag', `getSharedData error. Code: ${error?.code}, message: ${error?.message}`);
  });
}
```

## ShareController

分享面板在不同设备下有不同的展示形式，根据屏幕规格&参数为应用提供不同的预览形式以及分享方式。

* 例如手机和TV设备中，分享以模态显示；横屏/折叠屏展开状态时，分享面板以对话框形式显示；
* 而PC/2in1设备及Tablet，需要传入锚点信息并且以悬浮窗（Popup）形式显示。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

### constructor

constructor(data: SharedData)

用于创建分享面板的控制器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [SharedData](share-system-share.md#shareddata) | 是 | 分享数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.HYPERLINK,
  content: 'https://www.vmall.com/index.html?cid=128688',
  title: 'Huawei Vmall',
  description: 'Phone',
});

let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
```

### show

show(context: common.UIAbilityContext, options: ShareControllerOptions): Promise<void>

显示分享面板，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 拉起分享面板的上下文对象。 |
| options | [ShareControllerOptions](share-system-share.md#sharecontrolleroptions) | 是 | 分享控制器配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[分享服务错误码](share-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1003702001](share-error-code.md#section1003702001-数据记录格式非法类型不支持) | Record types are not support. (The batch and multiple selection modes support { @link UDMF.File } type records only.) |
| [1003702002](share-error-code.md#section1003702002-跨进程传输数据量超过上限) | IPC data is oversized. |

**示例：**

```typescript
@Component
export default struct LinkScenario {

  private async share() {
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.HYPERLINK,
      content: 'https://www.vmall.com/index.html?cid=128688',
      title: 'Huawei Vmall',
      description: 'Phone',
    });

    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    const uiContext: UIContext = this.getUIContext();
    const context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    controller.show(context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DEFAULT,
    }).then(() => {
      hilog.info(DOMAIN, 'testTag', 'ShareController show success.');
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, 'testTag', `ShareController show error. code: ${error?.code}, message: ${error?.message}`);
    });
  }
  // ...
}
```

### on('dismiss')

on(event: 'dismiss', callback: () => void): void

注册分享面板关闭事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件为'dismiss'，当分享面板关闭时，触发该事件。 |
| callback | () => void | 是 | 事件回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
private async handelShareDismiss(): Promise<void> {
  const uiContext: UIContext = this.getUIContext();
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: 'Hello HarmonyOS',
  });
  let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
  const context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
  const callback = () => {
    try {
      hilog.info(DOMAIN, 'testTag', 'HuaweiShare_ dismiss invoked.');
      uiContext.getPromptAction().showToast({ message: 'dismiss' });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  };
  controller.on('dismiss', callback);

  controller.show(context, {
    previewMode: systemShare.SharePreviewMode.DEFAULT,
    selectionMode: systemShare.SelectionMode.SINGLE,
  }).then(() => {
    hilog.info(DOMAIN, 'testTag', 'HuaweiShare_ show');
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, 'testTag', `HuaweiShare_ show error. Code: ${error?.code}, message: ${error?.message}`);
  });
}
```

### off('dismiss')

off(event: 'dismiss', callback: () => void): void

取消分享面板关闭事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件回调类型，支持的事件为'dismiss'，取消触发该事件。 |
| callback | () => void | 是 | 回调函数。传入on中的callback取消对应的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
private async handelShareDisableDismiss(): Promise<void> {
  const uiContext: UIContext = this.getUIContext();
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: 'Hello HarmonyOS',
  });
  let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
  const context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
  const callback = () => {
    try {
      hilog.info(DOMAIN, 'testTag', 'HuaweiShare_ dismiss invoked.');
      uiContext.getPromptAction().showToast({ message: 'dismiss' });
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', `showToast error. Code: ${error?.code}, message: ${error?.message}`);
    }
  };
  controller.on('dismiss', callback);
  controller.off('dismiss', callback);
}
```

### on('shareCompleted')

on(type: 'shareCompleted', callback: Callback<ShareOperationResult>): void

注册用户完成分享事件监听。返回用户分享渠道，可用于数据统计等。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'shareCompleted'，当用户完成分享时，触发该事件。 |
| callback | Callback<[ShareOperationResult](share-system-share.md#shareoperationresult)> | 是 | 事件回调，可通过回调参数获取分享渠道。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
private async handelShareCompleted(): Promise<void> {
  const uiContext: UIContext = this.getUIContext();
  const contextFaker: Context = uiContext.getHostContext() as Context;
  let filePath = contextFaker.filesDir + '/exampleImage.jpg';
  let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utdTypeId,
    uri: fileUri.getUriFromPath(filePath),
    title: 'Picture Title',
    description: 'Picture Description',
  });
  let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
  const context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
  const callback = (result: systemShare.ShareOperationResult) => {
    hilog.info(DOMAIN, 'testTag', `HuaweiShare_ shareCompleted invoked. result: ${result.targetAbilityInfo.name}`);
  };
  controller.on('shareCompleted', callback);
  controller.show(context, {
    previewMode: systemShare.SharePreviewMode.DETAIL,
    selectionMode: systemShare.SelectionMode.SINGLE,
  }).then(() => {
    hilog.info(DOMAIN, 'testTag', 'HuaweiShare_ show');
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, 'testTag', `HuaweiShare_ show error. Code: ${error?.code}, message: ${error?.message}`);
  });
}
```

### off('shareCompleted')

off(type: 'shareCompleted', callback?: Callback<ShareOperationResult>): void

取消用户完成分享事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'shareCompleted'，取消触发该事件。 |
| callback | Callback<[ShareOperationResult](share-system-share.md#shareoperationresult)> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |

**示例：**

```typescript
private async handelShareDisableCompleted(): Promise<void> {
  const uiContext: UIContext = this.getUIContext();
  const contextFaker: Context = uiContext.getHostContext() as Context;
  let filePath = contextFaker.filesDir + '/exampleImage.jpg';
  let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utdTypeId,
    uri: fileUri.getUriFromPath(filePath),
    title: 'Picture Title',
    description: 'Picture Description',
  });
  let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
  const context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
  const callback = (result: systemShare.ShareOperationResult) => {
    hilog.info(DOMAIN, 'testTag', `HuaweiShare_ shareCompleted invoked. result: ${result.targetAbilityInfo.name}`);
  };
  controller.on('shareCompleted', callback);
  controller.off('shareCompleted', callback);
}
```

## getSharedData

getSharedData(want: Want): Promise<SharedData>

通过目标应用获取的want信息，从中解析出分享数据，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-inner-ability-want.md) | 是 | 目标应用获取的want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SharedData](share-system-share.md#shareddata)> | Promise对象，返回分享数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[分享服务错误码](share-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1003703001](share-error-code.md#section1003703001-数据解析失败) | Parse data failed. |

**示例：**

```typescript
aboutToAppear(): void {
  systemShare.getSharedData(this.want).then((data: systemShare.SharedData) => {
    let records: systemShare.SharedRecord[] = data.getRecords();
    records.forEach(async (record: systemShare.SharedRecord) => {
      switch (true) {
        case this.belongsToImage(record.utd):
          record.uri && (this.imageUri = record.uri);
          break;
        default:
          break;
      }
    });
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, 'testTag', `getSharedData error. Code: ${error?.code}, message: ${error?.message}`);
  });
}
```

## getContactInfo

getContactInfo(want: Want): Promise<ContactInfo>

通过目标应用获取的want信息，从中解析联系人信息，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-inner-ability-want.md) | 是 | 目标应用获取的want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ContactInfo](share-system-share.md#contactinfo)> | Promise对象，返回联系人信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[分享服务错误码](share-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1003703001](share-error-code.md#section1003703001-数据解析失败) | Parse data failed. |

**示例：**

```typescript
aboutToAppear(): void {
  systemShare.getContactInfo(this.want).then(async (contact: systemShare.ContactInfo) => {
    let data = await systemShare.getSharedData(this.want);
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, 'testTag', `getContactInfo error. Code: ${error?.code}, message: ${error?.message}`);
  });
}
```

## getWant

getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>

基于SharedData和预览模式构造want数据，使用Promise异步回调。

**说明** 

请勿随意修改返回值want数据中的参数，可能会导致未知的错误。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.SystemShare

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [SharedData](share-system-share.md#shareddata) | 是 | 分享目标应用的分享数据信息。 |
| options | [ShareControllerOptions](share-system-share.md#sharecontrolleroptions) | 否 | 分享控制器配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Want](js-apis-inner-ability-want.md)> | Promise对象，返回分享目标应用的want信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[分享服务错误码](share-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| [1003703001](share-error-code.md#section1003703001-数据解析失败) | Parse data failed. |

**示例：**

不配置预览模式

```typescript
onSessionCreate(): void {
  let data: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: 'Hello HarmonyOS'
  });

  data.addRecord({
    utd: utd.UniformDataType.PNG,
    uri: 'file://.../test.png'
  });

  systemShare.getWant(data)
    .then((want) => {
    })
    .catch((error: BusinessError) => {
      hilog.error(DOMAIN, 'testTag', `Failed to getWant. Code: ${error?.code}, message: ${error?.message}`);
  });
}
```

配置预览模式

```typescript
onSessionCreatePreview(): void {
  let data: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN_TEXT,
    content: 'Hello HarmonyOS'
  });
  data.addRecord({
    utd: utd.UniformDataType.PNG,
    uri: 'file://.../test.png'
  });
  let options : systemShare.ShareControllerOptions = {
    previewMode: systemShare.SharePreviewMode.DETAIL,
    selectionMode: systemShare.SelectionMode.SINGLE
  };
  systemShare.getWant(data, options)
    .then((want) => {
    })
    .catch((error: BusinessError) => {
      hilog.error(DOMAIN, 'testTag', `Failed to getWant. Code: ${error?.code}, message: ${error?.message}`);
    });
}
```
