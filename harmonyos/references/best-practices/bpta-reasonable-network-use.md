---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-network-use
title: 网络资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 网络资源合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:a6465cf86ec27ee8705ddb2e4203622f4848dac891db5cfd650184fb95bf64fb
---

无长时任务的应用退到后台时，主动断开TCP和UDP连接。

## 约束

如果应用不主动断开socket连接，系统将强制断开TCP连接。应用返回前台后，需主动重新创建连接。

## 示例

### HTTP数据请求

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { http } from '@kit.NetworkKit';

4. export default class EntryAbility extends UIAbility {
5. // ...
6. onForeground(): void {
7. // Create an HTTP request based on the service requirements at the foreground
8. let httpRequest: http.HttpRequest = http.createHttp();
9. // ...
10. }

12. onBackground(): void {
13. // ...
14. // Go back to the background and release the http request
15. httpRequest.destroy();
16. }
17. }
```

[Https.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/Https.ets#L7-L25)

有关HTTP数据请求相关接口的使用，详情可以参考[使用HTTP访问网络](../harmonyos-guides/http-request.md)。

### Socket连接

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { socket } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. // ...
7. tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

9. onForeground(): void {
10. /**
11. * In the foreground, create a socket connection and send service data as required, for example:
12. * this.tcp.bind(ipAddress, (err: BusinessError) => {})
13. * this.tcp.connect(tcpConnect, (err: BusinessError) => {})
14. * this.tcp.send(tcpSendOptions, (err: BusinessError) => {})
15. */
16. }

18. onBackground(): void {
19. // Go back to the background and close the socket connection
20. this.tcp.close((err: BusinessError) => {})
21. }
22. }
```

[Socket.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/Socket.ets#L7-L28)

有关网络Socket相关接口的使用，详情可以参考[使用Socket访问网络](../harmonyos-guides/socket-connection.md)。

### WebSocket连接

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { webSocket } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. // Create a websocket based on service requirements
8. ws: webSocket.WebSocket = webSocket.createWebSocket();

11. onForeground(): void {
12. // Send data through websocket in the foreground
13. this.ws.on('open', (err: BusinessError, value: Object) => {
14. console.log("onopen,status:" + JSON.stringify(value));
15. // When an on ('open') event is received, you can communicate with the server through the send () method
16. this.ws.send("Hello,server!", (err: BusinessError, value: boolean) => {
17. if (!err) {
18. console.log("Messagesentsuccessfully");
19. } else {
20. console.log("Failedtosendthemessage.Err:" + JSON.stringify(err));
21. }
22. });
23. });
24. }

27. onBackground(): void {
28. // Backstage closes websocket
29. this.ws.close((err: BusinessError) => {});
30. }
31. }
```

[WebSocket.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/WebSocket.ets#L7-L37)

有关网络WebSocket相关接口的使用，详情可以参考[使用WebSocket访问网络](../harmonyos-guides/websocket-connection.md)。
