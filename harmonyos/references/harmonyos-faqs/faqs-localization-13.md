---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-13
title: 如何将文件转换成字符串
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何将文件转换成字符串
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:607dc7dbbe035ff0d2206f3a2164990e457ca5b4ca4c24ece2c085a01f9703a7
---

1. 获取resources/rawfile目录下对应的rawfile文件内容。
2. 调用util模块的TextDecoder将字节数组解码为字符串。
3. 对Uint8Array进行解码。

参考示例如下：

```
1. import { util } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct FileToString {
7. build() {
8. Row() {
9. Column() {
10. Button('file to string')
11. .onClick(() => {
12. getContext().resourceManager.getRawFileContent('test.txt').then((value: Uint8Array) => {
13. let textDecoder: util.TextDecoder = util.TextDecoder.create(); // Call the TextDecoder class of the til module
14. let decodedString: string = textDecoder.decodeToString(value); // 对Uint8Array解码
15. let strBase64 = new util.Base64Helper().encodeToStringSync(value); // Convert a Uint8Array to a Base64 string
16. console.info('retStr:', decodedString);
17. console.info('strBase64:', strBase64);
18. }).catch((error: BusinessError) => {
19. console.error(`callback getRawFileContent failed, error code: ${error.code}, message: ${error.message}.`);
20. });
21. })
22. }
23. .width('100%')
24. }
25. .height('100%')
26. }
27. }
```

[FileToString.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalizationKit/entry/src/main/ets/pages/FileToString.ets#L21-L47)

**参考链接**

[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)

[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)
