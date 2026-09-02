---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-63
title: 如何适配服务端AES加解密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何适配服务端AES加解密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:447539ce3766c51afde42182f53d662d517fabd925bf1ba470dbd0d4ca67b27a
---

## 问题现象

AES是常用的对称密钥加解密算法，HarmonyOS端和服务端传输的加密数据互相进行解密是常见场景，使用时发现HarmonyOS端无法解密服务端加密密文，如何参考服务端加解密代码生成HarmonyOS加解密。

服务端AES加解密代码：

```java
public class AESUtil {

    private static final String ALGORITHM = "AES/ECB/PKCS5Padding";

    public static String encrypt(String data, String key) throws Exception {
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] encrypted = cipher.doFinal(data.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }

    public static String decrypt(String encryptedData, String key) throws Exception {
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        byte[] decoded = Base64.getDecoder().decode(encryptedData);
        byte[] decrypted = cipher.doFinal(decoded);
        return new String(decrypted);
    }

    public static void main(String[] args) {
        try {
            // 16字节密钥（128位）
            String key = "1234567890123456";
            String text = "这是一条测试密文";

            System.out.println("data: " + text);

            String encrypted = encrypt(text, key);
            System.out.println("encrypted: " + encrypted);

            String decrypted = decrypt(encrypted, key);
            System.out.println("decrypted: " + decrypted);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

加密密文为：

```shell
MPpBFmzUAW276P3C5cAQj7CSeVxb85MFUnPzxPQ1O30=
```

## 解决方案

HarmonyOS端对应代码如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

const base64 = new util.Base64Helper();

// 加密消息。
function encryptMessage(symKey: cryptoFramework.SymKey, message: string) {
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let cipher = cryptoFramework.createCipher('AES128|ECB|PKCS5');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null); // ECB模式params为null。
  let cipherData = cipher.doFinalSync(plainText);
  return base64.encodeToStringSync(cipherData.data);
}

// 解密消息。
function decryptMessage(symKey: cryptoFramework.SymKey, encryptText: string) {
  let cipherText: cryptoFramework.DataBlob = { data: base64.decodeSync(encryptText) };
  let decoder = cryptoFramework.createCipher('AES128|ECB|PKCS5');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null); // ECB模式params为null。
  let decryptData = decoder.doFinalSync(cipherText);
  return buffer.from(decryptData.data).toString('utf-8');
}

function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = aesGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

function main() {
  try {
    let aesKey = '1234567890123456';
    let keyData = new Uint8Array(buffer.from(aesKey, 'utf-8').buffer);
    let symKey = genSymKeyByData(keyData);
    let message = '这是一条测试密文';
    console.info(`original data: ${message}`);
    let encryptText = encryptMessage(symKey, message);
    console.info(`decrypt plainText: ${encryptText}`);
    let decryptText = decryptMessage(symKey, encryptText);
    console.info(`decrypt plainText: ${decryptText}`);
  } catch (error) {
    console.error(`AES ECB error code: ${error.code}`);
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column({ space: 10 }) {
        Button('click me').onClick(() => {
          main();
        });
      }.width('100%');
    }.height('100%');
  }
}
```

## 总结

加解密算法使用过程需要对明文或密文数据做编码格式处理，本示例中服务端对加密结果采用Base64编码，在HarmonyOS端同样需要保持同样的编解码处理。
