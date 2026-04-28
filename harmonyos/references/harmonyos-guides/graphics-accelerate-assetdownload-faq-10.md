---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-10
title: 若开发者在游戏中使用Unity Addressables资源管理框架，如何集成游戏资源包后台下载功能？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 若开发者在游戏中使用Unity Addressables资源管理框架，如何集成游戏资源包后台下载功能？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8e879368e985edf66c5dae7730d76b873f865afbf3789d4b7691bb2cd275474
---

Addressables资源加载机制是根据Addressables的缓存文件判定资源包是否已下载，若未下载再通过游戏资源包后台下载功能把资源文件下载到Addressables的缓存目录下。集成步骤如下：

* 在游戏资源包下载的[onDownloadContentRequest](../harmonyos-references/graphics-accelerate-extensionability.md#ondownloadcontentrequest)生命周期函数中：

  1. 下载远端服务器上的Addressables的资源索引hash文件，与本地Addressables的hash文件做对比。
  2. 若hash值不一样，则表示有热更资源，准备进行资源更新，下载远端服务器上的Addressables的资源索引文件catalog.json文件。
  3. 将远端的catalog.json文件以及本地的catalog.json文件，按照catalog解析规则（具体可参考Addressables源码中ContentCatalogData.cs的解析实现）解析其中关键字段，diff后获取下载资源包列表信息。
  4. 把需要下载的资源列表信息转换成游戏资源包下载的[AssetDownloadConfig](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#assetdownloadconfig)对象返回给系统。
  5. 把catalog.json，catalog.hash以及GroupData.json文件存放在Addressables目标目录下，目录地址参考如下：

     ```
     1. /data/app/el2/<USERID>/base/<PACKAGENAME>/haps/entry/files/com.unity.addressables
     ```
* 在游戏资源包下载的[onBackgroundDownloadSucceeded](../harmonyos-references/graphics-accelerate-extensionability.md#onbackgrounddownloadsucceeded)生命周期函数中：

  完成下载的资源文件按照Addressables缓存文件规则，转移到Addressables缓存目录下。缓存目录参考如下：

  ```
  1. // 缓存目录规则：{缓存根目录}/{资源名称}/{资源哈希值}
  2. /data/app/el2/<USERID>/base/<PACKAGENAME>/haps/entry/files/TuanjieCache/Shared/feda8eb785f66e8cbfd86bda86dd111e/d73e91fc7611459d41ea88e823492c08
  ```
