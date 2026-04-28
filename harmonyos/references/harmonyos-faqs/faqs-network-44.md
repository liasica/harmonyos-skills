---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-44
title: 使用SocketServer时，如何解决较高概率接收不到 client.on("message", (value: SocketInfo) 中的回调问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 使用SocketServer时，如何解决较高概率接收不到 client.on("message", (value: SocketInfo) 中的回调问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1c277722a4e38a648cbf9ba2bee6f4609560e21a32753d8faadebd501431f7b4
---

**原因**

客户端的socket被回收释放而导致较高概率接收不到client.on("message", (value: SocketInfo) 中的回调。

**解决措施**

定义一个数组，客户端连接时，将客户端的socket添加到数组中，防止被回收，确保能接收数据。代码如下：

```
1. import { socket } from '@kit.NetworkKit';

3. let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
4. // 定义存放客户端连接的数组
5. let tcpConnectArray: socket.TCPSocketConnection[] = [];

7. class SocketInfo {
8. message: ArrayBuffer = new ArrayBuffer(1);
9. remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
10. }

12. @Entry
13. @Component
14. struct CreateSocket {
15. build() {
16. Column() {
17. Button('创建socket').onClick(async () => {
18. tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
19. // 保存客户端的socket
20. tcpConnectArray.push(client);
21. // Subscribe to events of the TCPSocketConnection object.
22. client.on('close', () => {
23. console.log("on close success");
24. });
25. client.on('message', (value: SocketInfo) => {
26. // 此处高概率收不到message
27. let buffer = value.message;
28. let dataView = new DataView(buffer);
29. let str = '';
30. for (let i = 0; i < dataView.byteLength; ++i) {
31. str += String.fromCharCode(dataView.getUint8(i));
32. }
33. console.log('received message--:' + str);
34. });
35. })
36. console.log('create socket Succeeded ');
37. })

39. }
40. .height('100%')
41. .width('100%')
42. .justifyContent(FlexAlign.Center)
43. }
44. }
```

[SetSocketServer.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetSocketServer.ets#L21-L64)
