---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-binary-data-to-sym-key
title: 指定二进制数据转换对称密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定二进制数据转换对称密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:395cf2c152e3cf98b8eeffa4699345b8418520c84d70ada0541935b46da94505
---

以3DES和HMAC为例，根据指定的对称密钥二进制数据，生成对称密钥对象（SymKey），即将外部或存储的二进制数据转换为算法库的密钥对象，该对象可用于后续的加解密等操作。

## 指定二进制数据转换3DES密钥

对应的算法规格请查看[对称密钥生成和转换规格：3DES](crypto-sym-key-generation-conversion-spec.md#section3des)。

1. 获取3DES二进制密钥数据，封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)，指定字符串参数'3DES192'，创建密钥算法为3DES、密钥长度为192位的对称密钥生成器（SymKeyGenerator）。
3. 调用[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，根据指定的对称密钥二进制数据生成对称密钥对象（SymKey）。
4. 调用[SymKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)，获取密钥对象的二进制数据。

* 以使用callback方式生成3DES密钥为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  5. let arr = [
  6. 0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
  7. 0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
  8. 0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // 密钥长度为192位，即24字节。
  9. let keyMaterial = new Uint8Array(arr);
  10. return { data: keyMaterial };
  11. }

  13. function testConvertSymKey() {
  14. // 创建SymKeyGenerator实例
  15. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  16. // 根据指定的数据生成对称密钥
  17. let keyMaterialBlob = genKeyMaterialBlob();
  18. try {
  19. symKeyGenerator.convertKey(keyMaterialBlob, (error, key) => {
  20. if (error) { // 如果业务逻辑执行失败，则callback的第一个参数返回错误信息，即异步抛出异常
  21. let e: BusinessError = error as BusinessError;
  22. console.error(`convertKey failed: errCode: ${e.code}, message: ${e.message}`);
  23. return;
  24. }
  25. console.info('key algName: ' + key.algName);
  26. console.info('key format: ' + key.format);
  27. let encodedKey = key.getEncoded(); // 获取对称密钥的二进制数据，并以字节数组形式输出。长度为24字节
  28. console.info('key getEncoded hex: ' + encodedKey.data);
  29. })
  30. } catch (error) { // 参数检查发现错误立即抛出异常
  31. let e: BusinessError = error as BusinessError;
  32. console.error(`convertKey failed: errCode: ${e.code}, message: ${e.message}`);
  33. }
  34. }
  ```

  [Callback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSymmetricKeyBinaryFormatArkTS/entry/src/main/ets/pages/3des/Callback.ets#L16-L51)
* 同步方法（调用方法[convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  5. let arr = [
  6. 0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
  7. 0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
  8. 0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // 密钥长度为192位，即24字节。
  9. let keyMaterial = new Uint8Array(arr);
  10. return { data: keyMaterial };
  11. }

  13. function testConvertSymKey() {
  14. // 创建SymKeyGenerator实例
  15. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  16. // 根据指定的数据生成对称密钥
  17. let keyMaterialBlob = genKeyMaterialBlob();
  18. try {
  19. symKeyGenerator.convertKey(keyMaterialBlob, (error, key) => {
  20. if (error) { // 如果业务逻辑执行失败，则callback的第一个参数返回错误信息，即异步抛出异常
  21. let e: BusinessError = error as BusinessError;
  22. console.error(`convertKey failed: errCode: ${e.code}, message: ${e.message}`);
  23. return;
  24. }
  25. console.info('key algName: ' + key.algName);
  26. console.info('key format: ' + key.format);
  27. let encodedKey = key.getEncoded(); // 获取对称密钥的二进制数据，并以字节数组形式输出。长度为24字节
  28. console.info('key getEncoded hex: ' + encodedKey.data);
  29. })
  30. } catch (error) { // 参数检查发现错误立即抛出异常
  31. let e: BusinessError = error as BusinessError;
  32. console.error(`convertKey failed: errCode: ${e.code}, message: ${e.message}`);
  33. }
  34. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSymmetricKeyBinaryFormatArkTS/entry/src/main/ets/pages/3des/Sync.ets#L16-L51)

## 指定二进制数据转换HMAC密钥

请查看[对称密钥生成和转换规格：HMAC](crypto-sym-key-generation-conversion-spec.md#hmac)。

1. 获取HMAC二进制密钥并封装成[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)，指定字符串参数'HMAC'，创建密钥算法为HMAC、密钥长度为[1, 32768]位的对称密钥生成器（SymKeyGenerator）。
3. 调用[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，根据指定的对称密钥二进制数据，生成对称密钥对象（SymKey）。
4. 调用[SymKey.getEncoded](../harmonyos-references/js-apis-cryptoframework.md#getencoded)，获取密钥的二进制数据。

* 以生成HMAC密钥为例，使用await方式：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function testConvertHmacKey() {
  5. // 对称密钥长度为64字节，512比特
  6. let keyMessage = '12345678abcdefgh12345678abcdefgh12345678abcdefgh12345678abcdefgh';
  7. let keyBlob: cryptoFramework.DataBlob = {
  8. data: new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
  9. }
  10. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  11. let key = await symKeyGenerator.convertKey(keyBlob);
  12. let encodedKey = key.getEncoded();
  13. console.info('key encoded data: ' + encodedKey.data);
  14. }
  ```

  [Await.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSymmetricKeyBinaryFormatArkTS/entry/src/main/ets/pages/hmac/Await.ets#L16-L31)
* 同步方法（调用方法[convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function testConvertKeySync() {
  5. // 对称密钥长度为64字节，512比特
  6. let keyMessage = '12345678abcdefgh12345678abcdefgh12345678abcdefgh12345678abcdefgh';
  7. let keyBlob: cryptoFramework.DataBlob = {
  8. data : new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
  9. }
  10. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  11. let key = symKeyGenerator.convertKeySync(keyBlob);
  12. let encodedKey = key.getEncoded();
  13. console.info('key encoded data: ' + encodedKey.data);
  14. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSymmetricKeyBinaryFormatArkTS/entry/src/main/ets/pages/hmac/Sync.ets#L16-L31)
