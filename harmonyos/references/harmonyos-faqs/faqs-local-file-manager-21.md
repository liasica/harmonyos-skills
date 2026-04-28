---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-21
title: 通过fileIo.openSync获得的fd，传递到C侧调close后，ArkTS侧fileIo.closeSync是不是不用调了
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 通过fileIo.openSync获得的fd，传递到C侧调close后，ArkTS侧fileIo.closeSync是不是不用调了
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:26+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:cb7fbf65b5f25ca14d42848f3f13f6709bba611589091d3a12a9163e95fd09ad
---

需要调用ArkTS侧的fileIo.openSync方法获取文件描述符（fd），并将该fd传递给C侧。C侧使用完fd后需要单独调用close关闭。同时，ArkTS侧在使用完文件对象后，仍需调用fileIo.closeSync关闭文件。由于跨语言边界传递的文件描述符需要双方各自管理资源，建议在关闭后设置null值避免重复操作。
