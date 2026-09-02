---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-61
title: AES加密密文与其他端结果不一致如何解决
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > AES加密密文与其他端结果不一致如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:de0e304acac546d35e04d4347ddaa25f7738a126eab799521bdbefeb4598339c
---

## 问题现象

采用和其他端一致的密钥参数使用AES算法加密，结果与其他端加密结果不一致，导致服务端无法实现解密，以AES的GCM模式为例。

HarmonyOS端代码如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

const aesKey = 'cZP1VQZUcwfp4mxFpXGP1x22oUFRL9aP';
const aesIv = 'J5VaZ4fNZY87YgXR';

function genGcmParamsSpec() {
  let iv = new Uint8Array(buffer.from(aesIv, 'utf-8').buffer);
  let ivBlob: cryptoFramework.DataBlob = { data: iv };
  let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: { data: new Uint8Array() },
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}
let gcmParams = genGcmParamsSpec();
// 加密消息
function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('AES256|GCM|NoPadding');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  let encryptUpdate = cipher.updateSync(plainText);
  // gcm模式加密doFinal时传入空，获得tag数据，并更新至gcmParams对象中。
  gcmParams.authTag = cipher.doFinalSync(null);
  return encryptUpdate;
}

function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let aesGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let symKey = aesGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

export function aesMain() {
  let originalData = '{121212}';
  let keyData = new Uint8Array(buffer.from(aesKey, 'utf-8').buffer);
  let symKey = genSymKeyByData(keyData);
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(originalData, 'utf-8').buffer) };
  let encryptText = encryptMessage(symKey, plainText);
  let base64 = new util.Base64Helper();
  console.info(`encryptText: ${base64.encodeToStringSync(encryptText.data)}`);
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column({ space: 10 }) {
        Button('click me').onClick(() => {
          aesMain();
        });
      }.width('100%');
    }.height('100%');
  }
}
```

服务端代码如下：

```java
import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Main {
    private static final String AES = "AES";
    private static final int TAG_LENGTH_BIT = 128;

    public static byte[] encrypt(byte[] data, SecretKey secretKey, byte[] iv) {
        try {
            Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
            GCMParameterSpec parameterSpec = new GCMParameterSpec(TAG_LENGTH_BIT, iv);
            cipher.init(Cipher.ENCRYPT_MODE, secretKey, parameterSpec);
            return cipher.doFinal(data);
        } catch (Exception e) {
            System.out.println("Error encrypting data." + e.getMessage());
        }
        return data;
    }

    static String aesKey = "cZP1VQZUcwfp4mxFpXGP1x22oUFRL9aP";
    static String aesIv = "J5VaZ4fNZY87YgXR";

    public static void main(String[] args) throws NoSuchAlgorithmException {
        byte[] keyBytes = aesKey.getBytes();
        SecretKey secretKey = new SecretKeySpec(keyBytes, 0, keyBytes.length, AES);
        byte[] iv = aesIv.getBytes();
        String originalData = "{121212}";
        byte[] originalBytes = originalData.getBytes(StandardCharsets.UTF_8);
        byte[] encryptedBytes = Main.encrypt(originalBytes, secretKey, iv);

        String encryptedDataStringBase64 = Base64.getEncoder().encodeToString(encryptedBytes);
        System.out.println("Encrypted Data (Base64): " + encryptedDataStringBase64);
    }
}
```

预期结果：HarmonyOS端和服务端输出结果一致为RZAKy0GGeyNu29J1Kin3NF9XhXF/gmdl。

实际结果：HarmonyOS端为RZAKy0GGeyM=，服务端为RZAKy0GGeyNu29J1Kin3NF9XhXF/gmdl。

## 背景知识

[AES](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#aes)：AES是一种典型的对称密钥加密算法，算法库提供7种加密模式：ECB、CBC、OFB、CFB、CTR、GCM和CCM。

[doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal)：在对称加解密中doFinal用于处理剩余数据和本次传入的数据，并最终结束加密或解密操作，如果数据量较小，可以在doFinal中一次性传入数据，获得的结果包含密文和authTag，且执行结果与加密模式有关，如GCM模式下authTag为末尾的16字节。

## 问题定位

HarmonyOS端的加密结果与其他端不一致，常见原因包含参数不一致、加密模式影响等，可结合加密模式与使用参数进行排查：

1. 检查两端所使用的明文与加密参数是否一致，包括填充模式、密钥、加解密参数等。
2. 检查数据的编码格式处理方法是否一致，检查对象包含明文、加密密文结果以及密钥参数等，检查转码方式包含Base64编解码、16进制转换等是否两端一致。
3. 结合加密模式查看加密结果处理方式是否正确，如doFinal方法GCM模式返回的结果包含authTag，服务端的结果是否为仅密文格式。

## 分析结论

1. 确认双端均采用GCM模式进行加密，密钥和加密参数一致，填充模式不一致，由于GCM加密模式下不需要对明文进行填充，不影响加密结果。
2. 编码方式选择一致，加密结果均采用Base64编码方式处理。
3. HarmonyOS端的结果为update方法返回结果进行Base64编码处理的内容，仅包含密文，而服务端执行结果默认包含密文和authTag，因此结果不一致。

## 修改建议

* 方式一：本示例中加密数据量小，可直接调用cipher.doFinal方法加密，无需在调用前使用update方法，加密结果包含密文和authTag。
* 方式二：数据量大使用update方法的场景下，将update和doFinal方法返回的结果进行拼接，然后通过Base64编码即可获得与服务端相同的加密结果，示例参考如下：

  ```ts
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer, util } from '@kit.ArkTS';

  const aesKey = 'cZP1VQZUcwfp4mxFpXGP1x22oUFRL9aP';
  const aesIv = 'J5VaZ4fNZY87YgXR';

  function genGcmParamsSpec() {
    let iv = new Uint8Array(buffer.from(aesIv, 'utf-8').buffer);
    let ivBlob: cryptoFramework.DataBlob = { data: iv };
    let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
    let dataTag = new Uint8Array(arr);
    let tagBlob: cryptoFramework.DataBlob = {
      data: dataTag
    };
    // GCM的authTag在加密时从doFinal结果中获取，在解密时填入init函数的params参数中
    let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
      iv: ivBlob,
      aad: { data: new Uint8Array() },
      authTag: tagBlob,
      algName: 'GcmParamsSpec'
    };
    return gcmParamsSpec;
  }

  let gcmParams = genGcmParamsSpec();

  // 加密消息
  function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('AES256|GCM|NoPadding');
    cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
    let encryptUpdate = cipher.updateSync(plainText);
    // gcm模式加密doFinal时传入空，获得tag数据，并更新至gcmParams对象中。
    // 数据量小直接调用doFinal，返回结果通过Base64编码与其他端一致
    gcmParams.authTag = cipher.doFinalSync(null);
    return encryptUpdate;
  }

  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let aesGenerator = cryptoFramework.createSymKeyGenerator('AES256');
    let symKey = aesGenerator.convertKeySync(symKeyBlob);
    console.info('convertKeySync success');
    return symKey;
  }

  export function aesMain() {
    let originalData = '{121212}';
    let keyData = new Uint8Array(buffer.from(aesKey, 'utf-8').buffer);
    let symKey = genSymKeyByData(keyData);
    let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(originalData, 'utf-8').buffer) };
    let encryptText = encryptMessage(symKey, plainText);
    let encBuffer: ArrayBuffer = new ArrayBuffer(encryptText.data.length + gcmParams.authTag?.data.length);
    let encResult: Uint8Array = new Uint8Array(encBuffer);
    // 密文与authTag拼接，通过Base64编码即为其他端一致格式
    encResult.set(encryptText.data, 0);
    encResult.set(gcmParams.authTag.data, encryptText.data.length);
    let base64 = new util.Base64Helper();
    console.info(`encryptText: ${base64.encodeToStringSync(encResult)}`);
  }

  @Entry
  @Component
  struct Index {
    build() {
      Row() {
        Column({ space: 10 }) {
          Button('click me').onClick(() => {
            aesMain();
          });
        }.width('100%');
      }.height('100%');
    }
  }
  ```

## 总结

对于GCM模式的对称加密：一次加密流程中，如果将每一次update和doFinal的结果拼接起来，会得到“密文+authTag”。如果doFinal的data参数传入null，则doFinal的结果仅包含authTag。
