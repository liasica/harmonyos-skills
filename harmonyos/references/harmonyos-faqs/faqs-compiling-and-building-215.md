---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-215
title: 如何解决打包时提示删除自定义字体无权限问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决打包时提示删除自定义字体无权限问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:658efdec9316608ff5d327765b9332ade2b9172e70a3722c52a0f81f33045edb
---

## 问题现象

首次执行build或者先clean后build操作时可正常打包，但连续执行build操作时会出现自定义ttf字体文件因权限不足导致删除失败的问题。

报错信息如下：

```screen
Tools execution failed.
Error: remove file 'E:\harmony_example\calendar-harmony\entry\build\default\intermediates\res\default\resources\rawfile\font\avenir_regular.ttf' failed, reason: Permission denied
Detail: Please check the message from tools.
```

在其他电脑上进行build操作可以成功打包，并不会出现上述报错。

## 背景知识

自定义字体业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/YYYZrjasRxCiu8y8YFqijQ/zh-cn_image_0000002628569180.png "点击放大")

## 问题定位

查看font文件下名为avenir\_regular的ttf文件，发现该ttf文件属性为【只读】权限，将该文件添加【读写】权限后，再次进行build构建时，编译通过。

ttf属性截图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/pq9RRt5jTfacxIlZ-puTCg/zh-cn_image_0000002658928505.png)

## 分析结论

出现删除自定义字体无权限问题的原因为ttf文件属性为只读权限，无法进行删除操作导致报错。

## 修改建议

经检查发现ttf文件属性为只读权限，进行再次build打包时因没有操作权限无法进行删除操作，将只读权限修改为读写权限即可。
