---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-21
title: IDE在线签名报错该怎么解决
breadcrumb: FAQ > DevEco Studio > 签名服务 > IDE在线签名报错该怎么解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:adc885cff6c8633d6e7c2532b94d5dfc6843ed6a97231f598d5f4a930ae618aa
---

## 问题现象

IDE自动签名时报错，报错信息为：

```screen
The bundle name contains 7 to 128 characters, including only letters, digits, and underscores ( ). It must start with a letter and contain at least three segments separated by periods (.), each of the segments ending with a digit or letter.
```

## 背景知识

进入File>Project Structure...>Project>Signing Configs界面，勾选“Automatically generate signature”（如果是HarmonyOS工程，需同时勾选“Support HarmonyOS”），即可完成签名。如果未登录，请先单击Sign In进行登录，然后自动完成签名。详情可参考[应用/元服务签名](../harmonyos-guides/ide-signing.md)。

## 问题定位

自动签名时，bundleName没有带出，显示为空，导致出现上述报错。往上定位，发现是AppScope下的app.json5文件没有被识别到，继续定位，发现是设置了忽略app.json5文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PnVw0h91QYKTJaWjvF0l-w/zh-cn_image_0000002658808643.png "点击放大")

## 分析结论

设置忽略app.json5文件，导致没有识别出AppScope下的app.json5文件。

## 修改建议

删除忽略app.json5文件设置。
