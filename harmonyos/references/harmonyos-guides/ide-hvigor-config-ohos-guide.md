---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-guide
title: 能力说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 动态修改编译配置 > 能力说明
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7738386e6b40a5b132a6079d6168bf5295d89a2fd87c7cc3dc780b849314aa22
---

Hvigor支持在hvigorfile.ts中接收部分编译配置，以实现动态修改编译配置，并将其应用到构建过程与结果中。

目前有两种实现方式：

* 以Hvigor hook能力为基础，通过插件上下文实现动态配置。(推荐使用)
* 在hvigorfile.ts中通过overrides关键字导出动态配置。(不推荐使用)

## 通过hook以及插件上下文实现动态配置

Hvigor支持Stage模型在Hvigor hook中操作从硬盘上读取的以下配置文件：

* 每个hvigorNode中的build-profile.json5
* module.json5
* app.json5
* 每个module下的oh-package.json5文件中的dependency、devDependency、dynamicDependency以及version。

目前可以通过Hvigor对象提供的上下文直接获取和动态修改配置，并将其应用到构建过程与结果中。

在hvigorfile.ts或hvigorconfig.ts文件中，可以使用Hvigor提供的API接口来实现此能力。

相比于下面的overrides的能力来说，通过hook以及插件上下文来动态修改编译配置更为灵活和易于理解，功能也更为全面，推荐采用此种方式。具体使用方式请参考[通过hook以及插件上下文动态修改配置(推荐使用)](ide-hvigor-config-ohos-sample.md#section67131365449)。

## 在hvigorfile.ts中通过overrides关键字导出动态配置

在hvigorfile.ts中，我们约定在导出的对象中的config.ohos属性里接收编译的配置：

```ts
export default {  
    system: hapTasks,  
    config: {  
        ohos: {
            ...
        }    
    }
}
```

目前可以在工程级的hvigorfile.ts的config.ohos中配置的字段：

* overrides：定义需要覆盖的字段，会在构建过程中覆盖原有的对应配置项。
  + signingConfig：签名配置，对应build-profile.json5里的[signingConfigs配置项](ide-hvigor-build-profile-app.md#section153288223224)。
    - type
    - material
      * certpath
      * storePassword
      * keyAlias
      * keyPassword
      * profile
      * signAlg
      * storeFile
  + appOpt：对应[app.json5](app-configuration-file.md)里的配置项字段。
    - bundleName
    - bundleType
    - icon
    - label
    - vendor
    - versionCode
    - versionName

目前可以在模块级的hvigorfile.ts的config.ohos中配置的字段：

* overrides：定义需要覆盖的字段，会在构建过程中覆盖原有的对应配置项。
  + buildOption：对应build-profile.json5里的[buildOption配置项](ide-hvigor-build-profile.md#section1010733210421)。
    - arkOptions
    - externalNativeOptions
    - napiLibFilterOption
    - nativeLib
    - resOptions
    - sourceOption

配置在overrides项中的参数，其优先级会高于在配置项中的对应字段。
