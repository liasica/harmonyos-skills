---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-44
title: 如何读取指定文件内容，并转为具体对象
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何读取指定文件内容，并转为具体对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:59edb6ebe161a17ccee2036535380ea46113f9cf6d9642a3318b52120429746a
---

可以使用[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)方法，参考代码如下：

```
1. import { Context } from '@kit.AbilityKit';
2. import { buffer } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct Index {
7. private context: Context | undefined = this.getUIContext().getHostContext();
8. private str: string = '';

10. getRawFile(): ESObject {
11. //Call the getRawFileContent interface to retrieve the content of a JSON file and read it as a string
12. this.getUIContext().getHostContext()!.resourceManager.getRawFileContent('test.json', (err, data) => {
13. try {
14. this.str = buffer.from(data.buffer).toString();
15. console.info(JSON.stringify(this.str));
16. } catch (e) {
17. console.info(JSON.stringify(e));
18. }
19. })
20. //You can also call the getRawFileContentSync interface to retrieve the content of the JSON file and read it as a string
21. try {
22. let data: Uint8Array = this.context!.resourceManager.getRawFileContentSync('test.json');
23. this.str = buffer.from(data.buffer).toString();
24. } catch (e) {
25. console.info(JSON.stringify(e));
26. }
27. // Convert string to ESObject
28. let obj: ESObject = JSON.parse(this.str);
29. console.info('ESObject', JSON.stringify(obj));
30. return obj;
31. }

33. build() {
34. Column() {
35. Button('get')
36. .onClick(() => {
37. this.getRawFile();
38. })
39. }.width('100%')
40. }
41. }
```

[FileContentParser.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/FileContentParser.ets#L21-L61)
