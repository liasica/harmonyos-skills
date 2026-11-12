---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/privacy-computation-pir
title: 使用PIR协议进行隐私信息检索
breadcrumb: 指南 > 系统 > 安全 > Data Protection Kit（数据保护服务） > 隐私计算 > 使用PIR协议进行隐私信息检索
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:35+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fe461bddcd1551ba7f568ed5d37e7a6ba2a90a8e8479c3d735b652b9c33cb795
---

## 场景介绍

PIR协议（隐私信息检索，Private Information Retrieval）适用于在不暴露查询条件的前提下从对方数据集中获取匹配项附加值的场景，例如根据标识查询配置信息、根据凭证查询权益信息等。

通过PIR协议进行隐私信息检索，包含生成隐私目标[genPrivacyTarget](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgenprivacytarget)、隐私搜索[privacySearch](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationprivacysearch)、获取搜索结果[getSearchResult](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgetsearchresult)三个步骤。PIR协议在命中时返回匹配元素的附加值。

## 开发步骤

1. 接口所需模块导入。

   ```typescript
   import { privacyComputation } from '@kit.DataProtectionKit';
   ```
2. 发起端生成隐私目标。

   构造[TargetElement](../harmonyos-references/js-apis-privacycomputation.md#targetelement)（目标元素原始数据与哈希算法）和[PrivacyProtocol](../harmonyos-references/js-apis-privacycomputation.md#privacyprotocol)（协议类型设为PIR\_PROTOCOL），调用[genPrivacyTarget](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgenprivacytarget)生成隐私目标。

   ```typescript
   const targetElement: privacyComputation.TargetElement = {
     elemData: new Uint8Array([0x01, 0x02, 0x03]),
     hashAlg: privacyComputation.HashAlg.SHA256
   };
   const privacyProtocol: privacyComputation.PrivacyProtocol = {
     dataSetSize: privacyComputation.DataSetSize.SIZE_256,
     protocolType: privacyComputation.ProtocolType.PIR_PROTOCOL
   };
   const privacyTarget: Uint8Array = await privacyComputation.genPrivacyTarget(targetElement, privacyProtocol);
   ```
3. 响应端执行隐私搜索。

   构造[Element](../harmonyos-references/js-apis-privacycomputation.md#element)数组（数据集元素，包含键、哈希算法与附加值elemValue），连同隐私目标和协议配置，调用[privacySearch](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationprivacysearch)执行隐私搜索。elemValue为命中时返回的附加值，仅在PIR协议中使用。

   ```typescript
   const elements: privacyComputation.Element[] = [
     {
       elemKey: new Uint8Array([0x01, 0x02, 0x03]),
       hashAlg: privacyComputation.HashAlg.SHA256,
       elemValue: new Uint8Array([0xA1, 0xA2])
     },
     {
       elemKey: new Uint8Array([0x07, 0x08, 0x09]),
       hashAlg: privacyComputation.HashAlg.SHA256,
       elemValue: new Uint8Array([0xB1, 0xB2])
     }
   ];
   const searchResult: privacyComputation.PrivacySearchResult =
     await privacyComputation.privacySearch(privacyTarget, elements, privacyProtocol);
   ```
4. 发起端获取最终结果。

   将[privacySearch](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationprivacysearch)返回的结果传入[getSearchResult](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgetsearchresult)，解密得到[SearchResult](../harmonyos-references/js-apis-privacycomputation.md#searchresult)。matchedResult指示是否命中；命中时attachedValues返回匹配元素的附加值。

   ```typescript
   const result: privacyComputation.SearchResult =
     await privacyComputation.getSearchResult(searchResult, privacyProtocol);
   console.info('matched: ' + result.matchedResult);
   if (result.matchedResult && result.attachedValues) {
     console.info('attachedValues count: ' + result.attachedValues.length);
   }
   ```

**说明** 

* privacyProtocol需在三个接口间保持一致。
* 若调用异常，可通过try/catch捕获BusinessError，错误码详见[关键资产存储服务错误码](../harmonyos-references/errorcode-asset.md)。
