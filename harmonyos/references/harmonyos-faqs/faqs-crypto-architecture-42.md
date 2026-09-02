---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-42
title: AES|GCM没有aad和authTag如何加解密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > AES|GCM没有aad和authTag如何加解密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b2bde85ee948236c07c7e038c776351b6167225d805faf257179286f5da9d6df
---

## 问题现象

HarmonyOS系统AES|GCM加解密时生成的GcmParamsSpec需要的aad和authTag参数，其他语言如java中没有这些参数。请问HarmonyOS加密的数据怎么在其他语言解密，并且其他语言加密的数据怎么在HarmonyOS解密？

## 背景知识

* [Crypto Architecture Kit](../harmonyos-guides/crypto-architecture-kit-intro.md)模块屏蔽了第三方密码学算法库实现差异的算法框架，提供加解密、签名验签、消息认证码、哈希、安全随机数、密钥派生等相关功能。
* 开发者可以参考[使用AES对称密钥（GCM模式）加解密(ArkTS)](../harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm.md)指导文档学习AES进行GCM模式加解步骤。

## 解决方案

AES加解密过程中需要生成[GcmParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#gcmparamsspec)参数，GcmParamsSpec参数值包括：

* iv初始化向量/随机数，长度为1~16字节，常用为12字节。
* aad附加认证数据，不加密但参与完整性校验，长度为0~INT\_MAX字节，常用为16字节。
* authTag认证标签，是加密过程输出的一部分，用于解密时验证数据完整性，长度为16字节。

当非HarmonyOS平台未配置aad和authTag时，可进行如下设置：

* HarmonyOS加密时，可将aad和authTag设置空字节，其他平台正常解密。
* HarmonyOS解密时，aad赋值空字节，authTag取密文的最后16个字节，最后16个字节前的数据用作待解密的密文字节。

核心示例代码参考如下：

```screen
import { buffer, util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

export class AESGCMHelper {
  private algName = 'AES128';
  private transformation = 'AES128|GCM|NoPadding';

  constructor(algName: string, transformation: string) {
    this.algName = algName;
    this.transformation = transformation;
  }

  genGcmParamsByUint8Array(iv: Uint8Array, aad: Uint8Array, authTag: Uint8Array): cryptoFramework.GcmParamsSpec {
    // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中。
    let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
      iv: { data: iv },
      aad: { data: aad },
      authTag: { data: authTag },
      algName: 'GcmParamsSpec'
    };
    return gcmParamsSpec;
  }

  async genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let aesGenerator = cryptoFramework.createSymKeyGenerator(this.algName);
    let symKey = await aesGenerator.convertKey(symKeyBlob);
    console.info('convertKey success');
    return symKey;
  }

  // 加密消息
  async encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob,
    gcmParams: cryptoFramework.GcmParamsSpec) {
    let cipher = cryptoFramework.createCipher(this.transformation);
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
    return await cipher.doFinal(plainText);
  }

  // 解密消息
  async decryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob,
    gcmParams: cryptoFramework.GcmParamsSpec) {
    let cipher = cryptoFramework.createCipher(this.transformation);
    let cipherData = plainText.data;
    let actualCipher = cipherData.slice(0, cipherData.length - 16); // 取出数据

    // 初始化解密模式
    await cipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
    return await cipher.doFinal({ data: actualCipher });
  }

  getAuthTag(plainText: cryptoFramework.DataBlob) {
    let cipherData = plainText.data;
    return cipherData.subarray(cipherData.length - 16, cipherData.length); // 取出authTag
  }

  str2Uint8Array(str: string) {
    return new Uint8Array(buffer.from(str, 'utf-8').buffer);
  }

  uint8Array2Str(uint8Array: Uint8Array) {
    return buffer.from(uint8Array).toString('utf-8');
  }
}

const base64Helper = new util.Base64Helper();
const aesGCMHelper = new AESGCMHelper('AES256', 'AES256|GCM|NoPadding');

@Entry
@Component
export struct TestPage {
  msg2encrypt: string = '';
  @State msgEncryptBase64: string = '';
  @State msg2Decrypt: string = 'HV2ZwerCyjWmfupV4UiUYtX7WpI9FF1cigAbyig8UHCb9P7c49WUVDw=';
  @State msgDecrypted: string = '';

  build() {
    Column({ space: 20 }) {
      Row() {
        Button('加密')
          .height('80%')
          .onClick(async () => {
            try {
              let keyData = aesGCMHelper.str2Uint8Array('1234567890abcdef1234567890abcdef'); // 秘钥key
              let symKey = await aesGCMHelper.genSymKeyByData(keyData);
              let iv = '123456789012'; // iv
              let aad = ''; // aad赋空值
              let authTag = ''; // authTag赋空值

              let gcmParams =
                aesGCMHelper.genGcmParamsByUint8Array(aesGCMHelper.str2Uint8Array(iv), aesGCMHelper.str2Uint8Array(aad),
                  aesGCMHelper.str2Uint8Array(authTag));

              let encryptText =
                await aesGCMHelper.encryptMessage(symKey, { data: aesGCMHelper.str2Uint8Array(this.msg2encrypt) },
                  gcmParams);
              this.msgEncryptBase64 = base64Helper.encodeToStringSync(encryptText.data);
              this.msg2Decrypt = this.msgEncryptBase64;
              console.info('encrypt plainText: ' + this.msgEncryptBase64);
            } catch (e) {
              console.error('error', e.message, e.stack);
            }
          })

        Column({ space: 10 }) {
          TextArea({ placeholder: '待加密内容', text: $$this.msg2encrypt })
            .height(60); // 待加密的信息
          Text(`加密base64:`)
          Text(this.msgEncryptBase64)
            .copyOption(CopyOptions.LocalDevice); // 加密后的信息
        }
        .height('90%')
        .width('90%')
        .justifyContent(FlexAlign.SpaceEvenly).alignItems(HorizontalAlign.Start)
      }
      .padding(10)
      .height(200)
      .width('100%')

      Row() {
        Button('解密')
          .onClick(async () => {
            try {
              let keyData = aesGCMHelper.str2Uint8Array('1234567890abcdef1234567890abcdef'); // 秘钥key
              let symKey = await aesGCMHelper.genSymKeyByData(keyData);
              let iv = '123456789012'; // iv
              let aad = ''; // aad赋空值
              let encryptMsg = base64Helper.decodeSync(this.msg2Decrypt); // 待解密的数据密文
              let authTag = aesGCMHelper.getAuthTag({ data: encryptMsg }); // authTag取密文的最后16个字节
              let gcmParams =
                aesGCMHelper.genGcmParamsByUint8Array(aesGCMHelper.str2Uint8Array(iv), aesGCMHelper.str2Uint8Array(aad),
                  authTag);

              let decryptText = await aesGCMHelper.decryptMessage(symKey, { data: encryptMsg }, gcmParams);
              this.msgDecrypted = aesGCMHelper.uint8Array2Str(decryptText.data);
              console.info('decrypt plainText: ' + this.msgDecrypted);
            } catch (e) {
              console.error('error', e.message, e.stack);
            }
          })
          .height('80%')

        Column({ space: 10 }) {
          TextArea({ placeholder: '待解密内容', text: $$this.msg2Decrypt })
            .height(60); // 待加密的信息
          Text(`解密的base64:`)
          Text(this.msgDecrypted)
            .copyOption(CopyOptions.LocalDevice); // 加密后的信息
        }
        .height('90%')
        .width('90%')
        .justifyContent(FlexAlign.SpaceEvenly).alignItems(HorizontalAlign.Start)
      }
      .padding(10)
      .height(200)
      .width('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```
