---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-37
title: 如何解决使用ArkTS的HMACSHA1算法加密后云侧无法解密的问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何解决使用ArkTS的HMACSHA1算法加密后云侧无法解密的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d0902ce3160744b4b14b210e7aa7eba48dc3c0a5dd8f1b43ddfb697a286635f1
---

## 问题现象

因安全需要，应用的关键信息需要在端侧进行加密，在云侧进行解密，以判断数据的合法性，端侧使用的是HMACSHA1算法，使用ArkTS实现得到的加密结果跟云侧Java侧加密结果不一致，导致云侧校验不通过。

* HarmonyOS侧加密的数据为:75,199,73,191,89,193,243,73,224,228,50,209,32,40,108,126,240,52,137,165。HarmonyOS侧核心代码如下：

  ```ts
  let macAlgName = 'SHA1';
  let mac = cryptoFramework.createMac(macAlgName);
  let arr = stringToUint8Array('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
  let KeyBLob: cryptoFramework.DataBlob = { data: arr };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  const symKey = await symKeyGenerator.convertKey(KeyBlob);
  await mac.init(symKey)
  await mac.update({ data: stringToUint8Array(message) });
  let macOutot = await mac.doFinal();
  ```
* 云侧Java加密的数据为:75,-57,73,-65,89,-63,-13,73,-32,-28,58,-47,32,40,108,126,-16,52,-119,-91。Java侧核心代码如下：

  ```java
  public String generateResponseCode(byte[] challenge)
  throws GeneralSecurityException, Base32String.DecodingException {
  String secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
  byte[] keyBytes = secret.getBytes();
  final Mac mac = Mac.getInstance("HMACSHA1");
  mac.init(new SecretKeySpec(keyBytes, ""));
  byte[] hash = mac.doFinal(challenge);
  ```

## 背景知识

[HMAC](../harmonyos-guides/huks-hmac-overview.md)（Hash-based Message Authentication Code）是一种基于哈希的消息认证码算法。

## 问题定位

1. 使用HarmonyOS侧的实现加密数据，在HarmonyOS侧进行解密发现没有问题，证明HarmonyOS侧加密没有问题。
2. 查看HarmonyOS加密的数据和云侧加密的数据，发现128以下的可以对应上，128以上的对应不上，并且HarmonyOS侧减去Java侧正好是256，怀疑是有字符格式问题。
3. 如上可以发现第一个是75，HarmonyOS侧和Java侧都是75，第二个HarmonyOS侧为199，Java侧为-57，区间相差256，同理第三个正常，第四个区间又是相差256。发现Java侧使用的是byte，byte表示范围是-128到127，比如139已经超出了其表示范围，转换过程是由int类型转换为byte类型，有精度丢失，所以是-117。
4. HarmonyOS侧使用了Uint8Array，是一个无符号8位整数数组，它的取值范围是0到255，139在其表示范围内，所以是139。

## 分析结论

ArkTS中Int8Array类型数组表示一个二进制位有符号整数数组。它的取值范围是-128到127。需要将doFinal返回的数组转换为Int8Array的类型以实现与Java侧保持的一致。

## 修改建议

将doFinal返回的Uint8Array数组转换为Int8Array的类型。可以使用Int8Array的构造函数实现，可参考[文档](../harmonyos-references/arkts-apis-arkts-collections-int8array.md#constructor-2)中的示例。

## 总结

1. [Mac类](../harmonyos-references/js-apis-cryptoframework.md#mac)是常用的加解密类，其方法的参数或返回值一般是Uint8Array组成的数组DataBlob，使用该类的方法时会存在类似的问题，需要根据本文所述方案进行转换。
2. Uint8Array类型是ArkTS的常用类型，ArkTS中其他类也有一些方法的返回值是Uint8Array类型，如果出现返回值溢出的问题时可参考本文进行转换。
