---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-31
title: SM2算法的C1C3C2格式密文与ASN.1编码格式如何互换
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > SM2算法的C1C3C2格式密文与ASN.1编码格式如何互换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:533fa6c5651e372e144ae82db0e5206d67660d2de23536aff61fc5039e41bed3
---

## 问题现象

服务端使用SM2算法加密后的密文格式为C1C3C2，使用ArkTS语言无法解密；同时ArkTS语言加密的SM2密文，服务端无法解密。C1C3C2格式密文如何与ArkTS生成的ASN.1编码格式密文互相转换？

## 背景知识

* [SM2](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#sm2)为非对称加密算法，加密长度需要在固定长度进行。算法库目前支持以GM/T 0009-2012定义的格式加密或解密数据。
* SM2非对称加密的结果由C1、C2、C3三部分组成：其中C1是根据生成的随机数计算出的椭圆曲线点，C2是密文数据，C3是通过指定的摘要算法计算的值。

**SM2密文长度**：

* C1：椭圆上的点X、Y，坐标均为256位（32字节），即C1通常为64字节（512位）。
* C2：裸密文，长度与明文一致。
* C3：哈希值，SM2使用SM3哈希算法，生成的哈希值为256位，即32字节。

通常SM2加密在服务端会使用不压缩的16进制格式进行加解密与传输，组合顺序为C1C3C2。每个16进制字符可以存储4位数据，所以C1构成为：前导04，X、Y坐标各64位16进制字符，长度共130字节。C3同样使用16进制需要64位的16进制字符，最终密文长度为2+64+64+64+N。

## 解决方案

根据以上的分析，用户可根据其他存量程序的方案选择以下合适的方法进行适配，即密文长度需要调整到固定长度，拼接顺序要符合标准。

**ArkTS加密**：

先解析密文得到C1（临时公钥，包括C1\_X, C1\_Y）、C2（密文）、C3（哈希值）并转化为16进制进行组合。

使用[getCipherTextSpec](../harmonyos-references/js-apis-cryptoframework.md#getciphertextspec12)得到[SM2CipherTextSpec](../harmonyos-references/js-apis-cryptoframework.md#sm2ciphertextspec12)，SM2CipherTextSpec包含以下几个变量：

* xCoordinate：X分量，即C1\_X。
* yCoordinate：Y分量，即C1\_Y。
* cipherTextData：裸密文，即C2。
* hashData：哈希值，即C3。

```ts
let cipherData = cipher.doFinalSync(dataBlog);
let spec: cryptoFramework.SM2CipherTextSpec = cryptoFramework.SM2CryptoUtil.getCipherTextSpec(cipherData, 'C1C3C2');
let C1x = spec.xCoordinate.toString(16).padStart(64, '0');
let C1y = spec.yCoordinate.toString(16).padStart(64, '0');
let C2 = buffer.from(spec.cipherTextData).toString('hex');
let C3 = buffer.from(spec.hashData).toString('hex');

// 拼接C1C2C3, 若要加前缀04表示C1未压缩
let result = '04' + C1x + C1y + C3 + C2;
```

**ArkTS解密**：

客户端得到服务端的密文后，通过2+64+64+64格式进行拆分提取参数，使用[genCipherTextBySpec](../harmonyos-references/js-apis-cryptoframework.md#genciphertextbyspec12)根据指定的SM2密文参数，生成符合国密标准的ASN.1格式SM2密文。

```ts
function genData(result: string): cryptoFramework.DataBlob {
  result = result.slice(2, result.length);
  let C1x = result.slice(0, 64);
  result = result.slice(64, result.length);
  let C1y = result.slice(0, 64);
  result = result.slice(64, result.length);
  let C3 = result.slice(0, 64);
  let C2 = result.slice(64, result.length);

  let spec: cryptoFramework.SM2CipherTextSpec = {
    xCoordinate: BigInt('0x' + C1x),
    yCoordinate: BigInt('0x' + C1y),
    cipherTextData: new Uint8Array(buffer.from(C2, 'hex').buffer),
    hashData: new Uint8Array(buffer.from(C3, 'hex').buffer),
  };
  // 此处的data可直接使用cryptoFramework进行SM2解密。
  let data = cryptoFramework.SM2CryptoUtil.genCipherTextBySpec(spec, 'C1C3C2');
  return data;
}
```

**加解密完整示例参考如下**：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function doEncryptByCommonKey2(data: string): string {
  let transformation: string = 'SM2_256|SM3';
  let pubSpec: cryptoFramework.ECCPubKeySpec = {
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC,
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    pk: {
      x: BigInt('0x26243808BA87B7908CAE11E8177005F2916894349CCE96470410B81631C9925B'),
      y: BigInt('0xDA8741620BC9146350E8BF5ABC0E047B8553EF6DBE9A0704BE6FF0A3569DAEF6')
    },
  };
  let keyGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(pubSpec);
  let pubKey = keyGenerator.generatePubKeySync();

  let cipher = cryptoFramework.createCipher(transformation);
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, pubKey, null);
  let dataBlog: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(data, 'utf-8').buffer) };

  let cipherData = cipher.doFinalSync(dataBlog);
  let spec: cryptoFramework.SM2CipherTextSpec = cryptoFramework.SM2CryptoUtil.getCipherTextSpec(cipherData, 'C1C3C2');
  let C1x = spec.xCoordinate.toString(16).padStart(64, '0');
  let C1y = spec.yCoordinate.toString(16).padStart(64, '0');
  let C2 = buffer.from(spec.cipherTextData).toString('hex');
  let C3 = buffer.from(spec.hashData).toString('hex');

  // 拼接C1C2C3, 若要加前缀04表示C1未压缩
  let result = '04' + C1x + C1y + C3 + C2;
  console.info('doEncryptByCommonKey result:' + result);
  return result;
}

function genData(result: string): cryptoFramework.DataBlob {
  result = result.slice(2, result.length);
  let C1x = result.slice(0, 64);
  result = result.slice(64, result.length);
  let C1y = result.slice(0, 64);
  result = result.slice(64, result.length);
  let C3 = result.slice(0, 64);
  let C2 = result.slice(64, result.length);

  let spec: cryptoFramework.SM2CipherTextSpec = {
    xCoordinate: BigInt('0x' + C1x),
    yCoordinate: BigInt('0x' + C1y),
    cipherTextData: new Uint8Array(buffer.from(C2, 'hex').buffer),
    hashData: new Uint8Array(buffer.from(C3, 'hex').buffer),
  };
  // 此处的data可直接使用cryptoFramework进行SM2解密。
  let data = cryptoFramework.SM2CryptoUtil.genCipherTextBySpec(spec, 'C1C3C2');
  return data;
}

function doDecryptByCommonKey(tempResult: string) {
  console.info('doDecryptByCommonKey begin');
  let transformation: string = 'SM2_256|SM3';
  let priSpec: cryptoFramework.ECCPriKeySpec = {
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.PRIVATE_KEY_SPEC,
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    sk: BigInt('0x00C0E0E55F8283D58CFF6B3820033B17E4427FADD02DDFE693F9131A32F71EC6FC'),
  };
  let keyGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(priSpec);
  let priKey = keyGenerator.generatePriKeySync();
  let cipher = cryptoFramework.createCipher(transformation);
  cipher.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, priKey, null);
  let data = genData(tempResult);
  let cipherData = cipher.doFinalSync(data);

  let message = buffer.from(cipherData.data).toString('utf-8');
  console.info(message);
}

function main(message: string) {
  let data = doEncryptByCommonKey2(message);
  doDecryptByCommonKey(data);
}

@Entry
@Component
struct Index {

  build() {
    RelativeContainer() {
      Button('SM2加解密')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          main('Welcome');
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：如何从ASN1 DER格式的签名数据获取SM2签名后数据的r和s部分，组成64字节数据？

A：升级到API20，[genEccSignatureSpec](../harmonyos-references/js-apis-cryptoframework.md#geneccsignaturespec20)支持从ASN1 DER格式的SM2签名数据获取r和s。

Q：解密时遇到错误码17630001该如何解决？

A：错误码[17630001](../harmonyos-references/errorcode-crypto-framework.md#section17630001-密码操作错误)表示调用三方算法库API出错，可以检查加密时SM2密文参数的长度是否规范。

国密算法的底层实现是OpenSSL，为了防止数据在拼接的时候被截取到，在返回OpenSSL数据时是直接透传返回的，中间不作任何操作来保证安全性。而OpenSSL底层返回的数据时高位如果是0会默认被舍弃，针对这种情况需要业务自己实现，即在拼接生成C1C3C2格式的密文时，检查x分量（C1\_X）或y分量（C1\_Y）的长度是否为32字节，如果长度不够需要在高位补0，使得x分量和y分量的长度均为32字节。

## 总结

存量加解密方式中通常使用固定长度非压缩格式密文进行加解密，与ArkTS进行交互需要转化成国密标准的ASN.1格式SM2密文；同样，与存量加解密方式交互需要转化成非压缩格式进行兼容。
