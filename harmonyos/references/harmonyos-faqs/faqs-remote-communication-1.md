---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-1
title: rcp模块发起请求时如何设置超时时间
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp模块发起请求时如何设置超时时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5b08cf0bb1866eb8a309d86f63d60c50e579fb241aebec0173399cfa024b38ad
---

rcp模块发起请求如需要设置超时时间，可在建立session会话前设置SessionConfiguration内有关参数。

相关示例如下：

```typescript
import { rcp } from '@kit.RemoteCommunicationKit';

const sessionConfig: rcp.SessionConfiguration = {
  // Used to specify the configuration of HTTP requests associated with the session
  requestConfiguration: {
    transfer: {
      // Timeout parameter setting
      timeout: {
        // The connection has timed out. The default value is 60,000
        connectMs: 5000,
        // Transmission timeout, with the default value being 60,000
        transferMs: 10000,
      },
    }
  }
};
const session = rcp.createSession(sessionConfig);

@Entry
@Component
export struct SetTimeout {
  build() {
    Row() {
      Column() {
        Button($r('app.string.timeout_parameter_setting'))
          .onClick(() => {
            if (session) {
              console.log('Created session successful!')
              console.log('Connection timeout parameter settings:',
                sessionConfig.requestConfiguration?.transfer?.timeout?.connectMs);
              console.log('Transmission timeout parameters settings:',
                sessionConfig.requestConfiguration?.transfer?.timeout?.transferMs);
            } else {
              console.log('Created session failure!');
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
