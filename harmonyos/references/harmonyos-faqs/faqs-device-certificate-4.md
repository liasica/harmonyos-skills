---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-certificate-4
title: 如何解决createX509Cert读取证书文件获取的PublicKey使用报错问题
breadcrumb: FAQ > 系统开发 > 安全 > 证书管理（Device Certificate） > 如何解决createX509Cert读取证书文件获取的PublicKey使用报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81164865562acf0a886e1496277468d114602b016f9e55ddc021192f1baae5c8
---

## 问题现象

使用certFramework的createX509Cert读取证书文件，使用getPublicKey方法可以成功获取到公钥，但使用此公钥进行初始化报错。

```screen
let publicKey = x509Cert.getPublicKey().getEncoded()
// 创建实例化对象
let cipher = cryptoFramework.createCipher('RSA1024|PKCS1')
// 初始化加解密对象
cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null)
```

## 背景知识

* 创建X509证书对象：[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)。
* 获取X509证书公钥：[x509Cert.getPublicKey()](../harmonyos-references/js-apis-cert.md#getpublickey)。
* 同步获取指定数据生成非对称密钥：[AsyKeyGenerator.convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12-1)。
* 初始化加解密的cipher对象：[cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)。

## 问题定位

1. 确认获取的公钥是否满足RSA公钥格式。
2. 获取到的公钥有没有加载到RSA密钥对象中。

## 分析结论

虽然成功获取到证书中的公钥，但没有将公钥数据通过convertKey方法生成RSA公钥进而加载到密钥对象中，就直接使用此公钥进行初始化操作，导致公钥参数错误引发初始化报错。

## 修改建议

将读取证书获取的公钥数据，通过convertKey方法生成RSA公钥，然后再使用此公钥进行初始化、加密数据等操作。

```screen
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import certFramework from '@ohos.security.cert';
import { BusinessError } from '@kit.BasicServicesKit';
import { cert } from '@kit.DeviceCertificateKit';
import { buffer } from '@kit.ArkTS';

function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

function create509(encodingBlob: certFramework.EncodingBlob, cb: (s: string) => void,
  errorCB: (error: BusinessError) => void) {
  certFramework.createX509Cert(encodingBlob).then(async x509Cert => {
    let publicKey = x509Cert.getPublicKey().getEncoded().data.toString();
    console.info('createX509Cert success: publicKey = ' + publicKey);
    // 进行密钥转换
    let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
    let keyPair = rsaGenerator.convertKeySync(x509Cert.getPublicKey().getEncoded(), null);
    // 创建实例化对象
    let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
    // 初始化加解密对象
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);

    let sha1 = '32**************d7';
    let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(sha1, 'utf-8').buffer) };

    cipher.doFinal(plainText).then((data) => {
      console.info('encryptData: ' + data.data);
      cb('ok');
    }).catch((e: BusinessError) => {
      console.error('error', e);
      errorCB(e);
    });
  }).catch((error: BusinessError) => {
    console.error('createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    errorCB(error);
  });
}

@Entry
@Component
struct CreateX509Cert {
  @State
  message: string = '';

  aboutToAppear(): void {
    // 证书二进制数据，需业务自行赋值。
    let certData = '-----BEGIN CERTIFICATE-----\r\n' +
      'MIIDTjCCAjagAwIBAgIBBDANBgkqhkiG9w0BAQsFADASMRAwDgYDVQQDDAdSb290\n' +
      'IENBMB4XDTI0MDMxOTAyMDQwMVoXDTM0MDMxNzAyMDQwMVowEjEQMA4GA1UEAwwH\n' +
      'ZGV2aWNlMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIXL3e7UE/c\n' +
      'Z1dPVgRZ5L8gsQ/azuYVBvoFf7o8ksYrL7G1+qZIJjVRqZkuTirLW4GicbkIkPNW\n' +
      'eix5cDhkjkC+q5SBCOrSSTTlvX3xcOY1gMlA5MgeBfGixFusq4d5VPF2KceZ20/a\n' +
      'ygwGD0Uv0X81OERyPom/dYdJUvfaD9ifPFJ1fKIj/cPFG3yJK/ojpEfndZNdESQL\n' +
      'TkoDekilg2UGOLtY6fb9Ns37ncuIj33gCS/R9m1tgtmqCTcgOQ4hwKhjVF3InmPO\n' +
      '2BbWKvD1RUX+rHC2a2HHDQILOOtDTy8dHvE+qZlK0efrpRgoFEERJAGPi1GDGWiA\n' +
      '7UX1c4MCxIECAwEAAaOBrjCBqzAJBgNVHRMEAjAAMB0GA1UdDgQWBBQbkAcMT7ND\n' +
      'fGp3VPFzYHppZ1zxLTAfBgNVHSMEGDAWgBR0W/koCbvDtFGHUQZLM3j6HKsW2DAd\n' +
      'BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwCwYDVR0PBAQDAgeAMDIGCCsG\n' +
      'AQUFBwEBBCYwJDAiBggrBgEFBQcwAYYWaHR0cHM6Ly8xMjcuMC4wLjE6OTk5OTAN\n' +
      'BgkqhkiG9w0BAQsFAAOCAQEAF1OTzTmbklFOdZCxrF3zg9owUPJR5RB+PbuBlUfI\n' +
      '8tkGXkMltQ8PN1dv6Cq+d8BluiJdWEzqVoJa/e5SHHJyYQSOhlurRG0GBXllVQ1I\n' +
      'n1PFaI40+9X2X6wrEcdC5nbzogR1jSiksCiTcARMddj0Xrp5FMrFaaGY8M/xqzdW\n' +
      'LTDl4nfbuxtA71cIjnE4kOcaemly9/S2wYWdPktsPxQPY1nPUOeJFI7o0sH3rK0c\n' +
      'JSqtgAG8vnjK+jbx9RpkgqCsXgUbIahL573VTgxrNrsRjCuVal7XVxl/xOKXr6Er\n' +
      'Gpc+OCrXbHNZkUQE5fZH3yL2tXd7EASEb6J3aEWHfF8YBA==\n' +
      '-----END CERTIFICATE-----';

    let encodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(certData),
      // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
    };
    create509(encodingBlob, () => {
      this.message = 'ok';
    }, (e) => {
      this.message = 'error:' + e.message;
    });
  }

  build() {
    Row() {
      Column() {
        Text(this.message);
      }.justifyContent(FlexAlign.Center);
    }.width('100%').height('100%').justifyContent(FlexAlign.Center);
  }
}
```

## 总结

使用证书中的公钥数据进行加解密相关操作，需要注意中间流程的公钥数据流转与转换，避免使用错误的公钥数据进行相关操作，相关API的使用需要满足其使用条件。
