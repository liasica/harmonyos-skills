---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-data-format-conversion
title: SM2签名数据格式转换(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > SM2签名数据格式转换(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a3ca2f78365e84782de882094c533666e068e4d044adfc45f8ecbfe563e94ab
---

当前支持DER格式与（r、s）格式互转的能力。

开发者可指定SM2签名数据，将其转换成DER格式密文。反之，也可以从DER格式密文中取出具体的SM2签名数据。

**指定密文参数，转换为DER格式**

1. 构造[EccSignatureSpec](../harmonyos-references/js-apis-cryptoframework.md#eccsignaturespec20)对象，用于指定SM2密文参数。
2. 调用[genEccSignature](../harmonyos-references/js-apis-cryptoframework.md#geneccsignature20)，将EccSignatureSpec对象传入，转换为DER格式的SM2密文。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function testSm2SignDataRsToDer() {
5. try {
6. let spec: cryptoFramework.EccSignatureSpec = {
7. r: BigInt('97726608965854271693043443511967021777934035174185659091642456228829830775155'),
8. s: BigInt('23084224202834231287427338597254751764391338275617140205467537273296855150376'),
9. };

11. let data = cryptoFramework.SignatureUtils.genEccSignature(spec);
12. console.info('genEccSignature result: success.');
13. console.info('data = ' + data);
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. console.error(`ecc failed: errCode: ${e.code}, message: ${e.message}`);
17. }
18. }
```

[sm2\_sign\_data\_rs\_to\_der.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/sm2_data_format_convertion/sm2_sign_data_rs_to_der.ets#L15-L34)

**指定DER格式，转换为（r、s）格式**

1. 指定DER格式的SM2密文参数。
2. 调用[genEccSignatureSpec](../harmonyos-references/js-apis-cryptoframework.md#geneccsignaturespec20)，将DER格式数据传入，转换为(r、s)格式的SM2密文。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function testSm2SignDataDerToRs() {
5. try {
6. let data =
7. new Uint8Array([48, 69, 2, 33, 0, 216, 15, 76, 238, 158, 165, 108, 76, 72, 63, 115, 52, 255, 51, 149, 54, 224,
8. 179, 49, 225, 70, 36, 117, 88, 154, 154, 27, 194, 161, 3, 1, 115, 2, 32, 51, 9, 53, 55, 248, 82, 7, 159, 179,
9. 144, 57, 151, 195, 17, 31, 106, 123, 32, 139, 219, 6, 253, 62, 240, 181, 134, 214, 107, 27, 230, 175, 40]);
10. let spec: cryptoFramework.EccSignatureSpec = cryptoFramework.SignatureUtils.genEccSignatureSpec(data);
11. console.info('genEccSignatureSpec result: success.');
12. } catch (err) {
13. let e: BusinessError = err as BusinessError;
14. console.error(`ecc failed: errCode: ${e.code}, message: ${e.message}`);
15. }
16. }
```

[sm2\_sign\_data\_der\_to\_rs.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/sm2_data_format_convertion/sm2_sign_data_der_to_rs.ets#L15-L32)
