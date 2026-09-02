---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-11
title: 如何解决应用市场更新失败，报错code"17700073"的问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何解决应用市场更新失败，报错code"17700073"的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ea970fb5d5922427eed6874d2f3b5d1222aa1dc7ba6ca83e435fb5dd64dca5a4
---

## 问题现象

已在手机上安装的应用，在应用市场更新失败，报错信息如下：

```txt
[AGDownload-DownloadHandler]:installApp return:{"isDeleteDownloadFiles":false,"costTime":164,"code":17700073,"message":"BusinessError 17700073: Failed to install the HAP because an application with the same bundle name but different signature information exists on the device."} data:"" cannotRemove:false
```

## 背景知识

在HarmonyOS系统中，应用的安装和更新依赖于包名和签名信息。如果设备上存在相同包名但签名信息不一致的应用，系统将拒绝安装或更新新版本的应用，以防止安全风险。

## 问题定位

* 检查设备上是否已安装具有相同包名但签名信息不同的应用，导致安装失败。
* 检查设备上是否曾安装相同包名但签名信息不同的应用，并且在卸载时保留了数据，导致安装失败。

## 分析结论

问题的原因是设备上存在相同包名但签名信息不同的应用，或者是相同包名但签名信息不同的应用在卸载时保留了数据。

一般如下场景会出现签名不一致的情况：

* 本地安装的应用是自动签名通过IDE或者命令行安装的，更新版本从应用市场安装，这样会导致签名信息不一致。
* 本地安装的应用是通过应用市场安装的，但是开发者新上架的版本修改了签名信息，这样重新从应用市场安装也会导致签名信息不一致。

## 修改建议

* 卸载设备上相同包名的应用。
* 如果设备上存在相同包名但签名信息不一致的应用，并且在卸载时保留了数据，请先重新安装该应用，然后卸载时选择不保留数据。

## 常见FAQ

Q：系统是否支持多签名机制，即同一应用同时使用多个签名密钥进行密钥轮换？

A：不支持。系统要求相同包名的应用必须使用一致的签名信息。如果应用版本签名信息不一致，会导致用户更新版本时安装失败。在进行密钥轮换时，需确保新旧版本使用相同的签名密钥，否则将触发安装冲突。
