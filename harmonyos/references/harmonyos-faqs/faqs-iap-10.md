---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-10
title: JWT Payload参数填写要求和常见问题
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > JWT Payload参数填写要求和常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d77fc542b0c031821238c1b1635fb37dc59aa9b6a699d00afc69e946162ae547
---

## 问题现象

接入应用内支付服务，在生成服务端请求的token时，请求的Header，Payload和对应的token中的参数如何填写？

## 背景知识

JSON Web Token（JWT）是一个开放标准（RFC 7519），定义了一种安全传输信息的方法。在应用内支付服务中JWT被用在服务端API请求的Authorization标头中来鉴权。目前可以通过从AppGallery Connect下载的私钥签名生成JWT。

## 解决方案

JWT的生成和密钥中的私钥相关，因此需要先[下载密钥](../app/download-0000001958955101.md)，特别关注的是私钥仅供下载一次，下载后的私钥需要安全保存，丢失后则需更换新的密钥重新生成JWT。

创建JWT格式的token分为下面三个步骤：

1. [创建JWT header](../harmonyos-references/iap-jwt-description.md#创建jwt-header)需要填写三个必填参数alg、typ和kid，前两个参数分别为固定值ES256和JWT，需要关注的是kid参数的填写，该参数对应的是密钥ID，密钥ID的获取可在[创建密钥](../app/key-0000001959074877.md)时获取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/xEsjVtVdTNu00tQCSTqMQw/zh-cn_image_0000002658913789.png "点击放大")

   创建密钥时需注意密钥名称长度不超过50字符，且只允许字母、数字和下划线，否则会提示创建失败。
2. [创建JWT Payload](../harmonyos-references/iap-jwt-description.md#创建jwt-payload)需注意iss（密钥颁发者ID）、exp（JWT到期时间）、aid（APPID）和digest参数的填写。
   * Issuer ID是在初次生成密钥时，服务器为商户自动生成唯一的ID，如何获取可以参考第一步中展示的图片。
   * exp（JWT到期时间）是一个以秒为单位的UTC时间戳（如：1769049727），且和iat（JWT签发时间）相隔时间不能超过3600s，超过会提示JWT参数校验失败，相隔时间可通过exp减去iat来计算得出，推荐通过iat（JWT签发时间）+秒数的形式来设置到期时间。
   * aid是应用对应的APPID，可登录AppGallery Connect平台，在“开发与服务”中选择目标项目，通过“项目设置>常规>应用”获取目标应用的APPID。
   * digest是用sha256加密的hash值字符串，用于验证Request Body的完整性，此处需要注意算法必须是sha256格式的，使用其他类型的算法生成会提示JWT参数校验失败。
3. [创建JWT格式的token](../harmonyos-references/iap-jwt-description.md#创建jwt格式的token)则是通过第一步Header中指定的算法(ES256)以及下载后私钥（密钥ID关联的私钥）进行签名生成JWT，该操作通常是在应用服务器端完成的，目前支持生成JWT的编程语言有Java、Python、PHP、JS和Golang，具体可以参考[示例代码](../harmonyos-references/iap-jwt-description.md#代码示例)。

## 常见FAQ

Q：支付失败查看日志，提示错误码9999，错误信息JWT verification failed，如何解决？

A：JWT验签的时候参数传的有问题导致的，需要检查必填参数和签名算法是否正确以及kid和私钥是否匹配。

Q：AGC后台密钥管理中下载的私钥是什么格式的？

A：私钥下载下来后是xxx.p8的格式，使用前请检查是否匹配。

Q：一个Issuer ID可以管理多少个密钥？

A：最多可以管理10个有效密钥，具体可以参考创建密钥。
