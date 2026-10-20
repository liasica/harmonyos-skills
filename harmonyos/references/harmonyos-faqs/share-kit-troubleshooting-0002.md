---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/share-kit-troubleshooting-0002
title: 碰一碰分享未跳转应用内页面问题
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 故障排查 > 碰一碰分享未跳转应用内页面问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:27+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:14f71f8eebf51d3eae587b61445bb7c113f5f4af06204323d8077eaba3a4f8a4
---

## 问题现象

参考官网文档碰一碰发送分享数据[App Linking](../harmonyos-guides/knock-share-between-phones-content.md#section11993134415016)，在目标方module.json5配置关联域名后，碰一碰分享直接打开浏览器，未跳转至应用内页面。

## 定位过程

1. 通过命令行验证是否可以通过App Linking成功拉起：

   ```bash
   hdc shell aa start -U "https://www.example.com/test.xxx" --pb appLinkingOnly true
   ```

   返回error: failed to start ability，说明App Linking未配置成功，未完成关联应用和网址域名关联，需在AGC开通App Linking。完善AGC相关配置后，还需要等待链接生效（参考[链接生效机制](../harmonyos-guides/applinking-direct-to-ag.md#section1928659151514)）24小时后，仍无法跳转应用。
2. 确认域名校验是否成功，使用以下命令查询验证结果：

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
3. 检查DevEco Studio中module.json5配置是否正确，以如下module.json5为例。

   ```json
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
