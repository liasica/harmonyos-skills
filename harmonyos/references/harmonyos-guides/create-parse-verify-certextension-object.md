---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-parse-verify-certextension-object
title: 证书扩展信息对象的创建、解析和校验
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书扩展信息对象的创建、解析和校验
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e0f66fcc8f2a4173ac02d17ab58a80a2f55e5cd9fd8b1af24101a6a2363eab0
---

以获取证书指定OID域段，并判断是否为CA证书为例，完成证书扩展信息对象的创建、解析和校验。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 解析证书扩展域段数据，调用[cert.createCertExtension](../harmonyos-references/js-apis-cert.md#certcreatecertextension10)创建证书扩展域段对象。
3. 调用[CertExtension.getEntry](../harmonyos-references/js-apis-cert.md#getentry10)获取指定OID证书扩展域段信息。比如，证书扩展域段对象标识符列表，根据对象标识符获取具体数据等。
4. 调用[CertExtension.checkCA](../harmonyos-references/js-apis-cert.md#checkca10)判断证书是否为CA证书。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. // 证书扩展数据，以下只是一个示例。需要根据具体业务来赋值。
6. let extData = new Uint8Array([
7. 0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D,
8. 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30, 0x03,
9. 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55,
10. 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03,
11. 0x02, 0x01, 0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55,
12. 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C,
13. 0x9B, 0xDB, 0x25, 0x49, 0xB3, 0xF1, 0x7C, 0x86,
14. 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0,
15. 0xD9, 0xE4
16. ]);

18. // 证书扩展示例
19. function certExtensionSample(): void {
20. let textEncoder = new util.TextEncoder();
21. let encodingBlob: cert.EncodingBlob = {
22. data: extData,
23. // 证书扩展格式，目前仅支持DER格式。
24. encodingFormat: cert.EncodingFormat.FORMAT_DER
25. };

27. // 创建一个证书扩展实例。
28. cert.createCertExtension(encodingBlob, (err, certExtension) => {
29. if (err != null) {
30. // 证书扩展实例创建失败。
31. console.error(`createCertExtension failed, errCode:${err.code}, errMsg:${err.message}`);
32. return;
33. }
34. // 证书扩展实例创建成功。
35. console.info('createCertExtension result: success.');

37. try {
38. // 根据OID获取证书扩展信息。
39. let oidData = '2.5.29.14';
40. let oid: cert.DataBlob = {
41. data: textEncoder.encodeInto(oidData),
42. }
43. let entry = certExtension.getEntry(cert.ExtensionEntryType.EXTENSION_ENTRY_TYPE_ENTRY, oid);

45. // 检查证书是否为CA证书。
46. let pathLen = certExtension.checkCA();
47. console.info('checkCA result: success.');
48. } catch (err) {
49. let e: BusinessError = err as BusinessError;
50. console.error(`operation failed, errCode:${e.code}, errMsg:${e.message}`);
51. }
52. });
53. }
```

[CreateParseVerifyCertextensionObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateParseVerifyCertextensionObject.ets#L17-L74)
