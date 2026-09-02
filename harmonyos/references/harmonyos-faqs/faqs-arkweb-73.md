---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-73
title: 如何设置request.agent.Config中saveas参数
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何设置request.agent.Config中saveas参数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fc268c430cba66bf09378d49e13c0fdb282502a4ba55b8a8bacf0cc2d35d4f71
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

```ts
import { webview } from '@kit.ArkWeb';
import { request } from '@kit.BasicServicesKit';

// In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
let context = AppStorage.get("context") as UIContext;
let filesDir = context.getHostContext()!.filesDir;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'https://www-file.huawei.com/minisite/media/annual_report/annual_report_2023_cn.pdf',
  title: 'createTest',
  description: 'Sample code for create task',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: true,
  method: "get",
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
  console.info('upload task progress.');
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
          this.controller.loadUrl('file://' + filesDir + '/test.pdf')
        })
        .margin({ bottom: '20vp' })
      Web({ src: $rawfile('test.html'), controller: this.controller })
        .domStorageAccess(true)
        .onPageBegin((event)=>{
          request.agent.create(this.getUIContext().getHostContext(), config).then((task: request.agent.Task) => {
            task.on('progress', createOnCallback);
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
