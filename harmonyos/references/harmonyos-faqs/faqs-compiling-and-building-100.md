---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-100
title: 打包体积大如何配置优化包体积问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 打包体积大如何配置优化包体积问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3294c3f8fab299821baf65ec8da70d1afaecab7c8129e6e130c0eb70411ccff6
---

**问题描述**

程序包当前打包后的体积为16MB，远超预期。

**解决措施**

1. 首先查看打包的类型，debug编译打包含有调试信息相对于release包的体积较大。可以通过配置"strip": true来去除so中的debug信息减小so体积。该配置需要配置在hap和hsp模块，release和debug模式下都可以[配置CPP](../harmonyos-guides/ide-hvigor-cpp.md) :

   ```json
   "nativeLib": {
     "debugSymbol": {
       // This configuration can be used to execute strip on the cpp compiled product so, removing debugging information and symbol tables from so
       "strip": true,
       // Execute strip
       "exclude": []
       // Execute strip filtering regular expression rules
     }
   },
   ```
2. DevEco Studio默认在打包应用时不压缩so库文件。配置so压缩选项后，DevEco Studio会以压缩形式打包so库文件，从而减小应用包的大小。在应用模块配置文件module.json5中，将compressNativeLibs字段的值设置为true，然后重新编译和打包应用。

   ```json
   {
     "module": {
       // ...
       "compressNativeLibs": true // Package libs library in compressed storage format
     }
   }
   ```
