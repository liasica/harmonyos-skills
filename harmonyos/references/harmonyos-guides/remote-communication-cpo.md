---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-cpo
title: 通过配置Configuration优化传输性能
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > 提升HTTP传输性能 > 通过配置Configuration优化传输性能
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:7deb257710618a0f61fc9d59f6f4f0cda3b65c865b217e67cf7e5b708247fbf6
---

## 约束与限制

通过配置Configuration优化传输性能能力支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备。

## 导入模块

```typescript
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

## 请求预处理阶段

* 基于Session抽象的高并发网络框架
* 支持创建多个Session
* 支持请求动态取消
* 支持关闭Session
* Session中的资源互相独立、互不影响
* 应用可以通过使用Session来获取最佳的网络性能体验

  ```typescript
  const session1 = rcp.createSession({
    requestConfiguration: {
      transfer: {
        timeout: {
          connectMs: 5000,
          transferMs: 5000
        }
      }
    }
  });
  // 'https://example.com'是示例代码，请根据实际需求更改
  const request1 = new rcp.Request('https://example.com');
  const request2 = new rcp.Request('https://example.com');
  session1.fetch(request1).then((response) => {
    console.info(`Request1 succeeded, message is ${JSON.stringify(response)}`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`err1: error code is ${err.code}, error data is ${err.data}`);
  });
  session1.fetch(request2).then((response) => {
    console.info(`Request2 succeeded, message is ${JSON.stringify(response)}`);
    // ...
    session1.close();
  }).catch((err: BusinessError) => {
    console.error(`err2: error code is ${err.code}, error data is ${err.data}`);
    session1.close();
  });
  session1.cancel(request1); // 取消request1请求
  ```

## DNS阶段

应用可[定制DNS](remote-communication-customdnsconfig.md)请求规则，如定制DNS服务器、重写DNS解析函数，从而获取最佳的DNS性能体验。

```typescript
// 定制DNS解析函数
const session = rcp.createSession();
// 'https://example.com'是示例网址，请根据实际需求更改
const request = new rcp.Request('https://example.com');
request.configuration = {
  dns: {
    dnsRules: (host: string, port: number): rcp.IpAddress[] => {
      // 'example.com'是示例域名,192.168.1.1'和'192.168.1.2'是示例IP，请根据实际需求更改
      if (host === 'example.com') {
        return ['192.168.1.1', '192.168.1.2'];
      }
      return [];
    }
  }
};
// ...
session.fetch(request).then((response) => {
  console.info(`Request succeeded, message is ${JSON.stringify(response)}`);
  // ...
}).catch((err: BusinessError) => {
  console.error(`err: error code is ${err.code}, error data is ${err.data}`);
  // ...
});
```

```typescript
// 定制DNS服务器
const session = rcp.createSession();
// 'https://example.com'是示例网址，请根据实际需求更改
const request = new rcp.Request('https://example.com');
request.configuration = {
  dns: {
    // '192.168.1.1'是示例IP，53是示例端口，请根据实际需求更改
    dnsRules: [
      {
        ip: '192.168.1.1',
        port: 53,
      },
    ]
  }
};
// ...
session.fetch(request).then((response) => {
  console.info(`Request succeeded, message is ${JSON.stringify(response)}`);
  // ...
}).catch((err: BusinessError) => {
  console.error(`err: error code is ${err.code}, error data is ${err.data}`);
  // ...
});
```

## 连接阶段

根据资源特征动态调整连接池大小

```typescript
const session = rcp.createSession({
  connectionConfiguration: {
    maxConnectionsPerHost: 16,
    maxTotalConnections: 1024,
  }
});
for (let i = 0; i < 1024; ++i) {
  // 请求的网址是示例网址，请根据实际需求更改
  session.get('https://example' + i.toString() + '.com/image.png').then((response) => {
    console.info(`Request succeeded, message is ${JSON.stringify(response)}`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`err: error code is ${err.code}, error data is ${err.data}`);
    // ...
  });
}
```

## HTTP请求阶段

* 支持响应体分段返回，以节省内存
* 支持直接将响应写入文件，以节省内存
* 支持请求体分段上传，以节省内存

  ```typescript
  // 使用响应体直接写入文件
  const session = rcp.createSession();
  try {
    // 'https://example.com/video.mp4'是示例网址，请根据实际需求更改
    const response = await session.get('https://example.com/video.mp4', {
      kind: 'file',
      file: '/data/storage/el2/base/entry/temp/videoMp4',
    });
    console.info(`Request succeeded, message is ${JSON.stringify(response)}`);
    // ...
  } catch (err) {
    console.error(`err: error code is ${err.code}, error data is ${err.data}`);
    // ...
  } finally {
    session.close();
  }
  ```

  ```typescript
  // 分段上传数据
  const session = rcp.createSession();
  try {
    // 'https://example.com/video.mp4'是示例网址，请根据实际需求更改
    const response = await session.post('https://example.com/video.mp4', (maxSize: number) => {
      return new ArrayBuffer(maxSize);
    });
    console.info(`Request succeeded, message is ${JSON.stringify(response)}`);
    // ...
  } catch (err) {
    console.error(`err: error code is ${err.code}, error data is ${err.data}`);
    // ...
  } finally {
    session.close();
  }
  ```

## HTTP响应阶段

获取响应各阶段耗时动态判断网络质量，动态调整请求（请求不同质量的资源、降低资源缓存数量）。更详细的示例请移步[HTTP请求过程中各时间点详解](remote-communication-tpms.md#http请求过程中各时间点详解)。

```typescript
// 获取各个阶段的耗时信息
const session = rcp.createSession({requestConfiguration: {tracing: tracingConfig}});
try {
  // 'https://example.com'是示例网址，请根据实际需求更改
  const response = await session.get('https://example.com');
  console.info(response.timeInfo?.nameLookupTimeMs.toString());
  console.info(response.timeInfo?.connectTimeMs.toString());
  console.info(response.timeInfo?.tlsHandshakeTimeMs.toString());
  console.info(response.timeInfo?.preTransferTimeMs.toString());
  console.info(response.timeInfo?.startTransferTimeMs.toString());
  console.info(response.timeInfo?.totalTimeMs.toString());
  console.info(response.timeInfo?.redirectTimeMs.toString());
  // ...
} catch (err) {
  console.error(`err: error code is ${err.code}, error data is ${err.data}`);
  // ...
} finally {
  session.close();
}
```
