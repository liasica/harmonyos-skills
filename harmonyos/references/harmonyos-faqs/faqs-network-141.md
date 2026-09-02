---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-141
title: 如何解决http报错2300023
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决http报错2300023
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a3607213353f5e29cdae987b8587f6bee932813a631eddbc3f505deeb97febb
---

## 问题现象

http执行request报错：2300023 Failed writing received data to disk/application。

* 场景1：使用http下载图片、视频等大文件报错。
* 场景2：封装http单例工具类，并发执行请求报错。

  ```ts
  private httpRequest: http.HttpRequest | null = null;
  // ...
  this.httpRequest = http.createHttp();
  // ...
  // 发送请求
  const response = await this.httpRequest.request(fullUrl, requestOptions);
  ```

## 背景知识

[2300023](../harmonyos-references/errorcode-net-http.md#section2300023-向磁盘应用程序写入接收数据失败)：向磁盘/应用程序写入接收数据失败。

## 问题定位

按照2300023错误码可能原因，重点从两方面排查：

1. 检查远端服务器资源，判断文件大小是否大于5M，并使用小文件下载测试是否复现问题。
2. 检查是否异常调用[destroy](../harmonyos-references/js-apis-http.md#destroy)销毁导致接收数据不完整。
   * 全局搜索destroy并注释代码，测试请求是否正常。
   * 检查请求实例是否被重新赋值，或复用同一个请求，导致系统自动销毁未完成的请求。使用let newHttp = http.createHttp()创建新的变量及实例发起请求，未复现问题。

## 分析结论

1. 下载大文件时未定义[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)请求设置中的maxLimit参数，超出默认限制导致下载失败，限制信息可参考[request](../harmonyos-references/js-apis-http.md#request)说明。
2. 实现工具类时，HttpRequest实例不可复用。

## 修改建议

* 对于下载大文件导致的报错，参考[http请求传输大于5M文件报错2300023](faqs-network-64.md)或参考[应用文件上传下载](../harmonyos-guides/app-file-upload-download.md)使用request.downloadFile下载。
* 不要复用HttpRequest实例，创建一个HttpRequest实例并赋值给一个新的变量执行请求，避免前一个实例请求未接收便被销毁。
