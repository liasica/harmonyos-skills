---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-esmodule-compile
title: 模块化编译
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 模块化编译
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:22+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0862b9c696ba31a06c219f30684b9b52d20b3508566f1845efedd3ed87d29b2c
---

应用模块化编译是指基于ES Module的Bundleless编译模式，使用原生ES Module规则构建源码。API 10及以上版本的Stage工程默认开启模块化编译，可有效缩短增量编译时间、减小编译后的包体积。

说明

FA 模板创建的工程依然使用基于bundle打包的构建方式。

模块化编译解决了Bundle编译打包模式引入的如下问题：

* 同一个模块多次引用导致的重复打包及运行时加载，运行状态无法共享，单例模式运行异常；
* 修改单个模块文件，需要完整重新编译打包，耗时过长；
* 全局变量污染问题。

模块化编译模式有以下价值：

* 修改单个模块代码无需整包编译构建，增量编译构建时间极大减少；
* 基于ESModule规则，模块缓存利用率高，模块内变量变化能够及时反映到模块本身，动态实时绑定；
* 解决了单例问题；
* 减少了包的ROM size；
* 解决了变量污染等问题，各模块基于接口进行开发，提升开发效率。

## 使用规格约束

* 支持工程内hap引用同工程下其他hap代码，但不推荐使用此引用方式，建议使用har包方式组织公共代码并引用；
* 支持工程内hap通过配置文件（oh-package.json5）使用ohpm包管理的方式引用同工程下其他hap代码，不推荐使用此引用方式，建议使用har包方式组织公共代码并引用；
* 不支持引用工程外的代码以及工程内任意创建目录下的代码，否则工程编译报错；
* 推荐使用hap通过har（static library）的方式引用公共代码；
* 推荐使用hap通过hsp（shared library）的方式引用共享库，共享状态。
