---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/crypto-architecture-kit-troubleshooting
title: 故障排查
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 故障排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:10+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:0df1ae391fe611065778493b9c04f08117333f1fb902eeae3fbd960a98bab5e8
---

## 如何解决DES密钥生成报错Invalid param: input key length is invalid

### 问题现象

使用密钥材料“TESTXXXX”进行DES加密，调用[SymKeyGenerator.convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)生成密钥时报错：ConvertSymmKey[316]: Invalid param: input key length is invalid!

### 定位过程

问题代码：

```ts
const keyData = new util.TextEncoder().encodeInto("TESTXXXX");
let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
const symKey = symKeyGenerator.convertKeySync({
  data: keyData
});
```

运行上文代码，使用密钥进行DES加密时报错如下图所示，根据报错信息可以判断是Key长度问题引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ihQYKlXJQuymweHre19GRg/zh-cn_image_0000002794642573.png "点击放大")

### 分析结论

参考背景知识中3DES算法规格的介绍，要求密钥长度必须为192位，即24个字节。而问题代码中的密钥材料“TESTXXXX”只有8个字节，因此需要用'\0'补充剩余长度。

| 对称密钥算法 | 密钥长度（bit） | 字符串参数 |
| --- | --- | --- |
| 3DES | 192 | 3DES192 |

### 修改建议

通过padEnd()补齐密钥长度，该方法会将当前字符串从末尾开始填充给定的字符串（如果需要会重复填充），直到达到给定的长度。

代码示例如下：

```ts
import { util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct SolutionOfDESKeyGenerationFailed {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          const keyData = new util.TextEncoder().encodeInto('TESTXXXX'.padEnd(24, '0'));
          let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
          const symKey = symKeyGenerator.convertKeySync({
            data: keyData
          });
          hilog.info(0x0000, 'TAG', `symKey: ${symKey}`);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## DES加密密文与其他端结果不一致问题如何解决

### 问题现象

使用ArkTS语言进行加解密操作与服务端加密结果不一致导致功能失败，如何修改ArkTS代码才能实现同样的加密结果？

DES目前支持分组模式为ECB/CBC/OFB/CFB，以下使用ECB/CBC分组模式使用错误来举例说明。

需要加密数据为1234，密钥为：MOBCB123，加密参数为：DES ECB PKCS7Padding；服务端加密结果为：dcc420f814a661c7；客户端加密结果为：OhGfo20IMls=。

### 定位过程

1. **确认加解密流程**：

   针对服务端与客户端加密结果不一致的问题，首先需要了解服务端使用什么语言与三方库，对特定的语言与三方库进行分析，确认加解密流程差异，如果使用了三方库或自定义加密流程则需要在ArkTS语言中复刻该流程。

   此处对于加解密流程不同不做详细说明，不同的三方库与服务端可能会根据自己的需求独特设计加密流程。例如：在生成密文后做逆序处理。

   以上例子中：服务端使用了java语言进行DES加密，并没有使用三方库进行加密，排除三方库对密文的特殊处理。
2. **确认编码格式**：

   加解密过程中有三处编码格式需要进行检查服务端与客户端是否一致：密钥、原文、密文。

   以上例子中：针对加密结果进行分析，服务端加密结果为数字以及a-f字母构成，而客户端加密结果则含有=等特殊符号；根据编码规则分析，服务端对密文进行了16进制编码，而客户端则进行了base64编码。更改客户端编码为16进制编码后得出结果为：3a119fa36d08325b，与服务端结果依旧不同。
3. **确认加解密参数**：

   DES加解密算法的参数分为：分组模式、密钥长度、填充模式。

   以上例子中：服务端使用的加密分组模式为CBC，与客户端使用的ECB模式不同导致加密结果不同。CBC分组模式需要添加偏移量进行加密，客户端添加偏移量MOBCB456后再次进行加密，结果为dcc420f814a661c7，与服务端结果一致。

### 分析结论

针对对称加解密，密钥参数、编码格式、加解密流程都一致才能保证加密结果一致。

以上例子中：客户端与服务端密文编码格式不同，且加密参数不同导致密文不一致。

### 修改建议

修改客户端编码模式与分组模式，代码如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

// 加密消息。
function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('DES64|CBC|PKCS7');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, genIvParamsSpec());
  let encryptData = cipher.doFinalSync(plainText);
  return encryptData;
}

// 解密消息。
function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('DES64|CBC|PKCS7');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, genIvParamsSpec());
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let symGenerator = cryptoFramework.createSymKeyGenerator('DES64');
  let symKey = symGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

// 生成偏移量
function genIvParamsSpec() {
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: 'IvParamsSpec',
    iv: { data: new Uint8Array(buffer.from('MOBCB456', 'utf-8').buffer) }
  };
  return ivParamsSpec;
}

function main() {
  let key = 'MOBCB123';
  let keyData = new Uint8Array(buffer.from(key, 'utf-8').buffer);
  let symKey = genSymKeyByData(keyData);
  let message = '1234';
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptText = encryptMessage(symKey, plainText);
  console.info('encryptText: ', buffer.from(encryptText.data).toString('hex'));
  let decryptText = decryptMessage(symKey, encryptText);
  if (plainText.data.toString() === decryptText.data.toString()) {
    console.info('decrypt ok');
    console.info('decrypt plainText: ', buffer.from(decryptText.data).toString('utf-8'));
  } else {
    console.error('decrypt failed');
  }
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('DES加密')
        .onClick(() => {
          main();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 使用OpenSSL创建的Ed25519签名验签报错

### 问题现象

使用OpenSSL创建的Ed25519密钥，然后使用HarmonyOS的方法生成密钥信息报错。

OpenSSL创建Ed25519密钥代码：

```sehll
openssl genpkey -algorithm ED25519 -out ed25519-private.pem && openssl pkey -pubout -in ed25519-private.pem > ed25519-public.pem
```

OpenSSL创建的Ed25519密钥：

```ts
let priKey = 'MC4CAQAwBQYDK2VwBCIEIPFypge0/4Q4Nj+g3rdkq1waRD/wmRetRJ4eUBT0D86S'
let pubKey = 'MCowBQYDK2VwAyEADb/Cqqww74MVIcezIun9Mh1lbnx3cw9Qy9vYztWx2NA='
```

Ed25519密钥转换代码：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

// 转换密钥对
function genKeyPairByData() {
  let priKey = 'MC4CAQAwBQYDK2VwBCIEIPFypge0/4Q4Nj+g3rdkq1waRD/wmRetRJ4eUBT0D86S'
  let pubKey = 'MCowBQYDK2VwAyEADb/Cqqww74MVIcezIun9Mh1lbnx3cw9Qy9vYztWx2NA='

  try {
    let pubKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(pubKey, 'utf-8').buffer) };
    let priKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(priKey, 'utf-8').buffer) };
    let ed25519Generator = cryptoFramework.createAsyKeyGenerator('Ed25519');
    let keyPair = ed25519Generator.convertKeySync(pubKeyBlob, priKeyBlob);
    console.info('convertKey success');
    return keyPair;
  } catch (error) {
    console.error(`ECDSA ${error}, error code: ${error.code}`);
    return null;
  }
}
```

报错信息：

```txt
ECDSA Error: convert key fail., error code: 17630001
```

### 定位过程

1. 根据[错误码17630001](../harmonyos-references/errorcode-crypto-framework.md#section17630001-算法相关的操作错误调用三方算法库api出错)查询相关错误信息。
2. 由于方法并未使用第三方算法库，所以根据错误码信息可以得知是输入参数错误。
3. 根据OpenSSL创建的Ed25519密钥结果可以看出提供的公私钥数据为Base64格式。
4. 检查代码，可以发现在将公私钥数据转换为方法需要的Uint8Array类型数据时，使用的是new Uint8Array(buffer.from(pubKey, 'utf-8').buffer)，而此方法是将utf-8类型字符串转换为Uint8Array类型。
5. 可以确认Base64格式类型数据转换为Uint8Array类型数据方法使用错误。

### 分析结论

在将Base64格式类型的Ed25519公私钥数据转换成Uint8Array类型的Ed25519公私钥数据时，使用了错误的数据类型转换方法，没有成功转换为正确的Uint8Array类型的Ed25519公私钥数据，从而导致非对称密钥转换API时报错。

### 修改建议

使用正确的数据类型转换方法，将Base64格式类型的Ed25519公私钥数据转换成Uint8Array类型，然后使用AsyKeyGenerator.convertKeySync方法将Ed25519公私钥数据转换为Ed25519密钥对keyPair，即可进行签名验签。示例代码参考：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct KeyPair {
  genKeyPairByData() {
    let priKey = 'MC4CAQAwBQYDK2VwBCIEIPFypge0/4Q4Nj+g3rdkq1waRD/wmRetRJ4eUBT0D86S';
    let pubKey = 'MCowBQYDK2VwAyEADb/Cqqww74MVIcezIun9Mh1lbnx3cw9Qy9vYztWx2NA=';

    try {
      let pubKeyBlob: cryptoFramework.DataBlob = { data: this.base64ToUint8Array(pubKey) };
      let priKeyBlob: cryptoFramework.DataBlob = { data: this.base64ToUint8Array(priKey) };
      let ed25519Generator = cryptoFramework.createAsyKeyGenerator('Ed25519');
      let keyPair = ed25519Generator.convertKeySync(pubKeyBlob, priKeyBlob);
      console.info('convertKey success');
      return keyPair;
    } catch (error) {
      return null;
    }
  }

  // Base64转Uint8Array
  base64ToUint8Array(str: string): Uint8Array {
    let base64Helper = new util.Base64Helper();
    return base64Helper.decodeSync(str);
  }

  // 签名
  signMessagePromise(message: string, priKey: cryptoFramework.PriKey) {
    let signer = cryptoFramework.createSign('Ed25519');
    let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    signer.initSync(priKey);
    let signData = signer.signSync(input);
    return signData;
  }

  // 验签
  verifyMessagePromise(message: string, signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
    let verifier = cryptoFramework.createVerify('Ed25519');
    let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    verifier.initSync(pubKey);
    let res = verifier.verifySync(input, signMessageBlob);
    console.info(`verify result is ${res}`);
    return res;
  }

  build() {
    Column() {
      Button('点击签名验签')
        .fontSize(20)
        .padding(10)
        .onClick(() => {
          let message = 'this is a test data';
          let keypair = this.genKeyPairByData();
          if (keypair) {
            let signData = this.signMessagePromise(message, keypair.priKey);
            this.verifyMessagePromise(message, signData, keypair.pubKey);
          } else {
            console.info('convertKey failed');
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

* **[加解密与签名验签问题定位](crypto-architecture-kit-troubleshooting-0001.md)**
