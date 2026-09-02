---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-38
title: SM2国密基于十六进制公钥参数加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > SM2国密基于十六进制公钥参数加密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f00f9a26145985dff31ed3fdf9e36751416d255601fa6f5f8e582aedaaa1683e
---

## 问题现象

应用需要基于十六进制公钥参数对数据进行SM2国密算法加密，通过给定的公钥参数生成密钥对并加密，未正常完成加密动作，日志显示convert key failed错误。

## 背景知识

SM2为非对称加密算法，算法规格及使用可以参考如下相关文档内容：[SM2](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#sm2)、[使用SM2非对称密钥加解密](../harmonyos-guides/crypto-sm2-asym-encrypt-decrypt.md)。

## 解决方案

由于给定的公钥参数为十六进制字符串类型，而加解密算法服务生成密钥对API所需要的DataBlob实际为Uint8Array类型，所以需要进行参数类型转换，转换接口参考如下：

```ts
async function convertStrToPubKey(publicKeyStr: string): Promise<cryptoFramework.PubKey> {
  let pubKeyStr = publicKeyStr.startsWith('04') ? publicKeyStr.slice(2) : publicKeyStr;
  let pkPart1 = pubKeyStr.slice(0, pubKeyStr.length / 2);
  let pkPart2 = pubKeyStr.slice(pubKeyStr.length / 2);
  let pk: cryptoFramework.Point = {
    x: BigInt('0x' + pkPart1),
    y: BigInt('0x' + pkPart2),
  };
  let pubKeySpec: cryptoFramework.ECCPubKeySpec = {
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    pk: pk,
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
  };
  let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(pubKeySpec);
  return await keypairGenerator.generatePubKey();
}
```

完整的加解密流程参考如：

```ts
import { PromptAction } from '@kit.ArkUI';
import { buffer } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';

export interface SM2Cipher {
  plainText?: string | undefined,
  encryptedStr?: string | undefined,
  pkData: Uint8Array | null,
  skData: Uint8Array | null,
}

// 公钥十六进制参数
const pkData = 'A5BF515F9BA06EFCE0110DA183DEF4AD428B8E379ECF296017A8DDD22B6FA86F320DD9AD0403F24340BAB5291B97F420FF22EB25284E3EB74BE726961B975196';
// 私钥十六进制参数
const skData = '2DA69465698665AA1FCA79AC4BA6E8717D6862AC23A2C35C37F53B965FBBC097';
const base64Helper = new util.Base64Helper();

/**
 * 生成密钥对
 * @param pubKeyData 公钥参数
 * @param privKeyData 私钥参数
 * @returns 生成的密钥对
 */
async function genKeyPairByData(pubKeyData: cryptoFramework.DataBlob | null,
  priKeyData: cryptoFramework.DataBlob | null): Promise<cryptoFramework.KeyPair> {
  let sm2Generator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  let keyPair = await sm2Generator.convertKey(pubKeyData, priKeyData);
  return keyPair;
}
/**
 * 加密
 * @param encryptKey 密钥
 * @param plainText 待加密字符串
 * @returns 加密后数据
 */
async function encryptMessage(encryptKey: cryptoFramework.Key, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('SM2_256|SM3');
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, encryptKey, null);
  let encryptData = await cipher.doFinal(plainText);
  return encryptData;
}

/**
 * utf-8格式字符串转Uint8Array
 * @param str
 * @returns Uint8Array
 */
function stringToUint8Array(str: string | undefined) {
  return new Uint8Array(buffer.from(str, 'utf-8').buffer);
}

async function encryptSM2BySpecifiedKeyPair(encryptOption: SM2Cipher): Promise<string> {
  let pubKeyBlob: cryptoFramework.DataBlob | null = encryptOption.pkData ? { data: encryptOption.pkData } : null;
  let priKeyBlob: cryptoFramework.DataBlob | null = encryptOption.skData ? { data: encryptOption.skData } : null;
  let keyPair = await genKeyPairByData(pubKeyBlob, priKeyBlob);
  let pubKey = keyPair.pubKey;
  // 把字符串按utf-8解码为Uint8Array
  let plainTextBlob: cryptoFramework.DataBlob = { data: stringToUint8Array(encryptOption.plainText) };
  let encryptText = await encryptMessage(pubKey, plainTextBlob);
  // 进行base64编码用于网络传输
  let encryptData = base64Helper.encodeToStringSync(encryptText.data);

  return encryptData;
}
async function convertStrToPubKey(publicKeyStr: string): Promise<cryptoFramework.PubKey> {
  let pubKeyStr = publicKeyStr.startsWith('04') ? publicKeyStr.slice(2) : publicKeyStr;
  let pkPart1 = pubKeyStr.slice(0, pubKeyStr.length / 2);
  let pkPart2 = pubKeyStr.slice(pubKeyStr.length / 2);
  let pk: cryptoFramework.Point = {
    x: BigInt('0x' + pkPart1),
    y: BigInt('0x' + pkPart2),
  };
  let pubKeySpec: cryptoFramework.ECCPubKeySpec = {
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    pk: pk,
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
  };
  let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(pubKeySpec);
  return await keypairGenerator.generatePubKey();
}
/**
 * 解密
 * @param cipherTransform 加解密算法
 * @param key 密钥
 * @param plainText 加密后的字符串
 * @returns 解密后数据
 */
async function decryptMessage(key: cryptoFramework.Key, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('SM2_256|SM3');
  await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, key, null);
  let decryptData = await decoder.doFinal(cipherText);
  return decryptData;
}

/**
 * Uint8Array转字符串
 * @param Uint8Array array
 * @returns 转化后的字符串
 */
function uint8ArrayToString(array: Uint8Array): string {
  // 将UTF-8编码转换成Unicode编码
  let out: string = '';
  let index: number = 0;
  let len: number = array.length;
  while (index < len) {
    let character = array[index++];
    switch (character >> 4) {
      case 0:
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
      case 6:
      case 7:
        out += String.fromCharCode(character);
        break;
      case 12:
      case 13:
        out += String.fromCharCode(((character & 0x1F) << 6) | (array[index++] & 0x3F));
        break;
      case 14:
        out += String.fromCharCode(((character & 0x0F) << 12) | ((array[index++] & 0x3F) << 6) |
          ((array[index++] & 0x3F) << 0));
        break;
      default:
        break;
    }
  }
  return out;
}

/**
 * 根据指定密钥进行SM2解密
 * @param decryptOption 解密的数据对象
 * @returns 解密后数据
 */
async function decryptSM2BySpecifiedKeyPair(decryptOption: SM2Cipher): Promise<string> {
  let encryptStr = decryptOption.encryptedStr || '';
  let plainMessage = base64Helper.decodeSync(encryptStr);
  let pubKeyBlob: cryptoFramework.DataBlob | null = decryptOption.pkData ? { data: decryptOption.pkData } : null;
  let priKeyBlob: cryptoFramework.DataBlob | null = decryptOption.skData ? { data: decryptOption.skData } : null;
  let keyPair = await genKeyPairByData(pubKeyBlob, priKeyBlob);
  let priKey = keyPair.priKey;
  // 把字符串按utf-8解码为Uint8Array
  let plainTextBlob: cryptoFramework.DataBlob = { data: plainMessage };
  let decryptText = await decryptMessage(priKey, plainTextBlob);
  let decryptData = uint8ArrayToString(decryptText.data);
  return decryptData;
}

/**
 * 根据私钥参数生成SM2私钥
 * @param privateKeyStr 十六进制的字符串
 * @returns 生成的密钥
 */
async function convertStrToPriKey(privateKeyStr: string): Promise<cryptoFramework.PriKey> {
  let sk = BigInt('0x' + privateKeyStr);
  let priKeySpec: cryptoFramework.ECCPriKeySpec = {
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    sk: sk,
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.PRIVATE_KEY_SPEC
  };
  let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(priKeySpec);
  return await keypairGenerator.generatePriKey();
}

@Entry
@Component
struct Index {
  plainText: string = '加密测试文本';
  SM2Text: string = '';
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    Column() {
      Row() {
        Button('测试SM2加密').onClick(async () => {
          let pkData1 = (await convertStrToPubKey(pkData)).getEncoded().data;
          const encryptData: SM2Cipher = {
            plainText: this.plainText,
            pkData: pkData1,
            skData: null,
          };
          this.SM2Text = await encryptSM2BySpecifiedKeyPair(encryptData);
          this.promptAction.showToast({ message: 'SM2加密密文：' + this.SM2Text });
        })

        Button('测试SM2解密').onClick(async () => {
          let pkData1 = (await convertStrToPubKey(pkData)).getEncoded().data;
          let skData1 = (await convertStrToPriKey(skData)).getEncoded().data;
          const decryptData: SM2Cipher = {
            encryptedStr: this.SM2Text,
            pkData: pkData1,
            skData: skData1,
          };
          let plainText = await decryptSM2BySpecifiedKeyPair(decryptData);
          this.promptAction.showToast({ message: 'SM2解密明文= ' + plainText });
        })
      }.width('100%')
      .justifyContent(FlexAlign.SpaceAround)
      .alignItems(VerticalAlign.Center)

      TextArea({ text: $$this.plainText })
        .margin({top: 10})
    }
  }
}
```
