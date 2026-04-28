---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-73
title: 如何设置request.agent.Config中saveas参数
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何设置request.agent.Config中saveas参数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:46+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:b7c4362f627780655c2852d1721609d0bcb66e6c7a5664afa83ca5094d231214
---

**问题场景**

可以通过设置saveas参数将下载保存路径设置为getHostContext().filesDir。

**解决措施**

saveas参数在[request.agent.Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)中有较为详细的描述，saveas参数支持以下几种方式：

1. 相对路径，位于调用方的缓存路径下，如"./xxx/yyy/zzz.html"、"xxx/yyy/zzz.html"。
2. internal协议路径，仅支持"internal://cache/"及其子路径，如"internal://cache/path/to/file.txt"。
3. 应用沙箱目录，只支持到base及其子目录下，如"/data/storage/el1/base/path/to/file.txt"。
4. file协议路径，必须匹配应用包名，只支持到base及其子目录下，如"file://com.example.test/data/storage/el2/base/file.txt"。

默认使用相对路径。

可以通过设置saveas参数将下载保存路径设置为getHostContext().filesDir。

**参考代码**

需要在工程中的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。

```
1. import { webview } from '@kit.ArkWeb';
2. import { request } from '@kit.BasicServicesKit';

4. // In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
5. let context = AppStorage.get("context") as UIContext;
6. let filesDir = context.getHostContext()!.filesDir;
7. let config: request.agent.Config = {
8. action: request.agent.Action.DOWNLOAD,
9. url: 'https://www-file.huawei.com/minisite/media/annual_report/annual_report_2023_cn.pdf',
10. title: 'createTest',
11. description: 'Sample code for create task',
12. mode: request.agent.Mode.FOREGROUND,
13. overwrite: true,
14. method: "get",
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
29. console.info('upload task progress.');
30. };

32. @Entry
33. @Component
34. struct Index {
35. controller: webview.WebviewController = new webview.WebviewController();
36. @State uri: string = '';
37. @State isChange: boolean = false;

39. build() {
40. Column() {
41. Button('Refresh UI')
42. .width('200vp')
43. .onClick(() => {
44. this.controller.loadUrl('file://' + filesDir + '/test.pdf')
45. })
46. .margin({ bottom: '20vp' })
47. Web({ src: $rawfile('test.html'), controller: this.controller })
48. .domStorageAccess(true)
49. .onPageBegin((event)=>{
50. request.agent.create(this.getUIContext().getHostContext(), config).then((task: request.agent.Task) => {
51. task.on('progress', createOnCallback);
52. console.info(`Succeeded in creating a download task. result: ${task.config}`);
53. task.start();
54. }).catch((err: Error) => {
55. console.error(`Failed to create a download task, message: ${err.message}`);
56. });
57. })
58. }
59. }
60. }
```

[ConfigSaveAsParameter.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/ConfigSaveAsParameter.ets#L21-L80)
