---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-17
title: HAP依赖HAR A，HAR A依赖HAR B。HAP能否调用HAR B提供的接口？如果不支持间接依赖HAR，设计的原因是什么
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAP依赖HAR A，HAR A依赖HAR B。HAP能否调用HAR B提供的接口？如果不支持间接依赖HAR，设计的原因是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:29+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d9909879408ffe64f655be9a082ccb99e3c38de48dfab3fb9f5529d5c0cf4007
---

不支持传递依赖。

间接依赖的版本是不可控的，如果代码里使用某个版本的间接依赖，不同时间安装的依赖可能版本不一致，程序运行可能出现意想不到的错误。

举例说明：依赖关系：project->A(1.0.0)->B(^1.0.0)->C (latest)

在dependencies只声明了A，但是工程中import了B和C。而B和C的版本是不可控的，如果C的开发者发布了一个2.0.0的版本，下次安装依赖时，可能会安装C的2.0.0的版本。然后就有可能出现一些问题，例如：在代码没有任何改动的情况下，程序运行却出现报错，不同时间不同PC上构建的应用运行表现不一致等。

所以ohpm为了解决幽灵依赖的问题，设计了一个特殊的存储结构，从技术上进行限制、不允许引用间接依赖，从而避免出现幽灵依赖问题。在上面例子中表现就是：代码里只能引用A，引用B或C就会编译报错，提醒用户修改依赖配置。
