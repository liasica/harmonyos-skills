---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec
title: 指定密钥参数生成非对称密钥对(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定密钥参数生成非对称密钥对(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:577f58ee16a12bdab2114ee6ca67e7b96c213de8b921ec847b98cd2f0a761ecf
---

以RSA、ECC、SM2为例，根据指定的密钥参数，生成非对称密钥对（KeyPair），并获取密钥参数属性。

该对象可用于后续的加解密等操作。获取的密钥参数属性可用于存储或传输。

## 指定密钥参数生成RSA公钥

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 构造[RSACommonParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#rsacommonparamsspec10)对象，用于指定RSA算法中公私钥包含的公共参数（n）。

   RSACommonParamsSpec是AsyKeySpec的子类。需要通过参数algName指定算法'RSA'；指定密钥参数类型AsyKeySpecType.COMMON\_PARAMS\_SPEC，表示是公私钥中包含的公共参数。

   使用密钥参数生成密钥时，bigint类型参数需采用大端字节序输入，且值应为正数以满足数学运算要求。
2. 创建[RSAPubKeySpec](../harmonyos-references/js-apis-cryptoframework.md#rsapubkeyspec10)对象，用于指定RSA算法中公钥包含的参数（n, pk）。

   RSAPubKeySpec是AsyKeySpec的子类。通过参数algName指定算法'RSA'；指定密钥参数类型AsyKeySpecType.PUBLIC\_KEY\_SPEC，表示是公钥中包含的参数。
3. 调用[cryptoFramework.createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10)，将RSAPubKeySpec对象传入，创建非对称密钥生成器（AsyKeyGeneratorBySpec）。
4. 调用[AsyKeyGeneratorBySpec.generatePubKey](../harmonyos-references/js-apis-cryptoframework.md#generatepubkey10)，获得指定的公钥（PubKey）。
5. 调用[PubKey.getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10)，获取模数n和公钥pk（即公钥指数e）。

* 以使用callback方式根据密钥参数生成RSA公钥为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. // RSA公钥密钥参数生成函数
  4. function genRsaPubKeySpec(nIn: bigint, eIn: bigint): cryptoFramework.RSAPubKeySpec {
  5. let rsaCommSpec: cryptoFramework.RSACommonParamsSpec = {
  6. n: nIn,
  7. algName: 'RSA',
  8. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC
  9. };
  10. let rsaPubKeySpec: cryptoFramework.RSAPubKeySpec = {
  11. params: rsaCommSpec,
  12. pk: eIn,
  13. algName: 'RSA',
  14. specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
  15. };
  16. return rsaPubKeySpec;
  17. }

  19. // 根据密钥参数构造RSA公钥规范对象
  20. function genRsa2048PubKeySpec() {
  21. let nIn =
  22. BigInt('0x9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f5bc54a88b57fa19fc4' +
  23. '328daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a00a72b711c116ef7686e8fee' +
  24. '34e4d933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d8626e8932b65c5bd8c92049c210932b7' +
  25. 'afa7ac59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4388da8cf8c64eefe1c5a0f5ab8057c39fa5c' +
  26. '0589c3e253f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d7ee552b3319b9266f05a25');
  27. let eIn = BigInt('0x010001');
  28. return genRsaPubKeySpec(nIn, eIn);
  29. }

  31. // 将RSA公钥规格与预期值进行比较
  32. function compareRsaPubKeyBySpec(rsaKeySpec: cryptoFramework.RSAPubKeySpec, n: bigint | string | number,
  33. e: bigint | string | number) {
  34. if (typeof n === 'string' || typeof e === 'string') {
  35. console.error('type: string');
  36. return false;
  37. }
  38. if (typeof n === 'number' || typeof e === 'number') {
  39. console.error('type: number');
  40. return false;
  41. }
  42. if (rsaKeySpec.params.n != n) {
  43. return false;
  44. }
  45. if (rsaKeySpec.pk != e) {
  46. return false;
  47. }
  48. return true;
  49. }

  51. // 根据RSA公钥规格生成RSA公钥，获取密钥规格，并与预期值进行比较
  52. function rsaUsePubKeySpecGetCallback() {
  53. let rsaPubKeySpec = genRsa2048PubKeySpec();
  54. let rsaGeneratorSpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaPubKeySpec);
  55. rsaGeneratorSpec.generatePubKey((error, key) => {
  56. if (error) {
  57. console.error('generate pubKey failed, ' + 'error code: ' + error.code + 'error message' + error.message);
  58. }
  59. let pubKey = key;
  60. let nBN = pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.RSA_N_BN);
  61. let eBN = pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.RSA_PK_BN);
  62. if (compareRsaPubKeyBySpec(rsaPubKeySpec, nBN, eBN) != true) {
  63. console.error('error pub key big number');
  64. } else {
  65. console.info('n, e in the pubKey are same as the spec.');
  66. }
  67. });
  68. }
  ```

  [Callback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/ets/pages/rsa/Callback.ets#L16-L85)
* 同步返回结果（调用方法[generatePubKeySync](../harmonyos-references/js-apis-cryptoframework.md#generatepubkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. // RSA公钥密钥参数生成函数
  4. function genRsaPubKeySpec(nIn: bigint, eIn: bigint): cryptoFramework.RSAPubKeySpec {
  5. let rsaCommSpec: cryptoFramework.RSACommonParamsSpec = {
  6. n: nIn,
  7. algName: 'RSA',
  8. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC
  9. };
  10. let rsaPubKeySpec: cryptoFramework.RSAPubKeySpec = {
  11. params: rsaCommSpec,
  12. pk: eIn,
  13. algName: 'RSA',
  14. specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
  15. };
  16. return rsaPubKeySpec;
  17. }

  19. // 根据密钥参数构造RSA公钥规范对象
  20. function genRsa2048PubKeySpec() {
  21. let nIn =
  22. BigInt('0x9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f5bc54a88b57fa19fc43' +
  23. '28daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a00a72b711c116ef7686e8fee34' +
  24. 'e4d933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d8626e8932b65c5bd8c92049c210932b7afa' +
  25. '7ac59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4388da8cf8c64eefe1c5a0f5ab8057c39fa5c0589' +
  26. 'c3e253f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d7ee552b3319b9266f05a25');
  27. let eIn = BigInt('0x010001');
  28. return genRsaPubKeySpec(nIn, eIn);
  29. }

  31. // 将RSA公钥规格与预期值进行比较
  32. function compareRsaPubKeyBySpec(rsaKeySpec: cryptoFramework.RSAPubKeySpec, n: bigint | string | number,
  33. e: bigint | string | number) {
  34. if (typeof n === 'string' || typeof e === 'string') {
  35. console.error('type: string');
  36. return false;
  37. }
  38. if (typeof n === 'number' || typeof e === 'number') {
  39. console.error('type: number');
  40. return false;
  41. }
  42. if (rsaKeySpec.params.n != n) {
  43. return false;
  44. }
  45. if (rsaKeySpec.pk != e) {
  46. return false;
  47. }
  48. return true;
  49. }

  51. // 根据RSA公钥规格生成RSA公钥，获取密钥规格，并与预期值进行比较
  52. function rsaUsePubKeySpecGetSync() {
  53. let rsaPubKeySpec = genRsa2048PubKeySpec();
  54. let rsaGeneratorSpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaPubKeySpec);
  55. try {
  56. let pubKey = rsaGeneratorSpec.generatePubKeySync();
  57. if (pubKey != null) {
  58. let nBN = pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.RSA_N_BN);
  59. let eBN = pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.RSA_PK_BN);
  60. if (compareRsaPubKeyBySpec(rsaPubKeySpec, nBN, eBN) != true) {
  61. console.error('error pub key big number');
  62. } else {
  63. console.info('n, e in the pubKey are same as the spec.');
  64. }
  65. } else {
  66. console.error('get pub key result: fail!');
  67. }
  68. } catch (e) {
  69. console.error(`get pub key result failed: errCode: ${e.code}, message: ${e.message}`);
  70. }
  71. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/ets/pages/rsa/Sync.ets#L16-L88)

## 指定密钥参数生成ECC密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

1. 构造[ECCCommonParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#ecccommonparamsspec10)对象，用于指定ECC算法中公私钥包含的公共参数。

   ECCCommonParamsSpec是AsyKeySpec的子类。需要通过参数algName指定算法'ECC'；指定密钥参数类型AsyKeySpecType.COMMON\_PARAMS\_SPEC，表示是公私钥中包含的公共参数。

   使用密钥参数生成密钥时，bigint类型参数需采用大端字节序输入，且值应为正数以满足数学运算要求。
2. 调用[cryptoFramework.createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10)，将ECCCommonParamsSpec对象传入，创建非对称密钥生成器（AsyKeyGeneratorBySpec）。
3. 调用[AsyKeyGeneratorBySpec.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair10)，得到随机生成的密钥对（KeyPair）。
4. 分别传入密钥对中的私钥和公钥，调用[PriKey.getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10-1)、[PubKey.getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10)，获取ECC算法中私钥和公钥的各种密钥参数。

* 以使用Promise方式根据密钥参数生成ECC密钥为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. // 打印bigint信息
  5. function showBigIntInfo(bnName: string, bnValue: bigint | string | number) {
  6. if (typeof bnValue === 'string') {
  7. console.error('type: string');
  8. return;
  9. }
  10. if (typeof bnValue === 'number') {
  11. console.error('type: number');
  12. return;
  13. }
  14. console.info(bnName + ':');
  15. console.info('. Decimal: ' + bnValue.toString());
  16. console.info('. Hexadecimal: ' + bnValue.toString(16));
  17. console.info('. Length (bits): ' + bnValue.toString(2).length);
  18. }

  20. // 根据密钥规格构造ECCCommonParamsSpec结构体。ECCCommonParamsSpec结构体定义了ECC私钥和公钥的公共参数
  21. function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  22. let fieldFp: cryptoFramework.ECFieldFp = {
  23. fieldType: 'Fp',
  24. p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  25. }
  26. let G: cryptoFramework.Point = {
  27. x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
  28. y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  29. }
  30. let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
  31. algName: 'ECC',
  32. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
  33. field: fieldFp,
  34. a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
  35. b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
  36. g: G,
  37. n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
  38. h: 1
  39. }
  40. return eccCommonSpec;
  41. }

  43. // 打印ECC密钥规格
  44. function showEccSpecDetailInfo(key: cryptoFramework.PubKey | cryptoFramework.PriKey, keyType: string) {
  45. console.info('show detail of ' + keyType + ':');
  46. try {
  47. let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FP_P_BN);
  48. showBigIntInfo('--- p', p); // length is 224, hex : ffffffffffffffffffffffffffffffff000000000000000000000001
  49. let a = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_A_BN);
  50. showBigIntInfo('--- a', a); // length is 224, hex : fffffffffffffffffffffffffffffffefffffffffffffffffffffffe
  51. let b = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_B_BN);
  52. showBigIntInfo('--- b', b); // length is 224, hex : b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
  53. let gX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_X_BN);
  54. showBigIntInfo('--- gX', gX); // length is 224, hex : b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
  55. let gY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_Y_BN);
  56. showBigIntInfo('--- gY', gY); // length is 224, hex : bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34
  57. let n = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_N_BN);
  58. showBigIntInfo('--- n', n); // length is 224, hex : ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d
  59. let h = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_H_NUM);
  60. console.warn('--- h: ' + h); // key h: 1
  61. let fieldType = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_TYPE_STR);
  62. console.warn('--- field type: ' + fieldType); // key field type: Fp
  63. let fieldSize = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_SIZE_NUM);
  64. console.warn('--- field size: ' + fieldSize); // key field size: 224
  65. let curveName = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
  66. console.warn('--- curve name: ' + curveName); // key curve name: NID_secp224r1
  67. if (keyType == 'priKey') {
  68. let sk = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_SK_BN);
  69. showBigIntInfo('--- sk', sk);
  70. } else if (keyType == 'pubKey') {
  71. let pkX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
  72. showBigIntInfo('--- pkX', pkX);
  73. let pkY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
  74. showBigIntInfo('--- pkY', pkY);
  75. }
  76. } catch (error) {
  77. let e: BusinessError = error as BusinessError;
  78. console.error(`getAsyKeySpec failed: errCode: ${e.code}, message: ${e.message}`);
  79. }
  80. }

  82. // 根据EccCommonSpec实例生成ECC密钥对，获取密钥规格
  83. function testEccUseCommKeySpecGet() {
  84. try {
  85. let commKeySpec = genEccCommonSpec(); // 使用参数属性，构造ECC公私钥公共密钥参数对象
  86. let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // 使用密钥参数对象创建生成器
  87. let keyPairPromise = generatorBySpec.generateKeyPair(); // Generate an ECC key pair.
  88. keyPairPromise.then(keyPair => { // 使用生成器创建ECC密钥对
  89. showEccSpecDetailInfo(keyPair.priKey, 'priKey'); // 对私钥获取相关密钥参数属性
  90. showEccSpecDetailInfo(keyPair.pubKey, 'pubKey'); // 对公钥获取相关密钥参数属性
  91. }).catch((error: BusinessError) => {
  92. // 逻辑错误等异步异常在此捕获
  93. console.error(`generateComm failed: errCode: ${error.code}, message: ${error.message}`);
  94. })
  95. } catch (error) {
  96. // 参数错误等同步异常在此捕获
  97. let e: BusinessError = error as BusinessError;
  98. console.error(`ecc comm spec failed: errCode: ${e.code}, message: ${e.message}`);
  99. }
  100. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/ets/pages/ecc/Promise.ets#L16-L117)
* 同步返回结果（调用方法[generateKeyPairSync](../harmonyos-references/js-apis-cryptoframework.md#generatekeypairsync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function showBigIntInfo(bnName: string, bnValue: bigint | string | number) {
  4. if (typeof bnValue === 'string') {
  5. console.error('type: string');
  6. return;
  7. }
  8. if (typeof bnValue === 'number') {
  9. console.error('type: number');
  10. return;
  11. }
  12. console.info(bnName + ':');
  13. console.info('. Decimal: ' + bnValue.toString());
  14. console.info('. Hexadecimal: ' + bnValue.toString(16));
  15. console.info('. Length (bits): ' + bnValue.toString(2).length);
  16. }

  18. // 根据密钥规格构造ECCCommonParamsSpec结构体。ECCCommonParamsSpec结构体定义了ECC私钥和公钥的公共参数
  19. function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  20. let fieldFp: cryptoFramework.ECFieldFp = {
  21. fieldType: 'Fp',
  22. p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  23. }
  24. let G: cryptoFramework.Point = {
  25. x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
  26. y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  27. }
  28. let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
  29. algName: 'ECC',
  30. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
  31. field: fieldFp,
  32. a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
  33. b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
  34. g: G,
  35. n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
  36. h: 1
  37. }
  38. return eccCommonSpec;
  39. }

  41. // 打印ECC密钥规格
  42. function showEccSpecDetailInfo(key: cryptoFramework.PubKey | cryptoFramework.PriKey, keyType: string) {
  43. console.info('show detail of ' + keyType + ':');
  44. try {
  45. let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FP_P_BN);
  46. showBigIntInfo('--- p', p); // length is 224, hex : ffffffffffffffffffffffffffffffff000000000000000000000001
  47. let a = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_A_BN);
  48. showBigIntInfo('--- a', a); // length is 224, hex : fffffffffffffffffffffffffffffffefffffffffffffffffffffffe
  49. let b = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_B_BN);
  50. showBigIntInfo('--- b', b); // length is 224, hex : b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
  51. let gX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_X_BN);
  52. showBigIntInfo('--- gX', gX); // length is 224, hex : b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
  53. let gY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_Y_BN);
  54. showBigIntInfo('--- gY', gY); // length is 224, hex : bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34
  55. let n = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_N_BN);
  56. showBigIntInfo('--- n', n); // length is 224, hex : ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d
  57. let h = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_H_NUM);
  58. console.warn('--- h: ' + h); // key h: 1
  59. let fieldType = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_TYPE_STR);
  60. console.warn('--- field type: ' + fieldType); // key field type: Fp
  61. let fieldSize = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_SIZE_NUM);
  62. console.warn('--- field size: ' + fieldSize); // key field size: 224
  63. let curveName = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
  64. console.warn('--- curve name: ' + curveName); // key curve name: NID_secp224r1
  65. if (keyType == 'priKey') {
  66. let sk = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_SK_BN);
  67. showBigIntInfo('--- sk', sk);
  68. } else if (keyType == 'pubKey') {
  69. let pkX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
  70. showBigIntInfo('--- pkX', pkX);
  71. let pkY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
  72. showBigIntInfo('--- pkY', pkY);
  73. }
  74. } catch (e) {
  75. console.error(`getAsyKeySpec failed: errCode: ${e.code}, message: ${e.message}`);
  76. }
  77. }

  79. // 根据EccCommonSpec实例生成ECC密钥对，获取密钥规格
  80. function testEccUseCommKeySpecGetSync() {
  81. try {
  82. let commKeySpec = genEccCommonSpec(); // 使用参数属性，构造ECC公私钥公共密钥参数对象
  83. let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // 使用密钥参数对象创建生成器
  84. let keyPair = generatorBySpec.generateKeyPairSync(); // Generate an ECC key pair.
  85. if (keyPair != null) {
  86. showEccSpecDetailInfo(keyPair.priKey, 'priKey'); // 对私钥获取相关密钥参数属性
  87. showEccSpecDetailInfo(keyPair.pubKey, 'pubKey'); // 对公钥获取相关密钥参数属性
  88. } else {
  89. console.error('get key pair result: fail!');
  90. }
  91. } catch (e) {
  92. // 逻辑错误等异常在此捕获
  93. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  94. }
  95. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/ets/pages/ecc/Sync.ets#L16-L112)

## 根据椭圆曲线名生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 构造[ECCCommonParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#ecccommonparamsspec10)对象，用于指定非对称公共密钥参数。根据[genECCCommonParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#genecccommonparamsspec11)接口传入相应的NID字符串名称生成相应的非对称公共密钥参数。

   使用密钥参数生成密钥时，bigint类型参数需采用大端字节序输入，且值应为正数以满足数学运算要求。
2. 创建[ECCKeyPairSpec](../harmonyos-references/js-apis-cryptoframework.md#ecckeypairspec10)对象，并且algName设置为SM2，用于指定SM2算法中密钥对包含的参数。
3. 调用[cryptoFramework.createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10)，将ECCKeyPairSpec对象传入，创建非对称密钥生成器。
4. 调用[AsyKeyGeneratorBySpec.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair10)，得到各项数据与密钥参数一致的密钥对（KeyPair）。
5. 调用[PriKey.getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10-1)，获取SM2算法中椭圆曲线参数。

* 以使用Promise方式根据椭圆曲线名生成SM2密钥为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function genSM2KeyPairSpec() {
  4. let sm2CommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2');
  5. let sm2KeyPairSpec: cryptoFramework.ECCKeyPairSpec = {
  6. algName: 'SM2',
  7. specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
  8. params: sm2CommonParamsSpec,
  9. sk: BigInt('0x6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074'),
  10. pk: {
  11. x: BigInt('0x67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4'),
  12. y: BigInt('0xD48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071')
  13. },
  14. };
  15. return sm2KeyPairSpec;
  16. }

  18. async function sm2Test() {
  19. let sm2KeyPairSpec = genSM2KeyPairSpec();
  20. let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(sm2KeyPairSpec);
  21. let keyPair = await generatorBySpec.generateKeyPair();
  22. let sm2CurveName = keyPair.priKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
  23. console.info('ECC_CURVE_NAME_STR: ' + sm2CurveName); // NID_sm2
  24. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/ets/pages/sm2/Promise.ets#L16-L41)
* 同步返回结果（调用方法[generateKeyPairSync](../harmonyos-references/js-apis-cryptoframework.md#generatekeypairsync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function genSM2KeyPairSpec() {
  4. let sm2CommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2');
  5. let sm2KeyPairSpec: cryptoFramework.ECCKeyPairSpec = {
  6. algName: 'SM2',
  7. specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
  8. params: sm2CommonParamsSpec,
  9. sk: BigInt('0x6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074'),
  10. pk: {
  11. x: BigInt('0x67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4'),
  12. y: BigInt('0xD48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071')
  13. },
  14. };
  15. return sm2KeyPairSpec;
  16. }

  18. function sm2TestSync() {
  19. let sm2KeyPairSpec = genSM2KeyPairSpec();
  20. let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(sm2KeyPairSpec);
  21. try {
  22. let keyPair = generatorBySpec.generateKeyPairSync();
  23. if (keyPair != null) {
  24. let sm2CurveName = keyPair.priKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
  25. console.info('ECC_CURVE_NAME_STR: ' + sm2CurveName); // NID_sm2
  26. } else {
  27. console.error('get key pair result: fail!');
  28. }
  29. } catch (e) {
  30. console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  31. }
  32. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/ets/pages/sm2/Sync.ets#L16-L49)
