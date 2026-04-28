---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-62
title: 如何判断应用程序是否安装
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何判断应用程序是否安装
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:951963ededb58fbf07a8f5e2d95d62da9d12f655e9058b51e2560242575b803a
---

为了应用A能判断设备上是否已安装应用B并决定是否引导用户下载应用B，需进行以下配置：

在B应用entry模块的module.json5文件中，添加配置的具体标签路径如下：module -> abilities -> skills -> uris。

```
1. "uris": [
2. {
3. "scheme":"schB",
4. "host":"com.example.test",
5. "path":"open",
6. }
7. ],
```

[a\_app\_module.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/a_app_module.json5#L38-L44)

在A应用entry模块的module.json5文件中，添加配置的具体标签路径为：module -> querySchemes。

```
1. "querySchemes": [
2. "schB"
3. ],
```

[b\_app\_module.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/b_app_module.json5#L12-L14)

应用A检查设备上是否安装了应用B。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { bundleManager } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. // Application A determines whether Application B is installed on the device
9. isAppBExist() {
10. let exist = false;
11. try {
12. let link = 'schB://com.example.test/open';
13. let data: boolean = bundleManager.canOpenLink(link);
14. hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(data));
15. exist = data;
16. } catch (err) {
17. let message = (err as BusinessError).message;
18. hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
19. exist = false;
20. }
21. console.info('Has application B been installed:' + exist);
22. }

24. @State text: string = 'isAppBExist'

26. build() {
27. Row() {
28. Column() {
29. Text(this.text)
30. .fontSize(30)
31. .fontWeight(FontWeight.Bold)
32. .onClick(() => {
33. this.isAppBExist();
34. });
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

[IndexA.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/ets/pages/IndexA.ets#L21-L60)

**参考链接**

[bundleManager.canOpenLink](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)
