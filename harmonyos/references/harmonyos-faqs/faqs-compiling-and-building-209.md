---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-209
title: 移除module.json5中label和icon字段导致photoAccessHelper接口报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 移除module.json5中label和icon字段导致photoAccessHelper接口报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c0d47c76548f347a58524e8732a102cefa8b9b8be2a78145b16988870f80bc1
---

## 问题现象

移除了entry/module.json5中label和icon字段，采用工程的根目录build-profile.json5里面product对应的label和icon字段，为什么photoAccessHelper.showAssetsCreationDialog报错？

## 背景知识

* [配置多目标产物](../harmonyos-guides/ide-customized-multi-targets-and-products.md)：配置不同的产物信息。
* [showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)：调用photoAccessHelper.showAssetsCreationDialog接口拉起保存确认弹窗。用户同意保存后，返回已创建并授予保存权限的uri列表，该列表永久生效，应用可使用该uri写入图片/视频。

## 问题定位

* 排查showAssetsCreationDialog接口单独使用是否可以保存到图库。
* 排查移除module.json5中label和icon字段，showAssetsCreationDialog接口报错的原因。

## 分析结论

* photoAccessHelper.showAssetsCreationDialog接口单独使用正常，可成功保存图片到图库。
* 移除module.json5中label和icon字段后，调用showAssetsCreationDialog接口报错：showAssetsCreationDialog failed,errCode is 401,errMsg is Invalid input parameter.

  原因是showAssetsCreationDialog接口保存图片到图库时，会先创建一个对应APP的相册，相册的图标和名称会使用module.json5的label和icon字段。

## 修改建议

不能移除module.json5中label和icon字段，showAssetsCreationDialog接口保存图片到图库时，会先创建相册，其底层代码逻辑使用module.json5的label和icon字段。
