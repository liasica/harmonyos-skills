---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-13
title: 如何合并多个PDF以及给PDF添加页码
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 如何合并多个PDF以及给PDF添加页码
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:24+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7477fbc32c69747e1094c259511a03340b3f4c8bed8beb40beeeb355153d353c
---

## 问题现象

HarmonyOS Next有没有提供将多个pdf合并成一个pdf以及给pdf添加页码的API。

## 背景知识

[insertPageFromDocument](../harmonyos-references/pdf-arkts-pdfservice.md#insertpagefromdocument)接口提供能力，将其他Document的Page添加到当前Document，Page中的批注不支持插入到当前Document。

参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| document | [PdfDocument](../harmonyos-references/pdf-arkts-pdfservice.md#pdfdocument) | 是 | PdfDocument对象。 |
| fromIndex | number | 是 | 从其他文档第几页开始添加，大于等于0，0为起始页。 |
| pageCount | number | 是 | 添加页数量，大于0，小于等于总页数。 |
| index | number | 是 | 从当前文档第几页开始添加，大于等于0，小于总页数，0为起始页。 |

[addHeaderFooter](../harmonyos-references/pdf-arkts-pdfservice.md#addheaderfooter)接口提供能力，插入pdf文档页眉页脚。该方法属于耗时业务，需要遍历每一页去添加页眉页脚，添加页面较多时建议放到线程里去处理。

参数说明：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [HeaderFooterInfo](../harmonyos-references/pdf-arkts-pdfservice.md#headerfooterinfo) | 是 | 页眉页脚的信息。 |
| startIndex | number | 是 | 起始页，必须大于等于0，0为起始页。 |
| endIndex | number | 是 | 结束页，小于总页数。 |
| oddPages | boolean | 是 | 奇数页是否添加，true表示是，false表示否。 |
| evenPages | boolean | 是 | 偶数页是否添加，true表示是，false表示否。 |

## 解决方案

1. aboutToAppear回调中，确保rawfile目录下有pdf文件，拷贝到沙箱内。
2. 使用[insertPageFromDocument](../harmonyos-references/pdf-arkts-pdfservice.md#insertpagefromdocument)接口将input\_add.pdf文档页插入到input\_src.pdf末尾的位置，并另存文档。
3. 给生成的testInsertPageFromDocument.pdf文档添加页码。

完整示例代码如下：

```ts
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { Font } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct PdfPage {
  @State lastPage: number = 0;
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  async aboutToAppear(): Promise<void> {
    try {
      //确保rawfile目录下有pdf文件
      await this.copyRawFileToSdcard(this.context, 'input_src.pdf');
      await this.copyRawFileToSdcard(this.context, 'input_add.pdf');
      promptAction.openToast({ message: '全部拷贝完成' });
    } catch (error) {
      promptAction.openToast({ message: '文件拷贝失败' });
    }
  }

  build() {
    Column() {
      // 将input_add.pdf文档页插入到input_src.pdf末尾的位置，并另存文档
      Button('insertPageFromDocument').onClick(async () => {
        let filePath = this.context.filesDir + '/input_src.pdf';
        let loadResult: pdfService.ParseResult = this.pdfDocument.loadDocument(filePath);
        if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
          this.lastPage = this.pdfDocument.getPageCount();
        } else {
          promptAction.openToast({ message: '加载失败' });
        }
        let pdfDoc: pdfService.PdfDocument = new pdfService.PdfDocument();
        // 确保该沙箱目录下有input_add.pdf文档
        let res = pdfDoc.loadDocument(this.context.filesDir + '/input_add.pdf');
        if (res === pdfService.ParseResult.PARSE_SUCCESS) {
          this.pdfDocument.insertPageFromDocument(pdfDoc, 0, pdfDoc.getPageCount(), this.lastPage);
          let outPdfPath = this.context.filesDir + '/testInsertPageFromDocument.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          this.lastPage = this.pdfDocument.getPageCount();
          hilog.info(0x0000, 'PdfPage', 'insertPageFromDocument %{public}s!', result ? 'success' : 'fail');
        } else {
          promptAction.openToast({ message: '加载失败' });
        }
        pdfDoc.releaseDocument();
      })

      Button('addHeaderFooter').onClick(async () => {
        // 确保沙箱目录有testInsertPageFromDocument.pdf文档
        let filePath = this.context.filesDir + '/testInsertPageFromDocument.pdf';
        let res = this.pdfDocument.loadDocument(filePath);
        if (res === pdfService.ParseResult.PARSE_SUCCESS) {
          let hfInfo: pdfService.HeaderFooterInfo = new pdfService.HeaderFooterInfo();
          hfInfo.fontInfo = new pdfService.FontInfo();
          // 确保字体路径存在
          let font: Font = new Font();
          hfInfo.fontInfo.fontPath = font.getFontByName('HarmonyOS Sans')?.path;
          // 如果不知道字体的具体名称，可以为空字符串
          hfInfo.fontInfo.fontName = '';
          hfInfo.textSize = 10;
          hfInfo.charset = pdfService.CharsetType.PDF_FONT_DEFAULT_CHARSET;
          hfInfo.underline = false;
          hfInfo.textColor = 0x00000000;
          hfInfo.leftMargin = 1.0;
          hfInfo.topMargin = 40.0;
          hfInfo.rightMargin = 1.0;
          hfInfo.bottomMargin = 40.0;
          let pdfPageCount = this.pdfDocument.getPageCount();
          for (let index = 0; index < pdfPageCount; index++) {
            hfInfo.footerCenterText = `${index + 1}`;
            this.pdfDocument.addHeaderFooter(hfInfo, index, index, true, true);
          }
          let outPdfPath = this.context.filesDir + '/testAddHeaderFooter.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'PdfPage', 'addHeaderFooter %{public}s!', result ? 'success' : 'fail');
        } else {
          promptAction.openToast({ message: '加载失败' });
        }
        this.pdfDocument.releaseDocument();
      })
    }
  }

  // 拷贝pdf文件到应用沙箱目录
  private copyRawFileToSdcard(context: common.Context, pdfName: string): Promise<void> {
    return new Promise((resolve) => {
      let destRoot = context.filesDir;
      // rawfile下的文件名
      let srcFileName = pdfName;
      let destFilePath = `${destRoot}/${srcFileName}`;
      context.resourceManager.getRawFileContent(srcFileName, (error: BusinessError, data: Uint8Array) => {
        if (error) {
          promptAction.openToast({ message: '拷贝失败' });
          hilog.error(0x0000, 'PdfCopy', `Copy failed: ${error.code}`);
          return;
        }
        const fileStream = fs.createStreamSync(destFilePath, 'w+');
        fileStream.writeSync(data.buffer);
        fileStream.close();
        promptAction.openToast({ message: '拷贝成功' });
        resolve();
      });
    });
  }
}
```

**说明** 

* 示例代码中input\_src、input\_add文件需要提前放在项目rawfile目录下，路径：项目/entry/src/main/resources/rawfile。
* 先点击insertPageFromDocument按钮将pdf文件合并。
* 再点击addHeaderFooter按钮给合并后的pdf文件添加页脚页码。
* IDE打开Device File Browser，查看保存的pdf文件，路径如下：应用包名/data/storage/el2/base/haps/entry/files，具体参考[访问设备文件](../harmonyos-guides/ide-device-file-explorer.md)。
