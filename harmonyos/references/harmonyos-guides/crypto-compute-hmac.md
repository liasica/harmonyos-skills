---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-hmac
title: 消息认证码计算HMAC(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息认证码计算介绍及算法规格 > 消息认证码计算HMAC(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:52a59a232296b4ae2bb4b6fb8a58d3aca5719a8c8b0e66269b9fc897ea661ead
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

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  async function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let hmacGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
    let symKey = await hmacGenerator.convertKey(symKeyBlob);
    console.info('convertKey result: success.');
    return symKey;
  }

  async function doHmac() {
    // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
    let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
    let key = await genSymKeyByData(keyData);
    let macAlgName = 'SHA256'; // 摘要算法名
    let message = 'hmacTestMessage'; // 待进行HMAC的数据
    let mac = cryptoFramework.createMac(macAlgName);
    await mac.init(key);
    // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
    await mac.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
    let macResult = await mac.doFinal();
    console.info('HMAC result: ' + macResult.data);
    let macLen = mac.getMacLength();
    console.info('HMAC len: ' + macLen);
  }
  ```
* 以使用同步方式一次性传入数据，获取消息认证码计算结果为例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let hmacGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
    let symKey = hmacGenerator.convertKeySync(symKeyBlob);
    console.info('[Sync]convertKey result: success.');
    return symKey;
  }

  function doHmacBySync() {
    // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
    let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
    let key = genSymKeyByData(keyData);
    let macAlgName = 'SHA256'; // 摘要算法名
    let message = 'hmacTestMessage'; // 待进行HMAC的数据
    let mac = cryptoFramework.createMac(macAlgName);
    mac.initSync(key);
    // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制
    mac.updateSync({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
    let macResult = mac.doFinalSync();
    console.info('[Sync]HMAC result: ' + macResult.data);
    let macLen = mac.getMacLength();
    console.info('HMAC len: ' + macLen);
  }
  ```

### 分段HMAC

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac)，指定摘要算法SHA256，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)和[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为HMAC的对称密钥（SymKey）。

   生成对称密钥的开发指导，请参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-7)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 传入自定义消息，将一次传入数据量设置为20字节，多次调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-9)，进行消息认证码计算。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-3)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac消息认证码的长度，单位为字节。

* 使用await方式分段传入数据，获取消息认证码计算结果。

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  async function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let hmacGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
    let symKey = await hmacGenerator.convertKey(symKeyBlob);
    console.info('convertKey result: success.');
    return symKey;
  }

  async function doLoopHmac() {
    // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
    let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
    let key = await genSymKeyByData(keyData);
    let macAlgName = 'SHA256'; // 摘要算法名
    let mac = cryptoFramework.createMac(macAlgName);
    // 假设信息总共43字节，根据utf-8解码后，也是43字节
    let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
    let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
    let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
    await mac.init(key);
    for (let i = 0; i < messageData.length; i += updateLength) {
      let updateMessage = messageData.subarray(i, i + updateLength);
      let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
      await mac.update(updateMessageBlob);
    }
    let macOutput = await mac.doFinal();
    console.info('HMAC result: ' + macOutput.data);
    let macLen = mac.getMacLength();
    console.info('HMAC len: ' + macLen);
  }
  ```
* 使用同步方式分段传入数据，获取消息认证码计算结果。

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let hmacGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
    let symKey = hmacGenerator.convertKeySync(symKeyBlob);
    console.info('[Sync]convertKey result: success.');
    return symKey;
  }

  function doLoopHmacBySync() {
    // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节
    let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
    let key = genSymKeyByData(keyData);
    let macAlgName = 'SHA256'; // 摘要算法名
    let mac = cryptoFramework.createMac(macAlgName);
    // 假设信息总共43字节，根据utf-8解码后，也是43字节
    let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
    let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
    let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
    mac.initSync(key);
    for (let i = 0; i < messageData.length; i += updateLength) {
      let updateMessage = messageData.subarray(i, i + updateLength);
      let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
      mac.updateSync(updateMessageBlob);
    }
    let macOutput = mac.doFinalSync();
    console.info('[Sync]HMAC result: ' + macOutput.data);
    let macLen = mac.getMacLength();
    console.info('HMAC len: ' + macLen);
  }
  ```

### HMAC（HmacSpec作为参数传入）

1. 调用[cryptoFramework.createMac](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemac)，指定消息认证码算法HMAC，指定摘要算法SHA256，生成消息认证码实例（Mac）。
2. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)和[SymKeyGenerator.convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-1)，生成密钥算法为HMAC的对称密钥（SymKey）。

   参考[指定二进制数据生成对称密钥](crypto-convert-binary-data-to-sym-key.md)。
3. 调用[Mac.init](../harmonyos-references/js-apis-cryptoframework.md#init-6)，指定共享对称密钥（SymKey），初始化Mac对象。
4. 调用[Mac.update](../harmonyos-references/js-apis-cryptoframework.md#update-8)，传入自定义消息，进行消息认证码计算。单次update长度没有限制。
5. 调用[Mac.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-2)，获取Mac计算结果。
6. 调用[Mac.getMacLength](../harmonyos-references/js-apis-cryptoframework.md#getmaclength)，获取Mac消息认证码的长度，单位为字节。

* 以使用await方式一次性传入数据，获取消息认证码计算结果为例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  async function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let hmacGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
    let symKey = await hmacGenerator.convertKey(symKeyBlob);
    console.info('convertKey result: success.');
    return symKey;
  }
  async function doHmac() {
    // 把字符串按utf-8解码为Uint8Array，使用固定的128位的密钥，即16字节。
    let keyData = new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer);
    let key = await genSymKeyByData(keyData);
    let spec: cryptoFramework.HmacSpec = {
        algName: 'HMAC',
        mdName: 'SHA256',
    };
    let message = 'hmacTestMessage'; // 待进行HMAC的数据。
    let mac = cryptoFramework.createMac(spec);
    await mac.init(key);
    // 数据量较少时，可以只做一次update，将所有数据传入，接口不对参数长度设限。
    await mac.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
    let macResult = await mac.doFinal();
    console.info('HMAC result: ' + macResult.data);
    let macLen = mac.getMacLength();
    console.info('HMAC len: ' + macLen);
  }
  ```
