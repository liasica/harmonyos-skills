---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-74
title: 如何使用Web组件下载pdf文件并展示给用户
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何使用Web组件下载pdf文件并展示给用户
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ce58e677aad619d37046901d7a0926b878914975dd59c8dabb5de95b0b4b8239
---

**问题场景**

使用Webview加载指定URL，下载PDF文件并展示。

**解决措施**

通过[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)方法可以区分是否下载 PDF 文件。下载 PDF 功能可以通过[request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10)方法实现。

具体实现逻辑为：首先，使用request模块将网络PDF下载到沙箱路径，然后通过Web组件加载并展示给用户。

在工程的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。

**参考代码**

```
1. import { webview } from '@kit.ArkWeb';
2. import { common } from '@kit.AbilityKit';
3. import { request } from '@kit.BasicServicesKit';

5. let context = AppStorage.get("context") as UIContext;
6. let filesDir = context.getHostContext()!.filesDir;
7. let config: request.agent.Config = {
8. action: request.agent.Action.DOWNLOAD,
9. url: 'https://www-file.huawei.com/minisite/media/annual_report/annual_report_2023_cn.pdf',
10. title: 'createTest',
11. description: 'Sample code for create task',
12. mode: request.agent.Mode.FOREGROUND,
13. overwrite: true,
14. method: 'get',
15. saveas: filesDir + '/test.pdf',
16. network: request.agent.Network.WIFI,
17. metered: false,
18. roaming: true,
19. retry: true,
20. redirect: true,
21. index: 0,
22. begins: 0,
23. ends: -1,
24. gauge: false,
25. precise: false,
26. token: 'it is a secret'
27. };
28. let createOnCallback = (progress: request.agent.Progress) => {
29. console.info('download task completed.');
30. context.getPromptAction().showToast({
31. message: 'Download completed',
32. duration: 2000
33. });
34. };

36. @Entry
37. @Component
38. struct Index {
39. controller: webview.WebviewController = new webview.WebviewController();
40. @State uri: string = '';
41. @State isChange: boolean = false;

43. build() {
44. Column() {
45. Button('Refresh UI')
46. .width('200vp')
47. .onClick(() => {
48. this.controller.loadUrl('file://' + filesDir + '/test.pdf');
49. })
50. .margin({ bottom: '20vp' })
51. Web({ src: $rawfile('WebDownloadPDF.html'), controller: this.controller })
52. .fileAccess(true)
53. .domStorageAccess(true)
54. .onPageBegin((event) => {
55. request.agent.create(this.getUIContext().getHostContext(), config).then((task: request.agent.Task) => {
56. task.on('completed', createOnCallback);
57. console.info(`Succeeded in creating a download task. result: ${task.config}`);
58. task.start();
59. }).catch((err: Error) => {
60. console.error(`Failed to create a download task, message: ${err.message}`);
61. });
62. })
63. }
64. }
65. }
```

[UseWebDownloadPdf.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UseWebDownloadPdf.ets#L21-L85)
