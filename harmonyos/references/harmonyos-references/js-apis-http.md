---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http
title: @ohos.net.http (数据请求)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.http (数据请求)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:17f4f0ec099fe7567e2bc5420fb73c96ca28e14d208a0262aff77560841683aa
---

本模块提供HTTP数据请求能力。应用可以通过HTTP发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、TRACE、CONNECT方法。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { http } from '@kit.NetworkKit';
```

## 完整示例

PhonePC/2in1TabletTVWearable

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. // 引入包名
2. import { http } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';

6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. // 每一个httpRequest对应一个HTTP请求任务，不可复用。
8. let httpRequest = http.createHttp();
9. // 用于订阅HTTP响应头，此接口会比request请求先返回。可以根据业务需要订阅此消息。
10. // 从API 8开始，使用on('headersReceive', Callback)替代on('headerReceive', AsyncCallback)。 8+
11. httpRequest.on('headersReceive', (header: Object) => {
12. console.info('header: ' + JSON.stringify(header));
13. });

15. httpRequest.request(// 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定。
16. "EXAMPLE_URL",
17. {
18. method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
19. // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
20. extraData: 'data to send',
21. expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
22. usingCache: true, // 可选，默认为true。
23. priority: 1, // 可选，默认为1。
24. // 开发者根据自身业务需要添加header字段，且header字段不支持传入map对象。
25. header: { 'Accept' : 'application/json' },
26. readTimeout: 60000, // 可选，默认为60000ms。
27. connectTimeout: 60000, // 可选，默认为60000ms。
28. usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
29. usingProxy: false, // 可选，默认不使用网络代理，自API 10开始支持该属性。
30. caPath: '/path/to/cacert.pem', // 可选，默认使用系统预设CA证书，自API 10开始支持该属性。
31. caData: '-----BEGIN CERTIFICATE-----\n' +
32. 'MIIDaTCCAlGgAwIBAgIICN287lmB2cMwDQYJKoZIhvcNAQELBQAwgYoxCzAJBgNV\n' +
33. 'BAYTAkNOMRMwEQYDVQQDDApleGFtcGxlLmNuMRAwDgYDVQQKDAdDb21wYW55MREw\n' +
34. 'DwYDVQQLDAhEaXZpc2lvbjEOMAwGA1UECAwFQW5IdWkxDjAMBgNVBAcMBUhlRmVp\n' +
35. 'MSEwHwYJKoZIhvcNAQkBFhJleGFtcGxlQGV4YW1wbGUuY24wHhcNMjUwNDEzMDAy\n' +
36. 'MjQxWhcNMjgwNDEzMDAyMjQxWjBeMQswCQYDVQQGEwJDTjESMBAGA1UEAwwJMTI3\n' +
37. 'LjAuMC4xMQkwBwYDVQQKDAAxCTAHBgNVBAsMADEJMAcGA1UECAwAMQkwBwYDVQQH\n' +
38. 'DAAxDzANBgkqhkiG9w0BCQEWADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\n' +
39. 'ggEBANN/JrQC8dy7sxUk+TDJlGlq4h8lajdqSASkFbWVBadU4eMCbRrKejXuFX/n\n' +
40. 'Yu4J3wkgni0NKRejdWu/M+LLibQEIF9RUGNR/OgdlR4AKr8ZxmG44+7Ps2aiDcOy\n' +
41. 'Z95UcxYj59ctfFk63cacbBi19aq200spjl/H0jTVsQ2/JvwMVEH62WbyjIJ3KXgq\n' +
42. 'yyjf75rKbR9CdVdGk+OoR4S4c6nY5cTZP6T7iCupYR6MpKEtIR2bbams/N5GxQEh\n' +
43. '9+7YxswTQn4EkVhi+UOFZolYLhtIdoLThmStN+WiSL5VDvchAkTUmwUBTGV21WnH\n' +
44. 'qo6J1t7XtwUpAZF6OuWl85R8D50CAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAqjKq\n' +
45. 'gwR+4B6bwdAOZ6k0cutLqxvVgBaktX28omuYtoiYagM0zfB8/8WijXL8jT1VLEFx\n' +
46. 'wPaojwegqYWANfQkPd7A6rjsabgOH7oYBCDoCH52cjzGlJunC0BL6w5g3z6MCOB4\n' +
47. 'Ciz8rnYMvYqQJiMqrO7Po9onoFBHiRQGO4Wva3O8ErEmd2dKvXb3vN02P3T7CtwM\n' +
48. 'Z6D0rtZbzdsSOQfGcX08WFIfvfpz6tdU/X/6VqKrt5oiaNQH7ded6gJ3C6RM/Q/x\n' +
49. 'I2j/hSKy0yU7FoCFSOnlhxbm3TlbIvtjZKQ9ymK4x7iE0VKqExUAA6Z8qsIUBUt4\n' +
50. 'aqNDeZWXFBqrSujLJA==\n' +
51. '-----END CERTIFICATE-----', // 可选，默认使用系统预设CA证书，自API 20开始支持该属性。
52. clientCert: { // 可选，默认不使用客户端证书，自API 11开始支持该属性。
53. certPath: '/path/to/client.pem', // 默认不使用客户端证书，自API 11开始支持该属性。
54. keyPath: '/path/to/client.key', // 若证书包含Key信息，传入空字符串，自API 11开始支持该属性。
55. certType: http.CertType.PEM, // 可选，默认使用PEM，自API 11开始支持该属性。
56. keyPassword: "passwordToKey" // 可选，输入key文件的密码，自API 11开始支持该属性。
57. },
58. certificatePinning: [ // 可选，支持证书锁定配置信息的动态设置，自API 12开始支持该属性。
59. {
60. publicKeyHash: 'Pin1', // 由应用传入的证书PIN码，自API 12开始支持该属性。
61. hashAlgorithm: 'SHA-256' // 加密算法，当前仅支持SHA-256，自API 12开始支持该属性。
62. }, {
63. publicKeyHash: 'Pin2', // 由应用传入的证书PIN码，自API 12开始支持该属性。
64. hashAlgorithm: 'SHA-256' // 加密算法，当前仅支持SHA-256，自API 12开始支持该属性。
65. }
66. ],
67. multiFormDataList: [ // 可选，仅当Header中，'content-Type'为'multipart/form-data'时生效，自API 11开始支持该属性。
68. {
69. name: "Part1", // 数据名，自API 11开始支持该属性。
70. contentType: 'text/plain', // 数据类型，自API 11开始支持该属性。
71. data: 'Example data', // 可选，数据内容，自API 11开始支持该属性。
72. remoteFileName: 'example.txt' // 可选，自API 11开始支持该属性。
73. }, {
74. name: "Part2", // 数据名，自API 11开始支持该属性。
75. contentType: 'text/plain', // 数据类型，自API 11开始支持该属性。
76. // data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.txt
77. filePath: `${context.filesDir}/fileName.txt`, // 可选，传入文件路径，自API 11开始支持该属性。
78. remoteFileName: 'fileName.txt' // 可选，自API 11开始支持该属性。
79. }
80. ],
81. addressFamily: http.AddressFamily.DEFAULT, // 可选，系统默认选择目标域名的IPv4地址或IPv6地址，自API 15开始支持该属性。
82. customMethod: 'GET', // 可选，自API 23开始支持该属性。
83. maxRedirects: 30, // 可选，默认值是30次，自API 23开始支持该属性。
84. sniHostName: "www.example.com" // 可选，自API 23开始支持该属性。
85. },
86. (err: BusinessError, data: http.HttpResponse) => {
87. if (!err) {
88. // data.result为HTTP响应内容，可根据业务需要进行解析。
89. console.info('Result:' + JSON.stringify(data.result));
90. console.info('code:' + JSON.stringify(data.responseCode));
91. console.info('type:' + JSON.stringify(data.resultType));
92. // data.header为HTTP响应头，可根据业务需要进行解析。
93. console.info('header:' + JSON.stringify(data.header));
94. console.info('cookies:' + JSON.stringify(data.cookies)); // 自API version 8开始支持cookie。
95. // 取消订阅HTTP响应头事件。
96. httpRequest.off('headersReceive');
97. // 当该请求使用完毕时，开发者务必调用destroy方法释放资源，避免出现内存泄漏。
98. httpRequest.destroy();
99. } else {
100. console.error('error:' + JSON.stringify(err));
101. // 取消订阅HTTP响应头事件。
102. httpRequest.off('headersReceive');
103. // 当该请求使用完毕时，开发者务必调用destroy方法释放资源，避免出现内存泄漏。
104. httpRequest.destroy();
105. }
106. });
```

说明

console.info()输出的数据中包含换行符会导致数据出现截断现象。

自API 12开始支持接收经过brotli算法压缩的HTTP响应。

## http.createHttp

PhonePC/2in1TabletTVWearable

createHttp(): HttpRequest

创建一个HTTP请求，里面包括发起请求、中断请求、订阅/取消订阅HTTP Response Header事件。当发起多个HTTP请求时，需为每个HTTP请求创建对应HttpRequest对象。每一个HttpRequest对象对应一个HTTP请求。

说明

当该请求使用完毕时，需调用destroy方法释放资源，否则会出现内存泄露问题。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HttpRequest | 返回一个HttpRequest对象，里面包括request、requestInStream、destroy、on和off方法。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
```

## HttpRequest

PhonePC/2in1TabletTVWearable

HTTP请求任务。在调用HttpRequest的方法前，需要先通过[createHttp()](js-apis-http.md#httpcreatehttp)创建一个任务。

### request

PhonePC/2in1TabletTVWearable

request(url: string, callback: AsyncCallback<HttpResponse>): void

根据URL地址，发起HTTP网络请求，使用callback方式作为异步方法。

说明

(1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据，则需主动在[HttpRequestOptions](js-apis-http.md#httprequestoptions)的maxLimit中进行设置，或者使用[requestInStream](js-apis-http.md#requestinstream10)接口发起流式请求。自API version 23开始，本接口支持的最大接收数据量为50MB，API version 23之前仍为5MB，超过5MB会接收失败。

(2) 如需传入cookies，请开发者自行在参数options中添加。

(3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 发起网络请求的URL地址。 |
| callback | AsyncCallback<[HttpResponse](js-apis-http.md#httpresponse)> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
5. if (!err) {
6. console.info('Result:' + data.result);
7. console.info('code:' + data.responseCode);
8. console.info('type:' + JSON.stringify(data.resultType));
9. console.info('header:' + JSON.stringify(data.header));
10. console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
11. } else {
12. console.error('error:' + JSON.stringify(err));
13. }
14. });
```

### request

PhonePC/2in1TabletTVWearable

request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>):void

根据URL地址和相关配置项，发起HTTP网络请求，使用callback方式作为异步方法。

说明

(1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据，则需主动在[HttpRequestOptions](js-apis-http.md#httprequestoptions)的maxLimit中进行设置，或者使用[requestInStream](js-apis-http.md#requestinstream10)接口发起流式请求。自API version 23开始，本接口支持的最大接收数据量为50MB，API version 23之前仍为5MB，超过5MB会接收失败。

(2) 如需传入cookies，请开发者自行在参数options中添加。

(3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 发起网络请求的URL地址。 |
| options | HttpRequestOptions | 是 | 参考[HttpRequestOptions](js-apis-http.md#httprequestoptions)。 |
| callback | AsyncCallback<[HttpResponse](js-apis-http.md#httpresponse)> | 是 | 回调函数。当请求成功时，回调内容是[HttpResponse](js-apis-http.md#httpresponse) ，请求失败时为undefined。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. class Header {
4. public contentType: string;

6. constructor(contentType: string) {
7. this.contentType = contentType;
8. }
9. }

11. let httpRequest = http.createHttp();
12. let options: http.HttpRequestOptions = {
13. method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
14. // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
15. extraData: 'data to send',
16. expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
17. usingCache: true, // 可选，默认为true。
18. priority: 1, // 可选，默认为1。
19. // 开发者根据自身业务需要添加header字段。
20. header: new Header('application/json'),
21. readTimeout: 60000, // 可选，默认为60000ms。
22. connectTimeout: 60000, // 可选，默认为60000ms。
23. usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
24. usingProxy: false, // 可选，默认不使用网络代理，自API 10开始支持该属性。
25. };

27. httpRequest.request("EXAMPLE_URL", options, (err: Error, data: http.HttpResponse) => {
28. if (!err) {
29. console.info('Result:' + data.result);
30. console.info('code:' + data.responseCode);
31. console.info('type:' + JSON.stringify(data.resultType));
32. console.info('header:' + JSON.stringify(data.header));
33. console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
34. } else {
35. console.error('error:' + JSON.stringify(err));
36. }
37. });
```

### request

PhonePC/2in1TabletTVWearable

request(url: string, options? : HttpRequestOptions): Promise<HttpResponse>

根据URL地址，发起HTTP网络请求，使用Promise方式作为异步方法。

说明

(1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据，则需主动在[HttpRequestOptions](js-apis-http.md#httprequestoptions)的maxLimit中进行设置，或者使用[requestInStream](js-apis-http.md#requestinstream10)接口发起流式请求。自API version 23开始，本接口支持的最大接收数据量为50MB，API version 23之前仍为5MB，超过5MB会接收失败。

(2) 如需传入cookies，请开发者自行在参数options中添加。

(3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 发起网络请求的URL地址。 |
| options | HttpRequestOptions | 否 | 参考[HttpRequestOptions](js-apis-http.md#httprequestoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HttpResponse](js-apis-http.md#httpresponse)> | 以Promise形式返回发起请求的结果。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. class Header {
4. public contentType: string;

6. constructor(contentType: string) {
7. this.contentType = contentType;
8. }
9. }

11. let httpRequest = http.createHttp();
12. let promise = httpRequest.request("EXAMPLE_URL", {
13. method: http.RequestMethod.GET,
14. connectTimeout: 60000,
15. readTimeout: 60000,
16. header: new Header('application/json')
17. });
18. promise.then((data:http.HttpResponse) => {
19. console.info('Result:' + data.result);
20. console.info('code:' + data.responseCode);
21. console.info('type:' + JSON.stringify(data.resultType));
22. console.info('header:' + JSON.stringify(data.header));
23. console.info('cookies:' + data.cookies); // 自API version 8开始支持cookie。
24. console.info('header.content-Type:' + data.header);
25. console.info('header.Status-Line:' + data.header);
26. }).catch((err:Error) => {
27. console.error('error:' + JSON.stringify(err));
28. });
```

### destroy

PhonePC/2in1TabletTVWearable

destroy(): void

终止HTTP请求任务，同时释放系统资源。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. let httpRequest = http.createHttp();

4. httpRequest.destroy();
```

### requestInStream10+

PhonePC/2in1TabletTVWearable

requestInStream(url: string, callback: AsyncCallback<number>): void

根据URL地址，发起HTTP网络请求并返回流式响应，使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 发起网络请求的URL地址。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当请求成功，err为undefined，返回HTTP请求响应错误码；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let httpRequest = http.createHttp();
5. httpRequest.requestInStream("EXAMPLE_URL", (err: BusinessError, data: number) => {
6. if (!err) {
7. console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
8. } else {
9. console.error("requestInStream ERROR : err = " + JSON.stringify(err));
10. }
11. })
```

### requestInStream10+

PhonePC/2in1TabletTVWearable

requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void

根据URL地址和相关配置项，发起HTTP网络请求并返回流式响应，使用callback方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 发起网络请求的URL地址。 |
| options | HttpRequestOptions | 是 | 参考[HttpRequestOptions](js-apis-http.md#httprequestoptions)。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当请求成功，err为undefined，返回[HTTP请求响应错误码](js-apis-http.md#responsecode)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Header {
5. public contentType: string;

7. constructor(contentType: string) {
8. this.contentType = contentType;
9. }
10. }

12. let httpRequest = http.createHttp();
13. let options: http.HttpRequestOptions = {
14. method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
15. // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
16. extraData: 'data to send',
17. expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
18. usingCache: true, // 可选，默认为true。
19. priority: 1, // 可选，默认为1。
20. // 开发者根据自身业务需要添加header字段。
21. header: new Header('application/json'),
22. readTimeout: 60000, // 可选，默认为60000ms。
23. connectTimeout: 60000, // 可选，默认为60000ms。
24. usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
25. usingProxy: false, // 可选，默认不使用网络代理，自API 10开始支持该属性。
26. };
27. httpRequest.requestInStream("EXAMPLE_URL", options, (err: BusinessError<void> , data: number) => {
28. if (!err) {
29. console.info("requestInStream OK! ResponseCode is " + JSON.stringify(data));
30. } else {
31. console.error("requestInStream ERROR : err = " + JSON.stringify(err));
32. }
33. })
```

### requestInStream10+

PhonePC/2in1TabletTVWearable

requestInStream(url: string, options? : HttpRequestOptions): Promise<number>

根据URL地址，发起HTTP网络请求并返回流式响应，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 发起网络请求的URL地址。 |
| options | HttpRequestOptions | 否 | 参考[HttpRequestOptions](js-apis-http.md#httprequestoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回[发起请求的结果](js-apis-http.md#responsecode)。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300001 | Unsupported protocol. |
| 2300003 | Invalid URL format or missing URL. |
| 2300005 | Failed to resolve the proxy name. |
| 2300006 | Failed to resolve the host name. |
| 2300007 | Failed to connect to the server. |
| 2300008 | Invalid server response. |
| 2300009 | Access to the remote resource denied. |
| 2300016 | Error in the HTTP2 framing layer. |
| 2300018 | Transferred a partial file. |
| 2300023 | Failed to write the received data to the disk or application. |
| 2300025 | Upload failed. |
| 2300026 | Failed to open or read local data from the file or application. |
| 2300027 | Out of memory. |
| 2300028 | Operation timeout. |
| 2300047 | The number of redirections reaches the maximum allowed. |
| 2300052 | The server returned nothing (no header or data). |
| 2300055 | Failed to send data to the peer. |
| 2300056 | Failed to receive data from the peer. |
| 2300058 | Local SSL certificate error. |
| 2300059 | The specified SSL cipher cannot be used. |
| 2300060 | Invalid SSL peer certificate or SSH remote key. |
| 2300061 | Invalid HTTP encoding format. |
| 2300063 | Maximum file size exceeded. |
| 2300070 | Remote disk full. |
| 2300073 | Remote file already exists. |
| 2300077 | The SSL CA certificate does not exist or is inaccessible. |
| 2300078 | Remote file not found. |
| 2300094 | Authentication error. |
| 2300997 | Cleartext traffic not permitted. |
| 2300998 | It is not allowed to access this domain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. class Header {
4. public contentType: string;

6. constructor(contentType: string) {
7. this.contentType = contentType;
8. }
9. }

11. let httpRequest = http.createHttp();
12. let promise = httpRequest.requestInStream("EXAMPLE_URL", {
13. method: http.RequestMethod.GET,
14. connectTimeout: 60000,
15. readTimeout: 60000,
16. header: new Header('application/json')
17. });
18. promise.then((data: number) => {
19. console.info("requestInStream OK!" + data);
20. }).catch((err: Error) => {
21. console.error("requestInStream ERROR : err = " + JSON.stringify(err));
22. });
```

### on("headerReceive")(deprecated)

PhonePC/2in1TabletTVWearable

on(type: "headerReceive", callback: AsyncCallback<Object>): void

订阅HTTP Response Header 事件。

说明

从API version 6开始支持，从API version 8开始废弃，建议使用[on("headersReceive")](js-apis-http.md#onheadersreceive8)替代。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，'headerReceive'。 |
| callback | AsyncCallback<Object> | 是 | 回调函数。当订阅成功，error为undefined，data为获取到HTTP响应头；否则为错误对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let httpRequest = http.createHttp();
5. httpRequest.on("headerReceive", (data: BusinessError) => {
6. console.error("error:" + JSON.stringify(data));
7. });
```

### off("headerReceive")(deprecated)

PhonePC/2in1TabletTVWearable

off(type: "headerReceive", callback?: AsyncCallback<Object>): void

取消订阅HTTP Response Header事件。

说明

从API version 6开始支持，从API version 8开始废弃，建议使用[off("headersReceive")](js-apis-http.md#offheadersreceive8)替代。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型，'headerReceive'。 |
| callback | AsyncCallback<Object> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.off("headerReceive");
```

### on("headersReceive")8+

PhonePC/2in1TabletTVWearable

on(type: "headersReceive", callback: Callback<Object>): void

订阅HTTP Response Header 事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型：'headersReceive'。 |
| callback | Callback<Object> | 是 | 回调函数，返回HTTP响应头对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("headersReceive", (header: Object) => {
5. console.info("header: " + JSON.stringify(header));
6. });
7. httpRequest.off("headersReceive");
```

### off("headersReceive")8+

PhonePC/2in1TabletTVWearable

off(type: "headersReceive", callback?: Callback<Object>): void

取消订阅HTTP Response Header 事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型：'headersReceive'。 |
| callback | Callback<Object> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("headersReceive", (header: Object) => {
5. console.info("header: " + JSON.stringify(header));
6. });
7. httpRequest.off("headersReceive");
```

### once("headersReceive")8+

PhonePC/2in1TabletTVWearable

once(type: "headersReceive", callback: Callback<Object>): void

订阅HTTP Response Header 事件，只能触发一次。触发之后，订阅器就会被移除。使用callback方式作为异步方法。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型：'headersReceive'。 |
| callback | Callback<Object> | 是 | 回调函数。返回HTTP响应头对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.once("headersReceive", (header: Object) => {
5. console.info("header: " + JSON.stringify(header));
6. });
```

### on("dataReceive")10+

PhonePC/2in1TabletTVWearable

on(type: "dataReceive", callback: Callback<ArrayBuffer>): void

订阅HTTP流式响应数据接收事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，'dataReceive'。 |
| callback | Callback<ArrayBuffer> | 是 | 回调函数。当订阅成功时，error为undefined，data为获取到的HTTP流式数据接收数据，类型为ArrayBuffer；否则为错误对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataReceive", (data: ArrayBuffer) => {
5. console.info("dataReceive length: " + JSON.stringify(data.byteLength));
6. });
7. httpRequest.off("dataReceive");
```

### off("dataReceive")10+

PhonePC/2in1TabletTVWearable

off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void

取消订阅HTTP流式响应数据接收事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型：'dataReceive'。 |
| callback | Callback<ArrayBuffer> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataReceive", (data: ArrayBuffer) => {
5. console.info("dataReceive length: " + JSON.stringify(data.byteLength));
6. });
7. httpRequest.off("dataReceive");
```

### on("dataEnd")10+

PhonePC/2in1TabletTVWearable

on(type: "dataEnd", callback: Callback<void>): void

订阅HTTP流式响应数据接收完毕事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，'dataEnd'。 |
| callback | Callback<void> | 是 | 回调函数。当订阅成功时，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataEnd", () => {
5. console.info("Receive dataEnd !");
6. });
7. httpRequest.off("dataEnd");
```

### off("dataEnd")10+

PhonePC/2in1TabletTVWearable

off(type: "dataEnd", callback?: Callback<void>): void

取消订阅HTTP流式响应数据接收完毕事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型：'dataEnd'。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataEnd", () => {
5. console.info("Receive dataEnd !");
6. });
7. httpRequest.off("dataEnd");
```

### on('dataReceiveProgress')10+

PhonePC/2in1TabletTVWearable

on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void

订阅HTTP流式响应数据接收进度事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，'dataReceiveProgress'。 |
| callback | Callback<[DataReceiveProgressInfo](js-apis-http.md#datareceiveprogressinfo11)> | 是 | 回调函数。当订阅成功时，回调内容是[DataReceiveProgressInfo](js-apis-http.md#datareceiveprogressinfo11)，订阅失败时为undefined。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
5. console.info("dataReceiveProgress:" + JSON.stringify(data));
6. });
7. httpRequest.off("dataReceiveProgress");
```

### off('dataReceiveProgress')10+

PhonePC/2in1TabletTVWearable

off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void

取消订阅HTTP流式响应数据接收进度事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型：'dataReceiveProgress'。 |
| callback | Callback<[DataReceiveProgressInfo](js-apis-http.md#datareceiveprogressinfo11)> | 否 | 回调函数。 可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataReceiveProgress", (data: http.DataReceiveProgressInfo) => {
5. console.info("dataReceiveProgress:" + JSON.stringify(data));
6. });
7. httpRequest.off("dataReceiveProgress");
```

### on('dataSendProgress')11+

PhonePC/2in1TabletTVWearable

on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void

订阅HTTP网络请求数据发送进度事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，'dataSendProgress'。 |
| callback | Callback<[DataSendProgressInfo](js-apis-http.md#datasendprogressinfo11)> | 是 | 回调函数。当订阅成功时，回调内容是[DataSendProgressInfo](js-apis-http.md#datasendprogressinfo11)，订阅失败时为undefined。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
5. console.info("dataSendProgress:" + JSON.stringify(data));
6. });
7. httpRequest.off("dataSendProgress");
```

### off('dataSendProgress')11+

PhonePC/2in1TabletTVWearable

off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void

取消订阅HTTP网络请求数据发送进度事件。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型：'dataSendProgress'。 |
| callback | Callback<[DataSendProgressInfo](js-apis-http.md#datasendprogressinfo11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpRequest = http.createHttp();
4. httpRequest.on("dataSendProgress", (data: http.DataSendProgressInfo) => {
5. console.info("dataSendProgress:" + JSON.stringify(data));
6. });
7. httpRequest.off("dataSendProgress");
```

## HttpRequestOptions

PhonePC/2in1TabletTVWearable

发起HTTP请求时，可选配置信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| method | [RequestMethod](js-apis-http.md#requestmethod) | 否 | 是 | 请求方式，默认为GET。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| extraData | string | Object | ArrayBuffer | 否 | 是 | 发送请求的额外数据，默认无此字段。  **说明：** 没有额外数据时，避免添加该参数；若必须添加，请填写undefined或者null，避免直接传入"。  1. 当HTTP请求为POST、PUT、DELETE等方法时，此字段为HTTP请求的content，以UTF-8编码形式作为请求体。  示例如下：  (1) 当'content-Type'为'application/x-www-form-urlencoded'时，请求提交的信息主体数据必须在key和value进行URL转码后（encodeURIComponent/encodeURI），按照键值对"key1=value1&key2=value2&key3=value3"的方式进行编码，该字段对应的类型通常为String。  (2) 当'content-Type'为'text/xml'时，该字段对应的类型通常为String。  (3) 当'content-Type'为'application/json'时，该字段对应的类型通常为Object。  (4) 当'content-Type'为'application/octet-stream'时，该字段对应的类型通常为ArrayBuffer。  (5) 当'content-Type'为'multipart/form-data'且需上传的字段为文件时，该字段对应的类型通常为ArrayBuffer。  以上信息仅供参考，并可能根据具体情况有所不同。  2. 当HTTP请求为GET、OPTIONS、TRACE、CONNECT等方法时，此字段为HTTP请求参数的补充。开发者需传入Encode编码后的string类型参数，Object类型的参数无需预编码，参数内容会拼接到URL中进行发送。ArrayBuffer类型的参数不会做拼接处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| expectDataType9+ | [HttpDataType](js-apis-http.md#httpdatatype9) | 否 | 是 | 指定返回数据的类型，默认无此字段。如果设置了此参数，系统将优先返回指定的类型。当指定其类型为Object时，最大长度为65536字符数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| usingCache9+ | boolean | 否 | 是 | 是否使用缓存，true表示请求时优先读取缓存，false表示不使用缓存；默认为true，请求时优先读取缓存。缓存跟随当前进程生效，新缓存会替换旧缓存。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| priority9+ | number | 否 | 是 | HTTP/HTTPS请求并发优先级，值越大优先级越高，范围[1,1000]，默认为1。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| header | Object | 否 | 是 | HTTP请求头字段。当请求方式为"POST" "PUT" "DELETE" 或者""时，默认{'content-Type': 'application/json'}， 否则默认{'content-Type': 'application/x-www-form-urlencoded'}。  如果head中包含number类型的字段，最大支持int64的整数。  header字段支持JSON格式如 [完整示例](js-apis-http.md#完整示例) 和Record<string, string>格式输入。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| readTimeout | number | 否 | 是 | 读取超时时间。单位为毫秒（ms），默认为60000ms。传入值需为uint32\_t范围内的整数。  设置为0表示不会出现超时情况。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| connectTimeout | number | 否 | 是 | 连接超时时间。单位为毫秒（ms），默认为60000ms。传入值需为uint32\_t范围内的整数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| usingProtocol9+ | [HttpProtocol](js-apis-http.md#httpprotocol9) | 否 | 是 | 使用协议。默认值由系统自动指定。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| usingProxy10+ | boolean | [HttpProxy](js-apis-net-connection.md#httpproxy10) | 否 | 是 | HTTP代理配置，该项不配置时默认使用系统代理。  - 当usingProxy为布尔类型true时，使用默认网络代理，为false时，不使用代理。  - 当usingProxy为HttpProxy类型时，使用指定网络代理。从API version 22开始，HttpProxy支持指定username和password字段。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| caPath10+ | string | 否 | 是 | 如果设置了此参数且证书有效，系统将使用用户指定的CA证书和系统预设的CA证书；否则仅使用系统预设的CA证书。CA证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。目前仅支持后缀名为.pem的文本格式证书。  系统预设CA证书位置：/etc/ssl/certs/cacert.pem。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| caData20+ | string | 否 | 是 | 如果设置了此参数且证书有效，系统将使用用户指定的CA证书和系统预设的CA证书；否则仅使用系统预设的CA证书。如果同时设置了caPath和caData，caData将被系统忽略。目前仅支持传入.pem格式的证书内容，最大长度为8000字节。仅支持传入单证书，不支持证书链传入。  系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| resumeFrom11+ | number | 否 | 是 | 用于设置下载起始位置，该参数只能用于GET方法，不能用于其他。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。  - 使用HTTP PUT时，不能使用该选项，因为该选项可能与其他选项冲突。  - 取值范围是：[1，4294967296（4GB）]，超出范围则不生效。 |
| resumeTo11+ | number | 否 | 是 | 用于设置下载结束位置，该参数只能用于GET方法，不能用于其他。HTTP标准（RFC 7233第3.1节）允许服务器忽略范围请求。  - 使用HTTP PUT时，不能使用该选项，因为该选项可能与其他选项冲突。  - 取值范围是：[1，4294967296（4GB）]，超出范围则不生效。 |
| clientCert11+ | [ClientCert](js-apis-http.md#clientcert11) | 否 | 是 | 支持传输客户端证书。 |
| dnsOverHttps11+ | string | 否 | 是 | 设置使用HTTPS协议的服务器进行DNS解析。  - 参数必须根据以下格式进行URL编码："https:// host:port/path"。 |
| dnsServers11+ | Array<string> | 否 | 是 | 设置指定的DNS服务器进行DNS解析。  - 最多可以设置3个DNS解析服务器。如果有3个以上，只取前3个。  - 服务器必须是IPV4或者IPV6地址。 |
| maxLimit11+ | number | 否 | 是 | 响应消息的最大字节限制。  默认值为5\*1024\*1024，以字节为单位。最大值为100\*1024\*1024，以字节为单位。 |
| multiFormDataList11+ | Array<[MultiFormData](js-apis-http.md#multiformdata11)> | 否 | 是 | 当'content-Type'为'multipart/form-data'时，则上传该字段定义的数据字段表单列表。 |
| certificatePinning12+ | [CertificatePinning](js-apis-http.md#certificatepinning12) | CertificatePinning[] | 否 | 是 | 支持动态设置证书锁定配置，可以传入单个或多个证书PIN码。 |
| addressFamily15+ | [AddressFamily](js-apis-http.md#addressfamily15) | 否 | 是 | 支持解析目标域名时限定地址类型。 |
| remoteValidation18+ | [RemoteValidation](js-apis-http.md#remotevalidation18) | 否 | 是 | 证书颁发机构（CA），用于验证远程服务器的身份。如果未设置此字段，系统CA将用于验证远程服务器的标识。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| tlsOptions18+ | [TlsOptions](js-apis-http.md#tlsoptions18) | 否 | 是 | TLS配置。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| serverAuthentication18+ | [ServerAuthentication](js-apis-http.md#serverauthentication18) | 否 | 是 | 安全连接期间的服务器身份验证配置。默认不认证。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| sslType20+ | [SslType](js-apis-http.md#ssltype20) | 否 | 是 | 使用安全通信协议TLS（默认）或TLCP。如果使用TLCP，相关的选项（如caPath、clientCert和clientEncCert）必须赋有效值。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| clientEncCert20+ | [ClientCert](js-apis-http.md#clientcert11) | 否 | 是 | 支持应用程序传入客户端证书，使服务器能够进行验证客户端的加密身份。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| customMethod23+ | string | 否 | 是 | 支持自定义请求方法，例如实现WebDAV扩展协议，当与method同时配置时，customMethod优先级更高。  - 默认值为空字符串，最大长度128个字符，超出则不生效。  - 当customMethod符合WebDAV扩展协议请求方式，但服务器不支持时，本次请求的服务器响应码通常为405或501（实际结果与服务器具体行为有关）。  - 当customMethod不符合WebDAV扩展协议请求方式时，本次请求的服务器响应码通常为400或405（实际结果与服务器具体行为有关）。 |
| maxRedirects23+ | number | 否 | 是 | 支持针对HttpRequest指定最大跳转次数。  - 默认值为30次。  - 取值范围是：[0，2147483647]，设置0即为关闭重定向，当服务器的重定向次数超过设置的最大重定向次数时会返回错误码2300047。超出此范围该配置不生效，配置默认值30。 |
| sniHostName23+ | string | 否 | 是 | 支持客户端通过配置SNI（Server Name Indication，服务器名称指示）在TLS握手阶段向服务器声明目标域名，使服务器能够根据域名选择对应的SSL/TLS证书进行加密通信。  - 默认值为空字符串，sniHostName参数长度上限为255个字符。若超出长度限制或设置为空字符串，该设置将不会生效。 |
| pathPreference23+ | [PathPreference](js-apis-http.md#pathpreference23) | 否 | 是 | 支持HTTP请求指定特定激活的网络。 |

## RequestMethod

PhonePC/2in1TabletTVWearable

HTTP 请求方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OPTIONS | "OPTIONS" | OPTIONS方法描述了目标资源的通信选项。 |
| GET | "GET" | GET方法请求指定资源的表示。使用GET的请求应该只检索数据，不应该包含请求内容。 |
| HEAD | "HEAD" | HEAD方法请求与GET请求相同的响应，但没有响应主体。 |
| POST | "POST" | POST方法将实体提交给指定的资源，通常会导致服务器上的状态更改。 |
| PUT | "PUT" | PUT方法将目标资源的所有当前表示替换为请求内容。 |
| DELETE | "DELETE" | DELETE方法用于删除指定的资源。 |
| TRACE | "TRACE" | TRACE方法沿到达目标资源的路径执行消息环回测试。 |
| CONNECT | "CONNECT" | CONNECT方法建立到由目标资源标识的服务器的隧道。 |

## ResponseCode

PhonePC/2in1TabletTVWearable

发起请求返回的响应码。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OK | 200 | 请求成功。用于GET与POST请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CREATED | 201 | 已创建。请求成功并已创建新资源。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ACCEPTED | 202 | 已接受。请求已被接受，但未处理完成。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NOT\_AUTHORITATIVE | 203 | 非授权信息。请求成功。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NO\_CONTENT | 204 | 无内容。服务器成功处理，但未返回内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| RESET | 205 | 重置内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PARTIAL | 206 | 部分内容。服务器成功处理了部分GET请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MULT\_CHOICE | 300 | 多种选择。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MOVED\_PERM | 301 | 永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MOVED\_TEMP | 302 | 临时移动。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SEE\_OTHER | 303 | 查看其它地址。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NOT\_MODIFIED | 304 | 未修改。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| USE\_PROXY | 305 | 使用代理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BAD\_REQUEST | 400 | 客户端请求的语法错误，服务器无法理解。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| UNAUTHORIZED | 401 | 请求需要用户的身份认证。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PAYMENT\_REQUIRED | 402 | 保留字段，将来使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FORBIDDEN | 403 | 服务器理解请求客户端的请求，但是拒绝执行此请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NOT\_FOUND | 404 | 服务器无法根据客户端的请求找到资源(网页)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BAD\_METHOD | 405 | 客户端请求中的方法被禁止。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NOT\_ACCEPTABLE | 406 | 服务器无法根据客户端请求的内容特性完成请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PROXY\_AUTH | 407 | 请求需要代理的身份认证。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CLIENT\_TIMEOUT | 408 | 请求超时。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CONFLICT | 409 | 服务器完成客户端的PUT请求时可能返回此代码，服务器处理请求时发生了冲突。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GONE | 410 | 客户端请求的资源已经不存在。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LENGTH\_REQUIRED | 411 | 服务器无法处理客户端发送的不带Content-Length的请求信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| PRECON\_FAILED | 412 | 客户端请求信息的先决条件错误。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ENTITY\_TOO\_LARGE | 413 | 由于请求的实体过大，服务器无法处理，因此拒绝请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| REQ\_TOO\_LONG | 414 | 请求的URI过长(URI通常为网址)，服务器无法处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| UNSUPPORTED\_TYPE | 415 | 服务器无法处理请求的格式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| RANGE\_NOT\_SATISFIABLE12+ | 416 | 请求范围不符合要求。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERNAL\_ERROR | 500 | 服务器内部错误，无法完成请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NOT\_IMPLEMENTED | 501 | 服务器不支持请求的功能，无法完成请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BAD\_GATEWAY | 502 | 充当网关或代理的服务器，从远端服务器接收到了一个无效的请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| UNAVAILABLE | 503 | 由于超载或系统维护，服务器暂时无法处理客户端的请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| GATEWAY\_TIMEOUT | 504 | 充当网关或代理的服务器，未及时从远端服务器获取请求。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| VERSION | 505 | 服务器不支持客户端请求中使用的HTTP协议版本。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## HttpResponse

PhonePC/2in1TabletTVWearable

request方法回调函数的返回值类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | string | Object | ArrayBuffer | 否 | 否 | HTTP请求根据响应头中content-type类型返回对应的响应格式内容，若HttpRequestOptions无expectDataType字段，按如下规则返回：  - application/json：返回JSON格式的字符串。  - application/octet-stream：ArrayBuffer。  - image：ArrayBuffer。  - 其他：string。  若HttpRequestOption有expectDataType字段，开发者需传入与服务器返回类型相同的数据类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| resultType9+ | [HttpDataType](js-apis-http.md#httpdatatype9) | 否 | 否 | 返回值类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| responseCode | [ResponseCode](js-apis-http.md#responsecode) | number | 否 | 否 | 回调函数执行成功时，此字段为[ResponseCode](js-apis-http.md#responsecode)。若执行失败，错误码将会从AsyncCallback中的err字段返回。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| header | Object | 否 | 否 | 发起HTTP请求返回来的响应头。当前返回的是JSON格式字符串，如需具体字段内容，需开发者自行解析。常见字段及解析方式如下：  - content-type：header['content-type']。  - status-line：header['status-line']。  - date：header.date/header['date']。  - server：header.server/header['server']。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| cookies8+ | string | 否 | 否 | 服务器返回的原始cookies。开发者可自行处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| performanceTiming11+ | [PerformanceTiming](js-apis-http.md#performancetiming11) | 否 | 否 | HTTP请求的各个阶段的耗时。 |

## ClientCert11+

PhonePC/2in1TabletTVWearable

客户端证书类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certPath | string | 否 | 否 | 证书路径。 |
| certType | [CertType](js-apis-http.md#certtype11) | 否 | 是 | 证书类型，默认是PEM。 |
| keyPath | string | 否 | 否 | 证书密钥的路径。 |
| keyPassword | string | 否 | 是 | 证书密钥的密码。默认值为空字符串。 |

## PerformanceTiming11+

PhonePC/2in1TabletTVWearable

性能打点(单位：毫秒)。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dnsTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到DNS解析完成耗时。 |
| tcpTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到TCP连接完成耗时。 |
| tlsTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到TLS连接完成耗时。 |
| firstSendTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到开始发送第一个字节的耗时。 |
| firstReceiveTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到接收第一个字节的耗时。 |
| totalFinishTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到完成请求的耗时。 |
| redirectTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到完成所有重定向步骤的耗时。 |
| responseHeaderTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到header解析完成的耗时。 |
| responseBodyTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求到body解析完成的耗时。 |
| totalTiming | number | 否 | 否 | 从[request](js-apis-http.md#request)请求回调到应用程序的耗时。 |

## DataReceiveProgressInfo11+

PhonePC/2in1TabletTVWearable

数据接收信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| receiveSize | number | 否 | 否 | 已接收的数据量（单位：字节）。 |
| totalSize | number | 否 | 否 | 总共要接收的数据量（单位：字节）。 |

## DataSendProgressInfo11+

PhonePC/2in1TabletTVWearable

数据发送信息。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sendSize | number | 否 | 否 | 每次发送的数据量(单位：字节)。 |
| totalSize | number | 否 | 否 | 总共要发送的数据量(单位：字节)。 |

## MultiFormData11+

PhonePC/2in1TabletTVWearable

多部分表单数据的类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 数据名称。 |
| contentType | string | 否 | 否 | 数据类型，如'text/plain'，'image/png', 'image/jpeg', 'audio/mpeg', 'video/mp4'等。 |
| remoteFileName | string | 否 | 是 | 上传到服务器保存为文件的名称。  **说明**：指定该字段后，请求头中会添加filename字段，表示上传到服务器文件的名称。  （1）当上传数据为文件时，若通过data字段指定文件内容，通常需要设置remoteFileName字段，用以指定上传到服务器文件的名称（实际结果与服务器具体行为有关）；若通过filePath字段指定文件路径，请求头中会自动添加filename字段，其默认值为filePath中的文件名称，如需特殊指定，也可通过本字段对filename重新设置。  （2）当上传数据为二进制格式时，则必须设置remoteFileName字段。 |
| data | string | Object | ArrayBuffer | 否 | 是 | 表单数据内容。 |
| filePath | string | 否 | 是 | 此参数将文件路径指向的文件内容设置为表单数据，如果未指定data内容，则必须设置filePath。  **说明**：需传入文件管理模块支持的格式，可以通过文件管理的[access](js-apis-file-fs.md#fileioaccess)接口，验证文件是否存在且可访问。 |

## http.createHttpResponseCache9+

PhonePC/2in1TabletTVWearable

createHttpResponseCache(cacheSize?: number): HttpResponseCache

创建一个HttpResponseCache对象，可用于存储HTTP请求的响应数据。对象中可调用[flush](js-apis-http.md#flush9)与[delete](js-apis-http.md#delete9)方法，cacheSize指定缓存大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheSize | number | 否 | 缓存大小。最大为10\*1024\*1024（10MB），默认最大。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HttpResponseCache](js-apis-http.md#httpresponsecache9) | 返回一个存储HTTP访问请求响应的对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let httpResponseCache = http.createHttpResponseCache();
```

## HttpResponseCache9+

PhonePC/2in1TabletTVWearable

存储HTTP访问请求响应的对象。在调用HttpResponseCache的方法前，需要先通过[createHttpResponseCache()](js-apis-http.md#httpcreatehttpresponsecache9)创建一个任务。

**响应头中的相应关键字使用**

* **Cache-Control**：用于指定缓存策略，如no-cache, no-store, max-age, public, private等。
* **Expires**：指定资源的过期时间，格式为GMT时间。
* **ETag**：用于资源版本标识，客户端可以使用If-None-Match请求头来验证资源是否已更改。
* **Last-Modified**：指定资源最后修改时间，客户端可以使用If-Modified-Since请求头来验证资源是否已更改。
* **Vary**：指定哪些请求头的值会影响缓存的响应，用于区分不同的缓存版本。

使用这些关键字时，服务器端需要正确配置响应头，客户端则需要根据这些响应头来决定是否使用缓存的资源，以及如何验证资源是否是最新的。正确的缓存策略可以显著提高应用的性能和用户体验。

**如何设置Cache-Control头**

Cache-Control为通用报头，但通常是在服务器端进行的，允许定义一个响应资源应该何时、如何被缓存以及缓存多长时间。以下是一些常用的Cache-Control指令及其含义：

* **no-cache**：表示在使用缓存前，必须先去源服务器校验资源的有效性。如果资源未变更，则响应状态码为304(Not Modified)，不发送资源内容，使用缓存中的资源。如果资源已经过期，则响应状态码为200(OK)，并发送资源内容。
* **no-store**：表示不允许缓存资源，每次请求都必须从服务器获取资源。
* **max-age**：指定缓存的最大时间(以秒为单位)。例如，Cache-Control: max-age=3600表示缓存的有效期为1小时。
* **public**：表明响应可以被任何对象(包括：发送请求的客户端，代理服务器等)缓存。
* **private**：表明响应只能被单个用户缓存，不能作为共享缓存(即代理服务器不能缓存)。
* **must-revalidate**：表示必须在使用缓存前验证旧资源的状态，并且在缓存过期后，需要重新验证资源。
* **no-transform**：表示不允许代理服务器修改响应内容。
* **proxy-revalidate**：与must-revalidate类似，但仅适用于共享缓存。
* **s-maxage**：类似于max-age，但仅适用于共享缓存。

### flush9+

PhonePC/2in1TabletTVWearable

flush(callback: AsyncCallback<void>): void

将缓存中的数据写入文件系统，以便在下一个HTTP请求中访问所有缓存数据，使用callback方式作为异步方法。缓存数据包括：响应头(header)、响应体(result)、cookies、请求时间(requestTime)和响应时间(responseTime)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。返回写入结果。当写入成功时，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let httpResponseCache = http.createHttpResponseCache();
5. let httpRequest = http.createHttp();
6. httpRequest.request("EXAMPLE_URL", (err: BusinessError, data: http.HttpResponse) => {
7. if (!err) {
8. httpResponseCache.flush((err: BusinessError) => {
9. if (err) {
10. console.error('flush fail');
11. }
12. console.info('flush success');
13. });
14. httpRequest.destroy();
15. } else {
16. console.error('error:' + JSON.stringify(err));
17. // 当该请求使用完毕时，开发者务必调用destroy方法释放资源，避免出现内存泄漏。
18. httpRequest.destroy();
19. }
20. });
```

### flush9+

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

将缓存中的数据写入文件系统，以便在下一个HTTP请求中访问所有缓存数据，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let httpRequest = http.createHttp();
5. let httpResponseCache = http.createHttpResponseCache();
6. let promise = httpRequest.request("EXAMPLE_URL");

8. promise.then((data: http.HttpResponse) => {
9. httpResponseCache.flush().then(() => {
10. console.error('flush success');
11. }).catch((err: BusinessError) => {
12. console.error('flush fail');
13. });
14. }).catch((err: Error) => {
15. console.error('error:' + JSON.stringify(err));
16. });
```

### delete9+

PhonePC/2in1TabletTVWearable

delete(callback: AsyncCallback<void>): void

禁用缓存并删除其中的数据，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功时，err为undefined，否则为错误对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let httpRequest = http.createHttp();
5. httpRequest.request("EXAMPLE_URL").then(data => {
6. const httpResponseCache = http.createHttpResponseCache();
7. httpResponseCache.delete((err: BusinessError) => {
8. try {
9. if (err) {
10. console.error('fail: ' + err);
11. } else {
12. console.info('success');
13. }
14. } catch (err) {
15. console.error('error: ' + err);
16. }
17. });
18. httpRequest.destroy();
19. }).catch((error: BusinessError) => {
20. console.error("errcode" + JSON.stringify(error));
21. });
```

### delete9+

PhonePC/2in1TabletTVWearable

delete(): Promise<void>

禁用缓存并删除其中的数据，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let httpRequest = http.createHttp();
5. httpRequest.request("EXAMPLE_URL").then(data => {
6. const httpResponseCache = http.createHttpResponseCache();
7. httpResponseCache.delete().then(() => {
8. console.info("success");
9. }).catch((err: BusinessError) => {
10. console.error("fail");
11. });
12. httpRequest.destroy();
13. }).catch((error: BusinessError) => {
14. console.error("errcode" + JSON.stringify(error));
15. });
```

## HttpDataType9+

PhonePC/2in1TabletTVWearable

HTTP的数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STRING | 0 | 字符串类型。 |
| OBJECT | 1 | 对象类型。 |
| ARRAY\_BUFFER | 2 | 二进制数组类型。 |

## HttpProtocol9+

PhonePC/2in1TabletTVWearable

HTTP协议版本。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HTTP1\_1 | 0 | 协议HTTP1.1。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| HTTP2 | 1 | 协议HTTP2。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| HTTP311+ | 2 | 协议HTTP3，若系统或服务器不支持，则使用低版本的HTTP协议请求。  **注意：** 仅对HTTPS的URL生效，HTTP则会请求失败。 |

## CertType11+

PhonePC/2in1TabletTVWearable

枚举，证书类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM | PEM | 证书类型PEM。 |
| DER | DER | 证书类型DER。 |
| P12 | P12 | 证书类型P12。 |

## CertificatePinning12+

PhonePC/2in1TabletTVWearable

由应用配置的证书。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| publicKeyHash | string | 否 | 否 | 字符串类型的证书PIN码。 |
| hashAlgorithm | 'SHA-256' | 否 | 否 | 加密算法，当前仅支持该算法。 |

## HttpProxy10+

PhonePC/2in1TabletTVWearable

type HttpProxy = connection.HttpProxy

网络代理配置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| connection.HttpProxy | 网络代理配置信息。 |

## AddressFamily15+

PhonePC/2in1TabletTVWearable

枚举，解析目标域名时限定的地址类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | CURL\_IPRESOLVE\_WHATEVER | 设置此选项后，系统将自行选择目标域名的IPv4地址或IPv6地址。 |
| ONLY\_V4 | CURL\_IPRESOLVE\_V4 | 设置此选项后，系统仅解析目标域名的IPv4地址，忽略IPv6地址。 |
| ONLY\_V6 | CURL\_IPRESOLVE\_V6 | 设置此选项后，系统仅解析目标域名的IPv6地址，忽略IPv4地址。 |

## Credential18+

PhonePC/2in1TabletTVWearable

会话中服务器身份验证设置所使用的身份验证凭据，包括用户名和密码。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| username | string | 否 | 否 | 用于身份验证的用户名。默认值为' '。 |
| password | string | 否 | 否 | 用于身份验证的密码。默认值为' '。 |

## ServerAuthentication18+

PhonePC/2in1TabletTVWearable

HTTP服务器身份验证。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credential | [Credential](js-apis-http.md#credential18) | 否 | 否 | 服务器的凭证。默认值为undefined。 |
| authenticationType | [AuthenticationType](js-apis-http.md#authenticationtype18) | 否 | 是 | 服务器的认证类型。如果没有设置，需与服务器协商。 |

## TlsConfig18+

PhonePC/2in1TabletTVWearable

TLS加密版本及套件配置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tlsVersionMin | [TlsVersion](js-apis-http.md#tlsversion18) | 否 | 否 | TLS最低版本号。 |
| tlsVersionMax | [TlsVersion](js-apis-http.md#tlsversion18) | 否 | 否 | TLS最高版本号。 |
| cipherSuites | [CipherSuite](js-apis-http.md#ciphersuite18)[] | 否 | 是 | 声明加密套件类型的数组。如果没有设置，默认携带全部支持的加密套件类型，加密套件类型参考[TlsV13SpecificCipherSuite](js-apis-http.md#tlsv13specificciphersuite18)、[TlsV12SpecificCipherSuite](js-apis-http.md#tlsv12specificciphersuite18)、[TlsV10SpecificCipherSuite](js-apis-http.md#tlsv10specificciphersuite18)。 |

## TlsVersion18+

PhonePC/2in1TabletTVWearable

枚举，TLS版本号。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TLS\_V\_1\_0 | 4 | TLS版本号1.0。 |
| TLS\_V\_1\_1 | 5 | TLS版本号1.1。 |
| TLS\_V\_1\_2 | 6 | TLS版本号1.2。 |
| TLS\_V\_1\_3 | 7 | TLS版本号1.3。 |

## TlsOptions18+

PhonePC/2in1TabletTVWearable

type TlsOptions = 'system' | TlsConfig

TLS配置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'system' | 表示使用系统的TLS版本，是未进行TLS设置的默认值，值固定为'system'字符串。 |
| TlsConfig | 表示使用自定义的TLS版本号和加密套件。 |

## RemoteValidation18+

PhonePC/2in1TabletTVWearable

type RemoteValidation = 'system' | 'skip'

验证远程服务器身份的方式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'system' | 表示使用系统CA验证远端服务器身份，值固定为'system'字符串，是未配置时的默认值。 |
| 'skip' | 表示跳过验证远端服务器身份流程，值固定为'skip'字符串。 |

## AuthenticationType18+

PhonePC/2in1TabletTVWearable

type AuthenticationType = 'basic' | 'ntlm' | 'digest'

在会话中的服务器身份验证时可以设置使用不同的身份验证机制。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'basic' | 表示使用基本认证方式，值固定为'basic'字符串。 |
| 'ntlm' | 表示使用ntlm认证方式，值固定为'ntlm'字符串。 |
| 'digest' | 表示使用摘要认证方式，值固定为'digest'字符串。 |

## CipherSuite18+

PhonePC/2in1TabletTVWearable

type CipherSuite = TlsV13CipherSuite

加密套件声明函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| TlsV13CipherSuite | 表示值的类型为[TlsV13CipherSuite](js-apis-http.md#tlsv13ciphersuite18)。 |

## TlsV13CipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV13CipherSuite = TlsV12CipherSuite | TlsV13SpecificCipherSuite

TLS1.3的加密套件声明函数，支持TLS1.3版本，兼容TLS1.2版本。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| TlsV12CipherSuite | 表示值的类型为[TlsV11CipherSuite](js-apis-http.md#tlsv11ciphersuite18)。 |
| TlsV13SpecificCipherSuite | 表示值的类型为[TlsV13SpecificCipherSuite](js-apis-http.md#tlsv13specificciphersuite18)。 |

## TlsV12CipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV12CipherSuite = TlsV11CipherSuite | TlsV12SpecificCipherSuite

TLS1.2的加密套件声明函数，支持TLS1.2版本，兼容TLS1.1版本。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| TlsV11CipherSuite | 表示值的类型为[TlsV11CipherSuite](js-apis-http.md#tlsv11ciphersuite18)。 |
| TlsV12SpecificCipherSuite | 表示值的类型为[TlsV12SpecificCipherSuite](js-apis-http.md#tlsv12specificciphersuite18)。 |

## TlsV11CipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV11CipherSuite = TlsV10CipherSuite

TLS1.1的加密套件声明函数，与TLS1.0的加密套件相同。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| TlsV10CipherSuite | 表示值的类型为[TlsV10CipherSuite](js-apis-http.md#tlsv10ciphersuite18)。 |

## TlsV10CipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV10CipherSuite = TlsV10SpecificCipherSuite

TLS1.0的加密套件声明函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| TlsV10SpecificCipherSuite | 表示值的类型为[TlsV10SpecificCipherSuite](js-apis-http.md#tlsv10specificciphersuite18)。 |

## TlsV13SpecificCipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV13SpecificCipherSuite = 'TLS\_AES\_128\_GCM\_SHA256' | 'TLS\_AES\_256\_GCM\_SHA384' | 'TLS\_CHACHA20\_POLY1305\_SHA256'

TLS1.3及以上版本支持的加密套件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'TLS\_AES\_128\_GCM\_SHA256' | 表示值的类型为字符串，可取'TLS\_AES\_128\_GCM\_SHA256'。 |
| 'TLS\_AES\_256\_GCM\_SHA384' | 表示值的类型为字符串，可取'TLS\_AES\_256\_GCM\_SHA384'。 |
| 'TLS\_CHACHA20\_POLY1305\_SHA256' | 表示值的类型为字符串，可取'TLS\_CHACHA20\_POLY1305\_SHA256'。 |

## TlsV12SpecificCipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV12SpecificCipherSuite = 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256' |

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384' |

'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | 'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256' |

'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | 'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384'

TLS1.2及以上版本支持的加密套件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256' | 表示值的类型为字符串，可取'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256'。 |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | 表示值的类型为字符串，可取'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256'。 |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384' | 表示值的类型为字符串，可取'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384'。 |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384' | 表示值的类型为字符串，可取'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384'。 |
| 'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | 表示值的类型为字符串，可取'TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256'。 |
| 'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256' | 表示值的类型为字符串，可取'TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256'。 |
| 'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256' | 表示值的类型为字符串，可取'TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256'。 |
| 'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384' | 表示值的类型为字符串，可取'TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384'。 |

## TlsV10SpecificCipherSuite18+

PhonePC/2in1TabletTVWearable

type TlsV10SpecificCipherSuite = 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA' |

'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA' |

'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA'

TLS1.0及以上版本支持的加密套件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA'。 |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA'。 |
| 'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA'。 |
| 'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA'。 |
| 'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA'。 |
| 'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA'。 |
| 'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA' | 表示值的类型为字符串，可取'TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA'。 |

## SslType20+

PhonePC/2in1TabletTVWearable

type SslType = 'TLS' | 'TLCP'

安全通信协议。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'TLS' | 表示使用TLS安全通信协议，值固定为'TLS'字符串。 |
| 'TLCP' | 表示使用TLCP安全通信协议，值固定为'TLCP'字符串。  **说明**：  （1）证书支持字符串的规格：  - UTF8String（英文字符集）  - PrintableString  - IA5String  从API Version 22开始支持：  - TeletexString  （2）证书支持扩展的规格：  - BasicConstraints（OID 2.5.29.19）  - KeyUsage（OID2.5.29.15）  - SubjectKeyIdentifier（OID2.5.29.14）  - AuthorityKeyIdentifier（OID2.5.29.35）  从API Version 22开始支持：  - SubjectAltName（OID 2.5.29.17）  - ExtendedKeyUsage（OID 2.5.29.37） |

## InterceptorType22+

PhonePC/2in1TabletTVWearable

HTTP拦截器的类型枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INITIAL\_REQUEST | 'INITIAL\_REQUEST' | 在初始HTTP请求组装完成后拦截。 |
| REDIRECTION | 'REDIRECTION' | 当收到重定向响应时拦截。 |
| CACHE\_CHECKED | 'READ\_CACHE' | 在检查并且命中HTTP缓存时拦截。 |
| NETWORK\_CONNECT | 'CONNECT\_NETWORK' | 在网络请求将要发出前拦截。 |
| FINAL\_RESPONSE | 'FINAL\_RESPONSE' | 在获取最终HTTP响应时拦截。 |

## HttpRequestContext22+

PhonePC/2in1TabletTVWearable

HTTP请求上下文数据。该对象实例在拦截器的[interceptorHandle](js-apis-http.md#interceptorhandle22)方法中作为参数传入，开发者可以通过该对象获取和修改HTTP请求的相关信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | HTTP拦截器从HTTP请求中获取到的URL，支持在拦截器中进行修改。 |
| header | Object | 否 | 否 | HTTP拦截器从HTTP请求中获取到的请求头，支持在拦截器中进行修改。 |
| body | Object | 否 | 否 | HTTP拦截器从HTTP请求中获取到的请求体，支持在拦截器中进行修改。 |

## ChainContinue22+

PhonePC/2in1TabletTVWearable

type ChainContinue = boolean

是否继续处理拦截器链。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| boolean | true表示继续处理拦截器链，false表示终止并返回HTTP响应。 |

## HttpInterceptor22+

PhonePC/2in1TabletTVWearable

HTTP拦截器接口。用户可以实现此接口来定义拦截处理函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interceptorType | [InterceptorType](js-apis-http.md#interceptortype22) | 否 | 否 | 拦截器类型，定义此拦截器何时被调用。 |

### interceptorHandle22+

PhonePC/2in1TabletTVWearable

interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>

拦截HTTP处理过程并进行所需的更改。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reqContext | [HttpRequestContext](js-apis-http.md#httprequestcontext22) | 是 | 经过HTTP拦截器的请求参数的上下文。 |
| rspContext | [HttpResponse](js-apis-http.md#httpresponse) | 是 | 经过HTTP拦截器的返回结果的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ChainContinue](js-apis-http.md#chaincontinue22)> | 继续HTTP处理或终止并返回HTTP响应。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. // 创建自定义拦截器
4. class CustomInterceptor implements http.HttpInterceptor {
5. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

7. async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
8. // 在初始请求阶段添加认证头
9. reqContext.header['Authorization'] = 'Bearer token';
10. console.info('Interceptor: Added authorization header');
11. return true; // 继续处理拦截器链
12. }
13. }

15. let customInterceptor = new CustomInterceptor();
```

## HttpInterceptorChain22+

PhonePC/2in1TabletTVWearable

HTTP拦截器链。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. let interceptorChain = new http.HttpInterceptorChain();
```

### addChain22+

PhonePC/2in1TabletTVWearable

addChain(chain: HttpInterceptor[]): boolean

向HTTP客户端添加拦截器。

说明

拦截器链中不能包含相同类型的拦截器实例。如果传入相同类型的拦截器，会抛出错误码2300802（Duplicated interceptor type in the chain）。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chain | [HttpInterceptor](js-apis-http.md#httpinterceptor22)[] | 是 | 拦截器实例组成的拦截链，支持传入单个或者多个不同类型的拦截器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 拦截器是否添加成功。true表示拦截器添加成功，false表示拦截器没有添加成功。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 2300801 | Parameter type not supported by the interceptor. |
| 2300802 | Duplicated interceptor type in the chain. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. // 创建认证拦截器
4. class AuthInterceptor implements http.HttpInterceptor {
5. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

7. async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
8. // 在初始请求阶段添加认证头
9. reqContext.header['Authorization'] = 'Bearer token';
10. console.info('Interceptor: Added authorization header');
11. return true; // 继续处理拦截器链
12. }
13. }

15. class LoggingInterceptor implements http.HttpInterceptor {
16. interceptorType: http.InterceptorType = http.InterceptorType.FINAL_RESPONSE;

18. async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
19. // 在最终响应阶段记录日志
20. console.info(`LoggingInterceptor: Request to ${reqContext.url} completed with status ${rspContext.responseCode}`);
21. return true; // 继续处理拦截器链
22. }
23. }

25. // 创建拦截器链并应用到请求
26. let interceptorChain = new http.HttpInterceptorChain();
27. let authInterceptor = new AuthInterceptor();
28. let loggingInterceptor = new LoggingInterceptor();

30. // 添加拦截器到链中
31. try {
32. let success = interceptorChain.addChain([authInterceptor, loggingInterceptor]);
33. if (!success) {
34. console.error('Failed to add interceptor chain');
35. }
36. } catch (e) {
37. console.error(`Interceptor chain add failed: code=${e.code}, message=${e.message}`);
38. }
```

### getChain22+

PhonePC/2in1TabletTVWearable

getChain(): HttpInterceptor[]

获取当前拦截器链中的所有拦截器实例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HttpInterceptor](js-apis-http.md#httpinterceptor22)[] | 返回通过[addChain](js-apis-http.md#addchain22)方法添加的所有拦截器实例。 |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. // 创建自定义拦截器
4. class CustomInterceptor implements http.HttpInterceptor {
5. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

7. async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
8. // 在初始请求阶段添加认证头
9. reqContext.header['Authorization'] = 'Bearer token';
10. console.info('Interceptor: Added authorization header');
11. return true; // 继续处理拦截器链
12. }
13. }

15. // 创建拦截器链并应用到请求
16. let interceptorChain = new http.HttpInterceptorChain();
17. let customInterceptor = new CustomInterceptor();

19. // 添加拦截器到链中
20. try {
21. let success = interceptorChain.addChain([customInterceptor]);
22. if (!success) {
23. console.error('Failed to add interceptor chain');
24. }
25. } catch (e) {
26. console.error(`Interceptor chain add failed: code=${e.code}, message=${e.message}`);
27. }

29. // 获取当前拦截器链中的所有拦截器
30. let chain = interceptorChain.getChain();
31. console.info(`Current interceptor chain has ${chain.length} interceptors`);
```

### apply22+

PhonePC/2in1TabletTVWearable

apply(httpRequest: HttpRequest): boolean

将拦截器链附加到目标HTTP请求。每个HTTP请求实例只能附加一个拦截器链。

说明

将拦截器链附加到[HttpRequest](js-apis-http.md#httprequest)实例后，当该实例发起HTTP请求时，会触发已附加的拦截器链中相应类型的拦截器。

更多使用HTTP请求触发拦截器功能，可以参考[HTTP拦截器功能代码示例](../harmonyos-guides/http-request.md#http拦截器)。

HTTP拦截器相关能力仅支持[HttpRequest.request](js-apis-http.md#request)接口，目前暂不支持[HttpRequest.requestInStream](js-apis-http.md#requestinstream10)(流式传输)接口。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| httpRequest | [HttpRequest](js-apis-http.md#httprequest) | 是 | 要发起HTTP请求的[HttpRequest](js-apis-http.md#httprequest)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 拦截器是否附加成功。true表示拦截器附加成功，false表示拦截器没有附加成功。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[HTTP错误码](errorcode-net-http.md)。

HTTP错误码映射关系：2300000 + curl错误码。更多常用错误码可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)

| 错误码ID | 错误信息 |
| --- | --- |
| 2300801 | Parameter type not supported by the interceptor. |
| 2300999 | Internal error. |

**示例：**

```
1. import { http } from '@kit.NetworkKit';

3. // 创建认证拦截器
4. class AuthInterceptor implements http.HttpInterceptor {
5. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

7. async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
8. // 在初始请求阶段添加认证头
9. reqContext.header['Authorization'] = 'Bearer token';
10. console.info('Interceptor: Added authorization header');
11. return true; // 继续处理拦截器链
12. }
13. }

15. class LoggingInterceptor implements http.HttpInterceptor {
16. interceptorType: http.InterceptorType = http.InterceptorType.FINAL_RESPONSE;

18. async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
19. // 在最终响应阶段记录日志
20. console.info(`LoggingInterceptor: Request to ${reqContext.url} completed with status ${rspContext.responseCode}`);
21. return true; // 继续处理拦截器链
22. }
23. }

25. // 创建拦截器链
26. let interceptorChain = new http.HttpInterceptorChain();
27. let authInterceptor = new AuthInterceptor();
28. let loggingInterceptor = new LoggingInterceptor();

30. // 创建HTTP请求
31. let httpRequest = http.createHttp();

33. try {
34. // 添加拦截器到链中
35. let success = interceptorChain.addChain([authInterceptor, loggingInterceptor]);
36. if (!success) {
37. console.error('Failed to add interceptor chain');
38. }

40. // 将拦截器链应用到HTTP请求
41. let applySuccess = interceptorChain.apply(httpRequest);
42. if (!applySuccess) {
43. console.error('Failed to apply interceptor chain');
44. }
45. } catch (e) {
46. console.error(`Interceptor chain add failed: code=${e.code}, message=${e.message}`);
47. }

49. // 发起HTTP请求。如需使用拦截，仅支持通过request接口发起请求
50. httpRequest.request("EXAMPLE_URL", {
51. method: http.RequestMethod.GET,
52. header: { 'Content-Type': 'application/json' }
53. }, (err: Error, data: http.HttpResponse) => {
54. if (!err) {
55. console.info('Request completed with response code: ' + data.responseCode);
56. } else {
57. console.error('Request failed: ' + JSON.stringify(err));
58. }
59. httpRequest.destroy();
60. });
```

## PathPreference23+

PhonePC/2in1TabletTVWearable

type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular'

HTTP请求指定特定网络的类型枚举。

说明

推荐在网络并发等场景下使用。

当指定的网络没有激活时，系统按照指定默认网络处理。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'auto' | 表示HTTP请求指定默认的网络连接。 |
| 'primaryCellular' | 表示在蜂窝网络激活的场景下，HTTP请求指定默认的蜂窝网络连接。 |
| 'secondaryCellular' | 表示在双蜂窝网络激活的场景下，HTTP请求指定副卡的蜂窝网络连接。 |
