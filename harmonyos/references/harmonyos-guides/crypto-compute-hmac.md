---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac
title: 消息认证码计算HMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息认证码 > 消息认证码计算HMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:40+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:96f9702fca419ffd47a973090242ef73768958a339c40c3a0c67829dbabbf479
---

HMAC使用指定的摘要算法，以共享密钥和消息作为输入，生成固定长度的消息认证码，用于检验报文的完整性。HMAC在消息摘要算法基础上增加密钥输入，确保信息正确性。

## 开发步骤

在调用update接口传入数据时，可以[一次性传入所有数据](crypto-compute-hmac.md#hmac一次性传入)，也可以把数据人工分段，然后[分段update](crypto-compute-hmac.md#分段hmac)。对于同一段数据而言，是否分段，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

### HMAC（一次性传入）

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac)，指定摘要算法SHA256，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为HMAC的对称密钥（SymKey）。

   详细开发指导请参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-6)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-8)，传入自定义消息，进行消息认证码计算。单次update长度没有限制。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-2)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac消息认证码的长度，单位为字节。

* 以使用await方式一次性传入数据，获取消息认证码计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  7. let symKey = await aesGenerator.convertKey(symKeyBlob);
  8. console.info('convertKey result: success.');
  9. return symKey;
  10. }

  12. async function doLoopHmac() {
  13. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
  14. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  15. let key = await genSymKeyByData(keyData);
  16. let macAlgName = 'SHA256'; // 摘要算法名
  17. let mac = cryptoFramework.createMac(macAlgName);
  18. // 假设信息总共43字节，根据utf-8解码后，也是43字节
  19. let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
  20. let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
  21. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
  22. await mac.init(key);
  23. for (let i = 0; i < messageData.length; i += updateLength) {
  24. let updateMessage = messageData.subarray(i, i + updateLength);
  25. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  26. await mac.update(updateMessageBlob);
  27. }
  28. let macOutput = await mac.doFinal();
  29. console.info('HMAC result: ' + macOutput.data);
  30. let macLen = mac.getMacLength();
  31. console.info('HMAC len: ' + macLen);
  32. }
  ```

  [Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/HMACSingleTime/Async.ets#L15-L50)
* 以使用同步方式一次性传入数据，获取消息认证码计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  7. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  8. console.info('[Sync]convertKey result: success.');
  9. return symKey;
  10. }

  12. function doLoopHmacBySync() {
  13. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
  14. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  15. let key = genSymKeyByData(keyData);
  16. let macAlgName = 'SHA256'; // 摘要算法名
  17. let mac = cryptoFramework.createMac(macAlgName);
  18. // 假设信息总共43字节，根据utf-8解码后，也是43字节
  19. let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
  20. let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
  21. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
  22. mac.initSync(key);
  23. for (let i = 0; i < messageData.length; i += updateLength) {
  24. let updateMessage = messageData.subarray(i, i + updateLength);
  25. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  26. mac.updateSync(updateMessageBlob);
  27. }
  28. let macOutput = mac.doFinalSync();
  29. console.info('[Sync]HMAC result: ' + macOutput.data);
  30. let macLen = mac.getMacLength();
  31. console.info('HMAC len: ' + macLen);
  32. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/HMACSingleTime/Sync.ets#L15-L50)

### 分段HMAC

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac)，指定摘要算法SHA256，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)和[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为HMAC的对称密钥（SymKey）。

   生成对称密钥的开发指导，请参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-7)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 传入自定义消息，将一次传入数据量设置为20字节，多次调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-9)，进行消息认证码计算。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-3)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac消息认证码的长度，单位为字节。

* 使用await方式分段传入数据，获取消息认证码计算结果。

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  7. let symKey = await aesGenerator.convertKey(symKeyBlob);
  8. console.info('convertKey result: success.');
  9. return symKey;
  10. }

  12. async function doHmac() {
  13. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
  14. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  15. let key = await genSymKeyByData(keyData);
  16. let macAlgName = 'SHA256'; // 摘要算法名
  17. let message = 'hmacTestMessage'; // 待进行HMAC的数据
  18. let mac = cryptoFramework.createMac(macAlgName);
  19. await mac.init(key);
  20. // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
  21. await mac.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  22. let macResult = await mac.doFinal();
  23. console.info('HMAC result: ' + macResult.data);
  24. let macLen = mac.getMacLength();
  25. console.info('HMAC len: ' + macLen);
  26. }
  ```

  [Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/HMACSegmentation/Async.ets#L16-L45)
* 使用同步方式分段传入数据，获取消息认证码计算结果。

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  7. let symKey = aesGenerator.convertKeySync(symKeyBlob);
  8. console.info('[Sync]convertKey result: success.');
  9. return symKey;
  10. }

  12. function doHmacBySync() {
  13. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
  14. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  15. let key = genSymKeyByData(keyData);
  16. let macAlgName = 'SHA256'; // 摘要算法名
  17. let message = 'hmacTestMessage'; // 待进行HMAC的数据
  18. let mac = cryptoFramework.createMac(macAlgName);
  19. mac.initSync(key);
  20. // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
  21. mac.updateSync({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  22. let macResult = mac.doFinalSync();
  23. console.info('[Sync]HMAC result: ' + macResult.data);
  24. let macLen = mac.getMacLength();
  25. console.info('HMAC len: ' + macLen);
  26. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageAuthenticationCode/entry/src/main/ets/pages/HMACSegmentation/Sync.ets#L15-L43)

### HMAC(HmacSpec作为参数传入)

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac)，指定消息认证码算法HMAC，指定摘要算法SHA256，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)和[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为HMAC的对称密钥（SymKey）。

   参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-6)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-8)，传入自定义消息，进行消息认证码计算。单次update长度没有限制。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-2)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac消息认证码的长度，单位为字节。

* 以使用await方式一次性传入数据，获取消息认证码计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function genSymKeyByData(symKeyData: Uint8Array) {
  5. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  6. let aesGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  7. let symKey = await aesGenerator.convertKey(symKeyBlob);
  8. console.info('convertKey success');
  9. return symKey;
  10. }
  11. async function doHmac() {
  12. // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节。
  13. let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
  14. let key = await genSymKeyByData(keyData);
  15. let spec: cryptoFramework.HmacSpec = {
  16. algName: 'HMAC',
  17. mdName: 'SHA256',
  18. };
  19. let message = 'hmacTestMessage'; // 待进行HMAC的数据。
  20. let mac = cryptoFramework.createMac(spec);
  21. await mac.init(key);
  22. // 数据量较少时，可以只做一次update，将所有数据传入，接口不对参数长度设限。
  23. await mac.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  24. let macResult = await mac.doFinal();
  25. console.info('HMAC result:' + macResult.data);
  26. let macLen = mac.getMacLength();
  27. console.info('HMAC len:' + macLen);
  28. }
  ```
