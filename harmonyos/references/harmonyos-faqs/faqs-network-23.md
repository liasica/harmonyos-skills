---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-23
title: Socket接口库是否支持绑定域名
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > Socket接口库是否支持绑定域名
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:49742efabdcde1f292a3ea67a3dc72df9e448d876717d527c87944f30f6d32a9
---

Socket不支持域名访问，只能使用IP地址。域名需要通过DNS解析为对应的IP地址。

参考代码如下：

```typescript
import { connection } from '@kit.NetworkKit'
import { BusinessError } from "@kit.BasicServicesKit"

connection.getAddressesByName("xxxx", (error: BusinessError, data: connection.NetAddress[]) => {
  console.log(JSON.stringify(error));
  console.log(JSON.stringify(data));
})
```

**参考链接**

[connection.getAddressesByName](../harmonyos-references/js-apis-net-connection.md#connectiongetaddressesbyname)
