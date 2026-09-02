---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-7
title: 如何将HAR（静态共享包）转为HSP（动态共享包）
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何将HAR（静态共享包）转为HSP（动态共享包）
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4d00680ebeb02173e2761d6efad288330d62cc38e57cf48d7ab10c73b818af09
---

[HAR](../harmonyos-guides/har-package.md)转换成[HSP](../harmonyos-guides/in-app-hsp.md)可参考如下步骤：

1. 新建一个HSP，将HAR包拷贝到lib目录，并在HSP的oh-package.json5文件的dependencies下配置HAR包。

   ```json
   "dependencies": {
     "myhar": "file:./lib/myHar.har" // MyHar.Har path: oh-package.json5 file in the same directory as the lib folder
   },
   ```
2. 在HSP的Index.ets中直接导出HAR内容。

   ```typescript
   export * as myhar from 'myhar';
   ```
3. 最后编译该HSP。
