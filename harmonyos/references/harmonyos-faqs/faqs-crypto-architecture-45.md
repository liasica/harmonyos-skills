---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-45
title: 如何实现SM4加解密工具
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何实现SM4加解密工具
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:35a85d44592797309ce4c6e939c301a5278b14a35e021a5e655e305c7c5a9d7e
---

## 问题现象

如何实现一个SM4加解密工具，例如其中入参symAlgName的值为SM4\_128，symKeyData的长度是32位，请提供一个SM4加解密Demo。

## 背景知识

* 在数据存储或传输场景中，可以使用加解密操作用于保证数据的机密性，防止敏感数据泄露，加解密开发可参考[加解密开发指导](../harmonyos-guides/crypto-encrypt-decrypt-dev.md)。
* [算法库](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md)当前提供了[SM4加解密](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#sm4)常用的7种加密模式：ECB、CBC、CTR、OFB、CFB、CFB128和GCM。
* 由于SM4为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的填充模式进行数据填充。

## 解决方案

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 30 }) {
      Text('SM4加密')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(async () => {
          const symAlgName = 'SM4_128';
          const sKey: string = '9f35eda67432c4ae3892305801b9d0b6';
          const symKeyData = buffer.from(sKey, 'hex');
          let symKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(symKeyData.buffer) };
          try {
            let aesGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
            let symKey = await aesGenerator.convertKey(symKeyBlob);
            console.info(`wsf: sm4 转密钥成功`);
            let plainText: cryptoFramework.DataBlob =
              { data: new Uint8Array(buffer.from('This is a test', 'utf-8').buffer) };
            const cipher = cryptoFramework.createCipher('SM4_128|ECB|PKCS7');
            await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
            const encryptData = await cipher.doFinal(plainText);
            if (encryptData){
              console.info(`wsf: 加密成功`);
            }
          } catch (e) {
            console.error(`wsf: 转密钥报错 e = ${e.code} ${e.message}`);
          }
        })
      Text('SM4解密')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(async () => {
          const symAlgName = 'SM4_128';
          const sKey: string = '9f35eda67432c4ae3892305801b9d0b6';
          const symKeyData = buffer.from(sKey, 'hex');
          let symKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(symKeyData.buffer) };
          try {
            let aesGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
            let symKey = await aesGenerator.convertKey(symKeyBlob);
            let arr = [186, 255, 20, 91, 43, 218, 215, 77, 185, 100, 22, 186, 42, 178, 121, 45];
            let dataAad = new Uint8Array(arr);
            let encryptData: cryptoFramework.DataBlob = { data: dataAad };
            let decoder = cryptoFramework.createCipher('SM4_128|ECB|PKCS7');
            await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
            let decryptData = await decoder.doFinal(encryptData);
            console.info(`wsf: 解密成功 ${buffer.from(decryptData.data).toString()}`);
          } catch (e) {
            console.error(`wsf: 转密钥报错 e = ${e.code} ${e.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
