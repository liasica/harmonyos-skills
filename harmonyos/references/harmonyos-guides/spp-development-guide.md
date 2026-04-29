---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spp-development-guide
title: 连接和传输数据
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 传统蓝牙 > 连接和传输数据
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7e206b73d2b4641c37e8d94dbeef9d9e9568d8a2f024a83d61d8cc4bb5c98e70
---

## 简介

本指南主要提供了基于串口通信协议（Serial Port Profile，SPP）实现设备间连接和传输数据的开发指导。当两个设备间进行SPP通信交互时，依据设备功能的不同，可区分为客户端与服务端，本指南将分别介绍客户端与服务端的实现方法。

## 实现原理

客户端获取到服务端的设备地址后，即可向服务端特定的UUID发起连接。服务端设备地址可以通过查找设备流程获取，详见[查找设备](br-discovery-development-guide.md)。待两端连接成功后，可向服务端发送数据或者接收服务端的数据。

服务端需要支持客户端连接的UUID服务，保持连接状态监听即可。待两端连接成功后，即可接收客户端数据或者向客户端发送数据。

客户端和服务端都可以主动断开连接，应用需要根据实际场景决定由哪一端执行断开操作。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### 导入所需API模块

导入socket和错误码模块。

```
1. import { socket } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 客户端

**1. 发起连接**

客户端通过查找设备流程搜索到目标设备后，即可发起连接。需要连接的UUID服务，必须与服务端创建socket时构造的UUID服务一致。在连接过程中，蓝牙子系统会去查询服务端是否支持该UUID服务，若不支持，则会连接失败。因此应用需要确保目标设备是否支持需要的UUID服务，否则发起的是无效连接。

```
1. // 设备地址可以通过查找设备流程获取
2. let peerDevice = 'XX:XX:XX:XX:XX:XX';

4. // 定义客户端socket id
5. let clientNumber = -1;

7. // 配置连接参数
8. let option: socket.SppOptions = {
9. uuid: '00009999-0000-1000-8000-00805F9B34FB', // 需要连接的服务端UUID服务，确保服务端支持
10. secure: false,
11. type: socket.SppType.SPP_RFCOMM
12. };
13. console.info('startConnect ' + peerDevice);
14. socket.sppConnect(peerDevice, option, (err, num: number) => {
15. if (err) {
16. console.error('startConnect errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. } else {
18. console.info('startConnect clientNumber: ' + num);
19. clientNumber = num;
20. }
21. });
22. console.info('startConnect after ' + peerDevice);
```

**2. 传输数据**

**2.1 发送数据**

待客户端和服务端连接建立成功后，即可向服务端发送数据。

```
1. let clientNumber = 1; // 注意：该值需要的是客户端发起连接时，异步callback获取到的客户端socket id，此处是伪代码id
2. let arrayBuffer = new ArrayBuffer(2);
3. let data = new Uint8Array(arrayBuffer);
4. data[0] = 3;
5. data[1] = 4;
6. try {
7. socket.sppWrite(clientNumber, arrayBuffer);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

**2.2 接收数据**

待客户端和服务端连接建立成功后，即可接收服务端的数据。通过订阅读取数据接口[socket.on('sppRead')](../harmonyos-references/js-apis-bluetooth-socket.md#socketonsppread)实现。

```
1. let clientNumber = 1; // 注意：该值需要的是客户端发起连接时，异步callback获取到的客户端socket id，此处是伪代码id

3. // 定义接收数据的回调函数
4. function read(dataBuffer: ArrayBuffer) {
5. let data = new Uint8Array(dataBuffer);
6. console.info('client data: ' + JSON.stringify(data));
7. }

9. try {
10. // 发起订阅
11. socket.on('sppRead', clientNumber, read);
12. } catch (err) {
13. console.error('readData errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

**3. 断开连接**

当应用不再需要已建立的连接时，可以通过客户端主动断开连接。需要先取消读取数据的订阅，再断开连接。

```
1. let clientNumber = 1; // 注意：该值需要的是客户端发起连接时，异步callback获取到的客户端socket id，此处是伪代码id

3. // 定义接收数据的回调函数
4. function read(dataBuffer: ArrayBuffer) {
5. let data = new Uint8Array(dataBuffer);
6. console.info('client data: ' + JSON.stringify(data));
7. }

9. try {
10. // 取消接收数据订阅
11. socket.off('sppRead', clientNumber, read);
12. } catch (err) {
13. console.error('off sppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
15. try {
16. // 从client端断开连接
17. socket.sppCloseClientSocket(clientNumber);
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
```

### 服务端

**1. 创建服务端套接字**

服务端需通过创建套接字的方式，在蓝牙子系统中注册指定的UUID服务。该UUID服务的名称无限制，可使用应用名称。当客户端发起连接请求时，会携带一个UUID以表示所需连接的服务。只有服务端与客户端的UUID一致时，连接才能成功建立。

```
1. // 定义服务端socket id
2. let serverNumber = -1;

4. // 配置监听参数
5. let option: socket.SppOptions = {
6. uuid: '00009999-0000-1000-8000-00805F9B34FB',
7. secure: false,
8. type: socket.SppType.SPP_RFCOMM
9. };

11. // 创建服务端监听socket，将在蓝牙子系统中注册该UUID服务
12. socket.sppListen("demonstration", option, (err, num: number) => {
13. if (err) {
14. console.error('sppListen errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
15. } else {
16. console.info('sppListen serverNumber: ' + num);
17. serverNumber = num;
18. }
19. });
```

**2. 监听客户端连接**

创建好服务端套接字后，服务端即可监听连接。待收到客户端连接后，会获取到标识此次客户端的socket id，此时也表示服务端和客户端的连接已建立成功。

```
1. let serverNumber = 1; // 注意：该值需要的是创建服务端套接字时，异步callback获取到的服务端socket id，此处是伪代码id

3. // 定义客户端socket id
4. let clientNumber = -1;

6. socket.sppAccept(serverNumber, (err, num: number) => {
7. if (err) {
8. console.error('accept errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. } else {
10. console.info('accept clientNumber: ' + num);
11. clientNumber = num;
12. }
13. });
```

**3. 传输数据**

**3.1 发送数据**

待服务端和客户端的连接建立成功后，即可向客户端发送数据。

```
1. let clientNumber = 1; // 注意：该值需要的是服务端监听连接时，异步callback获取到的客户端socket id，此处是伪代码id

3. let arrayBuffer = new ArrayBuffer(2);
4. let data = new Uint8Array(arrayBuffer);
5. data[0] = 9;
6. data[1] = 8;
7. try {
8. socket.sppWrite(clientNumber, arrayBuffer);
9. } catch (err) {
10. console.error('sppWrite errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

**3.2 接收数据**

待服务端和客户端的连接建立成功后，即可接收客户端的数据。通过订阅读取数据接口[socket.on('sppRead')](../harmonyos-references/js-apis-bluetooth-socket.md#socketonsppread)实现。

```
1. let clientNumber = 1; // 注意：该值需要的是服务端监听连接时，异步callback获取到的客户端socket id，此处是伪代码id

3. // 定义接收数据的回调函数
4. function read(dataBuffer: ArrayBuffer) {
5. let data = new Uint8Array(dataBuffer);
6. console.info('client data: ' + JSON.stringify(data));
7. }

9. try {
10. // 发起订阅
11. socket.on('sppRead', clientNumber, read);
12. } catch (err) {
13. console.error('readData errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

**4. 断开连接**

当应用不再需要已建立的连接时，可以通过服务端主动断开连接。

* 需要先取消读取数据的订阅，再断开连接。

```
1. let clientNumber = 1; // 注意：该值需要的是服务端监听连接时，异步callback获取到的客户端socket id，此处是伪代码id

3. // 定义接收数据的回调函数
4. function read(dataBuffer: ArrayBuffer) {
5. let data = new Uint8Array(dataBuffer);
6. console.info('client data: ' + JSON.stringify(data));
7. }

9. try {
10. // 取消订阅
11. socket.off('sppRead', clientNumber, read);
12. } catch (err) {
13. console.error('off sppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
15. try {
16. // 从server断开连接
17. socket.sppCloseClientSocket(clientNumber);
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
```

**5. 删除服务端套接字**

当应用不再需要该服务端套接字时，需要主动关闭创建时获取到的套接字，蓝牙子系统会删除此前注册的UUID服务。如果此时客户端发起连接，就会连接失败。

* 应用也可以通过删除套接字时，实现断开连接。在此之前，需要先取消读取数据的订阅。

```
1. let clientNumber = 1; // 注意：该值需要的是服务端监听连接时，异步callback获取到的客户端socket id，此处是伪代码id
2. let serverNumber = 1; // 注意：该值需要的是创建服务端套接字时，异步callback获取到的服务端socket id，此处是伪代码id

4. // 定义接收数据的回调函数
5. function read(dataBuffer: ArrayBuffer) {
6. let data = new Uint8Array(dataBuffer);
7. console.info('client data: ' + JSON.stringify(data));
8. }

10. try {
11. // 取消订阅
12. socket.off('sppRead', clientNumber, read);
13. } catch (err) {
14. console.error('off sppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
15. }

17. try {
18. // 若应用不再需要此能力，则主动删除
19. socket.sppCloseServerSocket(serverNumber);
20. } catch (err) {
21. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
22. }
```

## 完整示例

### 客户端

```
1. import { socket } from '@kit.ConnectivityKit'
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class SppClientManager {
5. // 定义客户端的socket id
6. clientNumber: number = -1;

8. // 发起连接
9. public startConnect(peerDevice: string): void {
10. // 配置连接参数
11. let option: socket.SppOptions = {
12. uuid: '00009999-0000-1000-8000-00805F9B34FB', // 需要连接的服务端UUID服务，确保服务端支持
13. secure: false,
14. type: socket.SppType.SPP_RFCOMM
15. };
16. console.info('startConnect ' + peerDevice);
17. socket.sppConnect(peerDevice, option, (err, num: number) => {
18. if (err) {
19. console.error('startConnect errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. } else {
21. console.info('startConnect clientNumber: ' + num);
22. this.clientNumber = num;
23. }
24. });
25. console.info('startConnect after ' + peerDevice);
26. }

28. // 发送数据
29. public sendData() {
30. console.info('sendData ' + this.clientNumber);
31. if (this.clientNumber == -1) {
32. console.error('invalid clientNumber');
33. return;
34. }
35. let arrayBuffer = new ArrayBuffer(2);
36. let data = new Uint8Array(arrayBuffer);
37. data[0] = 3;
38. data[1] = 4;
39. try {
40. socket.sppWrite(this.clientNumber, arrayBuffer);
41. } catch (err) {
42. console.error('sppWrite errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
43. }
44. }

46. // 定义接收数据的回调函数
47. read = (dataBuffer: ArrayBuffer) => {
48. let data = new Uint8Array(dataBuffer);
49. console.info('client data: ' + JSON.stringify(data));
50. };

52. // 接收数据
53. public readData() {
54. try {
55. // 发起订阅
56. if (this.clientNumber == -1) {
57. console.error('invalid clientNumber');
58. return;
59. }
60. socket.on('sppRead', this.clientNumber, this.read);
61. } catch (err) {
62. console.error('readData errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
63. }
64. }

66. // 断开连接
67. public stopConnect() {
68. console.info('closeSppClient ' + this.clientNumber);
69. if (this.clientNumber == -1) {
70. console.error('invalid clientNumber');
71. return;
72. }
73. try {
74. // 取消接收数据订阅
75. socket.off('sppRead', this.clientNumber, this.read);
76. } catch (err) {
77. console.error('off sppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
78. }
79. try {
80. // 从client端断开连接
81. socket.sppCloseClientSocket(this.clientNumber);
82. } catch (err) {
83. console.error('stopConnect errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
84. }
85. }
86. }

88. let sppClientManager = new SppClientManager();
89. export default sppClientManager as SppClientManager;
```

### 服务端

```
1. import { socket } from '@kit.ConnectivityKit'
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class SppServerManager {
5. serverNumber: number = -1;
6. clientNumber: number = -1;

8. // 创建服务端监听socket
9. public startListen(): void {
10. console.info('startListen');

12. // 配置监听参数
13. let option: socket.SppOptions = {
14. uuid: '00009999-0000-1000-8000-00805F9B34FB',
15. secure: false,
16. type: socket.SppType.SPP_RFCOMM
17. };

19. // 创建服务端监听socket，将在蓝牙子系统中注册该UUID服务
20. socket.sppListen("demonstration", option, (err, num: number) => {
21. if (err) {
22. console.error('sppListen errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
23. } else {
24. console.info('sppListen serverNumber: ' + num);
25. this.serverNumber = num;
26. }
27. });
28. }

30. // 监听连接请求，等待连接
31. public accept() {
32. console.info('accept ' + this.serverNumber);
33. if (this.serverNumber == -1) {
34. console.error('invalid serverNumber');
35. return;
36. }
37. socket.sppAccept(this.serverNumber, (err, num: number) => {
38. if (err) {
39. console.error('accept errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
40. } else {
41. console.info('accept clientNumber: ' + num);
42. this.clientNumber = num;
43. }
44. });
45. }

47. // 发送数据
48. public sendData() {
49. console.info('sendData serverNumber: ' + this.serverNumber + ' clientNumber: ' + this.clientNumber);
50. if (this.clientNumber == -1) {
51. console.error('invalid clientNumber');
52. return;
53. }
54. let arrayBuffer = new ArrayBuffer(2);
55. let data = new Uint8Array(arrayBuffer);
56. data[0] = 9;
57. data[1] = 8;
58. try {
59. socket.sppWrite(this.clientNumber, arrayBuffer);
60. } catch (err) {
61. console.error('sppWrite errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
62. }
63. }

65. // 定义接收数据的回调函数
66. read = (dataBuffer: ArrayBuffer) => {
67. let data = new Uint8Array(dataBuffer);
68. console.info('client data: ' + JSON.stringify(data));
69. };

71. // 接收数据
72. public readData() {
73. try {
74. // 发起订阅
75. if (this.clientNumber == -1) {
76. console.error('invalid clientNumber');
77. return;
78. }
79. socket.on('sppRead', this.clientNumber, this.read);
80. } catch (err) {
81. console.error('readData errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
82. }
83. }

85. // 停止连接
86. public stopConnect() {
87. console.info('stopConnect');
88. try {
89. // 取消订阅
90. if (this.clientNumber == -1) {
91. console.error('invalid clientNumber');
92. return;
93. }
94. socket.off('sppRead', this.clientNumber, this.read);
95. } catch (err) {
96. console.error('off sppRead errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
97. }
98. try {
99. // 从server断开连接
100. socket.sppCloseClientSocket(this.clientNumber);
101. } catch (err) {
102. console.error('stopConnect errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
103. }
104. }

106. // 删除能力
107. public closeSppServer() {
108. console.info('closeSppServer');
109. try {
110. // 若应用不再需要此能力，则主动删除
111. if (this.serverNumber == -1) {
112. console.error('invalid serverNumber');
113. return;
114. }
115. socket.sppCloseServerSocket(this.serverNumber);
116. } catch (err) {
117. console.error('sppCloseServerSocket errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
118. }
119. }
120. }

122. let sppServerManager = new SppServerManager();
123. export default sppServerManager as SppServerManager;
```
