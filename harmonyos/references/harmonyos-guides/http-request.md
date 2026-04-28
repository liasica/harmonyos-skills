---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/http-request
title: 使用HTTP访问网络
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 访问网络 > 使用HTTP访问网络
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:33bf902cee3586e85b28dca488184d3d1ef2356823eeb3f2c4dcc88b3f802ba3
---

## 场景介绍

应用通过HTTP发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、TRACE、CONNECT方法。当前提供了2种HTTP请求方式，若请求发送或接收的数据量较少，可使用[HttpRequest.request](../harmonyos-references/js-apis-http.md#request)，若是大文件的上传或者下载，且关注数据发送和接收进度，可使用HTTP请求流式传输[HttpRequest.requestInstream](../harmonyos-references/js-apis-http.md#requestinstream10)。从API version 22开始，若是需要在"HTTP请求-响应"生命周期中的关键节点插入自定义逻辑，可以使用[HTTP拦截器](http-request.md#http拦截器)。

说明

HTTP模块提供了标准的HTTP网络服务能力，Remote Communication Kit（远场通信服务）提供了场景化的网络服务能力，详见[Remote Communication Kit简介](remote-communication-introduction.md)，应用可根据自己的需要选择使用。

当前HTTP请求支持的场景如下，以下功能对应的选项可以在HTTP请求的[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)中进行设置：

| 功能分类 | 功能名称 | 功能描述 | 开始支持的版本 |
| --- | --- | --- | --- |
| 基础功能 | 设置请求方式 | 支持GET、POST、HEAD、PUT、DELETE、TRACE、CONNECT、OPTIONS方法，默认为GET。 | API version 6 |
| 基础功能 | 设置请求额外数据 | 支持发送请求时同步携带额外数据，默认无此字段。 | API version 6 |
| 基础功能 | 设置读取超时时间 | 该参数设置的是从请求开始到请求结束的总时间，包括DNS解析、连接建立、传输等。单位为毫秒（ms），默认为60000ms。 | API version 6 |
| 基础功能 | 设置连接超时时间 | 该参数设置的是连接超时时间。单位为毫秒（ms），默认为60000ms。 | API version 6 |
| 基础功能 | 设置HTTP请求头 | 当请求方式为"POST" "PUT" "DELETE" 或者""时，默认{'content-Type': 'application/json'}， 否则默认{'content-Type': 'application/x-www-form-urlencoded'}。 | API version 6 |
| 基础功能 | 设置响应数据类型 | 可以指定HTTP响应数据的类型，默认无此字段。如果设置了此参数，系统将优先返回指定的类型。 | API version 9 |
| 基础功能 | 设置请求并发优先级 | 指定HTTP/HTTPS请求并发优先级，值越大优先级越高，范围[1,1000]，默认为1。 | API version 9 |
| 基础功能 | 设置是否使用缓存 | 可以指定是否使用缓存，默认为true，请求时优先读取缓存。 缓存跟随当前进程生效。新缓存会替换旧缓存，设置为false表示不使用缓存。 | API version 9 |
| 基础功能 | 设置使用协议类型 | HTTPS的请求默认是HTTP/2，失败回退HTTP/1.1；HTTP直接用HTTP/1.1。用户可以指定为HTTP 1.1、HTTP 2、HTTP 3协议版本。 | API version 9 |
| 代理设置 | 设置HTTP请求代理 | 设置HTTP代理，默认值为false，表示不使用代理，若设置为true，表示使用HTTP代理，且为系统默认代理，也可通过配置HttpProxy自定义网络代理。 | API version 10 |
| 证书验证 | 设置CA证书路径 | 如果设置了此参数，系统将使用用户指定路径的CA证书（开发者需保证该路径下CA证书的可访问性），否则将使用系统预设CA证书。 | API version 10 |
| 证书验证 | 设置支持传输客户端证书 | 支持传输客户端证书，包括证书路径、证书类型、证书密钥路径和密码信息。 | API version 11 |
| 基础功能 | 设置下载起始位置和结束位置 | 指定客户端要获取的数据范围，通常在下载文件时配置该参数。 | API version 11 |
| 基础功能 | 设置需要上传的数据字段表单列表 | 设置多部分表单数据，通常用于上传文件。 | API version 11 |
| DNS设置 | 设置使用HTTPS协议的服务器进行DNS解析 | 设置使用HTTPS协议的服务器进行DNS解析。参数必须根据以下格式进行URL编码:'https://host:port/path'。 | API version 11 |
| DNS设置 | 设置指定的DNS服务器进行DNS解析 | 设置指定的DNS服务器进行DNS解析。可以设置多个DNS解析服务器，最多3个服务器。如果有3个以上，只取前3个。服务器必须是IPV4或者IPV6地址形式。 | API version 11 |
| 基础功能 | 设置响应消息的最大字节限制 | 响应消息的最大字节限制。以字节为单位，默认值为5\*1024\*1024，最大值为100\*1024\*1024。 | API version 11 |
| 证书验证 | 设置动态设置证书锁定配置 | 动态设置证书锁定配置，可以传入单个或多个证书PIN码。 | API version 12 |
| 证书验证 | 设置解析目标域名时限定地址类型 | 指定在解析目标域名时的地址类型，可以设置为：跟随系统网络配置、强制仅使用IPV4地址或者强制仅使用IPV6地址。 | API version 15 |
| 证书验证 | 设置跳过SSL证书校验 | 可以设置跳过SSL证书校验流程。 | API version 18 |
| 证书验证 | 设置证书校验的版本和加密套件 | 自定义证书校验版本和加密套件。 | API version 18 |
| 证书验证 | 设置安全连接期间的服务器身份验证配置信息 | 设置安全连接期间的服务器身份验证配置。 | API version 18 |

## 发起HTTP数据请求

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

完整示例代码见：[Http\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case)

1. 导入HTTP一般数据请求所需模块

   ```
   1. import { http } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L16-L21)
2. 创建HttpRequest对象

   调用[createHttp()](../harmonyos-references/js-apis-http.md#httpcreatehttp)方法，创建HttpRequest对象。

   ```
   1. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   2. // 每一个httpRequest对应一个HTTP请求任务，不可复用。
   3. let httpRequest = http.createHttp();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L79-L83)
3. 订阅HTTP响应头事件

   调用该对象的[on()](../harmonyos-references/js-apis-http.md#onheadersreceive8)方法，订阅HTTP响应头事件，此接口会比request请求先返回。可以根据业务需要订阅此消息。

   ```
   1. // 用于订阅HTTP响应头，此接口会比request请求先返回。可以根据业务需要订阅此消息。
   2. // 从API 8开始，使用on('headersReceive', Callback)替代on('headerReceive', AsyncCallback)。
   3. httpRequest.on('headersReceive', (header) => {
   4. hilog.info(0x0000, 'testTag', `header: ${JSON.stringify(header)}`);
   5. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L85-L91)
4. 发起HTTP请求，解析服务器响应事件

   调用该对象的[request()](../harmonyos-references/js-apis-http.md#httprequest)方法，传入HTTP请求的url地址和可选参数，发起网络请求，按照实际业务需要，解析返回结果。

   ```
   1. httpRequest.request(
   2. // 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定
   3. 'EXAMPLE_URL',
   4. {
   5. method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET，用于从服务器获取数据，而POST方法用于向服务器上传数据。
   6. // 开发者根据自身业务需要添加header字段
   7. header: {
   8. 'Content-Type': 'application/json'
   9. },
   10. // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定
   11. extraData: 'data to send',
   12. expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型
   13. usingCache: true, // 可选，默认为true
   14. priority: 1, // 可选，默认为1
   15. connectTimeout: 60000, // 可选，默认为60000ms
   16. readTimeout: 60000, // 可选，默认为60000ms
   17. usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定
   18. usingProxy: false, // 可选，默认不使用网络代理，自API 10开始支持该属性
   19. caPath:'/path/to/cacert.pem', // 可选，默认使用系统预制证书，自API 10开始支持该属性
   20. clientCert: { // 可选，默认不使用客户端证书，自API 11开始支持该属性
   21. certPath: '/path/to/client.pem', // 默认不使用客户端证书，自API 11开始支持该属性
   22. keyPath: '/path/to/client.key', // 若证书包含Key信息，传入空字符串，自API 11开始支持该属性
   23. certType: http.CertType.PEM, // 可选，默认使用PEM，自API 11开始支持该属性
   24. keyPassword: 'passwordToKey' // 可选，输入key文件的密码，自API 11开始支持该属性
   25. },
   26. // 可选，仅当Header中，'content-Type'为'multipart/form-data'时生效,自API 11开始支持该属性
   27. // 该属性用于支持向服务器上传二进制数据，根据上传的具体数据类型进行选择。
   28. multiFormDataList: [
   29. {
   30. name: 'Part1', // 数据名，自API 11开始支持该属性
   31. contentType: 'text/plain', // 数据类型，自API 11开始支持该属性，上传的数据类型为普通文本文件。
   32. data: 'Example data', // 可选，数据内容，自API 11开始支持该属性
   33. remoteFileName: 'example.txt' // 可选，自API 11开始支持该属性
   34. }, {
   35. name: 'Part2', // 数据名，自API 11开始支持该属性
   36. contentType: 'text/plain', // 数据类型，自API 11开始支持该属性，上传的数据类型为普通文本文件。
   37. // data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.txt
   38. filePath: `${context.filesDir}/fileName.txt`, // 可选，传入文件路径，自API 11开始支持该属性
   39. remoteFileName: 'fileName.txt' // 可选，自API 11开始支持该属性
   40. }, {
   41. name: 'Part3', // 数据名，自API 11开始支持该属性。
   42. contentType: 'image/png', // 数据类型，自API 11开始支持该属性，上传的数据类型为png格式的图片。
   43. // data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.png。
   44. filePath: `${context.filesDir}/fileName.png`, // 可选，传入文件路径，自API 11开始支持该属性。
   45. remoteFileName: 'fileName.png' // 可选，自API 11开始支持该属性。
   46. }, {
   47. name: 'Part4', // 数据名，自API 11开始支持该属性。
   48. contentType: 'audio/mpeg', // 数据类型，自API 11开始支持该属性，上传的数据类型为mpeg格式的音频。
   49. // data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.mpeg。
   50. filePath: `${context.filesDir}/fileName.mpeg`, // 可选，传入文件路径，自API 11开始支持该属性。
   51. remoteFileName: 'fileName.mpeg' // 可选，自API 11开始支持该属性。
   52. }, {
   53. name: 'Part5', // 数据名，自API 11开始支持该属性。
   54. contentType: 'video/mp4', // 数据类型，自API 11开始支持该属性，上传的数据类型为mp4格式的视频。
   55. // data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.mp4。
   56. filePath: `${context.filesDir}/fileName.mp4`, // 可选，传入文件路径，自API 11开始支持该属性。
   57. remoteFileName: 'fileName.mp4' // 可选，自API 11开始支持该属性。
   58. }
   59. ]
   60. }, (err: BusinessError, data: http.HttpResponse) => {
   61. if (!err) {
   62. // ...
   63. // data.result为HTTP响应内容，可根据业务需要进行解析。
   64. hilog.info(0x0000, 'testTag', `Result: ${JSON.stringify(data.result)}`);
   65. hilog.info(0x0000, 'testTag', `code: ${JSON.stringify(data.responseCode)}`);
   66. // data.header为HTTP响应头，可根据业务需要进行解析。
   67. hilog.info(0x0000, 'testTag', `header: ${JSON.stringify(data.header)}`);
   68. hilog.info(0x0000, 'testTag', `cookies: ${JSON.stringify(data.cookies)}`);
   69. // 当该请求使用完毕时，调用destroy方法主动销毁。
   70. httpRequest.destroy();
   71. } else {
   72. // ...
   73. hilog.error(0x0000, 'testTag', `error: ${JSON.stringify(err)}`);
   74. // 取消订阅HTTP响应头事件
   75. httpRequest.off('headersReceive');
   76. // 当该请求使用完毕时，调用destroy方法主动销毁
   77. httpRequest.destroy();
   78. }
   79. }
   80. );
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L93-L189)
5. 取消订阅HTTP响应头事件

   调用该对象的[off()](../harmonyos-references/js-apis-http.md#offheadersreceive8)方法，取消订阅HTTP响应头事件。

   ```
   1. // 在不需要该回调信息时，需要取消订阅HTTP响应头事件，该方法调用的时机，可以参考步骤4中的示例代码。
   2. httpRequest.off('headersReceive');
   ```
6. 调用destroy()方法销毁

   当该请求使用完毕时，调用[destroy()](../harmonyos-references/js-apis-http.md#destroy)方法销毁。

   ```
   1. // 当该请求使用完毕时，调用destroy方法主动销毁，该方法调用的时机，可以参考步骤4中的示例代码。
   2. httpRequest.destroy();
   ```

## 发起HTTP流式传输请求

HTTP流式传输是指在处理HTTP响应时，可以一次只处理响应内容的一小部分，而不是一次性将整个响应加载到内存，这对于处理大文件、实时数据流等场景非常有用。

完整示例代码见：[Http\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case)

1. 导入HTTP流式传输所需模块

   ```
   1. import { http } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L16-L21)
2. 创建HTTP流式传输HttpRequest对象

   调用[createHttp()](../harmonyos-references/js-apis-http.md#httpcreatehttp)方法，创建HttpRequest对象。

   ```
   1. // 每一个httpRequest对应一个HTTP请求任务，不可复用。
   2. let httpRequest = http.createHttp();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L198-L201)
3. 按需订阅HTTP流式响应事件

   服务器响应的数据在dataReceive回调中返回，可通过订阅该信息获取服务器响应的数据，其他流式响应事件可按需进行订阅。

   ```
   1. // 用于订阅HTTP流式响应数据接收事件。
   2. let res = new ArrayBuffer(0);
   3. // ...
   4. // 订阅HTTP流式响应数据接收事件
   5. httpRequest.on('dataReceive', (data: ArrayBuffer) => {
   6. const newRes = new ArrayBuffer(res.byteLength + data.byteLength);
   7. const resView = new Uint8Array(newRes);
   8. resView.set(new Uint8Array(res));
   9. resView.set(new Uint8Array(data), res.byteLength);
   10. res = newRes;
   11. hilog.info(0x0000, 'testTag', `res length: ${res.byteLength}`);
   12. });

   14. // 用于订阅HTTP流式响应数据接收完毕事件。
   15. httpRequest.on('dataEnd', () => {
   16. hilog.info(0x0000, 'testTag', `No more data in response, data receive end`);
   17. });

   19. // 订阅HTTP流式响应数据接收进度事件，下载服务器的数据时，可以通过该回调获取数据下载进度。
   20. httpRequest.on('dataReceiveProgress', (data: http.DataReceiveProgressInfo) => {
   21. hilog.info(0x0000, 'testTag', 'dataReceiveProgress receiveSize:' + data.receiveSize + ', totalSize:' + data.totalSize);
   22. });

   24. // 订阅HTTP流式响应数据发送进度事件，向服务器上传数据时，可以通过该回调获取数据上传进度。
   25. httpRequest.on('dataSendProgress', (data: http.DataSendProgressInfo) => {
   26. hilog.info(0x0000, 'testTag', 'dataSendProgress receiveSize:' + data.sendSize + ', totalSize:' + data.totalSize);
   27. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L203-L236)
4. 发起HTTP流式请求，获取服务端数据

   ```
   1. let streamInfo: http.HttpRequestOptions = {
   2. method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET，用于向服务器获取数据，而POST方法用于向服务器上传数据。
   3. // 开发者根据自身业务需要添加header字段。
   4. header: {
   5. 'Content-Type': 'application/json'
   6. },
   7. // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
   8. extraData: 'data to send', // 请求体内容
   9. expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
   10. usingCache: true,  // 可选，默认为true。
   11. priority: 1, // 可选，默认为1。
   12. connectTimeout: 60000, // 可选，默认为60000ms。
   13. readTimeout: 60000, // 可选，默认为60000ms。若传输的数据较大，需要较长的时间，建议增大该参数以保证数据传输正常终止。
   14. usingProtocol: http.HttpProtocol.HTTP1_1 // 可选，协议类型默认值由系统自动指定。
   15. };

   17. // 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定。
   18. httpRequest.requestInStream('EXAMPLE_URL', streamInfo)
   19. .then((data: number) => {
   20. // ...
   21. hilog.info(0x0000, 'testTag', `requestInStream OK!`);
   22. hilog.info(0x0000, 'testTag', `ResponseCode : ${JSON.stringify(data)}`);
   23. // 取消订阅步骤3中订阅的事件，并调用destroy方法主动销毁。
   24. this.destroyRequest(httpRequest);
   25. // ...
   26. }).catch((err: Error) => {
   27. // ...
   28. hilog.error(0x0000, 'testTag', `requestInStream ERROR : err = ${JSON.stringify(err)}`);
   29. // 取消订阅步骤3中订阅的事件，并调用destroy方法主动销毁。
   30. this.destroyRequest(httpRequest);
   31. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L238-L287)
5. 取消步骤3中订阅HTTP流式响应事件，并调用destroy()方法销毁流式HTTP请求

   调用该对象的[off()](../harmonyos-references/js-apis-http.md#offdatareceive10)方法，取消订阅步骤3中的事件，并且当该请求使用完毕时，调用[destroy()](../harmonyos-references/js-apis-http.md#destroy)方法销毁，该方法调用的时机，可以参考步骤4中的示例代码。

   ```
   1. public destroyRequest(httpRequest: http.HttpRequest) {
   2. // 取消订阅HTTP流式响应数据接收事件。
   3. httpRequest.off('dataReceive');
   4. // 取消订阅HTTP流式响应数据发送进度事件。
   5. httpRequest.off('dataSendProgress');
   6. // 取消订阅HTTP流式响应数据接收进度事件。
   7. httpRequest.off('dataReceiveProgress');
   8. // 取消订阅HTTP流式响应数据接收完毕事件。
   9. httpRequest.off('dataEnd');
   10. // 当该请求使用完毕时，调用destroy方法主动销毁。
   11. httpRequest.destroy();
   12. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case/entry/src/main/ets/pages/Index.ets#L291-L287)

## 通过HTTP发起WebDAV请求

从API version 23开始，HTTP请求支持WebDAV协议的文件访问，WebDAV是基于HTTP协议的扩展，支持对远程服务器上的文件进行创建、读取、更新、删除、移动、复制(MKCOL、GET、PUT、DELETE、MOVE、COPY)等操作。

完整示例代码见：[Http\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_case)

```
1. import { http } from '@kit.NetworkKit';
2. import { ComponentId } from '../common/CommonConstant';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. proppatchXml = `example_proppatchXml`; // 修改资源Xml
9. lockXml: string = `example_lockXml`; // 加锁Xml
10. lockToken: string = '';

12. build() {
13. Column({ space: 5 }) {
14. Button($r('app.string.HTTP_WEBDAV_PUT'))
15. .id(ComponentId.HTTP_WEBDAV_PUT)
16. .onClick(async () => {
17. let httpRequest = http.createHttp();
18. let file = 'example';
19. httpRequest.request('EXAMPLE_URL' + 'example.txt',
20. {
21. expectDataType: http.HttpDataType.STRING,
22. extraData: file, // 上传文件内容
23. header: { 'Content-Type': 'text/plain; charset=utf-8', 'Content-Length': file.length.toString() },
24. customMethod: 'PUT' // WebDav协议PUT请求方式
25. },
26. (err: Error, data: http.HttpResponse) => {
27. if (!err) {
28. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
29. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
30. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
31. httpRequest.destroy();
32. } else {
33. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
34. httpRequest.destroy();
35. }
36. })
37. })

39. Button($r('app.string.HTTP_WEBDAV_GET'))
40. .id(ComponentId.HTTP_WEBDAV_GET)
41. .onClick(() => {
42. let httpRequest = http.createHttp();
43. httpRequest.request('EXAMPLE_URL' + 'example.txt',
44. {
45. expectDataType: http.HttpDataType.STRING,
46. customMethod: 'GET' // WebDav协议GET请求方式
47. },
48. (err: Error, data: http.HttpResponse) => {
49. if (!err) {
50. hilog.info(0x0000, 'testTag', 'Result:' + data.result.toString());
51. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
52. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
53. httpRequest.destroy();
54. } else {
55. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
56. httpRequest.destroy();
57. }
58. })
59. })

61. Button($r('app.string.HTTP_WEBDAV_MKCOL'))
62. .id(ComponentId.HTTP_WEBDAV_MKCOL)
63. .onClick(() => {
64. let httpRequest = http.createHttp();
65. httpRequest.request('EXAMPLE_URL' + 'example/',
66. {
67. expectDataType: http.HttpDataType.STRING,
68. customMethod: 'MKCOL' // WebDav协议MKCOL请求方式
69. },
70. (err: Error, data: http.HttpResponse) => {
71. if (!err) {
72. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
73. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
74. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
75. httpRequest.destroy();
76. } else {
77. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
78. httpRequest.destroy();
79. }
80. })
81. })

83. Button($r('app.string.HTTP_WEBDAV_DELETE'))
84. .id(ComponentId.HTTP_WEBDAV_DELETE)
85. .onClick(() => {
86. let httpRequest = http.createHttp();
87. httpRequest.request('EXAMPLE_URL' + 'example/',
88. {
89. expectDataType: http.HttpDataType.STRING,
90. header: { 'Content-Type': 'text/xml' },
91. customMethod: 'DELETE' // WebDav协议DELETE请求方式
92. },
93. (err: Error, data: http.HttpResponse) => {
94. if (!err) {
95. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
96. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
97. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
98. httpRequest.destroy();
99. } else {
100. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
101. httpRequest.destroy();
102. }
103. })
104. })

106. Button($r('app.string.HTTP_WEBDAV_COPY'))
107. .id(ComponentId.HTTP_WEBDAV_COPY)
108. .onClick(() => {
109. let httpRequest = http.createHttp();
110. httpRequest.request('EXAMPLE_URL' + 'example.txt',
111. {
112. expectDataType: http.HttpDataType.STRING,
113. header: { 'Destination': 'EXAMPLE_URL' + 'new_example.txt' },
114. customMethod: 'COPY' // WebDav协议COPY请求方式
115. },
116. (err: Error, data: http.HttpResponse) => {
117. if (!err) {
118. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
119. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
120. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
121. httpRequest.destroy();
122. } else {
123. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
124. httpRequest.destroy();
125. }
126. })
127. })

129. Button($r('app.string.HTTP_WEBDAV_MOVE'))
130. .id(ComponentId.HTTP_WEBDAV_MOVE)
131. .onClick(() => {
132. let httpRequest = http.createHttp();
133. httpRequest.request('EXAMPLE_URL' + 'example.txt',
134. {
135. expectDataType: http.HttpDataType.STRING,
136. header: { 'Destination': 'EXAMPLE_URL' + 'reNameText.txt' },
137. customMethod: 'MOVE' // WebDav协议MOVE请求方式
138. },
139. (err: Error, data: http.HttpResponse) => {
140. if (!err) {
141. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
142. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
143. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
144. httpRequest.destroy();
145. } else {
146. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
147. httpRequest.destroy();
148. }
149. })
150. })

152. Button($r('app.string.HTTP_WEBDAV_PROPPATCH'))
153. .id(ComponentId.HTTP_WEBDAV_PROPPATCH)
154. .onClick(() => {
155. let httpRequest = http.createHttp();
156. httpRequest.request('EXAMPLE_URL' + 'example.txt',
157. {
158. extraData: this.proppatchXml,
159. expectDataType: http.HttpDataType.STRING,
160. header: { 'Content-Type': 'application/xml; charset=utf-8', 'Depth': 'infinity' },
161. customMethod: 'PROPPATCH' // WebDav协议PROPPATCH请求方式
162. },
163. (err: Error, data: http.HttpResponse) => {
164. if (!err) {
165. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
166. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
167. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
168. httpRequest.destroy();
169. } else {
170. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
171. httpRequest.destroy();
172. }
173. })
174. })

176. Button($r('app.string.HTTP_WEBDAV_PROPFIND'))
177. .id(ComponentId.HTTP_WEBDAV_PROPFIND)
178. .onClick(() => {
179. let httpRequest = http.createHttp();
180. httpRequest.request('EXAMPLE_URL' + 'example.txt',
181. {
182. expectDataType: http.HttpDataType.STRING,
183. header: {
184. 'Content-Type': 'text/xml',
185. 'Depth': '0'
186. },
187. customMethod: 'PROPFIND' // WebDav协议PROPFIND请求方式
188. },
189. (err: Error, data: http.HttpResponse) => {
190. if (!err) {
191. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
192. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
193. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
194. httpRequest.destroy();
195. } else {
196. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
197. httpRequest.destroy();
198. }
199. })
200. })

202. Button($r('app.string.HTTP_WEBDAV_LOCK'))
203. .id(ComponentId.HTTP_WEBDAV_LOCK)
204. .onClick(() => {
205. let httpRequest = http.createHttp();
206. httpRequest.request('EXAMPLE_URL' + 'example.txt',
207. {
208. extraData: this.lockXml,
209. expectDataType: http.HttpDataType.STRING,
210. header: {
211. 'Content-Type': 'application/xml',
212. 'Depth': '0',
213. },
214. customMethod: 'LOCK' // WebDav协议LOCK请求方式
215. },
216. (err: Error, data: http.HttpResponse) => {
217. if (!err) {
218. let lockTokenRegex = /<D:href>(urn:uuid:[a-fA-F0-9\-]+)<\/D:href>/;
219. let statusMatch: RegExpMatchArray | null = (data.result as string).match(lockTokenRegex);
220. if (statusMatch) {
221. this.lockToken = statusMatch[1];
222. }
223. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
224. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
225. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
226. hilog.info(0x0000, 'testTag', 'lockToken:' + this.lockToken);
227. httpRequest.destroy();
228. } else {
229. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
230. httpRequest.destroy();
231. }
232. })
233. })

235. Button($r('app.string.HTTP_WEBDAV_UNLOCK'))
236. .id(ComponentId.HTTP_WEBDAV_UNLOCK)
237. .onClick(() => {
238. let httpRequest = http.createHttp();
239. httpRequest.request('EXAMPLE_URL' + 'example.txt',
240. {
241. header: {
242. 'Content-Length': '0',
243. 'Lock-Token': this.lockToken, // 加锁时返回密钥
244. 'Depth': '0'
245. },
246. customMethod: 'UNLOCK' // WebDav协议UNLOCK请求方式
247. },
248. (err: Error, data: http.HttpResponse) => {
249. if (!err) {
250. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
251. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
252. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
253. httpRequest.destroy();
254. } else {
255. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
256. httpRequest.destroy();
257. }
258. })
259. })

261. Button($r('app.string.HTTP_WEBDAV_UNKNOWN'))
262. .id(ComponentId.HTTP_WEBDAV_UNKNOWN)
263. .onClick(() => {
264. let httpRequest = http.createHttp();
265. httpRequest.request('EXAMPLE_URL',
266. {
267. customMethod: 'UNKNOWN' // 非WebDav协议请求方式
268. },
269. (err: Error, data: http.HttpResponse) => {
270. if (!err) {
271. hilog.info(0x0000, 'testTag', 'Result:' + data.result);
272. hilog.info(0x0000, 'testTag', 'code:' + data.responseCode);
273. hilog.info(0x0000, 'testTag', 'header:' + JSON.stringify(data.header));
274. httpRequest.destroy();
275. } else {
276. hilog.error(0x0000, 'testTag', 'error:' + JSON.stringify(err));
277. httpRequest.destroy();
278. }
279. })
280. })
281. }
282. .width('100%')
283. .height('100%')
284. .justifyContent(FlexAlign.Center)
285. }
286. }
```

## 配置证书校验

当应用使用HTTPS协议时，涉及证书相关配置。面向互联网用户提供服务的应用仅需信任系统预置的CA证书。当前HTTP模块已默认信任系统预置的CA证书，无需特别设置。如果应用需要锁定证书，只信任开发者特别指定的证书，或者需要跳过证书校验，可以参考以下说明进行配置。

### TLS客户端证书验证流程

在TLS握手过程中，客户端验证服务端证书以确保连接可信。服务端证书通常包括域名证书和中间CA证书。

**证书链组成**

证书链采用层级信任结构：服务端证书 ← 中间CA证书 ← 根CA证书。其中←表示签发与信任关系，证书链必须完整追溯到可信根证书。

**验证流程**

客户端接收证书链后执行三级验证：

1. 证书链完整性验证

   * 从服务端证书开始逐级验证数字签名，确保每一级证书均由上一级有效签发，以形成完整的信任链条。
2. 根证书可信性验证

   * 在证书存储库中查找根证书是否存在。
   * 存储库来源包括：
     + 系统预置证书。
     + 应用信任证书。
     + 本次请求指定的CA证书。
   * 可通过相关API(请参考下方：**配置参考**)指定应用级和请求级信任证书。
3. 证书内容有效性验证

   * 证书有效期检查。
   * 域名匹配验证：主题备用名称(Subject Alternative Name, SAN)、通用名称(Common Name, CN)与访问域名一致。
   * 证书吊销状态检查：证书吊销列表(Certificate Revocation List, CRL)、在线证书状态协议(Online Certificate Status Protocol, OCSP)。

验证结果

* 验证成功：继续TLS握手建立安全连接。
* 验证失败：终止连接并提示错误信息。

此流程确保只有持有有效且可信证书的服务端才能建立安全连接。

**配置参考**

1. 配置应用信任证书（具体配置方法可参考[网络连接安全配置](../best-practices/bpta-network-ca-security.md#section5454123841911)）。
2. 配置请求级CA证书：
   * 通过[httprequestoptions](../harmonyos-references/js-apis-http.md#httprequestoptions)的caPath和caData字段配置HTTPS请求CA证书。
   * 通过[websocketrequestoptions](../harmonyos-references/js-apis-websocket.md#websocketrequestoptions)的caPath字段配置WebSocket请求CA证书。
   * 通过[tlssecureoptions](../harmonyos-references/js-apis-socket.md#tlssecureoptions9)的ca字段指定TLS请求CA证书。
3. 配置跳过证书校验：
   * HTTPS：通过[remoteValidation](../harmonyos-references/js-apis-http.md#remotevalidation18) = 'skip' 配置。
   * WebSocket：通过[websocketrequestoptions](../harmonyos-references/js-apis-websocket.md#websocketrequestoptions)的skipServerCertVerification = false 配置。
   * TLSSocket：通过[tlsconnectoptions](../harmonyos-references/js-apis-socket.md#tlsconnectoptions9)的skipRemoteValidation = false 配置。

**调试参考**

* 通过API校验指定证书是否可信：可参考[networkSecurity.certVerification](../harmonyos-references/js-apis-networksecurity.md#networksecuritycertverification)。
* 通过openssl命令校验域名服务器证书链是否被系统信任：hdc shell openssl s\_client -connect 主机名:端口 -CApath /etc/security/certificates -brief。若出现Verification: OK说明证书链可信。将-trace -showcerts替换为-brief可以打印详细的TLS握手信息。

### 证书锁定

可以通过预置应用级证书，或者预置证书公钥哈希值的方式来进行证书锁定，即只有开发者特别指定的证书才能正常建立HTTPS连接。

两种方式都是在配置文件中配置的，配置文件在APP中的路径是：src/main/resources/base/profile/network\_config.json。在该配置中，可以为预置的证书与网络服务器建立对应关系。

如果不知道服务器域名的证书，可以通过以下方式访问该域名获取证书，注意把www.example.com改成想要获取域名证书的域名，www.example.com.pem改成想保存的证书文件名：

```
1. openssl s_client -servername www.example.com -connect www.example.com:443 \
2. < /dev/null | sed -n "/-----BEGIN/,/-----END/p" > www.example.com.pem
```

如果你的环境是Windows系统，需要注意：

* 将/dev/null替换成NUL。
* 和Linux的OpenSSL表现可能不同，OpenSSL可能会等待用户输入才会退出，按Enter键即可。
* 如果没有sed命令，将输出中从-----BEGIN CERTIFICATE-----到-----END CERTIFICATE-----之间的部分复制下来保存即可（复制部分包括这两行）。

**预置应用级证书**

直接把证书原文件预置在APP中。目前支持crt和pem格式的证书文件。

注意

当前ohos.net.http和Image组件的证书锁定，会匹配证书链上所有证书的哈希值，如果服务器更新了任意一本证书，都会导致校验失败。如果服务器出现了更新证书的情况，APP版本应当随之更新并推荐消费者尽快升级APP版本，否则可能导致联网失败。

**预置证书公钥哈希值**

通过在配置中指定域名证书公钥的哈希值，只允许使用公钥哈希值匹配的域名证书访问此域名。

域名证书的公钥哈希值可以用如下的命令计算。假设域名证书是通过上面的OpenSSL命令获得的，并保存在www.example.com.pem文件。#开头的行是注释，可以不用输入：

```
1. # 从证书中提取出公钥
2. openssl x509 -in www.example.com.pem -pubkey -noout > www.example.com.pubkey.pem
3. # 将pem格式的公钥转换成der格式
4. openssl asn1parse -noout -inform pem -in www.example.com.pubkey.pem -out www.example.com.pubkey.der
5. # 计算公钥的SHA256并转换成base64编码
6. openssl dgst -sha256 -binary www.example.com.pubkey.der | openssl base64
```

**JSON配置文件示例**

预置应用级证书的配置例子如下（具体配置路径可参考[网络连接安全配置](../best-practices/bpta-network-ca-security.md#section5454123841911)）：

```
1. {
2. "network-security-config": {
3. "base-config": {
4. "trust-anchors": [
5. {
6. "certificates": "/etc/security/certificates"
7. }
8. ]
9. },
10. "domain-config": [
11. {
12. "domains": [
13. {
14. "include-subdomains": true,
15. "name": "example.com"
16. }
17. ],
18. "trust-anchors": [
19. {
20. "certificates": "/data/storage/el1/bundle/entry/resources/resfile"
21. }
22. ]
23. }
24. ]
25. }
26. }
```

预置证书公钥哈希值的配置例子如下：

```
1. {
2. "network-security-config": {
3. "domain-config": [
4. {
5. "domains": [
6. {
7. "include-subdomains": true,
8. "name": "*.server.com"
9. }
10. ],
11. "pin-set": {
12. "expiration": "2024-11-08",
13. "pin": [
14. {
15. "digest-algorithm": "sha256",
16. "digest": "FEDCBA987654321"
17. }
18. ]
19. }
20. }
21. ]
22. }
23. }
```

证书锁定的配置例子如下:

```
1. {
2. "network-security-config": {
3. "domain-config": [
4. {
5. "domains": [
6. {
7. "include-subdomains": true,
8. "name": "*.server.com"
9. }
10. ],
11. "pin-set": {
12. "expiration": "2024-11-08",
13. "pin": [
14. {
15. "digest-algorithm": "sha256",
16. "digest": "FEDCBA987654321"
17. }
18. ]
19. }
20. }
21. ]
22. },
23. "trust-global-user-ca": false,
24. "trust-current-user-ca": false,
25. }
```

**各个字段含义:**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| network-security-config | object | 网络安全配置。可包含0或者1个base-config，必须包含1个domain-config。 |
| base-config | object | 指示应用程序范围的安全配置。必须包含1个trust-anchors。 |
| domain-config | array | 指示每个域的安全配置。可以包含任意个item。item必须包含1个domains，可以包含0或者1个trust-anchors，可以包含0个或者1个pin-set。 |
| trust-anchors | array | 受信任的CA。可以包含任意个item。item必须包含1个certificates。 |
| certificates | string | CA证书路径。 |
| domains | array | 域。可以包含任意个item。item必须包含1个name(string：指示域名)，可以包含0或者1个include-subdomains。 |
| include-subdomains | boolean | 指示规则是否适用于子域。true：指示规则适用于子域；false：指示规则不适用于子域。 |
| pin-set | object | 证书公钥哈希设置。必须包含1个pin，可以包含0或者1个expiration。 |
| expiration | string | 指示证书公钥哈希的过期时间。 |
| pin | array | 证书公钥哈希。可以包含任意个item。item必须包含1个digest-algorithm，item必须包含1个digest。 |
| digest-algorithm | string | 指示用于生成哈希的摘要算法。目前只支持sha256。 |
| digest | string | 指示公钥哈希。 |

### 配置不信任用户安装的CA证书

系统默认信任系统预置的CA证书和用户安装的CA证书，可配置不信任用户安装的CA证书提升安全性。配置不信任用户安装的CA证书可以在src/main/resources/base/profile/network\_config.json进行配置，更多网络连接安全相关的配置可以参考[网络连接安全配置](../best-practices/bpta-network-ca-security.md#section5454123841911)。

```
1. {
2. "network-security-config": {
3. ... ...
4. },
5. "trust-global-user-ca": false, // 配置是否信任企业MDM系统或设备管理员用户手动安装的CA证书，默认为true
6. "trust-current-user-ca" : false // 配置是否信任当前用户安装的CA证书，默认为true
7. }
```

### 明文HTTP访问权限配置说明

该配置用于控制HTTP请求是否允许以明文形式传输。以下为明文HTTP访问权限的配置示例（含应用、组件及域名级配置），以及各字段的详细含义说明。更多网络连接安全相关的配置可以参考[网络连接安全配置](../best-practices/bpta-network-ca-security.md#section5454123841911)。

说明

配置优先级规则：组件配置（component-config）> 域名配置（domain-config）> 基础配置（base-config），优先级高的配置会覆盖优先级低的规则。

```
1. // src/main/resources/base/profile/network_config.json
2. {
3. "network-security-config": {
4. "base-config": {
5. "cleartextTrafficPermitted": true // 可选，自API version 20开始支持该属性。
6. },
7. "domain-config": [
8. {
9. "domains": [
10. {
11. "include-subdomains": true,
12. "name": "example.com"
13. }
14. ],
15. "cleartextTrafficPermitted": false // 可选，自API version 20开始支持该属性。
16. }
17. ],
18. "component-config": {
19. "Request": true // 可选，自API version 20开始支持配置该属性，默认值为true。配置为true表示支持禁止明文传输，false表示不支持禁止明文传输。
20. "Network Kit": true, // 可选，自API version 20开始支持配置该属性。
21. "ArkWeb": false // 可选，自API version 20开始支持配置该属性。
22. "Media Kit": false // 可选，自API version 23开始支持配置该属性。
23. "Remote Communication Kit": false // 可选，自API version 23开始支持配置该属性。
24. }
25. }
26. }
```

**各个字段含义:**

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| base-config | array | 否 | 指示应用程序范围的明文配置。优先级最低。 |
| cleartextTrafficPermitted18+ | boolean | 否 | 明文HTTP是否允许。true表示允许，false表示不允许，默认为true。 |
| domain-config | array | 否 | 指示每个域的明文配置。可以包含任意个item。每个item必须包含1个domains。若相同域存在规则冲突时，以匹配到的第一条为准。优先级次于component-config。 |
| include-subdomains | boolean | 否 | 配置为true时，name支持正则匹配。配置为false时，name不支持正则匹配。注意：每增加1000条域名配置，正则匹配的延迟将增加大约10至15毫秒。当域名配置数量超过10000条时，正则匹配会带来较高耗时。 |
| name | string | 否 | 配置主域名。 |
| component-config20+ | array | 否 | 指示每个组件的明文配置。优先级最高。 |
| Request | boolean | 否 | [Request](../harmonyos-references/js-apis-request.md)从API version 18开始默认支持明文HTTP功能，不可配置。从API version 20开始支持配置开启或关闭明文HTTP功能 。true表示支持，false表示不支持，默认为true。 |
| Network Kit | boolean | 否 | Network Kit从API version 18开始默认支持明文HTTP功能，不可配置。从API version 20开始支持配置开启或关闭明文HTTP功能。true表示支持，false表示不支持，默认为true。 |
| ArkWeb | boolean | 否 | ArkWeb从API version 20开始支持配置开启或关闭明文HTTP功能。true表示支持，false表示不支持，默认为false。 |
| Media Kit | boolean | 否 | Media Kit从API version 23开始支持配置开启或关闭明文HTTP功能。true表示支持，false表示不支持，默认为false。 |
| Remote Communication Kit | boolean | 否 | Remote Communication Kit从API version 23开始支持配置开启或关闭明文HTTP功能。true表示支持，false表示不支持，默认为false。 |

## HTTP拦截器

从API version 22开始，HTTP拦截器模块提供了一种强大且可定制的机制，允许开发者在"HTTP请求-响应"生命周期中的关键节点插入自定义逻辑。通过拦截器，开发者可以无需修改核心网络代码即可实现修改请求头/体、缓存策略、重定向处理、网络监控、响应预处理等全局功能。

### 拦截点说明

| 拦截点名称 | 位置说明 | 拦截点interceptorHandle接口的出参和入参 |
| --- | --- | --- |
| 初始请求拦截点（INITIAL\_REQUEST） | 初始请求组装完成后，这是第一个拦截点，适合用于添加全局参数、签名、加密请求体。 | 当出参为true时，此时入参中的request值为原始值，可以修改，response值为空值，修改无效。  当出参为false时，此时入参中的request值为原始值，修改无效，response值为空值，可以修改。 |
| 网络连接拦截点（CONNECT\_NETWORK） | 在网络连接建立之前，例如TCP/TLS连接。适合进行网络链路相关的操作，如记录网络连接开始时间。 | 当出参为true时，此时入参中的request值为原始值，可以修改，response值为空值，修改无效。  当出参为false时，此时入参中的request值为原始值，修改无效，response值为空值，可以修改。 |
| 缓存拦截点（CACHE\_CHECKED） | 缓存检查逻辑命中缓存之后，已确认存在可用缓存。适用于查看缓存值或者修改查询到的缓存结果。 | 当出参为true时，此时入参中的request值为原始值，修改无效，response值为原始值，修改无效。  当出参为false时，此时入参中的request值为原始值，修改无效，response值为原始值，可以修改。 |
| 重定向拦截点（REDIRECTION） | 收到重定向响应并准备发送新请求之前。允许修改重定向的目标URL或请求信息。 | 当出参为true时，此时入参中的request值为原始值，可以修改URL，response值为原始值，修改无效。  当出参为false时，此时入参中的request值为原始值，修改无效，response值为原始值，可以修改。 |
| 最终响应拦截点（FINAL\_RESPONSE） | 获得最终响应之后。最后一个拦截点，适合对响应进行统一解密、解析、日志记录、错误处理。 | 当出参为true时，此时入参中的request值为原始值，修改无效，response值为原始值，修改无效。  当出参为false时，此时入参中的request值为原始值，修改无效，response值为原始值，可以修改。 |

**顺序执行**：拦截器严格按照INITIAL\_REQUEST->CACHE\_CHECKED->NETWORK\_CONNECT->(REDIRECTION)->FINAL\_RESPONSE的顺序被触发调用。（括号中表示如果请求涉及重定向，则会走重定向拦截器）

**重定向循环**：这是流程中最关键的一个循环。当REDIRECTION拦截器被触发后，流程会跳回到NETWORK\_CONNECT阶段，重新开始一个新的“请求周期”，直到不再发生重定向为止。这确保了重定向后的新请求也能被所有必要的拦截器（如认证头添加、日志记录等）正确处理。

**缓存拦截**：CACHE\_CHECKED是一个决策点。如果缓存存在且有效，请求会在此处经过CACHE\_CHECKED处理后，直接跳转到FINAL\_RESPONSE阶段返回缓存数据，从而避免不必要的网络操作。

### HTTP拦截器开发步骤

1. 导入HTTP请求拦截器所需模块。

   ```
   1. import { http } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L16-L20)
2. 调用[createHttp()](../harmonyos-references/js-apis-http.md#httpcreatehttp)方法，创建HttpRequest对象。

   ```
   1. // 创建http请求
   2. let httpRequest: http.HttpRequest = http.createHttp();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L132-L135)
3. 调用[HttpInterceptorChain()](../harmonyos-references/js-apis-http.md#httpinterceptorchain22)方法，创建拦截器链对象。

   ```
   1. // 创建拦截器链
   2. let chain: http.HttpInterceptorChain = new http.HttpInterceptorChain();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L137-L140)
4. 创建拦截器类实现http.HttpInterceptor接口。

   ```
   1. class InitialHttpInterceptor implements http.HttpInterceptor {
   2. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;
   3. result: boolean = false;

   5. constructor(interceptorType: http.InterceptorType, result: boolean) {
   6. this.interceptorType = interceptorType;
   7. this.result = result;
   8. }

   10. interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
   11. // 命中拦截器后对请求报文与请求响应操作
   12. hilog.info(0xFF00, 'httpNormalRequest', `INITIAL_REQUEST, Original req: ${JSON.stringify(reqContext)}`);
   13. hilog.info(0xFF00, 'httpNormalRequest', `INITIAL_REQUEST, Original rsp: ${JSON.stringify(rspContext)}`);

   15. reqContext.url = EXAMPLE_INITIAL_URL;
   16. reqContext.header = { 'content-type': 'text/plain' };
   17. reqContext.body = { 'context': 'INITIAL_REQUEST' };

   19. rspContext.result = 'INITIAL_REQUEST';
   20. rspContext.responseCode = 200;
   21. rspContext.header =
   22. 'content-encoding:br \r\n content-type:text/html\r\ncharset=UTF-8,cxy_all:+5c4ea5d1638626cbb796a7db10e0d663\r\ndate:Tue';

   24. hilog.info(0xFF00, 'httpNormalRequest', `INITIAL_REQUEST, Update req: ${JSON.stringify(reqContext)}`);
   25. hilog.info(0xFF00, 'httpNormalRequest', `INITIAL_REQUEST, Update rsp: ${JSON.stringify(rspContext)}`);
   26. return Promise.resolve(this.result);
   27. }
   28. }

   30. class NetworkHttpInterceptor implements http.HttpInterceptor {
   31. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;
   32. result: boolean = false;

   34. constructor(interceptorType: http.InterceptorType, result: boolean) {
   35. this.interceptorType = interceptorType;
   36. this.result = result;
   37. }

   39. interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
   40. // 命中拦截器后对请求报文与请求响应操作
   41. hilog.info(0xFF00, 'httpNormalRequest', `NETWORK_CONNECT, Original req: ${JSON.stringify(reqContext)}`);
   42. hilog.info(0xFF00, 'httpNormalRequest', `NETWORK_CONNECT, Original rsp: ${JSON.stringify(rspContext)}`);

   44. reqContext.url = EXAMPLE_URL;
   45. reqContext.header = { 'content-type': 'text/xml' };
   46. reqContext.body = { 'context': 'NETWORK_CONNECT' };

   48. rspContext.result = 'NETWORK_CONNECT';
   49. rspContext.responseCode = 300;
   50. rspContext.header =
   51. 'content-encoding:br \r\n content-type:text/html\r\ncharset=UTF-8,cxy_all:+5c4ea5d1638626cbb796a7db10e0d663\r\ndate:Tue';

   53. hilog.info(0xFF00, 'httpNormalRequest', `NETWORK_CONNECT, Update req: ${JSON.stringify(reqContext)}`);
   54. hilog.info(0xFF00, 'httpNormalRequest', `NETWORK_CONNECT, Update rsp: ${JSON.stringify(rspContext)}`);
   55. return Promise.resolve(this.result);
   56. }
   57. }

   59. class FinalHttpInterceptor implements http.HttpInterceptor {
   60. interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;
   61. result: boolean = false;

   63. constructor(interceptorType: http.InterceptorType, result: boolean) {
   64. this.interceptorType = interceptorType;
   65. this.result = result;
   66. }

   68. interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
   69. // 命中拦截器后对请求报文与请求响应操作
   70. hilog.info(0xFF00, 'httpNormalRequest', `FINAL_RESPONSE, Original req: ${JSON.stringify(reqContext)}`);
   71. hilog.info(0xFF00, 'httpNormalRequest', `FINAL_RESPONSE, Original rsp: ${JSON.stringify(rspContext)}`);

   73. reqContext.url = EXAMPLE_Final_URL;
   74. reqContext.header = { 'content-type': 'text/html' };
   75. reqContext.body = { 'context': 'FINAL_RESPONSE' };

   77. rspContext.result = 'FINAL_RESPONSE';
   78. rspContext.responseCode = 200;
   79. rspContext.header =
   80. 'content-encoding:br \r\n content-type:text/html\r\ncharset=UTF-8,cxy_all:+5c4ea5d1638626cbb796a7db10e0d663\r\ndate:Tue';

   82. hilog.info(0xFF00, 'httpNormalRequest', `FINAL_RESPONSE, Update req: ${JSON.stringify(reqContext)}`);
   83. hilog.info(0xFF00, 'httpNormalRequest', `FINAL_RESPONSE, Update rsp: ${JSON.stringify(rspContext)}`);
   84. return Promise.resolve(this.result);
   85. }
   86. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L32-L128)
5. 调用[addChain()](../harmonyos-references/js-apis-http.md#addchain22)方法，将需要的拦截器实例加入到拦截器链中。

   ```
   1. // 创建所需要的拦截器对象,将拦截器对象加入拦截器链中
   2. chain.addChain([
   3. new InitialHttpInterceptor(http.InterceptorType.INITIAL_REQUEST, true),
   4. new NetworkHttpInterceptor(http.InterceptorType.NETWORK_CONNECT, true),
   5. new FinalHttpInterceptor(http.InterceptorType.FINAL_RESPONSE, true)
   6. ]);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L142-L149)
6. 调用[apply()](../harmonyos-references/js-apis-http.md#apply22)方法，将当前配置好的拦截器链附加到httpRequest中。

   ```
   1. // 将当前配置好的拦截器链附加到httpRequest中
   2. chain.apply(httpRequest);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L151-L154)
7. 创建请求可选项。

   ```
   1. // 创建请求可选项
   2. let options: http.HttpRequestOptions = {
   3. method: http.RequestMethod.POST,
   4. header: { 'content-type': 'text/html' } as Record<string, string>,
   5. extraData: { 'context': 'BODY' } as Record<string, string>,
   6. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L156-L163)
8. 调用该对象的[request()](../harmonyos-references/js-apis-http.md#request-1)方法，传入HTTP请求的URL地址和可选参数，发起网络请求，按照实际业务需要，解析服务器响应事件。

   ```
   1. // 发起请求
   2. httpRequest.request(EXAMPLE_URL, options, (err: BusinessError, res: http.HttpResponse) => {
   3. if (err) {
   4. hilog.error(0xFF00, 'httpNormalRequest', `request fail, error code: ${err.code}, msg: ${err.message}`);
   5. // ...
   6. } else {
   7. hilog.info(0xFF00, 'httpNormalRequest', `res:${JSON.stringify(res)}`);
   8. // ...
   9. }
   10. // ...
   11. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L165-L194)
9. 调用[destroy()](../harmonyos-references/js-apis-http.md#destroy)方法销毁http请求。

   ```
   1. // 销毁请求
   2. httpRequest.destroy();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/HTTP_interceptor_case/entry/src/main/ets/pages/Index.ets#L188-L191)
