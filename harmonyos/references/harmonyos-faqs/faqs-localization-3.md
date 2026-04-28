---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-3
title: 如何读取rawfile中的xml文件并转化为string类型
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何读取rawfile中的xml文件并转化为string类型
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2433728537e4453eaf595351369a0e301c80c6f2f4edd69058a8fa5ebca144ac
---

使用resourceManager的getRawFileContent接口获取xml数据。使用util工具函数中的decodeToString接口将数据转化为string类型。

参考代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { util } from '@kit.ArkTS';

4. // In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
5. let context = AppStorage.get("context") as UIContext;

7. try {
8. context.getHostContext()!.resourceManager.getRawFileContent('test.xml', (error, value) => {
9. if (error != null) {
10. console.log('error is ' + error);
11. } else {
12. let rawFile = value;
13. let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM : true });
14. let rawFileString = textDecoder.decodeToString( rawFile , {stream: false});
15. }
16. });
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let message = (error as BusinessError).message;
20. console.error(`callback getRawFileContent failed, error code: ${code}, message: ${message}.`);
21. }
```

[RawXmlFileToStringParser.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/LocalizationKit/entry/src/main/ets/pages/RawXmlFileToStringParser.ets#L21-L41)

**参考链接**

[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)
