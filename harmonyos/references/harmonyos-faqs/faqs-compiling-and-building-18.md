---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-18
title: 编译报错“No available entry module found”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“No available entry module found”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9044a4a96cec3e9e9b5925a3e6d65c2e7b04ecf00c16fe8540b7913b7230a0f6
---

**问题现象**

DevEco Studio编译时出现“No available entry module found”错误。

**解决措施**

在feature模块中需要配置依赖的entry模块。DevEco Studio在编译时会检查feature模块所依赖的entry模块是否存在。如果出现该问题，原因可能包括以下几种情况：

1. 在feature模块的build-profile.json5文件中，entryModules字段的值与实际entry模块的名称不一致。请将entryModules字段的值改为entry模块的名称。
2. 在项目级build-profile.json5文件的modules字段中，确保feature模块位于所依赖的entry模块之后。由于DevEco Studio在编译时会按从前往后的顺序进行配置，如果feature模块在entry模块之前配置，会因未读取和配置entry模块而报错。因为编译过程是顺序执行的，前置模块无法获取后置模块的配置信息。
