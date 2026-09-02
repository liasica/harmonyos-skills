---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-customsecurityconfig
title: SecurityConfiguration：定制安全传输行为
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 实现HTTP请求定制 > Configuration：高效实现定制功能 > SecurityConfiguration：定制安全传输行为
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:63320b51a9d716875048b108dc380029050598e060a67a7c92dfa7dcc00dfec0
---

## 场景介绍

在软件开发中，安全是非常重要的一环。Remote Communication Kit提供的[SecurityConfiguration](../harmonyos-references/remote-communication-rcp.md#securityconfiguration)是一个用于定制安全传输行为的工具，能够帮助开发者更好地保护其应用程序。通过合理的配置和使用，可以显著降低应用程序遭受攻击的风险。下面将详细说明如何使用证书校验来增强安全性。

| 证书校验方式 | 可以配置的参数 |
| --- | --- |
| remoteValidation（客户端校验服务端证书） | 'system'：使用系统默认证书。  'skip'：跳过证书校验。  CertificateAuthority：通过content指定证书内容，filePath指定证书文件路径，folderPath指定证书目录。  ValidationCallback：自定义证书。 |
| certificate（服务端校验客户端证书） | ClientCertificate（客户端证书校验）：通过content指定证书内容，filePath指定证书文件路径，type指定证书类型，并通过key和keyPassword分别指定私钥及其密码。 |

## 约束与限制

定制安全传输行为能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 客户端校验服务端证书

### 使用系统默认证书

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置'system'时，将使用系统中默认的CA。

   ```typescript
   async function testSystemRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         remoteValidation: 'system',
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 跳过证书校验

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置'skip'跳过证书校验。

   ```typescript
   async function testSkipRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         remoteValidation: 'skip',
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 使用字符串指定证书内容

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置content，可以配置string类型证书内容。

   ```typescript
   const PEM_CA_STRING = '-----BEGIN CERTIFICATE-----\n' +
     'MIICPzCCAcWgAwIBAgIQBVVWvPJepDU1w6QP1atFcjAKBggqhkjOPQQDAzBhMQswCQYDVQQGEwJV\n' +
     'UzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYD\n' +
     'VQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBHMzAeFw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAw\n' +
     'MDBaMGExCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5k\n' +
     'aWdpY2VydC5jb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEczMHYwEAYHKoZIzj0C\n' +
     'AQYFK4EEACIDYgAE3afZu4q4C/sLfyHS8L6+c/MzXRq8NOrexpu80JX28MzQC7phW1FGfp4tn+6O\n' +
     'YwwX7Adw9c+ELkCDnOg/QW07rdOkFFk2eJ0DQ+4QE2xy3q6Ip6FrtUPOZ9wj/wMco+I+o0IwQDAP\n' +
     'BgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUs9tIpPmhxdiuNkHMEWNp\n' +
     'Yim8S8YwCgYIKoZIzj0EAwMDaAAwZQIxAK288mw/EkrRLTnDCgmXc/SINoyIJ7vmiI1Qhadj+Z4y\n' +
     '3maTD/HMsQmP3Wyr+mt/oAIwOWZbwmSNuJ5Q3KjVSaLtx9zRSX8XAbjIho9OjIgrqJqpisXRAL34\n' +
     'VOKa5Vt8sycX\n' +
     '-----END CERTIFICATE-----';

   async function testStringRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         remoteValidation: {
           content: PEM_CA_STRING,
         }
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 使用二进制指定证书内容

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置content，可以配置ArrayBuffer类型证书内容。

   ```typescript
   const PEM_CA_BINARY = '-----BEGIN CERTIFICATE-----\n' +
     'MIICPzCCAcWgAwIBAgIQBVVWvPJepDU1w6QP1atFcjAKBggqhkjOPQQDAzBhMQswCQYDVQQGEwJV\n' +
     'UzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYD\n' +
     'VQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBHMzAeFw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAw\n' +
     'MDBaMGExCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5k\n' +
     'aWdpY2VydC5jb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEczMHYwEAYHKoZIzj0C\n' +
     'AQYFK4EEACIDYgAE3afZu4q4C/sLfyHS8L6+c/MzXRq8NOrexpu80JX28MzQC7phW1FGfp4tn+6O\n' +
     'YwwX7Adw9c+ELkCDnOg/QW07rdOkFFk2eJ0DQ+4QE2xy3q6Ip6FrtUPOZ9wj/wMco+I+o0IwQDAP\n' +
     'BgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUs9tIpPmhxdiuNkHMEWNp\n' +
     'Yim8S8YwCgYIKoZIzj0EAwMDaAAwZQIxAK288mw/EkrRLTnDCgmXc/SINoyIJ7vmiI1Qhadj+Z4y\n' +
     '3maTD/HMsQmP3Wyr+mt/oAIwOWZbwmSNuJ5Q3KjVSaLtx9zRSX8XAbjIho9OjIgrqJqpisXRAL34\n' +
     'VOKa5Vt8sycX\n' +
     '-----END CERTIFICATE-----';

   async function testBinaryRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     const buffer = new ArrayBuffer(PEM_CA_BINARY.length);
     util.TextEncoder.create('utf-8').encodeIntoUint8Array(PEM_CA_BINARY, new Uint8Array(buffer));
     request.configuration = {
       security: {
         remoteValidation: {
           content: buffer,
         }
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 使用文件指定证书内容

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 准备证书文件。在本例中，假设证书是example.pem，使用OpenSSL命令生成目标文件。

   ```cmd
   openssl x509 -subject_hash -in ./example.pem
   ```

   命令输出如下。以第一行为目标文件名，以.0为文件扩展名，以其他内容为文件内容，将输出保存为dd8e9d41.0。如果您使用Windows系统，OpenSSL可能会等待用户输入才会退出，按Enter键即可。

   ```cmd
   dd8e9d41
   -----BEGIN CERTIFICATE-----
   MIICPzCCAcWgAwIBAgIQBVVWvPJepDU1w6QP1atFcjAKBggqhkjOPQQDAzBhMQsw
   CQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cu
   ZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBHMzAe
   Fw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAwMDBaMGExCzAJBgNVBAYTAlVTMRUw
   EwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5jb20x
   IDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEczMHYwEAYHKoZIzj0CAQYF
   K4EEACIDYgAE3afZu4q4C/sLfyHS8L6+c/MzXRq8NOrexpu80JX28MzQC7phW1FG
   fp4tn+6OYwwX7Adw9c+ELkCDnOg/QW07rdOkFFk2eJ0DQ+4QE2xy3q6Ip6FrtUPO
   Z9wj/wMco+I+o0IwQDAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAd
   BgNVHQ4EFgQUs9tIpPmhxdiuNkHMEWNpYim8S8YwCgYIKoZIzj0EAwMDaAAwZQIx
   AK288mw/EkrRLTnDCgmXc/SINoyIJ7vmiI1Qhadj+Z4y3maTD/HMsQmP3Wyr+mt/
   oAIwOWZbwmSNuJ5Q3KjVSaLtx9zRSX8XAbjIho9OjIgrqJqpisXRAL34VOKa5Vt8
   sycX
   -----END CERTIFICATE-----
   ```
3. 在remoteValidation中通过filePath指定证书路径。关于文件路径，请参考[应用文件](app-file.md)。

   ```typescript
   async function testFileRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         remoteValidation: {
           filePath: '/data/storage/el1/bundle/entry/resources/resfile/dd8e9d41.0', // 将生成证书改名放入/resources/resfile/下
         }
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 使用文件目录指定证书

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置folderPath指定证书所在的沙箱目录。关于文件路径，请参考[应用文件](app-file.md)。目录中的证书文件格式和内容请参考示例5中的步骤2。

   ```typescript
   async function testDirRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         remoteValidation: {
           folderPath: '/data/storage/el1/bundle/entry/resources/resfile/', // 正式使用时需替换成证书所在的沙箱目录。
         }
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 自定义证书校验

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 校验证书的日期是否符合预期。

   ```typescript
   function makeItTwoChar(s: string): string {
     if (s.length === 1) {
       return '0' + s;
     }
     return s;
   }
   function getASNDateString(): string {
     const date = new Date();
     let dateStr = date.getFullYear().toString().slice(2);
     dateStr += makeItTwoChar((date.getMonth() + 1).toString());
     dateStr += makeItTwoChar(date.getDate().toString());
     dateStr += makeItTwoChar(date.getHours().toString());
     dateStr += makeItTwoChar(date.getMinutes().toString());
     dateStr += makeItTwoChar(date.getSeconds().toString());
     return dateStr + 'Z';
   }
   ```
3. 自定义证书校验逻辑。

   ```typescript
   async function validationRemoteServer(context: rcp.ValidationContext): Promise<boolean> {
     // 服务器未返回证书，校验失败
     let length = context.pemCerts.length;
     if (length <= 0) {
       return Promise.reject();
     }
     // 此示例中最后一个证书为根证书，开发中请根据实际情况调整
     const firstCaBlob: networkSecurity.CertBlob = {
       type: networkSecurity.CertType.CERT_TYPE_PEM,
       data: context.pemCerts[length - 1],
     }
     // 如果 certVerificationSync 的第二个参数未填写，则使用系统默认的 CA（"/etc/security/certificates"）进行验证
     if (networkSecurity.certVerificationSync(firstCaBlob) !== 0) {
       return Promise.reject();
     }
     // 此处可以添加所需的校验逻辑，如校验日期
     for (const x of context.x509Certs) {
       let dateStr = getASNDateString();
       try {
         x.checkValidityWithDate(dateStr);
       } catch (e) {
         return Promise.reject();
       }
     }
     // ...
     // 校验成功
     return Promise.resolve(true);
   }
   ```
4. 将定义好的自定义证书校验器配置到configuration中，并利用fetch发起请求。

   ```typescript
   async function testCustomRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         remoteValidation: validationRemoteServer,
       }
     }
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

## 服务器校验客户端证书

### 校验PEM类型证书

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 本示例使用自签名证书，以便完整演示本地证书生成流程。请通过以下OpenSSL命令依次完成：生成私钥、创建证书签名请求（CSR）文件、基于CSR签发自签名证书、将私钥与证书合并为PEM格式的完整证书文件。

   注意：本示例使用自签名证书演示流程，实际生产环境中一般采用由可信证书颁发机构（CA）正式签发的证书。

   ```cmd
   openssl genrsa -out cert.key 2048
   openssl req -new -key cert.key -out cert.csr
   openssl x509 -req -in cert.csr -out cert.crt -signkey cert.key -CAcreateserial -days 3650
   openssl x509 -in cert.crt -out cert.pem -outform PEM
   ```
3. 在certificate中通过filePath指定证书路径（也可以通过content指定证书内容），type配置PEM指定证书类型，key和keyPassword指定证书私钥和密码。关于文件路径，请参考[应用文件](app-file.md)。

   ```typescript
   async function testPemRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         certificate: {
           filePath: '/data/storage/el1/bundle/entry/resources/resfile/cert.pem', // 将生成证书放入/resources/resfile/下
           type: 'PEM',
           key: '/data/storage/el1/bundle/entry/resources/resfile/cert.key', // 这是证书私钥，放入/resources/resfile/下，可选
           keyPassword: 'keyPassword', // 证书私钥的密码，在使用中请替换为实际的证书秘钥密码，可选，本例中不生效
         }
       }
     };
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 校验DER类型证书

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在certificate中通过filePath指定证书路径（也可以通过content指定证书内容），type配置DER指定证书类型，key和keyPassword指定证书私钥和密码。使用openssl x509 -in cert.pem -outform der -out cert.der命令将上面例子中的pem文件转为der文件。关于文件路径，请参考[应用文件](app-file.md)。

   ```typescript
   async function testDerRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         certificate: {
           filePath: '/data/storage/el1/bundle/entry/resources/resfile/cert.der', // 将生成证书放入/resources/resfile/下
           type: 'DER',
           key: '/data/storage/el1/bundle/entry/resources/resfile/cert.key', // 这是证书私钥，放入/resources/resfile/下，可选
           keyPassword: 'keyPassword', // 证书私钥的密码，在使用中请替换为实际的证书秘钥密码，可选，本例中不生效
         }
       }
     };
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

### 校验P12类型证书

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在certificate中配置filePath指定证书路径（也可以配置content指定证书内容），type配置P12指定证书类型，keyPassword指定证书私钥的密码。使用openssl pkcs12 -export -out cert.p12 -inkey cert.key -in cert.pem命令将上面例子中的pem文件转为P12证书，设置密码“1234”。关于文件路径，请参考[应用文件](app-file.md)。

   ```typescript
   async function testPRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         certificate: {
           filePath: '/data/storage/el1/bundle/entry/resources/resfile/cert.p12', // 将生成证书放入/resources/resfile/下
           type: 'P12', // P12证书已包含私钥，不需要使用key指定私钥
           keyPassword: '1234', // 证书私钥的密码，在使用中请替换为实际的证书秘钥密码，可选
         }
       }
     };
     try {
       const response = await session.fetch(request);
       console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
       // ...
       console.info(`response: ${JSON.stringify(response.toString())}`);
     } catch (err) {
       console.error(`response error code is ${err.code}, error data is ${err.data}`);
       // ...
     } finally {
       session.close();
     }
   }
   ```

## 证书锁定

证书锁定可以设置信任的证书的范围。通过比较证书公钥的SHA256哈希值的BASE64编码，限定可信任的证书。

* 可以通过以下OpenSSL命令获得证书公钥，其中，example.pem是服务器的PEM格式的证书，请替换为实际证书：

  ```cmd
  openssl x509 -in example.pem -noout -pubkey | openssl asn1parse -noout -inform pem -out example.public.key
  ```
* 可以通过以下OpenSSL命令计算公钥的SHA256哈希值的BASE64编码，其中，example.public.key是上一步生成的证书的公钥：

  ```cmd
  openssl dgst -sha256 -binary example.public.key | openssl enc -base64
  ```

1. 导入需要的模块。

   ```typescript
   import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在certificatePinning中配置可信任的证书公钥的SHA256哈希值。

   ```typescript
   const RIGHT_EXAMPLE_PUBLIC_KEY_SHA256_HASH = [
     'iMMpIJdSf5VlClHaxZReyhaLxLsmZMMNAiA2pMR8/M4=', // 请替换成需要的字符串
     'qBRjZmOmkSNJL0p70zek7odSIzqs/muR4Jk9xYyCP+E=', // 请替换成需要的字符串
     '47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=', // 请替换成需要的字符串
   ];

   async function testPinningRcp() {
     const session = rcp.createSession();
     const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
     request.configuration = {
       security: {
         certificatePinning: [
           {
             kind: 'public-key',
             publicKeyHash: RIGHT_EXAMPLE_PUBLIC_KEY_SHA256_HASH[0],
             hashAlgorithm: 'SHA-256'
           },
           {
             kind: 'public-key',
             publicKeyHash: RIGHT_EXAMPLE_PUBLIC_KEY_SHA256_HASH[1],
             hashAlgorithm: 'SHA-256'
           },
         ]
       }
     };
     try {
       const response = await session.fetch(request);
       console.info('Test certificate pinning ' + response.statusCode);
       // ...
     } catch (e) {
       console.error('Test certificate pinning ' + JSON.stringify(e));
       // ...
     } finally {
       session.close();
     }
   }
   ```
