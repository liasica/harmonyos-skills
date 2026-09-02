---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-3
title: 如何读取rawfile中的xml文件并转化为String类型
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何读取rawfile中的xml文件并转化为String类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:90a4597c7c25ad3aa97c8c06921a0dacb29c13865f092c5620cc2533fad28ea2
---

使用resourceManager的getRawFileContent接口获取xml数据。使用util工具函数中的decodeToString接口将数据转化为string类型。

参考代码如下：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

// In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
let context = AppStorage.get("context") as UIContext;

try {
  context.getHostContext()!.resourceManager.getRawFileContent('test.xml', (error, value) => {
    if (error != null) {
      console.log('error is ' + error);
    } else {
      let rawFile = value;
      let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM : true });
      let rawFileString = textDecoder.decodeToString( rawFile , {stream: false});
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`callback getRawFileContent failed, error code: ${code}, message: ${message}.`);
}
```

**参考链接**

[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)
