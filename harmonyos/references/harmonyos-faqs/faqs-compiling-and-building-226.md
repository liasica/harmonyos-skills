---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-226
title: 编译构建时报错：资源缺失错误问题汇总
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译构建时报错：资源缺失错误问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:44d62ee31d4c434f636074dd7425f2999ffab44b59071c3dd58f55b3a1afa3c4
---

## 问题现象

编译构建时，有哪些问题会产生资源缺失的报错？

## 背景知识

* [应用资源](../best-practices/bpta-multi-device-resource.md#应用资源)：应用开发中使用的各类自定义资源文件，需要统一存放于应用的resources目录下，便于使用和维护。
* [资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)：应用开发过程中，需要使用字符串、颜色、字体、间距和图标等资源。不同设备或配置下，这些资源的值会有所不同。

## 问题定位

* **场景一**：编辑器Resource资源存在，调试的时候报错未知资源。使用单引号和双引号都会报错。反引号正常编译。但是页面上加载不到资源文字和图片都不行。
* **场景二**：将依赖放到feature里面通过router引入时会报错，提示找不到文件。
* **场景三**：把项目迁移到3层架构项目后，工程根目录下hvigorfile.ts报错，无法使用HMRouter跳转。

## 分析结论

* **场景一**：工程中模块A引用了模块B，编译模块A时出现错误。开发者使用了相对路径引用了模块B的资源从而**产生"Unknown resource name 'xxxx'"的报错**。
* **场景二**：引用第三方包，构建失败，**提示“Cannot find module 'xxx' or its corresponding type declarations”。**
* **场景三**：同样是在项目结构变化之后，引用第三方包，构建失败，**提示“Cannot find module 'xxx' or its corresponding type declarations”。**

## 修改建议

* **场景一解决方案**：资源放置在模块B目录resource/base路径下，并且将模块B安装。模块A中不能使用相对路径引用模块B的资源，改成直接通过定义的模块名称的方式来引用。
* **场景二和场景三的解决方案**：进入模块级或工程级的oh-package.json5文件，检查三方包是否已安装。若未安装，执行ohpm install安装。若已安装，检查“main”字段是否配置正确。若未配置或配置错误，需配置为正确的入口文件。
