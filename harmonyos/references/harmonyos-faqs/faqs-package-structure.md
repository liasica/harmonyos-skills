---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure
title: 程序包结构
breadcrumb: FAQ > 应用框架开发 > 程序包结构
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:26+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:34b91d11a2b196e91e78e67d79bfca30f0d36d693801aacddef4d0e5fa78781d
---

* **[HSP打包后，为什么会生成HAR包，它是否会导致App包大小膨胀](faqs-package-structure-2.md)**
* **[从包管理的角度，保证代码安全的措施有哪些](faqs-package-structure-4.md)**
* **[如何理解App、HAP、HAR、HSP的关系](faqs-package-structure-5.md)**
* **[HSP/HAR包中如何引用外部编译的so库文件](faqs-package-structure-6.md)**
* **[SharedLibrary能否在配置文件中声明abilities、extensionAbilities标签](faqs-package-structure-7.md)**
* **[HAR包中使用window作为Toast时无法引入页面组件](faqs-package-structure-8.md)**
* **[业务模块HAR如何获取宿主HAP的数据](faqs-package-structure-9.md)**
* **[如何安装打包出来的App包（通过什么命令安装）](faqs-package-structure-13.md)**
* **[如何判断应用可被卸载](faqs-package-structure-14.md)**
* **[HAR、HSP不能支持Ability、Page声明，限制的理由是什么？后续是否会支持](faqs-package-structure-15.md)**
* **[是否允许HAR的循环依赖](faqs-package-structure-16.md)**
* **[HAP依赖HAR A，HAR A依赖HAR B。HAP能否调用HAR B提供的接口？如果不支持间接依赖HAR，设计的原因是什么](faqs-package-structure-17.md)**
* **[通过resourceManager.getStringResource接口获取HSP资源文件报“Resource id invalid”错误](faqs-package-structure-18.md)**
* **[HAP/HAR/HSP的关系是什么？是否都可以声明注册Ability和Page？三种类型分别推荐哪些的使用场景？选择原则是什么](faqs-package-structure-19.md)**
* **[如何正确引用HAR/HSP包模块](faqs-package-structure-21.md)**
* **[从HAP的拆包中，如何区分是HAR和HSP](faqs-package-structure-23.md)**
* **[在HAP中调用createModuleContext方法获取的Context是什么层级](faqs-package-structure-25.md)**
* **[如何获取当前HAP的BundleName](faqs-package-structure-26.md)**
* **[如何实现在不使用UIAbility的情况下，能够模块化管理代码，并且各个模块之间可以相互路由跳转](faqs-package-structure-27.md)**
* **[Entry模块的HAP和Feature模块的HAP在使用和功能上的区别是什么](faqs-package-structure-28.md)**
* **[在HSP export类时，ts文件是按.d.ts导出还是.d.ets导出](faqs-package-structure-29.md)**
* **[如何避免模块下文件打包进HAR包后，存在的不可预期的资料、配置或信息安全风险](faqs-package-structure-31.md)**
* **[HAR包多账号如何上传](faqs-package-structure-32.md)**
* **[HSP包编译之后的.har文件的作用是什么](faqs-package-structure-33.md)**
* **[如何使HSP包版本号统一](faqs-package-structure-34.md)**
* **[如何将多工程的HAP打包成一个App](faqs-package-structure-35.md)**
* **[对于HAP包中引用的HSP包是否有数量限制](faqs-package-structure-36.md)**
* **[HAR如何转换为HSP](faqs-package-structure-37.md)**
* **[HAR包是否支持依赖传递](faqs-package-structure-38.md)**
* **[如何实现跨模块的页面跳转功能](faqs-package-structure-39.md)**
* **[如何卸载debug包](faqs-package-structure-40.md)**
* **[应用安装、卸载时是否有数据上报](faqs-package-structure-41.md)**
* **[如何解决依赖的版本冲突问题](faqs-package-structure-43.md)**
* **[为什么同一App下的HSP文件vendor参数不同时会安装失败](faqs-package-structure-44.md)**
* **[如何让两个HSP不相互依赖，使用对方的组件](faqs-package-structure-45.md)**
* **[应用安装到设备的方式有哪些](faqs-package-structure-47.md)**
* **[HAR和HSP的使用场景介绍](faqs-package-structure-48.md)**
* **[一个HSP模块如何快速切换成HAR模块](faqs-package-structure-49.md)**
* **[是否推荐使用BM QuickFix制造修复包](faqs-package-structure-50.md)**
* **[使用hdc命令安装release HAP包到设备时上报“INSTALL\_FAILED\_APP\_SOURCE\_NOT\_TRUSTED”错误](faqs-package-structure-51.md)**
* **[如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间等信息](faqs-package-structure-52.md)**
* **[如何安装打包出来的App包（通过什么命令安装）](faqs-package-structure-54.md)**
* **[应用免安装的限制、字段解释以及如何自测](faqs-package-structure-56.md)**
* **[安装HAP包报“failed to install bundle. install debug type not same”错误](faqs-package-structure-57.md)**
* **[除应用市场外，是否存在其它途径下载安装应用包](faqs-package-structure-58.md)**
* **[如何判断当前应用程序是Debug包还是Release包](faqs-package-structure-61.md)**
* **[如何判断应用程序是否安装](faqs-package-structure-62.md)**
* **[如何跨HSP包调用rawfile目录下的文件](faqs-package-structure-63.md)**
* **[如何获取应用包的签名指纹信息，即.p12文件信息](faqs-package-structure-64.md)**
* **[使用发布证书进行调试时出现安装错误: Install Failed: error: failed to install bundle.](faqs-package-structure-65.md)**
* **[使用HSP的多包场景下，直接崩溃并产生cppcrash异常日志，错误信息为resolveBufferCallback get buffer failed](faqs-package-structure-66.md)**
* **[HAP包中的“--BEGIN CERTIFICATE--”是什么格式的数据](faqs-package-structure-67.md)**
* **[sign包和unsign包产物之间是否有差异](faqs-package-structure-68.md)**
* **[如何在应用内共享HSP](faqs-package-structure-69.md)**
* **[如何通过代码获取Hap包的打包时间](faqs-package-structure-70.md)**
* **[应用静态快捷方式如何接入X键](faqs-package-structure-71.md)**
