---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/content-embed-faq
title: Content Embed Kit常见问题
breadcrumb: 指南 > 应用框架 > Content Embed Kit（内容嵌入服务） > Content Embed Kit常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:56+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:a709804c050dbed3cd2c516e7f59592a2e6447d0003b98e4aeef8cbf5ed39b0e
---

## 如何根据需求选择链接或嵌入模式来创建OE文档

客户端开发者在调用[OH\_ContentEmbed\_CreateDocumentByFile](../harmonyos-references/capi-content-embed-document-h.md#oh_contentembed_createdocumentbyfile)创建OE文档时，可根据是否需要同步源文件变更来设置isLinking参数。

* 当isLinking为true时，表示以链接方式创建OE文档。当服务端编辑OE文档时，源文件也会被修改。如果源文件被移动、删除或者重命名时，OE文档启动编辑会失败，如果用户在文件管理器中恢复原始源文件需要应用进行授权。同时链接方式不支持链接到客户端应用的沙箱目录。
* 当isLinking为false时，表示以嵌入方式创建OE文档。当客户端请求服务端编辑OE文档时，会先拷贝一份临时文件到客户端应用沙箱目录。服务端对OE文档修改时，不会修改源文件。当客户端正常退出时会清空创建的临时文件。

## 客户端基于文件创建OE文档时如何显示文档快照或应用图标

客户端基于[OH\_ContentEmbed\_CreateDocumentByFile](../harmonyos-references/capi-content-embed-document-h.md#oh_contentembed_createdocumentbyfile)创建文档时，客户端需要通过[OH\_ContentEmbed\_Proxy\_GetCapability](../harmonyos-references/capi-content-embed-proxy-h.md#oh_contentembed_proxy_getcapability)查询OE Extension是否支持获取快照。

* 如果服务端不支持快照时，客户端可以通过[getFileIconSync](../harmonyos-references/filemanagerservice-arkts-filemanagerservice.md#filemanagerservicegetfileiconsync)根据文件类型获取文件图标。
* 如果服务端支持获取快照时，客户端可以通过[OH\_ContentEmbed\_Proxy\_GetSnapshot](../harmonyos-references/capi-content-embed-proxy-h.md#oh_contentembed_proxy_getsnapshot)获取快照信息。
