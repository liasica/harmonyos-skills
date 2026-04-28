---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-isencrypt-removesecurity
title: 判断PDF文档是否加密及删除加密
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > pdfService能力 > 判断PDF文档是否加密及删除加密
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46c56461d0c53d1c4765527b2a946b99d9dddd880b38218965b57adb92a3e5bd
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

```
1. import { pdfService } from '@kit.PDFKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct PdfPage {
7. private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
8. private context = this.getUIContext().getHostContext() as Context;

10. build() {
11. Column() {
12. // 判断文档是否加密，并删除加密
13. Button('isEncryptedAndRemoveSecurity').onClick(async () => {
14. // 确保沙箱目录有input.pdf文档
15. let filePath = this.context.filesDir + '/input.pdf';
16. let isEncrypt = this.pdfDocument.isEncrypted(filePath);
17. if (isEncrypt) {
18. let hasRemoveEncrypt = this.pdfDocument.removeSecurity();
19. hilog.info(0x0000, 'PdfPage', 'isEncryptedAndRemoveSecurity %{public}s!',
20. hasRemoveEncrypt ? 'success' : 'fail');
21. }
22. })
23. }
24. }
25. }
```
