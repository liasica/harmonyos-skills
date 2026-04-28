---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-cmac
title: 消息认证码计算CMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息认证码 > 消息认证码计算CMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c497351224f7d8041350651d5ff5fd703bf0edd3eaf2f461ac217f0995e9aec6
---

CMAC通过使用分组密码（如AES）和一个密钥生成认证码，确保消息在传输过程中未被篡改。

## 开发步骤

在调用update接口传入数据时，可以[一次性传入所有数据](crypto-compute-cmac.md#cmac一次性传入数据)，也可以把数据人工分段，然后[分段update](crypto-compute-cmac.md#分段cmac)。对于同一段数据而言，是否分段，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

### CMAC（一次性传入数据）

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac18)，指定消息认证码算法为CMAC，指定对称算法为AES128，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)和[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为AES256的对称密钥（SymKey）。

   生成对称密钥的详细开发指导，请参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-6)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-8)，传入自定义消息，进行消息认证码计算。单次update的长度没有限制。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-2)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac长度，单位为字节。

* 以使用await方式一次性传入数据，获取消息认证码计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  7. let symKey = await aesGenerator.convertKey(symKeyBlob);
  8. console.info('convertKey result: success.');
  9. return symKey;
  10. }
  11. async function doCmac() {
  12. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节。
  13. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  14. let key = await genSymKeyByData(keyData);
  15. let spec: cryptoFramework.CmacSpec = {
  16. algName: 'CMAC',
  17. cipherName: 'AES128',
  18. };
  19. let message = 'cmacTestMessage'; // 待进行CMAC的数据。
  20. let mac = cryptoFramework.createMac(spec);
  21. await mac.init(key);
  22. // 数据量不多时，可以一次性更新，将所有数据传入，接口没有入参长度限制。
  23. await mac.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  24. let macResult = await mac.doFinal();
  25. console.info('CMAC result: ' + macResult.data);
  26. let macLen = mac.getMacLength();
  27. console.info('CMAC len: ' + macLen);
  28. }
  ```

  [Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/CMACSingleTime/Async.ets#L15-L46)
* 以使用同步方式一次性传入数据，获取消息认证码计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  7. let symKey =  aesGenerator.convertKeySync(symKeyBlob);
  8. console.info('[Sync]convertKey result: success.');
  9. return symKey;
  10. }
  11. function doCmacBySync() {
  12. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节。
  13. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  14. let key = genSymKeyByData(keyData);
  15. let spec: cryptoFramework.CmacSpec = {
  16. algName: 'CMAC',
  17. cipherName: 'AES128',
  18. };
  19. let message = 'cmacTestMessage'; // 待进行CMAC的数据。
  20. let mac = cryptoFramework.createMac(spec);
  21. mac.initSync(key);
  22. // 数据量不大时，可以一次性更新，将所有数据传入，接口没有入参长度限制。
  23. mac.updateSync({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  24. let macResult = mac.doFinalSync();
  25. console.info('[Sync]CMAC result: ' + macResult.data);
  26. let macLen = mac.getMacLength();
  27. console.info('CMAC len: ' + macLen);
  28. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/CMACSingleTime/Sync.ets#L15-L46)

### 分段CMAC

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac18)，指定消息认证码算法CMAC，对称算法AES256，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为AES256的对称密钥（SymKey）。

   生成对称密钥的详细开发指导，请参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-7)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 传入自定义消息，设置每次传入数据量为20字节，多次调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-9)，计算消息认证码。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-3)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac消息认证码的长度，单位为字节。

* 以使用await方式分段传入数据，获取消息认证码计算结果为例。

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  7. let symKey = await aesGenerator.convertKey(symKeyBlob);
  8. console.info('convertKey result: success.');
  9. return symKey;
  10. }
  11. async function doLoopCmac() {
  12. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节。
  13. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  14. let key = await genSymKeyByData(keyData);
  15. let spec: cryptoFramework.CmacSpec = {
  16. algName: 'CMAC',
  17. cipherName: 'AES128',
  18. };
  19. let mac = cryptoFramework.createMac(spec);
  20. // 假设消息共43字节，根据UTF-8解码后，仍是43字节。
  21. let messageText = 'aaaaa......bbbbb......ccccc......ddddd......eee';
  22. let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
  23. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无具体要求。
  24. await mac.init(key);
  25. for (let i = 0; i < messageData.length; i += updateLength) {
  26. let updateMessage = messageData.subarray(i, i + updateLength);
  27. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  28. await mac.update(updateMessageBlob);
  29. }
  30. let macOutput = await mac.doFinal();
  31. console.info('CMAC result: ' + macOutput.data);
  32. let macLen = mac.getMacLength();
  33. console.info('CMAC len: ' + macLen);
  34. }
  ```

  [Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/CMACSegmentation/Async.ets#L16-L53)
* 以使用同步方式分段传入数据，获取消息认证码计算结果为例。

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  7. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  8. console.info('[Sync]convertKey result: success.');
  9. return symKey;
  10. }
  11. function doLoopCmacBySync() {
  12. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节。
  13. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  14. let key = genSymKeyByData(keyData);
  15. let spec: cryptoFramework.CmacSpec = {
  16. algName: 'CMAC',
  17. cipherName: 'AES128',
  18. };
  19. let mac = cryptoFramework.createMac(spec);
  20. // 假设信息共43字节，utf-8解码后仍为43字节。
  21. let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
  22. let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
  23. let updateLength = 20; // 假设以20字节为单位进行分段update，实际没有具体要求。
  24. mac.initSync(key);
  25. for (let i = 0; i < messageData.length; i += updateLength) {
  26. let updateMessage = messageData.subarray(i, i + updateLength);
  27. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  28. mac.updateSync(updateMessageBlob);
  29. }
  30. let macOutput = mac.doFinalSync();
  31. console.info('[Sync]CMAC result: ' + macOutput.data);
  32. let macLen = mac.getMacLength();
  33. console.info('CMAC len: ' + macLen);
  34. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/CMACSegmentation/Sync.ets#L15-L51)
