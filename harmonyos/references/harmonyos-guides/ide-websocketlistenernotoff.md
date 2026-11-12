---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-websocketlistenernotoff
title: WebSocketListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > WebSocketListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:676be2fa50d5d9b1e19597533a072a43ab506e3030f5e7cbfdd8123a63dde57f
---

[@ohos.net.webSocket (WebSocket连接)](../doccenter-references/api/js-apis-websocket.md)提供WebSocket客户端与服务端的双向连接能力，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "WebSocketListenerNotOff",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import Ability from '@ohos.app.ability.Ability';

/**
 * 正例：正确释放资源
 */
class TestRelease extends Ability {
    private ws: webSocket.WebSocket = webSocket.createWebSocket();
    private ws2: webSocket.WebSocket = webSocket.createWebSocket();
    private webSocketCallbackOpen = (err: BusinessError, value: Object) => {
        console.info('on open');
    }
    private webSocketCallbackMessage = (err: BusinessError, value: Object) => {
        console.info('on message');
    }
    private webSocketCallbackError1 = (err: BusinessError) => {
        console.info('1 on error');
    }
    private webSocketCallbackError2 = (err: BusinessError) => {
        console.info('2 on error');
    }
    onCreate(): void {
        this.ws.on('open', this.webSocketCallbackOpen);
        this.ws.on('message', this.webSocketCallbackMessage);
        this.ws.on('error', this.webSocketCallbackError1);
        this.ws.on('error', this.webSocketCallbackError2);
        this.ws2.on('error', this.webSocketCallbackError2);
    }
    onDestroy(): void {
        this.ws.off('open', this.webSocketCallbackOpen);
        this.ws.off('message', this.webSocketCallbackMessage);
        this.ws.off('error', this.webSocketCallbackError1);
        this.ws.off('error', this.webSocketCallbackError2);
        this.ws2.off('error', this.webSocketCallbackError2);
    }
}
```

## 反例

```ts
import { webSocket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import Ability from '@ohos.app.ability.Ability';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends Ability {
    private ws: webSocket.WebSocket = webSocket.createWebSocket();
    private ws2: webSocket.WebSocket = webSocket.createWebSocket();
    private webSocketCallbackOpen = (err: BusinessError, value: Object) => {
        console.info('on open');
    }
    private webSocketCallbackMessage = (err: BusinessError, value: Object) => {
        console.info('on message');
    }
    private webSocketCallbackError1 = (err: BusinessError) => {
        console.info('1 on error');
    }
    private webSocketCallbackError2 = (err: BusinessError) => {
        console.info('2 on error');
    }
    onCreate(): void {
        this.ws.on('open', this.webSocketCallbackOpen);
        this.ws.on('message', this.webSocketCallbackMessage);
        this.ws.on('error', this.webSocketCallbackError1); // leak
        this.ws.on('error', this.webSocketCallbackError2);
        this.ws2.on('error', this.webSocketCallbackError2); // leak
    }
    onDestroy(): void {
        this.ws.off('open', this.webSocketCallbackOpen);
        this.ws.off('message', this.webSocketCallbackMessage);
        this.ws.off('error', this.webSocketCallbackError2);
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
