---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-9
title: 自定义界面扫码黑屏现象
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码黑屏现象
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:225440b5df18fceff95fa081509253e6fe0c2add14601db598ab4d978620d346
---

**问题现象**

自定义启动相机却显示黑屏现象。

**解决措施**

* 权限校验错误码：201，没有申请相机权限，[向用户申请授权](request-user-authorization.md)。
* 参考ArkTS API错误码[1000500001](../harmonyos-references/scan-error-code.md#section1000500001-内部错误)：如首次未调用customScan.[init](../harmonyos-references/scan-customscan-api.md#customscaninit)初始化，直接调用customScan.[start](../harmonyos-references/scan-customscan-api.md#customscanstart-1)启动扫码相机流，请参考自定义界面扫码的[业务流程](scan-customscan.md#业务流程)。
