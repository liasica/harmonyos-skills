---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-71
title: 如何判断当前网络的IP地址版本是多少
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何判断当前网络的IP地址版本是多少
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4d3f4e55e1381afea80e10e73f1572b541fd02ad47307dc592c99d1774a087b1
---

使用[NetAddress](../harmonyos-references/js-apis-net-connection.md#netaddress)类获取当前网络的地址信息，NetAddress类的family属性用于指定IP地址的版本，family属性的值为1表示IPv4，为2表示IPv6 。

示例代码如下：

```typescript
import { connection } from '@kit.NetworkKit';

@Entry
@Component
struct Index {
  getNetworkFamily() {
    try {
      let netHandle = connection.getDefaultNetSync();
      let connectionProperties = connection.getConnectionPropertiesSync(netHandle);
      if (connectionProperties !== undefined) {
        let linkAddressesArray = connectionProperties.linkAddresses;
        if (linkAddressesArray !== undefined && linkAddressesArray instanceof Array && linkAddressesArray.length > 0) {
          for (let i = 0; i < linkAddressesArray.length; i++) {
            let address: connection.NetAddress = linkAddressesArray[i].address;
            if (address !== undefined) {
              console.info("Succeeded to get address: " + JSON.stringify(address))
              if (address.family === 1) {
                console.info('Current network IP address version is ipv4')
              } else if (address.family === 2) {
                console.info('Current network IP address version is ipv6')
              }
            }
          }
        }
      }
    } catch (e) {
      console.error(`Get exception: ${e}`);
    }
  }

  build() {
    Column({ space: 10 }) {
      Button('获取当前网络IP地址版本')
        .onClick(() => {
          this.getNetworkFamily();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
