---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/socket-connection
title: 使用Socket访问网络
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 访问网络 > 使用Socket访问网络
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ad9c7b111f2db9f5b0bf4b28651444d1b821b077ce9f585d43294407e9b72f5a
---

## 简介

Socket连接主要是通过Socket进行数据传输，支持TCP/UDP/Multicast/TLS协议。

说明

应用退后台后，Socket可能会断开，当应用重新回到前台，发生通信失败时，需匹配错误码并重新创建新的TCP/UDP Socket。

## 基本概念

* Socket：套接字，就是对网络中不同主机上的应用进程之间进行双向通信的端点的抽象。
* TCP：传输控制协议(Transmission Control Protocol)，是一种面向连接的、可靠的、基于字节流的传输层通信协议。
* UDP：用户数据报协议(User Datagram Protocol)，是一个简单的面向消息的传输层，不需要连接。
* Multicast：多播，基于UDP的一种通信模式，用于实现组内所有设备之间广播形式的通信。
* LocalSocket：本地套接字，IPC(Inter-Process Communication)进程间通信的一种，实现设备内进程之间相互通信，无需网络。
* TLS：安全传输层协议(Transport Layer Security)，用于在两个通信应用程序之间提供保密性和数据完整性。

## 场景介绍

应用通过Socket进行数据传输，支持TCP/UDP/Multicast/TLS协议。主要场景有：

* 在TCP/UDP传输的客户端（UDP本身并没有客户端和服务器端的明确区分，此处描述UDP传输的客户端是指主动向服务器发送数据的一方），应用通过TCP/UDP Socket进行数据传输
* 在TCP传输的服务器端，应用通过TCP Socket Server进行数据传输
* 多播通信场景，应用通过Multicast Socket进行数据传输
* 同一台主机上不同进程之间传输的客户端，应用通过Local Socket进行数据传输
* 同一台主机上不同进程之间传输的服务器端，应用通过Local Socket Server进行数据传输
* 数据加密传输时，客户端侧通过TLS Socket进行加密数据传输
* 数据加密传输时，服务器侧通过TLS Socket Server进行加密数据传输

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

## 应用TCP/UDP协议进行通信

UDP与TCP流程大体类似，下面以TCP为例：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [TcpClientWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpClientWorker.ets#L18-L22)
2. 创建一个TCPSocket连接，返回一个TCPSocket对象。

   ```
   1. // 创建一个TCPSocket连接，返回一个TCPSocket对象。
   2. let tcpClient: socket.TCPSocket = socket.constructTCPSocketInstance();
   ```

   [TcpClientWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpClientWorker.ets#L26-L29)
3. （可选）订阅TCPSocket相关的订阅事件。

   ```
   1. class SocketInfo {
   2. public message: ArrayBuffer = new ArrayBuffer(1);
   3. public remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
   4. }

   6. tcpClient.on('message', (value: SocketInfo) => {
   7. hilog.info(0x0000, 'testTag', 'on message');
   8. let buffer = value.message;
   9. let dataView = new DataView(buffer);
   10. let str = '';
   11. for (let i = 0; i < dataView.byteLength; ++i) {
   12. str += String.fromCharCode(dataView.getUint8(i));
   13. }
   14. hilog.info(0x0000, 'testTag', 'on connect received:' + str);
   15. });

   17. tcpClient.on('connect', () => {
   18. hilog.info(0x0000, 'testTag', 'on connect');
   19. });

   21. tcpClient.on('close', () => {
   22. hilog.info(0x0000, 'testTag', 'on close');
   23. });
   ```

   [TcpClientWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpClientWorker.ets#L57-L81)
4. 绑定IP地址和端口，端口可以指定或由系统随机分配，绑定成功后可以连接到指定的IP地址和端口，连接成功后可以发送数据。

   ```
   1. // 绑定本地IP地址和端口。
   2. let ipAddress : socket.NetAddress = {} as socket.NetAddress;
   3. ipAddress.address = "192.168.xxx.xxx";
   4. ipAddress.port = 1234;

   6. // bind成功后，连接到指定的IP地址和端口。
   7. let netAddress: socket.NetAddress = {} as socket.NetAddress;
   8. netAddress.address = "192.168.xxx.xxx";
   9. netAddress.port = 5678;
   ```

   ```
   1. // 绑定本地IP地址和端口。
   2. // ···
   3. tcpClient.bind(ipAddress, (err: BusinessError) => {
   4. if (err) {
   5. hilog.error(0x0000, 'testTag', 'bind fail');
   6. return;
   7. }
   8. hilog.info(0x0000, 'testTag', 'bind success');

   10. // bind成功后，连接到指定的IP地址和端口。
   11. // ···
   12. let tcpConnect: socket.TCPConnectOptions = {
   13. address: netAddress,
   14. timeout: 6000 // 超时时间设置
   15. };
   16. tcpClient.connect(tcpConnect).then(() => {
   17. hilog.info(0x0000, 'testTag', 'connect success');
   18. let tcpSendOptions: socket.TCPSendOptions = {
   19. data: tcpMessage.message!
   20. };
   21. tcpClient.send(tcpSendOptions).then(() => {
   22. hilog.info(0x0000, 'testTag', 'send success');
   23. // ···
   24. }).catch(() => {
   25. hilog.info(0x0000, 'testTag', 'send fail');
   26. // ···
   27. });
   28. }).catch((err: BusinessError) => {
   29. hilog.error(0x0000, 'testTag', 'connect fail');
   30. });
   31. })
   ```

   [TcpClientWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpClientWorker.ets#L84-L129)
5. Socket连接使用完毕后，主动关闭。

   ```
   1. // 连接使用完毕后，主动关闭。取消相关事件的订阅。
   2. setTimeout(() => {
   3. tcpClient.close().then(() => {
   4. // ···
   5. hilog.info(0x0000, 'testTag', 'close success');
   6. }).catch((err: BusinessError) => {
   7. // ···
   8. hilog.error(0x0000, 'testTag', 'close fail');
   9. });
   10. tcpClient.off('message');
   11. tcpClient.off('connect');
   12. tcpClient.off('close');
   13. }, 30 * 1000);
   ```

   [TcpClientWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpClientWorker.ets#L133-L151)

## 应用通过TCP Socket Server进行数据传输

服务端TCP Socket流程：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [TcpServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpServerWorker.ets#L18-L22)
2. 创建一个TCPSocketServer连接，返回一个TCPSocketServer对象。

   ```
   1. // 创建一个TCPSocketServer连接，返回一个TCPSocketServer对象。
   2. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
   ```

   [TcpServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpServerWorker.ets#L24-L27)
3. 绑定本地IP地址和端口，监听并接受与此套接字建立的客户端TCPSocket连接。

   ```
   1. // 绑定本地IP地址和端口，进行监听。
   2. let ipAddress : socket.NetAddress = {} as socket.NetAddress;
   3. ipAddress.address = "192.168.xxx.xxx";
   4. ipAddress.port = 4651;
   ```

   ```
   1. // 绑定本地IP地址和端口，进行监听。
   2. tcpServer.listen(ipAddress).then(() => {
   3. hilog.info(0x0000, 'testTag', 'listen success');
   4. // ···
   5. }).catch(() => {
   6. hilog.info(0x0000, 'testTag', 'listen fail');
   7. // ···
   8. });
   ```

   [TcpServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpServerWorker.ets#L54-L67)
4. 订阅TCPSocketServer的connect事件，用于监听客户端的连接状态。客户端与服务端建立连接后，会返回一个TCPSocketConnection对象，用于与客户端通信，通过该对象可以订阅与客户端的连接关闭、客户端数据接收事件，也可以进行向客户端发送数据、关闭与客户端的连接、取消订阅TCPSocketConnection相关事件的动作。

   ```
   1. class SocketInfo {
   2. public message: ArrayBuffer = new ArrayBuffer(1);
   3. public remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
   4. }
   5. // 订阅TCPSocketServer的connect事件
   6. // 客户端与服务端建立连接后，返回一个TCPSocketConnection对象，用于与客户端通信。
   7. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
   8. // ···

   10. // client即为建立连接后获取到的连接对象，可以通过该对象订阅TCPSocketConnection相关的事件。
   11. client.on('close', () => {
   12. hilog.info(0x0000, 'testTag', 'client on close success');
   13. // ···
   14. });

   16. client.on('message', (value: SocketInfo) => {
   17. let buffer = value.message;
   18. let dataView = new DataView(buffer);
   19. let str = '';
   20. for (let i = 0; i < dataView.byteLength; ++i) {
   21. str += String.fromCharCode(dataView.getUint8(i));
   22. }
   23. hilog.info(0x0000, 'testTag', 'received message--:' + str);
   24. hilog.info(0x0000, 'testTag', 'received address--:' + value.remoteInfo.address);
   25. hilog.info(0x0000, 'testTag', 'received family--:' + value.remoteInfo.family);
   26. hilog.info(0x0000, 'testTag', 'received port--:' + value.remoteInfo.port);
   27. hilog.info(0x0000, 'testTag', 'received size--:' + value.remoteInfo.size);
   28. // ···
   29. });
   30. });
   31. // ···
   32. let tcpSendOptions: socket.TCPSendOptions = {} as socket.TCPSendOptions;
   33. // 用户可根据需要自行定义发送数据
   34. tcpSendOptions.data = tcpMessage.message!;

   36. client.send(tcpSendOptions).then(() => {
   37. hilog.info(0x0000, 'testTag', 'send success');
   38. // ···
   39. }).catch((err: Object) => {
   40. hilog.error(0x0000, 'testTag', 'send fail: ' + JSON.stringify(err));
   41. // ···
   42. });
   43. // ···
   44. client.close().then(() => {
   45. hilog.info(0x0000, 'testTag', 'close success');
   46. // ···
   47. }).catch((err: BusinessError) => {
   48. hilog.info(0x0000, 'testTag', 'close fail');
   49. // ···
   50. });

   52. // 取消事件订阅，设置关闭连接超时（例如 10 秒后取消关闭连接）
   53. setTimeout(() => {
   54. client?.off('message');
   55. client?.off('close');
   56. }, 10 * 1000);
   ```

   [TcpServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpServerWorker.ets#L69-L163)
5. 取消TCPSocketServer相关事件的订阅。

   ```
   1. // 设置连接超时（例如 30 秒后取消连接）
   2. setTimeout(() => {
   3. tcpServer.off('connect');
   4. }, 30 * 1000);
   ```

   [TcpServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TcpServerWorker.ets#L110-L115)

## 应用通过Multicast Socket进行数据传输

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L17-L20)
2. 创建multicastSocket多播对象。

   ```
   1. // 创建Multicast对象。
   2. let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L44-L47)
3. 指定多播IP与端口，加入多播组。

   ```
   1. // 构造一个对象用于加入多播组
   2. let addr : socket.NetAddress = {
   3. address: '239.255.0.1',
   4. port: 32123,
   5. family: 1
   6. }
   ```

   ```
   1. // 加入多播组。
   2. multicast.addMembership(addr).then(() => {
   3. // ...
   4. hilog.info(0x0000, 'testTag', 'addMembership success');
   5. }).catch((err: BusinessError) => {
   6. // ...
   7. hilog.error(0x0000, 'testTag', 'addMembership fail');
   8. });
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L55-L70)
4. 开启消息message监听。

   ```
   1. // 开启监听消息数据，将接收到的ArrayBuffer类型数据转换为String。
   2. class SocketInfo {
   3. public message: ArrayBuffer = new ArrayBuffer(1);
   4. public remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
   5. }
   6. multicast.on('message', (data: SocketInfo) => {
   7. hilog.info(0x0000, 'testTag', '接收的数据: ' + JSON.stringify(data))
   8. const uintArray = new Uint8Array(data.message)
   9. let str = ''
   10. for (let i = 0; i < uintArray.length; ++i) {
   11. str += String.fromCharCode(uintArray[i])
   12. }
   13. hilog.info(0x0000, 'testTag', str)
   14. // ...
   15. });
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L72-L90)
5. 发送数据，数据以广播的形式传输，同一多播组中已经开启消息message监听的多播对象都会接收到数据。

   ```
   1. // 发送一条多播消息
   2. multicast.send({ data: 'Hello multicast group!', address: addr }).then(() => {
   3. hilog.info(0x0000, 'testTag', 'Multicast: Message sent successfully');
   4. }).catch((err: BusinessError) => {
   5. hilog.error(0x0000, 'testTag', `Multicast: Failed to send message - ${JSON.stringify(err)}`);
   6. });
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L92-L99)
6. 关闭message消息的监听。

   ```
   1. // 关闭消息的监听。
   2. multicast.off('message');
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L103-L106)
7. 退出多播组。

   ```
   1. // 退出多播组。
   2. multicast.dropMembership(addr).then(() => {
   3. // ...
   4. hilog.info(0x0000, 'testTag', 'Multicast: Dropped membership successfully');
   5. }).catch((err: BusinessError) => {
   6. hilog.error(0x0000, 'testTag', `Multicast: Failed to drop membership - ${JSON.stringify(err)}`);
   7. });
   ```

   [MulticastWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/MulticastWorker.ets#L108-L118)

## 应用通过LocalSocket进行数据传输

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L17-L21)
2. 使用constructLocalSocketInstance接口，创建一个LocalSocket客户端对象。

   ```
   1. // 创建一个LocalSocket连接，返回一个LocalSocket对象。
   2. let client: socket.LocalSocket = socket.constructLocalSocketInstance();
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L57-L60)
3. 注册LocalSocket的消息(message)事件，以及一些其它事件(可选)。

   ```
   1. client.on('message', (value: socket.LocalSocketMessageInfo) => {
   2. const uintArray = new Uint8Array(value.message);
   3. let messageView = '';
   4. for (let i = 0; i < uintArray.length; i++) {
   5. messageView += String.fromCharCode(uintArray[i]);
   6. }
   7. hilog.info(0x0000, 'testTag', 'total receive: ' + JSON.stringify(value));
   8. hilog.info(0x0000, 'testTag', 'message information: ' + messageView);
   9. });

   11. client.on('connect', () => {
   12. // ...
   13. hilog.info(0x0000, 'testTag', 'Client connected');
   14. });

   16. client.on('close', () => {
   17. // ...
   18. hilog.info(0x0000, 'testTag', 'Client closed');
   19. });
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L64-L88)
4. 连接到指定的本地套接字文件路径，连接成功之后可以发送数据。

   ```
   1. // 传入指定的本地套接字路径，连接服务端。
   2. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. let sandboxPath: string = context.filesDir + '/testSocket';
   4. let localAddress : socket.LocalAddress = {
   5. address: sandboxPath
   6. }
   7. let connectOpt: socket.LocalConnectOptions = {
   8. address: localAddress,
   9. timeout: 6000
   10. }
   11. let sendOpt: socket.LocalSendOptions = {
   12. data: 'Hello world!'
   13. }
   ```

   ```
   1. client.connect(connectOpt).then(() => {
   2. hilog.info(0x0000, 'testTag', `connect success`);
   3. // 发送数据。
   4. client.send(sendOpt).then(() => {
   5. hilog.info(0x0000, 'testTag', `send success`);
   6. }).catch((err: Object) => {
   7. hilog.info(0x0000, 'testTag', `send failed: ` + JSON.stringify(err));
   8. });
   9. }).catch((err: Object) => {
   10. hilog.info(0x0000, 'testTag', `connect fail: ` + JSON.stringify(err));
   11. });
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L101-L113)
5. Socket连接使用完毕后，取消事件的注册，并关闭套接字。

   ```
   1. // 当不需要再连接服务端，需要断开且取消事件的监听时。
   2. client.off('message');
   3. client.off('connect');
   4. client.off('close');
   5. client.close().then(() => {
   6. hilog.info(0x0000, 'testTag', 'close client success')
   7. // ...
   8. }).catch((err: Object) => {
   9. hilog.error(0x0000, 'testTag', 'close client err: ' + JSON.stringify(err))
   10. // ...
   11. })
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L210-L226)

## 应用通过Local Socket Server进行数据传输

服务端LocalSocket Server的主要流程包括：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L17-L21)
2. 使用constructLocalSocketServerInstance接口，创建一个 LocalSocketServer 服务端对象。

   ```
   1. // 创建一个LocalSocketServer连接，返回一个LocalSocketServer对象。
   2. let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L124-L127)
3. 启动服务，绑定本地套接字路径，创建出本地套接字文件，监听客户端的连接请求。

   ```
   1. // 创建并绑定本地套接字文件testSocket，进行监听。
   2. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. let sandboxPath: string = context.filesDir + '/testSocket';
   4. let listenAddr: socket.LocalAddress = {
   5. address: sandboxPath
   6. }
   ```

   ```
   1. server.listen(listenAddr).then(() => {
   2. // ...
   3. hilog.info(0x0000, 'testTag', `Server listening on ${address}`);
   4. }).catch((err: object) => {
   5. // ...
   6. hilog.error(0x0000, 'testTag', `Server listen error: ${JSON.stringify(err)}`);
   7. });
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L131-L143)
4. 注册LocalSocket的客户端连接事件，以及一些其它事件(可选)，在客户端连接成功时，可以获取到客户端连接会话对象LocalSocketConnection，通过该会话对象可以订阅客户端收到消息(message)事件，以及一些其它事件(可选)，通过该会话对象也可发起主动向客户端发送数据，主动关闭与客户端的连接的动作，订阅事件不再需要时，可以取消LocalSocketConnection相关的事件订阅。

   ```
   1. // 订阅LocalSocketServer的connect事件。
   2. server.on('connect', (connection: socket.LocalSocketConnection) => {
   3. // 订阅LocalSocketConnection相关的事件。
   4. connection.on('error', (err: Object) => {
   5. hilog.info(0x0000, 'testTag', 'on error success');
   6. });

   8. connection.on('message', (value: socket.LocalSocketMessageInfo) => {
   9. const uintArray = new Uint8Array(value.message);
   10. let messageView = '';
   11. for (let i = 0; i < uintArray.length; i++) {
   12. messageView += String.fromCharCode(uintArray[i]);
   13. }
   14. hilog.info(0x0000, 'testTag', `Server received: ${messageView}`);
   15. });

   17. connection.on('error', (err: Object) => {
   18. hilog.error(0x0000, 'testTag', 'err:' + JSON.stringify(err));
   19. })

   21. // 向客户端发送数据。
   22. let sendOpt : socket.LocalSendOptions = {
   23. data: 'Hello world!'
   24. };
   25. connection.send(sendOpt).then(() => {
   26. hilog.info(0x0000, 'testTag', 'Server send success');
   27. }).catch((err: object) => {
   28. hilog.error(0x0000, 'testTag', `Server send failed: ${JSON.stringify(err)}`);
   29. });

   31. // ...
   32. // 关闭与客户端的连接。
   33. connection.close().then(() => {
   34. hilog.info(0x0000, 'testTag', 'close success');
   35. }).catch((err: Object) => {
   36. hilog.error(0x0000, 'testTag', 'close failed: ' + JSON.stringify(err));
   37. });

   39. // 取消LocalSocketConnection相关的事件订阅。
   40. connection.off('message');
   41. connection.off('error');
   42. // ...
   43. });
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L145-L193)
5. 取消LocalSocketServer相关事件的订阅。

   ```
   1. // 取消LocalSocketServer相关的事件订阅。
   2. server.off('connect');
   3. server.off('error');
   ```

   [LocalSocketWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/LocalSocketWorker.ets#L199-L203)

## 应用通过TLS Socket进行加密数据传输

客户端TLS Socket流程（双向认证）包括：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TwoWayTlsWorker.ets#L17-L21)
2. 创建一个双向认证TLSSocket连接，返回一个TLSSocket对象。

   ```
   1. // 创建一个（双向认证）TLS Socket连接，返回一个TLS Socket对象。
   2. let tlsSocket: socket.TLSSocket | null = socket.constructTLSSocketInstance();
   ```

   [TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TwoWayTlsWorker.ets#L109-L112)
3. 绑定本地IP地址和端口，确保bind成功后，再订阅TLS Socket相关的订阅事件。上传客户端CA证书及数字证书，调用[connect](../harmonyos-references/js-apis-socket.md#connect9)接口建立连接。连接成功后，可调用[send](../harmonyos-references/js-apis-socket.md#send9)接口发送数据。

   ```
   1. // 绑定本地IP地址和端口。
   2. let ipAddress : socket.NetAddress = {} as socket.NetAddress;
   3. ipAddress.address = "192.168.xxx.xxx";
   4. ipAddress.port = 4512;

   6. // 服务器IP地址和端口。
   7. let serverAddress : socket.NetAddress = {} as socket.NetAddress;
   8. serverAddress.address = "192.168.xxx.xxx";
   9. serverAddress.port = 1234;

   11. let tlsSecureOption : socket.TLSSecureOptions = {} as socket.TLSSecureOptions;
   12. tlsSecureOption.key = "xxxx";
   13. tlsSecureOption.cert = "xxxx";
   14. tlsSecureOption.ca = ["xxxx"];
   15. tlsSecureOption.password = "xxxx";
   16. tlsSecureOption.protocols = [socket.Protocol.TLSv12];
   17. tlsSecureOption.useRemoteCipherPrefer = true;
   18. tlsSecureOption.signatureAlgorithms = "rsa_pss_rsae_sha256:ECDSA+SHA256";
   19. tlsSecureOption.cipherSuite = "AES256-SHA256";

   21. let tlsTwoWayConnectOption : socket.TLSConnectOptions = {} as socket.TLSConnectOptions;
   22. tlsTwoWayConnectOption.address = serverAddress;
   23. tlsTwoWayConnectOption.secureOptions = tlsSecureOption;
   24. tlsTwoWayConnectOption.ALPNProtocols = ["spdy/1", "http/1.1"];
   ```

   ```
   1. class SocketInfo {
   2. public message: ArrayBuffer = new ArrayBuffer(1);
   3. public remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
   4. }
   5. // 绑定本地IP地址和端口。
   6. tlsSocket!.bind(ipAddress).then(() => {
   7. hilog.info(0x0000, 'testTag', 'bind success');
   8. // ...
   9. // 确保bind成功后，再订阅TLS Socket相关的订阅事件
   10. tlsSocket!.on('message', (value: SocketInfo) => {
   11. hilog.info(0x0000, 'testTag', 'on message');
   12. let buffer = value.message;
   13. let dataView = new DataView(buffer);
   14. let str = '';
   15. for (let i = 0; i < dataView.byteLength; ++i) {
   16. str += String.fromCharCode(dataView.getUint8(i));
   17. }
   18. hilog.info(0x0000, 'testTag', 'on connect received:' + str);
   19. });

   21. tlsSocket!.on('connect', () => {
   22. // ...
   23. hilog.info(0x0000, 'testTag', 'on connect');
   24. });
   25. // 监听连接关闭
   26. tlsSocket!.on('close', () => {
   27. hilog.info(0x0000, 'testTag', 'on close');
   28. // ...
   29. });
   30. tlsSocket!.connect({ address: serverAddress, secureOptions: opt }).then(() => {
   31. hilog.info(0x0000, 'testTag', 'Connected successfully');
   32. // ...
   33. }).catch((e: BusinessError) => {
   34. hilog.error(0x0000, 'testTag', `Failed to connect: ${e.message}`);
   35. // ...
   36. });
   37. }).catch((e: BusinessError) => {
   38. hilog.error(0x0000, 'testTag', 'bind fail');
   39. // ...
   40. });
   41. // ...
   42. tlsSocket!.send('message').then(() => {
   43. hilog.info(0x0000, 'testTag', 'send successfully');
   44. // ...
   45. }).catch((e: BusinessError) => {
   46. hilog.error(0x0000, 'testTag', 'send failed ' + JSON.stringify(e));
   47. // ...
   48. });
   ```

   [TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TwoWayTlsWorker.ets#L116-L209)
4. TLSSocket连接使用完毕后，主动关闭。

   ```
   1. // 连接使用完毕后，主动关闭，并取消相关事件的订阅。
   2. tlsSocket!.close((err: BusinessError) => {
   3. if (err) {
   4. hilog.error(0x0000, 'testTag', 'close callback error = ' + err);
   5. } else {
   6. hilog.info(0x0000, 'testTag', 'close success');
   7. }
   8. tlsSocket!.off('message');
   9. tlsSocket!.off('connect');
   10. tlsSocket!.off('close');
   11. });
   ```

   [TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TwoWayTlsWorker.ets#L189-L201)

客户端TLS Socket流程（单向认证）包括：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [OneWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/OneWayTlsWorker.ets#L18-L22)
2. 创建一个单向认证TLSSocket连接，返回一个TLSSocket对象。

   ```
   1. // 创建一个（单向认证）TLS Socket连接，返回一个TLS Socket对象。
   2. let tlsOneWaySocket: socket.TLSSocket = socket.constructTLSSocketInstance();  // One way authentication
   ```

   [OneWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/OneWayTlsWorker.ets#L98-L101)
3. 绑定本地IP地址和端口，确保bind成功后，再订阅TLS Socket相关的订阅事件。上传客户端CA证书及数字证书，调用[connect](../harmonyos-references/js-apis-socket.md#connect9)接口建立连接。连接成功后，可调用[send](../harmonyos-references/js-apis-socket.md#send9)接口发送数据。

   ```
   1. // 绑定本地IP地址和端口。
   2. let ipAddress : socket.NetAddress = {} as socket.NetAddress;
   3. ipAddress.address = "192.168.xxx.xxx";
   4. ipAddress.port = 5445;

   6. // 服务器IP地址和端口。
   7. let serverAddress : socket.NetAddress = {} as socket.NetAddress;
   8. serverAddress.address = "192.168.xxx.xxx";
   9. serverAddress.port = 8789;
   10. let tlsOneWaySecureOption : socket.TLSSecureOptions = {} as socket.TLSSecureOptions;
   11. tlsOneWaySecureOption.ca = ["xxxx", "xxxx"];
   12. tlsOneWaySecureOption.cipherSuite = "AES256-SHA256";

   14. let tlsOneWayConnectOptions: socket.TLSConnectOptions = {} as socket.TLSConnectOptions;
   15. tlsOneWayConnectOptions.address = serverAddress;
   16. tlsOneWayConnectOptions.secureOptions = tlsOneWaySecureOption;
   ```

   ```
   1. class SocketInfo {
   2. public message: ArrayBuffer = new ArrayBuffer(1);
   3. public remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
   4. }
   5. // ...
   6. // 绑定本地IP地址和端口。
   7. tlsOneWaySocket!.bind(ipAddress).then(() => {
   8. hilog.info(0x0000, 'testTag', 'bind success');
   9. // ...
   10. /// 订阅TLS Socket相关的订阅事件
   11. tlsOneWaySocket!.on('message', (value: SocketInfo) => {
   12. hilog.info(0x0000, 'testTag', 'on message');
   13. let buffer = value.message;
   14. let dataView = new DataView(buffer);
   15. let str = '';
   16. for (let i = 0; i < dataView.byteLength; ++i) {
   17. str += String.fromCharCode(dataView.getUint8(i));
   18. }
   19. hilog.info(0x0000, 'testTag', 'on connect received:' + str);
   20. });
   21. tlsOneWaySocket!.on('connect', () => {
   22. hilog.info(0x0000, 'testTag', 'on connect');
   23. });
   24. tlsOneWaySocket!.on('close', () => {
   25. hilog.info(0x0000, 'testTag', 'on close');
   26. // ...
   27. });
   28. tlsOneWaySocket!.connect({ address: serverAddress, secureOptions: opt }).then(() => {
   29. hilog.info(0x0000, 'testTag', 'connect successfully');
   30. // ...
   31. }).catch((e: BusinessError) => {
   32. hilog.error(0x0000, 'testTag', `Failed to connect: ${e.message}`);
   33. // ...
   34. });
   35. }).catch((e: BusinessError) => {
   36. hilog.error(0x0000, 'testTag', 'bind fail');
   37. // ...
   38. });
   39. // ...
   40. // 建立连接，连接建立成功后，可以发送数据。
   41. tlsOneWaySocket.send(message + '\r\n').then(() => {
   42. hilog.info(0x0000, 'testTag', 'send successfully');
   43. // ...
   44. }).catch((e: BusinessError) => {
   45. hilog.error(0x0000, 'testTag', 'send failed ' + JSON.stringify(e));
   46. // ...
   47. });
   ```

   [OneWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/OneWayTlsWorker.ets#L103-L177)
4. TLSSocket连接使用完毕后，主动关闭。

   ```
   1. // 连接使用完毕后，主动关闭，并取消相关事件的订阅。
   2. tlsOneWaySocket!.close((err: BusinessError) => {
   3. if (err) {
   4. hilog.error(0x0000, 'testTag', 'close callback error = ' + err);
   5. // ...
   6. } else {
   7. hilog.info(0x0000, 'testTag', 'close success');
   8. // ...
   9. }
   10. tlsOneWaySocket!.off('message');
   11. tlsOneWaySocket!.off('connect');
   12. tlsOneWaySocket!.off('close');
   13. });
   ```

   [OneWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/OneWayTlsWorker.ets#L185-L203)

## 应用通过将TCP Socket升级为TLS Socket进行加密数据传输

客户端TCP Socket升级为TLS Socket流程，以TLS Socket双向认证为例：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Tcp2TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/Tcp2TwoWayTlsWorker.ets#L18-L22)
2. 参考[应用 TCP/UDP 协议进行通信](socket-connection.md#应用tcpudp协议进行通信)，创建一个TCPSocket连接。

   ```
   1. // 创建一个TCPSocket连接，返回一个TCPSocket对象。
   2. let tcpSocket: socket.TCPSocket = socket.constructTCPSocketInstance();
   ```

   [Tcp2TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/Tcp2TwoWayTlsWorker.ets#L112-L115)
3. 绑定本地IP地址和端口，绑定成功后，连接到服务器端IP地址和端口，连接成功后使用该TCPSocket对象创建TLSSocket，配置双向认证上传客户端 CA 证书及数字证书，可以建立TLSSocket连接，连接使用完毕后，主动关闭并取消相关事件的订阅。。

   ```
   1. // 连接到服务器端指定的IP地址和端口。
   2. let serverAddress: socket.NetAddress = {} as socket.NetAddress;
   3. serverAddress.address = "192.168.xxx.xxx";
   4. serverAddress.port = 1234;

   6. let tcpConnect: socket.TCPConnectOptions = {} as socket.TCPConnectOptions;
   7. tcpConnect.address = serverAddress;
   8. tcpConnect.timeout = 6000;

   10. // 配置TLSSocket目的地址、证书等信息。
   11. let tlsSecureOption: socket.TLSSecureOptions = {} as socket.TLSSecureOptions;
   12. tlsSecureOption.key = "xxxx";
   13. tlsSecureOption.cert = "xxxx";
   14. tlsSecureOption.ca = ["xxxx"];
   15. tlsSecureOption.password = "xxxx";
   16. tlsSecureOption.protocols = [socket.Protocol.TLSv12];
   17. tlsSecureOption.useRemoteCipherPrefer = true;
   18. tlsSecureOption.signatureAlgorithms = "rsa_pss_rsae_sha256:ECDSA+SHA256";
   19. tlsSecureOption.cipherSuite = "AES256-SHA256";

   21. let tlsTwoWayConnectOption: socket.TLSConnectOptions = {} as socket.TLSConnectOptions;
   22. tlsSecureOption.key = "xxxx";
   23. tlsTwoWayConnectOption.address = serverAddress;
   24. tlsTwoWayConnectOption.secureOptions = tlsSecureOption;
   25. tlsTwoWayConnectOption.ALPNProtocols = ["spdy/1", "http/1.1"];
   ```

   ```
   1. // 如果需要绑定特定的端口，可通过bind接口实现
   2. tcpSocket.connect(tcpConnect).then(() => {
   3. hilog.info(0x0000, 'testTag', 'connect success');
   4. // ...
   5. // 确保TCPSocket已连接后，将其升级为TLSSocket连接。
   6. tlsSocket = socket.constructTLSSocketInstance(tcpSocket);
   7. // 订阅TLSSocket相关的订阅事件。
   8. tlsSocket.on('message', (value: SocketInfo) => {
   9. hilog.info(0x0000, 'testTag', 'tls on message');
   10. let buffer = value.message;
   11. let dataView = new DataView(buffer);
   12. let str = '';
   13. for (let i = 0; i < dataView.byteLength; ++i) {
   14. str += String.fromCharCode(dataView.getUint8(i));
   15. }
   16. hilog.info(0x0000, 'testTag', 'tls on connect received:' + str);
   17. });
   18. tlsSocket.on('connect', () => {
   19. hilog.info(0x0000, 'testTag', 'tls on connect');
   20. });
   21. tlsSocket!.on('close', () => {
   22. hilog.info(0x0000, 'testTag', 'tls on close');
   23. // ...
   24. });
   25. // ...
   26. // 建立TLSSocket连接。
   27. tlsSocket.connect(tlsTwoWayConnectOption).then(() => {
   28. hilog.info(0x0000, 'testTag', 'tls connect success');
   29. // ...
   30. }).catch((e: BusinessError) => {
   31. hilog.info(0x0000, 'testTag', 'tls connect fail');
   32. // ...
   33. });
   34. }).catch((e: BusinessError) => {
   35. hilog.error(0x0000, 'testTag', 'connect fail');
   36. // ...
   37. });
   ```

   [Tcp2TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/Tcp2TwoWayTlsWorker.ets#L121-L183)
4. 连接使用完毕后，主动关闭。取消相关事件的订阅。。

   ```
   1. // 连接使用完毕后，主动关闭。取消相关事件的订阅。
   2. tlsSocket!.close((err: BusinessError) => {
   3. if (err) {
   4. // ...
   5. hilog.error(0x0000, 'testTag', 'tls close callback error = ' + err);
   6. } else {
   7. hilog.info(0x0000, 'testTag', 'tls close success');
   8. // ...
   9. }
   10. tlsSocket!.off('message');
   11. tlsSocket!.off('connect');
   12. tlsSocket!.off('close');
   13. });
   ```

   [Tcp2TwoWayTlsWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/Tcp2TwoWayTlsWorker.ets#L205-L223)

## 应用通过TLS Socket Server进行加密数据传输

服务端TLS Socket Server流程：

1. 导入所需的socket模块。

   ```
   1. import { socket } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [TlsServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TlsServerWorker.ets#L15-L19)
2. 创建一个TLSSocketServer连接，返回一个TLSSocketServer对象。

   ```
   1. let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
   ```

   [TlsServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TlsServerWorker.ets#L23-L25)
3. 启动服务，绑定 IP 和端口号，监听客户端连接，创建并初始化TLS会话，加载证书密钥并验证。

   ```
   1. let netAddress: socket.NetAddress = {
   2. address: '192.168.xx.xxx',
   3. port: 8080
   4. }

   6. let tlsSecureOptions: socket.TLSSecureOptions = {
   7. key: "xxxx",
   8. cert: "xxxx",
   9. ca: ["xxxx"],
   10. password: "xxxx",
   11. protocols: socket.Protocol.TLSv12,
   12. useRemoteCipherPrefer: true,
   13. signatureAlgorithms: "rsa_pss_rsae_sha256:ECDSA+SHA256",
   14. cipherSuite: "AES256-SHA256"
   15. }

   17. let tlsConnectOptions: socket.TLSConnectOptions = {
   18. address: netAddress,
   19. secureOptions: tlsSecureOptions,
   20. ALPNProtocols: ["spdy/1", "http/1.1"]
   21. }
   ```

   ```
   1. tlsServer.listen(tlsConnectOptions).then(() => {
   2. hilog.info(0x0000, 'testTag', 'listen callback success');
   3. // ...
   4. }).catch((err: BusinessError) => {
   5. hilog.error(0x0000, 'testTag', 'failed' + err);
   6. // ...
   7. });
   ```

   [TlsServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TlsServerWorker.ets#L68-L81)
4. 订阅TLSSocketServer的连接事件，收到客户端连接，通过回调得到TLSSocketConnection对象，通过该对象可以实现订阅TLSSocketConnection相关的事件、向客户端发送数据的动作，TLSSocketConnection连接使用完毕后，需要主动断开连接，进行取消订阅回调的动作。

   ```
   1. class SocketInfo {
   2. public message: ArrayBuffer = new ArrayBuffer(1);
   3. public remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
   4. }
   5. let callback = (value: SocketInfo) => {
   6. let messageView = '';
   7. for (let i: number = 0; i < value.message.byteLength; i++) {
   8. let uint8Array = new Uint8Array(value.message)
   9. let messages = uint8Array[i]
   10. let message = String.fromCharCode(messages);
   11. messageView += message;
   12. }
   13. hilog.info(0x0000, 'testTag', 'on message message: ' + JSON.stringify(messageView));
   14. hilog.info(0x0000, 'testTag', 'remoteInfo: ' + JSON.stringify(value.remoteInfo));
   15. // ...
   16. }
   17. // ...
   18. tlsServer.on('connect', (client: socket.TLSSocketConnection) => {
   19. client.on('message', callback);
   20. // 发送数据。
   21. client.send('Hello, client!').then(() => {
   22. hilog.info(0x0000, 'testTag', 'send success');
   23. // ...
   24. }).catch((err: BusinessError) => {
   25. hilog.error(0x0000, 'testTag', 'send fail');
   26. // ...
   27. });
   28. // 断开连接。
   29. client.close().then(() => {
   30. hilog.info(0x0000, 'testTag', 'close success');
   31. // ...
   32. }).catch((err: BusinessError) => {
   33. hilog.error(0x0000, 'testTag', 'close fail');
   34. // ...
   35. });

   37. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
   38. client.off('message', callback);
   39. client.off('message');
   ```

   [TlsServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TlsServerWorker.ets#L87-L139)
5. 取消订阅TLSSocketServer的相关事件。

   ```
   1. tlsServer.close();
   2. // 取消订阅tlsServer的相关事件
   3. tlsServer.off('connect');
   ```

   [TlsServerWorker.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/Socket/entry/src/main/ets/workers/TlsServerWorker.ets#L146-L150)
