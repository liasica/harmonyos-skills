---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-9
title: 自定义界面扫码黑屏现象
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 自定义界面扫码黑屏现象
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:a4e237d0eaaf659b4c3da99d62088c9a49563aac40bb6a65865155afed3728ce
---

**问题现象**

自定义界面扫码启动相机却显示黑屏现象。

**解决措施**

* 权限校验错误码：201，没有申请相机权限，[向用户申请授权](request-user-authorization.md)。
* 参考ArkTS API错误码[1000500001](../harmonyos-references/errorcode-scan.md#section1000500001-内部错误)：如首次未调用[init](../harmonyos-references/scan-customscan-api.md#init)初始化，直接调用[start](../harmonyos-references/scan-customscan-api.md#start)启动扫码相机流，请参考自定义界面扫码的[业务流程](scan-customscan.md#业务流程)。
