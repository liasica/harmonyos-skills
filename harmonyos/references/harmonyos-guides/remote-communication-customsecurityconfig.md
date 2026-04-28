---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-customsecurityconfig
title: SecurityConfiguration：定制安全传输行为
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 使用HTTP协议进行网络通信 > 实现HTTP请求定制 > Configuration：高效实现定制功能 > SecurityConfiguration：定制安全传输行为
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4acc394d94f41f70991d1180b862452015b0c4ac1a3acb9d595532d1ef3ab530
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

### 1. 使用系统默认证书

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置'system'时，将使用系统中默认的CA。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. remoteValidation: 'system',
   7. }
   8. }
   9. try {
   10. const response = await session.fetch(request);
   11. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   12. console.info(`response: ${JSON.stringify(response.toString())}`);
   13. } catch (err) {
   14. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   15. } finally {
   16. session.close();
   17. }
   18. }
   ```

### 2. 跳过证书校验

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置'skip'跳过证书校验。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. remoteValidation: 'skip',
   7. }
   8. }
   9. try {
   10. const response = await session.fetch(request);
   11. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   12. console.info(`response: ${JSON.stringify(response.toString())}`);
   13. } catch (err) {
   14. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   15. } finally {
   16. session.close();
   17. }
   18. }
   ```

### 3. 使用字符串指定证书内容

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置content，可以配置string类型证书内容。

   ```
   1. const PEM_CA = '-----BEGIN CERTIFICATE-----\n' +
   2. 'MIICPzCCAcWgAwIBAgIQBVVWvPJepDU1w6QP1atFcjAKBggqhkjOPQQDAzBhMQswCQYDVQQGEwJV\n' +
   3. 'UzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYD\n' +
   4. 'VQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBHMzAeFw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAw\n' +
   5. 'MDBaMGExCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5k\n' +
   6. 'aWdpY2VydC5jb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEczMHYwEAYHKoZIzj0C\n' +
   7. 'AQYFK4EEACIDYgAE3afZu4q4C/sLfyHS8L6+c/MzXRq8NOrexpu80JX28MzQC7phW1FGfp4tn+6O\n' +
   8. 'YwwX7Adw9c+ELkCDnOg/QW07rdOkFFk2eJ0DQ+4QE2xy3q6Ip6FrtUPOZ9wj/wMco+I+o0IwQDAP\n' +
   9. 'BgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUs9tIpPmhxdiuNkHMEWNp\n' +
   10. 'Yim8S8YwCgYIKoZIzj0EAwMDaAAwZQIxAK288mw/EkrRLTnDCgmXc/SINoyIJ7vmiI1Qhadj+Z4y\n' +
   11. '3maTD/HMsQmP3Wyr+mt/oAIwOWZbwmSNuJ5Q3KjVSaLtx9zRSX8XAbjIho9OjIgrqJqpisXRAL34\n' +
   12. 'VOKa5Vt8sycX\n' +
   13. '-----END CERTIFICATE-----';

   15. async function TestRcp() {
   16. const session = rcp.createSession();
   17. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   18. request.configuration = {
   19. security: {
   20. remoteValidation: {
   21. content: PEM_CA,
   22. }
   23. }
   24. }
   25. try {
   26. const response = await session.fetch(request);
   27. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   28. console.info(`response: ${JSON.stringify(response.toString())}`);
   29. } catch (err) {
   30. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   31. } finally {
   32. session.close();
   33. }
   34. }
   ```

### 4. 使用二进制指定证书内容

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { util } from '@kit.ArkTS';
   ```
2. 在remoteValidation中配置content，可以配置ArrayBuffer类型证书内容。

   ```
   1. const PEM_CA = '-----BEGIN CERTIFICATE-----\n' +
   2. 'MIICPzCCAcWgAwIBAgIQBVVWvPJepDU1w6QP1atFcjAKBggqhkjOPQQDAzBhMQswCQYDVQQGEwJV\n' +
   3. 'UzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYD\n' +
   4. 'VQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBHMzAeFw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAw\n' +
   5. 'MDBaMGExCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5k\n' +
   6. 'aWdpY2VydC5jb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEczMHYwEAYHKoZIzj0C\n' +
   7. 'AQYFK4EEACIDYgAE3afZu4q4C/sLfyHS8L6+c/MzXRq8NOrexpu80JX28MzQC7phW1FGfp4tn+6O\n' +
   8. 'YwwX7Adw9c+ELkCDnOg/QW07rdOkFFk2eJ0DQ+4QE2xy3q6Ip6FrtUPOZ9wj/wMco+I+o0IwQDAP\n' +
   9. 'BgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUs9tIpPmhxdiuNkHMEWNp\n' +
   10. 'Yim8S8YwCgYIKoZIzj0EAwMDaAAwZQIxAK288mw/EkrRLTnDCgmXc/SINoyIJ7vmiI1Qhadj+Z4y\n' +
   11. '3maTD/HMsQmP3Wyr+mt/oAIwOWZbwmSNuJ5Q3KjVSaLtx9zRSX8XAbjIho9OjIgrqJqpisXRAL34\n' +
   12. 'VOKa5Vt8sycX\n' +
   13. '-----END CERTIFICATE-----';

   15. async function TestRcp() {
   16. const session = rcp.createSession();
   17. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   18. const buffer = new ArrayBuffer(PEM_CA.length);
   19. util.TextEncoder.create('utf-8').encodeIntoUint8Array(PEM_CA, new Uint8Array(buffer));
   20. request.configuration = {
   21. security: {
   22. remoteValidation: {
   23. content: buffer,
   24. }
   25. }
   26. }
   27. try {
   28. const response = await session.fetch(request);
   29. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   30. console.info(`response: ${JSON.stringify(response.toString())}`);
   31. } catch (err) {
   32. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   33. } finally {
   34. session.close();
   35. }
   36. }
   ```

### 5. 使用文件指定证书内容

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 准备证书文件。在本例中，假设证书是example.pem，使用OpenSSL命令生成目标文件。

   ```
   1. openssl x509 -subject_hash -in ./example.pem
   ```

   命令输出如下。以第一行为目标文件名，以.0为文件扩展名，以其他内容为文件内容，将输出保存为dd8e9d41.0。如果您使用Windows系统，OpenSSL可能会等待用户输入才会退出，按Enter键即可。

   ```
   1. dd8e9d41
   2. -----BEGIN CERTIFICATE-----
   3. MIICPzCCAcWgAwIBAgIQBVVWvPJepDU1w6QP1atFcjAKBggqhkjOPQQDAzBhMQsw
   4. CQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cu
   5. ZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBHMzAe
   6. Fw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAwMDBaMGExCzAJBgNVBAYTAlVTMRUw
   7. EwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5jb20x
   8. IDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEczMHYwEAYHKoZIzj0CAQYF
   9. K4EEACIDYgAE3afZu4q4C/sLfyHS8L6+c/MzXRq8NOrexpu80JX28MzQC7phW1FG
   10. fp4tn+6OYwwX7Adw9c+ELkCDnOg/QW07rdOkFFk2eJ0DQ+4QE2xy3q6Ip6FrtUPO
   11. Z9wj/wMco+I+o0IwQDAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAd
   12. BgNVHQ4EFgQUs9tIpPmhxdiuNkHMEWNpYim8S8YwCgYIKoZIzj0EAwMDaAAwZQIx
   13. AK288mw/EkrRLTnDCgmXc/SINoyIJ7vmiI1Qhadj+Z4y3maTD/HMsQmP3Wyr+mt/
   14. oAIwOWZbwmSNuJ5Q3KjVSaLtx9zRSX8XAbjIho9OjIgrqJqpisXRAL34VOKa5Vt8
   15. sycX
   16. -----END CERTIFICATE-----
   ```
3. 在remoteValidation中通过filePath指定证书路径。关于文件路径，请参考[应用文件](app-file.md)。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. remoteValidation: {
   7. filePath: '/data/storage/el1/bundle/entry/resources/resfile/dd8e9d41.0', // 正式使用时，需替换为证书的沙箱路径。
   8. }
   9. }
   10. }
   11. try {
   12. const response = await session.fetch(request);
   13. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   14. console.info(`response: ${JSON.stringify(response.toString())}`);
   15. } catch (err) {
   16. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   17. } finally {
   18. session.close();
   19. }
   20. }
   ```

### 6. 使用文件目录指定证书。

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在remoteValidation中配置folderPath指定证书所在的沙箱目录。关于文件路径，请参考[应用文件](app-file.md)。目录中的证书文件格式和内容请参考示例5中的步骤2。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. remoteValidation: {
   7. folderPath: '/data/storage/el1/bundle/entry/resources/resfile/', // 正式使用时需替换成证书所在的沙箱目录。
   8. }
   9. }
   10. }
   11. try {
   12. const response = await session.fetch(request);
   13. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   14. console.info(`response: ${JSON.stringify(response.toString())}`);
   15. } catch (err) {
   16. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   17. } finally {
   18. session.close();
   19. }
   20. }
   ```

### 7. 自定义证书校验

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   2. import { networkSecurity } from '@kit.NetworkKit';
   ```
2. 校验证书的日期是否符合预期。

   ```
   1. function makeItTwoChar(s: string): string {
   2. if (s.length === 1) {
   3. return '0' + s;
   4. }
   5. return s;
   6. }
   7. function getASNDateString(): string {
   8. const date = new Date();
   9. let dateStr = date.getFullYear().toString().slice(2);
   10. dateStr += makeItTwoChar((date.getMonth() + 1).toString());
   11. dateStr += makeItTwoChar(date.getDate().toString());
   12. dateStr += makeItTwoChar(date.getHours().toString());
   13. dateStr += makeItTwoChar(date.getMinutes().toString());
   14. dateStr += makeItTwoChar(date.getSeconds().toString());
   15. return dateStr + 'Z';
   16. }
   ```
3. 自定义证书校验逻辑。

   ```
   1. async function ValidationRemoteServer(context: rcp.ValidationContext): Promise<boolean> {
   2. // 服务器未返回证书，校验失败
   3. let length = context.pemCerts.length;
   4. if (length <= 0) {
   5. return Promise.reject();
   6. }
   7. // 此示例中最后一个证书为根证书，开发中请根据实际情况调整
   8. const firstCaBlob: networkSecurity.CertBlob = {
   9. type: networkSecurity.CertType.CERT_TYPE_PEM,
   10. data: context.pemCerts[length - 1],
   11. }
   12. // 如果 certVerificationSync 的第二个参数未填写，则使用系统默认的 CA（"/etc/security/certificates"）进行验证
   13. if (networkSecurity.certVerificationSync(firstCaBlob) !== 0) {
   14. return Promise.reject();
   15. }
   16. // 此处可以添加所需的校验逻辑，如校验日期
   17. for (const x of context.x509Certs) {
   18. let dateStr = getASNDateString();
   19. try {
   20. x.checkValidityWithDate(dateStr);
   21. } catch (e) {
   22. return Promise.reject();
   23. }
   24. }

   26. // 校验成功
   27. return Promise.resolve(true);
   28. }
   ```
4. 将定义好的自定义证书校验器配置到configuration中，并利用fetch发起请求。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. remoteValidation: ValidationRemoteServer,
   7. }
   8. }
   9. try {
   10. const response = await session.fetch(request);
   11. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   12. console.info(`response: ${JSON.stringify(response.toString())}`);
   13. } catch (err) {
   14. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   15. } finally {
   16. session.close();
   17. }
   18. }
   ```

## 服务器校验客户端证书

### 1. PEM证书

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 本示例使用自签名证书，以便完整演示本地证书生成流程。请通过以下OpenSSL命令依次完成：生成私钥、创建证书签名请求（CSR）文件、基于CSR签发自签名证书、将私钥与证书合并为PEM格式的完整证书文件。

   注意：本示例使用自签名证书演示流程，实际生产环境中一般采用由可信证书颁发机构（CA）正式签发的证书。

   ```
   1. openssl genrsa -out cert.key 2048
   2. openssl req -new -key cert.key -out cert.csr
   3. openssl x509 -req -in cert.csr -out cert.crt -signkey cert.key -CAcreateserial -days 3650
   4. openssl x509 -in cert.crt -out cert.pem -outform PEM
   ```
3. 在certificate中通过filePath指定证书路径（也可以通过content指定证书内容），type配置PEM指定证书类型，key和keyPassword指定证书私钥和密码。关于文件路径，请参考[应用文件](app-file.md)。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. certificate: {
   7. filePath: '/data/storage/el1/bundle/entry/resources/resfile/cert.pem', // 可以使用content字段指定证书内容
   8. type: 'PEM',
   9. key: '/data/storage/el1/bundle/entry/resources/resfile/cert.key', // 这是证书私钥，在使用中请替换为实际的证书秘钥路径，可选
   10. keyPassword: 'keyPassword', // 证书私钥的密码，在使用中请替换为实际的证书秘钥密码，可选，本例中不生效
   11. }
   12. }
   13. };
   14. try {
   15. const response = await session.fetch(request);
   16. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   17. console.info(`response: ${JSON.stringify(response.toString())}`);
   18. } catch (err) {
   19. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   20. } finally {
   21. session.close();
   22. }
   23. }
   ```

### 2. DER证书

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在certificate中通过filePath指定证书内容（也可以通过content指定证书内容），type配置DER指定证书类型，key和keyPassword指定证书私钥和密码。使用openssl x509 -in cert.pem -outform der -out cert.der命令将上面例子中的pem文件转为der文件。关于文件路径，请参考[应用文件](app-file.md)。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. certificate: {
   7. filePath: '/data/storage/el1/bundle/entry/resources/resfile/cert.der', // 可以使用content字段指定证书内容
   8. type: 'DER',
   9. key: '/data/storage/el1/bundle/entry/resources/resfile/cert.key', // 这是证书私钥，在使用中请替换为实际的证书秘钥路径，可选
   10. keyPassword: 'keyPassword', // 证书私钥的密码，在使用中请替换为实际的证书秘钥密码，可选，本例中不生效
   11. }
   12. }
   13. };
   14. try {
   15. const response = await session.fetch(request);
   16. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   17. console.info(`response: ${JSON.stringify(response.toString())}`);
   18. } catch (err) {
   19. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   20. } finally {
   21. session.close();
   22. }
   23. }
   ```

### 3. P12证书

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在certificate中配置filePath指定证书路径（也可以配置content指定证书内容），type配置P12指定证书类型，keyPassword指定证书私钥的密码。使用openssl pkcs12 -export -out cert.p12 -inkey cert.key -in cert.pem命令将上面例子中的pem文件转为P12证书，设置密码“1234”。关于文件路径，请参考[应用文件](app-file.md)。

   ```
   1. async function TestRcp() {
   2. const session = rcp.createSession();
   3. const request = new rcp.Request('https://example.com'); // 请替换为实际的网址
   4. request.configuration = {
   5. security: {
   6. certificate: {
   7. filePath: '/data/storage/el1/bundle/entry/resources/resfile/cert.p12', // 可以使用content字段指定证书内容
   8. type: 'P12', // P12证书已包含私钥，不需要使用key指定私钥
   9. keyPassword: '1234', // 证书私钥的密码，在使用中请替换为实际的证书秘钥密码，可选
   10. }
   11. }
   12. };
   13. try {
   14. const response = await session.fetch(request);
   15. console.info(`response statusCode: ${JSON.stringify(response.statusCode)}`);
   16. console.info(`response: ${JSON.stringify(response.toString())}`);
   17. } catch (err) {
   18. console.error(`response error code is ${err.code}, error data is ${err.data}`);
   19. } finally {
   20. session.close();
   21. }
   22. }
   ```

## 证书锁定

证书锁定可以设置信任的证书的范围。通过比较证书公钥的SHA256哈希值的BASE64编码，限定可信任的证书。

* 可以通过以下OpenSSL命令获得证书公钥，其中，example.pem是服务器的PEM格式的证书，请替换为实际证书：

  ```
  1. openssl x509 -in example.pem -noout -pubkey | openssl asn1parse -noout -inform pem -out example.public.key
  ```
* 可以通过以下OpenSSL命令计算公钥的SHA256哈希值的BASE64编码，其中，example.public.key是上一步生成的证书的公钥：

  ```
  1. openssl dgst -sha256 -binary example.public.key | openssl enc -base64
  ```

1. 导入需要的模块。

   ```
   1. import { rcp } from '@kit.RemoteCommunicationKit';
   ```
2. 在certificatePinning中配置可信任的证书公钥的SHA256哈希值。

   ```
   1. const TEST_URL = 'https://example.com'; // 请替换成需要的URL

   3. const RIGHT_EXAMPLE_PUBLIC_KEY_SHA256_HASH = [
   4. 'iMMpIJdSf5VlClHaxZReyhaLxLsmZMMNAiA2pMR8/M4=', // 请替换成需要的字符串
   5. 'qBRjZmOmkSNJL0p70zek7odSIzqs/muR4Jk9xYyCP+E=', // 请替换成需要的字符串
   6. ];

   8. async function TestRcp() {
   9. const session = rcp.createSession();
   10. const request = new rcp.Request(TEST_URL);
   11. request.configuration = {
   12. security: {
   13. certificatePinning: [
   14. {
   15. kind: 'public-key',
   16. publicKeyHash: RIGHT_EXAMPLE_PUBLIC_KEY_SHA256_HASH[0],
   17. hashAlgorithm: 'SHA-256'
   18. },
   19. {
   20. kind: 'public-key',
   21. publicKeyHash: RIGHT_EXAMPLE_PUBLIC_KEY_SHA256_HASH[1],
   22. hashAlgorithm: 'SHA-256'
   23. },
   24. ]
   25. }
   26. };
   27. try {
   28. const response = await session.fetch(request);
   29. console.info('Test certificate pinning ' + response.statusCode);
   30. } catch (e) {
   31. console.error('Test certificate pinning ' + JSON.stringify(e));
   32. } finally {
   33. session.close();
   34. }
   35. }
   ```
