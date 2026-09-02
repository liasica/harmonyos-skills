---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt
title: 使用ChaCha20对称密钥加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密介绍 > 使用ChaCha20对称密钥加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea9795ee1890b8010e369e69b35305addbbcc646d818b50918a26130494b02cc
---

从API版本22开始，算法库支持该算法。

对应的算法规格请查看[对称密钥加解密算法规格：ChaCha20](crypto-encryption-decryption.md#chacha20)。

## 使用ChaCha20对称密钥加解密

**创建对象**

调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为ChaCha20的对称密钥（SymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：ChaCha20](crypto-key-generation-conversion.md#chacha20)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解。参考文档与示例可能存在入参差异，请注意区分。

**加密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20'，创建对称密钥的Cipher实例，用于完成加密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和对应的加密参数（IvParamsSpec），初始化加密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   **说明** 

   由于已使用update传入数据，此处data传入null。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20'，创建对称密钥的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和对应的解密参数（IvParamsSpec），初始化解密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（密文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

* 异步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function generateRandom(len: number) {
    let rand = cryptoFramework.createRandom();
    let generateRandSync = rand.generateRandomSync(len);
    return generateRandSync;
  }

  function genIvParamsSpec() {
    let ivBlob = generateRandom(16);
    let ivParamsSpec: cryptoFramework.IvParamsSpec = {
      algName: 'IvParamsSpec',
      iv: ivBlob
    };
    return ivParamsSpec;
  }
  let ivSpec = genIvParamsSpec();

  // 加密消息。
  async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('ChaCha20');
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivSpec);
    let encryptData = await cipher.doFinal(plainText);
    return encryptData;
  }

  // 解密消息。
  async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('ChaCha20');
    await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivSpec);
    let decryptData = await decoder.doFinal(cipherText);
    return decryptData;
  }

  async function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
    let symKey = await chacha20Generator.convertKey(symKeyBlob);
    console.info('convertKey result: success.');
    return symKey;
  }

  async function main() {
    try {
      let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159, 83,
        217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
      let symKey = await genSymKeyByData(keyData);
      let message = 'This is a test';
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      let encryptText = await encryptMessagePromise(symKey, plainText);
      let decryptText = await decryptMessagePromise(symKey, encryptText);
      if (plainText.data.toString() === decryptText.data.toString()) {
        console.info('decrypt ok.');
        console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
      } else {
        console.error('decrypt failed.');
      }
    } catch (error) {
      console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
    }
  }
  ```
* 同步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function generateRandom(len: number) {
    let rand = cryptoFramework.createRandom();
    let generateRandSync = rand.generateRandomSync(len);
    return generateRandSync;
  }

  function genIvParamsSpec() {
    let ivBlob = generateRandom(16);
    let ivParamsSpec: cryptoFramework.IvParamsSpec = {
      algName: 'IvParamsSpec',
      iv: ivBlob
    };
    return ivParamsSpec;
  }

  let ivSpec = genIvParamsSpec();

  // 加密消息。
  function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('ChaCha20');
    cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, ivSpec);
    let encryptData = cipher.doFinalSync(plainText);
    return encryptData;
  }

  // 解密消息。
  function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('ChaCha20');
    decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, ivSpec);
    let decryptData = decoder.doFinalSync(cipherText);
    return decryptData;
  }

  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
    let symKey = chacha20Generator.convertKeySync(symKeyBlob);
    console.info('convertKeySync result: success.');
    return symKey;
  }

  function main() {
    try {
      let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159, 83,
        217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
      let symKey = genSymKeyByData(keyData);
      let message = 'This is a test';
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      let encryptText = encryptMessage(symKey, plainText);
      let decryptText = decryptMessage(symKey, encryptText);
      if (plainText.data.toString() === decryptText.data.toString()) {
        console.info('decrypt ok.');
        console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
      } else {
        console.error('decrypt failed.');
      }
    } catch (error) {
      console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
    }
  }
  ```

## 使用ChaCha20对称密钥（Poly1305模式）加解密

**创建对象**

调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为ChaCha20的对称密钥（SymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：ChaCha20](crypto-key-generation-conversion.md#chacha20)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解。参考文档与示例可能存在入参差异，请注意区分。

**加密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成加密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和Poly1305模式对应的加密参数（Poly1305ParamsSpec），初始化加密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   **说明** 

   由于已使用update传入数据，此处data传入null。

   doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
5. 读取[Poly1305ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#poly1305paramsspec22).authTag作为解密的认证信息。

   在Poly1305模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'ChaCha20|Poly1305'，创建对称密钥类型为ChaCha20、模式为Poly1305的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和Poly1305模式对应的解密参数（Poly1305ParamsSpec），初始化解密Cipher实例。
3. 调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（密文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

ChaCha20（Poly1305模式）解密失败返回错误码17630001可参考[使用ChaCha20-Poly1305算法解密时调用doFinal失败](../harmonyos-references/errorcode-crypto-framework.md#使用chacha20-poly1305算法解密时调用dofinal失败)

* 异步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function generateRandom(len: number) {
    let rand = cryptoFramework.createRandom();
    let generateRandSync = rand.generateRandomSync(len);
    return generateRandSync;
  }

  function genPoly1305ParamsSpec() {
    let ivBlob = generateRandom(12); // 12 bytes
    let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
    let dataAad = new Uint8Array(arr);
    let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
    let dataTag = new Uint8Array(arr);
    let tagBlob: cryptoFramework.DataBlob = {
      data: dataTag
    };
    // Poly1305的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中。
    let poly1305ParamsSpec: cryptoFramework.Poly1305ParamsSpec = {
      iv: ivBlob,
      aad: aadBlob,
      authTag: tagBlob,
      algName: 'Poly1305ParamsSpec'
    };
    return poly1305ParamsSpec;
  }

  let poly1305Params = genPoly1305ParamsSpec();

  // 加密消息。
  async function encryptMessagePromise(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('ChaCha20|Poly1305');
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, poly1305Params);
    let encryptUpdate = await cipher.update(plainText);
    // poly1305模式加密doFinal时传入空，获得tag数据，并更新至poly1305Params对象中。
    poly1305Params.authTag = await cipher.doFinal(null);
    return encryptUpdate;
  }
  // 解密消息。
  async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('ChaCha20|Poly1305');
    await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, poly1305Params);
    let decryptUpdate = await decoder.update(cipherText);
    // poly1305模式解密doFinal时传入空，验证init时传入的tag数据，如果验证失败会抛出异常。
    let decryptData = await decoder.doFinal(null);
    if (decryptData === null) {
      console.info('poly1305 decrypt result: success, decryptData is null.');
    }
    return decryptUpdate;
  }
  async function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
    let symKey = await chacha20Generator.convertKey(symKeyBlob);
    console.info('convertKey result: success.');
    return symKey;
  }
  async function main() {
    try {
      let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159,
        83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
      let symKey = await genSymKeyByData(keyData);
      let message = 'This is a test';
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      let encryptText = await encryptMessagePromise(symKey, plainText);
      let decryptText = await decryptMessagePromise(symKey, encryptText);
      if (plainText.data.toString() === decryptText.data.toString()) {
        console.info('decrypt ok.');
        console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
      } else {
        console.error('decrypt failed.');
      }
    } catch (error) {
      console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
    }
  }
  ```
* 同步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  function generateRandom(len: number) {
    let rand = cryptoFramework.createRandom();
    let generateRandSync = rand.generateRandomSync(len);
    return generateRandSync;
  }

  function genPoly1305ParamsSpec() {
    let ivBlob = generateRandom(12); // 12 bytes
    let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
    let dataAad = new Uint8Array(arr);
    let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
    let dataTag = new Uint8Array(arr);
    let tagBlob: cryptoFramework.DataBlob = {
      data: dataTag
    };
    // Poly1305的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中。
    let poly1305ParamsSpec: cryptoFramework.Poly1305ParamsSpec = {
      iv: ivBlob,
      aad: aadBlob,
      authTag: tagBlob,
      algName: 'Poly1305ParamsSpec'
    };
    return poly1305ParamsSpec;
  }

  let poly1305Params = genPoly1305ParamsSpec();

  // 加密消息。
  function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('ChaCha20|Poly1305');
    cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, poly1305Params);
    let encryptUpdate = cipher.updateSync(plainText);
    // poly1305模式加密doFinal时传入空，获得tag数据，并更新至poly1305Params对象中。
    poly1305Params.authTag = cipher.doFinalSync(null);
    return encryptUpdate;
  }
  // 解密消息。
  function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('ChaCha20|Poly1305');
    decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, poly1305Params);
    let decryptUpdate = decoder.updateSync(cipherText);
    // poly1305模式解密doFinal时传入空，验证init时传入的tag数据，如果验证失败会抛出异常。
    let decryptData = decoder.doFinalSync(null);
    if (decryptData === null) {
      console.info('poly1305 decrypt result: success, decryptData is null.');
    }
    return decryptUpdate;
  }
  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let chacha20Generator = cryptoFramework.createSymKeyGenerator('ChaCha20');
    let symKey = chacha20Generator.convertKeySync(symKeyBlob);
    console.info('convertKeySync result: success.');
    return symKey;
  }
  function main() {
    try {
      let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159,
        83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
      let symKey = genSymKeyByData(keyData);
      let message = 'This is a test';
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      let encryptText = encryptMessage(symKey, plainText);
      let decryptText = decryptMessage(symKey, encryptText);
      if (plainText.data.toString() === decryptText.data.toString()) {
        console.info('decrypt ok.');
        console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
      } else {
        console.error('decrypt failed.');
      }
    } catch (error) {
      console.error(`decrypt failed: errCode: ${error.code}, message: ${error.message}`);
    }
  }
  ```
