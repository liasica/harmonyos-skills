---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/privacy-computation-psi
title: 使用PSI协议进行隐私集合求交
breadcrumb: 指南 > 系统 > 安全 > Data Protection Kit（数据保护服务） > 隐私计算 > 使用PSI协议进行隐私集合求交
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:35+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:405bcb62c3f745dbcfed584b5d0af1993bdbb665dfe43d6ff70abfa591c74c79
---

## 场景介绍

PSI协议（隐私集合求交，Private Set Intersection）用于在不显示元素或数据集内容的前提下，判断目标元素是否存在于对方数据集中。适用于两方不可交换明文集合的情况，例如联系人匹配、好友推荐等。

通过PSI协议进行隐私集合求交，包含生成隐私目标[genPrivacyTarget](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgenprivacytarget)、隐私搜索[privacySearch](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationprivacysearch)、获取搜索结果[getSearchResult](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgetsearchresult)三个步骤。PSI协议仅返回是否命中，不返回附加值；如需检索匹配项的附加值，请使用[PIR协议](privacy-computation-pir.md)。

## 开发步骤

1. 接口所需模块导入。

   ```typescript
   import { privacyComputation } from '@kit.DataProtectionKit';
   ```
2. 发起端生成隐私目标。

   构造[TargetElement](../harmonyos-references/js-apis-privacycomputation.md#targetelement)（目标元素原始数据与哈希算法）和[PrivacyProtocol](../harmonyos-references/js-apis-privacycomputation.md#privacyprotocol)（协议类型设为PSI\_PROTOCOL），调用[genPrivacyTarget](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgenprivacytarget)生成隐私目标。

   ```typescript
   const targetElement: privacyComputation.TargetElement = {
     elemData: new Uint8Array([0x01, 0x02, 0x03]),
     hashAlg: privacyComputation.HashAlg.SHA256
   };
   const privacyProtocol: privacyComputation.PrivacyProtocol = {
     dataSetSize: privacyComputation.DataSetSize.SIZE_512,
     protocolType: privacyComputation.ProtocolType.PSI_PROTOCOL
   };
   const privacyTarget: Uint8Array = await privacyComputation.genPrivacyTarget(targetElement, privacyProtocol);
   ```
3. 响应端执行隐私搜索。

   构造[Element](../harmonyos-references/js-apis-privacycomputation.md#element)数组（数据集元素，包含键与哈希算法），连同隐私目标和协议配置，调用[privacySearch](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationprivacysearch)执行隐私搜索。

   ```typescript
   const elements: privacyComputation.Element[] = [
     { elemKey: new Uint8Array([0x01, 0x02, 0x03]), hashAlg: privacyComputation.HashAlg.SHA256 },
     { elemKey: new Uint8Array([0x07, 0x08, 0x09]), hashAlg: privacyComputation.HashAlg.SHA256 }
   ];
   const searchResult: privacyComputation.PrivacySearchResult =
     await privacyComputation.privacySearch(privacyTarget, elements, privacyProtocol);
   ```
4. 发起端获取最终结果。

   将[privacySearch](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationprivacysearch)返回的结果传入[getSearchResult](../harmonyos-references/js-apis-privacycomputation.md#privacycomputationgetsearchresult)，解密得到[SearchResult](../harmonyos-references/js-apis-privacycomputation.md#searchresult)。matchedResult指示目标元素是否存在于数据集中。

   ```typescript
   const result: privacyComputation.SearchResult =
     await privacyComputation.getSearchResult(searchResult, privacyProtocol);
   console.info('matched: ' + result.matchedResult);
   ```

**说明** 

* privacyProtocol需在三个接口间保持一致。
* 若调用异常，可通过try/catch捕获BusinessError，错误码详见[关键资产存储服务错误码](../harmonyos-references/errorcode-asset.md)。
