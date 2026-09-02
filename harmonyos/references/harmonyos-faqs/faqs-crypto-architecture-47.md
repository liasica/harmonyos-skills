---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-47
title: 实现高效且安全的RSA与AES混合加密过程
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 实现高效且安全的RSA与AES混合加密过程
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:255812cdbff62bb973a83ec1e3c451423cf654e8899c9577d15afa9804631cb5
---

## 问题现象

基于HarmonyOS5开发的物联网应用，在有限的设备资源计算能力、存储容量下，如何实现高效且安全的RSA与AES混合加密过程，同时保证设备的实时响应性能呢？

## 背景知识

1. 适用场景：

   [RSA](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#rsa)更适合用于加密小数据量（如对称密钥）和身份验证（如数字签名）。

   [AES](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)更适合用于加密大量数据（如文件、通信流）。
2. RSA密钥长度：

   1024位：这是目前主流的推荐长度，适用于大多数应用场景。

   2048位：适用于对安全性要求更高的场景，如金融或政府领域。

   3072位和4096位：适用于极高安全需求的场景，但计算效率会显著降低。

   密钥生成时间：密钥长度增加一倍，密钥对生成的时间可能增加16倍。

   加密和解密操作：公钥加密操作时长增加4倍，私钥解密操作时长增加8倍。
3. AES密钥长度：

   128位（16字节）适用于大多安全场景。

   192位（24字节）提供较高的安全性，适用于对安全性要求较高的场景。

   256位（32字节）提供更高级别的安全性，适用于对安全性要求极高的场景。

   安全性：密钥长度越长，安全性越高，但计算开销也越大。

   性能：较短的密钥（如128位）在性能上更具优势，适合对性能要求较高的场景。

   兼容性：128位密钥被广泛支持，而192位和256位密钥在某些环境中可能需要额外配置。

## 解决方案

结合背景知识，在实现RSA和AES混合加密过程中，我们可以选择AES-128加密实际数据，RSA-1024用于安全传输AES密钥。

1. 使用算法框架cryptoFramework生成aes-128的密钥。
2. 使用算法框架cryptoFramework生成RSA-1024的密钥对。
3. 使用RSA公钥加密AES密钥后，将密文单独保存。
4. 使用AES密钥加密数据后进行传输。
5. 使用RSA解密AES密钥，获取AES密钥。
6. 使用AES密钥解密数据后进行处理。

完整示例参考如下：

```screen
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct rsaWithAES {
  private message: string = 'RSA与AES混合加密';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('encrypt')
        .fontSize('30fp')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          main();
        })
    }
    .height('100%')
    .width('100%')
  }
}

// 生成随机数
function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

// 获取iv值
function genIvParamsSpec() {
  let ivBlob = generateRandom(16);
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: 'IvParamsSpec',
    iv: ivBlob
  };
  return ivParamsSpec;
}

let iv = genIvParamsSpec();

// 生成RSA密钥对
function genKeyPairByData() {
  let pubKeyData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 197, 64, 10, 198, 14, 110, 65, 92, 206, 35, 28, 123, 153, 24, 134, 255, 145, 74, 42, 173, 40, 215,
      146, 58, 143, 46, 10, 195, 154, 160, 69, 196, 220, 152, 179, 44, 111, 200, 84, 78, 215, 73, 210, 181, 12, 29, 70,
      68, 36, 135, 153, 89, 230, 202, 130, 212, 111, 243, 234, 92, 131, 62, 145, 50, 73, 48, 104, 245, 46, 70, 45, 157,
      147, 143, 140, 162, 156, 216, 220, 49, 121, 142, 194, 33, 223, 201, 0, 16, 163, 210, 240, 118, 92, 147, 121, 220,
      17, 114, 24, 52, 125, 135, 176, 88, 21, 83, 86, 17, 156, 88, 250, 48, 79, 86, 128, 248, 105, 208, 133, 140, 13,
      153, 164, 191, 136, 164, 44, 53, 2, 3, 1, 0, 1]);
  let priKeyData =
    new Uint8Array([48, 130, 2, 119, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 97, 48,
      130, 2, 93, 2, 1, 0, 2, 129, 129, 0, 197, 64, 10, 198, 14, 110, 65, 92, 206, 35, 28, 123, 153, 24, 134, 255, 145,
      74, 42, 173, 40, 215, 146, 58, 143, 46, 10, 195, 154, 160, 69, 196, 220, 152, 179, 44, 111, 200, 84, 78, 215, 73,
      210, 181, 12, 29, 70, 68, 36, 135, 153, 89, 230, 202, 130, 212, 111, 243, 234, 92, 131, 62, 145, 50, 73, 48, 104,
      245, 46, 70, 45, 157, 147, 143, 140, 162, 156, 216, 220, 49, 121, 142, 194, 33, 223, 201, 0, 16, 163, 210, 240,
      118, 92, 147, 121, 220, 17, 114, 24, 52, 125, 135, 176, 88, 21, 83, 86, 17, 156, 88, 250, 48, 79, 86, 128, 248,
      105, 208, 133, 140, 13, 153, 164, 191, 136, 164, 44, 53, 2, 3, 1, 0, 1, 2, 129, 128, 70, 75, 184, 139, 53, 1, 94,
      17, 240, 244, 218, 101, 193, 253, 215, 190, 164, 204, 197, 192, 200, 89, 107, 39, 171, 119, 65, 38, 204, 168, 105,
      180, 234, 217, 16, 161, 185, 132, 175, 103, 25, 154, 153, 153, 36, 36, 26, 178, 150, 66, 45, 8, 185, 19, 90, 228,
      210, 177, 30, 200, 177, 141, 78, 184, 248, 59, 113, 154, 145, 73, 160, 24, 73, 157, 86, 207, 186, 32, 95, 200,
      106, 252, 107, 69, 170, 193, 216, 196, 181, 142, 74, 203, 15, 18, 89, 228, 152, 19, 239, 21, 233, 98, 121, 214,
      57, 187, 111, 239, 223, 248, 199, 70, 223, 108, 108, 113, 234, 144, 155, 95, 246, 144, 244, 122, 39, 55, 127, 81,
      2, 65, 0, 246, 96, 188, 0, 0, 104, 221, 105, 139, 144, 63, 175, 209, 87, 179, 162, 88, 192, 99, 82, 125, 53, 54,
      48, 70, 245, 239, 37, 15, 242, 247, 84, 115, 187, 196, 95, 156, 40, 165, 60, 64, 102, 13, 229, 243, 2, 149, 0,
      232, 226, 221, 192, 95, 11, 12, 208, 5, 181, 98, 62, 210, 190, 141, 235, 2, 65, 0, 204, 244, 34, 10, 105, 80, 76,
      116, 163, 35, 231, 168, 187, 206, 189, 101, 215, 103, 80, 115, 86, 11, 34, 127, 203, 114, 84, 188, 121, 174, 169,
      31, 142, 2, 182, 27, 140, 225, 157, 227, 71, 98, 15, 203, 187, 213, 5, 190, 20, 121, 8, 30, 193, 100, 232, 101,
      141, 8, 124, 20, 29, 78, 6, 95, 2, 65, 0, 204, 43, 225, 224, 6, 118, 224, 117, 100, 200, 199, 94, 70, 23, 109,
      175, 173, 232, 208, 230, 61, 8, 105, 189, 156, 48, 150, 91, 154, 89, 248, 136, 173, 215, 254, 166, 84, 220, 130,
      1, 234, 68, 40, 100, 84, 251, 224, 202, 254, 51, 115, 28, 198, 38, 124, 25, 175, 129, 94, 199, 61, 17, 216, 189,
      2, 64, 72, 230, 129, 129, 48, 138, 134, 87, 106, 123, 231, 247, 165, 173, 216, 194, 115, 198, 228, 223, 209, 120,
      46, 114, 68, 92, 75, 117, 170, 214, 140, 131, 147, 208, 181, 19, 193, 157, 178, 186, 87, 246, 178, 101, 166, 79,
      20, 54, 211, 51, 101, 199, 2, 197, 48, 192, 134, 84, 193, 69, 170, 82, 201, 131, 2, 65, 0, 213, 165, 55, 166, 131,
      210, 195, 56, 250, 147, 195, 61, 205, 208, 189, 185, 40, 52, 50, 119, 137, 23, 246, 46, 220, 108, 52, 23, 152,
      154, 94, 32, 144, 195, 184, 249, 21, 168, 12, 57, 222, 18, 60, 117, 81, 157, 72, 30, 155, 190, 165, 242, 228, 139,
      240, 184, 145, 170, 103, 210, 160, 161, 135, 13]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  console.info('convertKeySync success');
  return keyPair;
}

// 生成AES密钥
function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = aesGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

// 使用RSA公钥加密AES密钥
function encryptAESKey(keyData_AES: Uint8Array, publicKey: cryptoFramework.PubKey) {
  let plainText: cryptoFramework.DataBlob = { data: keyData_AES };
  let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
  let encryptData = cipher.doFinalSync(plainText);
  return encryptData;
}

// 使用AES密钥加密数据
function encryptMessByAES(keyData_AES: Uint8Array, message: string) {
  let symKey = genSymKeyByData(keyData_AES);
  let plainText_Mes: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };

  let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  let cipherData = cipher.doFinalSync(plainText_Mes);
  return cipherData;
}

// 使用RSA解密AES密钥
function decryptAESKey(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('RSA1024|PKCS1');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

// 使用AES密钥解密数据
function decryptMessage(priKey_RSA: cryptoFramework.PriKey, encryptText_AESKey: cryptoFramework.DataBlob,
  cipherText: cryptoFramework.DataBlob) {
  // 使用RSA解密AES密钥
  let decryptText_AESKey = decryptAESKey(priKey_RSA, encryptText_AESKey);
  // 获取AES的密钥值
  let symKey = genSymKeyByData(decryptText_AESKey.data);
  // 解密
  let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

function main() {
  // 待加密数据
  let message = 'This is a test';
  // 创建RSA密钥对
  let keyPair_RSA = genKeyPairByData();
  // 公钥
  let pubKey_RSA = keyPair_RSA.pubKey;
  // 私钥
  let priKey_RSA = keyPair_RSA.priKey;
  // 创建AES密钥
  let keyData_AES = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  // 使用AES密钥加密数据
  let encryptText = encryptMessByAES(keyData_AES, message);
  // 使用RSA公钥加密AES密钥后，该加密后的密钥具有较高的安全性
  let encryptText_AESKey = encryptAESKey(keyData_AES, pubKey_RSA);

  // 获取解密后的数据用于进行结果比对验证
  let decryptText = decryptMessage(priKey_RSA, encryptText_AESKey, encryptText);
  let dec_message = buffer.from(decryptText.data).toString('utf-8');
  console.info('结果对比：' + (message === dec_message));
}
```
