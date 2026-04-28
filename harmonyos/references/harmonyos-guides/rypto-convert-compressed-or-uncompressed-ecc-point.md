---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rypto-convert-compressed-or-uncompressed-ecc-point
title: 使用ECC压缩/非压缩点格式转换(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 使用ECC压缩/非压缩点格式转换(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:dfc0b68da976ba477990fd30d698e248af3077f90615b2961852148cfe99fb83
---

支持将压缩/非压缩的点数据转换为Point对象，用于密钥对象生成；也支持将Point对象转换为压缩/非压缩的点数据。

ECC的算法规格请查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

通过传入字符串参数format，可指定需要获取的点数据格式。如果需要获取压缩格式，则指定format为："COMPRESSED"；需要获取非压缩格式，则指定format为："UNCOMPRESSED"。

## 指定非压缩点数据转换为压缩点数据

1. 指定Uint8Array类型的ECC非压缩点数据，调用[ECCKeyUtil.convertPoint](../harmonyos-references/js-apis-cryptoframework.md#convertpoint12)，构造[Point](../harmonyos-references/js-apis-cryptoframework.md#point10)对象，用于生成点数据。
2. 调用[ECCKeyUtil.getEncodedPoint](../harmonyos-references/js-apis-cryptoframework.md#getencodedpoint12)，获取压缩点数据。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. function eccPointUncompressedToCompressed() {
4. let pkData =
5. new Uint8Array([4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
6. 157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242,
7. 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
8. let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData);
9. console.info('convertPoint result: success.');
10. let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'COMPRESSED');
11. console.info('returnData: ' + returnData);
12. }
```

[CompressedPointData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ECCCompressPublicKeyFormatConversion/entry/src/main/ets/pages/CompressedPointData.ets#L16-L31)

## 指定压缩点数据获取密钥对象

1. 指定Uint8Array类型的ECC压缩点数据，调用[ECCKeyUtil.convertPoint](../harmonyos-references/js-apis-cryptoframework.md#convertpoint12)，得到[Point](../harmonyos-references/js-apis-cryptoframework.md#point10)对象，用于密钥对象生成。
2. 调用[ECCKeyUtil.genECCCommonParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#genecccommonparamsspec11)，指定曲线名'NID\_brainpoolP256r1'，生成ECC的非对称公共密钥参数。
3. 构造[ECCPubKeySpec](../harmonyos-references/js-apis-cryptoframework.md#eccpubkeyspec10)对象，用于指定ECC算法中公钥包含的参数。ECCPubKeySpec是AsyKeySpec的子类。需要通过参数algName指定算法'ECC'；指定密钥参数类型[AsyKeySpecType.PUBLIC\_KEY\_SPEC](../harmonyos-references/js-apis-cryptoframework.md#asykeyspectype10)，参数pk指定为得到的point对象。
4. 通过得到的公钥参数，调用[createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10)，创建非对称密钥生成器（AsyKeyGeneratorBySpec）。
5. 调用[AsyKeyGeneratorBySpec.generatePubKey](../harmonyos-references/js-apis-cryptoframework.md#generatepubkey10)，得到指定的公钥。
6. 调用[ECCKeyUtil.getEncodedPoint](../harmonyos-references/js-apis-cryptoframework.md#getencodedpoint12)，得到非压缩点数据。
7. 调用[PubKey.getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10)，获取ECC算法中公钥pk的x坐标。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. async function eccPointCompressedToPoint() {
4. let pkData =
5. new Uint8Array([2, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
6. 157, 111, 40, 217, 215, 148, 120, 224, 205, 82]);
7. let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData);
8. console.info('convertPoint result: success.');
9. let eccCommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_brainpoolP256r1');
10. let eccPubKeySpec: cryptoFramework.ECCPubKeySpec = {
11. algName: 'ECC',
12. specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC,
13. params: eccCommonParamsSpec,
14. pk: returnPoint
15. };
16. let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(eccPubKeySpec);
17. let pubKey = await generatorBySpec.generatePubKey();
18. let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'UNCOMPRESSED');
19. console.info('returnData: ' + returnData);
20. let eccPkX = pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
21. console.info('returnPoint x data: ' + returnPoint.x);
22. console.info('ECC_PK_X_BN: ' + eccPkX);
23. }
```

[GetKeyObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ECCCompressPublicKeyFormatConversion/entry/src/main/ets/pages/GetKeyObject.ets#L16-L45)
