---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-48
title: 如何解决RSA加密报-1错误码问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何解决RSA加密报-1错误码问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f3b4813d634e183c73d785a55f3d32225060e69fb0c11380899681ff1b4e3251
---

## 问题现象

使用RSA加密算法进行加密，执行后报-1错误码是什么原因？如何解决？

RSA公钥参数如下：

```text
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCuo5/hnnCOAERqdJwQM6Uwo2FZ
Gq/JHKRj43QnxxnxUIhnwaHH7PUv8V2v8pNdJl5NYD6qiEiD7i59HI0G5PSj3gjZ
4KuHy/RIN95BZyLtrg2BKzNiGvUV4IPFzE9ZAe0fcEvDPxGZn/vRWLRnQaEeYehc
OUkt2vbKPLwtTWKwzQIDAQAB
-----END PUBLIC KEY-----
```

报错信息截图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/q8t_gVLoSfS35ABXJcJNLw/zh-cn_image_0000002658848479.png "点击放大")

```txt
code = "-1"
message = "The input string contains unsupported characters"
```

## 背景知识

[RSA](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#rsa)是一种非对称加解密算法，使用RSA算法进行加解密可以参考[使用RSA非对称密钥（PKCS1模式）加解密(ArkTS)](../harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1.md)。

* 创建非对称密钥生成器实例API：[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)。
* 非对称密钥生成器密钥API：[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)。
* 创建加解密实例API：[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)。
* 初始化加解密实例对象API：[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)。
* 执行并结束加解密API：[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)。

## 问题定位

1. 分析错误码-1，使用RSA加密时遇到错误码-1，这通常表示“ERR\_UNEXPECTED”，即遇到了一个未被预期或未被特定处理的问题。
2. 根据错误提示信息“The input string contains unsupported characters”可以进一步判断出报错原因是因为输入参数错误。
3. RSA公钥加密输入参数为公钥和明文，明文传入后转换为Uint8Array数据类型，排除明文参数错误，可以确认报错是由传入的公钥参数导致。
4. 公钥数据中除公钥外尚有开头和结尾的标识符字符串，而RSA加密只需要公钥，最终可以确认报-1错误码是因为没有去除公钥数据首尾标识符导致。

## 分析结论

RSA加密报-1错误码是因为没有对公钥数据进行去除首尾标识符，从而传入了错误的公钥参数，导致加密方法解析公钥参数失败。

## 修改建议

将公钥数据去除'-----BEGIN PUBLIC KEY-----'和'-----END PUBLIC KEY-----'标识符后作为公钥参数执行RSA加密。

完整示例代码如下：

```ts
import { buffer, util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// RSA pubKey example. 实际使用需要更换自己的公钥PEM
const pubKeyStr = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCuo5/hnnCOAERqdJwQM6Uwo2FZ\n' +
  'Gq/JHKRj43QnxxnxUIhnwaHH7PUv8V2v8pNdJl5NYD6qiEiD7i59HI0G5PSj3gjZ\n' +
  '4KuHy/RIN95BZyLtrg2BKzNiGvUV4IPFzE9ZAe0fcEvDPxGZn/vRWLRnQaEeYehc\n' +
  'OUkt2vbKPLwtTWKwzQIDAQAB';

// RSA加密方法
async function encryptRSA(message: string, pubKeyStr: string) {
  try {
    // 初始化Base64工具实例
    let base64Helper = new util.Base64Helper();
    // 公钥转换为Uint8Array，然后包装为DataBlob类型
    let pubKeyBlob: cryptoFramework.DataBlob = { data: base64Helper.decodeSync(pubKeyStr) };
    // 创建RSA key生成器
    let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
    // 将公钥包装数据pubKeyBlob转换成密钥对类型KeyPair
    let keyPair = await rsaGenerator.convertKey(pubKeyBlob, null);
    // 创建Cipher对象
    let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
    // 初始化加密模式，指定密钥keyPair.pubKey
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);
    // 包装要加密的明文
    let plainTextBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    // 传入明文，获取加密后的数据
    let encryptBlob = await cipher.doFinal(plainTextBlob);
    // 返回加密后的字符串
    // return base64Helper.encodeToStringSync(encryptBlob.data);
    console.info(`base64Helper: ${base64Helper.encodeToStringSync(encryptBlob.data)}`);
  } catch (e) {
    console.error('[base64Helper] error');
  }
  return undefined;
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('RSA加密')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          encryptRSA('This is a test demo.', pubKeyStr);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 总结

方法报错问题可以根据错误码和错误提示进行判断错误原因，进行排查修改。
