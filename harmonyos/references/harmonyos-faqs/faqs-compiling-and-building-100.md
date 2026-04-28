---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-100
title: 打包体积大如何配置优化包体积问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 打包体积大如何配置优化包体积问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:920fa6d3b344ff42a129673ffa9f197ce13fed10caf77b0a07b5c80b07a5366b
---

**问题描述**

程序包当前打包后的体积为16MB，远超预期。

**解决措施**

1.首先查看打包的类型，debug编译打包含有调试信息相对于release包的体积较大。可以通过配置"strip": true来去除so中的debug信息减小so体积。该配置需要配置在hap和hsp模块，release和debug模式下都可以[配置CPP](../harmonyos-guides/ide-hvigor-cpp.md) :

```
1. "nativeLib": {
2. "debugSymbol": {
3. // This configuration can be used to execute strip on the cpp compiled product so, removing debugging information and symbol tables from so
4. "strip": true,
5. // Execute strip
6. "exclude": []
7. //Execute strip filtering regular expression rules
8. }
9. },
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library1/build-profile.json5#L39-L47)

2. DevEco Studio默认在打包应用时不压缩so库文件。配置so压缩选项后，DevEco Studio会以压缩形式打包so库文件，从而减小应用包的大小。在应用模块配置文件module.json5中，将compressNativeLibs字段的值设置为true，然后重新编译和打包应用。

```
1. {
2. "module": {
3. // ...
4. "compressNativeLibs": true // Package libs library in compressed storage format
5. }
6. }
```

[module.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/module.json5#L3-L72)
