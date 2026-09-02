---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-66
title: ohos.request下载文件使用https链接下载失败，改成http可以下载成功
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > ohos.request下载文件使用https链接下载失败，改成http可以下载成功
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:eab2a5715a3d4558ee3948bec537ccadb61b148aea5738e96331e05861d55758
---

## 问题现象

* 问题一：下载文件使用https链接下载失败，改成http可以下载成功，报错如下：

  ```txt
  03-0709:22:34.9063171-3218C01C50/downloa...equestServicedownload_serverETask791103119HttpClientError{ErrorKind:Connect,Cause:Custom{kind:Other,error:SslError{code:SslErrorCode(1),internal:Some(Ssl(ErrorStack([StackError{code:369098857,file:"",line:0,func:Some("ossl_store_get0_loader_int"),data:Some("scheme=file")},StackError{code:2147483650,file:"",line:0,func:Some("file_open"),data:Some("callingstat(/system/etc/certs)")},StackError{code:369098857,file:"",line:0,func:Some("ossl_store_get0_loader_int"),data:Some("scheme=file")},StackError{code:2147483650,file:"",line:0,func:Some("file_open"),data:Some("callingstat(/system/etc/certs)")},StackError{code:369098857,file:"",line:0,func:Some("ossl_store_get0_loader_int"),data:Some("scheme=file")},StackError{code:2147483650,file:"",line:0,func:Some("file_open"),data:Some("callingstat(/system/etc/certs)")},StackError{code:167772294,file:"",line:0,func:Some("tls_post_process_server_certificate"),data:None}])))}}}
  ```
* 问题二：https服务器下载没任何反应，但是http服务器没问题？

## 解决方案

* 问题一：

  开发者可以使用上传下载模块[ohos.request](../harmonyos-references/js-apis-request.md)将应用文件上传到网络服务器，也可以从网络服务器下载网络资源文件到本地应用文件目录。

  从日志可以看出openssl报的错，原因是手机本地SSL证书有问题，证书校验失败。需要检查服务端发送的证书有没有问题，详情可参考[网络连接安全配置开发实践](../harmonyos-guides/network-connection-security-configuration.md)。
* 问题二：

  使用request.downloadFile从云服务器下载文件，服务器回应的response报文中Content-Security-Policy字段格式是obs-line-fold，这个格式不能解析导致报错，这个格式当前rfc中表示是只支持在message/http媒体类型上使用。

  解决办法：

  客户端设置回应报文中Content-Security-Policy字段格式，不使用obs-line-fold格式，或使用[ohos.net.http](../harmonyos-references/js-apis-http.md)接口下载。
