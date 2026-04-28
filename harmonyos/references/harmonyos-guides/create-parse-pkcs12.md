---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-parse-pkcs12
title: 证书PKCS12的创建和解析
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书PKCS12的创建和解析
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eacc4bb2b81bec57ad2b57500fafe6014e93c4dd6971c538b85e19cb89d671a1
---

从API 18开始，支持解析PKCS12证书。

从API 21开始，支持创建PKCS12证书。

PKCS12是一种用于存储和传输用户私钥、证书及其相关证书链的标准格式。该格式通过密码保护，将多个密码学对象打包为一个加密的容器文件，支持存储私钥、公钥证书、证书颁发机构证书以及其他相关的密码学数据。PKCS12广泛应用于数字证书的安全存储、跨平台传输和证书备份场景，是实现证书管理和PKI应用的重要标准之一。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createPkcs12](../harmonyos-references/js-apis-cert.md#certcreatepkcs1221)创建PKCS12文件。
3. 调用[cert.parsePkcs12](../harmonyos-references/js-apis-cert.md#certparsepkcs1218)解析PKCS12文件。

* 异步方法示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: number[] = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
13. // 证书二进制数据，需业务自行赋值。
14. let encodingBlob: cert.EncodingBlob = {
15. data: stringToUint8Array(certData),
16. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
17. encodingFormat: cert.EncodingFormat.FORMAT_PEM
18. };

20. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
21. try {
22. x509Cert = await cert.createX509Cert(encodingBlob);
23. } catch (err) {
24. console.error(`createX509Cert failed: errCode: ${err.code}, message: ${err.message}`);
25. }
26. return x509Cert;
27. }

29. let priKey = '-----BEGIN PRIVATE KEY-----\n' +
30. 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9kBV6Cqd3vSi5\n' +
31. 'RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnxObpDLyQw0Uu08tbn\n' +
32. 'EQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd0LS9k8Q57FRqOrQm\n' +
33. '7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfkDbuSKRD7UvVV/JZi\n' +
34. 'BklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLRnRPCVePV6xtoCmbN\n' +
35. 'A3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNxkDQtugv14qeDsFPS\n' +
36. 'IU8CtkCbAgMBAAECggEBAKbMmMlJhLCM5r+ZDJE/j55ujRLe6XwC1xP2keEeTdK9\n' +
37. '18aKLGR41BPsSH8JfAxh0m75lSvLjoVLRSQPUOZIfjXqUF/2hzzug5F2W8xKVovH\n' +
38. 'o1uqHlp71nVZPrJK7Q9H7TH/SyP4uxK6UvkKzt0j34WLHgeqV3t8qCMhB34zIAWG\n' +
39. 'BcAuKJNRZGvMvjK99OSOh0SyvGQ5Yb5vyj1/znx3gM4z4deYXxDSyCO0m5I16jmM\n' +
40. 'gBEUG0UDUp8Xr2xs/EkhhWYRT1bkDlYZ9IuCbH/vB1YJJFdaO2tDivDUF6IObvNt\n' +
41. 'GaVuLlA/rSOJmJFBetrm7n+O2vNJxvoQmBYDKm3+qYkCgYEA9p5C1ZY5XfwwOcqi\n' +
42. 'KQ+Asd2NWLG2blhsII5wB8uPhFapjV0S9xTabScUD35AfxHgctafpZeQk4x5niRP\n' +
43. 'BHq7hpitaDdYs6A/jhZ7fdVYKb1KRTDt1LXmcg0qVmi/ANNvjhqjvyZM+pEj8yxM\n' +
44. 'aOl4isbBfUbzSsEbda3LcHi6+w8CgYEAxMYtkl3gbXJcgbAEdW+nMMQGoFDLkgyu\n' +
45. 'n0ZYuRRrWLnnUzZUyqNBwQUaZpwxHaAqi0OAEGSRSZBKRHz9IA2iP9YzcaJ0WtpB\n' +
46. 'CPqwBZjrCaVEpHldo2pIdujysXgiXRUiE+VR9ViDmftoVbdL6kttGS08jBBDVIV/\n' +
47. 'uQgC/q29UbUCgYAJHirMaMRwNB24VUSPjhItAUrzh4Z+J+i/f2Sm9SC2PNoB7vn/\n' +
48. 'hpbYyEQWmo1Z5VhOBp9aaPMgcWYhsaf2O29pd4WZv8oYwgj3gN9J9LRQvr3bNwbk\n' +
49. 'AWGmv9Pb4/2D001hjJyXOZxI+0q/99hPXKpnPxfyQMhH8EHKpQVLgDsxgwKBgEiH\n' +
50. '+DJUci5Fkj2ngO08u7bo+rxLK85o6FEDYB7QnQT2eYMdqsGKzej1FZcvCZeu+x+c\n' +
51. 'QO9J8pfYHNgD7lXLULwRG6NOS29VtdU2en2FsVU72wJ5Tf+3ZICYOyUZcCk5afdF\n' +
52. 'dyFlgBTZK8s0pkH1jYBTQVcrg3X7Q2oTvu7bYcZlAoGAUwQI11mMR8oqfgWMoI/1\n' +
53. 'smOoq9qSMlutuWBjoPkbtJEGHEXAvjW1kgdBlPjUCwn6j+oIDLYu8DbfQRdiFQeP\n' +
54. 'rVCbbgOgayVpr+8Tv2DqB370GwBpOpuq0yiiN+c39Y0u03Yfve3icyl8+lN1t4h6\n' +
55. 'a20rj9HG4sb8tUIHPBv0dgY=\n' +
56. '-----END PRIVATE KEY-----\n';

58. let othercerts = '-----BEGIN CERTIFICATE-----\n' +
59. 'MIIDZTCCAk0CFAoqA7Irtoo7/3+sfOHy0s91pKkiMA0GCSqGSIb3DQEBCwUAMG8x\n' +
60. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
61. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
62. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NDM0WhcNMjYwODE0MTE1NDM0WjBv\n' +
63. 'MQswCQYDVQQGEwJFTjENMAsGA1UECAwEVEVTVDENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
64. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR4aWFuMQ0wCwYDVQQDDAR4aWFuMRMwEQYJ\n' +
65. 'KoZIhvcNAQkBFgR4aWFuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n' +
66. 'wk4aByV5nOw+zIh/1agaN7rQyk+NFuXlYSwINrONRZt8zePSxhxz6gMq0XAb8ld0\n' +
67. 'DFC5onGQEI4ED8iP3v7C7yHqIAybTmIy22RWWk8c6h9S40Azp/YHujTTRs2XMe9G\n' +
68. 'A/iKed9DwLclbv6+m+WPmIvgFFAJlebtFI6X0E/zBxs/TknR8tJ2uk2G/CGCBlo5\n' +
69. 'bbSz5RIPfEmz93rR7prMxQLOsvfdNewNlhe82jxMKfzGEPXYXUj+Xwp8ep+aaUTr\n' +
70. 'Kb6Thvx7+uOBxgMM1crREepTKJM/4bsOpb2yIXXcOqclUPAZBvtzIjgs/DdKtCZo\n' +
71. '0Jzr3gUbDJeE2xd+DcADxQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5RyDOMYJV\n' +
72. 'AsdBUihPvnnakKfAY9CYN9I1tR0b9DaboeL+bONeIKzXyFdDrAj6eZLKZLUblFlH\n' +
73. 'BZnbP4lNwfYjmNgp4j7cqSIFVwd2Y+6T29pK6T6XYRsFGOaSp7wFzXplfbP8Ou1b\n' +
74. 'o2zTZWWWHbiExuXot4RfQkgH3Zhk5zjJGWvaOksvEhJUaufkWAXbRY2KHmH64dDB\n' +
75. 'Bgp50CPObTuc2a+5PAi7W5nj1se2OqKvepoeYLl8pfF/GFRqrvcII9kCm0oyMqBx\n' +
76. '25R7aCNtSnENZnvRBspdYcX8zu6fR1qf0JmpLqLw5pPxJ2Puvq7g+33GWJ3Gq45f\n' +
77. 'ZcLXS+9LpW3a\n' +
78. '-----END CERTIFICATE-----\n';

80. let certData = '-----BEGIN CERTIFICATE-----\n' +
81. 'MIIDZzCCAk8CFCwQ5cxuFI+fsf/2fkG4gy8UT1gmMA0GCSqGSIb3DQEBCwUAMG8x\n' +
82. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
83. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
84. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NTQ1WhcNMjYwODE0MTE1NTQ1WjBx\n' +
85. 'MQswCQYDVQQGEwJHVDEPMA0GA1UECAwGaHVhd2VpMQ0wCwYDVQQHDAR4aWFuMQ8w\n' +
86. 'DQYDVQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzAR\n' +
87. 'BgkqhkiG9w0BCQEWBHhpYW4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n' +
88. 'AQC9kBV6Cqd3vSi5RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnx\n' +
89. 'ObpDLyQw0Uu08tbnEQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd\n' +
90. '0LS9k8Q57FRqOrQm7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfk\n' +
91. 'DbuSKRD7UvVV/JZiBklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLR\n' +
92. 'nRPCVePV6xtoCmbNA3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNx\n' +
93. 'kDQtugv14qeDsFPSIU8CtkCbAgMBAAEwDQYJKoZIhvcNAQELBQADggEBALuqlvql\n' +
94. 'q/5SVghmtdzVNlsif9JofSgJhmww3r8HblZ7zD7ALfR6JcxxbBJYdBIn6mf2eNx/\n' +
95. 'kTzwYs94D12PhyAP63AcDxS/4Sh7QhmnNIx2SGi/rbFdPm8cmkaFfwr5gQP+ouNB\n' +
96. '1e7vVyNpSjr4F8YcfjOHPofoCdWaOaBPrM760h711y/BTVMjuYkdzn0D1bHZIBc+\n' +
97. 'tljIMWXKsTwR6wCIpnFRJbEATTBwV843Q071d62jYueLgdS2wT39Syqb3ao3aHAS\n' +
98. 'ZI8k9GgNNKD4qBAZUbQVCs6diTBbeUMaqJ2N+tcQfmGfnNZK+/olEF6Ue/H0LZzY\n' +
99. 'nZSOvPxc0c2O34k=\n' +
100. '-----END CERTIFICATE-----\n';

102. async function doTestCreatePkcs12() {
103. const caCert = await createX509Cert(othercerts);
104. const x509Cert = await createX509Cert(certData);

106. let data: cert.Pkcs12Data = {
107. privateKey: priKey,
108. cert: x509Cert,
109. otherCerts: [caCert]
110. }

112. let keyParam: cert.PbesParams = {
113. saltLen: 16,
114. iterations: 2048,
115. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_192_CBC
116. }

118. let certParam: cert.PbesParams = {
119. saltLen: 16,
120. iterations: 2048,
121. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_256_CBC
122. }

124. let config: cert.Pkcs12CreationConfig = {
125. password: '123456',
126. keyEncParams: keyParam,
127. encryptCert: true,
128. certEncParams: certParam,
129. macSaltLen: 16,
130. macIterations: 2048,
131. macDigestAlgorithm: cert.Pkcs12MacDigestAlgorithm.SHA384
132. }

134. try {
135. let p12 = await cert.createPkcs12(data, config);
136. console.info(`createPkcs12 result: success, p12 = ` + p12);
137. let out: cert.Pkcs12Data = await cert.parsePkcs12(p12, '123456');
138. console.info(`parsePKCS12 result: success.`);
139. if (out.privateKey) {
140. console.info(`privateKey:` + out.privateKey.toString());
141. }
142. if (out.cert) {
143. console.info(`cert:` + out.cert.toString());
144. }
145. if (out.otherCerts && Array.isArray(out.otherCerts)) {
146. console.info(`otherCerts counts: `, out.otherCerts.length);
147. out.otherCerts.forEach((cert, idx) => {
148. console.info(`otherCerts[${idx}]:\n${cert.toString()}`);
149. });
150. } else {
151. console.info(`otherCerts is empty or not an array.`);
152. }
153. } catch (err) {
154. console.error(`doTestCreatePkcs12 failed: errCode: ${err.code}, message: ${err.message}`);
155. }
156. }
```

[CreateParsePkcs12Async.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateParsePkcs12Async.ets#L16-L175)

* 同步方法示例：

```
1. import { cert } from '@kit.DeviceCertificateKit';

3. // string转Uint8Array。
4. function stringToUint8Array(str: string): Uint8Array {
5. let arr: number[] = [];
6. for (let i = 0, j = str.length; i < j; i++) {
7. arr.push(str.charCodeAt(i));
8. }
9. return new Uint8Array(arr);
10. }

12. async function createX509Cert(certData: string): Promise<cert.X509Cert> {
13. // 证书二进制数据，需业务自行赋值。
14. let encodingBlob: cert.EncodingBlob = {
15. data: stringToUint8Array(certData),
16. // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
17. encodingFormat: cert.EncodingFormat.FORMAT_PEM
18. };

20. let x509Cert: cert.X509Cert = {} as cert.X509Cert;
21. try {
22. x509Cert = await cert.createX509Cert(encodingBlob);
23. } catch (err) {
24. console.error(`doTestCreatePkcs12 failed: errCode: ${err.code}, message: ${err.message}`);
25. }
26. return x509Cert;
27. }

29. let priKey = '-----BEGIN PRIVATE KEY-----\n' +
30. 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9kBV6Cqd3vSi5\n' +
31. 'RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnxObpDLyQw0Uu08tbn\n' +
32. 'EQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd0LS9k8Q57FRqOrQm\n' +
33. '7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfkDbuSKRD7UvVV/JZi\n' +
34. 'BklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLRnRPCVePV6xtoCmbN\n' +
35. 'A3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNxkDQtugv14qeDsFPS\n' +
36. 'IU8CtkCbAgMBAAECggEBAKbMmMlJhLCM5r+ZDJE/j55ujRLe6XwC1xP2keEeTdK9\n' +
37. '18aKLGR41BPsSH8JfAxh0m75lSvLjoVLRSQPUOZIfjXqUF/2hzzug5F2W8xKVovH\n' +
38. 'o1uqHlp71nVZPrJK7Q9H7TH/SyP4uxK6UvkKzt0j34WLHgeqV3t8qCMhB34zIAWG\n' +
39. 'BcAuKJNRZGvMvjK99OSOh0SyvGQ5Yb5vyj1/znx3gM4z4deYXxDSyCO0m5I16jmM\n' +
40. 'gBEUG0UDUp8Xr2xs/EkhhWYRT1bkDlYZ9IuCbH/vB1YJJFdaO2tDivDUF6IObvNt\n' +
41. 'GaVuLlA/rSOJmJFBetrm7n+O2vNJxvoQmBYDKm3+qYkCgYEA9p5C1ZY5XfwwOcqi\n' +
42. 'KQ+Asd2NWLG2blhsII5wB8uPhFapjV0S9xTabScUD35AfxHgctafpZeQk4x5niRP\n' +
43. 'BHq7hpitaDdYs6A/jhZ7fdVYKb1KRTDt1LXmcg0qVmi/ANNvjhqjvyZM+pEj8yxM\n' +
44. 'aOl4isbBfUbzSsEbda3LcHi6+w8CgYEAxMYtkl3gbXJcgbAEdW+nMMQGoFDLkgyu\n' +
45. 'n0ZYuRRrWLnnUzZUyqNBwQUaZpwxHaAqi0OAEGSRSZBKRHz9IA2iP9YzcaJ0WtpB\n' +
46. 'CPqwBZjrCaVEpHldo2pIdujysXgiXRUiE+VR9ViDmftoVbdL6kttGS08jBBDVIV/\n' +
47. 'uQgC/q29UbUCgYAJHirMaMRwNB24VUSPjhItAUrzh4Z+J+i/f2Sm9SC2PNoB7vn/\n' +
48. 'hpbYyEQWmo1Z5VhOBp9aaPMgcWYhsaf2O29pd4WZv8oYwgj3gN9J9LRQvr3bNwbk\n' +
49. 'AWGmv9Pb4/2D001hjJyXOZxI+0q/99hPXKpnPxfyQMhH8EHKpQVLgDsxgwKBgEiH\n' +
50. '+DJUci5Fkj2ngO08u7bo+rxLK85o6FEDYB7QnQT2eYMdqsGKzej1FZcvCZeu+x+c\n' +
51. 'QO9J8pfYHNgD7lXLULwRG6NOS29VtdU2en2FsVU72wJ5Tf+3ZICYOyUZcCk5afdF\n' +
52. 'dyFlgBTZK8s0pkH1jYBTQVcrg3X7Q2oTvu7bYcZlAoGAUwQI11mMR8oqfgWMoI/1\n' +
53. 'smOoq9qSMlutuWBjoPkbtJEGHEXAvjW1kgdBlPjUCwn6j+oIDLYu8DbfQRdiFQeP\n' +
54. 'rVCbbgOgayVpr+8Tv2DqB370GwBpOpuq0yiiN+c39Y0u03Yfve3icyl8+lN1t4h6\n' +
55. 'a20rj9HG4sb8tUIHPBv0dgY=\n' +
56. '-----END PRIVATE KEY-----\n';

58. let othercerts = '-----BEGIN CERTIFICATE-----\n' +
59. 'MIIDZTCCAk0CFAoqA7Irtoo7/3+sfOHy0s91pKkiMA0GCSqGSIb3DQEBCwUAMG8x\n' +
60. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
61. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
62. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NDM0WhcNMjYwODE0MTE1NDM0WjBv\n' +
63. 'MQswCQYDVQQGEwJFTjENMAsGA1UECAwEVEVTVDENMAsGA1UEBwwEeGlhbjEPMA0G\n' +
64. 'A1UECgwGaHVhd2VpMQ0wCwYDVQQLDAR4aWFuMQ0wCwYDVQQDDAR4aWFuMRMwEQYJ\n' +
65. 'KoZIhvcNAQkBFgR4aWFuMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\n' +
66. 'wk4aByV5nOw+zIh/1agaN7rQyk+NFuXlYSwINrONRZt8zePSxhxz6gMq0XAb8ld0\n' +
67. 'DFC5onGQEI4ED8iP3v7C7yHqIAybTmIy22RWWk8c6h9S40Azp/YHujTTRs2XMe9G\n' +
68. 'A/iKed9DwLclbv6+m+WPmIvgFFAJlebtFI6X0E/zBxs/TknR8tJ2uk2G/CGCBlo5\n' +
69. 'bbSz5RIPfEmz93rR7prMxQLOsvfdNewNlhe82jxMKfzGEPXYXUj+Xwp8ep+aaUTr\n' +
70. 'Kb6Thvx7+uOBxgMM1crREepTKJM/4bsOpb2yIXXcOqclUPAZBvtzIjgs/DdKtCZo\n' +
71. '0Jzr3gUbDJeE2xd+DcADxQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQA5RyDOMYJV\n' +
72. 'AsdBUihPvnnakKfAY9CYN9I1tR0b9DaboeL+bONeIKzXyFdDrAj6eZLKZLUblFlH\n' +
73. 'BZnbP4lNwfYjmNgp4j7cqSIFVwd2Y+6T29pK6T6XYRsFGOaSp7wFzXplfbP8Ou1b\n' +
74. 'o2zTZWWWHbiExuXot4RfQkgH3Zhk5zjJGWvaOksvEhJUaufkWAXbRY2KHmH64dDB\n' +
75. 'Bgp50CPObTuc2a+5PAi7W5nj1se2OqKvepoeYLl8pfF/GFRqrvcII9kCm0oyMqBx\n' +
76. '25R7aCNtSnENZnvRBspdYcX8zu6fR1qf0JmpLqLw5pPxJ2Puvq7g+33GWJ3Gq45f\n' +
77. 'ZcLXS+9LpW3a\n' +
78. '-----END CERTIFICATE-----\n';

80. let certData = '-----BEGIN CERTIFICATE-----\n' +
81. 'MIIDZzCCAk8CFCwQ5cxuFI+fsf/2fkG4gy8UT1gmMA0GCSqGSIb3DQEBCwUAMG8x\n' +
82. 'CzAJBgNVBAYTAkVOMQ0wCwYDVQQIDARURVNUMQ0wCwYDVQQHDAR4aWFuMQ8wDQYD\n' +
83. 'VQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzARBgkq\n' +
84. 'hkiG9w0BCQEWBHhpYW4wHhcNMjUwODE0MTE1NTQ1WhcNMjYwODE0MTE1NTQ1WjBx\n' +
85. 'MQswCQYDVQQGEwJHVDEPMA0GA1UECAwGaHVhd2VpMQ0wCwYDVQQHDAR4aWFuMQ8w\n' +
86. 'DQYDVQQKDAZodWF3ZWkxDTALBgNVBAsMBHhpYW4xDTALBgNVBAMMBHhpYW4xEzAR\n' +
87. 'BgkqhkiG9w0BCQEWBHhpYW4wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB\n' +
88. 'AQC9kBV6Cqd3vSi5RuRAWjXEvsfD20ekCYyeJvnnSrHwnKodbF8VWFSv4sqYzMnx\n' +
89. 'ObpDLyQw0Uu08tbnEQvxv0lOwnWkZR+Oc3M9Ow1uhDkm3eFbY5858mAmtY7Sqzhd\n' +
90. '0LS9k8Q57FRqOrQm7ngHb0O+yjCIn/zmjyEuw51/cPDTM4h3P3di9nhbIg+UOMfk\n' +
91. 'DbuSKRD7UvVV/JZiBklF5ZrjFYgzYnWKv7N7XkYMGkaOx8+tue24eK06SapQWDLR\n' +
92. 'nRPCVePV6xtoCmbNA3ib/Uvr0qvRwPDCzGGOW9JvQdrI6Z/GD9nt5hqHB15iJVNx\n' +
93. 'kDQtugv14qeDsFPSIU8CtkCbAgMBAAEwDQYJKoZIhvcNAQELBQADggEBALuqlvql\n' +
94. 'q/5SVghmtdzVNlsif9JofSgJhmww3r8HblZ7zD7ALfR6JcxxbBJYdBIn6mf2eNx/\n' +
95. 'kTzwYs94D12PhyAP63AcDxS/4Sh7QhmnNIx2SGi/rbFdPm8cmkaFfwr5gQP+ouNB\n' +
96. '1e7vVyNpSjr4F8YcfjOHPofoCdWaOaBPrM760h711y/BTVMjuYkdzn0D1bHZIBc+\n' +
97. 'tljIMWXKsTwR6wCIpnFRJbEATTBwV843Q071d62jYueLgdS2wT39Syqb3ao3aHAS\n' +
98. 'ZI8k9GgNNKD4qBAZUbQVCs6diTBbeUMaqJ2N+tcQfmGfnNZK+/olEF6Ue/H0LZzY\n' +
99. 'nZSOvPxc0c2O34k=\n' +
100. '-----END CERTIFICATE-----\n';

102. async function doTestCreatePkcs12Sync() {
103. const caCert = await createX509Cert(othercerts);
104. const x509Cert = await createX509Cert(certData);

106. let data: cert.Pkcs12Data = {
107. privateKey: priKey,
108. cert: x509Cert,
109. otherCerts: [caCert]
110. }

112. let keyParam: cert.PbesParams = {
113. saltLen: 16,
114. iterations: 2048,
115. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_192_CBC
116. }

118. let certParam: cert.PbesParams = {
119. saltLen: 16,
120. iterations: 2048,
121. encryptionAlgorithm: cert.PbesEncryptionAlgorithm.AES_256_CBC
122. }

124. let config: cert.Pkcs12CreationConfig = {
125. password: '123456',
126. keyEncParams: keyParam,
127. encryptCert: true,
128. certEncParams: certParam,
129. macSaltLen: 16,
130. macIterations: 2048,
131. macDigestAlgorithm: cert.Pkcs12MacDigestAlgorithm.SHA384
132. }

134. try {
135. let p12 = cert.createPkcs12Sync(data, config);
136. console.info(`createPkcs12Sync result: success, p12 = ` + p12);
137. let conf: cert.Pkcs12ParsingConfig = {
138. password: '123456',
139. needsCert: true,
140. needsPrivateKey: true,
141. privateKeyFormat: cert.EncodingBaseFormat.PEM,
142. needsOtherCerts: true,
143. };
144. let out: cert.Pkcs12Data = cert.parsePkcs12(p12, conf);
145. console.info(`parsePKCS12 result: success.`);
146. if (out.privateKey) {
147. console.info(`privateKey:` + out.privateKey.toString());
148. }
149. if (out.cert) {
150. console.info(`cert:` + out.cert.toString());
151. }
152. if (out.otherCerts && Array.isArray(out.otherCerts)) {
153. console.info(`otherCerts counts:`, out.otherCerts.length);
154. out.otherCerts.forEach((cert, idx) => {
155. console.info(`otherCerts[${idx}]:\n${cert.toString()}`);
156. });
157. } else {
158. console.info(`otherCerts is empty or not an array.`);
159. }
160. } catch (err) {
161. console.error(`doTestCreatePkcs12 failed: errCode: ${err.code}, message: ${err.message}`);
162. }
163. }
```

[CreateParsePkcs12Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateParsePkcs12Sync.ets#L16-L182)
