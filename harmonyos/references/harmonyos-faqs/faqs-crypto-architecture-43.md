---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-43
title: 如何解决AES解密Base64格式密文失败的问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何解决AES解密Base64格式密文失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:433a0220edaba3959272ace23969889af60cbe5cdf018b938c64dc7ef8ad71a3
---

## 问题现象

使用AES算法进行加解密，明文在加密后转为Base64格式密文进行传输，在执行解密方法时已经将参数转换为Uint8Array类型数据，但却解密失败，是什么原因？

问题代码示例参考如下：

```screen
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

async function aesEncryptString(data: string): Promise<string> {
  let symKey = await genSymKeyByData(new Uint8Array(buffer.from('aeskey0123456789', 'utf-8').buffer));
  let plainText: cryptoFramework.DataBlob = {
    data: new Uint8Array(buffer.from(data, 'utf-8').buffer)
  };
  let encryptText = await encryptMessagePromise(symKey, plainText);
  return new util.Base64Helper().encodeToString(encryptText.data)
}

async function aesDecryptString(data: string): Promise<string> {
  let symKey = await genSymKeyByData(new Uint8Array(buffer.from('aeskey0123456789', 'utf-8').buffer))
  let plainText: cryptoFramework.DataBlob = {
    data: new Uint8Array(buffer.from(data, 'utf-8').buffer)
  };
  let decryptText = await decryptMessagePromise(symKey, plainText)
  return new util.Base64Helper().encodeToString(decryptText.data)
}

// 加密方法
async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  let iv = genIvParamsSpec();
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  let cipherData = await cipher.doFinal(plainText);
  return cipherData;
}

// 解密方法
async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  let iv = genIvParamsSpec();
  await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  let decryptData = await decoder.doFinal(cipherText);
  return decryptData;
}

function genIvParamsSpec() {
  let ivBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('0123456789101112', 'utf-8').buffer) };
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: 'IvParamsSpec',
    iv: ivBlob
  };
  return ivParamsSpec;
}

async function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = await aesGenerator.convertKey(symKeyBlob);
  return symKey
}
```

## 背景知识

AES加解密算法是一种常见的对称加解密算法。

* [AES密钥规格](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)。
* [随机生成AES密钥](../harmonyos-guides/crypto-generate-sym-key-randomly.md#随机生成aes密钥)。
* [AES加解密算法规格](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#aes)。

数据类型介绍。

* Base64编码：Base64编码是一种常用于将二进制数据转换为ASCII字符串的编码方式。
* Uint8Array：Uint8Array是一种基本的JavaScript数组类型，用于处理二进制数据。它是定长的，包含八个位（bit）的无符号整数（0到255），非常适合处理原始字节数据。

## 问题定位

1. 由于AES算法解密失败，对AES算法解密方法进行error信息打印，获取error信息。

   ```screen
   aesDecryptString(encryptString).then((data) => {
     console.info(`test string = ${data}`)
   }).catch((error: BusinessError) => {
     console.error(`DecryptString failed, error code: ${error.code}, error message: ${error.message}`);
   })
   ```
2. 获取到错误码[17630001](../harmonyos-references/errorcode-crypto-framework.md#section17630001-密码操作错误)，查询错误码信息可以分析得出输入参数错误。

   ```screen
   DecryptString failed, error code: 17630001, error message: doFinal failed.
   ```
3. 进一步确认AES解密算法的规格、模式、填充方式、密钥及iv值都正确，可判断出待解密的密文参数错误，打印加密后的密文数据。

   ```screen
   aesEncryptString('This is a test').then((data) => {
     encryptString = data;
     console.info(`encryptString = ${encryptString}`)
   })
   ```

   ```screen
   aqHCyoI0dFwQ873GtpLSpw==
   ```
4. 根据加密方法及加密结果可以确认密文为Base64编码格式数据，而在解密方法中直接将Base64编码格式数据转换为Uint8Array格式数据，导致获取的是对应普通字符串的Uint8Array格式数据，未成功获取到密文数据。

## 分析结论

由于密文被转换成Base64编码格式数据进行传输，在解密时没有进行解码，直接按照普通字符串的方式直接转换为Uint8Array格式数据，导致获取到的密文数据错误，最终解密失败。

## 修改建议

在解密时，先对密文数据进行解码，然后对解码后的密文数据进行解密。

```screen
async aesDecryptString(data: string): Promise<string> {
  let symKey = await this.genSymKeyByData(new Uint8Array(buffer.from('aeskey0123456789', 'utf-8').buffer));
  let uint8ArrayDecryptString = new util.Base64Helper().decodeSync(data);
  let plainText: cryptoFramework.DataBlob = {
    data: uint8ArrayDecryptString
  };
  let decryptText = await this.decryptMessagePromise(symKey, plainText);
  return new util.Base64Helper().encodeToString(decryptText.data);
}
```

完整示例及运行结果参考如下：

```screen
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct AESalgorithm {
  @State encryptString: string = '';
  @State base64String: string = '';
  @State string: string = '';

  async aesEncryptString(data: string): Promise<string> {
    let symKey = await this.genSymKeyByData(new Uint8Array(buffer.from('aeskey0123456789', 'utf-8').buffer));
    let plainText: cryptoFramework.DataBlob = {
      data: new Uint8Array(buffer.from(data, 'utf-8').buffer)
    };
    let encryptText = await this.encryptMessagePromise(symKey, plainText);
    return new util.Base64Helper().encodeToString(encryptText.data);
  }

  async aesDecryptString(data: string): Promise<string> {
    let symKey = await this.genSymKeyByData(new Uint8Array(buffer.from('aeskey0123456789', 'utf-8').buffer));
    let uint8ArrayDecryptString = new util.Base64Helper().decodeSync(data);
    let plainText: cryptoFramework.DataBlob = {
      data: uint8ArrayDecryptString
    };
    let decryptText = await this.decryptMessagePromise(symKey, plainText);
    return new util.Base64Helper().encodeToString(decryptText.data);
  }

  // 加密方法
  async encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
    let iv = this.genIvParamsSpec();
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
    let cipherData = await cipher.doFinal(plainText);
    return cipherData;
  }

  // 解密方法
  async decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
    let iv = this.genIvParamsSpec();
    await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
    let decryptData = await decoder.doFinal(cipherText);
    return decryptData;
  }

  genIvParamsSpec() {
    let ivBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('0123456789101112', 'utf-8').buffer) };
    let ivParamsSpec: cryptoFramework.IvParamsSpec = {
      algName: 'IvParamsSpec',
      iv: ivBlob
    };
    return ivParamsSpec;
  }

  async genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
    let symKey = await aesGenerator.convertKey(symKeyBlob);
    return symKey;
  }

  main() {
    let encryptString: string = '';
    this.aesEncryptString('This is a test').then((data) => {
      encryptString = data;
      this.encryptString = data;
      hilog.info(0x0000, 'test', `encryptString = ${encryptString}`);
      this.aesDecryptString(encryptString).then((data) => {
        this.base64String = data;
        hilog.info(0x0000, 'test', `test string base64 = ${data}`);
        let stringUint8Array = new util.Base64Helper().decodeSync(data);
        let decoder = util.TextDecoder.create('utf-8');
        let testString = decoder.decodeToString(stringUint8Array);
        hilog.info(0x0000, 'test', `test string = ${testString}`);
        this.string = testString;
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'test', `DecryptString failed, error code: ${error.code}, error message: ${error.message}`);
      });
    });
  }

  build() {
    Column({ space: 20 }) {
      Row() {
        Text('初始字符串：');
        Text('This is a test');
      };

      Button('点击对字符串进行加解密')
        .onClick(() => {
          this.main();
        });
      Row() {
        Text('加密结果：');
        Text(this.encryptString);
      };

      Row() {
        Text('解密后的Base64字符串：');
        Text(this.base64String);
      };

      Row() {
        Text('解密后的原始字符串：');
        Text(this.string);
      };

    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：Base64编码格式数据大小写是否有区别？

A：Base64编码格式是一种基于64个可打印字符来表示任意二进制数据的方法。在进行Base64编码时，数据的大小写是有区别的，因为Base64编码使用的字符集中包括了大小写字母、数字和其他字符。
