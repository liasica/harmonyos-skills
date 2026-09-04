---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-add-bookmark
title: 添加、删除书签
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 添加、删除书签
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:16+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f2241901d2cc39a92a270e1044be17d578affa55cf380559d94729ae9c43e613
---

PDF Kit支持添加和删除PDF文档书签。

添加书签时，可设置标题、颜色，是否粗体、斜体、跳转信息等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/YibrqBNQTkOFk67-ZF2M2A/zh-cn_image_0000002742124277.png)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [createBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#createbookmark)(): Bookmark | 创建PDF文档书签。 |
| [getRootBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#getrootbookmark)(): Bookmark | 获取PDF文档第一个根书签。 |
| [insertBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#insertbookmark)(bookmark: Bookmark, parent: Bookmark, position: number): boolean | 插入PDF文档书签。 |
| [setBookmarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#setbookmarkinfo)(info: BookmarkInfo): void | 设置书签信息。 |
| [removeBookmark](../harmonyos-references/pdf-arkts-pdfservice.md#removebookmark)(bookmark: Bookmark): boolean | 移除PDF文档书签。 |
| [setDestInfo](../harmonyos-references/pdf-arkts-pdfservice.md#setdestinfo)(info: DestInfo): void | 设置书签的跳转信息。 |
| [getBookmarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#getbookmarkinfo)(): BookmarkInfo | 获取书签信息。 |

## 示例代码

**添加书签**：

1. 调用loadDocument方法，加载PDF文档。
2. 调用createBookmark方法，创建书签。
3. 调用setDestInfo方法，设置书签的跳转信息。
4. 调用getBookmarkInfo方法，获取书签信息。
5. 调用setBookmarkInfo方法，设置书签内容及样式。
6. 设置保存文档沙箱路径并保存。

**删除书签**：

1. 调用loadDocument方法，加载PDF文档。
2. 调用getRootBookmark方法，获取文档的第一个根书签。
3. 调用removeBookmark方法，删除书签。
4. 设置保存文档沙箱路径并保存。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...

@Entry
@Component
struct BookmarkPage {
  private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;

  build() {
    Column() {
    // ...
        Button('addBookmark').onClick(async () => {
          // 确保在工程目录src/main/resources/resfile里有input.pdf文档
          let filePath = this.context.resourceDir + '/input.pdf';
          this.pdfDocument.loadDocument(filePath);
          // 创建书签
          let mark1: pdfService.Bookmark = this.pdfDocument.createBookmark();
          let mark2: pdfService.Bookmark = this.pdfDocument.createBookmark();
          // 设置书签的跳转信息
          let destInfo: pdfService.DestInfo = mark1.getDestInfo();
          destInfo.fitMode = pdfService.FitMode.FIT_MODE_XYZ;
          destInfo.pageIndex = 1;
          destInfo.left = 20;
          destInfo.top = 30;
          destInfo.zoom = 1.5;
          mark1.setDestInfo(destInfo);
          // 设置书签内容及样式
          let bookInfo: pdfService.BookmarkInfo = mark1.getBookmarkInfo();
          bookInfo.title = '这里是跳到第一页的书签';
          bookInfo.titleColor = 12;
          bookInfo.isBold = true;
          bookInfo.isItalic = true;
          mark1.setBookmarkInfo(bookInfo);
          // 把创建的书签插入到PDF页面
          this.pdfDocument.insertBookmark(mark1, null, 1);
          this.pdfDocument.insertBookmark(mark2, mark1, 1);
          // 设置保存文档沙箱路径并保存
          let outPdfPath = this.context.filesDir + '/testAddBookmark.pdf';
          let result = this.pdfDocument.saveDocument(outPdfPath);
          hilog.info(0x0000, 'BookmarkPage', 'saveAddBookmark %{public}s!', result ? 'success' : 'fail');
        })
        // 删除书签
        Button('removeBookmark').onClick(async () => {
          // 确保沙箱目录有testAddBookmark.pdf文档
          this.pdfDocument.loadDocument(this.context.filesDir + '/testAddBookmark.pdf');
          let bookmarks: pdfService.Bookmark = this.pdfDocument.getRootBookmark();
          if (bookmarks.isRootBookmark()) {
            let hasRemoveBookmark: boolean = this.pdfDocument.removeBookmark(bookmarks);
            hilog.info(0x0000, 'BookmarkPage', 'removeBookmark %{public}s!', hasRemoveBookmark ? 'success' : 'fail');
            let outPdfPath = this.context.filesDir + '/testRemoveBookmark.pdf';
            let result = this.pdfDocument.saveDocument(outPdfPath);
            hilog.info(0x0000, 'BookmarkPage', 'saveRemoveBookmark %{public}s!', result ? 'success' : 'fail');
          }
        })
        // ...
    }
  }
}
```
