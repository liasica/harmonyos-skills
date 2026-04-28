---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket
title: @ohos.net.socket (Socket连接)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.socket (Socket连接)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b4d7ef6e3c4606b9cfb73da715813fcd3b82129625116f3e9b53d0e5af1c6702
---

本模块提供利用Socket进行数据传输的能力，支持TCPSocket、UDPSocket、WebSocket和TLSSocket。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块API使用时建议放在worker线程或者taskpool中做网络操作，否则可能会导致UI线程卡顿。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { socket } from '@kit.NetworkKit';
```

## socket.constructUDPSocketInstance

PhonePC/2in1TabletTVWearable

constructUDPSocketInstance(): UDPSocket

创建一个UDPSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UDPSocket](js-apis-socket.md#udpsocket) | 返回一个UDPSocket对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```

## UDPSocket

PhonePC/2in1TabletTVWearable

UDPSocket连接。在调用UDPSocket的方法前，需要先通过[socket.constructUDPSocketInstance](js-apis-socket.md#socketconstructudpsocketinstance)创建UDPSocket对象。

### bind

PhonePC/2in1TabletTVWearable

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以由用户指定或由系统随机分配。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 本端地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',  // 本端地址
7. port: 1234
8. }
9. udp.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
```

### bind

PhonePC/2in1TabletTVWearable

bind(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以由用户指定或由系统随机分配。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 本端地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',  // 本端地址
7. port: 8080
8. }
9. udp.bind(bindAddr).then(() => {
10. console.info('bind success');
11. }).catch((err: BusinessError) => {
12. console.error('bind fail');
13. });
```

### send

PhonePC/2in1TabletTVWearable

send(options: UDPSendOptions, callback: AsyncCallback<void>): void

通过UDPSocket连接发送数据。使用callback异步回调。

发送数据前，需要先调用[UDPSocket.bind()](js-apis-socket.md#bind)绑定IP地址和端口。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UDPSendOptions](js-apis-socket.md#udpsendoptions) | 是 | UDPSocket发送参数，参考[UDPSendOptions](js-apis-socket.md#udpsendoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',  // 本端地址
7. port: 1234
8. }
9. udp.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. let netAddress: socket.NetAddress = {
17. address: '192.168.xx.xxx',  // 对端地址
18. port: 8080
19. }
20. let sendOptions: socket.UDPSendOptions = {
21. data: 'Hello, server!',
22. address: netAddress
23. }
24. udp.send(sendOptions, (err: BusinessError) => {
25. if (err) {
26. console.error('send fail');
27. return;
28. }
29. console.info('send success');
30. });
```

**示例（设置socket代理）：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',  // 本端地址
7. port: 1234
8. }
9. udp.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. let netAddress: socket.NetAddress = {
17. address: '192.168.xx.xxx',  // 对端地址
18. port: 8080
19. }
20. let socks5Server: socket.NetAddress = {
21. address: '192.168.xx.xxx',
22. port: 8080
23. }
24. let proxyOptions: socket.ProxyOptions = {
25. type : 1,
26. address: socks5Server,
27. username: "xxx",
28. password: "xxx"
29. }
30. let sendOptions: socket.UDPSendOptions = {
31. data: 'Hello, server!',
32. address: netAddress,
33. proxy: proxyOptions,
34. }
35. udp.send(sendOptions, (err: BusinessError) => {
36. if (err) {
37. console.error('send fail');
38. return;
39. }
40. console.info('send success');
41. });
```

### send

PhonePC/2in1TabletTVWearable

send(options: UDPSendOptions): Promise<void>

通过UDPSocket连接发送数据。使用Promise异步回调。

发送数据前，需要先调用[UDPSocket.bind()](js-apis-socket.md#bind)绑定IP地址和端口。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UDPSendOptions](js-apis-socket.md#udpsendoptions) | 是 | UDPSocket发送参数，参考[UDPSendOptions](js-apis-socket.md#udpsendoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx', // 本端地址
7. port: 8080
8. }
9. udp.bind(bindAddr).then(() => {
10. console.info('bind success');
11. }).catch((err: BusinessError) => {
12. console.error('bind fail');
13. return;
14. });
15. let netAddress: socket.NetAddress = {
16. address: '192.168.xx.xxx', // 对端地址
17. port: 8080
18. }
19. let sendOptions: socket.UDPSendOptions = {
20. data: 'Hello, server!',
21. address: netAddress
22. }
23. udp.send(sendOptions).then(() => {
24. console.info('send success');
25. }).catch((err: BusinessError) => {
26. console.error('send fail');
27. });
```

**示例（设置socket代理）：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx', // 本端地址
7. port: 8080
8. }
9. udp.bind(bindAddr).then(() => {
10. console.info('bind success');
11. }).catch((err: BusinessError) => {
12. console.error('bind fail');
13. return;
14. });
15. let netAddress: socket.NetAddress = {
16. address: '192.168.xx.xxx', // 对端地址
17. port: 8080
18. }
19. let socks5Server: socket.NetAddress = {
20. address: '192.168.xx.xxx',
21. port: 8080
22. }
23. let proxyOptions: socket.ProxyOptions = {
24. type : 1,
25. address: socks5Server,
26. username: "xxx",
27. password: "xxx"
28. }
29. let sendOptions: socket.UDPSendOptions = {
30. data: 'Hello, server!',
31. address: netAddress,
32. proxy: proxyOptions,
33. }
34. udp.send(sendOptions).then(() => {
35. console.info('send success');
36. }).catch((err: BusinessError) => {
37. console.error('send fail');
38. });
```

### close

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

关闭UDPSocket连接。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。关闭UDPSocket连接后触发回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. udp.close((err: BusinessError) => {
6. if (err) {
7. console.error('close fail');
8. return;
9. }
10. console.info('close success');
11. })
```

### close

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭UDPSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. udp.close().then(() => {
6. console.info('close success');
7. }).catch((err: BusinessError) => {
8. console.error('close fail');
9. });
```

### getState

PhonePC/2in1TabletTVWearable

getState(callback: AsyncCallback<SocketStateBase>): void

获取UDPSocket状态。使用callback异步回调。

说明

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 是 | 回调函数。成功返回UDPSocket状态信息，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. udp.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.error('bind success');
15. udp.getState((err: BusinessError, data: socket.SocketStateBase) => {
16. if (err) {
17. console.error('getState fail');
18. return;
19. }
20. console.info('getState success:' + JSON.stringify(data));
21. })
22. })
```

### getState

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

获取UDPSocket状态。使用Promise异步回调。

说明

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取UDPSocket状态的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. udp.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. udp.getState().then((data: socket.SocketStateBase) => {
16. console.info('getState success:' + JSON.stringify(data));
17. }).catch((err: BusinessError) => {
18. console.error('getState fail' + JSON.stringify(err));
19. });
20. });
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取UDPSocket的文件描述符。使用Promise异步回调。

说明

* [bind](js-apis-socket.md#bind)方法调用成功后，才可调用此方法。
* bind异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. udp.bind(bindAddr)
10. .then(() => {
11. udp.getSocketFd()
12. .then((fd: number) => {
13. console.info(`Socket FD：${fd}`);
14. }).catch((err: BusinessError) => {
15. console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
16. });
17. }).catch((err: BusinessError) => {
18. console.error('bind fail');
19. });
```

### setExtraOptions

PhonePC/2in1TabletTVWearable

setExtraOptions(options: UDPExtraOptions, callback: AsyncCallback<void>): void

设置UDPSocket连接的其他属性。使用callback异步回调。

说明

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UDPExtraOptions](js-apis-socket.md#udpextraoptions) | 是 | UDPSocket连接的其他属性，参考[UDPExtraOptions](js-apis-socket.md#udpextraoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

6. let bindAddr: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. udp.bind(bindAddr, (err: BusinessError) => {
11. if (err) {
12. console.error('bind fail');
13. return;
14. }
15. console.info('bind success');
16. let udpextraoptions: socket.UDPExtraOptions = {
17. receiveBufferSize: 8192,
18. sendBufferSize: 8192,
19. reuseAddress: false,
20. socketTimeout: 6000,
21. broadcast: true
22. }
23. udp.setExtraOptions(udpextraoptions, (err: BusinessError) => {
24. if (err) {
25. console.error('setExtraOptions fail');
26. return;
27. }
28. console.info('setExtraOptions success');
29. })
30. })
```

### setExtraOptions

PhonePC/2in1TabletTVWearable

setExtraOptions(options: UDPExtraOptions): Promise<void>

设置UDPSocket连接的其他属性。使用Promise异步回调。

说明

bind方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UDPExtraOptions](js-apis-socket.md#udpextraoptions) | 是 | UDPSocket连接的其他属性，参考[UDPExtraOptions](js-apis-socket.md#udpextraoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

6. let bindAddr: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. udp.bind(bindAddr, (err: BusinessError) => {
11. if (err) {
12. console.error('bind fail');
13. return;
14. }
15. console.info('bind success');
16. let udpextraoptions: socket.UDPExtraOptions = {
17. receiveBufferSize: 8192,
18. sendBufferSize: 8192,
19. reuseAddress: false,
20. socketTimeout: 6000,
21. broadcast: true
22. }
23. udp.setExtraOptions(udpextraoptions).then(() => {
24. console.info('setExtraOptions success');
25. }).catch((err: BusinessError) => {
26. console.error('setExtraOptions fail');
27. });
28. })
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取UDP连接的本地Socket地址。使用Promise异步回调。

说明

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

6. let bindAddr: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. udp.bind(bindAddr).then(() => {
11. console.info('bind success');
12. udp.getLocalAddress().then((localAddress: socket.NetAddress) => {
13. console.info("UDP_Socket get SUCCESS! Address：" + JSON.stringify(localAddress));
14. }).catch((err: BusinessError) => {
15. console.error("UDP_Socket get FAILED! Error: " + JSON.stringify(err));
16. })
17. }).catch((err: BusinessError) => {
18. console.error('bind fail');
19. });
```

### on('message')

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅UDPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 是 | 回调函数。返回订阅某类事件后UDPSocket连接成功的状态信息。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();

6. udp.on('message', (value: socket.SocketMessageInfo) => {
7. let messageView = '';
8. let uint8Array = new Uint8Array(value.message);
9. for (let i: number = 0; i < value.message.byteLength; i++) {
10. let messages = uint8Array[i];
11. let message = String.fromCharCode(messages);
12. messageView += message;
13. }
14. console.info('on message message: ' + JSON.stringify(messageView));
15. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
16. });
```

### off('message')

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅UDPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let messageView = '';
6. let callback = (value: socket.SocketMessageInfo) => {
7. for (let i: number = 0; i < value.message.byteLength; i++) {
8. let uint8Array = new Uint8Array(value.message)
9. let messages = uint8Array[i]
10. let message = String.fromCharCode(messages);
11. messageView += message;
12. }
13. console.info('on message message: ' + JSON.stringify(messageView));
14. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
15. }
16. udp.on('message', callback);
17. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
18. udp.off('message', callback);
19. udp.off('message');
```

### on('listening' | 'close')

PhonePC/2in1TabletTVWearable

on(type: 'listening' | 'close', callback: Callback<void>): void

订阅UDPSocket连接的数据包消息事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。  - 'listening'：数据包消息事件。  - 'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。UDPSocket连接的某类数据包消息事件或关闭事件发生变化后触发回调函数。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. udp.on('listening', () => {
6. console.info("on listening success");
7. });
8. udp.on('close', () => {
9. console.info("on close success");
10. });
```

### off('listening' | 'close')

PhonePC/2in1TabletTVWearable

off(type: 'listening' | 'close', callback?: Callback<void>): void

取消订阅UDPSocket连接的数据包消息事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅事件类型。  - 'listening'：数据包消息事件。  - 'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let callback1 = () => {
6. console.info("on listening, success");
7. }
8. udp.on('listening', callback1);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. udp.off('listening', callback1);
11. udp.off('listening');
12. let callback2 = () => {
13. console.info("on close, success");
14. }
15. udp.on('close', callback2);
16. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
17. udp.off('close', callback2);
18. udp.off('close');
```

### on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅UDPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。UDPSocket连接发生error事件后触发回调函数。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. udp.on('error', (err: BusinessError) => {
6. console.error("on error, err:" + JSON.stringify(err))
7. });
```

### off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅UDPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
5. let callback = (err: BusinessError) => {
6. console.error("on error, err:" + JSON.stringify(err));
7. }
8. udp.on('error', callback);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. udp.off('error', callback);
11. udp.off('error');
```

## NetAddress

PhonePC/2in1TabletTVWearable

目标地址信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address11+ | string | 否 | 否 | 本地绑定的ip地址。 |
| port | number | 否 | 否 | 端口号 ，范围0~65535。如果不指定系统随机分配端口。 |
| family | number | 否 | 否 | 网络协议类型，可选类型：  - 1：IPv4。默认为1。  - 2：IPv6。地址为IPV6类型，该字段必须被显式指定为2。  - 3：Domain18+。地址为Domain类型，该字段必须被显式指定为3。当前仅支持[TCPSocket.connect](js-apis-socket.md#connect)和[TLSSocket.connect](js-apis-socket.md#connect9)。 |

## ProxyOptions18+

PhonePC/2in1TabletTVWearable

Socket代理信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ProxyTypes](js-apis-socket.md#proxytypes18) | 否 | 否 | 代理类型。 |
| address | [NetAddress](js-apis-socket.md#netaddress) | 否 | 否 | 代理地址信息。 |
| username | string | 否 | 是 | 指定用户名，如果使用用户密码验证方式。 |
| password | string | 否 | 是 | 指定密码，如果使用用户密码验证方式。 |

## ProxyTypes18+

PhonePC/2in1TabletTVWearable

Socket代理类型。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不使用代理。 |
| SOCKS5 | 1 | 使用Socks5代理。 |

## UDPSendOptions

PhonePC/2in1TabletTVWearable

UDPSocket发送参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | string | ArrayBuffer | 否 | 否 | 发送的数据。 |
| address | [NetAddress](js-apis-socket.md#netaddress) | 否 | 否 | 目标地址信息。 |
| proxy18+ | [ProxyOptions](js-apis-socket.md#proxyoptions18) | 否 | 是 | 使用的代理信息，默认不使用代理。 |

## UDPExtraOptions

PhonePC/2in1TabletTVWearable

UDPSocket连接的其他属性。继承自[ExtraOptionsBase](js-apis-socket.md#extraoptionsbase)。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| broadcast | boolean | 否 | 是 | 是否可以发送广播。true表示可发送广播，false表示不可发送广播。默认为false。 |

## SocketMessageInfo11+

PhonePC/2in1TabletTVWearable

socket连接信息

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | ArrayBuffer | 否 | 否 | 接收的事件消息。 |
| remoteInfo | [SocketRemoteInfo](js-apis-socket.md#socketremoteinfo) | 否 | 否 | socket连接信息。 |

## SocketStateBase

PhonePC/2in1TabletTVWearable

Socket的状态信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isBound | boolean | 否 | 否 | 是否绑定。true：绑定；false：不绑定。 |
| isClose | boolean | 否 | 否 | 是否关闭。true：关闭；false：打开。 |
| isConnected | boolean | 否 | 否 | 是否连接。true：连接；false：断开。 |

## SocketRemoteInfo

PhonePC/2in1TabletTVWearable

Socket的连接信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 本地绑定的ip地址。 |
| family | 'IPv4' | 'IPv6' | 否 | 否 | 网络协议类型，可选类型：  - IPv4  - IPv6  默认为IPv4。 |
| port | number | 否 | 否 | 端口号，范围0~65535。 |
| size | number | 否 | 否 | 服务器响应信息的字节长度。 |

## UDP 错误码说明

PhonePC/2in1TabletTVWearable

UDP 其余错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](errorcode-net-socket.md)。

## socket.constructMulticastSocketInstance11+

PhonePC/2in1TabletTVWearable

constructMulticastSocketInstance(): MulticastSocket

创建一个MulticastSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MulticastSocket](js-apis-socket.md#multicastsocket11) | 返回一个MulticastSocket对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
```

## MulticastSocket11+

PhonePC/2in1TabletTVWearable

MulticastSocket连接。在调用MulticastSocket的方法前，需要先通过[socket.constructMulticastSocketInstance](js-apis-socket.md#socketconstructmulticastsocketinstance11)创建MulticastSocket对象。

### addMembership11+

PhonePC/2in1TabletTVWearable

addMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

加入多播组。使用callback异步回调。

说明

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| multicastAddress | [NetAddress](js-apis-socket.md#netaddress) | 是 | 目标地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. let addr: socket.NetAddress = {
5. address: '239.255.0.1',
6. port: 8080
7. }
8. multicast.addMembership(addr, (err: Object) => {
9. if (err) {
10. console.error('add membership fail, err: ' + JSON.stringify(err));
11. return;
12. }
13. console.info('add membership success');
14. })
```

### addMembership11+

PhonePC/2in1TabletTVWearable

addMembership(multicastAddress: NetAddress): Promise<void>

加入多播组。使用Promise异步回调。

说明

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

加入多播组后，既可以是发送端，也可以是接收端，相互之间以广播的形式传递数据，不区分客户端或服务端。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| multicastAddress | [NetAddress](js-apis-socket.md#netaddress) | 是 | 目标地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回MulticastSocket加入多播组的行为结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. let addr: socket.NetAddress = {
5. address: '239.255.0.1',
6. port: 8080
7. }
8. multicast.addMembership(addr).then(() => {
9. console.info('addMembership success');
10. }).catch((err: Object) => {
11. console.error('addMembership fail');
12. });
```

### dropMembership11+

PhonePC/2in1TabletTVWearable

dropMembership(multicastAddress: NetAddress, callback: AsyncCallback<void>): void

退出多播组。使用callback异步回调。

说明

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

从已加入的多播组中退出，必须在加入多播组 [addMembership](js-apis-socket.md#addmembership11) 之后退出才有效。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| multicastAddress | [NetAddress](js-apis-socket.md#netaddress) | 是 | 目标地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. let addr: socket.NetAddress = {
5. address: '239.255.0.1',
6. port: 8080
7. }
8. multicast.dropMembership(addr, (err: Object) => {
9. if (err) {
10. console.error('drop membership fail, err: ' + JSON.stringify(err));
11. return;
12. }
13. console.info('drop membership success');
14. })
```

### dropMembership11+

PhonePC/2in1TabletTVWearable

dropMembership(multicastAddress: NetAddress): Promise<void>

退出多播组。使用Promise异步回调。

说明

多播使用的IP地址属于特定的范围（例如224.0.0.0到239.255.255.255）。

从已加入的多播组中退出，必须在加入多播组 [addMembership](js-apis-socket.md#addmembership11) 之后退出才有效。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| multicastAddress | [NetAddress](js-apis-socket.md#netaddress) | 是 | 目标地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回MulticastSocket加入多播组的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301088 | Not a socket. |
| 2301098 | Address in use. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. let addr: socket.NetAddress = {
5. address: '239.255.0.1',
6. port: 8080
7. }
8. multicast.dropMembership(addr).then(() => {
9. console.info('drop membership success');
10. }).catch((err: Object) => {
11. console.error('drop membership fail');
12. });
```

### setMulticastTTL11+

PhonePC/2in1TabletTVWearable

setMulticastTTL(ttl: number, callback: AsyncCallback<void>): void

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用callback异步回调。

说明

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ttl | number | 是 | ttl设置数值，类型为数字number。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. let ttl = 8
5. multicast.setMulticastTTL(ttl, (err: Object) => {
6. if (err) {
7. console.error('set ttl fail, err: ' + JSON.stringify(err));
8. return;
9. }
10. console.info('set ttl success');
11. })
```

### setMulticastTTL11+

PhonePC/2in1TabletTVWearable

setMulticastTTL(ttl: number): Promise<void>

设置多播通信时数据包在网络传输过程中路由器最大跳数。使用Promise异步回调。

说明

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ttl | number | 是 | ttl设置数值，类型为数字Number。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回MulticastSocket设置TTL数值的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301022 | Invalid argument. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.setMulticastTTL(8).then(() => {
5. console.info('set ttl success');
6. }).catch((err: Object) => {
7. console.error('set ttl failed');
8. });
```

### getMulticastTTL11+

PhonePC/2in1TabletTVWearable

getMulticastTTL(callback: AsyncCallback<number>): void

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用callback异步回调。

说明

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.getMulticastTTL((err: Object, value: Number) => {
5. if (err) {
6. console.error('set ttl fail, err: ' + JSON.stringify(err));
7. return;
8. }
9. console.info('set ttl success, value: ' + JSON.stringify(value));
10. })
```

### getMulticastTTL11+

PhonePC/2in1TabletTVWearable

getMulticastTTL(): Promise<number>

获取数据包在网络传输过程中路由器最大跳数(TTL)的值。使用Promise异步回调。

说明

用于限制数据包在网络中传输时能够经过的最大路由器跳数的字段，TTL (Time to live)。

范围为 0～255，默认值为 1 。

如果一个多播数据包的 TTL 值为 1，那么它只能被直接连接到发送者的主机接收。如果 TTL 被设置为一个较大的值，那么数据包就能够被传送到更远的网络范围内。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回当前TTL数值。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.getMulticastTTL().then((value: Number) => {
5. console.info('ttl: ', JSON.stringify(value));
6. }).catch((err: Object) => {
7. console.error('set ttl failed');
8. });
```

### setLoopbackMode11+

PhonePC/2in1TabletTVWearable

setLoopbackMode(flag: boolean, callback: AsyncCallback<void>): void

设置多播通信中的环回模式标志位。使用callback异步回调。

说明

用于设置环回模式，开启或关闭两种状态，默认为开启状态。

如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | boolean | 是 | 是否开启环回模式。true表示环回模式开启，false表示环回模式关闭。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.setLoopbackMode(false, (err: Object) => {
5. if (err) {
6. console.error('set loopback mode fail, err: ' + JSON.stringify(err));
7. return;
8. }
9. console.info('set loopback mode success');
10. })
```

### setLoopbackMode11+

PhonePC/2in1TabletTVWearable

setLoopbackMode(flag: boolean): Promise<void>

设置多播通信中的环回模式标志位。使用Promise异步回调。

说明

用于设置环回模式，开启或关闭两种状态，默认为开启状态。

如果一个多播通信中环回模式设置值为 true，那么它允许主机在本地循环接收自己发送的多播数据包。如果为 false，则主机不会接收到自己发送的多播数据包。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | boolean | 是 | 是否开启环回模式。true表示环回模式开启，false表示环回模式关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回MulticastSocket设置环回模式的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.setLoopbackMode(false).then(() => {
5. console.info('set loopback mode success');
6. }).catch((err: Object) => {
7. console.error('set loopback mode failed');
8. });
```

### getLoopbackMode11+

PhonePC/2in1TabletTVWearable

getLoopbackMode(callback: AsyncCallback<boolean>): void

获取多播通信中的环回模式状态。使用callback异步回调。

说明

用于获取当前环回模式开启或关闭的状态。

如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回值为环回模式状态，true表示环回模式开启，false表示环回模式关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.getLoopbackMode((err: Object, value: Boolean) => {
5. if (err) {
6. console.error('get loopback mode fail, err: ' + JSON.stringify(err));
7. return;
8. }
9. console.info('get loopback mode success, value: ' + JSON.stringify(value));
10. })
```

### getLoopbackMode11+

PhonePC/2in1TabletTVWearable

getLoopbackMode(): Promise<boolean>

获取多播通信中的环回模式状态。使用Promise异步回调。

说明

用于获取当前环回模式开启或关闭的状态。

如果获取的属性值为 true，表示环回模式是开启的状态，允许主机在本地循环接收自己发送的多播数据包。如果为 false，则表示环回模式是关闭的状态，主机不会接收到自己发送的多播数据包。

在调用 [addMembership](js-apis-socket.md#addmembership11) 之后，调用此接口才有效。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示环回模式开启，返回false表示环回模式关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301088 | Not a socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
4. multicast.getLoopbackMode().then((value: Boolean) => {
5. console.info('loopback mode: ', JSON.stringify(value));
6. }).catch((err: Object) => {
7. console.error('get loopback mode failed');
8. });
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取MulticastSocket的文件描述符。使用Promise异步回调。

说明

* [bind](js-apis-socket.md#bind)方法调用成功后，才可调用此方法。
* bind异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. multicast.bind(bindAddr)
10. .then(() => {
11. console.info('bind success');
12. multicast.getSocketFd().then((fd: number) => {
13. console.info(`Socket FD：${fd}`);
14. }).catch((err: BusinessError) => {
15. console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
16. });
17. }).catch((err: BusinessError) => {
18. console.error('bind fail');
19. });
```

## socket.constructTCPSocketInstance

PhonePC/2in1TabletTVWearable

constructTCPSocketInstance(): TCPSocket

创建一个TCPSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TCPSocket](js-apis-socket.md#tcpsocket) | 返回一个TCPSocket对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
```

## TCPSocket

PhonePC/2in1TabletTVWearable

TCPSocket连接。在调用TCPSocket的方法前，需要先通过[socket.constructTCPSocketInstance](js-apis-socket.md#socketconstructtcpsocketinstance)创建TCPSocket对象。

### bind

PhonePC/2in1TabletTVWearable

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用callback异步回调。

说明

bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。

TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。

bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 本端地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tcp.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. })
```

### bind

PhonePC/2in1TabletTVWearable

bind(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以指定为0由系统随机分配或由用户指定为其它非0端口。使用Promise异步回调。

说明

bind方法如果因为端口冲突而执行失败，则会由系统随机分配端口号。

TCP客户端可先调用该接口(tcp.bind)显式绑定IP地址和端口号，再调用tcp.connect完成与服务端的连接；也可直接调用tcp.connect由系统自动绑定IP地址和端口号，完成与服务端的连接。

bind的IP为'localhost'或'127.0.0.1'时，只允许本地回环接口的连接，即服务端和客户端运行在同一台机器上。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 本端地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回TCPSocket绑定本机的IP地址和端口的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tcp.bind(bindAddr).then(() => {
10. console.info('bind success');
11. }).catch((err: BusinessError) => {
12. console.error('bind fail');
13. });
```

### connect

PhonePC/2in1TabletTVWearable

connect(options: TCPConnectOptions, callback: AsyncCallback<void>): void

连接到指定的IP地址和端口。使用callback异步回调。

说明

在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPConnectOptions](js-apis-socket.md#tcpconnectoptions) | 是 | TCPSocket连接的参数，参考[TCPConnectOptions](js-apis-socket.md#tcpconnectoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions, (err: BusinessError) => {
14. if (err) {
15. console.error('connect fail');
16. return;
17. }
18. console.info('connect success');
19. })
```

**示例（设置socket代理）：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let socks5Server: socket.NetAddress = {
10. address: '192.168.xx.xxx',
11. port: 8080
12. }
13. let proxyOptions: socket.ProxyOptions = {
14. type : 1,
15. address: socks5Server,
16. username: "xxx",
17. password: "xxx"
18. }
19. let tcpconnectoptions: socket.TCPConnectOptions = {
20. address: netAddress,
21. timeout: 6000,
22. proxy: proxyOptions,
23. }
24. tcp.connect(tcpconnectoptions, (err: BusinessError) => {
25. if (err) {
26. console.error('connect fail');
27. return;
28. }
29. console.info('connect success');
30. })
```

### connect

PhonePC/2in1TabletTVWearable

connect(options: TCPConnectOptions): Promise<void>

连接到指定的IP地址和端口。使用promise异步回调。

说明

在没有执行tcp.bind的情况下，也可以直接调用该接口完成与TCP服务端的连接。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPConnectOptions](js-apis-socket.md#tcpconnectoptions) | 是 | TCPSocket连接的参数，参考[TCPConnectOptions](js-apis-socket.md#tcpconnectoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回TCPSocket连接到指定的IP地址和端口的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions).then(() => {
14. console.info('connect success')
15. }).catch((err: BusinessError) => {
16. console.error('connect fail');
17. });
```

**示例（设置socket代理）：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let socks5Server: socket.NetAddress = {
10. address: '192.168.xx.xxx',
11. port: 8080
12. }
13. let proxyOptions: socket.ProxyOptions = {
14. type : 1,
15. address: socks5Server,
16. username: "xxx",
17. password: "xxx"
18. }
19. let tcpconnectoptions: socket.TCPConnectOptions = {
20. address: netAddress,
21. timeout: 6000,
22. proxy: proxyOptions,
23. }
24. tcp.connect(tcpconnectoptions).then(() => {
25. console.info('connect success')
26. }).catch((err: BusinessError) => {
27. console.error('connect fail');
28. });
```

### send

PhonePC/2in1TabletTVWearable

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

通过TCPSocket连接发送数据。使用callback异步回调。

说明

connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPSendOptions](js-apis-socket.md#tcpsendoptions) | 是 | TCPSocket发送请求的参数，参考[TCPSendOptions](js-apis-socket.md#tcpsendoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions, () => {
14. console.info('connect success');
15. let tcpSendOptions: socket.TCPSendOptions = {
16. data: 'Hello, server!'
17. }
18. tcp.send(tcpSendOptions, (err: BusinessError) => {
19. if (err) {
20. console.error('send fail');
21. return;
22. }
23. console.info('send success');
24. })
25. })
```

### send

PhonePC/2in1TabletTVWearable

send(options: TCPSendOptions): Promise<void>

通过TCPSocket连接发送数据。使用Promise异步回调。

说明

connect方法调用成功后，才可调用此方法。该接口为耗时操作，请在Worker线程或taskpool线程调用该接口。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPSendOptions](js-apis-socket.md#tcpsendoptions) | 是 | TCPSocket发送请求的参数，参考[TCPSendOptions](js-apis-socket.md#tcpsendoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions, () => {
14. console.info('connect success');
15. let tcpSendOptions: socket.TCPSendOptions = {
16. data: 'Hello, server!'
17. }
18. tcp.send(tcpSendOptions).then(() => {
19. console.info('send success');
20. }).catch((err: BusinessError) => {
21. console.error('send fail');
22. });
23. })
```

### close

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

关闭TCPSocket连接。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

6. tcp.close((err: BusinessError) => {
7. if (err) {
8. console.error('close fail');
9. return;
10. }
11. console.info('close success');
12. })
```

### close

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭TCPSocket连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

6. tcp.close().then(() => {
7. console.info('close success');
8. }).catch((err: BusinessError) => {
9. console.error('close fail');
10. });
```

### getRemoteAddress

PhonePC/2in1TabletTVWearable

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

获取对端Socket地址。使用callback异步回调。

说明

connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetAddress](js-apis-socket.md#netaddress)> | 是 | 回调函数。成功时返回对端Socket地址，失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions, () => {
14. console.info('connect success');
15. tcp.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
16. if (err) {
17. console.error('getRemoteAddressfail');
18. return;
19. }
20. console.info('getRemoteAddresssuccess:' + JSON.stringify(data));
21. })
22. });
```

### getRemoteAddress

PhonePC/2in1TabletTVWearable

getRemoteAddress(): Promise<NetAddress>

获取对端Socket地址。使用Promise异步回调。

说明

connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取对端socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions).then(() => {
14. console.info('connect success');
15. tcp.getRemoteAddress().then(() => {
16. console.info('getRemoteAddress success');
17. }).catch((err: BusinessError) => {
18. console.error('getRemoteAddressfail');
19. });
20. }).catch((err: BusinessError) => {
21. console.error('connect fail');
22. });
```

### getState

PhonePC/2in1TabletTVWearable

getState(callback: AsyncCallback<SocketStateBase>): void

获取TCPSocket状态。使用callback异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 是 | 回调函数。成功时获取TCPSocket状态，失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions, () => {
14. console.info('connect success');
15. tcp.getState((err: BusinessError, data: socket.SocketStateBase) => {
16. if (err) {
17. console.error('getState fail');
18. return;
19. }
20. console.info('getState success:' + JSON.stringify(data));
21. });
22. });
```

### getState

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

获取TCPSocket状态。使用Promise异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取TCPSocket状态的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }
13. tcp.connect(tcpconnectoptions).then(() => {
14. console.info('connect success');
15. tcp.getState().then(() => {
16. console.info('getState success');
17. }).catch((err: BusinessError) => {
18. console.error('getState fail');
19. });
20. }).catch((err: BusinessError) => {
21. console.error('connect fail');
22. });
```

### getSocketFd10+

PhonePC/2in1TabletTVWearable

getSocketFd(callback: AsyncCallback<number>): void

获取TCPSocket的文件描述符。使用callback异步回调。

说明

* bind或connect方法调用成功后，才可调用此方法。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，当成功时，返回socket的文件描述符，失败时，返回undefined。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. // 绑定指定网络接口
8. }
9. tcp.bind(bindAddr)
10. let netAddress: socket.NetAddress = {
11. address: '192.168.xx.xxx',
12. port: 8080
13. }
14. let tcpconnectoptions: socket.TCPConnectOptions = {
15. address: netAddress,
16. timeout: 6000
17. }
18. tcp.connect(tcpconnectoptions)
19. tcp.getSocketFd((err: BusinessError, data: number) => {
20. console.error("getSocketFd failed: " + err);
21. console.info("socketFd: " + data);
22. })
```

### getSocketFd10+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取TCPSocket的文件描述符。使用Promise异步回调。

说明

* bind或connect方法调用成功后，才可调用此方法。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回socket的文件描述符。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. // 绑定指定网络接口
8. }
9. tcp.bind(bindAddr)
10. let netAddress: socket.NetAddress = {
11. address: '192.168.xx.xxx',
12. port: 8080
13. }
14. let tcpconnectoptions: socket.TCPConnectOptions = {
15. address: netAddress,
16. timeout: 6000
17. }
18. tcp.connect(tcpconnectoptions)
19. tcp.getSocketFd().then((data: number) => {
20. console.info("socketFd: " + data);
21. })
```

### setExtraOptions

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

设置TCPSocket连接的其他属性。使用callback异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](js-apis-socket.md#tcpextraoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }

14. interface SocketLinger {
15. on: boolean;
16. linger: number;
17. }

19. tcp.connect(tcpconnectoptions, () => {
20. console.info('connect success');
21. let tcpExtraOptions: socket.TCPExtraOptions = {
22. keepAlive: true,
23. OOBInline: true,
24. TCPNoDelay: true,
25. socketLinger: { on: true, linger: 10 } as SocketLinger,
26. receiveBufferSize: 8192,
27. sendBufferSize: 8192,
28. reuseAddress: true,
29. socketTimeout: 3000
30. }
31. tcp.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
32. if (err) {
33. console.error('setExtraOptions fail');
34. return;
35. }
36. console.info('setExtraOptions success');
37. });
38. });
```

### setExtraOptions

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions): Promise<void>

设置TCPSocket连接的其他属性。使用Promise异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](js-apis-socket.md#tcpextraoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }

14. interface SocketLinger {
15. on: boolean;
16. linger: number;
17. }

19. tcp.connect(tcpconnectoptions, () => {
20. console.info('connect success');
21. let tcpExtraOptions: socket.TCPExtraOptions = {
22. keepAlive: true,
23. OOBInline: true,
24. TCPNoDelay: true,
25. socketLinger: { on: true, linger: 10 } as SocketLinger,
26. receiveBufferSize: 8192,
27. sendBufferSize: 8192,
28. reuseAddress: true,
29. socketTimeout: 3000
30. }
31. tcp.setExtraOptions(tcpExtraOptions).then(() => {
32. console.info('setExtraOptions success');
33. }).catch((err: BusinessError) => {
34. console.error('setExtraOptions fail');
35. });
36. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取TCPSocket的本地Socket地址。使用Promise异步回调。

说明

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. family: 1,
8. port: 8080
9. }
10. tcp.bind(bindAddr).then(() => {
11. tcp.getLocalAddress().then((localAddress: socket.NetAddress) => {
12. console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
13. }).catch((err: BusinessError) => {
14. console.error("FAILED! Error:" + JSON.stringify(err));
15. })
16. }).catch((err: BusinessError) => {
17. console.error('bind fail');
18. });
```

### on('message')

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TCPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 是 | 回调函数。返回TCPSocket连接信息。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. tcp.on('message', (value: socket.SocketMessageInfo) => {
6. let messageView = '';
7. let uint8Array = new Uint8Array(value.message);
8. for (let i: number = 0; i < value.message.byteLength; i++) {
9. let messages = uint8Array[i];
10. let message = String.fromCharCode(messages);
11. messageView += message;
12. }
13. console.info('on message message: ' + JSON.stringify(messageView));
14. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
15. });
```

### off('message')

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TCPSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let messageView = '';
6. let callback = (value: socket.SocketMessageInfo) => {
7. for (let i: number = 0; i < value.message.byteLength; i++) {
8. let uint8Array = new Uint8Array(value.message)
9. let messages = uint8Array[i]
10. let message = String.fromCharCode(messages);
11. messageView += message;
12. }
13. console.info('on message message: ' + JSON.stringify(messageView));
14. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
15. }
16. tcp.on('message', callback);
17. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
18. tcp.off('message', callback);
19. tcp.off('message');
```

### on('connect' | 'close')

PhonePC/2in1TabletTVWearable

on(type: 'connect' | 'close', callback: Callback<void>): void

订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。  - 'connect'：连接事件。  - 'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。TCPSocket的连接事件或关闭事件触发时调用回调函数。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. tcp.on('connect', () => {
6. console.info("on connect success")
7. });
8. tcp.on('close', () => {
9. console.info("on close success")
10. });
```

### off('connect' | 'close')

PhonePC/2in1TabletTVWearable

off(type: 'connect' | 'close', callback?: Callback<void>): void

取消订阅TCPSocket的连接事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。  - 'connect'：连接事件。  - 'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let callback1 = () => {
6. console.info("on connect success");
7. }
8. tcp.on('connect', callback1);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. tcp.off('connect', callback1);
11. tcp.off('connect');
12. let callback2 = () => {
13. console.info("on close success");
14. }
15. tcp.on('close', callback2);
16. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
17. tcp.off('close', callback2);
18. tcp.off('close');
```

### on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。TCPSocket连接订阅的某类error事件触发时调用回调函数。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. tcp.on('error', (err: BusinessError) => {
6. console.error("on error, err:" + JSON.stringify(err))
7. });
```

### off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let callback = (err: BusinessError) => {
6. console.error("on error, err:" + JSON.stringify(err));
7. }
8. tcp.on('error', callback);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. tcp.off('error', callback);
11. tcp.off('error');
```

## TCPConnectOptions

PhonePC/2in1TabletTVWearable

TCPSocket连接的参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 否 | 否 | 绑定的地址以及端口。 |
| timeout | number | 否 | 是 | 超时时间，单位毫秒（ms）。默认值为5000。 |
| proxy18+ | [ProxyOptions](js-apis-socket.md#proxyoptions18) | 否 | 是 | 使用的代理信息，默认不使用代理。 |

## TCPSendOptions

PhonePC/2in1TabletTVWearable

TCPSocket发送请求的参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | string| ArrayBuffer | 否 | 否 | 发送的数据。 |
| encoding | string | 否 | 是 | 字符编码(UTF-8，UTF-16BE，UTF-16LE，UTF-16，US-AECII，ISO-8859-1)，默认为UTF-8。 |

## TCPExtraOptions

PhonePC/2in1TabletTVWearable

TCPSocket连接的其他属性。继承自[ExtraOptionsBase](js-apis-socket.md#extraoptionsbase)。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keepAlive | boolean | 否 | 是 | 是否保持连接。默认为false。true：保持连接；false：断开连接。 |
| OOBInline | boolean | 否 | 是 | 是否为OOB内联。默认为false。true：是OOB内联；false：不是OOB内联。 |
| TCPNoDelay | boolean | 否 | 是 | TCPSocket连接是否无时延。默认为false。true：无时延；false：有时延。 |
| socketLinger | {on:boolean, linger:number} | 否 | 是 | socket是否继续逗留。  - on：是否逗留（true：逗留；false：不逗留）。  - linger：逗留时长，单位毫秒（ms），取值范围为0~65535。  当入参on设置为true时，才需要设置。 |

## socket.constructTCPSocketServerInstance10+

PhonePC/2in1TabletTVWearable

constructTCPSocketServerInstance(): TCPSocketServer

创建一个TCPSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TCPSocketServer](js-apis-socket.md#tcpsocketserver10) | 返回一个TCPSocketServer对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
```

## TCPSocketServer10+

PhonePC/2in1TabletTVWearable

TCPSocketServer连接。在调用TCPSocketServer的方法前，需要先通过[socket.constructTCPSocketServerInstance](js-apis-socket.md#socketconstructtcpsocketserverinstance10)创建TCPSocketServer对象。

### listen10+

PhonePC/2in1TabletTVWearable

listen(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用callback异步回调。

说明

服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 目标地址信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr, (err: BusinessError) => {
11. if (err) {
12. console.error("listen fail");
13. return;
14. }
15. console.info("listen success");
16. })
```

### listen10+

PhonePC/2in1TabletTVWearable

listen(address: NetAddress): Promise<void>

绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise异步回调。

说明

服务端使用该方法完成bind，listen，accept操作，bind方法失败会由系统随机分配端口号。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 目标地址信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr).then(() => {
11. console.info('listen success');
12. }).catch((err: BusinessError) => {
13. console.error('listen fail');
14. });
```

### getState10+

PhonePC/2in1TabletTVWearable

getState(callback: AsyncCallback<SocketStateBase>): void

获取TCPSocketServer状态。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr, (err: BusinessError) => {
11. if (err) {
12. console.error("listen fail");
13. return;
14. }
15. console.info("listen success");
16. })
17. tcpServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
18. if (err) {
19. console.error('getState fail');
20. return;
21. }
22. console.info('getState success:' + JSON.stringify(data));
23. })
```

### getState10+

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

获取TCPSocketServer状态。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取TCPSocket状态的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr, (err: BusinessError) => {
11. if (err) {
12. console.error("listen fail");
13. return;
14. }
15. console.info("listen success");
16. })
17. tcpServer.getState().then((data: socket.SocketStateBase) => {
18. console.info('getState success' + JSON.stringify(data));
19. }).catch((err: BusinessError) => {
20. console.error('getState fail');
21. });
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取TCPSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

说明

* [listen](js-apis-socket.md#listen10)方法调用成功后，才可调用此方法。多次调用listen时，会获取最新监听端口绑定的文件描述符。
* 监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close20)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr).then(() => {
11. console.info('listen success');
12. tcpServer.getSocketFd().then((fd: number) => {
13. console.info(`Socket FD：${fd}`);
14. }).catch((err: BusinessError) => {
15. console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
16. });
17. }).catch((err: BusinessError) => {
18. console.error('listen fail');
19. });
```

### setExtraOptions10+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

设置TCPSocketServer连接的其他属性。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TCPSocketServer连接的其他属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr, (err: BusinessError) => {
11. if (err) {
12. console.error("listen fail");
13. return;
14. }
15. console.info("listen success");
16. })

18. interface SocketLinger {
19. on: boolean;
20. linger: number;
21. }

23. let tcpExtraOptions: socket.TCPExtraOptions = {
24. keepAlive: true,
25. OOBInline: true,
26. TCPNoDelay: true,
27. socketLinger: { on: true, linger: 10 } as SocketLinger,
28. receiveBufferSize: 8192,
29. sendBufferSize: 8192,
30. reuseAddress: true,
31. socketTimeout: 3000
32. }
33. tcpServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
34. if (err) {
35. console.error('setExtraOptions fail');
36. return;
37. }
38. console.info('setExtraOptions success');
39. });
```

### setExtraOptions10+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions): Promise<void>

设置TCPSocketServer连接的其他属性。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TCPSocketServer连接的其他属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address:  '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }

11. interface SocketLinger {
12. on: boolean;
13. linger: number;
14. }

16. tcpServer.listen(listenAddr, (err: BusinessError) => {
17. if (err) {
18. console.error("listen fail");
19. return;
20. }
21. console.info("listen success");
22. })

24. let tcpExtraOptions: socket.TCPExtraOptions = {
25. keepAlive: true,
26. OOBInline: true,
27. TCPNoDelay: true,
28. socketLinger: { on: true, linger: 10 } as SocketLinger,
29. receiveBufferSize: 8192,
30. sendBufferSize: 8192,
31. reuseAddress: true,
32. socketTimeout: 3000
33. }
34. tcpServer.setExtraOptions(tcpExtraOptions).then(() => {
35. console.info('setExtraOptions success');
36. }).catch((err: BusinessError) => {
37. console.error('setExtraOptions fail');
38. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取TCPSocketServer的本地Socket地址。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr).then(() => {
11. tcpServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
12. console.info("SUCCESS! Address:" + JSON.stringify(localAddress));
13. }).catch((err: BusinessError) => {
14. console.error("FerrorAILED! Error:" + JSON.stringify(err));
15. })
16. }).catch((err: BusinessError) => {
17. console.error('listen fail');
18. });
```

### on('connect')10+

PhonePC/2in1TabletTVWearable

on(type: 'connect', callback: Callback<TCPSocketConnection>): void

订阅TCPSocketServer的连接事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TCPSocketConnection](js-apis-socket.md#tcpsocketconnection10)> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. let listenAddr: socket.NetAddress = {
7. address:  '192.168.xx.xxx',
8. port: 8080,
9. family: 1
10. }
11. tcpServer.listen(listenAddr, (err: BusinessError) => {
12. if (err) {
13. console.error("listen fail");
14. return;
15. }
16. console.info("listen success");
17. tcpServer.on('connect', (data: socket.TCPSocketConnection) => {
18. console.info(JSON.stringify(data))
19. });
20. })
```

### off('connect')10+

PhonePC/2in1TabletTVWearable

off(type: 'connect', callback?: Callback<TCPSocketConnection>): void

取消订阅TCPSocketServer的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TCPSocketConnection](js-apis-socket.md#tcpsocketconnection10)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. let listenAddr: socket.NetAddress = {
7. address:  '192.168.xx.xxx',
8. port: 8080,
9. family: 1
10. }
11. tcpServer.listen(listenAddr, (err: BusinessError) => {
12. if (err) {
13. console.error("listen fail");
14. return;
15. }
16. console.info("listen success");
17. let callback = (data: socket.TCPSocketConnection) => {
18. console.info('on connect message: ' + JSON.stringify(data));
19. }
20. tcpServer.on('connect', callback);
21. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
22. tcpServer.off('connect', callback);
23. tcpServer.off('connect');
24. })
```

### on('error')10+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocketServer连接的error事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. let listenAddr: socket.NetAddress = {
7. address:  '192.168.xx.xxx',
8. port: 8080,
9. family: 1
10. }
11. tcpServer.listen(listenAddr, (err: BusinessError) => {
12. if (err) {
13. console.error("listen fail");
14. return;
15. }
16. console.info("listen success");
17. tcpServer.on('error', (err: BusinessError) => {
18. console.error("on error, err:" + JSON.stringify(err))
19. });
20. })
```

### off('error')10+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocketServer连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. let listenAddr: socket.NetAddress = {
7. address:  '192.168.xx.xxx',
8. port: 8080,
9. family: 1
10. }
11. tcpServer.listen(listenAddr, (err: BusinessError) => {
12. if (err) {
13. console.error("listen fail");
14. return;
15. }
16. console.info("listen success");
17. let callback = (err: BusinessError) => {
18. console.error("on error, err:" + JSON.stringify(err));
19. }
20. tcpServer.on('error', callback);
21. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
22. tcpServer.off('error', callback);
23. tcpServer.off('error');
24. })
```

### close20+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

TCPSocketServer停止监听并释放通过[listen](js-apis-socket.md#listen10)方法绑定的端口。若多次调用[listen](js-apis-socket.md#listen10)方法，再调用此方法时会释放TCPSocketServer的所有监听端口。使用Promise异步回调。

说明

该方法不会关闭已有连接。如需关闭，请调用[TCPSocketConnection](js-apis-socket.md#tcpsocketconnection10)的[close](js-apis-socket.md#close10)方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080,
8. family: 1
9. }
10. tcpServer.on('connect', (connection: socket.TCPSocketConnection) => {
11. console.info("connection clientId: " + connection.clientId);
12. // 逻辑处理
13. tcpServer.close(); // 停止监听
14. connection.close(); // 关闭当前连接
15. });
16. tcpServer.listen(listenAddr).then(() => {
17. console.info('listen success');
18. }).catch((err: BusinessError) => {
19. console.error('listen fail: ' + err.code);
20. });
```

## TCPSocketConnection10+

PhonePC/2in1TabletTVWearable

TCPSocketConnection连接，即TCPSocket客户端与服务端的连接。在调用TCPSocketConnection的方法前，需要先获取TCPSocketConnection对象。

说明

客户端与服务端成功建立连接后，才能通过返回的TCPSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientId | number | 否 | 否 | 客户端与TCPSocketServer建立连接的id。 |

### send10+

PhonePC/2in1TabletTVWearable

send(options: TCPSendOptions, callback: AsyncCallback<void>): void

通过TCPSocketConnection连接发送数据。使用callback异步回调。

说明

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPSendOptions](js-apis-socket.md#tcpsendoptions) | 是 | TCPSocketConnection发送请求的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

5. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
6. let tcpSendOption: socket.TCPSendOptions = {
7. data: 'Hello, client!'
8. }
9. client.send(tcpSendOption, () => {
10. console.info('send success');
11. });
12. });
```

### send10+

PhonePC/2in1TabletTVWearable

send(options: TCPSendOptions): Promise<void>

通过TCPSocketConnection连接发送数据。使用Promise异步回调。

说明

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPSendOptions](js-apis-socket.md#tcpsendoptions) | 是 | TCPSocketConnection发送请求的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
7. let tcpSendOption: socket.TCPSendOptions = {
8. data: 'Hello, client!'
9. }
10. client.send(tcpSendOption).then(() => {
11. console.info('send success');
12. }).catch((err: BusinessError) => {
13. console.error('send fail');
14. });
15. });
```

### close10+

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

关闭一个与TCPSocket建立的连接。使用callback异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
7. client.close((err: BusinessError) => {
8. if (err) {
9. console.error('close fail');
10. return;
11. }
12. console.info('close success');
13. });
14. });
```

### close10+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭一个与TCPSocket建立的连接。使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
6. client.close().then(() => {
7. console.info('close success');
8. }).catch((err: BusinessError) => {
9. console.error('close fail');
10. });
11. });
```

### getRemoteAddress10+

PhonePC/2in1TabletTVWearable

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

获取对端Socket地址。使用callback异步回调。

说明

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetAddress](js-apis-socket.md#netaddress)> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
6. client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
7. if (err) {
8. console.error('getRemoteAddress fail');
9. return;
10. }
11. console.info('getRemoteAddress success:' + JSON.stringify(data));
12. });
13. });
```

### getRemoteAddress10+

PhonePC/2in1TabletTVWearable

getRemoteAddress(): Promise<NetAddress>

获取对端Socket地址。使用Promise异步回调。

说明

与客户端建立连接后，才可调用此方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取对端socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
6. client.getRemoteAddress().then(() => {
7. console.info('getRemoteAddress success');
8. }).catch((err: BusinessError) => {
9. console.error('getRemoteAddress fail');
10. });
11. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取TCPSocketConnection连接的本地Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address: "192.168.xx.xx",
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr, (err: BusinessError) => {
11. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
12. let netAddress: socket.NetAddress = {
13. address: "192.168.xx.xx",
14. port: 8080
15. }
16. let options: socket.TCPConnectOptions = {
17. address: netAddress,
18. timeout: 6000
19. }
20. tcp.connect(options, (err: BusinessError) => {
21. if (err) {
22. console.error('connect fail');
23. return;
24. }
25. console.info('connect success!');
26. })
27. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
28. client.getLocalAddress().then((localAddress: socket.NetAddress) => {
29. console.info("Family IP Port: " + JSON.stringify(localAddress));
30. }).catch((err: BusinessError) => {
31. console.error('Error:' + JSON.stringify(err));
32. });
33. })
34. })
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取TCPSocketConnection连接的文件描述符。使用Promise异步回调。

说明

* 与客户端建立连接后，才可调用此方法。
* 连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close10)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let listenAddr: socket.NetAddress = {
6. address: "192.168.xx.xx",
7. port: 8080,
8. family: 1
9. }
10. tcpServer.listen(listenAddr, (err: BusinessError) => {
11. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
12. client.getSocketFd().then((fd: number) => {
13. console.info(`Socket FD：${fd}`);
14. }).catch((err: BusinessError) => {
15. console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
16. });
17. })
18. }).catch((err: BusinessError) => {
19. console.error('listen fail');
20. });
```

### on('message')10+

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TCPSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

6. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
7. client.on('message', (value: socket.SocketMessageInfo) => {
8. let messageView = '';
9. let uint8Array = new Uint8Array(value.message);
10. for (let i: number = 0; i < value.message.byteLength; i++) {
11. let messages = uint8Array[i];
12. let message = String.fromCharCode(messages);
13. messageView += message;
14. }
15. console.info('on message message: ' + JSON.stringify(messageView));
16. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
17. });
18. });
```

### off('message')10+

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TCPSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. let callback = (value: socket.SocketMessageInfo) => {
6. let messageView = '';
7. for (let i: number = 0; i < value.message.byteLength; i++) {
8. let uint8Array = new Uint8Array(value.message)
9. let messages = uint8Array[i]
10. let message = String.fromCharCode(messages);
11. messageView += message;
12. }
13. console.info('on message message: ' + JSON.stringify(messageView));
14. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
15. }
16. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
17. client.on('message', callback);
18. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
19. client.off('message', callback);
20. client.off('message');
21. });
```

### on('close')10+

PhonePC/2in1TabletTVWearable

on(type: 'close', callback: Callback<void>): void

订阅TCPSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
6. client.on('close', () => {
7. console.info("on close success")
8. });
9. });
```

### off('close')10+

PhonePC/2in1TabletTVWearable

off(type: 'close', callback?: Callback<void>): void

取消订阅TCPSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
4. let callback = () => {
5. console.info("on close success");
6. }
7. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
8. client.on('close', callback);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. client.off('close', callback);
11. client.off('close');
12. });
```

### on('error')10+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅TCPSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
5. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
6. client.on('error', (err: BusinessError) => {
7. console.error("on error, err:" + JSON.stringify(err))
8. });
9. });
```

### off('error')10+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅TCPSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callback = (err: BusinessError) => {
5. console.error("on error, err:" + JSON.stringify(err));
6. }
7. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
8. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
9. client.on('error', callback);
10. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
11. client.off('error', callback);
12. client.off('error');
13. });
```

## TCP 错误码说明

PhonePC/2in1TabletTVWearable

TCP 其余错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](errorcode-net-socket.md)。

## socket.constructLocalSocketInstance11+

PhonePC/2in1TabletTVWearable

constructLocalSocketInstance(): LocalSocket

创建一个LocalSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalSocket](js-apis-socket.md#localsocket11) | 返回一个LocalSocket对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
```

## LocalSocket11+

PhonePC/2in1TabletTVWearable

LocalSocket连接。在调用LocalSocket的方法前，需要先通过[socket.constructLocalSocketInstance](js-apis-socket.md#socketconstructlocalsocketinstance11)创建LocalSocket对象。

### bind11+

PhonePC/2in1TabletTVWearable

bind(address: LocalAddress): Promise<void>;

绑定本地套接字文件的路径。使用promise异步回调。

说明

bind方法可以使客户端确保有个明确的本地套接字路径，显式的绑定一个本地套接字文件。

bind方法在本地套接字通信中非必须。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [LocalAddress](js-apis-socket.md#localaddress11) | 是 | 本端地址信息，参考[LocalAddress](js-apis-socket.md#localaddress11)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301098 | Address already in use. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance()
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let address : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. client.bind(address).then(() => {
11. console.info('bind success')
12. }).catch((err: Object) => {
13. console.error('failed to bind: ' + JSON.stringify(err))
14. })
```

### connect11+

PhonePC/2in1TabletTVWearable

connect(options: LocalConnectOptions): Promise<void>

连接到指定的套接字文件。使用promise异步回调。

说明

在没有执行localsocket.bind的情况下，也可以直接调用该接口完成与LocalSocket服务端的连接。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LocalConnectOptions](js-apis-socket.md#localconnectoptions11) | 是 | LocalSocket连接的参数，参考[LocalConnectOptions](js-apis-socket.md#localconnectoptions11)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回LocalSocket连接服务端的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301111 | Connection refused. |
| 2301099 | Cannot assign requested address. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let localAddress : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. let connectOpt: socket.LocalConnectOptions = {
11. address: localAddress,
12. timeout: 6000
13. }
14. client.connect(connectOpt).then(() => {
15. console.info('connect success')
16. }).catch((err: Object) => {
17. console.error('connect fail: ' + JSON.stringify(err));
18. });
```

### send11+

PhonePC/2in1TabletTVWearable

send(options: LocalSendOptions): Promise<void>

通过LocalSocket连接发送数据。使用Promise异步回调。

说明

connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LocalSendOptions](js-apis-socket.md#localsendoptions11) | 是 | LocalSocket发送请求的参数，参考[LocalSendOptions](js-apis-socket.md#localsendoptions11)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301011 | Operation would block. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance()
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let localAddress : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. let connectOpt: socket.LocalConnectOptions = {
11. address: localAddress,
12. timeout: 6000
13. }
14. client.connect(connectOpt).then(() => {
15. console.info('connect success')
16. }).catch((err: Object) => {
17. console.error('connect failed: ' + JSON.stringify(err))
18. })
19. let sendOpt: socket.LocalSendOptions = {
20. data: 'Hello world!'
21. }
22. client.send(sendOpt).then(() => {
23. console.info('send success')
24. }).catch((err: Object) => {
25. console.error('send fail: ' + JSON.stringify(err))
26. })
```

### close11+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭LocalSocket连接。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2301009 | Bad file descriptor. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();

5. client.close().then(() => {
6. console.info('close success');
7. }).catch((err: Object) => {
8. console.error('close fail: ' + JSON.stringify(err));
9. });
```

### getState11+

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

获取LocalSocket状态。使用Promise异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取LocalSocket状态的结果。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let localAddress : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. let connectOpt: socket.LocalConnectOptions = {
11. address: localAddress,
12. timeout: 6000
13. }
14. client.connect(connectOpt).then(() => {
15. console.info('connect success');
16. client.getState().then(() => {
17. console.info('getState success');
18. }).catch((err: Object) => {
19. console.error('getState fail: ' + JSON.stringify(err))
20. });
21. }).catch((err: Object) => {
22. console.error('connect fail: ' + JSON.stringify(err));
23. });
```

### getSocketFd11+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取LocalSocket的文件描述符。使用Promise异步回调。

说明

* bind或connect方法调用成功后，才可调用此方法。
* 获取由系统内核分配的唯一文件描述符，用于标识当前使用的套接字。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close11)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回socket的文件描述符。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let localAddress : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. let connectOpt: socket.LocalConnectOptions = {
11. address: localAddress,
12. timeout: 6000
13. }
14. client.connect(connectOpt).then(() => {
15. console.info('connect ok')
16. }).catch((err: Object) => {
17. console.error('connect fail: ' + JSON.stringify(err))
18. })
19. client.getSocketFd().then((data: number) => {
20. console.info("fd: " + data);
21. }).catch((err: Object) => {
22. console.error("getSocketFd failed: " + JSON.stringify(err));
23. })
```

### setExtraOptions11+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: ExtraOptionsBase): Promise<void>

设置LocalSocket的套接字属性。使用Promise异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ExtraOptionsBase](js-apis-socket.md#extraoptionsbase) | 是 | LocalSocket连接的其他属性，参考[ExtraOptionsBase](js-apis-socket.md#extraoptionsbase)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回设置LocalSocket套接字属性的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301009 | Bad file descriptor. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let localAddress : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. let connectOpt: socket.LocalConnectOptions = {
11. address: localAddress,
12. timeout: 6000
13. }
14. client.connect(connectOpt).then(() => {
15. console.info('connect success');
16. let options: socket.ExtraOptionsBase = {
17. receiveBufferSize: 8192,
18. sendBufferSize: 8192,
19. socketTimeout: 3000
20. }
21. client.setExtraOptions(options).then(() => {
22. console.info('setExtraOptions success');
23. }).catch((err: Object) => {
24. console.error('setExtraOptions fail: ' + JSON.stringify(err));
25. });
26. }).catch((err: Object) => {
27. console.error('connect fail: ' + JSON.stringify(err));
28. });
```

### getExtraOptions11+

PhonePC/2in1TabletTVWearable

getExtraOptions(): Promise<ExtraOptionsBase>;

获取LocalSocket的套接字属性。使用Promise异步回调。

说明

bind或connect方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ExtraOptionsBase](js-apis-socket.md#extraoptionsbase)> | 以Promise形式返回设置LocalSocket套接字的属性。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2301009 | Bad file descriptor. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let localAddress : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. let connectOpt: socket.LocalConnectOptions = {
11. address: localAddress,
12. timeout: 6000
13. }
14. client.connect(connectOpt).then(() => {
15. console.info('connect success');
16. client.getExtraOptions().then((options : socket.ExtraOptionsBase) => {
17. console.info('options: ' + JSON.stringify(options));
18. }).catch((err: Object) => {
19. console.error('setExtraOptions fail: ' + JSON.stringify(err));
20. });
21. }).catch((err: Object) => {
22. console.error('connect fail: ' + JSON.stringify(err));
23. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<string>

获取LocalSocket的本地Socket地址。使用Promise异步回调。

说明

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common } from '@kit.AbilityKit';
2. import { socket } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let sandboxPath: string = context.filesDir + '/testSocket';
8. let address : socket.LocalAddress = {
9. address: sandboxPath
10. }
11. client.bind(address).then(() => {
12. console.error('bind success');
13. client.getLocalAddress().then((localPath: string) => {
14. console.info("SUCCESS " + JSON.stringify(localPath));
15. }).catch((err: BusinessError) => {
16. console.error("FAIL " + JSON.stringify(err));
17. })
18. }).catch((err: Object) => {
19. console.error('failed to bind: ' + JSON.stringify(err));
20. })
```

### on('message')11+

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

订阅LocalSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](js-apis-socket.md#localsocketmessageinfo11)> | 是 | 以callback的形式异步返回接收的消息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. client.on('message', (value: socket.LocalSocketMessageInfo) => {
5. const uintArray = new Uint8Array(value.message)
6. let messageView = '';
7. for (let i = 0; i < uintArray.length; i++) {
8. messageView += String.fromCharCode(uintArray[i]);
9. }
10. console.info('total: ' + JSON.stringify(value));
11. console.info('message information: ' + messageView);
12. });
```

### off('message')11+

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

取消订阅LocalSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](js-apis-socket.md#localsocketmessageinfo11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. let messageView = '';
5. let callback = (value: socket.LocalSocketMessageInfo) => {
6. const uintArray = new Uint8Array(value.message)
7. let messageView = '';
8. for (let i = 0; i < uintArray.length; i++) {
9. messageView += String.fromCharCode(uintArray[i]);
10. }
11. console.info('total: ' + JSON.stringify(value));
12. console.info('message information: ' + messageView);
13. }
14. client.on('message', callback);
15. client.off('message');
```

### on('connect')11+

PhonePC/2in1TabletTVWearable

on(type: 'connect', callback: Callback<void>): void

订阅LocalSocket的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。 |
| callback | Callback<void> | 是 | 以callback的形式异步返回与服务端连接的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. client.on('connect', () => {
5. console.info("on connect success")
6. });
```

### off('connect')11+

PhonePC/2in1TabletTVWearable

off(type: 'connect', callback?: Callback<void>): void

取消订阅LocalSocket的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'connect'：LocalSocket的connect事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. let callback = () => {
5. console.info("on connect success");
6. }
7. client.on('connect', callback);
8. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
9. client.off('connect', callback);
10. client.off('connect');
```

### on('close')11+

PhonePC/2in1TabletTVWearable

on(type: 'close', callback: Callback<void>): void

订阅LocalSocket的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅LocalSocket的关闭事件。 |
| callback | Callback<void> | 是 | 以callback的形式异步返回关闭localsocket的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. let callback = () => {
5. console.info("on close success");
6. }
7. client.on('close', callback);
```

### off('close')11+

PhonePC/2in1TabletTVWearable

off(type: 'close', callback?: Callback<void>): void

取消订阅LocalSocket的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'close'：LocalSocket的关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. let callback = () => {
5. console.info("on close success");
6. }
7. client.on('close', callback);
8. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
9. client.off('close', callback);
10. client.off('close');
```

### on('error')11+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅LocalSocket的error事件。 |
| callback | ErrorCallback | 是 | 以callback的形式异步返回出现错误的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. client.on('error', (err: Object) => {
5. console.error("on error, err:" + JSON.stringify(err))
6. });
```

### off('error')11+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：LocalSocket的error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
4. let callback = (err: Object) => {
5. console.error("on error, err:" + JSON.stringify(err));
6. }
7. client.on('error', callback);
8. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
9. client.off('error', callback);
10. client.off('error');
```

## LocalSocketMessageInfo11+

PhonePC/2in1TabletTVWearable

LocalSocket客户端与服务端通信时接收的数据。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | ArrayBuffer | 否 | 否 | 收到的消息数据。 |
| address | string | 否 | 否 | 使用的本地套接字路径。 |
| size | number | 否 | 否 | 数据长度。 |

## LocalAddress11+

PhonePC/2in1TabletTVWearable

LocalSocket本地套接字文件路径信息，在传入套接字路径进行绑定时，会在此路径下创建套接字文件。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 本地套接字路径。 |

## LocalConnectOptions11+

PhonePC/2in1TabletTVWearable

LocalSocket客户端在连接服务端时传入的参数信息。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | [LocalAddress](js-apis-socket.md#localaddress11) | 否 | 否 | 指定的本地套接字路径。 |
| timeout | number | 否 | 是 | 连接服务端的超时时间，单位为毫秒。默认值为0。需要应用手动设置一下，建议设置为5000。 |

## LocalSendOptions11+

PhonePC/2in1TabletTVWearable

LocalSocket发送请求的参数。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | string | ArrayBuffer | 否 | 否 | 需要发送的数据。 |
| encoding | string | 否 | 是 | 字符编码。 |

## ExtraOptionsBase

PhonePC/2in1TabletTVWearable

Socket套接字的基础属性。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| receiveBufferSize | number | 否 | 是 | 接收缓冲区大小（单位：Byte），取值范围0~262144，不设置或设置的值超过取值范围则会默认为8192。 |
| sendBufferSize | number | 否 | 是 | 发送缓冲区大小（单位：Byte），取值范围0~262144，不设置或设置的值超过取值范围则会默认为8192。 |
| reuseAddress | boolean | 否 | 是 | 是否重用地址。true：重用地址；false：不重用地址。 |
| socketTimeout | number | 否 | 是 | 套接字超时时间，单位毫秒（ms）。 |

## socket.constructLocalSocketServerInstance11+

PhonePC/2in1TabletTVWearable

constructLocalSocketServerInstance(): LocalSocketServer

创建一个LocalSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalSocketServer](js-apis-socket.md#localsocketserver11) | 返回一个LocalSocketServer对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
```

## LocalSocketServer11+

PhonePC/2in1TabletTVWearable

LocalSocketServer类。在调用LocalSocketServer的方法前，需要先通过[socket.constructLocalSocketServerInstance](js-apis-socket.md#socketconstructlocalsocketserverinstance11)创建LocalSocketServer对象。

### listen11+

PhonePC/2in1TabletTVWearable

listen(address: LocalAddress): Promise<void>

绑定本地套接字文件，监听并接受与此套接字建立的LocalSocket连接。该接口使用多线程并发处理客户端的数据。使用Promise异步回调。

说明

服务端使用该方法完成bind，listen，accept操作，传入套接字文件路径，调用此接口后会自动生成本地套接字文件。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [LocalAddress](js-apis-socket.md#localaddress11) | 是 | 目标地址信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回执行结果， 成功返回空，失败返回错误码错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303109 | Bad file number. |
| 2301013 | Insufficient permissions. |
| 2301022 | Invalid argument. |
| 2301098 | Address already in use. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let addr: socket.LocalAddress = {
8. address: sandboxPath
9. }
10. server.listen(addr).then(() => {
11. console.info('listen success');
12. }).catch((err: Object) => {
13. console.error('listen fail: ' + JSON.stringify(err));
14. });
```

### getState11+

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

获取LocalSocketServer状态。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取LocalSocketServer状态的结果。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

5. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let sandboxPath: string = context.filesDir + '/testSocket';
8. let listenAddr: socket.LocalAddress = {
9. address: sandboxPath
10. }
11. server.listen(listenAddr).then(() => {
12. console.info("listen success");
13. }).catch((err: Object) => {
14. console.error("listen fail: " + JSON.stringify(err));
15. })
16. server.getState().then((data: socket.SocketStateBase) => {
17. console.info('getState success: ' + JSON.stringify(data));
18. }).catch((err: Object) => {
19. console.error('getState fail: ' + JSON.stringify(err));
20. });
```

### setExtraOptions11+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: ExtraOptionsBase): Promise<void>

设置LocalSocketServer连接的套接字属性。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ExtraOptionsBase](js-apis-socket.md#extraoptionsbase) | 是 | LocalSocketServer连接的其他属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301009 | Bad file descriptor. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let listenAddr: socket.NetAddress = {
8. address: sandboxPath
9. }
10. server.listen(listenAddr).then(() => {
11. console.info("listen success");
12. }).catch((err: Object) => {
13. console.error("listen fail: " + JSON.stringify(err));
14. })

16. let options: socket.ExtraOptionsBase = {
17. receiveBufferSize: 8192,
18. sendBufferSize: 8192,
19. socketTimeout: 3000
20. }
21. server.setExtraOptions(options).then(() => {
22. console.info('setExtraOptions success');
23. }).catch((err: Object) => {
24. console.error('setExtraOptions fail: ' + JSON.stringify(err));
25. });
```

### getExtraOptions11+

PhonePC/2in1TabletTVWearable

getExtraOptions(): Promise<ExtraOptionsBase>;

获取LocalSocketServer中连接的套接字的属性。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ExtraOptionsBase](js-apis-socket.md#extraoptionsbase)> | 以Promise形式返回套接字的属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let listenAddr: socket.LocalAddress = {
8. address: sandboxPath
9. }
10. server.listen(listenAddr).then(() => {
11. console.info("listen success");
12. }).catch((err: Object) => {
13. console.error("listen fail: " + JSON.stringify(err));
14. })
15. server.getExtraOptions().then((options: socket.ExtraOptionsBase) => {
16. console.info('options: ' + JSON.stringify(options));
17. }).catch((err: Object) => {
18. console.error('getExtraOptions fail: ' + JSON.stringify(err));
19. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<string>

获取LocalSocketServer中本地Socket地址。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common } from '@kit.AbilityKit';
2. import { socket } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let sandboxPath: string = context.filesDir + '/testSocket';
8. let listenAddr: socket.LocalAddress = {
9. address: sandboxPath
10. }
11. server.listen(listenAddr).then(() => {
12. console.info("listen success");
13. server.getLocalAddress().then((localPath: string) => {
14. console.info("SUCCESS " + JSON.stringify(localPath));
15. }).catch((err: BusinessError) => {
16. console.error("FAIL " + JSON.stringify(err));
17. })
18. }).catch((err: Object) => {
19. console.error("listen fail: " + JSON.stringify(err));
20. })
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取LocalSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

说明

* [listen](js-apis-socket.md#listen11)方法调用成功后，才可调用此方法。
* 监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close20-1)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let listenAddr : socket.LocalAddress = {
8. address: sandboxPath
9. }

11. server.listen(listenAddr).then(() => {
12. console.info("listen success");
13. server.getSocketFd().then((fd: number) => {
14. console.info(`Socket FD：${fd}`);
15. }).catch((err: Object) => {
16. console.error(`getSocketFd fail: ${JSON.stringify(err)}`);
17. });
18. }).catch((err: Object) => {
19. console.error("listen fail: " + JSON.stringify(err));
20. })
```

### on('connect')11+

PhonePC/2in1TabletTVWearable

on(type: 'connect', callback: Callback<LocalSocketConnection>): void

订阅LocalSocketServer的连接事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[LocalSocketConnection](js-apis-socket.md#localsocketconnection11)> | 是 | 以callback的形式异步返回接收到客户端连接的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. server.on('connect', (connection: socket.LocalSocketConnection) => {
5. if (connection) {
6. console.info('accept a client')
7. }
8. });
```

### off('connect')11+

PhonePC/2in1TabletTVWearable

off(type: 'connect', callback?: Callback<LocalSocketConnection>): void

取消订阅LocalSocketServer的连接事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'connect'：LocalSocketServer的连接事件。 |
| callback | Callback<[LocalSocketConnection](js-apis-socket.md#localsocketconnection11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. let callback = (connection: socket.LocalSocketConnection) => {
5. if (connection) {
6. console.info('accept a client')
7. }
8. }
9. server.on('connect', callback);
10. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
11. server.off('connect', callback);
12. server.off('connect');
```

### on('error')11+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocketServer连接的error事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 以callback的形式异步返回出现错误的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. server.on('error', (err: Object) => {
5. console.error("on error, err:" + JSON.stringify(err))
6. });
```

### off('error')11+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocketServer连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. let callback = (err: Object) => {
5. console.error("on error, err:" + JSON.stringify(err));
6. }
7. server.on('error', callback);
8. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
9. server.off('error', callback);
10. server.off('error');
```

### close20+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

LocalSocketServer停止监听并释放通过[listen](js-apis-socket.md#listen11)方法绑定的监听端口。使用Promise异步回调。

说明

该方法不会关闭已有连接。如需关闭，请调用[LocalSocketConnection](js-apis-socket.md#localsocketconnection11)的[close](js-apis-socket.md#close11-1)方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let localserver: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let sandboxPath: string = context.filesDir + '/testSocket';
8. let addr: socket.LocalAddress = {
9. address: sandboxPath
10. }
11. localserver.on('connect', (connection: socket.LocalSocketConnection) => {
12. console.info("connection clientId: " + connection.clientId);
13. // 逻辑处理
14. localserver.close(); // 停止监听
15. connection.close(); // 关闭当前连接
16. });
17. localserver.listen(addr).then(() => {
18. console.info('listen success');
19. }).catch((err: BusinessError) => {
20. console.error('listen fail: ' + err.code);
21. });
```

## LocalSocketConnection11+

PhonePC/2in1TabletTVWearable

LocalSocketConnection连接，即LocalSocket客户端与服务端的会话连接。在调用LocalSocketConnection的方法前，需要先获取LocalSocketConnection对象。

说明

客户端与服务端成功建立连接后，才能通过返回的LocalSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientId | number | 否 | 否 | 客户端与服务端建立的会话连接的id。 |

### send11+

PhonePC/2in1TabletTVWearable

send(options: LocalSendOptions): Promise<void>

通过LocalSocketConnection连接对象发送数据。使用Promise异步回调。

说明

服务端与客户端建立连接后，服务端通过connect事件回调得到LocalSocketConnection连接对象后，才可使用连接对象调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LocalSendOptions](js-apis-socket.md#localsendoptions11) | 是 | LocalSocketConnection发送请求的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2301011 | Operation would block. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();

5. server.on('connect', (connection: socket.LocalSocketConnection) => {
6. let sendOptions: socket.LocalSendOptions = {
7. data: 'Hello, client!'
8. }
9. connection.send(sendOptions).then(() => {
10. console.info('send success');
11. }).catch((err: Object) => {
12. console.error('send fail: ' + JSON.stringify(err));
13. });
14. });
```

### close11+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭一个LocalSocket客户端与服务端建立的连接。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2301009 | Bad file descriptor. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. server.on('connect', (connection: socket.LocalSocketConnection) => {
5. connection.close().then(() => {
6. console.info('close success');
7. }).catch((err: Object) => {
8. console.error('close fail: ' + JSON.stringify(err));
9. });
10. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<string>

获取LocalSocketConnection连接中的本地Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common } from '@kit.AbilityKit';
2. import { socket } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
6. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. let sandboxPath: string = context.filesDir + '/testSocket';
8. let localAddr: socket.LocalAddress = {
9. address: sandboxPath
10. }
11. server.listen(localAddr).then(() => {
12. console.info('listen success');
13. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
14. let connectOpt: socket.LocalConnectOptions = {
15. address: localAddr,
16. timeout: 6000
17. }
18. client.connect(connectOpt).then(() => {
19. server.getLocalAddress().then((localPath: string) => {
20. console.info("success, localPath is" + JSON.stringify(localPath));
21. }).catch((err: BusinessError) => {
22. console.error("FAIL " + JSON.stringify(err));
23. })
24. }).catch((err: Object) => {
25. console.error('connect fail: ' + JSON.stringify(err));
26. });
27. });
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取LocalSocketConnection连接的文件描述符。使用Promise异步回调。

说明

* 成功建立连接后，才可调用此方法。
* 连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close11-1)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let listenAddr : socket.LocalAddress = {
8. address: sandboxPath
9. }
10. server.on('connect', (connection: socket.LocalSocketConnection) => {
11. connection.getSocketFd().then((fd: number) => {
12. console.info(`Socket FD：${fd}`);
13. }).catch((err: Object) => {
14. console.error(`getSocketFd fail: ${JSON.stringify(err)}`);
15. });
16. });
17. server.listen(listenAddr).then(() => {
18. console.info("listen success");
19. }).catch((err: Object) => {
20. console.error(`listen fail: ${JSON.stringify(err)}`);
21. })
```

### on('message')11+

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<LocalSocketMessageInfo>): void

订阅LocalSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](js-apis-socket.md#localsocketmessageinfo11)> | 是 | 以callback的形式异步返回接收到的来自客户端的消息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

```
1. import { socket } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';

4. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
5. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let sandboxPath: string = context.filesDir + '/testSocket';
7. let listenAddr: socket.LocalAddress = {
8. address: sandboxPath
9. }
10. server.listen(listenAddr).then(() => {
11. console.info("listen success");
12. }).catch((err: Object) => {
13. console.error("listen fail: " + JSON.stringify(err));
14. });
15. server.on('connect', (connection: socket.LocalSocketConnection) => {
16. connection.on('message', (value: socket.LocalSocketMessageInfo) => {
17. const uintArray = new Uint8Array(value.message);
18. let messageView = '';
19. for (let i = 0; i < uintArray.length; i++) {
20. messageView += String.fromCharCode(uintArray[i]);
21. }
22. console.info('total: ' + JSON.stringify(value));
23. console.info('message information: ' + messageView);
24. });
25. });
```

### off('message')11+

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<LocalSocketMessageInfo>): void

取消订阅LocalSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[LocalSocketMessageInfo](js-apis-socket.md#localsocketmessageinfo11)> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. let callback = (value: socket.LocalSocketMessageInfo) => {
5. const uintArray = new Uint8Array(value.message)
6. let messageView = '';
7. for (let i = 0; i < uintArray.length; i++) {
8. messageView += String.fromCharCode(uintArray[i]);
9. }
10. console.info('total: ' + JSON.stringify(value));
11. console.info('message information: ' + messageView);
12. }
13. server.on('connect', (connection: socket.LocalSocketConnection) => {
14. connection.on('message', callback);
15. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
16. connection.off('message', callback);
17. connection.off('message');
18. });
```

### on('close')11+

PhonePC/2in1TabletTVWearable

on(type: 'close', callback: Callback<void>): void

订阅LocalSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 是 | 以callback的形式异步返回会话关闭的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. server.on('connect', (connection: socket.LocalSocketConnection) => {
5. connection.on('close', () => {
6. console.info("on close success")
7. });
8. });
```

### off('close')11+

PhonePC/2in1TabletTVWearable

off(type: 'close', callback?: Callback<void>): void

取消订阅LocalSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. let callback = () => {
5. console.info("on close success");
6. }
7. server.on('connect', (connection: socket.LocalSocketConnection) => {
8. connection.on('close', callback);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. connection.off('close', callback);
11. connection.off('close');
12. });
```

### on('error')11+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅LocalSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 以callback的形式异步返回出现错误的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
4. server.on('connect', (connection: socket.LocalSocketConnection) => {
5. connection.on('error', (err: Object) => {
6. console.error("on error, err:" + JSON.stringify(err))
7. });
8. });
```

### off('error')11+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅LocalSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let callback = (err: Object) => {
4. console.error("on error, err: " + JSON.stringify(err));
5. }
6. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
7. server.on('connect', (connection: socket.LocalSocketConnection) => {
8. connection.on('error', callback);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. connection.off('error', callback);
11. connection.off('error');
12. });
```

## LocalSocket 错误码说明

PhonePC/2in1TabletTVWearable

LocalSocket 错误码映射形式为：2301000 + Linux内核错误码。

错误码的详细介绍参见[Socket错误码](errorcode-net-socket.md)。

## socket.constructTLSSocketInstance9+

PhonePC/2in1TabletTVWearable

constructTLSSocketInstance(): TLSSocket

创建并返回一个TLSSocket对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值:**

| 类型 | 说明 |
| --- | --- |
| [TLSSocket](js-apis-socket.md#tlssocket9) | 返回一个TLSSocket对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';

3. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
```

## socket.constructTLSSocketInstance12+

PhonePC/2in1TabletTVWearable

constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket

将TCPSocket升级为TLSSocket，创建并返回一个TLSSocket对象。

说明

需要确保TCPSocket已连接，并且当前已经没有传输数据，再调用constructTLSSocketInstance升级TLSSocket。当升级成功后，无需对TCPSocket对象调用close方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tcpSocket | [TCPSocket](js-apis-socket.md#tcpsocket) | 是 | 需要进行升级的TCPSocket对象。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| [TLSSocket](js-apis-socket.md#tlssocket9) | 返回一个TLSSocket对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2300002 | System internal error. |
| 2303601 | Invalid socket FD. |
| 2303602 | Socket is not connected. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tcpconnectoptions: socket.TCPConnectOptions = {
10. address: netAddress,
11. timeout: 6000
12. }

14. tcp.connect(tcpconnectoptions, (err: BusinessError) => {
15. if (err) {
16. console.error('connect fail');
17. return;
18. }
19. console.info('connect success');

21. // 确保TCPSocket已连接后，再升级TLSSocket
22. let tls: socket.TLSSocket = socket.constructTLSSocketInstance(tcp);
23. })
```

## TLSSocket9+

PhonePC/2in1TabletTVWearable

TLSSocket连接。在调用TLSSocket的方法前，需要先通过[socket.constructTLSSocketInstance](js-apis-socket.md#socketconstructtlssocketinstance9)创建TLSSocket对象。

### bind9+

PhonePC/2in1TabletTVWearable

bind(address: NetAddress, callback: AsyncCallback<void>): void

绑定IP地址和端口。使用callback异步回调。

说明

如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 本端地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回TLSSocket绑定本机的IP地址和端口的结果。失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2303198 | Address already in use. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
```

### bind9+

PhonePC/2in1TabletTVWearable

bind(address: NetAddress): Promise<void>

绑定IP地址和端口。使用Promise异步回调。

说明

如果TLSSocket对象是通过TCPSocket对象升级创建的，可以不用执行bind方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 是 | 本端地址信息，参考[NetAddress](js-apis-socket.md#netaddress)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回TLSSocket绑定本机的IP地址和端口的结果。失败返回错误码，错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2303198 | Address already in use. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr).then(() => {
10. console.info('bind success');
11. }).catch((err: BusinessError) => {
12. console.error('bind fail');
13. });
```

### getState9+

PhonePC/2in1TabletTVWearable

getState(callback: AsyncCallback<SocketStateBase>): void

在TLSSocket的bind成功之后，获取TLSSocket状态。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 是 | 回调函数。成功返回TLSSocket状态，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. tls.getState((err: BusinessError, data: socket.SocketStateBase) => {
17. if (err) {
18. console.error('getState fail');
19. return;
20. }
21. console.info('getState success:' + JSON.stringify(data));
22. });
```

### getState9+

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

在TLSSocket的bind成功之后，获取TLSSocket状态。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取TLSSocket状态的结果。失败返回错误码，错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. tls.getState().then(() => {
17. console.info('getState success');
18. }).catch((err: BusinessError) => {
19. console.error('getState fail');
20. });
```

### setExtraOptions9+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](js-apis-socket.md#tcpextraoptions)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回设置TCPSocket连接的其他属性的结果，失败返回错误码、错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });

17. interface SocketLinger {
18. on: boolean;
19. linger: number;
20. }

22. let tcpExtraOptions: socket.TCPExtraOptions = {
23. keepAlive: true,
24. OOBInline: true,
25. TCPNoDelay: true,
26. socketLinger: { on: true, linger: 10 } as SocketLinger,
27. receiveBufferSize: 8192,
28. sendBufferSize: 8192,
29. reuseAddress: true,
30. socketTimeout: 3000
31. }
32. tls.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
33. if (err) {
34. console.error('setExtraOptions fail');
35. return;
36. }
37. console.info('setExtraOptions success');
38. });
```

### setExtraOptions9+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions): Promise<void>

在TLSSocket的bind成功之后，设置TCPSocket连接的其他属性。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TCPSocket连接的其他属性，参考[TCPExtraOptions](js-apis-socket.md#tcpextraoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });

17. interface SocketLinger {
18. on: boolean;
19. linger: number;
20. }

22. let tcpExtraOptions: socket.TCPExtraOptions = {
23. keepAlive: true,
24. OOBInline: true,
25. TCPNoDelay: true,
26. socketLinger: { on: true, linger: 10 } as SocketLinger,
27. receiveBufferSize: 8192,
28. sendBufferSize: 8192,
29. reuseAddress: true,
30. socketTimeout: 3000
31. }
32. tls.setExtraOptions(tcpExtraOptions).then(() => {
33. console.info('setExtraOptions success');
34. }).catch((err: BusinessError) => {
35. console.error('setExtraOptions fail');
36. });
```

### on('message')9+

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TLSSocket连接的接收消息事件。使用callback异步回调。

说明

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 是 | 回调函数。TLSSocket连接订阅某类接受消息事件触发的调用函数，返回TLSSocket连接信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. tls.on('message', (value: socket.SocketMessageInfo) => {
16. let messageView = '';
17. let uint8Array = new Uint8Array(value.message);
18. for (let i: number = 0; i < value.message.byteLength; i++) {
19. let messages = uint8Array[i];
20. let message = String.fromCharCode(messages);
21. messageView += message;
22. }
23. console.info('on message message: ' + JSON.stringify(messageView));
24. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
25. });
26. });
```

### off('message')9+

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TLSSocket连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 否 | 回调函数。TLSSocket连接取消订阅某类接受消息事件触发的调用函数，返回TLSSocket连接信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let messageView = '';
6. let callback = (value: socket.SocketMessageInfo) => {
7. for (let i: number = 0; i < value.message.byteLength; i++) {
8. let uint8Array = new Uint8Array(value.message)
9. let messages = uint8Array[i]
10. let message = String.fromCharCode(messages);
11. messageView += message;
12. }
13. console.info('on message message: ' + JSON.stringify(messageView));
14. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
15. }
16. tls.on('message', callback);
17. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
18. tls.off('message', callback);
```

### on('connect' | 'close')9+

PhonePC/2in1TabletTVWearable

on(type: 'connect' | 'close', callback: Callback<void>): void

订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

说明

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。  - 'connect'：连接事件。  - 'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。TLSSocket连接订阅某类事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. tls.on('connect', () => {
16. console.info("on connect success")
17. });
18. tls.on('close', () => {
19. console.info("on close success")
20. });
21. });
```

### off('connect' | 'close')9+

PhonePC/2in1TabletTVWearable

off(type: 'connect' | 'close', callback?: Callback<void>): void

取消订阅TLSSocket的连接事件或关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。  - 'connect'：连接事件。  - 'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。TLSSocket连接订阅某类事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let callback1 = () => {
6. console.info("on connect success");
7. }
8. tls.on('connect', callback1);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. tls.off('connect', callback1);
11. tls.off('connect');
12. let callback2 = () => {
13. console.info("on close success");
14. }
15. tls.on('close', callback2);
16. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
17. tls.off('close', callback2);
```

### on('error')9+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocket连接的error事件。使用callback异步回调。

说明

bind方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。TLSSocket连接订阅某类error事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. tls.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. tls.on('error', (err: BusinessError) => {
16. console.error("on error, err:" + JSON.stringify(err))
17. });
18. });
```

### off('error')9+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocket连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。TLSSocket连接取消订阅某类error事件触发的调用函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. let callback = (err: BusinessError) => {
6. console.error("on error, err:" + JSON.stringify(err));
7. }
8. tls.on('error', callback);
9. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
10. tls.off('error', callback);
```

### connect9+

PhonePC/2in1TabletTVWearable

connect(options: TLSConnectOptions, callback: AsyncCallback<void>): void

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，使用callback异步回调。需要注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TLSConnectOptions](js-apis-socket.md#tlsconnectoptions9) | 是 | TLSSocket连接所需要的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，成功无返回，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303104 | Interrupted system call. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303188 | Socket operation on non-socket. |
| 2303191 | Incorrect socket protocol type. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303210 | Connection timed out. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. // 绑定指定网络接口
8. }
9. tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. let twoWayNetAddr: socket.NetAddress = {
17. address: '192.168.xx.xxx',
18. port: 8080
19. }
20. let twoWaySecureOptions: socket.TLSSecureOptions = {
21. key: "xxxx",
22. cert: "xxxx",
23. ca: ["xxxx"],
24. password: "xxxx",
25. protocols: socket.Protocol.TLSv12,
26. useRemoteCipherPrefer: true,
27. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
28. cipherSuite: "AES256-SHA256"
29. }
30. let tlsConnectOptions: socket.TLSConnectOptions = {
31. address: twoWayNetAddr,
32. secureOptions: twoWaySecureOptions,
33. ALPNProtocols: ["spdy/1", "http/1.1"]
34. }

36. tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
37. console.error("connect callback error" + err);
38. });

40. let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
41. tlsOneWay.bind(bindAddr, (err: BusinessError) => {
42. if (err) {
43. console.error('bind fail');
44. return;
45. }
46. console.info('bind success');
47. });
48. let oneWayNetAddr: socket.NetAddress = {
49. address: '192.168.xx.xxx',
50. port: 8080
51. }
52. let oneWaySecureOptions: socket.TLSSecureOptions = {
53. ca: ["xxxx", "xxxx"],
54. cipherSuite: "AES256-SHA256"
55. }
56. let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
57. address: oneWayNetAddr,
58. secureOptions: oneWaySecureOptions
59. }
60. tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
61. console.error("connect callback error" + err);
62. });
```

**示例（设置socket代理）：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // 双向认证
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. // 绑定指定网络接口
8. }
9. tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. let twoWayNetAddr: socket.NetAddress = {
17. address: '192.168.xx.xxx',
18. port: 8080
19. }
20. let socks5Server: socket.NetAddress = {
21. address: '192.168.xx.xxx',
22. port: 8080
23. }
24. let twoWaySecureOptions: socket.TLSSecureOptions = {
25. key: "xxxx",
26. cert: "xxxx",
27. ca: ["xxxx"],
28. password: "xxxx",
29. protocols: socket.Protocol.TLSv12,
30. useRemoteCipherPrefer: true,
31. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
32. cipherSuite: "AES256-SHA256"
33. }
34. let proxyOptions: socket.ProxyOptions = {
35. type : 1,
36. address: socks5Server,
37. username: "xxx",
38. password: "xxx"
39. }
40. let tlsConnectOptions: socket.TLSConnectOptions = {
41. address: twoWayNetAddr,
42. secureOptions: twoWaySecureOptions,
43. ALPNProtocols: ["spdy/1", "http/1.1"],
44. proxy: proxyOptions,
45. }

47. tlsTwoWay.connect(tlsConnectOptions, (err: BusinessError) => {
48. console.error("connect callback error" + err);
49. });

51. let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // 单向认证
52. tlsOneWay.bind(bindAddr, (err: BusinessError) => {
53. if (err) {
54. console.error('bind fail');
55. return;
56. }
57. console.info('bind success');
58. });
59. let oneWayNetAddr: socket.NetAddress = {
60. address: '192.168.xx.xxx',
61. port: 8080
62. }
63. let oneWaySecureOptions: socket.TLSSecureOptions = {
64. ca: ["xxxx", "xxxx"],
65. cipherSuite: "AES256-SHA256"
66. }
67. let oneWayProxyOptions: socket.ProxyOptions = {
68. type : 1,
69. address: socks5Server,
70. username: "xxx",
71. password: "xxx"
72. }
73. let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
74. address: oneWayNetAddr,
75. secureOptions: oneWaySecureOptions,
76. proxy: oneWayProxyOptions,
77. }
78. tlsOneWay.connect(tlsOneWayConnectOptions, (err: BusinessError) => {
79. console.error("connect callback error" + err);
80. });
```

### connect9+

PhonePC/2in1TabletTVWearable

connect(options: TLSConnectOptions): Promise<void>

在TLSSocket上bind成功之后，进行通信连接，并创建和初始化TLS会话，实现建立连接过程，启动与服务器的TLS/SSL握手，实现数据传输功能，该连接包括两种认证方式，单向认证与双向认证，使用Promise异步回调。需要注意options入参下secureOptions内的ca在API11及之前的版本为必填项，需填入服务端的ca证书(用于认证校验服务端的数字证书)，证书内容以"-----BEGIN CERTIFICATE-----"开头，以"-----END CERTIFICATE-----"结尾，自API12开始，为非必填项。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TLSConnectOptions](js-apis-socket.md#tlsconnectoptions9) | 是 | 连接所需要的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回，成功无返回，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303104 | Interrupted system call. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303188 | Socket operation on non-socket. |
| 2303191 | Incorrect socket protocol type. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303210 | Connection timed out. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |
| 2301206 | Socks5 failed to connect to the proxy server. |
| 2301207 | Socks5 username or password is invalid. |
| 2301208 | Socks5 failed to connect to the remote server. |
| 2301209 | Socks5 failed to negotiate the authentication method. |
| 2301210 | Socks5 failed to send the message. |
| 2301211 | Socks5 failed to receive the message. |
| 2301212 | Socks5 serialization error. |
| 2301213 | Socks5 deserialization error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // Two way authentication
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. // 绑定指定网络接口
8. }
9. tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. let twoWayNetAddr: socket.NetAddress = {
17. address: '192.168.xx.xxx',
18. port: 8080
19. }
20. let twoWaySecureOptions: socket.TLSSecureOptions = {
21. key: "xxxx",
22. cert: "xxxx",
23. ca: ["xxxx"],
24. password: "xxxx",
25. protocols: socket.Protocol.TLSv12,
26. useRemoteCipherPrefer: true,
27. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
28. cipherSuite: "AES256-SHA256"
29. }
30. let tlsConnectOptions: socket.TLSConnectOptions = {
31. address: twoWayNetAddr,
32. secureOptions: twoWaySecureOptions,
33. ALPNProtocols: ["spdy/1", "http/1.1"]
34. }

36. tlsTwoWay.connect(tlsConnectOptions).then(() => {
37. console.info("connect successfully");
38. }).catch((err: BusinessError) => {
39. console.error("connect failed " + JSON.stringify(err));
40. });

42. let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // One way authentication
43. tlsOneWay.bind(bindAddr, (err: BusinessError) => {
44. if (err) {
45. console.error('bind fail');
46. return;
47. }
48. console.info('bind success');
49. });
50. let oneWayNetAddr: socket.NetAddress = {
51. address: '192.168.xx.xxx',
52. port: 8080
53. }
54. let oneWaySecureOptions: socket.TLSSecureOptions = {
55. ca: ["xxxx", "xxxx"],
56. cipherSuite: "AES256-SHA256"
57. }
58. let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
59. address: oneWayNetAddr,
60. secureOptions: oneWaySecureOptions
61. }
62. tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
63. console.info("connect successfully");
64. }).catch((err: BusinessError) => {
65. console.error("connect failed " + JSON.stringify(err));
66. });
```

**示例（设置socket代理）：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsTwoWay: socket.TLSSocket = socket.constructTLSSocketInstance();  // 双向认证
5. let bindAddr: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. // 绑定指定网络接口
8. }
9. tlsTwoWay.bind(bindAddr, (err: BusinessError) => {
10. if (err) {
11. console.error('bind fail');
12. return;
13. }
14. console.info('bind success');
15. });
16. let twoWayNetAddr: socket.NetAddress = {
17. address: '192.168.xx.xxx',
18. port: 8080
19. }
20. let socks5Server: socket.NetAddress = {
21. address: '192.168.xx.xxx',
22. port: 8080
23. }
24. let twoWaySecureOptions: socket.TLSSecureOptions = {
25. key: "xxxx",
26. cert: "xxxx",
27. ca: ["xxxx"],
28. password: "xxxx",
29. protocols: socket.Protocol.TLSv12,
30. useRemoteCipherPrefer: true,
31. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
32. cipherSuite: "AES256-SHA256"
33. }
34. let proxyOptions: socket.ProxyOptions = {
35. type : 1,
36. address: socks5Server,
37. username: "xxx",
38. password: "xxx"
39. }
40. let tlsConnectOptions: socket.TLSConnectOptions = {
41. address: twoWayNetAddr,
42. secureOptions: twoWaySecureOptions,
43. ALPNProtocols: ["spdy/1", "http/1.1"],
44. proxy: proxyOptions,
45. }

47. tlsTwoWay.connect(tlsConnectOptions).then(() => {
48. console.info("connect successfully");
49. }).catch((err: BusinessError) => {
50. console.error("connect failed " + JSON.stringify(err));
51. });

53. let tlsOneWay: socket.TLSSocket = socket.constructTLSSocketInstance(); // 单向认证
54. tlsOneWay.bind(bindAddr, (err: BusinessError) => {
55. if (err) {
56. console.error('bind fail');
57. return;
58. }
59. console.info('bind success');
60. });
61. let oneWayNetAddr: socket.NetAddress = {
62. address: '192.168.xx.xxx',
63. port: 8080
64. }
65. let oneWaySecureOptions: socket.TLSSecureOptions = {
66. ca: ["xxxx", "xxxx"],
67. cipherSuite: "AES256-SHA256"
68. }
69. let oneWayProxyOptions: socket.ProxyOptions = {
70. type : 1,
71. address: socks5Server,
72. username: "xxx",
73. password: "xxx"
74. }
75. let tlsOneWayConnectOptions: socket.TLSConnectOptions = {
76. address: oneWayNetAddr,
77. secureOptions: oneWaySecureOptions,
78. proxy: oneWayProxyOptions,
79. }
80. tlsOneWay.connect(tlsOneWayConnectOptions).then(() => {
81. console.info("connect successfully");
82. }).catch((err: BusinessError) => {
83. console.error("connect failed " + JSON.stringify(err));
84. });
```

### getRemoteAddress9+

PhonePC/2in1TabletTVWearable

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

在TLSSocket通信连接成功之后，获取对端Socket地址。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetAddress](js-apis-socket.md#netaddress)> | 是 | 回调函数。成功返回对端的socket地址，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
6. if (err) {
7. console.error('getRemoteAddress fail');
8. return;
9. }
10. console.info('getRemoteAddress success:' + JSON.stringify(data));
11. });
```

### getRemoteAddress9+

PhonePC/2in1TabletTVWearable

getRemoteAddress(): Promise<NetAddress>

在TLSSocket通信连接成功之后，获取对端Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取对端socket地址的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getRemoteAddress().then(() => {
6. console.info('getRemoteAddress success');
7. }).catch((err: BusinessError) => {
8. console.error('getRemoteAddress fail');
9. });
```

### getCertificate9+

PhonePC/2in1TabletTVWearable

getCertificate(callback: AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>): void

在TLSSocket通信连接成功之后，获取本地的数字证书，该接口只适用于双向认证时，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 是 | 回调函数，成功返回本地的证书，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
6. if (err) {
7. console.error("getCertificate callback error = " + err);
8. } else {
9. console.info("getCertificate callback = " + data);
10. }
11. });
```

### getCertificate9+

PhonePC/2in1TabletTVWearable

getCertificate():Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>

在TLSSocket通信连接之后，获取本地的数字证书，该接口只适用于双向认证时，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 以Promise形式返回本地的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
6. tls.getCertificate().then((data: socket.X509CertRawData) => {
7. const decoder = util.TextDecoder.create();
8. const str = decoder.decodeToString(data.data);
9. console.info("getCertificate: " + str);
10. }).catch((err: BusinessError) => {
11. console.error("failed" + err);
12. });
```

### getRemoteCertificate9+

PhonePC/2in1TabletTVWearable

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>): void

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 是 | 回调函数，返回服务端的证书。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
6. tls.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
7. if (err) {
8. console.error("getRemoteCertificate callback error = " + err);
9. } else {
10. const decoder = util.TextDecoder.create();
11. const str = decoder.decodeToString(data.data);
12. console.info("getRemoteCertificate callback = " + str);
13. }
14. });
```

### getRemoteCertificate9+

PhonePC/2in1TabletTVWearable

getRemoteCertificate():Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>

在TLSSocket通信连接成功之后，获取服务端的数字证书，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 以Promise形式返回服务端的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
6. tls.getRemoteCertificate().then((data: socket.X509CertRawData) => {
7. const decoder = util.TextDecoder.create();
8. const str = decoder.decodeToString(data.data);
9. console.info("getRemoteCertificate:" + str);
10. }).catch((err: BusinessError) => {
11. console.error("failed" + err);
12. });
```

### getProtocol9+

PhonePC/2in1TabletTVWearable

getProtocol(callback: AsyncCallback<string>): void

在TLSSocket通信连接成功之后，获取通信的协议版本，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回通信的协议。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getProtocol((err: BusinessError, data: string) => {
6. if (err) {
7. console.error("getProtocol callback error = " + err);
8. } else {
9. console.info("getProtocol callback = " + data);
10. }
11. });
```

### getProtocol9+

PhonePC/2in1TabletTVWearable

getProtocol():Promise<string>

在TLSSocket通信连接成功之后，获取通信的协议版本，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回通信的协议。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getProtocol().then((data: string) => {
6. console.info(data);
7. }).catch((err: BusinessError) => {
8. console.error("failed" + err);
9. });
```

### getCipherSuite9+

PhonePC/2in1TabletTVWearable

getCipherSuite(callback: AsyncCallback<Array<string>>): void

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回通信双方支持的加密套件。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getCipherSuite((err: BusinessError, data: Array<string>) => {
6. if (err) {
7. console.error("getCipherSuite callback error = " + err);
8. } else {
9. console.info("getCipherSuite callback = " + data);
10. }
11. });
```

### getCipherSuite9+

PhonePC/2in1TabletTVWearable

getCipherSuite(): Promise<Array<string>>

在TLSSocket通信连接成功之后，获取通信双方协商后的加密套件，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | 以Promise形式返回通信双方支持的加密套件。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getCipherSuite().then((data: Array<string>) => {
6. console.info('getCipherSuite success:' + JSON.stringify(data));
7. }).catch((err: BusinessError) => {
8. console.error("failed" + err);
9. });
```

### getSignatureAlgorithms9+

PhonePC/2in1TabletTVWearable

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

在TLSSocket通信连接成功之后，获取通信双方协商后签名算法，该接口只适配双向认证模式下，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
6. if (err) {
7. console.error("getSignatureAlgorithms callback error = " + err);
8. } else {
9. console.info("getSignatureAlgorithms callback = " + data);
10. }
11. });
```

### getSignatureAlgorithms9+

PhonePC/2in1TabletTVWearable

getSignatureAlgorithms(): Promise<Array<string>>

在TLSSocket通信连接成功之后，获取通信双方协商后的签名算法，该接口只适配双向认证模式下，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | 以Promise形式返回获取到的双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getSignatureAlgorithms().then((data: Array<string>) => {
6. console.info("getSignatureAlgorithms success" + data);
7. }).catch((err: BusinessError) => {
8. console.error("failed" + err);
9. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取TLSSocket的本地Socket地址。使用Promise异步回调。

说明

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.getLocalAddress().then((localAddress: socket.NetAddress) => {
6. console.info("Get success: " + JSON.stringify(localAddress));
7. }).catch((err: BusinessError) => {
8. console.error("Get failed, error: " + JSON.stringify(err));
9. })
```

### getSocketFd16+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取TLSSocket的文件描述符。使用Promise异步回调。

说明

* bind方法调用成功后，才可调用此方法。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close9)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回socket的文件描述符。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
4. let bindAddr: socket.NetAddress = {
5. address: '192.168.xx.xxx',
6. port: 8080
7. }
8. tls.bind(bindAddr, (err: BusinessError) => {
9. if (err) {
10. console.error('bind fail');
11. return;
12. }
13. console.info('bind success');
14. });
15. tls.getSocketFd().then((data: number) => {
16. console.info("tls socket fd: " + data);
17. })
```

### send9+

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

在TLSSocket通信连接成功之后，向服务端发送消息，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | 发送的数据内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数,返回TLSSocket发送数据的结果。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.send("xxxx", (err: BusinessError) => {
6. if (err) {
7. console.error("send callback error = " + err);
8. } else {
9. console.info("send success");
10. }
11. });
```

### send9+

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer): Promise<void>

在TLSSocket通信连接成功之后，向服务端发送消息，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | 发送的数据内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回,返回TLSSocket发送数据的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.send("xxxx").then(() => {
6. console.info("send success");
7. }).catch((err: BusinessError) => {
8. console.error("failed" + err);
9. });
```

### close9+

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

在TLSSocket通信连接成功之后，断开连接，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数,成功返回TLSSocket关闭连接的结果。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.close((err: BusinessError) => {
6. if (err) {
7. console.error("close callback error = " + err);
8. } else {
9. console.info("close success");
10. }
11. });
```

### close9+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

在TLSSocket通信连接成功之后，断开连接，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回,返回TLSSocket关闭连接的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tls: socket.TLSSocket = socket.constructTLSSocketInstance();
5. tls.close().then(() => {
6. console.info("close success");
7. }).catch((err: BusinessError) => {
8. console.error("failed" + err);
9. });
```

## TLSConnectOptions9+

PhonePC/2in1TabletTVWearable

TLS连接的操作。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | [NetAddress](js-apis-socket.md#netaddress) | 否 | 否 | 网关地址。 |
| secureOptions | [TLSSecureOptions](js-apis-socket.md#tlssecureoptions9) | 否 | 否 | TLS安全相关操作。 |
| ALPNProtocols | Array<string> | 否 | 是 | ALPN协议，支持["spdy/1", "http/1.1"]，默认为[]。 |
| skipRemoteValidation12+ | boolean | 否 | 是 | 是否跳过对服务端进行证书认证，默认为false。true：跳过对服务端进行证书认证；false：不跳过对服务端进行证书认证。 |
| proxy18+ | [ProxyOptions](js-apis-socket.md#proxyoptions18) | 否 | 是 | 使用的代理信息，默认不使用代理。 |
| timeout22+ | number | 否 | 是 | 连接超时时间，单位：ms，默认为0。传入值需为0-4294967295范围内的整数。TLSSocket连接在超时后会失败。 |

## TLSSecureOptions9+

PhonePC/2in1TabletTVWearable

TLS安全相关操作。当本地证书cert和私钥key不为空时，开启双向验证模式。cert和key其中一项为空时，开启单向验证模式。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ca | string | Array<string> | 否 | 是 | 服务端的ca证书，用于认证校验服务端的数字证书。默认为系统预置CA证书12+。最多支持设置1000本证书。 |
| cert | string | 否 | 是 | 本地客户端的数字证书。 |
| key | string | 否 | 是 | 本地数字证书的私钥。 |
| password | string | 否 | 是 | 读取私钥的密码。 |
| protocols | [Protocol](js-apis-socket.md#protocol9) |Array<[Protocol](js-apis-socket.md#protocol9)> | 否 | 是 | TLS的协议版本，默认为"TLSv1.2"。 |
| useRemoteCipherPrefer | boolean | 否 | 是 | 优先使用对等方的密码套件。true：优先使用对等方的密码套件；false：不优先使用对等方的密码套件。 |
| signatureAlgorithms | string | 否 | 是 | 通信过程中的签名算法，默认为"" 。 |
| cipherSuite | string | 否 | 是 | 通信过程中的加密套件，默认为"" 。 |
| isBidirectionalAuthentication12+ | boolean | 否 | 是 | 用于设置双向认证，默认为false。true：设置双向认证；false：不设置双向认证。 |

## Protocol9+

PhonePC/2in1TabletTVWearable

TLS通信的协议版本。

**系统能力**：SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TLSv12 | "TLSv1.2" | 使用TLSv1.2协议通信。 |
| TLSv13 | "TLSv1.3" | 使用TLSv1.3协议通信。 |

## X509CertRawData9+

PhonePC/2in1TabletTVWearable

type X509CertRawData = cert.EncodingBlob

存储证书的数据。

**系统能力**：SystemCapability.Communication.NetStack

| 类型 | 说明 |
| --- | --- |
| cert.EncodingBlob | 提供证书编码blob类型。 |

## socket.constructTLSSocketServerInstance10+

PhonePC/2in1TabletTVWearable

constructTLSSocketServerInstance(): TLSSocketServer

创建并返回一个TLSSocketServer对象。

**系统能力**：SystemCapability.Communication.NetStack

**返回值:**

| 类型 | 说明 |
| --- | --- |
| [TLSSocketServer](js-apis-socket.md#tlssocketserver10) | 返回一个TLSSocketServer对象。 |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
```

## TLSSocketServer10+

PhonePC/2in1TabletTVWearable

TLSSocketServer连接。在调用TLSSocketServer的方法前，需要先通过[socket.constructTLSSocketServerInstance](js-apis-socket.md#socketconstructtlssocketserverinstance10)创建TLSSocketServer对象。

### listen10+

PhonePC/2in1TabletTVWearable

listen(options: TLSConnectOptions, callback: AsyncCallback<void>): void

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用callback异步回调。

注意

IP地址设置为0.0.0.0时，可以监听本机所有地址。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TLSConnectOptions](js-apis-socket.md#tlsconnectoptions9) | 是 | TLSSocketServer连接所需要的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"],
23. skipRemoteValidation: false
24. }
25. tlsServer.listen(tlsConnectOptions, (err: BusinessError) => {
26. console.error("listen callback error" + err);
27. });
```

### listen10+

PhonePC/2in1TabletTVWearable

listen(options: TLSConnectOptions): Promise<void>

绑定IP地址和端口，在TLSSocketServer上bind成功之后，监听客户端的连接，并创建和初始化TLS会话，实现建立连接过程，加载证书秘钥并验证，使用Promise异步回调。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TLSConnectOptions](js-apis-socket.md#tlsconnectoptions9) | 是 | 连接所需要的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回，成功返回空，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 2300002 | System internal error. |
| 2303109 | Bad file number. |
| 2303111 | Resource temporarily unavailable. Try again. |
| 2303198 | Address already in use. |
| 2303199 | Cannot assign requested address. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"],
23. skipRemoteValidation: false
24. }
25. tlsServer.listen(tlsConnectOptions).then(() => {
26. console.info("listen callback success");
27. }).catch((err: BusinessError) => {
28. console.error("failed: " + JSON.stringify(err));
29. });
```

### getState10+

PhonePC/2in1TabletTVWearable

getState(callback: AsyncCallback<SocketStateBase>): void

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 是 | 回调函数。成功返回TLSSocketServer状态，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });
29. tlsServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
30. if (err) {
31. console.error('getState fail');
32. return;
33. }
34. console.info('getState success:' + JSON.stringify(data));
35. });
```

### getState10+

PhonePC/2in1TabletTVWearable

getState(): Promise<SocketStateBase>

在TLSSocketServer的listen成功之后，获取TLSSocketServer状态。使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SocketStateBase](js-apis-socket.md#socketstatebase)> | 以Promise形式返回获取TLSSocketServer状态的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });
29. tlsServer.getState().then(() => {
30. console.info('getState success');
31. }).catch((err: BusinessError) => {
32. console.error('getState fail');
33. });
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取TLSSocketServer监听端口绑定的文件描述符。使用Promise异步回调。

说明

* [listen](js-apis-socket.md#listen10-3)方法调用成功后，才可调用此方法。多次调用listen时，会获取最新监听端口绑定的文件描述符。
* 监听异常、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close20-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen success");
26. tlsServer.getSocketFd().then((fd: number) => {
27. console.info(`Socket FD：${fd}`);
28. }).catch((err: BusinessError) => {
29. console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
30. });
31. }).catch((err: BusinessError) => {
32. console.error(`listen failed: ${JSON.stringify(err)}`);
33. });
```

### setExtraOptions10+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions, callback: AsyncCallback<void>): void

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TLSSocketServer连接的其他属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });

30. interface SocketLinger {
31. on: boolean;
32. linger: number;
33. }

35. let tcpExtraOptions: socket.TCPExtraOptions = {
36. keepAlive: true,
37. OOBInline: true,
38. TCPNoDelay: true,
39. socketLinger: { on: true, linger: 10 } as SocketLinger,
40. receiveBufferSize: 8192,
41. sendBufferSize: 8192,
42. reuseAddress: true,
43. socketTimeout: 3000
44. }
45. tlsServer.setExtraOptions(tcpExtraOptions, (err: BusinessError) => {
46. if (err) {
47. console.error('setExtraOptions fail');
48. return;
49. }
50. console.info('setExtraOptions success');
51. });
```

### setExtraOptions10+

PhonePC/2in1TabletTVWearable

setExtraOptions(options: TCPExtraOptions): Promise<void>

在TLSSocketServer的listen成功之后，设置TLSSocketServer连接的其他属性，使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TCPExtraOptions](js-apis-socket.md#tcpextraoptions) | 是 | TLSSocketServer连接的其他属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回，成功返回空，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });

30. interface SocketLinger {
31. on: boolean;
32. linger: number;
33. }

35. let tcpExtraOptions: socket.TCPExtraOptions = {
36. keepAlive: true,
37. OOBInline: true,
38. TCPNoDelay: true,
39. socketLinger: { on: true, linger: 10 } as SocketLinger,
40. receiveBufferSize: 8192,
41. sendBufferSize: 8192,
42. reuseAddress: true,
43. socketTimeout: 3000
44. }
45. tlsServer.setExtraOptions(tcpExtraOptions).then(() => {
46. console.info('setExtraOptions success');
47. }).catch((err: BusinessError) => {
48. console.error('setExtraOptions fail');
49. });
```

### getCertificate10+

PhonePC/2in1TabletTVWearable

getCertificate(callback: AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>): void

在TLSSocketServer通信连接成功之后，获取本地的数字证书，使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 是 | 回调函数，成功返回本地的证书，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
6. let netAddress: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. let tlsSecureOptions: socket.TLSSecureOptions = {
11. key: "xxxx",
12. cert: "xxxx",
13. ca: ["xxxx"],
14. password: "xxxx",
15. protocols: socket.Protocol.TLSv12,
16. useRemoteCipherPrefer: true,
17. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
18. cipherSuite: "AES256-SHA256"
19. }
20. let tlsConnectOptions: socket.TLSConnectOptions = {
21. address: netAddress,
22. secureOptions: tlsSecureOptions,
23. ALPNProtocols: ["spdy/1", "http/1.1"]
24. }
25. tlsServer.listen(tlsConnectOptions).then(() => {
26. console.info("listen callback success");
27. }).catch((err: BusinessError) => {
28. console.error("failed: " + JSON.stringify(err));
29. });
30. tlsServer.getCertificate((err: BusinessError, data: socket.X509CertRawData) => {
31. if (err) {
32. console.error("getCertificate callback error = " + err);
33. } else {
34. const decoder = util.TextDecoder.create();
35. const str = decoder.decodeToString(data.data);
36. console.info("getCertificate callback: " + str);
37. }
38. });
```

### getCertificate10+

PhonePC/2in1TabletTVWearable

getCertificate():Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>

在TLSSocketServer通信连接之后，获取本地的数字证书，使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 以Promise形式返回本地的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303504 | An error occurred when verifying the X.509 certificate. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
6. let netAddress: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. let tlsSecureOptions: socket.TLSSecureOptions = {
11. key: "xxxx",
12. cert: "xxxx",
13. ca: ["xxxx"],
14. password: "xxxx",
15. protocols: socket.Protocol.TLSv12,
16. useRemoteCipherPrefer: true,
17. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
18. cipherSuite: "AES256-SHA256"
19. }
20. let tlsConnectOptions: socket.TLSConnectOptions = {
21. address: netAddress,
22. secureOptions: tlsSecureOptions,
23. ALPNProtocols: ["spdy/1", "http/1.1"]
24. }
25. tlsServer.listen(tlsConnectOptions).then(() => {
26. console.info("listen callback success");
27. }).catch((err: BusinessError) => {
28. console.error("failed: " + JSON.stringify(err));
29. });
30. tlsServer.getCertificate().then((data: socket.X509CertRawData) => {
31. const decoder = util.TextDecoder.create();
32. const str = decoder.decodeToString(data.data);
33. console.info("getCertificate: " + str);
34. }).catch((err: BusinessError) => {
35. console.error("failed" + err);
36. });
```

### getProtocol10+

PhonePC/2in1TabletTVWearable

getProtocol(callback: AsyncCallback<string>): void

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回通信的协议。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });
29. tlsServer.getProtocol((err: BusinessError, data: string) => {
30. if (err) {
31. console.error("getProtocol callback error = " + err);
32. } else {
33. console.info("getProtocol callback = " + data);
34. }
35. });
```

### getProtocol10+

PhonePC/2in1TabletTVWearable

getProtocol():Promise<string>

在TLSSocketServer通信连接成功之后，获取通信的协议版本，使用Promise异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回通信的协议。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });
29. tlsServer.getProtocol().then((data: string) => {
30. console.info(data);
31. }).catch((err: BusinessError) => {
32. console.error("failed" + err);
33. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取TLSSocketServer的本地Socket地址。使用Promise异步回调。

说明

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. tlsServer.getLocalAddress().then((localAddress: socket.NetAddress) => {
6. console.info("Get success: " + JSON.stringify(localAddress));
7. }).catch((err: BusinessError) => {
8. console.error("Get failed, error: " + JSON.stringify(err));
9. })
```

### on('connect')10+

PhonePC/2in1TabletTVWearable

on(type: 'connect', callback: Callback<TLSSocketConnection>): void

订阅TLSSocketServer的连接事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TLSSocketConnection](js-apis-socket.md#tlssocketconnection10)> | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. tlsServer.on('connect', (data: socket.TLSSocketConnection) => {
27. console.info(JSON.stringify(data));
28. });
29. }).catch((err: BusinessError) => {
30. console.error("failed: " + JSON.stringify(err));
31. });
```

### off('connect')10+

PhonePC/2in1TabletTVWearable

off(type: 'connect', callback?: Callback<TLSSocketConnection>): void

取消订阅TLSSocketServer的连接事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'connect'：连接事件。 |
| callback | Callback<[TLSSocketConnection](js-apis-socket.md#tlssocketconnection10)> | 否 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });

30. let callback = (data: socket.TLSSocketConnection) => {
31. console.info('on connect message: ' + JSON.stringify(data));
32. }
33. tlsServer.on('connect', callback);
34. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
35. tlsServer.off('connect', callback);
36. tlsServer.off('connect');
```

### on('error')10+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocketServer连接的error事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });
29. tlsServer.on('error', (err: BusinessError) => {
30. console.error("on error, err:" + JSON.stringify(err))
31. });
```

### off('error')10+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocketServer连接的error事件。使用callback异步回调。

说明

listen方法调用成功后，才可调用此方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed: " + JSON.stringify(err));
28. });

30. let callback = (err: BusinessError) => {
31. console.error("on error, err:" + JSON.stringify(err));
32. }
33. tlsServer.on('error', callback);
34. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
35. tlsServer.off('error', callback);
36. tlsServer.off('error');
```

### close20+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

TLSSocketServer停止监听并释放通过[listen](js-apis-socket.md#listen10-2)方法绑定的端口。使用Promise异步回调。

说明

该方法不会关闭已有连接。如需关闭，请调用[TLSSocketConnection](js-apis-socket.md#tlssocketconnection10)的[close](js-apis-socket.md#close10-2)方法。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Socket错误码](errorcode-net-socket.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.on('connect', (connection: socket.TLSSocketConnection) => {
25. console.info("connection clientId: " + connection.clientId);
26. // 逻辑处理
27. tlsServer.close(); // 停止监听
28. connection.close(); // 关闭当前连接
29. });
30. tlsServer.listen(tlsConnectOptions).then(() => {
31. console.info("listen callback success");
32. }).catch((err: BusinessError) => {
33. console.error("listen failed: " + err.code);
34. });
```

## TLSSocketConnection10+

PhonePC/2in1TabletTVWearable

TLSSocketConnection连接，即TLSSocket客户端与服务端的连接。在调用TLSSocketConnection的方法前，需要先获取TLSSocketConnection对象。

说明

客户端与服务端成功建立连接后，才能通过返回的TLSSocketConnection对象调用相应的接口。

**系统能力**：SystemCapability.Communication.NetStack

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| clientId | number | 否 | 否 | 客户端与TLSSocketServer建立连接的id。 |

### send10+

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer, callback: AsyncCallback<void>): void

在TLSSocketServer通信连接成功之后，向客户端发送消息，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | TLSSocketServer发送数据所需要的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.send('Hello, client!', (err: BusinessError) => {
32. if (err) {
33. console.error('send fail');
34. return;
35. }
36. console.info('send success');
37. });
38. });
```

### send10+

PhonePC/2in1TabletTVWearable

send(data: string | ArrayBuffer): Promise<void>

在TLSSocketServer通信连接成功之后，向服务端发送消息，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | ArrayBuffer | 是 | TLSSocketServer发送数据所需要的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回，成功返回空，失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303503 | An error occurred when writing data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.send('Hello, client!').then(() => {
32. console.info('send success');
33. }).catch((err: BusinessError) => {
34. console.error('send fail');
35. });
36. });
```

### close10+

PhonePC/2in1TabletTVWearable

close(callback: AsyncCallback<void>): void

在与TLSSocketServer通信连接成功之后，断开连接，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，成功返回空，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.close((err: BusinessError) => {
32. if (err) {
33. console.error('close fail');
34. return;
35. }
36. console.info('close success');
37. });
38. });
```

### close10+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

在与TLSSocketServer通信连接成功之后，断开连接，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 以Promise形式返回，成功返回空。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303505 | An error occurred in the TLS system call. |
| 2303506 | Failed to close the TLS connection. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.close().then(() => {
31. console.info('close success');
32. }).catch((err: BusinessError) => {
33. console.error('close fail');
34. });
35. });
```

### getRemoteAddress10+

PhonePC/2in1TabletTVWearable

getRemoteAddress(callback: AsyncCallback<NetAddress>): void

在TLSSocketServer通信连接成功之后，获取对端Socket地址。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetAddress](js-apis-socket.md#netaddress)> | 是 | 回调函数。成功返回对端的socket地址，失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.getRemoteAddress((err: BusinessError, data: socket.NetAddress) => {
31. if (err) {
32. console.error('getRemoteAddress fail');
33. return;
34. }
35. console.info('getRemoteAddress success:' + JSON.stringify(data));
36. });
37. });
```

### getRemoteAddress10+

PhonePC/2in1TabletTVWearable

getRemoteAddress(): Promise<NetAddress>

在TLSSocketServer通信连接成功之后，获取对端Socket地址。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取对端socket地址的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303188 | Socket operation on non-socket. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.getRemoteAddress().then((data: socket.NetAddress) => {
31. console.info('getRemoteAddress success:' + JSON.stringify(data));
32. }).catch((err: BusinessError) => {
33. console.error("failed" + err);
34. });
35. });
```

### getRemoteCertificate10+

PhonePC/2in1TabletTVWearable

getRemoteCertificate(callback: AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>): void

在TLSSocketServer通信连接成功之后，获取对端的数字证书，该接口只适用于客户端向服务端发送证书时，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 是 | 回调函数，返回对端的证书。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
6. let netAddress: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. let tlsSecureOptions: socket.TLSSecureOptions = {
11. key: "xxxx",
12. cert: "xxxx",
13. ca: ["xxxx"],
14. password: "xxxx",
15. protocols: socket.Protocol.TLSv12,
16. useRemoteCipherPrefer: true,
17. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
18. cipherSuite: "AES256-SHA256"
19. }
20. let tlsConnectOptions: socket.TLSConnectOptions = {
21. address: netAddress,
22. secureOptions: tlsSecureOptions,
23. ALPNProtocols: ["spdy/1", "http/1.1"]
24. }
25. tlsServer.listen(tlsConnectOptions).then(() => {
26. console.info("listen callback success");
27. }).catch((err: BusinessError) => {
28. console.error("failed" + err);
29. });
30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.getRemoteCertificate((err: BusinessError, data: socket.X509CertRawData) => {
32. if (err) {
33. console.error("getRemoteCertificate callback error: " + err);
34. } else {
35. const decoder = util.TextDecoder.create();
36. const str = decoder.decodeToString(data.data);
37. console.info("getRemoteCertificate callback: " + str);
38. }
39. });
40. });
```

### getRemoteCertificate10+

PhonePC/2in1TabletTVWearable

getRemoteCertificate():Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)>

在TLSSocketServer通信连接成功之后，获取对端的数字证书，该接口只适用于客户端向服务端发送证书时，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[X509CertRawData](js-apis-socket.md#x509certrawdata9)> | 以Promise形式返回对端的数字证书的结果。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
6. let netAddress: socket.NetAddress = {
7. address: '192.168.xx.xxx',
8. port: 8080
9. }
10. let tlsSecureOptions: socket.TLSSecureOptions = {
11. key: "xxxx",
12. cert: "xxxx",
13. ca: ["xxxx"],
14. password: "xxxx",
15. protocols: socket.Protocol.TLSv12,
16. useRemoteCipherPrefer: true,
17. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
18. cipherSuite: "AES256-SHA256"
19. }
20. let tlsConnectOptions: socket.TLSConnectOptions = {
21. address: netAddress,
22. secureOptions: tlsSecureOptions,
23. ALPNProtocols: ["spdy/1", "http/1.1"]
24. }
25. tlsServer.listen(tlsConnectOptions).then(() => {
26. console.info("listen callback success");
27. }).catch((err: BusinessError) => {
28. console.error("failed" + err);
29. });
30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.getRemoteCertificate().then((data: socket.X509CertRawData) => {
32. const decoder = util.TextDecoder.create();
33. const str = decoder.decodeToString(data.data);
34. console.info("getRemoteCertificate success: " + str);
35. }).catch((err: BusinessError) => {
36. console.error("failed" + err);
37. });
38. });
```

### getCipherSuite10+

PhonePC/2in1TabletTVWearable

getCipherSuite(callback: AsyncCallback<Array<string>>): void

在TLSSocketServer通信连接成功之后，获取通信双方协商后的加密套件，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回通信双方支持的加密套件。失败返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.getCipherSuite((err: BusinessError, data: Array<string>) => {
31. if (err) {
32. console.error("getCipherSuite callback error = " + err);
33. } else {
34. console.info("getCipherSuite callback = " + data);
35. }
36. });
37. });
```

### getCipherSuite10+

PhonePC/2in1TabletTVWearable

getCipherSuite(): Promise<Array<string>>

在TLSSocketServer通信连接成功之后，获取通信双方协商后的加密套件，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | 以Promise形式返回通信双方支持的加密套件。失败返回错误码，错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2303502 | An error occurred when reading data on the TLS socket. |
| 2303505 | An error occurred in the TLS system call. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.getCipherSuite().then((data: Array<string>) => {
31. console.info('getCipherSuite success:' + JSON.stringify(data));
32. }).catch((err: BusinessError) => {
33. console.error("failed" + err);
34. });
35. });
```

### getSignatureAlgorithms10+

PhonePC/2in1TabletTVWearable

getSignatureAlgorithms(callback: AsyncCallback<Array<string>>): void

在TLSSocketServer通信连接成功之后，获取通信双方协商后签名算法，使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.getSignatureAlgorithms((err: BusinessError, data: Array<string>) => {
31. if (err) {
32. console.error("getSignatureAlgorithms callback error = " + err);
33. } else {
34. console.info("getSignatureAlgorithms callback = " + data);
35. }
36. });
37. });
```

### getSignatureAlgorithms10+

PhonePC/2in1TabletTVWearable

getSignatureAlgorithms(): Promise<Array<string>>

在TLSSocketServer通信连接成功之后，获取通信双方协商后的签名算法，使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | 以Promise形式返回获取到的双方支持的签名算法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2303501 | SSL is null. |
| 2300002 | System internal error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.getSignatureAlgorithms().then((data: Array<string>) => {
31. console.info("getSignatureAlgorithms success" + data);
32. }).catch((err: BusinessError) => {
33. console.error("failed" + err);
34. });
35. });
```

### getLocalAddress12+

PhonePC/2in1TabletTVWearable

getLocalAddress(): Promise<NetAddress>

获取TLSSocketConnection连接的本地Socket地址。使用Promise异步回调。

说明

在TLSSocketServer通信连接成功之后，才可调用此方法。

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetAddress](js-apis-socket.md#netaddress)> | 以Promise形式返回获取本地socket地址的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2300002 | System internal error. |
| 2301009 | Bad file descriptor. |
| 2303188 | Socket operation on non-socket. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.getLocalAddress().then((localAddress: socket.NetAddress) => {
32. console.info("Family IP Port: " + JSON.stringify(localAddress));
33. }).catch((err: BusinessError) => {
34. console.error("TLS Client Get Family IP Port failed, error: " + JSON.stringify(err));
35. })
36. });
```

### getSocketFd23+

PhonePC/2in1TabletTVWearable

getSocketFd(): Promise<number>

获取TLSSocketConnection连接的文件描述符。使用Promise异步回调。

说明

* 在TLSSocketServer通信连接成功之后，才可调用此方法。
* 连接断开、Socket已关闭（如调用close后）等异常情况下调用本接口会返回-1。
* 文件描述符的生命周期由系统管理，应用可以通过[close](js-apis-socket.md#close10-2)方法关闭Socket连接，避免直接操作文件描述符进行关闭。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回Socket的文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen success");
26. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
27. client.getSocketFd().then((fd: number) => {
28. console.info(`Socket FD：${fd}`);
29. }).catch((err: BusinessError) => {
30. console.error(`getSocketFd fail: ${err.message}, errorCode: ${err.code}`);
31. })
32. });
33. }).catch((err: BusinessError) => {
34. console.error(`listen failed: ${JSON.stringify(err)}`);
35. });
```

### on('message')10+

PhonePC/2in1TabletTVWearable

on(type: 'message', callback: Callback<SocketMessageInfo>): void

订阅TLSSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 是 | 回调函数。成功时返回TLSSocketConnection连接信息，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.on('message', (value: socket.SocketMessageInfo) => {
32. let messageView = '';
33. let uint8Array = new Uint8Array(value.message);
34. for (let i: number = 0; i < value.message.byteLength; i++) {
35. let messages = uint8Array[i];
36. let message = String.fromCharCode(messages);
37. messageView += message;
38. }
39. console.info('on message message: ' + JSON.stringify(messageView));
40. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
41. });
42. });
```

### off('message')10+

PhonePC/2in1TabletTVWearable

off(type: 'message', callback?: Callback<SocketMessageInfo>): void

取消订阅TLSSocketConnection连接的接收消息事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'message'：接收消息事件。 |
| callback | Callback<[SocketMessageInfo](js-apis-socket.md#socketmessageinfo11)> | 否 | 回调函数。成功时返回TLSSocketConnection连接信息，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. let callback = (value: socket.SocketMessageInfo) => {
31. let messageView = '';
32. for (let i: number = 0; i < value.message.byteLength; i++) {
33. let uint8Array = new Uint8Array(value.message)
34. let messages = uint8Array[i]
35. let message = String.fromCharCode(messages);
36. messageView += message;
37. }
38. console.info('on message message: ' + JSON.stringify(messageView));
39. console.info('remoteInfo: ' + JSON.stringify(value.remoteInfo));
40. }
41. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
42. client.on('message', callback);
43. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
44. client.off('message', callback);
45. client.off('message');
46. });
```

### on('close')10+

PhonePC/2in1TabletTVWearable

on(type: 'close', callback: Callback<void>): void

订阅TLSSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 是 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });
29. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
30. client.on('close', () => {
31. console.info("on close success")
32. });
33. });
```

### off('close')10+

PhonePC/2in1TabletTVWearable

off(type: 'close', callback?: Callback<void>): void

取消订阅TLSSocketConnection的关闭事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'close'：关闭事件。 |
| callback | Callback<void> | 否 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. let callback = () => {
31. console.info("on close success");
32. }
33. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
34. client.on('close', callback);
35. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
36. client.off('close', callback);
37. client.off('close');
38. });
```

### on('error')10+

PhonePC/2in1TabletTVWearable

on(type: 'error', callback: ErrorCallback): void

订阅TLSSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 是 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
31. client.on('error', (err: BusinessError) => {
32. console.error("on error, err:" + JSON.stringify(err))
33. });
34. });
```

### off('error')10+

PhonePC/2in1TabletTVWearable

off(type: 'error', callback?: ErrorCallback): void

取消订阅TLSSocketConnection连接的error事件。使用callback异步回调。

**系统能力**：SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型。'error'：error事件。 |
| callback | ErrorCallback | 否 | 回调函数。成功时返回空，失败时返回错误码、错误信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

```
1. import { socket } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
5. let netAddress: socket.NetAddress = {
6. address: '192.168.xx.xxx',
7. port: 8080
8. }
9. let tlsSecureOptions: socket.TLSSecureOptions = {
10. key: "xxxx",
11. cert: "xxxx",
12. ca: ["xxxx"],
13. password: "xxxx",
14. protocols: socket.Protocol.TLSv12,
15. useRemoteCipherPrefer: true,
16. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
17. cipherSuite: "AES256-SHA256"
18. }
19. let tlsConnectOptions: socket.TLSConnectOptions = {
20. address: netAddress,
21. secureOptions: tlsSecureOptions,
22. ALPNProtocols: ["spdy/1", "http/1.1"]
23. }
24. tlsServer.listen(tlsConnectOptions).then(() => {
25. console.info("listen callback success");
26. }).catch((err: BusinessError) => {
27. console.error("failed" + err);
28. });

30. let callback = (err: BusinessError) => {
31. console.error("on error, err:" + JSON.stringify(err));
32. }
33. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
34. client.on('error', callback);
35. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
36. client.off('error', callback);
37. client.off('error');
38. });
```
