---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-4
title: onInterceptRequest拦截URL并自定义HTML文件，页面加载失败
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > onInterceptRequest拦截URL并自定义HTML文件，页面加载失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:31892b566591473d5e447e5731428d00eb9a8ce50675113846c552ea2d8c1fd7
---

**问题现象**

当使用onInterceptRequest拦截页面Web的src链接后返回自定义HTML时，如果自定义HTML文件中的script标签内容未加载，需要检查脚本路径和加载方式。

**解决措施**

设置拦截器时，需要同时设置setResponseEncoding、setResponseMimeType和setResponseHeader等参数，仅设置setResponseData内核将无法识别这是HTML文件。参考代码如下：

```ts
Web({ src: 'www.example.com',controller: this.controller })
  .onInterceptRequest((event) => {
    console.log('url:' + event.request.getRequestUrl())
    this.responseWeb = new WebResourceResponse();
    let head1: Header = {
      headerKey: "Connection",
      headerValue: "keep-alive"
    }
    let length = this.heads.push(head1)
    this.responseWeb.setResponseHeader(this.heads)
    this.responseWeb.setResponseData(this.webData)
    this.responseWeb.setResponseEncoding('utf-8')
    this.responseWeb.setResponseMimeType('text/html')
    this.responseWeb.setResponseCode(200)
    this.responseWeb.setReasonMessage('OK')
    return this.responseWeb
  })
```

**参考链接**

[Class (WebResourceResponse)](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md)
