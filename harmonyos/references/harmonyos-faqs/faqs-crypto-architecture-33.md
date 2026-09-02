---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-33
title: 如何解决ArkTS SM2签名数据服务端无法验证问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何解决ArkTS SM2签名数据服务端无法验证问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ba42bc357dfe578170035a26fd1c0bb405c3ca6a8bf7944d0ffa6cf6f324019c
---

## 问题现象

在ArkTS中使用SM2签名的数据，在其他平台进行验签时，验签失败。

原文：This is Sign test plan。

公钥：3059301306072a8648ce3d020106082a811ccf5501822d03420004974399fbf088c7c90bd2df21153d1e0d0a96b26026c3c8ad2374f63b9f04c1a3c5a19813d269653b4231a0d162d57ad35dbe0d9337fb6d89d1b404005f162b0e。

签名：3059301306072a8648ce3d020106082a811ccf5501822d03420004974399fbf088c7c90bd2df21153d1e0d0a96b26026c3c8ad2374f63b9f04c1a3c5a19813d269653b4231a0d162d57ad35dbe0d9337fb6d89d1b404005f162b0e。

## 背景知识

* [SM2](../harmonyos-guides/crypto-sign-sig-verify-overview.md#sm2)数字签名算法，是基于椭圆曲线的非对称签名验签算法。
* DER格式：在SM2数字签名中，DER格式是签名值（r, s）的标准编码方式，遵循ASN.1标准。这是一种结构化的二进制编码格式，用于确保签名数据的完整性和可解析性。ArkTS中使用SM2签名完的数据通常是DER格式，而其他端通常是裸签名，即直接拼接r||s（64字节）。
* 压缩格式与非压缩格式：SM2公钥，通常指的是椭圆曲线上的一个点。在非压缩格式中，公钥由一个前缀0x04加上X坐标和Y坐标组成，所以总长度为1+32+32=65字节（十六进制表示为130个字符，包括04前缀）。而压缩格式的公钥只包括X坐标和一个前缀（0x02或0x03），其中前缀由Y坐标的奇偶性决定，所以总长度为1+32=33字节（十六进制表示为66个字符），两端的公钥格式不一致。

## 问题定位

1. **确认加解密流程**：

   针对服务端与客户端加密结果不一致的问题，先验证同一端加签、验签流程无误，以此确定是否为跨端的问题。
2. **确认编码格式**：

   加签验签过程中有两处编码格式需要检查服务端与客户端是否一致：公钥格式、签名格式。

## 分析结论

1. 在ArkTS端和服务端独立进行加签验签操作，验证都成功，说明验签失败是跨端的问题。
2. 分析公钥格式，ArkTS端[getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)生成的公钥转换成十六进制后，为十六进制编码的X.509格式的公钥，而服务端生成的公钥是裸椭圆曲线公钥，格式为64字节的X||Y坐标拼接（没有0x04前缀），两端公钥格式不一致。
3. 分析签名格式，ArkTS端[signSync](../harmonyos-references/js-apis-cryptoframework.md#signsync12)生成的签名为DER格式，而服务端生成的签名格式为裸签名，两端签名格式不一致。

## 修改建议

1. 将ArkTS端[getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)生成的公钥转换成裸公钥的格式：通过[getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10)方法，指定参数[AsyKeySpecItem](../harmonyos-references/js-apis-cryptoframework.md#asykeyspecitem10)为ECC\_PK\_X\_BN和ECC\_PK\_Y\_BN分别获取公钥的X坐标和Y坐标，然后将坐标转换成十六进制数据，数据不足64位补充前导零，将处理完的X和Y拼接起来，最后补充前缀04即可，代码实现为：

   ```ts
   // 将压缩公钥转换成非压缩公钥
   function convertPublicKeyFormat(keyPair: cryptoFramework.KeyPair): string {
     let x = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
     let y = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
     let pk = '04' + x.toString(16).padStart(64, '0') + y.toString(16).padStart(64, '0');
     return pk;
   }
   ```
2. ArkTS中有[genEccSignatureSpec](../harmonyos-references/js-apis-cryptoframework.md#geneccsignaturespec20)方法可以从ASN1 DER格式的SM2签名数据获取r和s，获取到r和s后拼接起来即可，最终转换完成的数据为64字节二进制数据。为了方便调试、日志配置，通常还需要转换成16进制的数据，DER格式签名转换为裸签名代码如下：

   ```ts
   function bigIntTo32Bytes(bn: bigint): Uint8Array {
     let hex = bn.toString(16).padStart(64, '0');
     let bytes = new Uint8Array(32);
     for (let i = 0; i < 64; i += 2) {
       bytes[i / 2] = parseInt(hex.slice(i, i + 2), 16);
     }
     return bytes;
   }

   function convertSignFormat(signData: cryptoFramework.DataBlob): string {
     let spec: cryptoFramework.EccSignatureSpec = cryptoFramework.SignatureUtils.genEccSignatureSpec(signData.data);
     // 拼接r||s裸签名
     let rBytes = bigIntTo32Bytes(spec.r);
     let sBytes = bigIntTo32Bytes(spec.s);
     let rawSignature = new Uint8Array(64);
     rawSignature.set(rBytes, 0); // 0-31位写入r
     rawSignature.set(sBytes, 32); // 32-63位写入s
     return uint8ArrayToHexStr(rawSignature);
   }
   ```

   完整代码如下：

   ```ts
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { buffer } from '@kit.ArkTS';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const DOMAIN = 0x0000;
   const FLAG = 'SM2_CRYPTO';
   const rawMsg = 'This is Sign test plan';
   let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(rawMsg, 'utf-8').buffer) };

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Button('加签&验签').onClick(() => {
           main();
         });
       };
     }
   }

   // uint8Array转16进制工具函数
   function uint8ArrayToHexStr(array: Uint8Array): string {
     let result = '';
     for (let i = 0; i < array.length; i++) {
       // 将字节转为16进制并补齐两位，确保格式统一
       const hexByte = array[i].toString(16).padStart(2, '0');
       result += hexByte;
     }
     return result;
   }

   function signMessagePromise(priKey: cryptoFramework.PriKey) {
     let signAlg = 'SM2_256|SM3';
     let signer = cryptoFramework.createSign(signAlg);
     signer.initSync(priKey);
     let signData = signer.signSync(input);
     return signData;
   }

   function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
     let verifyAlg = 'SM2_256|SM3';
     let verifier = cryptoFramework.createVerify(verifyAlg);
     verifier.initSync(pubKey);
     let res = verifier.verifySync(input, signMessageBlob);
     return res;
   }

   function bigIntTo32Bytes(bn: bigint): Uint8Array {
     let hex = bn.toString(16).padStart(64, '0');
     let bytes = new Uint8Array(32);
     for (let i = 0; i < 64; i += 2) {
       bytes[i / 2] = parseInt(hex.slice(i, i + 2), 16);
     }
     return bytes;
   }

   function convertSignFormat(signData: cryptoFramework.DataBlob): string {
     let spec: cryptoFramework.EccSignatureSpec = cryptoFramework.SignatureUtils.genEccSignatureSpec(signData.data);
     // 拼接r||s裸签名
     let rBytes = bigIntTo32Bytes(spec.r);
     let sBytes = bigIntTo32Bytes(spec.s);
     let rawSignature = new Uint8Array(64);
     rawSignature.set(rBytes, 0); // 0-31位写入r
     rawSignature.set(sBytes, 32); // 32-63位写入s
     return uint8ArrayToHexStr(rawSignature);
   }

   // 将压缩公钥转换成非压缩公钥
   function convertPublicKeyFormat(keyPair: cryptoFramework.KeyPair): string {
     let x = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
     let y = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
     let pk = '04' + x.toString(16).padStart(64, '0') + y.toString(16).padStart(64, '0');
     return pk;
   }

   async function main() {
     let keyGenAlg = 'SM2_256';
     try {
       let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
       let keyPair = generator.generateKeyPairSync();
       let signData = signMessagePromise(keyPair.priKey);
       let verifyResult = verifyMessagePromise(signData, keyPair.pubKey);
       let signedData = convertSignFormat(signData);
       hilog.info(DOMAIN, FLAG, `原文：${rawMsg}`);
       hilog.info(DOMAIN, FLAG, `压缩公钥：${uint8ArrayToHexStr(keyPair.pubKey.getEncoded().data)}`);
       hilog.info(DOMAIN, FLAG, `非压缩公钥：${convertPublicKeyFormat(keyPair)}`);
       hilog.info(DOMAIN, FLAG, `私钥：${uint8ArrayToHexStr(keyPair.priKey.getEncoded().data)}`);
       hilog.info(DOMAIN, FLAG, `DER签名：${uint8ArrayToHexStr(signData.data)}`);
       hilog.info(DOMAIN, FLAG, `裸签名：${signedData}`);
       if (verifyResult === true) {
         hilog.info(DOMAIN, FLAG, 'verify success');
       } else {
         hilog.error(DOMAIN, FLAG, 'verify success');
       }
     } catch (e) {
       hilog.info(DOMAIN, FLAG, `error：${e}`);
     }
   }
   ```
