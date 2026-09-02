---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-search
title: 搜索关键字
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PdfView预览组件 > 搜索关键字
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8e4a9c336809d3a90a3ada88cd3e3ca8932002b9ac56b1819ad781574594c9fc
---

预览PDF文档时，可以对页面的关键词（英文字符不区分大小写）进行搜索并高亮显示，同时使用[setSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setsearchindex)方法高亮显示指定的搜索结果。

使用[getSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getsearchindex)方法获取当前高亮的索引，可以使用[clearSearch](../harmonyos-references/pdf-arkts-pdfviewmanage.md#clearsearch)方法清除所有搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/dPcjeI4rSGO0dtIGytoLPw/zh-cn_image_0000002706835128.png)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [searchKey](../harmonyos-references/pdf-arkts-pdfviewmanage.md#searchkey)(text: string, listener: Callback<number>): void | 搜索文本并返回匹配的总数。 |
| [clearSearch](../harmonyos-references/pdf-arkts-pdfviewmanage.md#clearsearch)(): void | 清除搜索文本的高亮，等价于搜索空字符串 。 |
| [setSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setsearchindex)(index: number): void | 设置搜索匹配结果的索引，页面会跳转到索引对应搜索结果处。 |
| [getSearchIndex](../harmonyos-references/pdf-arkts-pdfviewmanage.md#getsearchindex)(): number | 获取当前命中搜索关键字匹配结果的索引，执行搜索接口后默认命中索引为0。 |

## 示例代码

1. 先加载PDF文档。
2. 调用PdfView预览组件，渲染显示。
3. 在按钮【searchKey】里，调用searchKey方法，搜索指定关键字。
4. 上一个、下一个搜索按钮跳转到对应的结果。
5. 在按钮【getSearchIndex】里，调用getSearchIndex方法，获取当前的搜索结果索引。
6. 在按钮【clearSearch】里，调用clearSearch方法，清除搜索结果。

```typescript
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SearchPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;
  private searchIndex = 0;
  private charCount = 0;

  aboutToAppear(): void {
    let dir: string = this.context.resourceDir;
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath: string = dir + '/input.pdf';
    try {
      let res = fileIo.accessSync(filePath);
      if (!res) {
        let content: Uint8Array = this.context.resourceManager.getRawFileContentSync('resfile/input.pdf');
        let fdSand = fileIo.openSync(
            filePath,
            fileIo.OpenMode.WRITE_ONLY |
            fileIo.OpenMode.CREATE |
            fileIo.OpenMode.TRUNC
        );
        fileIo.writeSync(fdSand.fd, content.buffer);
        fileIo.closeSync(fdSand.fd);
      }
    } catch (e) {
      let error: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'SearchPage', `Code: ${error.code}, message: ${error.message} `);
    }
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {

      Column() {
        Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.Start }) {
          Button('searchKey').onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              this.controller.searchKey('PDF', (index: number) => {
                this.charCount = index;
                hilog.info(0x0000, 'SearchPage', 'searchKey %{public}s!', index + '');
              })
            }
          })
            .flexShrink(0)
          Button('setSearchPrevIndex').onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              if (this.searchIndex > 0) {
                this.controller.setSearchIndex(--this.searchIndex);
              }
            }
          })
            .flexShrink(0)
          Button('setSearchNextIndex').onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              if (this.searchIndex < this.charCount) {
                this.controller.setSearchIndex(++this.searchIndex);
              }
            }
          })
            .flexShrink(0)
          Button('getSearchIndex').onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              let curSearchIndex = this.controller.getSearchIndex();
              hilog.info(0x0000, 'SearchPage', 'curSearchIndex %{public}s!', curSearchIndex + '');
            }
          })
            .flexShrink(0)
          Button('clearSearch').onClick(async () => {
            if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
              this.controller.clearSearch();
            }
          })
            .flexShrink(0)
        }
        .margin({ top: 50, bottom: 10 })
        .padding({ left: 10, right: 10 })
        PdfView({
          controller: this.controller,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1);
      }
      // ...
    }
    .width('100%').height('100%')
  }
}
```
