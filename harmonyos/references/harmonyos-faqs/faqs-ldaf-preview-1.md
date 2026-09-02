---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ldaf-preview-1
title: 在线视频下载后默认打开的是文件预览器
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 文件预览（Preview） > 在线视频下载后默认打开的是文件预览器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:47a76a6dececbf52e95dbde4db9e4df1fce1d95904a72bb4751fc7bddf804e7c
---

## 问题现象

应用内视频点击下载按钮后，默认跳转系统的文件预览，无法查看下载后的视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Q3ZmLluWQbmGRI1drb9OjQ/zh-cn_image_0000002659138381.png "点击放大")

## 背景知识

[Preview Kit（文件预览服务）](../harmonyos-guides/preview-introduction.md)为应用提供便捷的文件快速预览和文件打开加速能力，文件预览支持图片、视频、音频、文本、html进行查看，具体类型可参考[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。

## 问题定位

日志全局搜索关键字“FilePreview”，查看发起文件预览时传入的mimeType类型参数：

```screen
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: openPreview
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: system startup time is: 460103097
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: the value read from the system parameter is 2
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: openPreviewPhone
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: isApkFile, mimetype is application/msword, extName is .mp4
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: calling bundlename is com.example.test
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: openPreview promise
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: addEventProcessor
A0FF01/com.exa...p/FilePreview  com.example.test      I     FilePreview: system startup time is: 460103122
```

## 分析结论

发起文件预览时传入的参数mimeType类型为“application/msword”，该类型对应的是Office文档，导致文件预览器使用doc文档类型预览该视频文件。

## 修改建议

发起文件预览时传入的mimeType类型参数需与待预览文件类型相匹配，如MP4视频需要传入“video/mp4”。示例代码如下：

```screen
import { filePreview } from '@kit.PreviewKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, fileUri, picker } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  promptAction = this.getUIContext().getPromptAction();
  @State uri: string = '';

  build() {
    Column({ space: 20 }) {
      Button('拷贝公共目录视频到沙箱')
        .type(ButtonType.ROUNDED_RECTANGLE)
        .onClick(() => {
          try {
            const documentSelectOptions = new picker.DocumentSelectOptions();
            // 选择文档的最大数目（可选）。
            documentSelectOptions.maxSelectNumber = 1;
            // 选择文件的后缀类型['后缀类型描述|后缀类型']（可选，不传该参数，默认不过滤，即显示所有文件），若选择项存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔（可选），后缀类型名不能超过100。此外2in1设备支持通配符方式['所有文件(*.*)|.*']（说明：从API version 17开始，手机支持该配置），表示为显示所有文件。
            documentSelectOptions.fileSuffixFilters = ['视频|.mp4'];
            // 创建文件选择器实例
            const documentViewPicker = new picker.DocumentViewPicker(this.context);
            documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
              //文件选择成功后，返回被选中文档的URI结果集。
              let uri = documentSelectResult[0];
              let path = this.context.filesDir + '/test.mp4';
              let srcFile = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              fileIo.copyFileSync(srcFile.fd, file.fd);
              fileIo.close(srcFile.fd);
              fileIo.close(file.fd);
              this.uri = fileUri.getUriFromPath(path);
              console.info('documentViewPicker.select to file succeed and uris are:' + this.uri);
            }).catch((err: BusinessError) => {
              console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
              this.promptAction.showToast({
                message: '拷贝失败',
                duration: 2000
              });
            });
          } catch (err) {
            console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
            this.promptAction.showToast({
              message: '拷贝失败',
              duration: 2000
            });
          }
        });

      Button('预览视频')
        .type(ButtonType.ROUNDED_RECTANGLE)
        .onClick(() => {
          let fileUri: string = this.uri; // 此处实际需替换为视频的本地沙箱路径
          filePreview.canPreview(this.context, fileUri).then((result) => { // 传入支持的文件类型且项目存在时会返回true
            console.info(`Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
            let fileInfo: filePreview.PreviewInfo = {
              title: 'test.mp4',
              uri: fileUri,
              mimeType: 'video/mp4' // mimeType需与实际需要预览的文件类型匹配
            };
            filePreview.openPreview(this.context, fileInfo).then(() => {
              console.info('Succeeded in opening preview');
            }).catch((err: BusinessError) => {
              console.error(`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
              this.promptAction.showToast({
                message: '预览失败',
                duration: 2000
              });
            });
          }).catch((err: BusinessError) => {
            console.error(`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
            this.promptAction.showToast({
              message: '预览失败',
              duration: 2000
            });
          });
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
