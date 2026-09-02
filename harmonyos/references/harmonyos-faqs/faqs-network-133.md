---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-133
title: 下载文件时，下载代理提示已下载完成，并且有实际下载内容，但是保存文件时为空
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 下载文件时，下载代理提示已下载完成，并且有实际下载内容，但是保存文件时为空
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:890bd238ac66b8061010e822f323351204b3fa16fee2cccd7e5e7e92aecabb44
---

## 问题现象

应用需要提供文件（如PDF、图片）的下载和预览功能，并允许用户将文件保存到手机的公共目录（如下载、文档等）。在开发过程中，发现无法通过代码直接将网络文件下载并写入到应用的沙箱之外的公共目录。

## 背景知识

* 应用支持将文件上传到网络服务器，也支持从网络服务器下载资源文件到本地目录。开发者可以使用ohos.request的request.agent接口[下载网络资源文件至用户文件](../harmonyos-guides/app-file-upload-download.md#下载网络资源文件至用户文件)指定目录。
* 访问和管理应用文件，对于每个应用，系统会在内部存储空间映射出一个专属的“应用沙箱目录”，[应用沙箱](../harmonyos-guides/app-sandbox-directory.md)提供了一个完全隔离的环境，使用户可以安全地访问应用文件。

## 问题定位

这是HarmonyOS出于安全和隐私保护考虑而设计的沙箱隔离机制。应用默认只对其私有的沙箱目录拥有完全的读写权限，对公共目录的直接写入受到严格限制，以防止恶意应用滥用存储空间。试图直接使用文件API向公共目录写入路径是违反平台安全模型的，必然会导致权限不足、文件为空等的错误。

## 分析结论

* 使用应用沙箱机制安全下载文件并与应用内预览。
* 通过用户授权，使用公共目录保存下载的文件。

## 修改建议

* 使用request.agent.create等网络请求工具，将目标文件安全地下载到应用的私有沙箱目录中。这个过程完全在应用内部进行，无需特殊权限。下载完成后，获取文件在沙箱内的访问路径。然后利用HarmonyOS UI组件（如PdfView用于PDF，Image用于图片）加载并展示该文件。
* 在预览界面，提供一个“保存到手机”的按钮。用户点击该按钮时，我们调用picker.DocumentViewPicker这个API拉起系统文件浏览器界面，让用户亲自选择希望将文件保存到公共目录的哪个具体位置（如“下载”文件夹）。
* 用户做出选择后，系统会通过回调将一个代表目标位置的可写URI返回给我们的应用。此时，应用就获得了对这个特定位置的临时写入授权。
* 最后，我们通过save等文件操作方法，将之前下载在沙箱中的文件，复制或移动到用户通过Picker选择的公共目录位置。

```ts
import { BusinessError, request, systemDateTime } from '@kit.BasicServicesKit';
import { fileIo as fs, picker } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct RingAnimationExample {
  build() {
    Column() {
      Button('点击下载')
        .onClick(() => {
          // 此处地址实际使用过程中替换为真实pdf文件下载地址
          let url: string = '';
          let time = systemDateTime.getTime();
          //文件名称、文件所在的沙箱路径
          let fileName: string = 'PDF' + time + '文件';
          let fileExtension: string = 'pdf'; // 文件后缀名
          let uiContext = this.getUIContext();
          let context = uiContext.getHostContext() as common.UIAbilityContext;
          let cacheDir = context.cacheDir;
          let savePath: string = cacheDir + '/' + fileName;

          let options: DownloadOptions = {
            url: url, // 文件的网络下载地址
            fileName: fileName, // 在本地保存的文件名
            fileExtension: fileExtension, // 文件后缀名
            savePath: savePath, // 文件的沙箱路径
            context: context, // 应用上下文，用于获取文件存储路径
            onProgress: (progress: request.agent.Progress) => {
              console.log(`下载进度：${progress.processed}`);
            }
          };
          downloadFileToPublicDownloads(options, uiContext);
        })
        .margin({
          top: 30
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
/**
 * 下载文件的参数接口
 */
export interface DownloadOptions {
  url: string // 文件的网络下载地址
  fileName: string // 在本地保存的文件名
  fileExtension: string // 文件后缀名
  savePath: string, // 文件的沙箱路径
  context: Context // 应用上下文，用于获取文件存储路径
  onProgress: (progress: request.agent.Progress) => void // 可选的进度回调
}

/**
 * 下载文件到用户公共目录。
 * @param options
 * @returns void
 */
export function downloadFileToPublicDownloads(options: DownloadOptions, uiContext: UIContext) {
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = [`${options.fileName}.${options.fileExtension}`];
    let documentPicker = new picker.DocumentViewPicker(options.context);
    let uri: string = '';
    documentPicker.save(documentSaveOptions).then(async (documentSaveResult: Array<string>) => {
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' +
      JSON.stringify(documentSaveResult));
      uri = documentSaveResult[0];
      await downloadFile(options, uiContext, uri);
    }).catch((err: BusinessError) => {
      console.error('DocumentViewPicker.save failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('[picker] photoViewPickerSave error = ' + JSON.stringify(err));
  }
}

/**
 * 下载文件到沙箱目录。
 * @param uri 下载地址
 * @param options
 * @param uri(可选，用于下载文件到公共目录)
 * @returns void
 */
export function downloadFile(options: DownloadOptions, uiContext: UIContext, uri?: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const config: request.agent.Config = {
      action: request.agent.Action.DOWNLOAD,
      url: options.url,
      saveas: options.savePath,
      gauge: true,
      overwrite: true, // 覆盖已存在的文件
      mode: request.agent.Mode.FOREGROUND,
    };

    request.agent.create(options.context, config).then((task: request.agent.Task) => {
      // 监听progress事件
      if (options.onProgress) {
        task.on('progress', options.onProgress);
      }

      // 监听completed事件
      task.on('completed', () => {
        console.info(`下载成功: ${options.savePath}`);
        request.agent.remove(task.tid); // 移除任务
        if (uri) {
          writeFileToPublic(options, uiContext, uri);
        }
        resolve(options.savePath); // 成功时，返回文件路径
      });
      // 监听failed事件
      task.on('failed', (progress) => {
        const err = new Error(`下载失败: ${JSON.stringify(progress)}`);
        console.error(err.message);
        request.agent.remove(task.tid);
        reject(err); // 失败时，拒绝Promise
      });
      // 监听start事件
      task.start((err: BusinessError) => {
        if (err) {
          const startErr = new Error(`启动下载任务失败, Code: ${err.code}, message: ${err.message}`);
          console.error(startErr.message);
          reject(startErr);
        }
      });
    }).catch((err: BusinessError) => {
      const createErr = new Error(`创建下载任务失败, Code: ${err.code}, message: ${err.message}`);
      console.error(createErr.message);
      reject(createErr);
    });
  });
}

export async function writeFileToPublic(options: DownloadOptions, uiContext: UIContext, uri: string): Promise<void> {
  let sourceFile: fs.File | null = null;
  let destFile: fs.File | null = null;
  try {
    sourceFile = await fs.open(options.savePath, fs.OpenMode.READ_ONLY);
    const stat = await fs.stat(sourceFile.fd);
    let arrayBuffer = new ArrayBuffer(stat.size);
    const readLen = await fs.read(sourceFile.fd, arrayBuffer);
    console.info('成功读取文件数据');
    let buf = buffer.from(arrayBuffer, 0, readLen).buffer;
    destFile = await fs.open(uri, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
    await fs.write(destFile.fd, buf);
    console.info(`成功将内容写入文件: ${uri}`);
    uiContext.getPromptAction().showToast({
      message: '成功将内容写入文件'
    });
  } catch (err) {
    const businessErr = err as BusinessError;
    console.error(`文件操作失败, 错误码: ${businessErr.code}, 信息: ${businessErr.message}`);
    uiContext.getPromptAction().showToast({
      message: '文件操作失败'
    });
  } finally {
    if (sourceFile) {
      await fs.close(sourceFile);
      console.info('源文件已关闭');
    }
    if (destFile) {
      await fs.close(destFile);
      console.info('目标文件已关闭');
    }
  }
}
```
