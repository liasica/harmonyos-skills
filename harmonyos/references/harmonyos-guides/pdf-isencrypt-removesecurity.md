---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-isencrypt-removesecurity
title: 判断PDF文档是否加密及删除加密
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 判断PDF文档是否加密及删除加密
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b27bd1c11afccaeae98277d2a916c1a1e6f47d48efb8ca120abccaca542bb180
---

PDF Kit支持判断PDF文档是否加密及删除PDF加密锁。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [isEncrypted](../harmonyos-references/pdf-arkts-pdfservice.md#isencrypted)(path: string): boolean | 判断当前文档是否已加密。 |
| [removeSecurity](../harmonyos-references/pdf-arkts-pdfservice.md#removesecurity)(): boolean | 删除文档加密锁。 |

## 示例代码

1. 调用isEncrypted方法，判断PDF文档是否加密。
2. 如果是加密PDF文档，调用removeSecurity方法移除PDF文档的加密锁。

```typescript
import { pdfService } from '@kit.PDFKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...

@Entry
@Component
struct SecurityPage {
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;
  private password: string = '123456';

  aboutToAppear(): void {
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      let doc = new pdfService.PdfDocument();
      this.loadResult = await doc.loadDocument(filePath);
      doc.releaseDocument();
    })()
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column({ space: 10 }) {
        // ...
        Row({ space: 10 }) {
          Button('isEncryptedAndRemoveSecurity')
            .onClick(() => {
              if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
                let inputPath = this.context.resourceDir + '/input.pdf';
                let tmpPath = this.context.filesDir + '/tmp.pdf';
                let tmp1Path = this.context.filesDir + '/tmp1.pdf';
                let doc = new pdfService.PdfDocument();
                // 加载原始PDF文档
                doc.loadDocument(inputPath);
                // 设置密码，对文档进行加密
                doc.setPdfPassword(this.password);
                // 保存加密后的文档到tmp.pdf
                doc.saveDocument(tmpPath);
                // 检查tmp.pdf是否加密
                let isTmpEncrypted = doc.isEncrypted(tmpPath);
                hilog.info(0x0000, 'testTag', 'isTmpEncrypted: %{public}s', isTmpEncrypted.toString());
                doc.releaseDocument();
                // 加载加密的tmp.pdf
                doc.loadDocument(tmpPath, this.password);
                // 移除密码
                doc.removeSecurity();
                // 保存无密码的文档到tmp1.pdf
                doc.saveDocument(tmp1Path);
                // 检查tmp1.pdf是否已移除密码
                let isTmp1Encrypted = doc.isEncrypted(tmp1Path);
                hilog.info(0x0000, 'testTag', 'isTmp1Encrypted: %{public}s', isTmp1Encrypted.toString());
              }
            })
        }
      }
      .alignItems(HorizontalAlign.Start)
      .padding(10)
    }
    .width('100%').height('100%')
  }
}
```
