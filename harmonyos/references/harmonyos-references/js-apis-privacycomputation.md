---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-privacycomputation
title: "@ohos.security.privacyComputation (隐私计算)"
breadcrumb: API参考 > 系统 > 安全 > Data Protection Kit（数据保护服务） > ArkTS API > @ohos.security.privacyComputation (隐私计算)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a975d776deb37343954b9d0a3006347c60bfb93609ed79e3c642b2887763fc45
---

本模块提供隐私保护的计算能力，包括隐私目标生成、隐私搜索、搜索结果检索等，可用于在不向对方透露原始数据与数据集内容的前提下完成数据比对与检索。

一次完整的隐私计算包含三个步骤：发起端调用[genPrivacyTarget](js-apis-privacycomputation.md#privacycomputationgenprivacytarget)生成隐私目标，响应端调用[privacySearch](js-apis-privacycomputation.md#privacycomputationprivacysearch)执行隐私搜索并返回结果密文，发起端调用[getSearchResult](js-apis-privacycomputation.md#privacycomputationgetsearchresult)解密结果密文得到命中结果及响应端的原始附加值。

**起始版本**：26.0.1

## 导入模块

```ts
import { privacyComputation } from '@kit.DataProtectionKit';
```

## HashAlg

定义用于隐私保护计算的哈希算法枚举。用于对目标元素或数据集元素计算哈希值。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 没有哈希算法。未显式指定哈希算法时，默认为NONE。 |
| SHA256 | 1 | SHA256哈希算法。 |
| SHA384 | 2 | SHA384哈希算法。 |
| SHA512 | 3 | SHA512哈希算法。 |

## DataSetSize

枚举隐私协议支持的数据集大小。数据集大小定义单个结果密文可以包含的比较次数，生成的结果密文总数由⌈elements.size/dataSetSize⌉决定。

请根据隐私搜索中元素的数量与每个结果密文可接受的大小选择合适的取值。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIZE\_128 | 0 | 单个结果密文可以包含128次比较。 |
| SIZE\_256 | 1 | 单个结果密文可以包含256次比较。 |
| SIZE\_512 | 2 | 单个结果密文可以包含512次比较。 |

## ProtocolType

隐私协议类型的枚举，决定了隐私保护搜索的算法。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PSI\_PROTOCOL | 0 | PSI协议（隐私集合求交）。判断目标元素是否存在于数据集中，不泄露元素与数据集内容。 |
| PIR\_PROTOCOL | 1 | PIR协议（隐私信息检索）。检索数据集中与目标键匹配的附加值，不泄露键与检索到的值。 |

## PrivacyProtocol

定义隐私协议配置，包括数据集大小与协议类型。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSetSize | [DataSetSize](js-apis-privacycomputation.md#datasetsize) | 否 | 否 | 隐私协议的数据集大小。 |
| protocolType | [ProtocolType](js-apis-privacycomputation.md#protocoltype) | 否 | 否 | 隐私计算的协议类型。 |

## TargetElement

定义隐私计算的目标元素，包括原始元素数据与可选的哈希算法。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| elemData | Uint8Array | 否 | 否 | 要搜索的目标元素的原始数据。长度必须不大于1KB。 |
| hashAlg | [HashAlg](js-apis-privacycomputation.md#hashalg) | 否 | 是 | 用于对目标元素计算的哈希算法。未显式指定哈希算法时，默认为NONE。 |

## Element

定义隐私搜索使用的数据集元素。每个元素包含一个用于匹配的键、可选的哈希算法，以及用于PIR协议检索的可选附加值。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| elemKey | Uint8Array | 否 | 否 | 数据集元素的键，用于与隐私目标进行匹配。长度必须不大于1KB。 |
| hashAlg | [HashAlg](js-apis-privacycomputation.md#hashalg) | 否 | 是 | 用于对元素键计算的哈希算法。未显式指定哈希算法时，默认为NONE。 |
| elemValue | Uint8Array | 否 | 是 | 与元素键关联的附加值。  **说明：**  仅在PIR协议中使用，当找到匹配项时检索该附加值。  未指定时元素只支持键匹配，不支持值检索。 |

## PrivacySearchResult

定义隐私搜索操作的结果，包含结果密文与可选的附加值密文。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCipherText | Uint8Array[] | 否 | 否 | 隐私搜索生成的结果密文数组。可通过[getSearchResult](js-apis-privacycomputation.md#privacycomputationgetsearchresult)进行解密。 |
| valueCipherText | Uint8Array[] | 否 | 是 | 使用PIR协议进行隐私搜索时生成的值密文数组。这些密文包含与匹配元素相关的加密值。  **说明：** 仅PIR协议下存在，PSI协议不读取该值。 |

## SearchResult

定义解密后的最终搜索结果，指示是否找到匹配项以及与匹配元素关联的可选附加值。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| matchedResult | boolean | 否 | 否 | 指示是否在数据集中找到隐私目标。true表示找到匹配项；false表示未匹配。 |
| attachedValues | Uint8Array[] | 否 | 是 | 与匹配元素关联的附加值。仅当使用PIR协议且找到匹配项时返回；否则为undefined。 |

## privacyComputation.genPrivacyTarget

genPrivacyTarget(targetElement: TargetElement, privacyProtocol: PrivacyProtocol): Promise<Uint8Array>

为给定元素生成隐私目标。隐私目标是搜索元素的加密表示，可用于隐私保护搜索而不泄露原始数据。使用Promise异步回调。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetElement | [TargetElement](js-apis-privacycomputation.md#targetelement) | 是 | 要搜索的目标元素，包括原始数据与可选的哈希算法。 |
| privacyProtocol | [PrivacyProtocol](js-apis-privacycomputation.md#privacyprotocol) | 是 | 隐私协议配置，包括数据集大小与协议类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回加密的隐私目标。 |

**错误码**：

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24000001 | The service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000009 | The cryptography operation failed. |
| 24000017 | The capability is not supported. |
| 24000018 | Parameter verification failed. |

**示例**：

```ts
import { privacyComputation } from '@kit.DataProtectionKit';

async function genTarget() {
  const targetElement: privacyComputation.TargetElement = {
    elemData: new Uint8Array([0x01, 0x02, 0x03]),
    hashAlg: privacyComputation.HashAlg.SHA256
  };
  const privacyProtocol: privacyComputation.PrivacyProtocol = {
    dataSetSize: privacyComputation.DataSetSize.SIZE_512,
    protocolType: privacyComputation.ProtocolType.PSI_PROTOCOL
  };

  const privacyTarget: Uint8Array = await privacyComputation.genPrivacyTarget(targetElement, privacyProtocol);
  console.info('privacyTarget length: ' + privacyTarget.length);
}
```

## privacyComputation.privacySearch

privacySearch(privacyTarget: Uint8Array, elements: Element[], privacyProtocol: PrivacyProtocol): Promise<PrivacySearchResult>

执行隐私保护搜索。根据加密的隐私目标搜索给定的数据集元素，不向对方透露目标或数据集内容。使用Promise异步回调。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| privacyTarget | Uint8Array | 是 | 由[genPrivacyTarget](js-apis-privacycomputation.md#privacycomputationgenprivacytarget)生成的加密隐私目标。 |
| elements | [Element](js-apis-privacycomputation.md#element)[] | 是 | 要搜索的数据集元素。 |
| privacyProtocol | [PrivacyProtocol](js-apis-privacycomputation.md#privacyprotocol) | 是 | 隐私协议配置，需与生成隐私目标时一致。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[PrivacySearchResult](js-apis-privacycomputation.md#privacysearchresult)> | Promise对象，返回隐私搜索结果，包含结果密文与可选的附加值密文。 |

**错误码**：

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24000001 | The service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000009 | The cryptography operation failed. |
| 24000017 | The capability is not supported. |
| 24000018 | Parameter verification failed. |

**示例**：

```ts
import { privacyComputation } from '@kit.DataProtectionKit';

async function search(privacyTarget: Uint8Array) {
  const elements: Array<privacyComputation.Element> = [
    {
      elemKey: new Uint8Array([0x01, 0x02, 0x03]),
      hashAlg: privacyComputation.HashAlg.SHA256,
      elemValue: new Uint8Array([0xA1, 0xA2])
    },
    {
      elemKey: new Uint8Array([0x07, 0x08, 0x09]),
      hashAlg: privacyComputation.HashAlg.SHA256
    }
  ];
  const privacyProtocol: privacyComputation.PrivacyProtocol = {
    dataSetSize: privacyComputation.DataSetSize.SIZE_256,
    protocolType: privacyComputation.ProtocolType.PIR_PROTOCOL
  };

  const result: privacyComputation.PrivacySearchResult =
    await privacyComputation.privacySearch(privacyTarget, elements, privacyProtocol);
  console.info('resultCipherText count: ' + result.resultCipherText.length + ', valueCipherText count: ' + (result.valueCipherText?.length ?? 0));
}
```

## privacyComputation.getSearchResult

getSearchResult(privacySearchResult: PrivacySearchResult, privacyProtocol: PrivacyProtocol): Promise<SearchResult>

获取隐私搜索结果与最终搜索结果。解密[privacySearch](js-apis-privacycomputation.md#privacycomputationprivacysearch)返回的结果密文，获取最终匹配结果与可选的附加值。使用Promise异步回调。

**起始版本**：26.0.1

**元服务API**：从API版本26.0.1开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.Asset

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| privacySearchResult | [PrivacySearchResult](js-apis-privacycomputation.md#privacysearchresult) | 是 | [privacySearch](js-apis-privacycomputation.md#privacycomputationprivacysearch)返回的结果。 |
| privacyProtocol | [PrivacyProtocol](js-apis-privacycomputation.md#privacyprotocol) | 是 | 隐私协议配置，需与生成隐私目标时一致。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[SearchResult](js-apis-privacycomputation.md#searchresult)> | Promise对象，返回最终搜索结果。matchedResult指示是否命中；attachedValues为命中项附加值（仅PIR协议且命中时返回）。 |

**错误码**：

以下错误码的详细介绍请参见[关键资产存储服务错误码](errorcode-asset.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 24000001 | The service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000009 | The cryptography operation failed. |
| 24000017 | The capability is not supported. |
| 24000018 | Parameter verification failed. |

**示例**：

```ts
import { privacyComputation } from '@kit.DataProtectionKit';

async function getResult(searchResult: privacyComputation.PrivacySearchResult) {
  const privacyProtocol: privacyComputation.PrivacyProtocol = {
    dataSetSize: privacyComputation.DataSetSize.SIZE_256,
    protocolType: privacyComputation.ProtocolType.PIR_PROTOCOL
  };

  const result: privacyComputation.SearchResult =
    await privacyComputation.getSearchResult(searchResult, privacyProtocol);
  if (result.matchedResult) {
    console.info('matched, attachedValues count: ' + (result.attachedValues?.length ?? 0));
  } else {
    console.info('not matched');
  }
}
```
