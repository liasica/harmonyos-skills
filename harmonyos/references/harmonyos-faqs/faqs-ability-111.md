---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-111
title: 如何通过resourceManager获取rawFile路径下的文件
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何通过resourceManager获取rawFile路径下的文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0192eee3efa39574f954a6c0c7534c346a6b16f355a7267d531d3d4208bb945c
---

**解决方案**

可以通过[@ohos.resourceManager](../harmonyos-references/js-apis-resource-manager.md)中的[getRawFileList](../harmonyos-references/js-apis-resource-manager.md#getrawfilelist10)方法获取RawFile路径下的所有文件。参考代码如下：

```screen
import { BusinessError } from '@kit.BasicServicesKit';

// Passing in '' indicates obtaining a list of files in the root directory of rawfile
try {
  let context = AppStorage.get('context') as UIContext;
  context.getHostContext()!.resourceManager.getRawFileList('', (error: BusinessError, value: Array<string>) => {
    if (error != null) {
      console.error(`callback getRawFileList failed, error code: ${error.code}, message: ${error.message}.`);
    } else {
      let rawFile = value;
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`callback getRawFileList failed, error code: ${code}, message: ${message}.`);
}
```
