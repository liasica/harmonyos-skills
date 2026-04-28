---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-ciphertext-conversion
title: 使用SM2密文格式转换(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM2密文格式转换(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58a1c82bbcbccfcc7dec1a5f1b4d4d5c0dcaf3168e82b5bb6aa9a5f2551cbf7e
---

当前支持的SM2密文格式为国密标准的ASN.1格式，其中各参数组合顺序为C1C3C2，具体参数含义请参考[转换SM2密文格式](crypto-asym-encrypt-decrypt-spec.md#转换sm2密文格式)。

开发者可指定SM2密文的参数，将其转换成符合国密标准的ASN.1格式密文。反之，也可以从国密标准的ASN.1格式密文中取出具体的SM2密文参数，便于开发者自行组合成其他格式的SM2密文。

**指定密文参数，生成标准ASN.1密文**

1. 构造[SM2CipherTextSpec](../harmonyos-references/js-apis-cryptoframework.md#sm2ciphertextspec12)对象，用于指定SM2密文参数。如果开发者使用的不是国密标准的ASN.1格式密文，需自行提取所需要的参数。
2. 调用[genCipherTextBySpec](../harmonyos-references/js-apis-cryptoframework.md#genciphertextbyspec12)，将SM2CipherTextSpec对象传入，生成符合国密标准的ASN.1格式的SM2密文。
3. 生成的密文可直接使用cryptoFramework进行SM2解密。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. function testGenCipherTextBySpec() {
4. let spec: cryptoFramework.SM2CipherTextSpec = {
5. xCoordinate: BigInt('20625015362595980457695435345498579729138244358573902431560627260141789922999'),
6. yCoordinate: BigInt('48563164792857017065725892921053777369510340820930241057309844352421738767712'),
7. cipherTextData: new Uint8Array([100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123]),
8. hashData: new Uint8Array([87, 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201,
9. 111, 143, 115, 169, 125, 128, 42, 157, 31, 114, 198, 109, 244]),
10. }
11. // 此处的data可直接使用cryptoFramework进行SM2解密
12. let data = cryptoFramework.SM2CryptoUtil.genCipherTextBySpec(spec, 'C1C3C2');
13. console.info('genCipherTextBySpec result: success.');
14. }
```

[CreateASN.1Ciphertext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM2/entry/src/main/ets/pages/sm2/CreateASN.1Ciphertext.ets#L16-L32)

**从标准ASN.1密文中，获取密文参数**

1. 准备符合国密标准的ASN.1格式的SM2密文。
2. 调用[getCipherTextSpec](../harmonyos-references/js-apis-cryptoframework.md#genciphertextbyspec12)，从标准密文中，获取具体的SM2密文参数。
3. 根据业务需要，自行拼接SM2密文参数，形成其他格式的SM2密文。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. function testGetCipherTextSpec() {
4. let cipherTextArray =
5. new Uint8Array([48, 118, 2, 32, 45, 153, 88, 82, 104, 221, 226, 43, 174, 21, 122, 248, 5, 232, 105, 41, 92, 95, 102,
6. 224, 216, 149, 85, 236, 110, 6, 64, 188, 149, 70, 70, 183, 2, 32, 107, 93, 198, 247, 119, 18, 40, 110, 90, 156,
7. 193, 158, 205, 113, 170, 128, 146, 109, 75, 17, 181, 109, 110, 91, 149, 5, 110, 233, 209, 78, 229, 96, 4, 32, 87,
8. 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201, 111, 143, 115, 169, 125, 128,
9. 42, 157, 31, 114, 198, 109, 244, 4, 14, 100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123]);
10. let cipherText: cryptoFramework.DataBlob = { data: cipherTextArray };
11. let spec: cryptoFramework.SM2CipherTextSpec = cryptoFramework.SM2CryptoUtil.getCipherTextSpec(cipherText, 'C1C3C2');
12. console.info('getCipherTextSpec result: success.');
13. }
```

[ObtainCiphertext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM2/entry/src/main/ets/pages/sm2/ObtainCiphertext.ets#L16-L31)
