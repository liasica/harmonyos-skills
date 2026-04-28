---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-platform-compatibility
title: 加解密跨平台数据兼容性
breadcrumb: 最佳实践 > 应用安全 > 加解密跨平台数据兼容性
category: best-practices
scraped_at: 2026-04-28T08:22:17+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c4614d93ef7bab5d25483355fd1e19522181aca218fcdd4e8ad80358e0202348
---

## 概述

为确保数据安全，数据传输过程中需进行加解密操作。实现加密和解密操作在不同环境下的互操作性和跨平台数据的兼容性也极为关键。这一目标受以下两方面影响：

1. 数据编码格式差异：不同平台可能使用不同的数据格式，导致跨平台传输和存储时出现不兼容。
2. 加解密算法使用差异：不同平台支持相同的算法，但算法框架的使用方式会有所不同。

本文从[数据编码格式差异](bpta-cross-platform-compatibility.md#section1152116421582)以及[加解密算法使用差异](bpta-cross-platform-compatibility.md#section61961942185518)两个方面来深入分析加解密失败的可能原因，并提供相应的解决方案，避免跨平台加解密失败，帮助开发者在HarmonyOS平台上高效、准确地完成加解密任务，实现跨平台数据兼容性。

## 加解密开发步骤

加解密通常遵循以下流程：

1. 选择加解密算法并确定密钥
   * 根据具体的安全需求，选择合适的加解密算法。可以是[对称密钥加解密算法](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md)（例如AES）、[非对称密钥加解密算法](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md)（例如RSA）等。
   * 确定加解密所需密钥。对称密钥为随机生成的二进制数据，非对称密钥需生成公钥和私钥。
2. 准备待加解密的数据
   * 明确需要加密的数据，如文本、文件或数据库记录。
   * 对数据进行预处理，如格式化、编码转换，确保符合加密算法的输入要求。
3. 初始化加解密引擎

   根据所选加密算法，初始化加密引擎。设置加密模式（如CBC、ECB）和填充方式等参数，以满足特定安全需求。
4. 执行加解密操作
   * 将明文数据输入加密引擎。
   * 加密引擎根据设定的算法和密钥对数据进行加密，通常逐块处理。对于大文件，可能需要分块加密。
5. 输出结果
   * 加密后得到密文数据。
   * 可以将密文存储在文件或数据库中，或通过网络传输给接收方。

## 数据编码格式差异

加解密操作常跨平台进行，例如服务端加密的数据需在移动设备上解密。HarmonyOS平台的加解密API要求密钥和待处理数据为Uint8Array格式。因此，需将Uint8Array字节数据与其他编码格式数据互相转换，确保编码格式一致。

以下列举三种数据格式之间的转换方法：

* 普通编码格式的字符串与Uint8Array类型的转换

  建议采用UTF-8编码。UTF-8编码广泛支持大多数语言的字符，且在不同平台间具有良好的兼容性。

  ```
  1. // Convert string to uint8Array.
  2. public static stringToUint8Array(str: string): Uint8Array {
  3. let textEncoder = util.TextEncoder.create('utf-8');
  4. return textEncoder.encodeInto(str);
  5. }

  7. // Convert uint8Array to string.
  8. public static uint8ArrayToString(input: Uint8Array): string {
  9. let textDecoder = util.TextDecoder.create('utf-8');
  10. return textDecoder.decodeToString(input);
  11. }
  ```

  [DataConversion.ets](https://gitcode.com/harmonyos_samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L267-L278)

* Base64编码格式字符串与Uint8Array类型的转换

  在HarmonyOS侧接收数据后，先进行Base64解码，将字符串转换为Uint8Array类型的字节流，再进行解密操作。

  反之，如果需要将数据从HarmonyOS侧发送到服务端，需要先将数据加密后的字节流进行Base64编码，转换为字符串后再进行传输。

  ```
  1. // Convert base64 to uint8Array.
  2. public static base64ToUint8Array(str: string): Uint8Array {
  3. let base64Helper = new util.Base64Helper();
  4. return base64Helper.decodeSync(str);
  5. }

  7. // Convert uint8Array to base64.
  8. public static uint8ArrayToBase64(input: Uint8Array): string {
  9. let base64Helper = new util.Base64Helper();
  10. return base64Helper.encodeToStringSync(input);
  11. }
  ```

  [DataConversion.ets](https://gitcode.com/HarmonyOS_Samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L281-L292)

* 16进制编码格式字符串与Uint8Array类型的转换

  ```
  1. // Convert hex to uint8Array.
  2. public static hexStrToUint8Array(data: string): Uint8Array {
  3. return new Uint8Array(buffer.from(data, 'hex').buffer);
  4. }

  6. // Convert uint8Array to hex.
  7. public static uint8ArrayToHexStr(input: Uint8Array): string {
  8. let hexString = '';
  9. for (let i = 0; i < input.length; i++) {
  10. let char = ('00' + input[i].toString(16)).slice(-2);
  11. hexString += char;
  12. }
  13. return hexString;
  14. }
  ```

  [DataConversion.ets](https://gitcode.com/harmonyos_samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L295-L309)

## 加解密算法使用差异

不同平台支持相同的算法，但加解密算法在使用时可能存在差异，这些差异可能导致加解密无法跨平台正常工作。

HarmonyOS平台与其它平台在加解密使用上存在差异。

1. HarmonyOS平台加解密API要求密钥和待处理的数据为Uint8Array格式，可参考[数据编码格式差异](bpta-cross-platform-compatibility.md#section1152116421582)实现数据格式的转换。
2. 在HarmonyOS平台上，默认支持SM2算法。需要注意的是，HarmonyOS仅支持ASN.1格式的数据（如密钥和密文）。因此，SM2算法在跨平台加解密时，需要进行原始裸数据与ASN.1格式数据的转换，包括密钥格式转换和密文格式转换，具体可参考[SM2加解密](bpta-cross-platform-compatibility.md#section48982572218)。
3. HarmonyOS平台在初始化加解密引擎时，需要传入固定的参数，参数格式可参考[加解密算法规格](../harmonyos-guides/crypto-encrypt-decrypt-spec.md)。以AES为例，详细分析密钥长度使用问题和偏移量参数的设置问题，具体可参考[AES加解密](bpta-cross-platform-compatibility.md#section848458172418)。

### SM2加解密

[SM2](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#sm2)，是一种基于椭圆曲线的公钥密码算法。

下面介绍并解决在HarmonyOS平台与其他平台交互使用SM2加解密开发时遇到的密钥格式和密文数据格式问题。

* SM2密钥格式转换

  SM2加解密中，HarmonyOS平台支持ASN.1序列化后的密钥数据（公钥91字节，私钥51字节），而其他平台的密钥数据通常为未序列化过的原始裸数据（公钥64字节，私钥32字节）。这些密钥不能直接在HarmonyOS平台使用，需要转换为ASN.1格式。下面以其他平台生成的十六进制密钥为例，介绍如何转换为HarmonyOS平台可用的SM2密钥。

  其他平台生成的公钥格式为04+x+y，私钥为128位字符串。

  将对应的16进制参数放入对应的位置，可通过[使用密钥参数生成](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#使用密钥参数生成-3)SM2公钥。

  ```
  1. public static async convertStrToPubKey(keyStr: string): Promise<cryptoFramework.PubKey | undefined> {
  2. const puKeyStr = keyStr.startsWith('04') ? keyStr.slice(2) : keyStr;
  3. const pkPart1 = puKeyStr.slice(0, puKeyStr.length / 2);
  4. const pkPart2 = puKeyStr.slice(puKeyStr.length / 2);
  5. const pks: cryptoFramework.Point = {
  6. x: BigInt('0x' + pkPart1),
  7. y: BigInt('0x' + pkPart2)
  8. };
  9. try {
  10. const pubKeySpec: cryptoFramework.ECCPubKeySpec = {
  11. params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
  12. pk: pks,
  13. algName: 'SM2',
  14. specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
  15. };
  16. const keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(pubKeySpec);
  17. return keypairGenerator.generatePubKeySync();
  18. } catch (error) {
  19. let err = error as BusinessError;
  20. hilog.error(0x0000, TAG, `convertStrToPubKey failed, error code=${err.code}, message=${err.message}`);
  21. return undefined;
  22. }
  23. }
  ```

  [DataConversion.ets](https://gitcode.com/harmonyos_samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L38-L61)

  同理，可通过[使用密钥参数生成](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#使用密钥参数生成-3)SM2私钥。

  ```
  1. public static async convertStrToPriKey(keyStr: string): Promise<cryptoFramework.PriKey | undefined> {
  2. try {
  3. const sks = BigInt('0x' + keyStr);
  4. const priKeySpec: cryptoFramework.ECCPriKeySpec = {
  5. params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
  6. sk: sks,
  7. algName: 'SM2',
  8. specType: cryptoFramework.AsyKeySpecType.PRIVATE_KEY_SPEC
  9. };
  10. const priKeypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(priKeySpec);
  11. let sksData = priKeypairGenerator.generatePriKeySync();
  12. return sksData;
  13. } catch (error) {
  14. let err = error as BusinessError;
  15. hilog.error(0x0000, TAG, `convertStrToPriKey failed, error code=${err.code}, message=${err.message}`);
  16. return undefined;
  17. }
  18. }
  ```

  [DataConversion.ets](https://gitcode.com/harmonyos_samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L71-L89)

* SM2密文格式转换

  SM2是一种国产非对称加密算法，其密文格式由三部分组成：

  C1：椭圆曲线点，长度为65字节，用于解密过程中的计算。

  C2：实际加密数据，长度由加密数据决定。

  C3：32字节的哈希值，用于验证密文完整性。

  目前SM2密文数据的参数组合顺序有老标准C1C2C3和新标准C1C3C2。

  HarmonyOS平台支持的SM2密文格式为国密标准的ASN.1格式，参数组合顺序为C1C3C2。具体参数含义请参考[转换SM2密文格式](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#转换sm2密文格式)。

  对于其他平台加密的C1C2C3顺序的密文，在HarmonyOS平台解密时，需先提取所需要的参数，并构造[SM2CipherTextSpec](../harmonyos-references/js-apis-cryptoframework.md#sm2ciphertextspec12)对象，接着调用[genCipherTextBySpec()](../harmonyos-references/js-apis-cryptoframework.md#genciphertextbyspec12)方法序列化生成ASN.1格式的SM2密文。具体可参考[使用SM2密文格式转换(ArkTS)](../harmonyos-guides/crypto-sm2-ciphertext-conversion.md)。

  ```
  1. bytesToBigInt(bytes: Uint8Array): bigint {
  2. let result = 0n;
  3. for (const byte of bytes) {
  4. result = (result << 8n) | BigInt(byte);
  5. }
  6. return result;
  7. }

  9. i2dSM2CipherText(primal_data: string): Uint8Array | undefined {
  10. // Converting a Hex String to byte array.
  11. const cipherBytes = DataConversion.hexStrToUint8Array(primal_data);

  13. // Defines that the length of C1 is 65 bytes (uncompressed format: 04 + x(32) + y(32)).
  14. const c1Length = 65;
  15. const totalLength = cipherBytes.length;

  17. if (totalLength < c1Length + 32) {
  18. hilog.error(0, 'id2_SM2_Ciphertext', 'Non-SM2 criterion compliant.');
  19. }

  21. // Extract C1 Part.
  22. const c1Bytes = cipherBytes.slice(0, c1Length);

  24. // Verify that C1 is in uncompressed format starting with 04.
  25. if (c1Bytes[0] !== 0x04) {
  26. hilog.error(0, 'id2_SM2_Ciphertext', 'C1 is not in uncompressed format.');
  27. }

  29. // Extract x and y coordinates.
  30. const xBytes = c1Bytes.slice(1, 33);
  31. const yBytes = c1Bytes.slice(33, 65);

  33. // Convert to BigInt.
  34. const xBigInt = this.bytesToBigInt(xBytes);
  35. const yBigInt = this.bytesToBigInt(yBytes);

  37. // Extract the C3 part (last 32 bytes).
  38. const c3Start = totalLength - 32;
  39. const c3Bytes = cipherBytes.slice(c3Start);

  41. // Extract C2 part (middle part).
  42. const c2Bytes = cipherBytes.slice(c1Length, c3Start);

  44. let spec: cryptoFramework.SM2CipherTextSpec = {
  45. xCoordinate: xBigInt,
  46. yCoordinate: yBigInt,
  47. cipherTextData: c2Bytes,
  48. hashData: c3Bytes
  49. }

  51. try {
  52. let data = cryptoFramework.SM2CryptoUtil.genCipherTextBySpec(spec, 'C1C3C2');
  53. return data.data;
  54. } catch (error) {
  55. let err = error as BusinessError;
  56. hilog.error(0x0000, 'xxx', ` failed, error code=${err.code}, message=${err.message}`);
  57. return undefined;
  58. }
  59. }
  ```

  [DataConversion.ets](https://gitcode.com/harmonyos_samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L205-L264)

  同理，HarmonyOS平台生成的C1C3C2顺序的ASN.1格式密文在其他平台使用时，需要先解码为C1C3C2的裸密文。

  ```
  1. d2i_SM2_Ciphertext(standard_data: string): string {
  2. let message: string = standard_data;
  3. if (!message.startsWith('30')) {
  4. hilog.error(0, 'd2i_SM2_Ciphertext', 'Incorrect ciphertext format');
  5. }
  6. message = message.slice('30'.length, message.length);

  8. // The length of the SM2 sequence content.
  9. let sequence_lexHex: string = this.getLenHex(message);
  10. message = message.slice(sequence_lexHex.length, message.length);
  11. let sequence_len: number = this.lenHex2number(sequence_lexHex);

  13. if (sequence_len !== message.length / 2) {
  14. hilog.error(0x0000, 'd2i_SM2_Ciphertext', 'Incorrect ciphertext format');
  15. }

  17. let sm2_sequence = new SM2Sequence();
  18. message = this.readC1(sm2_sequence, message);
  19. message = this.readC3(sm2_sequence, message);
  20. message = this.readC2(sm2_sequence, message);
  21. hilog.info(0x0000, 'sm2_sequence', sm2_sequence.toString());

  23. let primal_data: string = sm2_sequence.C1x + sm2_sequence.C1y + sm2_sequence.C3 + sm2_sequence.C2;
  24. return primal_data;
  25. }
  ```

  [DataConversion.ets](https://gitcode.com/harmonyos_samples/crypto-collection/blob/master/entry/src/main/ets/utils/DataConversion.ets#L170-L195)

### AES加解密

[AES](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)（Advanced Encryption Standard），最常见的对称加密算法。

下面介绍并解决在HarmonyOS平台与其他平台交互使用AES加解密开发中遇到的问题：密钥长度和指定分组模式后的偏移量参数设置。

* AES密钥长度使用问题

  在[AES](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)加解密算法中，密钥长度是固定的。

  初始化HarmonyOS平台的加解密引擎时，需指定算法规格及密钥长度。密钥长度可为128位（对应字符串参数AES128）、192位（对应字符串参数AES192）或256位（对应字符串参数AES256）。AES密钥的字节长度与位数对应关系为：16字节对应128位，24字节对应192位，32字节对应256位。通过密钥位数可推断其字节长度。

  以指南[使用AES对称密钥（GCM模式）加解密(ArkTS)](../harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm.md)为例，使用'AES128|GCM|PKCS7'初始化加解密算法实例。加解密时对应的密钥应为128位，即16个字符。因此，在生成密钥时，传入的字符为newUint8Array([83,217,231,76,28,113,23,219,250,71,209,210,205,97,32,159])。

  **通过字符串获取密钥位数**

  使用HarmonyOS的加解密API时，需明确指定算法规格和密钥长度，且该参数必须与传入的密钥匹配。密钥字符串通常以字节序列或十六进制字符串形式表示，无法直接获取其位数信息。

  因此，当给定一个表示AES密钥的字符串，需要确定其密钥长度（以位数表示）时，可以按照以下步骤进行：

  1. 确定密钥字符串的编码：确定密钥字符串的编码方式，常见的编码方式包括Base64、UTF-8、16进制等。
  2. 计算密钥的字节长度：根据密钥字符串的编码，将其转换为Uint8Array格式，计算其对应的字节长度。转换方式可参考[数据格式转换](bpta-cross-platform-compatibility.md#section1152116421582)。
  3. 推断密钥位数：根据AES密钥的字节长度与位数之间的对应关系，推断密钥的位数。16字节对应128位，24字节对应192位，32字节对应256位。
* AES指定分组模式后偏移量参数设置问题

  由于AES为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。

  以[GCM模式](../harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm.md)和[CBC模式](../harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc.md)为例，指定字符串参数分别为'AES128|GCM|PKCS7'和'AES128|CBC|PKCS7'，偏移量分别为16字节和12字节。

  | 分组模式 | 所需参数 | 备注 |
  | --- | --- | --- |
  | ECB | 没有偏移量等参数。 | - |
  | CBC、CTR、OFB、CFB | iv长度为16字节。 | - |
  | GCM | 加解密参数iv，长度为1~16字节，常用为12字节。  加解密参数add，长度为0~INT\_MAX字节，常用为16字节。  加解密参数authTag，长度为16字节。 | 在GCM模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。 |

## 示例代码

* [基于cryptoFramework实现加解密功能](https://gitcode.com/harmonyos_samples/crypto-collection)
