---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-6
title: 碰一碰分享直接打开浏览器，未跳转至应用内页面
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 碰一碰分享直接打开浏览器，未跳转至应用内页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:1525ecb8766ad8f1755edd0437bbafe95f71702ea7c9b7198b1353e8d6eec331
---

## 问题现象

参考官网文档碰一碰发送分享数据[App Linking](../harmonyos-guides/knock-share-between-phones-content.md#app-linking)，在目标方module.json5配置关联域名后，碰一碰分享直接打开浏览器，未跳转至应用内页面。

## 背景知识

1. 排查[OpenLinkOptions](../harmonyos-references/js-apis-app-ability-openlinkoptions.md#openlinkoptions)中是否配置appLinkingOnly参数。当appLinkingOnly参数为false时，若有App Linking匹配的应用，则直接打开目标应用；若无App Linking匹配的应用，则尝试以浏览器打开链接的方式打开应用。
2. 开通App Linking服务，并完成相关配置，参考AppLinking[开发准备](../harmonyos-guides/applinking-preparations.md)。
3. module.json5配置域名时需要注意[uris标签说明](../harmonyos-guides/app-uri-config.md#uris标签说明)。

## 问题定位

步骤一：通过命令行验证是否可以通过App Linking成功拉起：

```bash
hdc shell aa start -U "https://www.example.com/test.xxx" --pb appLinkingOnly true
```

返回error: failed to start ability，说明App Linking未配置成功，未完成关联应用和网址域名关联，需在AGC开通App Linking。完善AGC相关配置后，还需要等待链接生效（参考[链接生效机制](../harmonyos-guides/applinking-direct-to-ag.md#链接生效机制)）24小时后，仍无法跳转应用。

步骤二：确认域名校验是否成功，使用以下命令查询验证结果：

```bash
hdc shell hidumper -s AppDomainVerifyManager
```

运行hidumper命令后，可以在控制台上看到当前应用配置的域名已经success，说明当前应用已完成域名配置，服务端正常：

```bash
com.example.application:
  appIdentifier:5760000000000000
  domain verify status:
    https://www.example.com:success
```

步骤三：检查DevEco Studio中module.json5配置是否正确，以如下module.json5为例。

```bash
{
  "scheme": "https",
  "host": "www.example.com",
  "pathRegex": "/test.*/.*"
}
```

参考uris标签要求可知：path、pathStartWith、pathRegex的取值前后均不需要加斜杠/。例如对于应用链接https://developer.huawei.com/consumer/cn/support，path字段应配置为consumer/cn/support。

当前pathRegex路径正则配置不正确，取值前多了一个斜杠/。

## 分析结论

当module.json5中未配置appLinkingOnly（默认为false）时，App Linking未匹配到应用，会以浏览器打开链接的方式打开应用，无法跳转应用。

排查思路：先从App Linking云侧配置开始排查，检查App Linking开通情况；若已完成云侧配置则检查端侧module.json5中的配置。

## 修改建议

完成云侧配置并修改uris后，可使App Linking正常拉起应用，实现碰一碰分享效果。

## 常见FAQ

Q：使用App Linking实现应用内跳转，正确配置了module.json5和applinking.json，使用碰一碰分享的sharableTarget.share(shareData)，超链接识别接收分享的内容后还是打开华为浏览器？

A：不能使用DevEco Studio的自动签名功能，必须使用手动签名，否则无法拉起应用。
