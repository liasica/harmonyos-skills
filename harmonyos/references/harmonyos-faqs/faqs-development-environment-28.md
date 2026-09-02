---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-28
title: DevEco Studio无法识别复制的模块
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio无法识别复制的模块
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f7000e790987473512f49024b017953ab784bcdf084f256c2b3e42f415f1e84e
---

## 问题现象

* 复制一个模块到新项目，DevEco Studio无法识别模块，导致无法打包。
* 使用版本控制软件拉取他人代码到本地，未正确识别module，文件夹右下角没有蓝色角标，打包报错：

  ```screen
  * Try the following:
  > Check whether the module which D:\xxx.ets belongs to is correctly configured.
  > Check the corresponding file name is correct(including case-sensitivity).
  ```

## 解决方案

* 如果是通过import形式导入模块，可以参考文档：[导入Module](../harmonyos-guides/ide-import-module.md)。具体步骤如下：
  1. 在菜单栏单击File > New > Import... > Import Module。
  2. 选择导入的模块。在指定路径下，选择导入的模块，单击OK。导入的模块可以为文件夹，也可以为zip格式。

* 若是从其他项目复制的/拉取他人代码的模块，在工程级别的build-profile.json5中，在app.modules数组中添加一个对象，其中name属性为实际模块名称、src属性为实际模块相对路径。

  如：{"name":"harlibrary","srcPath":"./harlibrary"}。
