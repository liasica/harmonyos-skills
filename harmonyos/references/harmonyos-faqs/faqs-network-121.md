---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-121
title: HTTP中usingCache设置为true没有生效
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HTTP中usingCache设置为true没有生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3ea1b8e43c7801b2056be0ad8c4f3166a30a46806e1b3e60789c35e41529f82b
---

## 问题现象

使用http请求，设置usingCache：true同时调用flush方法，但是还是获取不到缓存。

问题代码示例参考如下：

```ts
let option: http.HttpRequestOptions = {
  usingCache: true,
  header: {
    'Cache-Control': 'max-age=315360000'
  }
}
let httpRequest = http.createHttp()
let httpResponseCache = http.createHttpResponseCache();
httpRequest.request('https://xxxxxx', option, (err: BusinessError, res: http.HttpResponse) => {
  if (!err) {
    httpResponseCache.flush((err: BusinessError) => {
      if (err) {
        console.error('HttpCache flush fail');
      }
      const newsResponse = JSON.parse(res.result.toString()) as NewsResponse
      this.newsList = newsResponse.data
      console.info('HttpCache flush success');
    });
    httpRequest.destroy();
  } else {
    console.error(`HttpCache error:${err}`);
    // 当该请求使用完毕时，开发者务必调用destroy方法主动销毁该JavaScript Object。
    httpRequest.destroy();
  }
})
```

## 背景知识

* [flush](../harmonyos-references/js-apis-http.md#flush9)：将缓存中的数据写入文件系统，以便在下一个http请求中访问所有缓存数据，使用callback方式作为异步方法。缓存数据包括：响应头(header)、响应体(result)、cookies、请求时间(requestTime)和响应时间(responseTime)。
* Cache-Control：用于指定缓存策略，如no-cache, no-store, max-age, public, private等。

## 问题定位

检查服务端是否设置了Cache-Control字段。

## 分析结论

Cache-Control为通用报头，通常是在服务器端设置的，如果在HttpRequestOptions中header里设置'Cache-Control': 'max-age=xxxx'，缓存不会生效。

## 修改建议

在服务器端中设置http请求头为Cache-Control：max-age=xxxx即可。

## 常见FAQ

Q：IP地址响应头也设置的Cache-Control：max-age=60，但依然还是缓存失败，这是为什么？

A：可能因为之前其他缓存影响，导致此IP地址缓存失败，重新清空浏览器缓存或者重新卸载安装APP。
