---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-suggest-use-socket-in-async-thread
title: "@performance/suggest-use-socket-in-async-thread"
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/suggest-use-socket-in-async-thread
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5e90abff7c2caa99241f81488e0346f7bb8eafaad84fcc6f53b3f3d2cf4bde4d
---

使用Socket连接时，建议在异步线程或子线程中进行，在UI主线程进行耗时过长影响性能。

## 规则配置

```json
// code-linter.json5
{
  "rules": {
    "@performance/suggest-use-socket-in-async-thread": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Concurrent
async function doSocketTask(address: string, port: number, message: string): Promise<string> {
  let tcp = socket.constructTCPSocketInstance();

  try {
    // 在子线程进行连接  
    await tcp.connect({ address: { address: address, port: port } });
    await tcp.send({ data: message });
    return "发送成功并收到响应";
  } catch (err) {
    let error = err as BusinessError;
    throw new Error(`Socket Error: ${error.code} - ${error.message}`);
  } finally {
    await tcp.close();
  }
}
```

## 反例

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SocketBadExample {
  @State message: string = '等待发送...';

  build() {
    Column() {
      Text(this.message).fontSize(20).margin(20)
      Button('发送数据').onClick(() => {
        this.message = '连接中...';
        let tcp = socket.constructTCPSocketInstance();

        tcp.connect({ address: { address: '192.168.1.100', port: 8080 } })
          .then(() => {
            this.message = '连接成功';
            return tcp.send({ data: 'Hello, HarmonyOS!' });
          })
          .then(() => {
            this.message = '发送完成';
          })
          .catch((err: BusinessError) => {
            this.message = '出错：' + err.message;
          });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查（ArkTS/TS）](ide-code-linter.md)。
