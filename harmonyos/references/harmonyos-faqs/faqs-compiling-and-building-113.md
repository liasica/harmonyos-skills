---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-113
title: 编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:31+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:bb3ee7048448df0a4355aa985dde77ed5fcee3843ce0dbc39bc653f97b1839cb
---

**问题现象**

编译构建时，出现错误：Init keystore failed: parseAlgParameters failed: ObjectIdentifier()

```
1. hap-sign-tool: error: ACCESS_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools
```

**错误原因**

使用高版本JDK生成密钥对(p12)，低版本JDK执行签名命令时，会因不兼容导致解析p12失败，签名失败。

**场景**

1. 使用DevEco Studio生成密钥对时，默认会调用软件预置的JDK17。如果使用本地低版本JDK进行签名，则会导致错误。
2. 用户本地使用高版本 JDK 生成密钥对，然后通过 DevEco Studio 进行签名。由于 DevEco Studio 中预置的 JDK 17 版本低于用户本地的 JDK，因此导致报错。

**解决方案**

检查本地环境DevEco Studio版本是否使用了JDK17。

命令：java -version

也可以使用DevEco Studio内部自带的JDK17，路径为${DevEco Studio}/jbr
