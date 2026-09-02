---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-70
title: connection如何获取网卡链路地址、DNS地址等信息
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > connection如何获取网卡链路地址、DNS地址等信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:f95e8810fda800887b2940f29c4aebbc78601c5212afdded0d7e265ba030bc82
---

使用[connection.getConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)获取netHandle对应网络的连接信息，包括网卡链路地址和DNS地址。需要权限：ohos.permission.INTERNET、ohos.permission.GET\_NETWORK\_INFO。参考代码如下：

```typescript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetConnectionProperties {
  getConnectionProperties() {
    connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
      connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
        if (error) {
          console.error(`Failed to get connection properties. Code:${error.code}, message:${error.message}`);
          return;
        }
        console.info('Succeeded to get data: ' + JSON.stringify(data));
      })
    });
  }

  build() {
    Column({ space: 10 }) {
      Button('获取对应的网络连接信息')
        .onClick(() => {
          this.getConnectionProperties();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
