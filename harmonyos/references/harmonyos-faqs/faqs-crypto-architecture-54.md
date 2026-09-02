---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-54
title: SM4加解密CTR的分组模式使用IVParamsSpec参数后加解密失败
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > SM4加解密CTR的分组模式使用IVParamsSpec参数后加解密失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f22d88dc8a05fabe5c143777e2974f2ea75a07dd0c77448ff79fa67fcdd2b081
---

## 问题现象

使用SM4加解密算法采用CTR的分组模式，在增加iv参数后，加密后的结果不对，导致解密失败。

加解密代码参考如下：

```ts
// 加密消息。
async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('SM4_128|CTR|NoPadding');
  let smIV = '12345678'
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: "IvParamsSpec",
    iv: { data: new Uint8Array(buffer.from(smIV, 'utf-8').buffer) }
  };
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivParamsSpec);
  let encryptData = await cipher.doFinal(plainText);
  return encryptData;
}

// 解密消息。
async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('SM4_128|CTR|NoPadding');
  let smIV = '12345678'
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: "IvParamsSpec",
    iv: { data: new Uint8Array(buffer.from(smIV, 'utf-8').buffer) }
  };
  await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivParamsSpec);
  let decryptData = await decoder.doFinal(cipherText);
  return decryptData;
}
```

报错信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/SQJla1kLTHWX5zv_5E3hTg/zh-cn_image_0000002658968435.png "点击放大")

## 背景知识

算法库当前提供了[SM4](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#sm4)加解密常用的7种加密模式：ECB、CBC、CTR、OFB、CFB、CFB128和GCM。不同的加密模式适用的加解密参数不同，具体请参考[ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#paramsspec)。

## 问题定位

1. 检查创建加解密实例时传入的参数是否正确。
2. 检查加解密实例init初始化执行时传入的参数是否正确。
3. 检查传入的IVParamsSpec参数是否符合要求。

## 分析结论

传入的IVParamsSpec参数为8个字节，加解密参数中的IVParamsSpec参数要求为16字节，传入的IVParamsSpec参数长度不对导致加解密报错。

## 修改建议

加解密参数中的[IVParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#ivparamsspec)参数长度修改为16字节。

## 常见FAQ

Q：加解密时随机生成的IVParamsSpec参数长度一致，解密失败为什么？

A：需要保证加解密使用的随机生成IVParamsSpec参数一致，不一致将会导致解密失败。

Q：SM4加密在有padding的情况下，加密的字节位数是否固定，固定的是多少？

A：SM4为分组加密算法，分组长度固定为128位，在实际应用中，有padding的情形下，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。

## 总结

IVParamsSpec参数为进行加解密时的数据偏移量，不同加解密算法及其分组模式对此参数的要求不一致，需要使用此参数参与加解密时需要保证此参数符合所使用的加解密算法及其分组模式的要求。
