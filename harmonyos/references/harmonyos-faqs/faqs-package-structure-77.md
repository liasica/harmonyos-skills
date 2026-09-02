---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-77
title: 跨工程引用模块报错
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 跨工程引用模块报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:261857ad9346ab7a54d471d1193df353b62f26db2f1e41098e4eb3be90717ca5
---

## 问题现象

目前有两个HarmonyOS工程ProjectA和ProjectB，现在需要在ProjectA中引用ProjectB内的模块。

编译运行ProjectA，报错如下：

```screen
Error Message: Failed to generate the cache path corresponding to file /path/to/project/CommonSDK/ProjectB_SDK/oh_modules/.ohpm/@ohos+hypium@1.0.18/oh_modules/@ohos/hypium/src/main/Constant.js.
Because the file belongs to a module outside the project and has no project information.
```

## 背景知识

Module是HarmonyOS应用的基本功能单元，包含了源代码、资源文件、第三方库及应用清单文件，每一个Module都可以独立进行编译。

## 问题定位

查看ProjectA配置build-profile.json5中，modules的srcPath字段是否添加了ProjectB的模块。

## 分析结论

工程不能引工程，可以引用模块。工程级build-profile.json5中modules的srcPath字段下没有引用工程外模块。

## 修改建议

在工程级build-profile.json5文件[modules](../harmonyos-guides/ide-hvigor-build-profile-app.md#section1961794812219)配置中，srcPath字段下配置工程外Module的相对路径来导入ProjectB模块，具体请参考[导入/引用模块](../harmonyos-guides/ide-add-new-module.md)。

示例如下：

在工程级build-profile.json5文件中添加配置参考如下：

```screen
{
  "name": "library",
  "srcPath": "../MyApplication2/library"
}
```

在oh-package.json5中添加依赖参考如下：

```screen
"dependencies": {
  "library":"../MyApplication2/library"
},
```
