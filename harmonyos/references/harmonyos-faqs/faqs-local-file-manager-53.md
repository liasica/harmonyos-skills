---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-53
title: 应用内下载的非图片、视频类文件，在设备上找不到
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 应用内下载的非图片、视频类文件，在设备上找不到
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fd659d63ae24c65d1454d792bf331219777fc4255112bd9feb95548d2389c51e
---

## 问题现象

用户在应用中选择下载非图片、视频类的文件后。在应用内可以看到文件已下载到“已下载”的目录下，但是进行查看，却找不到该路径和已经下载的文件。

但是对于图片、视频等媒体类型的文件，在应用内下载后，可以在用户的相册中看到对应的文件。

## 背景知识

* [应用文件概述](../harmonyos-guides/app-file-overview.md)：应用文件包括应用安装文件、应用资源文件和应用缓存文件，文件所有者是应用。
* [应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)：应用沙箱是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。
* [DownloadFileButton](../harmonyos-references/ohos-arkui-advanced-downloadfilebutton.md)：下载文件按钮，通过点击该下载按钮，可以获取到当前应用在Download公共目录中所属的存储路径。
* [选择用户文件](../harmonyos-guides/select-user-file.md)：用户需要分享文件、保存图片、视频等用户文件时，开发者可以通过系统预置的文件选择器（FilePicker），实现该能力。
* [DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)：文件选择器对象，用来支撑选择和保存各种格式文档。在使用前，需要先创建DocumentViewPicker实例。
* [应用文件上传下载](../harmonyos-guides/app-file-upload-download.md)：应用可以将应用文件上传到网络服务器，也可以从网络服务器下载网络资源文件到本地应用文件目录。
* [下载网络资源文件至用户文件](../harmonyos-guides/app-file-upload-download.md#下载网络资源文件至用户文件)：开发者可以使用上传下载模块（ohos.request）的request.agent下载接口将网络资源文件下载到用户文件。
* [使用弹窗授权保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md#使用弹窗授权保存媒体库资源)：通过弹窗授权的方式保存文件到用户文件下。

## 问题定位

1. 根据HiLog日志进行定位，根据关键字“storage”进行检索：

   ```screen
   07-15 13:56:49.070   51395-51395   C01406/com.hm.example/OHOS::RS  com.hm.example  I     RSUIDirector::PostTask messageId:78, cmdCount:2, instanceId:100000
   07-15 13:56:49.172   51395-52404   C015B0/com.hm.example/NETSTACK  com.hm.example  I     [http_exec.cpp:418] taskid=-2147483647, size:1179024, dns:0.079, connect:0.486, tls:0.000, firstSend:0.201, firstRecv:131.338, total:503.940, redirect:0.000, errCode:0, RespCode:200, httpVer:2, method:GET, osErr:0
   07-15 13:56:49.174   51395-51395   C03F01/com.hm.example/NAPI  com.hm.example  I     [(:467)(HandleTaskResultCallback)] taskpool:: Task PerformTask End: taskId : 394970511104, performResult : Successful
   07-15 13:56:49.175   51395-51395   A03D00/com.hm.example/JSAPP  com.hm.example  I     沙箱路径 根路径已存在: /data/storage/el2/base/haps/entry/files
   07-15 13:56:49.175   51395-51395   A03D00/com.hm.example/JSAPP  com.hm.example  I     file exists
   07-15 13:56:49.175   51395-51395   A03D00/com.hm.example/JSAPP  com.hm.example  I     file exists
   07-15 13:56:49.175   51395-51395   A03D00/com.hm.example/JSAPP  com.hm.example  I     file exists
   07-15 13:56:49.175   51395-51395   A03D00/com.hm.example/JSAPP  com.hm.example  I     file exists
   07-15 13:56:49.176   51395-51395   A03D00/com.hm.example/JSAPP  com.hm.example  I     file exists
   ```

2. 以上日志信息中有存储的文件路径信息：/data/storage/el2/base/haps/entry/files，该文件路径为文件沙箱目录。

   | 目录名 | Context属性名称 | 类型 | 说明 |
   | --- | --- | --- | --- |
   | base | NA | 本设备文件路径 | 应用在本设备上存放持久化数据的目录，子目录包含files/、cache/、temp/和haps/；随应用卸载而清理。 |

## 分析结论

由于应用将非媒体文件直接存储在应用沙箱目录，而用户无法直接访问应用沙箱目录，所以导致了下载的非媒体文件对用户不可见。

## 修改建议

* 方案1：

  通过调用DocumentViewPicker的save()接口保存文件并获得用户文件的uri，将此uri作为request.agent的config中的saveas字段值进行下载。

  ```screen
  import { BusinessError, request } from '@kit.BasicServicesKit';
  import { picker } from '@kit.CoreFileKit';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    build() {
      Row() {
        Column() {
          Button("下载文档").width("50%").margin({ top: 20 }).height(40).onClick(async () => {
            // 创建文件管理器选项实例。
            const documentSaveOptions = new picker.DocumentSaveOptions();
            // 保存文件名（可选）。 默认为空。
            documentSaveOptions.newFileNames = ["xxxx.txt"];
            // 保存文件类型['后缀类型描述|后缀类型']，选择所有文件：'所有文件(*.*)|.*'（可选），如果选择项存在多个后缀（最大限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
            documentSaveOptions.fileSuffixChoices = ['文档|.txt', '.pdf'];

            let uri: string = '';
            // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            const documentViewPicker = new picker.DocumentViewPicker(context);
            await documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
              uri = documentSaveResult[0];
            }).catch((err: BusinessError) => {
              console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
            });
            if (uri != '') {
              let config: request.agent.Config = {
                action: request.agent.Action.DOWNLOAD,
                url: 'https://xxxx/xxxx.txt',
                // saveas字段是DocumentViewPicker保存的文件的uri
                saveas: uri,
                gauge: true,
                // overwrite字段必须为true
                overwrite: true,
                network: request.agent.Network.WIFI,
                // mode字段必须为request.agent.Mode.FOREGROUND
                mode: request.agent.Mode.FOREGROUND,
              };
              try {
                request.agent.create(context, config).then((task: request.agent.Task) => {
                  task.start((err: BusinessError) => {
                    if (err) {
                      console.error(`Failed to start the download task, Code: ${err.code}  message: ${err.message}`);
                      return;
                    }
                  });
                  task.on('progress', async (progress) => {
                    console.warn(`Request download status ${progress.state}, downloaded ${progress.processed}`);
                  });
                  task.on('completed', async () => {
                    // 该方法需用户管理任务生命周期，任务结束后调用remove释放task对象
                    request.agent.remove(task.tid);
                  });
                }).catch((err: BusinessError) => {
                  console.error(`Failed to operate a download task, Code: ${err.code}, message: ${err.message}`);
                });
              } catch (err) {
                console.error(`Failed to create a download task, err: ${err}`);
              }
            }
          })
        }
        .width('100%')
        .alignItems(HorizontalAlign.Center)
      }
    }
  }
  ```
* 方案2：

  在从网络下载文件到本地或将已有用户文件另存为新的文件路径等场景下，需要使用FilePicker提供的保存用户文件的能力。

  详情请参考[保存文档类文件](../harmonyos-guides/save-user-file.md#保存文档类文件)。
