---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pss
title: 使用RSA密钥对签名验签（PSS模式）(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > 使用RSA密钥对签名验签（PSS模式）(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:33+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9f0601a5ca2a5a2ddc12932a9d8c8158d673b002936b6123b99a19cfea6a133c
---

对应的算法规格请查看[签名验签算法规格：RSA](crypto-sign-sig-verify-overview.md#rsa)。

**签名**

1. 调用[cryptoFramework.createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10)、[AsyKeyGeneratorBySpec.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair10)，指定密钥参数，生成RSA非对称密钥对（KeyPair）。

   如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[指定密钥参数生成非对称密钥对](crypto-generate-asym-key-pair-from-key-spec.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createSign](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)，指定字符串参数'RSA|PSS|SHA256|MGF1\_SHA256'，创建非对称密钥类型为不带长度的RSA、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1\_SHA256的Sign实例，用于完成签名操作。
3. 调用[Sign.init](../harmonyos-references/js-apis-cryptoframework.md#init-3)，使用私钥（PriKey）初始化Sign实例。
4. 调用[Sign.setSignSpec](../harmonyos-references/js-apis-cryptoframework.md#setsignspec10)，设置签名参数。此处设置盐值的长度（SignSpecItem.PSS\_SALT\_LEN\_NUM）为32字节。在验签时将校验此数据。
5. 调用[Sign.getSignSpec](../harmonyos-references/js-apis-cryptoframework.md#getsignspec10)，获取其他签名参数。
6. 调用[Sign.update](../harmonyos-references/js-apis-cryptoframework.md#update-3)，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
7. 调用[Sign.sign](../harmonyos-references/js-apis-cryptoframework.md#sign-1)，生成数据签名。

**验签**

1. 调用[cryptoFramework.createVerify](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateverify)，指定字符串参数'RSA2048|PSS|SHA256|MGF1\_SHA256'，创建非对称密钥类型为RSA2048、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1\_SHA256的Verify实例，用于完成验签操作。
2. 调用[Verify.setVerifySpec](../harmonyos-references/js-apis-cryptoframework.md#setverifyspec10)，设置签名参数。需要与签名时设置的保持一致。
3. 调用[Verify.init](../harmonyos-references/js-apis-cryptoframework.md#init-5)，使用公钥（PubKey）初始化Verify实例。
4. 调用[Verify.update](../harmonyos-references/js-apis-cryptoframework.md#update-5)，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
5. 调用[Verify.verify](../harmonyos-references/js-apis-cryptoframework.md#verify-1)，对数据进行验签。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 根据密钥参数属性构造RSA非对称密钥对密钥参数
  5. function genRsaKeyPairSpec(nIn: bigint, eIn: bigint, dIn: bigint) {
  6. let rsaCommSpec: cryptoFramework.RSACommonParamsSpec = {
  7. n: nIn,
  8. algName: 'RSA',
  9. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC
  10. };
  11. let rsaKeyPairSpec: cryptoFramework.RSAKeyPairSpec = {
  12. params: rsaCommSpec,
  13. sk: dIn,
  14. pk: eIn,
  15. algName: 'RSA',
  16. specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC
  17. };
  18. return rsaKeyPairSpec;
  19. }

  21. // 生成RSA2048密钥对参数
  22. function genRsa2048KeyPairSpec(): cryptoFramework.RSAKeyPairSpec {
  23. let nIn =
  24. BigInt('0x9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f5bc54a88b57fa19fc432' +
  25. '8daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a00a72b711c116ef7686e8fee34e4' +
  26. 'd933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d8626e8932b65c5bd8c92049c210932b7afa7ac' +
  27. '59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4388da8cf8c64eefe1c5a0f5ab8057c39fa5c0589c3e2' +
  28. '53f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d7ee552b3319b9266f05a25');
  29. let eIn = BigInt('0x010001');
  30. let dIn =
  31. BigInt('0x6a7df2ca63ead4dda191d614b6b385e0d9056a3d6d5cfe07db1daabee022db08212d97613d3328e0267c9dd23d787abde2afcb3' +
  32. '06aeb7dfce69246cc73f5c87fdf06030179a2114b767db1f083ff841c025d7dc00cd82435b9a90f695369e94df23d2ce458bc3b3283ad8' +
  33. 'bba2b8fa1ba62e2dce9accff3799aae7c840016f3ba8e0048c0b6cc4339af7161003a5beb864a0164b2c1c9237b64bc87556994351b275' +
  34. '06c33d4bcdfce0f9c491a7d6b0628c7c852be4f0a9c3132b2ed3a2c8881e9aab07e20e17deb074691be677776a78b5c502e05d9bdde721' +
  35. '26b3738695e2dd1a0a98a14247c65d8a7ee79432a092cb0721a12df798e44f7cfce0c498147a9b1');
  36. return genRsaKeyPairSpec(nIn, eIn, dIn);
  37. }

  39. async function verifyMessagePSS() {
  40. // 完整的明文被拆分为input1和input2
  41. let plan1 = 'This is Sign test plan1';
  42. let plan2 = 'This is Sign test plan2';
  43. let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(plan1, 'utf-8').buffer) };
  44. let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(plan2, 'utf-8').buffer) };
  45. // 获得RSA密钥对密钥参数对象
  46. let rsaKeyPairSpec = genRsa2048KeyPairSpec();
  47. // 构造RSA密钥对生成器
  48. let rsaGeneratorSpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaKeyPairSpec);
  49. // sign和verify均支持RSA密钥带长度/不带长度的写法
  50. let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  51. let verifyer = cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1_SHA256');
  52. let keyPair = await rsaGeneratorSpec.generateKeyPair();
  53. await signer.init(keyPair.priKey);
  54. // 在签名初始化后，对PSS参数进行set和get操作
  55. let setN = 32;
  56. signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  57. let saltLen = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
  58. console.info('SaltLen == ' + saltLen);
  59. let tf = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_TRAILER_FIELD_NUM);
  60. console.info('trailer field == ' + tf);
  61. let md = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_MD_NAME_STR);
  62. console.info('md == ' + md);
  63. let mgf = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_MGF_NAME_STR);
  64. console.info('mgf == ' + mgf);
  65. let mgf1Md = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_MGF1_MD_STR);
  66. console.info('mgf1Md == ' + mgf1Md);
  67. await signer.update(input1);
  68. let signMessageBlob = await signer.sign(input2);
  69. // 在验签初始化前，对PSS参数进行set和get操作
  70. verifyer.setVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  71. saltLen = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
  72. console.info('SaltLen == ' + saltLen);
  73. tf = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_TRAILER_FIELD_NUM);
  74. console.info('trailer field == ' + tf);
  75. md = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_MD_NAME_STR);
  76. console.info('md == ' + md);
  77. mgf = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_MGF_NAME_STR);
  78. console.info('mgf == ' + mgf);
  79. mgf1Md = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_MGF1_MD_STR);
  80. await verifyer.init(keyPair.pubKey);
  81. await verifyer.update(input1);
  82. let verifyResult = await verifyer.verify(input2, signMessageBlob);
  83. if (verifyResult === true) {
  84. console.info('verify result: success.');
  85. } else {
  86. console.error('verify result: failed.');
  87. }
  88. }
  ```

  [rsa\_pss\_signature\_verification\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pss_signature_verification/rsa_pss_signature_verification_asynchronous.ets#L16-L106)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 根据密钥参数属性构造RSA非对称密钥对密钥参数
  5. function genRsaKeyPairSpec(nIn: bigint, eIn: bigint, dIn: bigint) {
  6. let rsaCommSpec: cryptoFramework.RSACommonParamsSpec = {
  7. n: nIn,
  8. algName: 'RSA',
  9. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC
  10. };
  11. let rsaKeyPairSpec: cryptoFramework.RSAKeyPairSpec = {
  12. params: rsaCommSpec,
  13. sk: dIn,
  14. pk: eIn,
  15. algName: 'RSA',
  16. specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC
  17. };
  18. return rsaKeyPairSpec;
  19. }

  21. // 生成RSA2048密钥对参数
  22. function genRsa2048KeyPairSpec(): cryptoFramework.RSAKeyPairSpec {
  23. let nIn =
  24. BigInt('0x9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f5bc54a88b57fa19fc43' +
  25. '28daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a00a72b711c116ef7686e8fee34' +
  26. 'e4d933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d8626e8932b65c5bd8c92049c210932b7afa' +
  27. '7ac59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4388da8cf8c64eefe1c5a0f5ab8057c39fa5c0589' +
  28. 'c3e253f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d7ee552b3319b9266f05a25');
  29. let eIn = BigInt('0x010001');
  30. let dIn =
  31. BigInt('0x6a7df2ca63ead4dda191d614b6b385e0d9056a3d6d5cfe07db1daabee022db08212d97613d3328e0267c9dd23d787abde2afcb' +
  32. '306aeb7dfce69246cc73f5c87fdf06030179a2114b767db1f083ff841c025d7dc00cd82435b9a90f695369e94df23d2ce458bc3b3283a' +
  33. 'd8bba2b8fa1ba62e2dce9accff3799aae7c840016f3ba8e0048c0b6cc4339af7161003a5beb864a0164b2c1c9237b64bc87556994351b' +
  34. '27506c33d4bcdfce0f9c491a7d6b0628c7c852be4f0a9c3132b2ed3a2c8881e9aab07e20e17deb074691be677776a78b5c502e05d9bdd' +
  35. 'e72126b3738695e2dd1a0a98a14247c65d8a7ee79432a092cb0721a12df798e44f7cfce0c498147a9b1');
  36. return genRsaKeyPairSpec(nIn, eIn, dIn);
  37. }

  39. function verifyMessagePSS() {
  40. // 完整的明文被拆分为input1和input2
  41. let plan1 = 'This is Sign test plan1';
  42. let plan2 = 'This is Sign test plan2';
  43. let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(plan1, 'utf-8').buffer) };
  44. let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(plan2, 'utf-8').buffer) };
  45. // 获得RSA密钥对密钥参数对象
  46. let rsaKeyPairSpec = genRsa2048KeyPairSpec();
  47. // 构造RSA密钥对生成器
  48. let rsaGeneratorSpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaKeyPairSpec);
  49. // sign和verify均支持RSA密钥带长度/不带长度的写法
  50. let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  51. let verifyer = cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1_SHA256');
  52. let keyPair = rsaGeneratorSpec.generateKeyPairSync();
  53. signer.initSync(keyPair.priKey);
  54. // 在签名初始化后，对PSS参数进行set和get操作
  55. let setN = 32;
  56. signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  57. let saltLen = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
  58. console.info('SaltLen == ' + saltLen);
  59. let tf = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_TRAILER_FIELD_NUM);
  60. console.info('trailer field == ' + tf);
  61. let md = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_MD_NAME_STR);
  62. console.info('md == ' + md);
  63. let mgf = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_MGF_NAME_STR);
  64. console.info('mgf == ' + mgf);
  65. let mgf1Md = signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_MGF1_MD_STR);
  66. console.info('mgf1Md == ' + mgf1Md);
  67. signer.updateSync(input1);
  68. let signMessageBlob = signer.signSync(input2);
  69. // 在验签初始化前，对PSS参数进行set和get操作
  70. verifyer.setVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  71. saltLen = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
  72. console.info('SaltLen == ' + saltLen);
  73. tf = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_TRAILER_FIELD_NUM);
  74. console.info('trailer field == ' + tf);
  75. md = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_MD_NAME_STR);
  76. console.info('md == ' + md);
  77. mgf = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_MGF_NAME_STR);
  78. console.info('mgf == ' + mgf);
  79. mgf1Md = verifyer.getVerifySpec(cryptoFramework.SignSpecItem.PSS_MGF1_MD_STR);
  80. verifyer.initSync(keyPair.pubKey);
  81. verifyer.updateSync(input1);
  82. let verifyResult = verifyer.verifySync(input2, signMessageBlob);
  83. if (verifyResult === true) {
  84. console.info('verify result: success.');
  85. } else {
  86. console.error('verify result: failed.');
  87. }
  88. }
  ```

  [rsa\_pss\_signature\_verification\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pss_signature_verification/rsa_pss_signature_verification_synchronous.ets#L16-L106)
