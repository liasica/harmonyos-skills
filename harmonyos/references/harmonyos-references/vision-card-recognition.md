---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-card-recognition
title: CardRecognition（卡证识别控件）
breadcrumb: API参考 > AI > Vision Kit（场景化视觉服务） > ArkTS组件 > CardRecognition（卡证识别控件）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8b88feef2b95dfbc1106e5aeb65be737628f0038bc2939127556bbb9eda8e3e
---

卡证识别控件提供身份证、行驶证、驾驶证、护照、银行卡证件的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。

**起始版本：** 5.0.0(12)

说明

使用该控件会创建弹窗，并以全模态形式展示。因此，该控件被拉起或退出时均会触发接入页面的生命周期变化，拉起时会触发页面的onPageHide，退出时则触发页面的onPageShow。

## 导入模块

PhoneTablet

```
1. import { CardRecognition, CardRecognitionResult, CardType, CardSide,
2. CardRecognitionConfig, ShootingMode, CardContentConfig, BankCardConfig } from "@kit.VisionKit";
```

## CardRecognition

PhoneTablet

卡证识别控件，集成此控件可以实现卡证识别。

**装饰器类型：** @Component

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| supportType | [CardType](vision-card-recognition.md#cardtype) | 是 | - | 表示需要识别的卡证类型。当前仅支持中国大陆地区相关卡证的识别。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| cardSide | [CardSide](vision-card-recognition.md#cardside) | 否 | - | 表示需要识别的卡证页面。默认值：DEFAULT。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| callback(deprecated) | [Callback](js-apis-base.md#callback)<[CallbackParam](vision-card-recognition.md#callbackparamdeprecated)> | 是 | - | 卡证识别结果的返回。callback和onResult参数同时配置时只有callback生效。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **说明：**  从5.1.1(19)开始废弃。建议使用onResult替代。 |
| onResult | [Callback](js-apis-base.md#callback)<[CardRecognitionResult](vision-card-recognition.md#cardrecognitionresult)> | 是 | - | 卡证识别结果的返回。callback和onResult参数同时配置时只有callback生效。  **元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。  **起始版本：** 5.1.1(19) |
| cardRecognitionConfig | [CardRecognitionConfig](vision-card-recognition.md#cardrecognitionconfig) | 否 | - | 卡证识别配置项。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

## CardType

PhoneTablet

支持识别的卡证类型的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CARD\_AUTO | 0 | 自动识别卡证类型，不预设类型。 |
| CARD\_ID | 1 | 身份证。 |
| CARD\_BANK | 2 | 银行卡。 |
| CARD\_PASSPORT | 3 | 护照。 |
| CARD\_DRIVER\_LICENSE | 4 | 驾驶证。 |
| CARD\_VEHICLE\_LICENSE | 5 | 行驶证。 |

## CardSide

PhoneTablet

需要识别的卡证页面的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FRONT | 0 | 身份证人像面或其他卡证正面。 |
| BACK | 1 | 身份证国徽面或其他卡证反面。 |
| DEFAULT | 2 | 卡证默认面。如身份证为人像面，其他卡证为正面。 |

## CallbackParam(deprecated)

PhoneTablet

卡证识别结果返回的参数。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

说明

从5.1.1(19)开始废弃。建议使用[CardRecognitionResult](vision-card-recognition.md#cardrecognitionresult)替代。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 返回的结果码（200：识别成功，-1：识别失败）。 |
| cardType | [CardType](vision-card-recognition.md#cardtype) | 否 | 是 | 卡证类型。默认值：CARD\_AUTO。 |
| cardInfo | Record<string, Record<string, string>> | 否 | 是 | 卡证信息。默认值：undefined。  对于双面卡证，包含信息为”front”和”back”。  对于单面卡证，包含信息为”main”。 |

## CardRecognitionResult

PhoneTablet

卡证识别结果返回的参数。

**元服务API：** 从版本5.1.1(19)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 返回的结果码：  200：识别成功。  1008701001：未识别。  1008701002：识别失败。  1008701003：部分识别失败。  1008701004：未完成识别。 |
| cardType | [CardType](vision-card-recognition.md#cardtype) | 否 | 是 | 卡证类型。默认值：CARD\_AUTO。 |
| cardInfo | Record<string, Record<string, string>> | 否 | 是 | 卡证信息。默认值：undefined。  对于双面卡证，包含信息为”front”和”back”。  对于单面卡证，包含信息为”main”。 |

## CardRecognitionConfig

PhoneTablet

卡证识别配置项。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| defaultShootingMode | [ShootingMode](vision-card-recognition.md#shootingmode) | 否 | 是 | 拍摄模式，默认值：ShootingMode.MANUAL。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| isPhotoSelectionSupported | boolean | 否 | 是 | 是否支持从图库选图。  - true为显示图库按钮并支持从图库选图。  - false为不显示图库按钮且不支持从图库选图。  默认值：true。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| setCardMargins | number | 否 | 是 | 设置经裁剪的卡证图片预留边距。范围[10,10000]。  若设定值大于原图某边边距，此边边距取原图，不做裁剪。  默认值：10。单位：px。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.3(15) |
| cardContentConfig | [CardContentConfig](vision-card-recognition.md#cardcontentconfig) | 否 | 是 | 卡证内容配置。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

## ShootingMode

PhoneTablet

拍摄模式的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 自动拍摄。 |
| MANUAL | 1 | 手动拍摄。 |

## CardContentConfig

PhoneTablet

卡证内容配置项，可设置各类型卡证的具体配置。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bankCard | [BankCardConfig](vision-card-recognition.md#bankcardconfig) | 否 | 是 | 识别银行卡的具体配置。  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| idCard | [IdCardConfig](vision-card-recognition.md#idcardconfig) | 否 | 是 | 识别身份证的具体配置。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。  **起始版本**：5.0.2(14)。 |

## BankCardConfig

PhoneTablet

银行卡识别的具体配置。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isBankNumberDialogShown | boolean | 否 | 是 | 识别到银行卡后是否弹出银行卡号确认弹框，true为识别后弹出确认弹框，false为识别后不弹出确认弹框，默认值：true。 |

## IdCardConfig

PhoneTablet

身份证识别的具体配置。

**系统能力：** SystemCapability.AI.Component.CardRecognition

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isPhotoNeeded | boolean | 否 | 是 | 识别到身份证人像面后是否需要返回身份证的人像图片。  true：需要返回身份证人像照片。  false：不需要返回身份证人像照片。  默认值：false。 |
| isQualityDetectionNeeded | boolean | 否 | 是 | 是否开启质量检测。  true：开启质量检测。  false：不开启质量检测。  默认值：false。 |

## cardInfo

PhoneTablet

具体证件相关信息，包含身份证人像面和国徽面、银行卡、护照、驾驶证正反面、行驶证正反面。

身份证人像面

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| name | string | 姓名。 |
| sex | string | 性别。 |
| nationality | string | 民族。 |
| birth | string | 出生日期。 |
| address | string | 住址。 |
| idNumber | string | 公民身份号码。 |
| cardImageUri | string | 身份证人像面图片uri（不含背景）。 |
| originalImageUri | string | 身份证人像面图片uri（含背景）。 |
| photoUri | string | 身份证人像面内的人像图片uri。仅在isPhotoNeeded为true时返回。  **起始版本**：5.0.2(14)。 |
| photoLocation | string | 人像图片在cardImageUri字段所代表的身份证（人像面）图片内的坐标。按top、left作为左上角顶点，width、height人像图片的宽高。  仅在isPhotoNeeded为true时返回。  **起始版本**：5.0.2(14)。 |
| completenessProbability | string | 完整的概率。取值范围：(0,1)。值越大，完整的概率越大。  **起始版本**：5.0.2(14)。 |
| reflectionProbability | string | 反光的概率。取值范围：(0,1)。值越大，反光的概率越大。  **起始版本**：5.0.2(14)。 |
| clarityProbability | string | 清晰的概率。取值范围：(0,1)。值越大，清晰的概率越大。  **起始版本**：5.0.2(14)。 |
| occlusionProbability | string | 遮挡的概率。取值范围：(0,1)。值越大，遮挡的概率越大。  **起始版本**：5.0.2(14)。 |

身份证国徽面

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| authority | string | 签发机关。 |
| validPeriod | string | 有效期限。 |
| cardImageUri | string | 身份证国徽面图片uri（不含背景）。 |
| originalImageUri | string | 身份证国徽面图片uri（含背景）。 |
| completenessProbability | string | 完整的概率。取值范围：(0,1)。值越大，完整的概率越大。  **起始版本**：5.0.2(14)。 |
| reflectionProbability | string | 反光的概率。取值范围：(0,1)。值越大，反光的概率越大。  **起始版本**：5.0.2(14)。 |
| clarityProbability | string | 清晰的概率。取值范围：(0,1)。值越大，清晰的概率越大。  **起始版本**：5.0.2(14)。 |
| occlusionProbability | string | 遮挡的概率。取值范围：(0,1)。值越大，遮挡的概率越大。  **起始版本**：5.0.2(14)。 |

银行卡

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| bankNum | string | 银行卡号。 |
| validPeriod | string | 有效期限。 |
| cardImageUri | string | 银行卡图片uri（不含背景）。 |
| originalImageUri | string | 银行卡图片uri（含背景）。 |

护照

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| cardNum | string | 护照号码。 |
| name | string | 姓名。 |
| sex | string | 性别。 |
| nationality | string | 国籍。 |
| birth | string | 出生日期。 |
| address | string | 出生地点。 |
| issueDate | string | 签发日期。 |
| issuePlace | string | 签发地点。 |
| expiryDate | string | 有效期至。 |
| authority | string | 签发机关。 |
| pochn | string | 因私护照。 |
| cardImageUri | string | 护照图片uri（不含背景）。 |
| originalImageUri | string | 护照图片uri（含背景）。 |

驾驶证正面

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| cardNum | string | 证号。 |
| name | string | 姓名。 |
| sex | string | 性别。 |
| nationality | string | 国籍。 |
| birth | string | 出生日期。 |
| address | string | 住址。 |
| dateOfFirstIssue | string | 初次领证日期。 |
| carClass | string | 准驾车型。 |
| validPeriodStart | string | 有效期限-起始。 |
| validPeriodEnd | string | 有效期限-终止。 |
| cardImageUri | string | 驾驶证正面图片uri（不含背景）。 |
| originalImageUri | string | 驾驶证正面图片uri（含背景）。 |

驾驶证反面

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| cardNum | string | 证号。 |
| name | string | 姓名。 |
| archivesNum | string | 档案编号。 |
| record | string | 记录。 |
| cardImageUri | string | 驾驶证反面图片uri（不含背景）。 |
| originalImageUri | string | 驾驶证反面图片uri（含背景）。 |

行驶证正面

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| licensePlateNumber | string | 号牌号码。 |
| vehicleType | string | 车辆类型。 |
| owner | string | 所有人。 |
| address | string | 住址。 |
| useCharacter | string | 使用性质。 |
| model | string | 品牌型号。 |
| vin | string | 车辆识别代码。 |
| engineNum | string | 发动机号码。 |
| registerDate | string | 注册日期。 |
| issueDate | string | 发证日期。 |
| cardImageUri | string | 行驶证正面图片uri（不含背景）。 |
| originalImageUri | string | 行驶证正面图片uri（含背景）。 |

行驶证反面

**起始版本：** 5.0.0(12)

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| cardNum | string | 号牌号码。 |
| size | string | 外廓尺寸。 |
| remark | string | 备注。 |
| record | string | 检验记录。 |
| cardImageUri | string | 行驶证反面图片uri（不含背景）。 |
| originalImageUri | string | 行驶证反面图片uri（含背景）。 |
