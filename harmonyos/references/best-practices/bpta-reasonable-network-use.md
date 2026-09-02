---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-network-use
title: 网络资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 网络资源合理使用
category: best-practices
scraped_at: 2026-09-02T15:03:22+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d6c74658f47172a90ff4b724484539fc38bc6170ea64b42df3a07c0b7db2b5ec
---

无长时任务的应用退到后台时，主动断开TCP和UDP连接。

## 约束

如果应用不主动断开socket连接，系统将强制断开TCP连接。应用返回前台后，需主动重新创建连接。

## 示例

### HTTP数据请求

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { http } from '@kit.NetworkKit';

export default class EntryAbility extends UIAbility {
  // ...
  onForeground(): void {
    // Create an HTTP request based on the service requirements at the foreground
    let httpRequest: http.HttpRequest = http.createHttp();
    // ...
  }

  onBackground(): void {
    // ...
    // Go back to the background and release the http request
    httpRequest.destroy();
  }
}
```

有关HTTP数据请求相关接口的使用，详情可以参考[使用HTTP访问网络](../harmonyos-guides/http-request.md)。

### Socket连接

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...
  tcp: socket.TCPSocket = socket.constructTCPSocketInstance();

  onForeground(): void {
    /**
     * In the foreground, create a socket connection and send service data as required, for example:
     * this.tcp.bind(ipAddress, (err: BusinessError) => {})
     * this.tcp.connect(tcpConnect, (err: BusinessError) => {})
     * this.tcp.send(tcpSendOptions, (err: BusinessError) => {})
     */
  }

  onBackground(): void {
    // Go back to the background and close the socket connection
    this.tcp.close((err: BusinessError) => {})
  }
}
```

有关网络Socket相关接口的使用，详情可以参考[使用Socket访问网络](../harmonyos-guides/socket-connection.md)。

### WebSocket连接

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // Create a websocket based on service requirements
  ws: webSocket.WebSocket = webSocket.createWebSocket();

  onForeground(): void {
    // Send data through websocket in the foreground
    this.ws.on('open', (err: BusinessError, value: Object) => {
      console.log("onopen,status:" + JSON.stringify(value));
      // When an on ('open') event is received, you can communicate with the server through the send () method
      this.ws.send("Hello,server!", (err: BusinessError, value: boolean) => {
        if (!err) {
          console.log("Messagesentsuccessfully");
        } else {
          console.log("Failedtosendthemessage.Err:" + JSON.stringify(err));
        }
      });
    });
  }

  onBackground(): void {
    // Backstage closes websocket
    this.ws.close((err: BusinessError) => {});
  }
}
```

有关网络WebSocket相关接口的使用，详情可以参考[使用WebSocket访问网络](../harmonyos-guides/websocket-connection.md)。
