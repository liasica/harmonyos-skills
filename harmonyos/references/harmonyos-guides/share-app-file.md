---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file
title: 应用文件分享
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用文件分享
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0b878955c2be89e4a40ebe2412cd96d355872c84007e1d5c42dade5ab4a7d2ca
---

应用文件分享是应用之间通过分享URI（Uniform Resource Identifier）进行文件共享的过程。

## 通过拉起文件处理类应用进行文件分享(startAbility)

基于[文件选择器(startAbility)](file-processing-apps-startup.md)的分享方式，应用可分享单个文件，通过[ohos.app.ability.wantConstant的wantConstant.Flags接口](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)以只读或读写权限授权给其他应用。被分享应用可通过[fileIo.open](../harmonyos-references/js-apis-file-fs.md#fileioopen)打开URI，并进行读写操作。

## 应用可分享目录

| 沙箱路径 | 说明 |
| --- | --- |
| /data/storage/el1/base | 应用el1级别加密数据目录 |
| /data/storage/el2/base | 应用el2级别加密数据目录 |
| /data/storage/el2/distributedfiles | 应用el2加密级别有账号分布式数据融合目录 |

## 文件URI规范

文件URI的格式：

格式为：file://<bundleName>/<path>

* file：文件URI的标志。
* bundleName：该文件资源的属主。
* path：文件资源在应用沙箱中的路径。

注意

1. 因URI处理涉及编解码，系统无法保证应用自行拼接的URI地址的可用性。
2. 推荐使用系统提供的接口获取URI，如[getUriFromPath接口](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)。
