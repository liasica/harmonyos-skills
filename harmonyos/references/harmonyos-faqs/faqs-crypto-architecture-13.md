---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-13
title: 如何实现RSA的公钥PK加密一段文字
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何实现RSA的公钥PK加密一段文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:226ad5c10a8955f62514fe33a77450f83f07f8e8402e9f128c2ad9be8f5c37d8
---

算法库目前提供了RSA加解密常用的三种模式：NoPadding、PKCS1 和 PKCS1\_OAEP。不同 RSA 密钥规格和不同填充方式支持加密的数据长度不同，详情见参考链接。

参考代码如下：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

// Convert string to byte stream 
function stringToUint8Array(str: string) {
  return new Uint8Array(buffer.from(str, 'utf-8').buffer);
}

// Convert byte stream into an understandable string
function uint8ArrayToString(array: Uint8Array) {
  // Convert UTF-8 encoding to Unicode encoding
  let out: string = '';
  let index: number = 0;
  let len: number = array.length;
  while (index < len) {
    let character = array[index++];
    switch (character >> 4) {
      case 0:
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
      case 6:
      case 7:
        out += String.fromCharCode(character);
        break;
      case 12:
      case 13:
        out += String.fromCharCode(((character & 0x1F) << 6) | (array[index++] & 0x3F));
        break;
      case 14:
        out += String.fromCharCode(((character & 0x0F) << 12) | ((array[index++] & 0x3F) << 6) |
          ((array[index++] & 0x3F) << 0));
        break;
      default:
        break;
    }
  }
  return out;
}

export class KeyPair {
  publicKey: string = '';
  privateKey: string = '';
}

export class RSA {
  private ASY_KEY_NAME_RSA_3072: string = 'RSA1024';
  private ALG_NAME_RSA_3072: string = 'RSA|PKCS1';
  static priKey: Uint8Array = new Uint8Array(); // For temporary storage
  static pubKey: Uint8Array = new Uint8Array(); // For temporary storage
  private base: util.Base64Helper = new util.Base64Helper();

  public async generateRsaKeyPair(): Promise<KeyPair> {
    let keyPair: KeyPair = new KeyPair();
    try {
      let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator(this.ASY_KEY_NAME_RSA_3072);
      const tempKeyPair = await asyKeyGenerator.generateKeyPair();
      keyPair = {
        publicKey: this.base.encodeToStringSync(tempKeyPair.pubKey.getEncoded().data),
        privateKey: this.base.encodeToStringSync(tempKeyPair.priKey.getEncoded().data)
      }
    } catch (err) {
      console.error(err);
    }
    return keyPair;
  }

  public async add(str: string, publicKey: string): Promise<string> {
    let result = '';
    try {
      let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator(this.ASY_KEY_NAME_RSA_3072);
      // Create a Cipher (decryption) object 
      let cipher = cryptoFramework.createCipher(this.ALG_NAME_RSA_3072);
      // Introduce external public key encryption
      let keyGenPromise: cryptoFramework.KeyPair =
        await asyKeyGenerator.convertKey({ data: this.base.decodeSync(publicKey) }, null);
      await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyGenPromise.pubKey, null);
      let put: cryptoFramework.DataBlob = { data: stringToUint8Array(str) };
      const finalRes = await cipher.doFinal(put);
      result = this.base.encodeToStringSync(finalRes.data);
      console.info(result);
    } catch (err) {
      console.log(err.message);
    }
    return result;
  }

  public async rsaDecrypt(message: string | Uint8Array, privateKey: string): Promise<string> {
    let result = '';
    try {
      let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator(this.ASY_KEY_NAME_RSA_3072);
      const keyPair = await asyKeyGenerator.convertKey(null, { data: this.base.decodeSync(privateKey) });
      let cipher = cryptoFramework.createCipher(this.ALG_NAME_RSA_3072); // Create a Cipher (decryption) object
      await cipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, keyPair.priKey, null);
      let bytes: Uint8Array | string = message;
      if (typeof message === 'string') {
        bytes = this.base.decodeSync(message);
      } else {
        bytes = message;
      }
      const finalRes = await cipher.doFinal({ data: bytes });
      result = uint8ArrayToString(finalRes.data);
      console.info(result);
    } catch (err) {
      console.error(err.code);
    }
    return result;
  }
}

@Entry
@Component
struct EncryptedText {
  @State word: string = '加解密文字';
  private EncryptionAndDecryption = new RSA();

  async aboutToAppear(): Promise<void> {
    let key = await this.EncryptionAndDecryption.generateRsaKeyPair();
    let result = await this.EncryptionAndDecryption.add(this.word, key.publicKey);
    this.EncryptionAndDecryption.rsaDecrypt(result, key.privateKey);
  }

  build() {
  }
}
```

**参考链接：**

[RSA](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#rsa)
