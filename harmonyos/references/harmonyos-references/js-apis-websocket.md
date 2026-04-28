---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket
title: @ohos.net.webSocket (WebSocket连接)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.webSocket (WebSocket连接)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed5bb28d1dbba8f8cf889ec2a69ac62f413d116d68db64284abc746598eca5d3
---

给第三方应用提供webSocket客户端和服务端服务器，实现客户端与服务端的双向连接。

客户端：使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocket](js-apis-websocket.md#websocketcreatewebsocket)方法创建[WebSocket](js-apis-websocket.md#websocket)对象，然后通过[connect](js-apis-websocket.md#connect)方法连接到服务器。当连接成功后，客户端会收到[open](js-apis-websocket.md#onopen)事件的回调，之后客户端就可以通过[send](js-apis-websocket.md#send)方法与服务器进行通信。当服务器发信息给客户端时，客户端会收到[message](js-apis-websocket.md#onmessage)事件的回调。当客户端想要取消此连接时，通过调用[close](js-apis-websocket.md#close)方法主动断开连接后，客户端会收到[close](js-apis-websocket.md#onclose)事件的回调。若在上述任一过程中发生错误，客户端会收到[error](js-apis-websocket.md#onerror)事件的回调。

服务端：（从API version 23开始支持全设备使用，之前仅支持TV设备使用）使用WebSocket建立服务器与客户端的双向连接，需要先通过[createWebSocketServer](js-apis-websocket.md#websocketcreatewebsocketserver19)方法创建[WebSocketServer](js-apis-websocket.md#websocketserver19)对象，然后通过[start](js-apis-websocket.md#start19)方法启动服务器，监听客户端的申请建链的消息。当连接成功后，服务端会收到[connect](js-apis-websocket.md#onconnect19)事件的回调，之后服务端可以通过[send](js-apis-websocket.md#send19)方法与客户端进行通信，或者通过[listAllConnections](js-apis-websocket.md#listallconnections19)方法列举出当前与服务端建链的所有客户端信息。当客户端给服务端发消息时，服务端会收到[messageReceive](js-apis-websocket.md#onmessagereceive19)事件回调。当服务端想断开与某个客户端的连接时，可以通过调用[close](js-apis-websocket.md#close19)方法主动断开与某个客户端的连接，之后服务端会收到[close](js-apis-websocket.md#onclose19)事件的回调。当服务端想停止service时，可以调用[stop](js-apis-websocket.md#stop19)方法。若在上述任一过程中发生错误，服务端会收到[error](js-apis-websocket.md#onerror19)事件的回调。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webSocket } from '@kit.NetworkKit';
```

## webSocket.createWebSocket

PhonePC/2in1TabletTVWearable

createWebSocket(): WebSocket

创建一个WebSocket对象，里面包括建立连接、关闭连接、发送数据和订阅/取消订阅WebSocket连接的打开事件、接收到服务器消息事件、关闭事件和错误事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSocket](js-apis-websocket.md#websocket) | 返回一个WebSocket对象，里面包括connect、send、close、on和off方法。 |

**示例：**

```
1. let ws: webSocket.WebSocket = webSocket.createWebSocket();
```

## WebSocket

PhonePC/2in1TabletTVWearable

在调用WebSocket的方法前，需要先通过[webSocket.createWebSocket](js-apis-websocket.md#websocketcreatewebsocket)创建一个WebSocket。

### connect

PhonePC/2in1TabletTVWearable

connect(url: string, callback: AsyncCallback<boolean>): void

根据URL地址，建立一个WebSocket连接，使用callback异步回调。

说明

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](js-apis-websocket.md#onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

注意

URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 建立WebSocket连接的URL地址。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:连接请求创建成功；false:连接请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](errorcode-net-websocket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. let url = "ws://";
6. ws.connect(url, (err: BusinessError, value: boolean) => {
7. if (!err) {
8. console.info("connect success")
9. } else {
10. console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
11. }
12. });
```

### connect

PhonePC/2in1TabletTVWearable

connect(url: string, options: WebSocketRequestOptions, callback: AsyncCallback<boolean>): void

根据URL地址，建立一个WebSocket连接，使用callback异步回调。

说明

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](js-apis-websocket.md#onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

注意

URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 建立WebSocket连接的URL地址。 |
| options | WebSocketRequestOptions | 是 | 参考[WebSocketRequestOptions](js-apis-websocket.md#websocketrequestoptions)。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:连接请求创建成功；false:连接请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](errorcode-net-websocket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. let options: webSocket.WebSocketRequestOptions | undefined;
6. if (options !=undefined) {
7. options.header = {
8. name1: "value1",
9. name2: "value2",
10. name3: "value3"
11. };
12. options.caPath = "";
13. }
14. let url = "ws://"
15. ws.connect(url, options, (err: BusinessError, value: Object) => {
16. if (!err) {
17. console.info("connect success")
18. } else {
19. console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
20. }
21. });
```

### connect

PhonePC/2in1TabletTVWearable

connect(url: string, options?: WebSocketRequestOptions): Promise<boolean>

根据URL地址和header，建立一个WebSocket连接。使用Promise异步回调。

说明

callback中返回的boolean值仅表示连接请求创建是否成功。如需感知WebSocket是否连接成功，需要在调用该接口前调用[on('open')](js-apis-websocket.md#onopen)订阅open事件。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

注意

URL地址长度不能超过1024个字符，否则会连接失败。从API version 15开始，URL地址长度限制由1024修改为2048。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 建立WebSocket连接的URL地址。 |
| options | WebSocketRequestOptions | 否 | 参考[WebSocketRequestOptions](js-apis-websocket.md#websocketrequestoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 回调函数。true:连接请求创建成功；false:连接请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[webSocket错误码](errorcode-net-websocket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2302001 | Websocket url error. |
| 2302002 | Websocket certificate file does not exist. |
| 2302003 | Websocket connection already exists. |
| 2302998 | It is not allowed to access this domain. |
| 2302999 | Internal error. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. let url = "ws://"
5. let promise = ws.connect(url);
6. promise.then((value: boolean) => {
7. console.info("connect success")
8. }).catch((err:string) => {
9. console.error("connect fail, error:" + JSON.stringify(err))
10. });
```

### send

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer, callback: AsyncCallback<boolean>): void

通过WebSocket连接发送数据，使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | 发送的数据。  API 6及更早版本仅支持string类型。API 8起同时支持string和ArrayBuffer类型。最大支持发送5242864字节数据(即5 \* 1024 \* 1024 - 16)，超过该大小会返回401错误码。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:发送请求创建成功；false:发送请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. let url = "ws://"
6. class OutValue {
7. status: number = 0
8. message: string = ""
9. }
10. ws.connect(url, (err: BusinessError, value: boolean) => {
11. if (!err) {
12. console.info("connect success")
13. } else {
14. console.error(`connect fail. Code: ${err.code}, message: ${err.message}`)
15. }
16. });
17. ws.on('open', (err: BusinessError, value: Object) => {
18. console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
19. ws.send("Hello, server!", (err: BusinessError, value: boolean) => {
20. if (!err) {
21. console.info("send success")
22. } else {
23. console.error(`send fail. Code: ${err.code}, message: ${err.message}`)
24. }
25. });
26. });
```

说明

send接口必须在监听到open事件后才可以调用。

### send

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer): Promise<boolean>

通过WebSocket连接发送数据。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | 发送的数据。  API 6及更早版本仅支持string类型。API 8起同时支持string和ArrayBuffer类型。最大支持发送5242864字节数据(即5 \* 1024 \* 1024 - 16)，超过该大小会返回401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回发送数据的结果。true:发送请求创建成功；false:发送请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. let url = "ws://"
6. class OutValue {
7. status: number = 0
8. message: string = ""
9. }
10. ws.connect(url, (err: BusinessError, value: boolean) => {
11. if (!err) {
12. console.info("connect success")
13. } else {
14. console.error("connect fail. Code: ${err.code}, message: ${err.message}")
15. }
16. });

18. ws.on('open', (err: BusinessError, value: Object) => {
19. console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
20. let promise = ws.send("Hello, server!");
21. promise.then((value: boolean) => {
22. console.info("send success")
23. }).catch((err:string) => {
24. console.error("send fail, error:" + JSON.stringify(err))
25. });
26. });
```

说明

send接口必须在监听到open事件后才可以调用。

### close

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<boolean>): void

关闭WebSocket连接，使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:关闭请求创建成功；false:关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. ws.close((err: BusinessError) => {
6. if (!err) {
7. console.info("close success")
8. } else {
9. console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
10. }
11. });
```

### close

PhonePC/2in1TabletTVWearable

close(options: WebSocketCloseOptions, callback: AsyncCallback<boolean>): void

根据参数options，关闭WebSocket连接，使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | WebSocketCloseOptions | 是 | 参考[WebSocketCloseOptions](js-apis-websocket.md#websocketcloseoptions)。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。true:关闭请求创建成功；false:关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();

6. let options: webSocket.WebSocketCloseOptions | undefined;
7. if (options != undefined) {
8. options.code = 1000
9. options.reason = "your reason"
10. }
11. ws.close(options, (err: BusinessError) => {
12. if (!err) {
13. console.info("close success")
14. } else {
15. console.error(`close fail. Code: ${err.code}, message: ${err.message}`)
16. }
17. });
```

### close

PhonePC/2in1TabletTVWearable

close(options?: WebSocketCloseOptions): Promise<boolean>

根据可选参数code和reason，关闭WebSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | WebSocketCloseOptions | 否 | 参考[WebSocketCloseOptions](js-apis-websocket.md#websocketcloseoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回关闭连接的结果。true:关闭请求创建成功；false:关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. let options: webSocket.WebSocketCloseOptions | undefined;
5. if (options != undefined) {
6. options.code = 1000
7. options.reason = "your reason"
8. }
9. let promise = ws.close();
10. promise.then((value: boolean) => {
11. console.info("close success")
12. }).catch((err:string) => {
13. console.error("close fail, error:" + JSON.stringify(err))
14. });
```

### on('open')

PhonePC/2in1TabletTVWearable

on(type: 'open', callback: AsyncCallback<Object>): void

订阅WebSocket的打开事件，使用callback异步回调。该事件用于指示WebSocket是否连接成功。该接口需要在调用[connect](js-apis-websocket.md#connect)发起连接请求前调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'open'：WebSocket的打开事件。 |
| callback | AsyncCallback<Object> | 是 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError, Callback } from '@kit.BasicServicesKit';

4. let ws= webSocket.createWebSocket();
5. class OutValue {
6. status: number = 0
7. message: string = ""
8. }
9. ws.on('open', (err: BusinessError, value: Object) => {
10. console.info("on open, status:" + (value as OutValue).status + ", message:" + (value as OutValue).message)
11. });
```

### off('open')

PhonePC/2in1TabletTVWearable

off(type: 'open', callback?: AsyncCallback<Object>): void

取消订阅WebSocket的打开事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'open'：WebSocket的打开事件。 |
| callback | AsyncCallback<Object> | 否 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. class OutValue {
6. status: number = 0
7. message: string = ""
8. }
9. let callback1 = (err: BusinessError, value: Object) => {
10. console.info("on open, status:" + ((value as OutValue).status + ", message:" + (value as OutValue).message))
11. }
12. ws.on('open', callback1);
13. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
14. ws.off('open', callback1);
```

### on('message')

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: AsyncCallback<string | ArrayBuffer>): void

订阅WebSocket的接收服务器消息事件，使用callback异步回调。

说明

AsyncCallback中的数据可以是字符串（API version 6开始支持）或ArrayBuffer（API version 8开始支持）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：WebSocket的接收服务器消息事件。 |
| callback | AsyncCallback<string | ArrayBuffer 8+> | 是 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. ws.on('message', (err: BusinessError<void>, value: string | ArrayBuffer) => {
6. console.info("on message, message:" + value)
7. });
```

### off('message')

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: AsyncCallback<string | ArrayBuffer>): void

取消订阅WebSocket的接收服务器消息事件，使用callback异步回调。

说明

AsyncCallback中的数据可以是字符串(API 6)或ArrayBuffer(API 8)。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'message'：WebSocket的接收到服务器消息事件。 |
| callback | AsyncCallback<string |ArrayBuffer 8+> | 否 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.off('message');
```

### on('close')

PhonePC/2in1TabletTVWearable

on(type: 'close', callback: AsyncCallback<CloseResult>): void

订阅WebSocket的关闭事件，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'close'：WebSocket的关闭事件。 |
| callback | AsyncCallback<CloseResult> | 是 | 回调函数。  close：close错误码，reason：错误码说明 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. ws.on('close', (err: BusinessError, value: webSocket.CloseResult) => {
6. console.info("on close, code is " + value.code + ", reason is " + value.reason)
7. });
```

### off('close')

PhonePC/2in1TabletTVWearable

off(type: 'close', callback?: AsyncCallback<CloseResult>): void

取消订阅WebSocket的关闭事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'close'：WebSocket的关闭事件。 |
| callback | AsyncCallback<CloseResult> | 否 | 回调函数。  close：close错误码，reason：错误码说明 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.off('close');
```

### on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅WebSocket的Error事件，使用callback异步回调。

关于[error](js-apis-websocket.md#onerror)事件回调的错误码说明：WebSocket的本质是HTTP协议升级，若服务器同意升级，服务器会返回101。状态码表示协议从HTTP切换为WebSocket协议（触发open回调），而如果服务器拒绝了升级或出现其他异常，则返回200，表示服务器只是将请求当作普通的HTTP请求来处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：WebSocket的Error事件。 |
| callback | ErrorCallback | 是 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let ws = webSocket.createWebSocket();
5. ws.on('error', (err: BusinessError) => {
6. console.error(`on error. Code: ${err.code}, message: ${err.message}`)
7. });
```

### off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅WebSocket的Error事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：WebSocket的Error事件。 |
| callback | ErrorCallback | 否 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.off('error');
```

### on('dataEnd')11+

PhonePC/2in1TabletTVWearable

on(type: 'dataEnd', callback: Callback<void>): void

订阅WebSocket的数据接收结束事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'dataEnd'：WebSocket的数据接收结束事件。 |
| callback | Callback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.on('dataEnd', () => {
5. console.info("on dataEnd")
6. });
```

### off('dataEnd')11+

PhonePC/2in1TabletTVWearable

off(type: 'dataEnd', callback?: Callback<void>): void

取消订阅WebSocket的数据接收结束事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'dataEnd'：WebSocket的数据接收结束事件。 |
| callback | Callback<void> | 否 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.off('dataEnd');
```

### on('headerReceive')12+

PhonePC/2in1TabletTVWearable

on(type: 'headerReceive', callback: Callback<ResponseHeaders>): void

订阅HTTP Response Header事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'headerReceive'：WebSocket的headerReceive事件。 |
| callback | Callback<ResponseHeaders> | 是 | 回调函数，返回订阅事件。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.on('headerReceive', (data) => {
5. console.info("on headerReceive " + JSON.stringify(data))
6. });
```

### off('headerReceive')12+

PhonePC/2in1TabletTVWearable

off(type: 'headerReceive', callback?: Callback<ResponseHeaders>): void

取消订阅HTTP Response Header事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'headerReceive'：WebSocket的headerReceive事件。 |
| callback | Callback<ResponseHeaders> | 否 | 回调函数，返回订阅事件。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';

3. let ws = webSocket.createWebSocket();
4. ws.off('headerReceive');
```

## webSocket.createWebSocketServer19+

PhonePC/2in1TabletTVWearable

createWebSocketServer(): WebSocketServer

创建一个WebSocketServer对象，包括启动服务、发送数据、关闭连接、列出客户端信息、停止服务，订阅/取消订阅webSocket连接的连接事件、接收到客户端消息事件、关闭事件和错误事件。

说明

从API version 23开始支持全设备使用，之前仅支持TV设备使用。

**系统能力**: SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSocketServer](js-apis-websocket.md#websocketserver19) | 返回一个WebSocketServer对象，里面包括start、listAllConnections、send、close、stop、on和off方法。 |

**示例：**

```
1. let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```

## WebSocketServer19+

PhonePC/2in1TabletTVWearable

在调用WebSocketServer方法前，需要先通过[webSocket.createWebSocketServer](js-apis-websocket.md#websocketcreatewebsocketserver19)创建一个WebSocketServer。

### start19+

PhonePC/2in1TabletTVWearable

start(config: WebSocketServerConfig): Promise<boolean>

配置config参数，启动服务端service。使用Promise异步回调。

说明

在多次调用该接口时，应避免监听同一端口。

**需要权限**: ohos.permission.INTERNET

**系统能力**: SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [WebSocketServerConfig](js-apis-websocket.md#websocketserverconfig19) | 是 | 启动websocketServer服务器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | promise对象。返回true表示服务器启动成功；返回false表示服务启动失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[webSocket错误码](errorcode-net-websocket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2302002 | Websocket certificate file does not exist. |
| 2302004 | Can't listen on the given NIC. |
| 2302005 | Can't listen on the given Port. |
| 2302999 | Websocket other unknown error. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer: webSocket.WebSocketServer;
5. let config: webSocket.WebSocketServerConfig = {
6. serverPort: 8080, // 监听端口
7. maxConcurrentClientsNumber: 10,
8. maxConnectionsForOneClient: 10,
9. }

11. localServer = webSocket.createWebSocketServer();
12. localServer.start(config).then((success: boolean) => {
13. if (success) {
14. console.info('webSocket server start success');
15. } else {
16. console.error('websocket server start failed');
17. }
18. }).catch((error: BusinessError) => {
19. console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
20. });
```

### send19+

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer, connection: WebSocketConnection): Promise<boolean>

通过WebSocket连接发送数据。使用Promise异步回调。

说明

send接口必须在监听到connect事件后才可以调用。

**需要权限**: ohos.permission.INTERNET

**系统能力**: SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | 服务端发送消息的数据，同时支持string（字符串）和ArrayBuffer（二进制）类型。最大支持发送5242864字节数据(即5 \* 1024 \* 1024 - 16)，超过该大小会返回401错误码。 |
| connection | [WebSocketConnection](js-apis-websocket.md#websocketconnection19) | 是 | 发送的客户端信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | promise对象。返回true表示发送请求创建成功；返回false表示发送请求创建失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[webSocket错误码](errorcode-net-websocket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2302006 | websocket connection does not exist. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer: webSocket.WebSocketServer;
5. let config: webSocket.WebSocketServerConfig = {
6. serverPort: 8080, // 监听端口
7. maxConcurrentClientsNumber: 10,
8. maxConnectionsForOneClient: 10,
9. }

11. localServer = webSocket.createWebSocketServer();
12. localServer.start(config).then((success: boolean) => {
13. if (success) {
14. console.info('webSocket server start success');
15. } else {
16. console.error('websocket server start failed');
17. }
18. }).catch((error: BusinessError) => {
19. console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
20. });

22. localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
23. console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
24. // 当收到on('connect')事件时，可以通过send()方法与客户端进行通信
25. localServer.send("Hello, I'm server!", connection).then((success: boolean) => {
26. if (success) {
27. console.info('message send successfully');
28. } else {
29. console.error('message send failed');
30. }
31. }).catch((error: BusinessError) => {
32. console.error(`message send failed, Code: ${error.code}, message: ${error.message}`);
33. });
34. });
```

### listAllConnections19+

PhonePC/2in1TabletTVWearable

listAllConnections(): WebSocketConnection[]

获取与服务端连接的所有客户端信息。

**需要权限**: ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

说明

该接口为异步调用，返回结果需通过await关键字等待异步操作完成，以确保正确获取到所有客户端连接信息。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSocketConnection[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket#websocketconnection19) | 以字符串数组形式返回所有客户端的信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let connections: webSocket.WebSocketConnection[] = [];
5. let localServer: webSocket.WebSocketServer;
6. let config: webSocket.WebSocketServerConfig = {
7. serverPort: 8080, // 监听端口
8. maxConcurrentClientsNumber: 10,
9. maxConnectionsForOneClient: 10,
10. }

12. localServer = webSocket.createWebSocketServer();
13. localServer.start(config).then((success: boolean) => {
14. if (success) {
15. console.info('webSocket server start success');
16. } else {
17. console.error('websocket server start failed');
18. }
19. }).catch((error: BusinessError) => {
20. console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
21. });

23. localServer.on('connect', async (connection: webSocket.WebSocketConnection) => {
24. console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
25. try {
26. connections = await localServer.listAllConnections();
27. if (connections.length === 0) {
28. console.info('client list is empty');
29. } else {
30. console.info(`client list cnt: ${connections.length}, client connections list is: ${connections}`);
31. }
32. } catch (error) {
33. console.error(`Failed to listAllConnections. Code: ${error.code}, message: ${error.message}`);
34. }
35. });
```

### close19+

PhonePC/2in1TabletTVWearable

close(connection: WebSocketConnection, options?: webSocket.WebSocketCloseOptions): Promise<boolean>

关闭指定websocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | [WebSocketConnection](js-apis-websocket.md#websocketconnection19) | 是 | 客户端信息，包括客户端的ip地址和端口号port。 |
| options | [webSocket.WebSocketCloseOptions](js-apis-websocket.md#websocketcloseoptions) | 否 | 关闭WebSocket连接时，可选参数的类型和说明。  - 错误码默认：200。原因值默认：Websocket connect failed。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | promise对象。返回true表示关闭请求创建成功；返回false表示关闭请求创建失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[webSocket错误码](errorcode-net-websocket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2302006 | websocket connection does not exist. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer: webSocket.WebSocketServer;
5. let config: webSocket.WebSocketServerConfig = {
6. serverPort: 8080, // 监听端口
7. maxConcurrentClientsNumber: 10,
8. maxConnectionsForOneClient: 10,
9. }

11. localServer = webSocket.createWebSocketServer();
12. localServer.start(config).then((success: boolean) => {
13. if (success) {
14. console.info('webSocket server start success');
15. } else {
16. console.error('websocket server start failed');
17. }
18. }).catch((error: BusinessError) => {
19. console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
20. });

22. localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
23. console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
24. localServer.close(connection).then((success: boolean) => {
25. if (success) {
26. console.info('close client successfully');
27. } else {
28. console.error('close client failed');
29. }
30. });
31. });
```

### stop19+

PhonePC/2in1TabletTVWearable

stop(): Promise<boolean>

停止服务端服务。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | promise对象。返回true表示停止服务端service请求创建成功；返回false表示停止服务端service请求创建失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer: webSocket.WebSocketServer;
5. let config: webSocket.WebSocketServerConfig = {
6. serverPort: 8080, // 监听端口
7. maxConcurrentClientsNumber: 10,
8. maxConnectionsForOneClient: 10,
9. }

11. localServer = webSocket.createWebSocketServer();
12. localServer.start(config).then((success: boolean) => {
13. if (success) {
14. console.info('webSocket server start success');
15. } else {
16. console.error('websocket server start failed');
17. }
18. }).catch((error: BusinessError) => {
19. console.error(`Failed to start. Code: ${error.code}, message: ${error.message}`);
20. });

22. localServer.stop().then((success: boolean) => {
23. if (success) {
24. console.info('server stop service successfully');
25. } else {
26. console.error('server stop service failed');
27. }
28. });
```

### on('connect')19+

PhonePC/2in1TabletTVWearable

on(type: 'connect', callback: Callback<WebSocketConnection>): void

订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'，当onconnect()调用完成，客户端与服务端建链成功。 |
| callback | Callback<[WebSocketConnection](js-apis-websocket.md#websocketconnection19)> | 是 | 回调函数。连接的客户端信息。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError, Callback } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.on('connect', (connection: webSocket.WebSocketConnection) => {
6. console.info(`New client connected! Client ip: ${connection.clientIP}, Client port: ${connection.clientPort}`);
7. });
```

### off('connect')19+

PhonePC/2in1TabletTVWearable

off(type: 'connect', callback?: Callback<WebSocketConnection>): void

取消订阅WebSocketServer的连接事件（客户端与服务端建链成功），使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connect'，当offconnect()调用完成，取消监听连接事件成功。 |
| callback | Callback<[WebSocketConnection](js-apis-websocket.md#websocketconnection19)> | 否 | 回调函数。连接的客户端信息。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.off('connect');
```

### on('messageReceive')19+

PhonePC/2in1TabletTVWearable

on(type: 'messageReceive', callback: Callback<WebSocketMessage>): void

订阅WebSocketServer的接收客户端消息的事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'messageReceive'，当onmessageReceive()调用完成，接收到客户端消息成功。 |
| callback | Callback<[WebSocketMessage](js-apis-websocket.md#websocketmessage19)> | 是 | 回调函数。  clientconnection:客户端信息，data:客户端发送的数据消息。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError, Callback } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.on('messageReceive', (message: webSocket.WebSocketMessage) => {
6. console.info(`on message received, client: ${message.clientConnection}, data: ${message.data}`);
7. });
```

### off('messageReceive')19+

PhonePC/2in1TabletTVWearable

off(type: 'messageReceive', callback?: Callback<WebSocketMessage>): void

取消订阅WebSocketServer的接收到客户端消息事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'messageReceive'，当offmessageReceive()调用完成，取消订阅接收客户端消息成功。 |
| callback | Callback<[WebSocketMessage](js-apis-websocket.md#websocketmessage19)> | 否 | 从指定客户端接收到的消息，包括客户端的信息和数据。  - clientconnection：客户端信息。  - data：客户端发送的消息。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError, Callback } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.off('messageReceive');
```

### on('close')19+

PhonePC/2in1TabletTVWearable

on(type: 'close', callback: ClientConnectionCloseCallback): void

订阅WebSocketServer的关闭事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'close'，当onclose()调用完成，连接关闭成功。 |
| callback | [ClientConnectionCloseCallback](js-apis-websocket.md#clientconnectionclosecallback19) | 是 | 回调函数。  close：close错误码；reason：错误码说明。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.on('close', (clientConnection: webSocket.WebSocketConnection, closeReason: webSocket.CloseResult) => {
6. console.info(`client close, client: ${clientConnection}, closeReason: Code: ${closeReason.code}, reason: ${closeReason.reason}`);
7. });
```

### off('close')19+

PhonePC/2in1TabletTVWearable

off(type: 'close', callback?: ClientConnectionCloseCallback): void

取消订阅WebSocketServer的关闭事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'close'，当offclose()调用完成，取消订阅连接关闭事件成功。 |
| callback | [ClientConnectionCloseCallback](js-apis-websocket.md#clientconnectionclosecallback19) | 否 | 回调函数。  close：close错误码；reason：错误码说明。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.off('close');
```

### on('error')19+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅WebSocketServer的Error事件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'error'，当onerror()调用完成，error事件发生。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 回调函数。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let wsServer: webSocket.WebSocketServer = webSocket.createWebSocketServer();
5. wsServer.on('error', (err: BusinessError) => {
6. console.error(`error. Code: ${err.code}, message: ${err.message}`);
7. });
```

### off('error')19+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅WebSocketServer的Error事件，使用callback异步回调。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'error'，当offerror()调用完成，取消订阅error事件成功。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 回调函数。默认值：200。 |

**示例：**

```
1. import { webSocket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let localServer = webSocket.createWebSocketServer();
5. localServer.off('error');
```

## WebSocketRequestOptions

PhonePC/2in1TabletTVWearable

建立WebSocket连接时，可选参数的类型和说明。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| header | Object | 否 | 是 | 建立WebSocket连接可选参数，代表建立连接时携带的HTTP头信息。参数内容自定义，也可以不指定。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| caPath11+ | string | 否 | 是 | 如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。目前仅支持格式为pem的文本证书。 |
| clientCert11+ | [ClientCert](js-apis-websocket.md#clientcert11) | 否 | 是 | 支持传输客户端证书。 |
| proxy12+ | [ProxyConfiguration](js-apis-websocket.md#proxyconfiguration12) | 否 | 是 | 通信过程中的代理信息，默认使用系统网络代理。 |
| protocol12+ | string | 否 | 是 | 自定义Sec-WebSocket-Protocol字段，默认为""。 |
| skipServerCertVerification20+ | boolean | 否 | 是 | 是否跳过服务器证书验证。true表示跳过服务器证书验证，false表示不跳过服务器证书验证。默认为false。 |
| pingInterval21+ | number | 否 | 是 | 自定义[心跳检测](../harmonyos-guides/websocket-connection.md#场景介绍)时间，默认为30s。每pingInterval周期会发起心跳检测，设置为0则表示关闭心跳检测。最大值：30000s，最小值：0s。 |
| pongTimeout21+ | number | 否 | 是 | 自定义发起心跳检测后，超时断开时间，默认为30s。发起心跳检测后若pongTimeout时间未响应则断开连接。最大值：30000s，最小值：0s。pongTimeout须小于等于pingInterval。 |

## ClientCert11+

PhonePC/2in1TabletTVWearable

客户端证书类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certPath | string | 否 | 否 | 证书路径。 |
| keyPath | string | 否 | 否 | 证书密钥的路径。 |
| keyPassword | string | 否 | 是 | 证书密钥的密码。缺省为空字符串。 |

## ProxyConfiguration12+

PhonePC/2in1TabletTVWearable

type ProxyConfiguration = 'system' | 'no-proxy' | HttpProxy

网络代理配置信息

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| 'system' | 使用系统默认网络代理。 |
| 'no-proxy' | 不使用网络代理。 |
| [HttpProxy](js-apis-net-connection.md#httpproxy10) | 使用指定的网络代理。 |

## WebSocketCloseOptions

PhonePC/2in1TabletTVWearable

关闭WebSocket连接时，可选参数的类型和说明。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 是 | 错误码，关闭WebSocket连接时的可选参数，可根据实际情况来填。传入值必须为正整数，取值范围为[1000,1015]。如果未指定错误码或传入值不在上述范围内，code将会被设置为默认值1000。 |
| reason | string | 否 | 是 | 原因值，关闭WebSocket连接时的可选参数，可根据实际情况来填。如果未指定原因值，则原因值将会被设置为默认值"CLOSE\_NORMAL"。 |

## CloseResult10+

PhonePC/2in1TabletTVWearable

关闭WebSocket连接时，订阅close事件得到的关闭结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 错误码，订阅close事件得到的关闭连接的错误码。 |
| reason | string | 否 | 否 | 原因值，订阅close事件得到的关闭连接的错误原因。 |

## ResponseHeaders12+

PhonePC/2in1TabletTVWearable

type ResponseHeaders = { [k: string]: string | string[] | undefined; }

服务器发送的响应头。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [k:string] | string | string[] | undefined | 否 | 键值对形式存储。其键的类型为字符，可取任意值，其值的类型为字符、字符数组或undefined。 |

## close错误码说明

PhonePC/2in1TabletTVWearable

发送给服务端的错误码必须为正整数，取值范围为[1000,1015],可以自行定义，如果未指定错误码或传入值不在上述范围内，错误码将会被设置为默认值1000。下面的列表仅供参考。

**系统能力**：SystemCapability.Communication.NetStack

| 值 | 说明 |
| --- | --- |
| 1000 | 正常关闭。 |
| 1001 | 服务器主动关闭。 |
| 1002 | 协议错误。 |
| 1003 | 无法处理的数据类型。 |
| 1004~1015 | 保留值。 |

## HttpProxy12+

PhonePC/2in1TabletTVWearable

type HttpProxy = connection.HttpProxy

网络全局代理配置信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| connection.HttpProxy | 使用指定的网络代理。 |

## WebSocketServerConfig19+

PhonePC/2in1TabletTVWearable

启动服务端的service时，需要输入的配置信息和说明。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serverIP | string | 否 | 是 | 服务端监听特定ip地址，默认是"0.0.0.0"。 |
| serverPort | number | 否 | 否 | 服务端监听的端口号。 |
| serverCert | [ServerCert](js-apis-websocket.md#servercert19) | 否 | 是 | 指定服务端证书的信息，包括服务端证书文件路径和服务端证书的私钥文件路径。 |
| protocol | string | 否 | 是 | 自定义协议。 |
| maxConcurrentClientsNumber | number | 否 | 否 | 最大并发客户端数量，当达到最大数时，服务端拒绝新连接。默认最大数量为10。 |
| maxConnectionsForOneClient | number | 否 | 否 | 单个客户端的最大连接数。默认最大数量为10。 |

## ServerCert19+

PhonePC/2in1TabletTVWearable

指定服务端证书的信息，包括服务端证书文件路径和服务端证书的私钥文件路径。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certPath | string | 否 | 否 | 服务端证书文件路径。 |
| keyPath | string | 否 | 否 | 服务端证书的私钥文件路径。 |

## WebSocketMessage19+

PhonePC/2in1TabletTVWearable

从指定客户端接收到的消息，包括客户端的信息和数据。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | string |ArrayBuffer | 否 | 否 | 接收到的客户端发的消息数据。 |
| clientConnection | [WebSocketConnection](js-apis-websocket.md#websocketconnection19) | 否 | 否 | 客户端信息，包括客户端的ip地址和端口号port。 |

## WebSocketConnection19+

PhonePC/2in1TabletTVWearable

客户端信息，包括客户端的ip地址和端口号port。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientIP | string | 否 | 否 | 客户端的ip地址。 |
| clientPort | number | 否 | 否 | 客户端的端口号port。 |

## ClientConnectionCloseCallback19+

PhonePC/2in1TabletTVWearable

type ClientConnectionCloseCallback = (clientConnection: WebSocketConnection, closeReason: CloseResult) => void

关闭WebSocketServer连接时，订阅close事件得到的指定客户端的关闭结果。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientConnection | [WebSocketConnection](js-apis-websocket.md#websocketconnection19) | 是 | 客户端信息，包括客户端的ip地址和端口号port。 |
| closeReason | [CloseResult](js-apis-websocket.md#closeresult10) | 是 | 关闭WebSocket连接时，订阅close事件得到的关闭结果。 |
