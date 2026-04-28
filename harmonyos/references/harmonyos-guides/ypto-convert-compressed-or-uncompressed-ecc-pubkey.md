---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ypto-convert-compressed-or-uncompressed-ecc-pubkey
title: 使用ECC压缩/非压缩公钥格式转换(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 使用ECC压缩/非压缩公钥格式转换(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e70014dbcd817b7dfbdfa40aaeaded63e6404b111ee79a4b8748f40a86aaddea
---

可通过指定ECC公钥数据生成公钥对象（PubKey），也可以从公钥对象（PubKey）中获取ECC公钥数据。

当前仅支持满足X509规范的ECC算法压缩和非压缩格式的公钥数据。此处的公钥数据应当是完整的X509公钥，对于只使用点数据的情况，请参考[使用ECC压缩/非压缩点格式转换](rypto-convert-compressed-or-uncompressed-ecc-point.md)。

ECC的算法规格请查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

通过传入字符串参数format，可指定需要获取的ECC公钥数据格式。如果需要获取满足X509规范的压缩格式数据，则指定format为："X509|COMPRESSED"；需要获取非压缩格式，则指定format为："X509|UNCOMPRESSED"。

## 指定非压缩公钥数据转换为压缩公钥数据

1. 将Uint8Array类型的ECC非压缩公钥数据封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象。

   公钥和私钥可只传入其中一个。此处示例传入非压缩公钥。
2. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'ECC\_BrainPoolP256r1'，创建密钥算法为ECC、密钥长度为256位的非对称密钥生成器（AsyKeyGenerator）。
3. 调用[AsyKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)，传入封装后的DataBlob对象，生成非对称密钥对象（KeyPair）。
4. 调用[PubKey.getEncodedDer](../harmonyos-references/js-apis-cryptoframework.md#getencodedder12)，设置参数为'X509|COMPRESSED'，获取压缩公钥数据的字节流。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. async function eccPubUncompressedToCompressed() {
4. let pkData =
5. new Uint8Array([48, 90, 48, 20, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 9, 43, 36, 3, 3, 2, 8, 1, 1, 7, 3, 66, 0, 4,
6. 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111, 40,
7. 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242, 206, 200, 98,
8. 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
9. let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
10. let generator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
11. let keyPair = await generator.convertKey(pubKeyBlob, null);
12. let returnBlob = keyPair.pubKey.getEncodedDer('X509|COMPRESSED');
13. console.info('returnBlob data: ' + returnBlob.data);
14. }
```

[SpecifyUncompressedPublicKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ECCCompressPublicKeyFormatConversion/entry/src/main/ets/pages/SpecifyUncompressedPublicKey.ets#L16-L31)
