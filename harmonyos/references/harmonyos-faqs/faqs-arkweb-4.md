---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-4
title: onInterceptRequest拦截URL并自定义HTML文件，页面加载失败
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > onInterceptRequest拦截URL并自定义HTML文件，页面加载失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:644e520bbed9d941bd205705bc11911f95fe2c592d626ebec4abd3bd2b531864
---

**问题现象**

当使用onInterceptRequest拦截页面Web的src链接后返回自定义HTML时，如果自定义HTML文件中的script标签内容未加载，需要检查脚本路径和加载方式。

**解决措施**

设置拦截器时，需要同时设置setResponseEncoding、setResponseMimeType和setResponseHeader等参数，仅设置setResponseData内核将无法识别这是HTML文件。参考代码如下：

```
1. Web({ src: 'www.example.com',controller: this.controller })
2. .onInterceptRequest((event) => {
3. console.log('url:' + event.request.getRequestUrl())
4. this.responseWeb = new WebResourceResponse();
5. let head1: Header = {
6. headerKey: "Connection",
7. headerValue: "keep-alive"
8. }
9. let length = this.heads.push(head1)
10. this.responseWeb.setResponseHeader(this.heads)
11. this.responseWeb.setResponseData(this.webData)
12. this.responseWeb.setResponseEncoding('utf-8')
13. this.responseWeb.setResponseMimeType('text/html')
14. this.responseWeb.setResponseCode(200)
15. this.responseWeb.setReasonMessage('OK')
16. return this.responseWeb
17. })
```

[InterceptRequest.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/InterceptRequest.ets#L32-L48)

**参考链接**

[Class (WebResourceResponse)](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)
