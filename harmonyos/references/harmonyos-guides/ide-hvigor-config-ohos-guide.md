---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-guide
title: 能力说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 动态修改编译配置 > 能力说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0cf2a55e949a2e5729abd02adcdad3b3d979d469e58103de0702e58bbe4070f
---

Hvigor支持在hvigorfile.ts里接收部分编译配置，以实现动态配置构建配置、并使能到构建的过程与结果中。

此能力现有两种方式实现：

* 以hvigor hook能力为基础通过插件上下文来动态配置。(推荐使用)
* 在hvigorfile.ts中通过overrides关键字导出动态配置。(不推荐使用)

## 通过hook以及插件上下文实现动态配置

Hvigor支持stage模型在hvigor hook中操作从硬盘上读取的以下配置文件：

* 每个hvigorNode中的build-profile.json5
* module.json5
* app.json5
* 每个module下的oh-package.json5文件中的dependency、devDependency、dynamicDependency以及version。

目前可以通过hvigor对象提供的上下文直接获取和修改配置以实现动态配置构建配置、并使能到构建的过程与结果中。

在hvigorfile.ts或hvigorconfig.ts文件中，可以使用Hvigor提供的API接口来实现此能力。

相比于下面的overrides的能力来说，通过hook以及插件上下文来动态修改签名和编译配置更为灵活和易于理解，功能也更为全面，推荐采用此种方式。具体使用方式请参考[通过hook以及插件上下文动态配置构建配置(推荐使用)](ide-hvigor-config-ohos-sample.md#section67131365449)。

## 在hvigorfile.ts中通过overrides关键字导出动态配置

在hvigorfile.ts中，我们约定在导出的对象中的config.ohos属性里接收编译的配置：

```
1. export default {
2. system: hapTasks,
3. config: {
4. ohos: {
5. ...
6. }
7. }
8. }
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
