---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-52
title: 相册选择图片缩略图不显示
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 相册选择图片缩略图不显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f09b5f40819a67f432fabcba816075affb9c0fc0d3bfb6acf09146c71cd095a9
---

## 问题现象

从相册选择图片上传预览时不展示缩略图。

## 背景知识

* [应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)是安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问，开发者可以使用Device File Browser[访问设备文件](../harmonyos-guides/ide-device-file-explorer.md)。
* 应用沙箱路径下通过[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)读写文件，经过映射转换，实际读写的是真实物理路径中的应用文件。
* [用户文件URI](../harmonyos-guides/user-file-uri-intro.md)：用户文件URI是文件的唯一标识，在对用户文件进行访问与修改等操作时往往都会使用到URI。

## 问题定位

通过日志排查图片加载报错信息，发现显示GetAsset failed，可知图片路径不对。

```shell
04-19 15:34:30.062 25379 26202 W C03900/Ace: [(100000:100000:scope)] GetAsset failed: data/storage/el2/base/cache/a835451856dd41b588ad31d86b51ee31.jpg
04-19 15:34:30.062 25379 26202 W C0391F/AceImage: [(100000:100000:scope)] No asset data! NodeId = 761-759.
04-19 15:34:30.062 25379 26202 W C0391F/AceImage: [(100000:100000:scope)] Fail load imageData. src = <private>, nodeId = 761-759.
04-19 15:34:30.062 25379 25379 I C03945/AceStateStyle: [(100000:100000:scope)] Start execution, node is Text/766, reset is 1
04-19 15:34:30.062 25379 25379 I C03945/AceStateStyle: [(100000:100000:scope)] Find customNode from parent: Button2
04-19 15:34:30.063 25379 25379 W C0391F/AceImage: [(100000:100000:scope)] Image LoadFail, source = <private>, reason: Failed to load image data
```

## 分析结论

data/storage/el2/base/是沙箱路径，直接使用而未转换为系统可识别的URI，导致图片不显示。

## 修改建议

选择相册图片，将文件保存到应用沙箱目录后，将路径转换成系统可识别的URI显示。

* 方案一：可以利用[getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)方法把传入的路径path生成应用自己的URI。
* 方案二：给filePath加上"file://"前缀，可以参考[媒体文件URI介绍](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri介绍)，通过字符串拼接转换成URI。
