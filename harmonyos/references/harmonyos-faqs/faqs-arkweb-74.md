---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-74
title: 如何使用Web组件下载pdf文件并展示给用户
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何使用Web组件下载pdf文件并展示给用户
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7fd87dc9e5727ceeda1651a37ac53b50691a37a9fe176b55de9e024dddf714cf
---

**问题场景**

使用Webview加载指定URL，下载PDF文件并展示。

**解决措施**

通过[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)方法可以区分是否下载 PDF 文件。下载 PDF 功能可以通过[request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10)方法实现。

具体实现逻辑为：首先，使用request模块将网络PDF下载到沙箱路径，然后通过Web组件加载并展示给用户。

在工程的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。

**参考代码**

```ts
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { request } from '@kit.BasicServicesKit';

let context = AppStorage.get("context") as UIContext;
let filesDir = context.getHostContext()!.filesDir;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'https://www-file.huawei.com/minisite/media/annual_report/annual_report_2023_cn.pdf',
  title: 'createTest',
  description: 'Sample code for create task',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: true,
  method: 'get',
  saveas: filesDir + '/test.pdf',
  network: request.agent.Network.WIFI,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: 'it is a secret'
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('download task completed.');
  context.getPromptAction().showToast({
    message: 'Download completed',
    duration: 2000
  });
};

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State uri: string = '';
  @State isChange: boolean = false;

  build() {
    Column() {
      Button('Refresh UI')
        .width('200vp')
        .onClick(() => {
          this.controller.loadUrl('file://' + filesDir + '/test.pdf');
        })
        .margin({ bottom: '20vp' })
      Web({ src: $rawfile('WebDownloadPDF.html'), controller: this.controller })
        .fileAccess(true)
        .domStorageAccess(true)
        .onPageBegin((event) => {
          request.agent.create(this.getUIContext().getHostContext(), config).then((task: request.agent.Task) => {
            task.on('completed', createOnCallback);
            console.info(`Succeeded in creating a download task. result: ${task.config}`);
            task.start();
          }).catch((err: Error) => {
            console.error(`Failed to create a download task, message: ${err.message}`);
          });
        })
    }
  }
}
```
