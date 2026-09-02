---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-15
title: 从相册中选择图片添加到PDF页面中
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 从相册中选择图片添加到PDF页面中
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a224a9b0c27f4017155493a7c4b721b277415ad9fd92d502f7dba1a3248f01dc
---

## 问题现象

从相册选择的图片怎么转换成PDF文档，或者说新建一个PDF文档，怎么插入在相册选择的图片。

## 背景知识

* [使用PhotoPicker组件访问图片/视频](../harmonyos-guides/component-guidelines-photoviewpicker.md)：当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。
* [PDF Kit（PDF服务）](../harmonyos-guides/pdf-kit-guide.md)支持编辑PDF页面内容，包括：添加、删除文本、添加、删除图片、添加、修改、删除批注、通过索引指定PDF页面添加批注。

## 解决方案

* aboutToAppear回调中，确保rawfile目录下有PDF文件如input.pdf文档，拷贝到沙箱内。
* selectPhoto()通过PhotoPicker组件直接返回该图片资源，而不需要授予应用读取图片文件的权限。PhotoViewPicker选择图片保存到uri。
* getFilePath()使用基础文件fs.openSync接口，通过uri打开这个文件得到fd，复制到沙箱中，获取沙箱路径。
* 确保沙箱目录已有如input.pdf文档调用loadDocument方法，加载PDF文档。在【addImage】按钮中调用addImageObject的方法添加沙箱路径中上述步骤选择的相册图片。
* 添加图片后保存PDF到沙箱路径中。可在IDE中查看通过View -> Tool Windows -> Device File Browser打开，Device File Browser对应沙箱目录如下：“/data/app/el2/100/base/com.example.myapplication/haps/entry/files/testAddImage.pdf”。

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { promptAction } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PhotoPickerComponentDemo {
  // 缓存选择的图片uri
  uri: Array<string> = [];
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  async aboutToAppear(): Promise<void> {
    try {
      //确保rawfile目录下有pdf文件
      await this.copyRawFileToSdcard(this.context, 'input.pdf');
      promptAction.openToast({ message: '全部拷贝完成' });
    } catch (error) {
      promptAction.openToast({ message: '文件拷贝失败' });
    }
  }

  private copyRawFileToSdcard(context: common.Context, pdfName: string): Promise<void> {
    return new Promise((resolve) => {
      let destRoot = context.filesDir;
      // rawfile下的文件名
      let srcFileName = pdfName;
      let destFilePath = `${destRoot}/${srcFileName}`;
      context.resourceManager.getRawFileContent(srcFileName, (error: BusinessError, data: Uint8Array) => {
        if (error) {
          promptAction.openToast({ message: '拷贝失败' });
          console.error(`error.code is ${error.code},error.message is ${error.message},`);
          return;
        }
        let fileStream = fileIo.createStreamSync(destFilePath, 'w+');
        fileStream.writeSync(data.buffer);
        fileStream.close();
        promptAction.openToast({ message: '拷贝成功' });
        resolve();
      });
    });
  }

  selectPhoto() {
    try {
      let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      photoSelectOptions.maxSelectNumber = 5;
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(photoSelectOptions).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
        // select方法：在选择图片点击完成之后，PhotoSelectResult.photoUris返回选中的uri
        this.uri = PhotoSelectResult.photoUris;
        console.info(`PhotoViewPicker.select successfully, PhotoSelectResult uri: ${JSON.stringify(PhotoSelectResult)}`);
      }).catch((err: BusinessError) => {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
    }
  }

  // 使用fs.openSync接口，通过uri打开这个文件得到fd，拷贝到新路径
  getFilePath(uri: string): string {
    let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
    const dateStr = (new Date().getTime()).toString();
    // 临时文件目录
    let newPath = this.context.filesDir + `/${dateStr + file.name}`;
    // 转化路径
    fileIo.copyFileSync(file.fd, newPath);
    // 沙箱路径
    let realUri = newPath;
    console.info(`newPath is : ${realUri}`);
    return realUri;
  }

  build() {
    Column() {
      Button('select').onClick(() => {
        this.selectPhoto();
      })
      // 添加图片
      Button('addImage').onClick(async () => {
        // 确保沙箱目录有input.pdf文档
        let filePath = this.context.filesDir + '/input.pdf';
        let loadResult = this.pdfDocument.loadDocument(filePath, '');
        if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
          let page: pdfService.PdfPage = this.pdfDocument.getPage(0);
          console.info(`click info>>`);
          console.info(`file path info>> ${this.getFilePath(this.uri[0])}`);
          // 插入图片，沙箱目录已有选择后的图片
          page.addImageObject(this.getFilePath(this.uri[0]), 100, 100, 100, 120);
          let outPdfPath = this.context.filesDir + '/testAddImage.pdf';
          console.info(`outPdfPath info>>${outPdfPath}`);
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'addImage %{public}s!', result ? 'success' : 'fail');
        }
      })
    }

  }
}
```
