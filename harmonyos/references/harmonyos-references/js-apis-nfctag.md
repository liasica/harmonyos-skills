---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfctag
title: @ohos.nfc.tag (标准NFC-Tag)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.nfc.tag (标准NFC-Tag)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:01+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:cac1c75bbbb088488b78d4cd3db56ced3f7217300ed11f3f04c7fb15bcf4da8d
---

本模块主要用于操作及管理NFC Tag，提供后台读卡和前台应用优先分发两种读卡模式。

后台读卡是指不需要打开应用程序，电子设备通过NFC读取标签卡片后，根据标签卡片的类型匹配到一个或多个应用程序。如果仅匹配到一个，则直接拉起应用程序的读卡页面；如果是多个则弹出应用选择器，让用户选择指定的读卡应用。后台读卡不涉及tag相关接口，示例参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md#后台读取标签)。

前台读卡是指提前打开应用程序，并进入对应的NFC读卡页面后读卡，只会把读到的标签卡片信息分发给前台应用程序。

说明

1. 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
2. 调用本模块接口和常量时请使用canIUse("SystemCapability.Communication.NFC.Tag")判断设备是否支持NFC能力，否则可能导致应用运行稳定性问题，参考[nfc-tag开发指南](../harmonyos-guides/nfc-tag-access-guide.md)。
3. 导入tag模块编辑器报错，在某个具体设备型号上能力可能超出工程默认设备定义的能力集范围，如需要使用此部分能力需额外配置自定义syscap，参考[syscap开发指南](syscap.md#syscap开发指导)。

## **导入模块**

PhoneWearable

```
1. import { tag } from '@kit.ConnectivityKit';
```

## **tag.TagInfo**

PhoneWearable

在对相关Tag类型卡片进行读写之前，必须先获取[TagInfo](js-apis-nfctag.md#taginfo)相关属性值，以确认设备读取到的Tag卡片支持哪些技术类型。这样Tag应用程序才能调用正确的接口和所读取到的Tag卡片进行通信。

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want : Want, launchParam: AbilityConstant.LaunchParam) {
6. // 添加其他功能代码...

8. // want由nfc服务初始化，包含找到的tag
9. let tagInfo : tag.TagInfo | null = null;
10. try {
11. tagInfo = tag.getTagInfo(want);
12. } catch (error) {
13. console.error("tag.getTagInfo catch error: " + error);
14. }
15. if (tagInfo == null) {
16. console.error("no TagInfo to be created, ignore it.");
17. return;
18. }

20. // 获取发现标签的支持技术
21. let isNfcATag =  false;
22. let isIsoDepTag =  false;
23. for (let i = 0; i < tagInfo.technology.length; i++) {
24. if (tagInfo.technology[i] == tag.NFC_A) {
25. isNfcATag = true;
26. }
27. if (tagInfo.technology[i] == tag.ISO_DEP) {
28. isIsoDepTag = true;
29. }
30. // 检查其他技术类型: tag.NFC_B/NFC_F/NFC_V/NDEF/MIFARE_CLASSIC/MIFARE_ULTRALIGHT/NDEF_FORMATABLE
31. }

33. // 使用 NfcA APIs 去访问发现的标签
34. if (isNfcATag) {
35. let nfcA : tag.NfcATag | null = null;
36. try {
37. nfcA = tag.getNfcA(tagInfo);
38. } catch (error) {
39. console.error("tag.getNfcA catch error: " + error);
40. }
41. // 其他代码：对发现的标签执行读取或写入
42. }

44. // 使用 IsoDep APIs 去访问发现的标签
45. if (isIsoDepTag) {
46. let isoDep : tag.IsoDepTag | null = null;
47. try {
48. isoDep = tag.getIsoDep(tagInfo);
49. } catch (error) {
50. console.error("tag.getIsoDep catch error: " + error);
51. }
52. // 其他代码：对发现的标签执行读取或写入
53. }
54. // 使用相同的代码来处理 "NfcA/NfcB/NfcF/NfcV/Ndef/MifareClassic/MifareUL/NdefFormatable".
55. }
56. }
```

## tag.getNfcATag(deprecated)

PhoneWearable

getNfcATag(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcATag](js-apis-nfctech.md#nfcatag)

获取NFC A类型Tag对象，通过该对象可访问NfcA技术类型的Tag。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcA](js-apis-nfctag.md#taggetnfca9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcATag](js-apis-nfctech.md#nfcatag) | NFC A类型Tag对象。 |

## tag.getNfcA9+

PhoneWearable

getNfcA(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcATag](js-apis-nfctech.md#nfcatag)

获取NFC A类型Tag对象，通过该对象可访问NfcA技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcATag](js-apis-nfctech.md#nfcatag) | NFC A类型Tag对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getNfcBTag(deprecated)

PhoneWearable

getNfcBTag(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcBTag](js-apis-nfctech.md#nfcbtag)

获取NFC B类型Tag对象，通过该对象可访问NfcB技术类型的Tag。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcB](js-apis-nfctag.md#taggetnfcb9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcBTag](js-apis-nfctech.md#nfcbtag) | NFC B类型Tag对象。 |

## tag.getNfcB9+

PhoneWearable

getNfcB(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcBTag](js-apis-nfctech.md#nfcbtag)

获取NFC B类型Tag对象，通过该对象可访问NfcB技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcBTag](js-apis-nfctech.md#nfcbtag) | NFC B类型Tag对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getNfcFTag(deprecated)

PhoneWearable

getNfcFTag(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcFTag](js-apis-nfctech.md#nfcftag)

获取NFC F类型Tag对象，通过该对象可访问NfcF技术类型的Tag。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcF](js-apis-nfctag.md#taggetnfcf9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcFTag](js-apis-nfctech.md#nfcftag) | NFC F类型Tag对象。 |

## tag.getNfcF9+

PhoneWearable

getNfcF(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcFTag](js-apis-nfctech.md#nfcftag)

获取NFC F类型Tag对象，通过该对象可访问NfcF技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcFTag](js-apis-nfctech.md#nfcftag) | NFC F类型Tag对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getNfcVTag(deprecated)

PhoneWearable

getNfcVTag(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcVTag](js-apis-nfctech.md#nfcvtag)

获取NFC V类型Tag对象，通过该对象可访问NfcV技术类型的Tag。

说明

从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[tag.getNfcV](js-apis-nfctag.md#taggetnfcv9)替代。

**系统能力：** SystemCapability.Communication.NFC.Tag

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcVTag](js-apis-nfctech.md#nfcvtag) | NFC V类型Tag对象。 |

## tag.getNfcV9+

PhoneWearable

getNfcV(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NfcVTag](js-apis-nfctech.md#nfcvtag)

获取NFC V类型Tag对象，通过该对象可访问NfcV技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NfcVTag](js-apis-nfctech.md#nfcvtag) | NFC V类型Tag对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getIsoDep9+

PhoneWearable

getIsoDep(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [IsoDepTag](js-apis-nfctech.md#isodeptag9)

获取IsoDep类型Tag对象，通过该对象可访问支持IsoDep技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [IsoDepTag](js-apis-nfctech.md#isodeptag9) | IsoDep类型Tag对象，通过该对象访问IsoDep类型的相关接口。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getNdef9+

PhoneWearable

getNdef(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NdefTag](js-apis-nfctech.md#ndeftag9)

获取NDEF类型Tag对象，通过该对象可访问支持NDEF技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefTag](js-apis-nfctech.md#ndeftag9) | NDEF类型Tag对象，通过该对象访问NDEF类型的相关接口。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getMifareClassic9+

PhoneWearable

getMifareClassic(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [MifareClassicTag](js-apis-nfctech.md#mifareclassictag9)

获取MIFARE Classic类型Tag对象，通过该对象访问支持MIFARE Classic技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [MifareClassicTag](js-apis-nfctech.md#mifareclassictag9) | MIFARE Classic类型Tag对象，通过该对象访问MIFARE Classic类型的相关接口。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getMifareUltralight9+

PhoneWearable

getMifareUltralight(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [MifareUltralightTag](js-apis-nfctech.md#mifareultralighttag9)

获取MIFARE Ultralight类型Tag对象，通过该对象可访问支持MIFARE Ultralight技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [MifareUltralightTag](js-apis-nfctech.md#mifareultralighttag9) | MIFARE Ultralight类型Tag对象，通过该对象访问MIFARE Ultralight类型的相关接口。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getNdefFormatable9+

PhoneWearable

getNdefFormatable(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [NdefFormatableTag](js-apis-nfctech.md#ndefformatabletag9)

获取NDEF Formatable类型Tag对象，通过该对象可访问支持NDEF Formatable技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefFormatableTag](js-apis-nfctech.md#ndefformatabletag9) | NDEF Formatable类型Tag对象，通过该对象访问NDEF Formatable类型的相关接口。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getBarcodeTag18+

PhoneWearable

getBarcodeTag(tagInfo: [TagInfo](js-apis-nfctag.md#taginfo)): [BarcodeTag](js-apis-nfctech.md#barcodetag18)

获取BarcodeTag类型Tag对象，通过该对象可访问BarcodeTag技术类型的Tag。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tagInfo | [TagInfo](js-apis-nfctag.md#taginfo) | 是 | 包含Tag技术类型和相关参数，从[tag.getTagInfo(want: Want)](js-apis-nfctag.md#taggettaginfo9)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BarcodeTag](js-apis-nfctech.md#barcodetag18) | BarcodeTag类型Tag对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

## tag.getTagInfo9+

PhoneWearable

getTagInfo(want: [Want](js-apis-app-ability-want.md#want)): [TagInfo](js-apis-nfctag.md#taginfo)

从Want中获取TagInfo，Want是被NFC服务初始化，包含了TagInfo所需的属性值。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md#want) | 是 | 分发Ability时，在系统onCreate入口函数的参数中获取。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [TagInfo](js-apis-nfctag.md#taginfo) | TagInfo对象，用于获取不同技术类型的Tag对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |

## tag.registerForegroundDispatch10+

PhoneWearable

registerForegroundDispatch(elementName: [ElementName](js-apis-bundlemanager-elementname.md), discTech: number[], callback: AsyncCallback<[TagInfo](js-apis-nfctag.md#taginfo)>): void

注册对NFC Tag读卡事件的监听，实现前台应用优先分发的目的。通过discTech设置支持的读卡技术类型，通过callback方式获取读取到Tag的[TagInfo](js-apis-nfctag.md#taginfo)信息。应用必须在前台才能调用。需要与取消监听接口[tag.unregisterForegroundDispatch](js-apis-nfctag.md#tagunregisterforegrounddispatch10)成对使用。如果已注册事件监听，需要在页面退出前台或页面销毁前调用取消注册。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| discTech | number[] | 是 | 前台应用指定的NFC读卡技术类型，不可以为空，至少指定一种读卡技术类型。每个number值表示所支持技术类型的常量值型，根据number值设置NFC读卡轮询的Tag技术类型（仅包含[NFC\_A](js-apis-nfctag.md#常量), [NFC\_B](js-apis-nfctag.md#常量), [NFC\_F](js-apis-nfctag.md#常量), [NFC\_V](js-apis-nfctag.md#常量)中的一种或多种）。 |
| callback | AsyncCallback<[TagInfo](js-apis-nfctag.md#taginfo)> | 是 | 前台读卡监听回调函数，返回读到的Tag信息，不可以为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100202 | The element state is invalid. |

**示例：**

示例请参见[tag.unregisterForegroundDispatch](js-apis-nfctag.md#tagunregisterforegrounddispatch10)接口的示例。

## tag.unregisterForegroundDispatch10+

PhoneWearable

unregisterForegroundDispatch(elementName: [ElementName](js-apis-bundlemanager-elementname.md)): void

取消注册对NFC Tag读卡事件的监听，退出前台应用优先分发。如果已注册事件监听，需要在页面退出前台或页面销毁前调用取消注册。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

5. let discTech : number[] = [tag.NFC_A, tag.NFC_B]; // 用前台ability时所需要的技术代替
6. let elementName : bundleManager.ElementName;
7. function foregroundCb(err : BusinessError, tagInfo : tag.TagInfo) {
8. if (!err) {
9. console.info("foreground callback: tag found tagInfo = ", JSON.stringify(tagInfo));
10. } else {
11. console.error("foreground callback err: " + err.message);
12. return;
13. }
14. // taginfo的其他操作
15. }

17. export default class MainAbility extends UIAbility {
18. OnCreate(want : Want, launchParam : AbilityConstant.LaunchParam) {
19. console.info("OnCreate");
20. elementName = {
21. bundleName: want.bundleName as string,
22. abilityName: want.abilityName as string,
23. moduleName: want.moduleName as string
24. }
25. }

27. onForeground() {
28. console.info("onForeground");
29. try {
30. tag.registerForegroundDispatch(elementName, discTech, foregroundCb);
31. } catch (e) {
32. console.error("registerForegroundDispatch error: " + (e as BusinessError).message);
33. }
34. }

36. onBackground() {
37. console.info("onBackground");
38. try {
39. tag.unregisterForegroundDispatch(elementName);
40. } catch (e) {
41. console.error("unregisterForegroundDispatch error: " + (e as BusinessError).message);
42. }
43. }

45. onWindowStageDestroy() {
46. console.info("onWindowStageDestroy");
47. try {
48. tag.unregisterForegroundDispatch(elementName);
49. } catch (e) {
50. console.error("unregisterForegroundDispatch error: " + (e as BusinessError).message);
51. }
52. }

54. // ability生命周期内的其他功能
55. }
```

## tag.on11+

PhoneWearable

on(type: 'readerMode', elementName: [ElementName](js-apis-bundlemanager-elementname.md), discTech: number[], callback: AsyncCallback<[TagInfo](js-apis-nfctag.md#taginfo)>): void

订阅NFC Tag读卡事件，实现前台应用优先分发。设备会进入读卡器模式，同时关闭卡模拟。通过discTech设置支持的读卡技术类型，通过callback方式获取到Tag的[TagInfo](js-apis-nfctag.md#taginfo)信息。需要与取消读卡器模式的[tag.off](js-apis-nfctag.md#tagoff11)成对使用，如果已通过on进行设置，需要在页面退出前台或页面销毁时调用[tag.off](js-apis-nfctag.md#tagoff11)。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要注册的回调类型，固定填"readerMode"字符串。 |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| discTech | number[] | 是 | 前台应用指定的NFC读卡技术类型，不可以为空，至少指定一种读卡技术类型。每个number值表示所支持技术类型的常量值型，根据number值设置NFC读卡轮询的Tag技术类型（仅包含[NFC\_A](js-apis-nfctag.md#常量), [NFC\_B](js-apis-nfctag.md#常量), [NFC\_F](js-apis-nfctag.md#常量), [NFC\_V](js-apis-nfctag.md#常量)中的一种或多种）。 |
| callback | AsyncCallback<[TagInfo](js-apis-nfctag.md#taginfo)> | 是 | 读卡器模式监听回调函数，返回读到的Tag信息，不可以为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100202 | The element state is invalid. |

**示例：**

示例请参见[tag.off](js-apis-nfctag.md#tagoff11)接口的示例。

## tag.off11+

PhoneWearable

off(type: 'readerMode', elementName: [ElementName](js-apis-bundlemanager-elementname.md), callback?: AsyncCallback<[TagInfo](js-apis-nfctag.md#taginfo)>): void

取消订阅NFC Tag读卡事件。设备退出读卡模式，并恢复卡模拟。如果已通过[tag.on](js-apis-nfctag.md#tagon11)设置NFC的读卡器模式，需要在页面退出前台或页面销毁时调用off进行取消。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要注销的回调类型，固定填"readerMode"字符串。 |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| callback | AsyncCallback<[TagInfo](js-apis-nfctag.md#taginfo)> | 否 | 前台读卡监听回调函数，返回读到的Tag信息。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100203 | The off() API can be called only when the on() has been called. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

5. let discTech : number[] = [tag.NFC_A, tag.NFC_B]; // 用前台ability时所需要的技术代替
6. let elementName : bundleManager.ElementName;

8. function readerModeCb(err : BusinessError, tagInfo : tag.TagInfo) {
9. if (!err) {
10. console.info("offCallback: tag found tagInfo = ", JSON.stringify(tagInfo));
11. } else {
12. console.error("offCallback err: " + err.message);
13. return;
14. }
15. // taginfo的其他操作
16. }

18. export default class MainAbility extends UIAbility {
19. OnCreate(want : Want, launchParam : AbilityConstant.LaunchParam) {
20. console.info("OnCreate");
21. elementName = {
22. bundleName: want.bundleName as string,
23. abilityName: want.abilityName as string,
24. moduleName: want.moduleName as string
25. }
26. }

28. onForeground() {
29. console.info("on start");
30. try {
31. tag.on('readerMode', elementName, discTech, readerModeCb);
32. } catch (e) {
33. console.error("tag.on error: " + (e as BusinessError).message);
34. }
35. }

37. onBackground() {
38. console.info("onBackground");
39. try {
40. tag.off('readerMode', elementName, readerModeCb);
41. } catch (e) {
42. console.error("tag.off error: " + (e as BusinessError).message);
43. }
44. }

46. onWindowStageDestroy() {
47. console.info("onWindowStageDestroy");
48. try {
49. tag.off('readerMode', elementName, readerModeCb);
50. } catch (e) {
51. console.error("tag.off error: " + (e as BusinessError).message);
52. }
53. }

55. // ability生命周期内的其他功能
56. }
```

## tag.on23+

PhoneWearable

on(type: 'readerModeWithInterval', elementName: ElementName, discTech: number[], callback: Callback<TagInfo>, interval: number): void

订阅NFC Tag读卡事件，实现前台应用优先分发，并支持卡在位检测间隔设置。使用callback异步回调。

* 设备会进入读卡器模式，同时关闭卡模拟。
* 通过discTech设置支持的读卡技术类型，通过callback方式获取到Tag的[TagInfo](js-apis-nfctag.md#taginfo)信息，通过interval设置卡在位检测间隔。
* 需要与取消读卡器模式的[tag.off](js-apis-nfctag.md#tagoff23)成对使用，如果已通过on进行设置，需要在页面退出前台或页面销毁时调用[tag.off](js-apis-nfctag.md#tagoff23)。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要注册的回调类型，固定填"readerModeWithInterval"字符串。 |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值）。 |
| discTech | number[] | 是 | 前台应用指定的NFC读卡技术类型，至少指定一种读卡技术类型。每个number值表示所支持技术类型的常量值型，根据number值设置NFC读卡轮询的Tag技术类型（仅包含[NFC\_A](js-apis-nfctag.md#常量), [NFC\_B](js-apis-nfctag.md#常量), [NFC\_F](js-apis-nfctag.md#常量), [NFC\_V](js-apis-nfctag.md#常量)中的一种或多种）。 |
| callback | Callback<[TagInfo](js-apis-nfctag.md#taginfo)> | 是 | 读卡器模式监听回调函数，返回读到的Tag信息。 |
| interval | number | 是 | 设置卡在位检测间隔，单位为ms。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100202 | The element state is invalid. |

**示例：**

示例请参见[tag.off](js-apis-nfctag.md#tagoff23)接口的示例。

## tag.off23+

PhoneWearable

off(type: 'readerModeWithInterval', elementName: ElementName, callback?: Callback<TagInfo>): void

取消订阅NFC Tag读卡事件。设备退出读卡模式，并恢复卡模拟。如果已通过[tag.on](js-apis-nfctag.md#tagon23)设置NFC的读卡器模式，需要在页面退出前台或页面销毁时调用off进行取消。使用callback异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要注销的回调类型，固定填"readerModeWithInterval"字符串。 |
| elementName | [ElementName](js-apis-bundlemanager-elementname.md) | 是 | 所属应用读卡的页面信息（至少包含bundleName、abilityName这两项的赋值）。 |
| callback | Callback<[TagInfo](js-apis-nfctag.md#taginfo)> | 否 | 前台读卡监听回调函数，返回读到的Tag信息。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |
| 3100203 | The off() API can be called only when the on() has been called. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

5. let discTech : number[] = [tag.NFC_A, tag.NFC_B]; // 用前台ability时所需要的技术代替
6. let elementName : bundleManager.ElementName;
7. let interval : number = 200;

9. function readerModeCb(err : BusinessError, tagInfo : tag.TagInfo) {
10. if (!err) {
11. console.info("offCallback: tag found tagInfo = ", JSON.stringify(tagInfo));
12. } else {
13. console.error("offCallback err: " + err.message);
14. return;
15. }
16. // taginfo的其他操作
17. }

19. export default class MainAbility extends UIAbility {
20. OnCreate(want : Want, launchParam : AbilityConstant.LaunchParam) {
21. console.info("OnCreate");
22. elementName = {
23. bundleName: want.bundleName as string,
24. abilityName: want.abilityName as string,
25. moduleName: want.moduleName as string
26. }
27. }

29. onForeground() {
30. console.info("on start");
31. try {
32. tag.on('readerModeWithInterval', elementName, discTech, readerModeCb, interval);
33. } catch (e) {
34. console.error("tag.on error: " + (e as BusinessError).message);
35. }
36. }

38. onBackground() {
39. console.info("onBackground");
40. try {
41. tag.off('readerModeWithInterval', elementName, readerModeCb);
42. } catch (e) {
43. console.error("tag.off error: " + (e as BusinessError).message);
44. }
45. }

47. onWindowStageDestroy() {
48. console.info("onWindowStageDestroy");
49. try {
50. tag.off('readerModeWithInterval', elementName, readerModeCb);
51. } catch (e) {
52. console.error("tag.off error: " + (e as BusinessError).message);
53. }
54. }

56. // ability生命周期内的其他功能
57. }
```

## tag.ndef.makeUriRecord9+

PhoneWearable

makeUriRecord(uri: string): NdefRecord

根据输入的URI，构建NDEF标签的Record数据对象。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 写入到NDEF Record里面的数据内容。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefRecord](js-apis-nfctag.md#ndefrecord9) | NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. try {
4. let uri = "https://www.example.com"; // 修改为正确可用的uri
5. let ndefRecord : tag.NdefRecord = tag.ndef.makeUriRecord(uri);
6. if (ndefRecord != undefined) {
7. console.info("ndefMessage makeUriRecord rtdType: " + ndefRecord.rtdType);
8. console.info("ndefMessage makeUriRecord payload: " + ndefRecord.payload);
9. } else {
10. console.error("ndefMessage makeUriRecord ndefRecord: " + ndefRecord);
11. }
12. } catch (businessError) {
13. console.error("ndefMessage makeUriRecord catch businessError: " + businessError);
14. }
```

## tag.ndef.makeTextRecord9+

PhoneWearable

makeTextRecord(text: string, locale: string): NdefRecord

根据输入的文本数据和编码类型，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 写入到NDEF Record里面的文本数据内容。 |
| locale | string | 是 | 文本数据内容的编码方式。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefRecord](js-apis-nfctag.md#ndefrecord9) | NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. try {
4. let text = "Hello World";   // 修改为想要写入的文本
5. let locale = "en"; // 修改为预期的编码格式
6. let ndefRecord : tag.NdefRecord = tag.ndef.makeTextRecord(text, locale);
7. if (ndefRecord != undefined) {
8. console.info("ndefMessage makeTextRecord rtdType: " + ndefRecord.rtdType);
9. console.info("ndefMessage makeTextRecord payload: " + ndefRecord.payload);
10. } else {
11. console.error("ndefMessage makeTextRecord ndefRecord: " + ndefRecord);
12. }
13. } catch (businessError) {
14. console.error("ndefMessage makeTextRecord catch businessError: " + businessError);
15. }
```

## tag.ndef.makeApplicationRecord18+

PhoneWearable

makeApplicationRecord(bundleName: string): NdefRecord

根据HarmonyOS应用的bundlename，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 要创建标签的应用包名。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefRecord](js-apis-nfctag.md#ndefrecord9) | NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. try {
4. let bundleName: string = 'com.demo.test';
5. let ndefRecord : tag.NdefRecord = tag.ndef.makeApplicationRecord(bundleName);
6. if (ndefRecord != undefined) {
7. console.info("ndefMessage makeApplicationRecord rtdType: " + ndefRecord.rtdType);
8. console.info("ndefMessage makeApplicationRecord payload: " + ndefRecord.payload);
9. } else {
10. console.error("ndefMessage makeApplicationRecord ndefRecord: " + ndefRecord);
11. }
12. } catch (businessError) {
13. console.error("ndefMessage makeApplicationRecord catch businessError: " + businessError);
14. }
```

## tag.ndef.makeMimeRecord9+

PhoneWearable

makeMimeRecord(mimeType: string, mimeData: number[]): NdefRecord

根据输入的MIME数据和类型，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mimeType | string | 是 | 符合RFC规则的MIME类型，比如"text/plain"或"image/jpeg"。 |
| mimeData | number[] | 是 | MIME数据内容，每个number十六进制表示，范围是0x00~0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefRecord](js-apis-nfctag.md#ndefrecord9) | NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. try {
4. let mimeType = "text/plain";   // 修改为预期的符合规则的MIME类型
5. let mimeData = [0x01, 0x02, 0x03, 0x04]; // 修改为预期的符合格式的数据
6. let ndefRecord : tag.NdefRecord = tag.ndef.makeMimeRecord(mimeType, mimeData);
7. if (ndefRecord != undefined) {
8. console.info("ndefMessage makeMimeRecord rtdType: " + ndefRecord.rtdType);
9. console.info("ndefMessage makeMimeRecord payload: " + ndefRecord.payload);
10. } else {
11. console.error("ndefMessage makeMimeRecord ndefRecord: " + ndefRecord);
12. }
13. } catch (businessError) {
14. console.error("ndefMessage makeMimeRecord catch businessError: " + businessError);
15. }
```

## tag.ndef.makeExternalRecord9+

PhoneWearable

makeExternalRecord(domainName: string, type: string, externalData: number[]): NdefRecord

根据应用程序特定的外部数据，构建NDEF标签的Record。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainName | string | 是 | 外部数据发布组织的域名，一般是应用程序的包名。 |
| type | string | 是 | 外部数据的指定类型。 |
| externalData | number[] | 是 | 外部数据内容，每个number十六进制表示，范围是0x00~0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefRecord](js-apis-nfctag.md#ndefrecord9) | NDEF标签的Record，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. try {
4. let domainName = "ohos.nfc.application"; // 修改为符合规范的包名
5. let type = "test"; // 修改为正确的数据类型
6. let externalData = [0x01, 0x02, 0x03, 0x04]; // 修改为正确的外部数据内容
7. let ndefRecord : tag.NdefRecord = tag.ndef.makeExternalRecord(domainName, type, externalData);
8. if (ndefRecord != undefined) {
9. console.info("ndefMessage makeExternalRecord rtdType: " + ndefRecord.rtdType);
10. console.info("ndefMessage makeExternalRecord payload: " + ndefRecord.payload);
11. } else {
12. console.error("ndefMessage makeExternalRecord ndefRecord: " + ndefRecord);
13. }
14. } catch (businessError) {
15. console.error("ndefMessage makeExternalRecord catch businessError: " + businessError);
16. }
```

## tag.ndef.messageToBytes9+

PhoneWearable

messageToBytes(ndefMessage: [NdefMessage](js-apis-nfctech.md#ndefmessage9)): number[]

把输入的NDEF消息数据对象，转换为字节格式的数据。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ndefMessage | [NdefMessage](js-apis-nfctech.md#ndefmessage9) | 是 | NDEF消息数据对象。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number[] | NDEF消息数据对象，所转换成的字节格式的数据。每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. let rawData = [0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43]; // 必须符合NDEF格式的数据
4. try {
5. let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(rawData);
6. console.info("ndef createNdefMessage, ndefMessage: " + ndefMessage);
7. let rawData2 : number[] = tag.ndef.messageToBytes(ndefMessage);
8. console.info("ndefMessage messageToBytes rawData2: " + rawData2);
9. } catch (businessError) {
10. console.error("ndef createNdefMessage businessError: " + businessError);
11. }
```

## tag.ndef.createNdefMessage9+

PhoneWearable

createNdefMessage(data: number[]): [NdefMessage](js-apis-nfctech.md#ndefmessage9)

使用原始字节数据创建NDEF标签的Message。该数据必须符合NDEF Record数据格式，如果不符合格式，则返回的NdefMessage数据对象，所包含的NDEF Record列表会为空。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | number[] | 是 | 原始字节，每个number十六进制表示，范围是0x00~0xFF。要求必须满足NDEF Record的格式。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefMessage](js-apis-nfctech.md#ndefmessage9) | NDEF标签的Message，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. let rawData = [0xD1, 0x01, 0x03, 0x54, 0x4E, 0x46, 0x43];  //必须是可以被解析的NDEF记录
4. try {
5. let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(rawData);
6. console.info("ndef createNdefMessage, ndefMessage: " + ndefMessage);
7. } catch (businessError) {
8. console.error("ndef createNdefMessage businessError: " + businessError);
9. }
```

## tag.ndef.createNdefMessage9+

PhoneWearable

createNdefMessage(ndefRecords: NdefRecord[]): [NdefMessage](js-apis-nfctech.md#ndefmessage9)

使用NDEF Records列表，创建NDEF Message。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| ndefRecords | [NdefRecord](js-apis-nfctag.md#ndefrecord9)[] | 是 | NDEF标签的Record列表，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| [NdefMessage](js-apis-nfctech.md#ndefmessage9) | NDEF标签的Message，详见NDEF技术规范《NFCForum-TS-NDEF\_1.0》。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. import { tag } from '@kit.ConnectivityKit';

3. let uriRecord : tag.NdefRecord = tag.ndef.makeUriRecord("https://www.example.com");
4. let textRecord : tag.NdefRecord = tag.ndef.makeTextRecord("Hello World", "en");
5. let ndefRecords : tag.NdefRecord[] = [uriRecord, textRecord];
6. try {
7. let ndefMessage : tag.NdefMessage = tag.ndef.createNdefMessage(ndefRecords);
8. console.info("ndef createNdefMessage ndefMessage: " + ndefMessage);
9. } catch (businessError) {
10. console.error("ndef createNdefMessage businessError: " + businessError);
11. }
```

## TagInfo

PhoneWearable

NFC服务在读取到标签时给出的对象，通过该对象属性，应用知道该标签支持哪些技术类型，并使用匹配的技术类型来调用相关接口。

**系统能力：** SystemCapability.Communication.NFC.Tag

**需要权限：** ohos.permission.NFC\_TAG

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| uid9+ | number[] | 否 | 否 | 标签的uid，每个number值是十六进制表示，范围是0x00~0xFF。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| technology9+ | number[] | 否 | 否 | 支持的技术类型，每个number值表示所支持技术类型的常量值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| supportedProfiles(deprecated) | number[] | 否 | 否 | 支持的技术类型。  **说明：** 从API version 7开始支持，从API version 9开始废弃，使用[tag.TagInfo#technology](js-apis-nfctag.md#taginfo)替代。 |

## NdefRecord9+

PhoneWearable

NDEF标签Record属性的定义，参考NDEF标签技术规范《NFCForum-TS-NDEF\_1.0》的定义细节。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| tnf | number | 否 | 否 | NDEF Record的TNF(Type Name Field)。 |
| rtdType | number[] | 否 | 否 | NDEF Record的RTD(Record Type Definition)类型值，每个number十六进制表示，范围是0x00~0xFF。 |
| id | number[] | 否 | 否 | NDEF Record的ID，每个number十六进制表示，范围是0x00~0xFF。 |
| payload | number[] | 否 | 否 | NDEF Record的PAYLOAD，每个number十六进制表示，范围是0x00~0xFF。 |

## 常量

PhoneWearable

NFC Tag有多种不同的技术类型，定义常量描述不同的技术类型。

**系统能力：** SystemCapability.Communication.NFC.Tag

| **名称** | **类型** | **值** | **说明** |
| --- | --- | --- | --- |
| NFC\_A | number | 1 | NFC-A (ISO 14443-3A)技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NFC\_B | number | 2 | NFC-B (ISO 14443-3B)技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ISO\_DEP | number | 3 | ISO-DEP (ISO 14443-4)技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NFC\_F | number | 4 | NFC-F (JIS 6319-4)技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NFC\_V | number | 5 | NFC-V (ISO 15693)技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NDEF | number | 6 | NDEF技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NDEF\_FORMATABLE9+ | number | 7 | 可以格式化的NDEF技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MIFARE\_CLASSIC | number | 8 | MIFARE Classic技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MIFARE\_ULTRALIGHT | number | 9 | MIFARE Ultralight技术。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| NFC\_BARCODE18+ | number | 10 | BARCODE技术。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| RTD\_TEXT9+ | number[] | [0x54] | 文本类型的NDEF Record，参考NDEF标签技术规范《NFCForum-TS-NDEF\_1.0》的定义细节。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| RTD\_URI9+ | number[] | [0x55] | URI类型的NDEF Record，参考NDEF标签技术规范《NFCForum-TS-NDEF\_1.0》的定义细节。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## TnfType9+

PhoneWearable

NDEF Record的TNF(Type Name Field)类型值，参考NDEF标签技术规范《NFCForum-TS-NDEF\_1.0》的定义细节。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| TNF\_EMPTY | 0x0 | Empty。 |
| TNF\_WELL\_KNOWN | 0x1 | NFC Forum well-known type [NFC RTD]。 |
| TNF\_MEDIA | 0x2 | Media-type as defined in RFC 2046 [RFC 2046]。 |
| TNF\_ABSOLUTE\_URI | 0x3 | Absolute URI as defined in RFC 3986 [RFC 3986]。 |
| TNF\_EXT\_APP | 0x4 | NFC Forum external type [NFC RTD]。 |
| TNF\_UNKNOWN | 0x5 | Unknown。 |
| TNF\_UNCHANGED | 0x6 | Unchanged (see section 2.3.3)。 |

## NfcForumType9+

PhoneWearable

NFC Forum标准里面Tag类型的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NFC\_FORUM\_TYPE\_1 | 1 | NFC论坛类型1。 |
| NFC\_FORUM\_TYPE\_2 | 2 | NFC论坛类型2。 |
| NFC\_FORUM\_TYPE\_3 | 3 | NFC论坛类型3。 |
| NFC\_FORUM\_TYPE\_4 | 4 | NFC论坛类型4。 |
| MIFARE\_CLASSIC | 101 | MIFARE Classic类型。 |

## MifareClassicType9+

PhoneWearable

MIFARE Classic标签类型的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| TYPE\_UNKNOWN | 0 | 未知的MIFARE类型。 |
| TYPE\_CLASSIC | 1 | MIFARE Classic类型。 |
| TYPE\_PLUS | 2 | MIFARE Plus类型。 |
| TYPE\_PRO | 3 | MIFARE Pro类型。 |

## MifareClassicSize9+

PhoneWearable

MIFARE Classic标签存储大小的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| MC\_SIZE\_MINI | 320 | 每个标签5个扇区，每个扇区4个块。 |
| MC\_SIZE\_1K | 1024 | 每个标签16个扇区，每个扇区4个块。 |
| MC\_SIZE\_2K | 2048 | 每个标签32个扇区，每个扇区4个块。 |
| MC\_SIZE\_4K | 4096 | 每个标签40个扇区，每个扇区4个块。 |

## MifareUltralightType9+

PhoneWearable

MIFARE Ultralight标签类型的定义。

**系统能力：** SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| **名称** | **值** | **说明** |
| --- | --- | --- |
| TYPE\_UNKNOWN | 0 | 未知的 MIFARE 类型。 |
| TYPE\_ULTRALIGHT | 1 | MIFARE Ultralight类型。 |
| TYPE\_ULTRALIGHT\_C | 2 | MIFARE UltralightC 类型。 |

## NfcATag

PhoneWearable

type NfcATag = \_NfcATag

获取NfcATag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NfcATag](js-apis-nfctech.md#nfcatag) | NfcATag 提供 NFC-A(ISO 14443-3A)技术的属性和I/O操作的访问。 |

## NfcBTag

PhoneWearable

type NfcBTag = \_NfcBTag

获取NfcBTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NfcBTag](js-apis-nfctech.md#nfcbtag) | NfcBTag 提供 NFC-B(ISO 14443-3B)技术的属性和I/O操作的访问。 |

## NfcFTag

PhoneWearable

type NfcFTag = \_NfcFTag

获取NfcFTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NfcFTag](js-apis-nfctech.md#nfcftag) | NfcFTag 提供对 NFC-F(JIS 6319-4)技术的属性和I/O操作的访问。 |

## NfcVTag

PhoneWearable

type NfcVTag = \_NfcVTag

获取NfcVTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NfcVTag](js-apis-nfctech.md#nfcvtag) | NfcVTag 提供对 NFC-V(ISO 15693)技术的属性和I/O操作的访问。 |

## IsoDepTag9+

PhoneWearable

type IsoDepTag = \_IsoDepTag

获取IsoDepTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_IsoDepTag](js-apis-nfctech.md#isodeptag9) | IsoDepTag 提供 ISO-DEP(ISO 14443-4)技术的属性和I/O操作的访问。 |

## NdefTag9+

PhoneWearable

type NdefTag = \_NdefTag

获取NdefTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NdefTag](js-apis-nfctech.md#ndeftag9) | 提供对已格式化为NDEF的NFC标签的数据和操作的访问。 |

## MifareClassicTag9+

PhoneWearable

type MifareClassicTag = \_MifareClassicTag

获取MifareClassicTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_MifareClassicTag](js-apis-nfctech.md#mifareclassictag9) | MifareClassicTag提供对MIFARE Classic属性和I/O操作的访问。 |

## MifareUltralightTag9+

PhoneWearable

type MifareUltralightTag = \_MifareUltralightTag;

获取MifareUltralightTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_MifareUltralightTag](js-apis-nfctech.md#mifareultralighttag9) | MifareUltralightTag 提供对MIFARE Ultralight属性和I/O操作的访问。 |

## NdefFormatableTag9+

PhoneWearable

type NdefFormatableTag = \_NdefFormatableTag

获取NdefFormatableTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NdefFormatableTag](js-apis-nfctech.md#ndefformatabletag9) | NdefFormatableTag为NDEF Formattable的标签提供格式化操作。 |

## BarcodeTag18+

PhoneWearable

type BarcodeTag = \_BarcodeTag

获取BarcodeTag。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_BarcodeTag](js-apis-nfctech.md#barcodetag18) | 提供对条形码标签的属性和I/O操作的访问。 |

## NdefMessage9+

PhoneWearable

type NdefMessage = \_NdefMessage

获取NdefMessage。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_NdefMessage](js-apis-nfctech.md#ndefmessage9) | 获取NDEF消息中的所有记录。 |

## TagSession

PhoneWearable

type TagSession = \_TagSession

获取TagSession。

**系统能力**：SystemCapability.Communication.NFC.Tag

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_TagSession](js-apis-tagsession.md#tagsession) | TagSession是所有[NFC Tag技术类型](js-apis-nfctech.md)的基类， 提供建立连接和发送数据等共同接口。 |
