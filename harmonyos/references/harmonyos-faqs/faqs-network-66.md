---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-66
title: 无网络环境下使用同步方法获取网络状态报错
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 无网络环境下使用同步方法获取网络状态报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:914141783ac2dba93676243b59d24172ef6df76ea8a230ec846b0764e876bb2d
---

在无网环境中调用同步方法请求时，无法解析nethandle对应的内容，方法执行时会报错。可以使用try-catch语句捕获并处理报错信息。参考代码如下：

```typescript
import { connection } from '@kit.NetworkKit'
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetErrInfo {
  getErrInfo() {
    try {
      let netHandle = connection.getDefaultNetSync();
      let connectionproperties = connection.getConnectionPropertiesSync(netHandle);
    } catch (err) {
      let error: BusinessError = err as BusinessError;
      console.log('error: ' + JSON.stringify(error));
    }
  }

  build() {
    Row() {
      Column() {
        Button('获取网络类型')
          .onClick(() => {
            this.getErrInfo();

          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
