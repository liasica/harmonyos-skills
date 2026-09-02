---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-46
title: AES加密如何使用ISO7816-4PADDING进行填充
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > AES加密如何使用ISO7816-4PADDING进行填充
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:79a707e6898c5c756e927784363a21922abb9bfcd4e2b2207236b3315666b83d
---

## 问题现象

AES加密无法在CBC模式下用ISO7816-4PADDING进行填充，CBC模式下填充模式为[NoPadding|PKCS5|PKCS7]。

## 背景知识

* AES为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。
* 不同分组模式支持的填充模式如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/zrcFZv-2SCGKCOMsUt6Olg/zh-cn_image_0000002628609218.png "点击放大")
* 使用算法库CBC的NoPadding填充，依据业务自行对数据进行ISO7816-4PADDING填充和校验。
* ISO 7816-4是智能卡通信的国际标准，其中定义了一种特殊的数据填充（Padding）机制，用于将数据块扩展到特定长度；这种填充方案确保数据在传输或加密时符合块大小要求，同时保持数据完整性。
* ISO 7816-4填充的核心规则：
  1. 添加固定标记：在数据末尾添加第一个字节0x80（二进制1000 0000）。
  2. 补零：随后添加0x00直到数据块长度达到目标大小。

## 解决方案

当前HarmonyOS Crypto Architecture Kit（加解密算法框架服务）提供的对称算法仅支持PKCS7和NoPadding填充算法，以下介绍如何基于Crypto Architecture Kit实现ISO 7816-4填充的AES算法。

加密实现思路：

1. 对明文进行ISO 7816-4填充。
2. 对填充后的数据进行AES-CBC加密，指定填充为NoPadding，得到密文。

解密实现思路：

1. 对密文进行AES-CBC解密，指定填充为NoPadding。
2. 对解密的数据进行ISO 7816-4去填充，得到真正的明文。

代码示例如下：

* ISO7816\_4\_PADDING函数实现ISO 7816-4填充算法。

  ```ts
  async function ISO7816_4_PADDING(addPadding: boolean, data: Uint8Array): Promise<Uint8Array> {
    let blockSize = 16;
    try {
      if (addPadding == true) {
        let paddingLen = blockSize - (data.length % blockSize);
        let cipherText = new Uint8Array(data.length + paddingLen);
        cipherText.set(data);
        cipherText[data.length] = 0x08;
        for (let i = 1; i < paddingLen; i++) {
          cipherText[data.length + i] = 0x00;
        }
        return cipherText;
      } else {
        if (data.length == 0 || data.length % blockSize != 0) {
          throw new TypeError("invalid len!");
        }
        let i = 0;
        for (i = 0; i < blockSize; i++) {
          if (data[data.length - 1 - i] != 0x00) {
            break;
          }
        }
        if (i == blockSize || data[data.length - 1 - i] != 0x08) {
          throw new TypeError("invalid padding!");
        }
        return data.slice(0, data.length - 1 - i);
      }
    } catch (error) {
      console.error(error, `error code: ${error.code}`);
      return new Uint8Array([]);
    }
  }
  ```
* aes\_enc\_with\_ISO7816\_4PADDING实现ISO 7816-4填充的AES-CBC加密算法。

  ```ts
  async function aes_enc_with_ISO7816_4PADDING(key: Uint8Array, iv: Uint8Array, plaintext: Uint8Array): Promise<Uint8Array> {
    try {
      let ivParam: cryptoFramework.IvParamsSpec = { iv: { data: iv }, algName: 'IvParamsSpec' };
      let cipherAlg = 'AES' + key.length * 8;
      let keyGen = cryptoFramework.createSymKeyGenerator(cipherAlg);
      let symKey = keyGen.convertKeySync({ data: key });
      let plaintextWithPadding = await ISO7816_4_PADDING(true, plaintext);

      let cipher = cryptoFramework.createCipher("AES|CBC|NoPadding");
      cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivParam);
      let ciphertext = await cipher.doFinal({ data: plaintextWithPadding });
      return ciphertext.data;
    } catch (error) {
      console.error(error, `error code: ${error.code}`);
      return new Uint8Array([]);
    }
  }
  ```
* aes\_dec\_with\_ISO7816\_4PADDING实现ISO 7816-4填充的AES-CBC解密算法。

  ```ts
  async function aes_dec_with_ISO7816_4PADDING(key: Uint8Array, iv: Uint8Array, ciphertext: Uint8Array): Promise<Uint8Array> {
    try {
      let ivParam: cryptoFramework.IvParamsSpec = { iv: { data: iv }, algName: 'IvParamsSpec' };
      let cipherAlg = 'AES' + key.length * 8;
      let keyGen = cryptoFramework.createSymKeyGenerator(cipherAlg);
      let symKey = keyGen.convertKeySync({ data: key });

      let cipher = cryptoFramework.createCipher("AES|CBC|NoPadding");
      cipher.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivParam);
      let tmpData = await cipher.doFinal({ data: ciphertext });

      return await ISO7816_4_PADDING(false, tmpData.data);
    } catch (error) {
      console.error(error, `error code: ${error.code}`);
      return new Uint8Array([]);
    }
  }
  ```

完整示例参考如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct Crypto {
  build() {
    Column() {
      Text('点击开始')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          test();
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

//ISO7816_4_PADDING函数实现ISO 7816-4填充算法：
async function ISO7816_4_PADDING(addPadding: boolean, data: Uint8Array): Promise<Uint8Array> {
  let blockSize = 16;
  try {
    if (addPadding == true) {
      let paddingLen = blockSize - (data.length % blockSize);
      let cipherText = new Uint8Array(data.length + paddingLen);
      cipherText.set(data);
      cipherText[data.length] = 0x08;
      for (let i = 1; i < paddingLen; i++) {
        cipherText[data.length + i] = 0x00;
      }
      return cipherText;
    } else {
      if (data.length == 0 || data.length % blockSize != 0) {
        throw new TypeError("invalid len!");
      }
      let i = 0;
      for (i = 0; i < blockSize; i++) {
        if (data[data.length - 1 - i] != 0x00) {
          break;
        }
      }
      if (i == blockSize || data[data.length - 1 - i] != 0x08) {
        throw new TypeError("invalid padding!");
      }
      return data.slice(0, data.length - 1 - i);
    }
  } catch (error) {
    console.error(error, `error code: ${error.code}`);
    return new Uint8Array([]);
  }
}

// aes_enc_with_ISO7816_4PADDING实现ISO 7816-4填充的AES-CBC加密算法：
async function aes_enc_with_ISO7816_4PADDING(key: Uint8Array, iv: Uint8Array, plaintext: Uint8Array): Promise<Uint8Array> {
  try {
    let ivParam: cryptoFramework.IvParamsSpec = { iv: { data: iv }, algName: 'IvParamsSpec' };
    let cipherAlg = 'AES' + key.length * 8;
    let keyGen = cryptoFramework.createSymKeyGenerator(cipherAlg);
    let symKey = keyGen.convertKeySync({ data: key });
    let plaintextWithPadding = await ISO7816_4_PADDING(true, plaintext);

    let cipher = cryptoFramework.createCipher("AES|CBC|NoPadding");
    cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivParam);
    let ciphertext = await cipher.doFinal({ data: plaintextWithPadding });
    return ciphertext.data;
  } catch (error) {
    console.error(error, `error code: ${error.code}`);
    return new Uint8Array([]);
  }
}

//aes_dec_with_ISO7816_4PADDING实现ISO 7816-4填充的AES-CBC解密算法：
async function aes_dec_with_ISO7816_4PADDING(key: Uint8Array, iv: Uint8Array, ciphertext: Uint8Array): Promise<Uint8Array> {
  try {
    let ivParam: cryptoFramework.IvParamsSpec = { iv: { data: iv }, algName: 'IvParamsSpec' };
    let cipherAlg = 'AES' + key.length * 8;
    let keyGen = cryptoFramework.createSymKeyGenerator(cipherAlg);
    let symKey = keyGen.convertKeySync({ data: key });

    let cipher = cryptoFramework.createCipher("AES|CBC|NoPadding");
    cipher.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivParam);
    let tmpData = await cipher.doFinal({ data: ciphertext });

    return await ISO7816_4_PADDING(false, tmpData.data);
  } catch (error) {
    console.error(error, `error code: ${error.code}`);
    return new Uint8Array([]);
  }
}

async function test() {
  let message = 'This is a test';
  let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  let iv = new Uint8Array([82, 216, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  let textEncoder = util.TextEncoder.create("utf-8");
  let array: Uint8Array = textEncoder.encodeInto(message);
  let encUint8Array = await aes_enc_with_ISO7816_4PADDING(keyData, iv, array);

  let decUint8Array = await aes_dec_with_ISO7816_4PADDING(keyData, iv, encUint8Array);
  let textDecoderOptions: util.TextDecoderOptions = {
    fatal: false,
    ignoreBOM: true
  };
  let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
  let res = textDecoder.decodeToString(decUint8Array);
  console.info(`res:${res}`);
}
```
