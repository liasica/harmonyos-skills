---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-137
title: 使用ArkWeb下载文件提示完成但文件为何为空
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 使用ArkWeb下载文件提示完成但文件为何为空
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a9aa1f3e49a1c9aece9a47137c22f96238d5e0491228e3332a68b47eeff9b24d
---

## 问题现象

使用ArkWeb下载文件时，下载代理提示已下载完成，并且有实际下载内容，但是保存文件时为空。

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri, picker } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          // 下载开始前通知给用户，用户需要在此接口中调用WebDownloadItem.start("xxx")并提供下载路径，否则下载会一直处于PENDING状态。
          this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
            console.info('EntryAbility: will start a download.');
            const documentSaveOptions = new picker.DocumentSaveOptions();
            documentSaveOptions.newFileNames =
              ['fileName_' + (new Date()).getTime() + '.txt'];
            documentSaveOptions.fileSuffixChoices = ['.txt'];
            let uris: Array<string> = [];
            let documentViewPicker = new picker.DocumentViewPicker();
            documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
              uris = documentSaveResult;
              if (0 == uris.length) {
                return;
              }
              console.info(`EntryAbility: documentViewPicker.save to file succeed and uris are:${uris}`);
              webDownloadItem.start(uris[0].toString());
              console.info(`EntryAbility: download to ${uris[0].toString()}`);
            }).catch((err: BusinessError) => {
              console.error(`EntryAbility: Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
            });
          });

          this.controller.setDownloadDelegate(this.delegate);
        });
      Button('startDownload')
        .onClick(() => {
          try {
            this.controller.startDownload('www.example.com');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      Web({ src: 'www.example.com', controller: this.controller });
    };
  }
}
```

日志打印下载完成：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/kJbZyg25QASBHQFyRLwZ_A/zh-cn_image_0000002659138403.png "点击放大")

实际下载文件为空：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/w9S2x46ITpOqFYW700zT7Q/zh-cn_image_0000002629059052.png "点击放大")

## 背景知识

* [监听页面触发的下载](../harmonyos-guides/web-download.md#监听页面触发的下载)：通过[setDownloadDelegate()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setdownloaddelegate11)向Web组件注册一个DownloadDelegate来监听页面触发的下载任务。资源由Web组件进行下载，Web组件会通过DownloadDelegate将下载的进度通知给应用。
* [@ohos.file.picker](../harmonyos-references/js-apis-file-picker.md)：选择器(Picker)是一个封装DocumentViewPicker、AudioViewPicker、PhotoViewPicker的API模块，具有选择与保存的能力。
* [DocumentSaveOptions](../harmonyos-references/js-apis-file-picker.md#documentsaveoptions)：文档保存选项。DocumentSaveOptions是选择器(@ohos.file.picker)模块的核心配置类，用于定制文件保存操作的行为。

## 问题定位

* 确认文件是否由webDownloadItem.start下载生成：
  1. 在picker选择器后打断点执行，发现在webDownloadItem.start执行之前，手机中已经生成文件。由此判断，此时文件并非由webDownloadItem.start下载，而是picker选择器创建的空文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/hwD9uWrdQdSHKpmp9IR63A/zh-cn_image_0000002659258355.png "点击放大")
  2. 添加URI转换const uri = new fileUri.FileUri\(uris\[0\]\);，文件下载成功。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/DMFHFeJuSzmvKGr_tHT4Dw/zh-cn_image_0000002628899136.png "点击放大")
* 验证非当前HAP包名的文件夹是否可以作为文件下载路径：选择非当前HAP包名的文件夹进行下载，此时文件无法下载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/BKVgcbAHSP-sqm_PDLxH3g/zh-cn_image_0000002659138405.png "点击放大")

## 分析结论

未设置picker选择器配置DocumentSaveOptions的pickerMode时，pickerMode = picker.DocumentPickerMode.DEFAULT，此时选择指定目录，会在目录下生成空文件，适合需要生成文件再进行数据写入的场景。

## 修改建议

修改picker选择器配置DocumentSaveOptions的pickerMode文档保存选项为picker.DocumentPickerMode.DOWNLOAD，选择器自动返回当前HAP包名的文件夹。修改后代码如下：

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri, picker } from '@kit.CoreFileKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();

  build() {
    Column() {
      Button('setDownloadDelegate')
        .onClick(() => {
          // 下载开始前通知给用户，用户需要在此接口中调用WebDownloadItem.start("xxx")并提供下载路径，否则下载会一直处于PENDING状态。
          this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
            console.info('EntryAbility: will start a download.');
            const documentSaveOptions = new picker.DocumentSaveOptions();
            // 修改pickerMode为DOWNLOAD，删除newFileNames和fileSuffixChoices，设置为DOWNLOAD时，配置的参数newFileNames和fileSuffixChoices将不会生效
            documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
            let uris: Array<string> = [];
            let documentViewPicker = new picker.DocumentViewPicker();
            documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
              // 固定返回当前HAP包名的文件夹
              uris = documentSaveResult;
              if (0 == uris.length) {
                return;
              }
              console.info(`EntryAbility: documentViewPicker.save to file succeed and uris are:${uris}`);

              const uriString = documentSaveResult[0];
              if (!uriString) {
                return;
              }
              // 添加文件路径转换
              const uri = new fileUri.FileUri(uriString);
              webDownloadItem.start(uri.path + '/fileName_' + (new Date()).getTime() + '.txt');
              console.info(`EntryAbility: download to ${uri.path}`);
            }).catch((err: BusinessError) => {
              console.error(`EntryAbility: Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
            });
          });

          this.controller.setDownloadDelegate(this.delegate);
        });
      Button('startDownload')
        .onClick(() => {
          try {
            // 运行时需替换为实际的链接
            this.controller.startDownload('XXX');
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
      // 运行时需替换为实际的链接
      Web({ src: 'XXX', controller: this.controller }).fileAccess(false).geolocationAccess(false);
    };
  }
}
```

## 总结

使用选择器选择下载路径时，需要注意DocumentSaveOptions的pickerMode选项：

* pickerMode = picker.DocumentPickerMode.DEFAULT适用场景：选择指定目录，在目录下生成空文件，适合需要生成文件再进行数据写入的场景。
* pickerMode = picker.DocumentPickerMode.DOWNLOAD适用场景：固定返回当前HAP包名的文件夹路径，没有文件夹时自动创建，适合需要下载文件存放路径的场景。
