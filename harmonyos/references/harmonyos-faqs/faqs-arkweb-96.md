---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-96
title: Web加载失败时的白屏页面如何改为自定义错误页
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web加载失败时的白屏页面如何改为自定义错误页
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed0bc9c493c836803db1c69f760d33e7f0533cd66da0558a48e6912df9373b4f
---

**问题场景：**

在网络条件较差或链接资源有问题时，Web组件加载失败会出现白屏状态，这种场景下用户无法感知页面加载状态，导致体验较差，需要将白屏替换为自定义错误页面的方案。

**解决措施：**

应用可以监听页面加载异常的相关事件如[onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)、[onHttpErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onhttperrorreceive)和[onSslErrorEventReceive](../harmonyos-references/arkts-basic-components-web-events.md#onsslerroreventreceive9)等，在对应的回调中按需实现业务逻辑，如使用[loadurl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)加载自定义错误页；本文以[onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)为例对主资源报错的场景进行处理，加载本地错误页面资源文件。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Stack() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onErrorReceive((event) => {
13. // Only handle loading errors of the main framework to avoid duplicate processing of errors in sub-resources
14. if (event && event.request.isMainFrame()) {
15. try {
16. // 加载自定义错误页面
17. this.controller.loadUrl($rawfile('custom_failure_page.html'));
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
20. }
21. }
22. })
23. }
24. }
25. }
```

[CustomFailurePage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/CustomFailurePage.ets#L21-L45)
