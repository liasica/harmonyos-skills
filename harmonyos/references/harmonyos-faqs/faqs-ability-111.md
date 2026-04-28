---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-111
title: 如何通过resourceManager获取rawFile路径下的文件
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何通过resourceManager获取rawFile路径下的文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:52+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:ee326988541697f8da2419227f9b78619a775d7c3faceee12b2489cdcbbef320
---

**解决方案**

可以通过[@ohos.resourceManager](../harmonyos-references/js-apis-resource-manager.md)中的[getRawFileList](../harmonyos-references/js-apis-resource-manager.md#getrawfilelist10)方法获取RawFile路径下的所有文件。参考代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // Passing in '' indicates obtaining a list of files in the root directory of rawfile
4. try {
5. let context = AppStorage.get('context') as UIContext;
6. context.getHostContext()!.resourceManager.getRawFileList('', (error: BusinessError, value: Array<string>) => {
7. if (error != null) {
8. console.error(`callback getRawFileList failed, error code: ${error.code}, message: ${error.message}.`);
9. } else {
10. let rawFile = value;
11. }
12. });
13. } catch (error) {
14. let code = (error as BusinessError).code;
15. let message = (error as BusinessError).message;
16. console.error(`callback getRawFileList failed, error code: ${code}, message: ${message}.`);
17. }
```

[GetRaw.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetRaw.ets#L21-L37)
