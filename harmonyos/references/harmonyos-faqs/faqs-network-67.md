---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-67
title: 如何监听判断VPN类型网络
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何监听判断VPN类型网络
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:3dd658a84b6940e1850632242c12cb2f5aa23e0d78f4a4166de5564850eb831c
---

VPN类型可使用getNetCapabilities方法获取到bearerTypes，当[bearerTypes](../harmonyos-references/js-apis-net-connection.md#netbeartype)的值是4时表示使用了VPN。需要权限：ohos.permission.INTERNET、ohos.permission.GET\_NETWORK\_INFO。

参考代码如下：

```typescript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct JudeNetType {
  getNetType() {
    connection.getAllNets((error: BusinessError, allNets: connection.NetHandle[]) => {
      if (error) {
        console.error(`Failed to get getAllNets. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      for (let netHandle of allNets) {
        connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
          if (error) {
            console.error(`Failed to get capabilities. Code: ${error.code}, message: ${error.message}`);
            return;
          }
          if (data.bearerTypes[0] == connection.NetBearType.BEARER_VPN) {
            console.info('The VPN network is connected');
          }
        })
      }
    });
  }

  build() {
    Column({ space: 10 }) {
      Button('Obtain the type of network connection').onClick(() => {
        this.getNetType()
      })
    }.alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

参考文档：[网络连接管理](../harmonyos-references/js-apis-net-connection.md#netbeartype)
