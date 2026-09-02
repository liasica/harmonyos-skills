---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app
title: 工程级build-profile.json5文件
breadcrumb: 指南 > 构建应用 > 配置文件 > 工程级build-profile.json5文件
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:82e96cfec12f1416d81181dbdf2442d606e9ccf7a295b9bd02d66716d3dd8dd5
---

## 配置文件结构

工程级build-profile.json5文件整体的结构如下。

```json
app
└── signingConfigs
    └── name
    └── material
        └── storePassword
        └── certpath
        └── keyAlias
        └── keyPassword
        └── profile
        └── signAlg
        └── storeFile
    └── type
└── products
    └── name
    └── signingConfig
    └── bundleName
    └── buildOption
        └── packOptions
            └── buildAppSkipSignHap
            └── fastBuildApp
            └── enableSourceCodeCheck
            └── deduplicateHar
            └── appWithSignedPkg
            └── enableIncrementalSoCompress
            └── deduplicateSo
        └── debuggable
        └── generateSharedTgz
        └── resOptions
            └── compression
                └── media
                    └── enable
                └── filters
                    └── method
                        └── type
                        └── blocks
                    └── files
                        └── path
                        └── size
                        └── resolution
                    └── exclude
                        └── path
                        └── size
                        └── resolution
            └── resCompileThreads
            └── copyCodeResource
                └── enable
                └── includes
                └── excludes
            └── ignoreResourcePattern
            └── excludeHarRes
            └── includeAppScopeRes
            └── idDefinedFilePath
        └── externalNativeOptions
            └── path
            └── abiFilters
            └── arguments
            └── cppFlags
        └── sourceOption
            └── workers
        └── nativeLib
            └── filter
                └── excludes
                └── pickFirsts
                └── pickLasts
                └── enableOverride
                └── select
                    └── package
                    └── version
                    └── includePattern
                    └── excludePattern
                    └── include
                    └── exclude
            └── debugSymbol
                └── strip
                └── exclude
            └── headerPath
            └── collectAllLibs
            └── excludeFromHar
            └── excludeSoFromInterfaceHar
            └── excludeSoFromBinXO
        └── napiLibFilterOption
            └── excludes
            └── pickFirsts
            └── pickLasts
            └── enableOverride
        └── arkOptions
            └── buildProfileFields
            └── types
            └── tscConfig
                └── targetESVersion
                └── maxFlowDepth
                └── tsImportSoCheck
            └── autoLazyImport
            └── autoLazyFilter
                └── include
                └── exclude
            └── reExportCheckMode
            └── branchElimination
            └── skipOhModulesLint
            └── expandImportPath
                └── enable
                └── exclude
            └── apPath
            └── hostPGO
        └── strictMode
            └── noExternalImportByPath
            └── useNormalizedOHMUrl
            └── caseSensitiveCheck
            └── duplicateDependencyCheck
            └── harLocalDependencyCheck
            └── enableStrictCheckOHModule
            └── disableStrictCheckPaths
            └── disableSendableCheckRules
            └── strictCheckerOnly
            └── apiCompatibilityCheck
        └── nativeCompiler
        └── removePermissions
            └── name
        └── preloadSystemSo
    └── runtimeOS
    └── arkTSVersion
    └── compileSdkVersion
    └── compatibleSdkVersion
    └── targetSdkVersion
    └── compatibleSdkVersionStage
    └── bundleType
    └── label
    └── icon
    └── versionCode
    └── versionName
    └── buildVersion
    └── resource
        └── directories
    └── output
        └── artifactName
    └── vendor
└── buildModeSet
    └── name
    └── buildOption
└── multiProjects
└── capabilities
    └── bundleName
    └── config
        └── name
        └── capability
        └── subCapabilities
            └── name
            └── capability
modules
└── name
└── srcPath
└── targets
    └── name
    └── applyToProducts
```

## 配置文件字段说明

工程级build-profile.json5文件包含以下字段。

**表1** 工程级build-profile.json5文件字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [app](ide-hvigor-build-profile-app.md#section1140014592111) | 对象 | 必选 | 编译配置信息。 |
| [modules](ide-hvigor-build-profile-app.md#section1961794812219) | 对象数组 | 必选 | 工程中包含的所有模块的信息，数组长度至少为1。 |

## app

app是工程级的编译配置，包含签名、product等信息。

**表2** app

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [signingConfigs](ide-hvigor-build-profile-app.md#section153288223224) | 对象数组 | 可选 | 签名方案信息，可配置多个。 |
| [products](ide-hvigor-build-profile-app.md#section45865492619) | 对象数组 | 可选 | 产品品类，可配置多个。如需配置多个，相关说明请参见[配置多目标产物](ide-customized-multi-targets-and-products.md)章节。 |
| [buildModeSet](ide-hvigor-build-profile-app.md#section137297344398) | 对象数组 | 可选 | 构建模式集合，可配置多个。 |
| multiProjects | 布尔值 | 可选 | 当前工程是否支持多工程构建：   * true：支持。 * false（缺省默认值）：不支持。 |
| [capabilities](ide-hvigor-build-profile-app.md#section1526318211219) | 对象数组 | 可选 | 应用开通的开放能力，具体开通方式请参考[关联注册应用进行签名](ide-signing-auto.md#section6333421192714)。  从DevEco Studio 6.0.0 Beta5版本开始支持。 |

## modules

modules是一个对象数组，用于描述工程中包含的所有模块，数组长度至少为1。模块配置包括名称、路径和target-product关联配置。

**表3** modules

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 模块的名称。该名称需与module.json5文件中的[module.name](module-configuration-file.md#配置文件标签)保持一致。  在FA模型中，对应的文件为config.json。 |
| srcPath | 字符串 | 必选 | 模块的源码路径，为模块根目录相对工程根目录的相对路径，允许模块根目录不在当前工程下，详情请参考[导入/引用模块](ide-import-module.md)。  说明：  当前支持引用其他工程下的HAR和HSP模块。 |
| [targets](ide-hvigor-build-profile-app.md#table1433185416814) | 对象数组 | 可选 | 模块的target信息，用于[定制多目标构建产物](ide-customized-multi-targets-and-products.md)时，配置模块target和应用product之间的关联关系。HAR模块无需配置。 |

**表4** targets

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | target名称，在各个模块级build-profile.json5中的targets字段定义。 |
| applyToProducts | 字符串数组 | 可选 | target关联的product。HAR模块无需配置。 |

modules字段示例：

```json5
{
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": [  
            "default"    // 表示将该模块下的"default" Target打包到"default" Product中
          ]
        }
      ]
    }
  ]
}
```

## signingConfigs

signingConfigs是一个对象数组，用于配置签名方案，可配置多个。

**表5** signingConfigs

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 签名方案的名称，仅支持数字和字母，长度为1~64个字符。 |
| [material](ide-hvigor-build-profile-app.md#table1269413811158) | 对象 | 必选 | 签名方案相关材料，如密码、证书等。  通过**File > Project Structure... > Project > Signing Configs**界面，进行自动签名后，material节点中的各配置项会自动填充。 |
| type | 字符串 | 可选 | 签名类型：   * HarmonyOS * OpenHarmony |

**表6** material

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| storePassword | 字符串 | 必选 | 密钥库密码，以密文形式呈现。 |
| certpath | 字符串 | 必选 | 调试或发布证书文件地址，文件后缀为.cer，支持绝对路径和相对路径，相对路径以工程根目录为起点。 |
| keyAlias | 字符串 | 必选 | 密钥别名信息。 |
| keyPassword | 字符串 | 必选 | 密钥密码，以密文形式呈现。 |
| profile | 字符串 | 必选 | 调试或发布证书Profile文件地址，文件后缀为.p7b，支持绝对路径和相对路径，相对路径以工程根目录为起点。 |
| signAlg | 字符串 | 必选 | 密钥库signAlg参数。当前可配置值SHA256withECDSA。 |
| storeFile | 字符串 | 必选 | 密钥库文件地址，文件后缀为.p12，支持绝对路径和相对路径，相对路径以工程根目录为起点。 |

signingConfigs字段示例：

```json5
// 使用绝对路径
{
  "app": { 
    "signingConfigs": [
      {
        "name": "default",
        "type": "HarmonyOS",
        "material": {  
          "certpath": "D:\\SigningConfig\\debug_hos.cer",
          "storePassword": "************************************",  // 密文形式的密钥库密码
          "keyAlias": "debugKey",
          "keyPassword": "************************************",  // 密文形式的密钥密码
          "profile": "D:\\SigningConfig\\debug_hos.p7b", 
          "signAlg": "SHA256withECDSA",
          "storeFile": "D:\\SigningConfig\\debug_hos.p12"
        }
      }
    ]
  }
}
// 使用相对路径
{
  "app": { 
    "signingConfigs": [
      {
        "name": "default",
        "type": "HarmonyOS",
        "material": {  
          "certpath": "./SigningConfig/debug_hos.cer",
          "storePassword": "************************************",  // 密文形式的密钥库密码
          "keyAlias": "debugKey",
          "keyPassword": "************************************",  // 密文形式的密钥密码
          "profile": "./SigningConfig/debug_hos.p7b", 
          "signAlg": "SHA256withECDSA",
          "storeFile": "./SigningConfig/debug_hos.p12"
        }
      }
    ]
  }
}
```

## products

products是一个对象数组，用于配置产品品类信息，可配置多个，如通用默认版、付费版、免费版等。如需配置多个，相关说明请参见[配置多目标产物](ide-customized-multi-targets-and-products.md)章节。

**表7** products

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 产品的名称，必须存在name为"default"的product。 |
| signingConfig | 字符串 | 可选 | 当前产品品类的签名方案名称，需要在[signingConfigs.name](ide-hvigor-build-profile-app.md#section153288223224)中定义。如果没有配置，默认不签名。 |
| compatibleSdkVersion | 字符串/数值 | 必选 | 标识应用/元服务运行所需兼容的最低SDK版本，应用/元服务不能安装在低于该版本的设备。当前支持的版本参考[所有HarmonyOS版本](../harmonyos-releases/overview-allversion.md)。相关字段与应用兼容性关系参见[应用兼容性说明](../harmonyos-releases/app-compatibility.md)。  从API 26.0.0开始，HarmonyOS和OpenHarmony配置统一，字段类型是字符串，配置示例："compatibleSdkVersion": "26.0.0"。  API 26.0.0之前的版本：   * 运行环境是HarmonyOS时，字段类型是字符串，配置示例："compatibleSdkVersion": "6.1.1(24)"。 * 运行环境是OpenHarmony时，字段类型是数值，配置示例："compatibleSdkVersion": 24。   说明：  构建APP包时，打包工具会对HSP和HAP的compatibleSdkVersion字段进行校验，满足条件的才能打包，具体请参考[打包工具](packing-tool.md)。 |
| targetSdkVersion | 字符串/数值 | 可选 | 标识应用/元服务运行所需目标SDK版本，是系统提供的前向兼容手段。如果新SDK版本中API行为发生变更，将应用/元服务安装到新系统后，可通过该字段提供向前兼容手段，在新系统版本保持老的API行为。  如未配置，默认与compileSdkVersion保持一致。当前支持的版本参考[所有HarmonyOS版本](../harmonyos-releases/overview-allversion.md)。相关标签与应用兼容性关系参见[应用兼容性说明](../harmonyos-releases/app-compatibility.md)。  从API 26.0.0开始，HarmonyOS和OpenHarmony配置统一，字段类型是字符串，配置示例："targetSdkVersion": "26.0.0"。  API 26.0.0之前的版本：   * 运行环境是HarmonyOS时，字段类型是字符串，配置示例："targetSdkVersion": "6.1.1(24)"。 * 运行环境是OpenHarmony时，字段类型是数值，配置示例："targetSdkVersion": 24。   说明：  * 建议配置该字段。 * 构建APP包时，打包工具会对HSP和HAP的targetSdkVersion字段进行校验，满足条件的才能打包，具体请参考[打包工具](packing-tool.md)。 |
| compileSdkVersion | 字符串/数值 | 可选 | 标识编译应用/元服务所使用的SDK版本。当前支持的版本参考[所有HarmonyOS版本](../harmonyos-releases/overview-allversion.md)。相关标签与应用兼容性关系参见[应用兼容性说明](../harmonyos-releases/app-compatibility.md)。  从API 26.0.0开始，HarmonyOS和OpenHarmony配置统一，字段类型是字符串，配置示例："compileSdkVersion": "26.0.0"。  API 26.0.0之前的版本：   * 运行环境是HarmonyOS时，字段类型是字符串，配置示例："compileSdkVersion": "6.1.1(24)"。 * 运行环境是OpenHarmony时，字段类型是数值，配置示例："compileSdkVersion": 24。   说明：  * 运行环境是HarmonyOS时，该字段不需要显性配置，编译时默认使用DevEco Studio内置的SDK版本。如果配置，只能配置为当前DevEco Studio配套的SDK版本，不允许配置为其他SDK版本。 * 运行环境是OpenHarmony时，必须配置该字段。 |
| compatibleSdkVersionStage | 字符串 | 可选 | 当compatibleSdkVersion为API 12时，用于控制不同beta版本的兼容，默认值为beta1，应用/元服务不能安装在低于该版本的设备。  当compatibleSdkVersion高于API 12时，该字段无效，无需配置。  说明：  配置betaX就能生成在对应betaX版本镜像上运行的应用，但是无法使用高于betaX版本的特性，例如在API 12中beta3版本提供的sendable function和lazy import两个特性在配置beta2或beta1时无法正常使用。 |
| bundleName | 字符串 | 可选 | 产品的包名。 |
| [buildOption](ide-hvigor-build-profile-app.md#section14222051575) | 对象 | 可选 | 产品的编译构建配置。 |
| runtimeOS | 字符串 | 可选 | 产品的运行环境：   * HarmonyOS * OpenHarmony |
| arkTSVersion | 字符串 | 可选 | ArkTS语法检查工具的版本号：1.0，1.1。  默认为当前ArkTS语法检查工具支持的最新版本。  仅API 11及以上版本工程支持。 |
| bundleType | 字符串 | 可选 | 包的类型：   * app：应用 * atomicService：元服务 * shared：共享包 |
| label | 字符串 | 可选 | 应用的名称。  说明：  配置products中的label、icon、versionCode、versionName、resource字段后，编译构建时将根据此处的配置替换app.json5中的相关配置，常用于应用和元服务可分可合构建打包场景。 |
| icon | 字符串 | 可选 | 应用的图标。 |
| versionCode | 整型数值 | 可选 | 应用的版本号。 |
| versionName | 字符串 | 可选 | 应用的版本名称。 |
| buildVersion | 字符串 | 可选 | 应用的构建版本号。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| [resource](ide-hvigor-build-profile-app.md#table49010413236) | 对象 | 可选 | 名称和图标对应的资源所在目录。 |
| [output](ide-hvigor-build-profile-app.md#table41925113333) | 对象 | 可选 | 定制产品生成的应用包的配置。 |
| vendor | 字符串 | 可选 | 供应商。 |

**表8** resource

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| directories | 字符串数组 | 必选 | 资源地址路径。 |

**表9** output

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| artifactName | 字符串 | 必选 | 自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。 |

products字段示例：

```json5
{
  "products": [
    {
      "name": "default",
      "signingConfig": "default",
      "bundleName": "com.example.myapplication",
      "compatibleSdkVersion": "26.0.0",
      "targetSdkVersion": "26.0.0",
      "runtimeOS": "HarmonyOS",
      "arkTSVersion": "1.1",
      "bundleType": "app",
      "label": "$string:app_name",
      "icon": "$media:app_background",
      "versionCode": 1000000,
      "versionName": "1.0.0",
      "buildVersion": "1",
      "resource": {
        "directories": [
          "./AppScope/resources"
        ]
      },
      "output": {
        "artifactName": "customizedTargetOutputName-1.0.0"
      },
      "vendor": "customizedProductVendorName",
    }
  ]
}
```

## buildModeSet

buildModeSet是一个对象数组，表示构建模式集合，可配置多个构建模式。

**表10** buildModeSet

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 构建模式名称。默认生成debug，release和test三种模式，支持开发者自定义，其中test模式虽然没有出现在配置文件中，但是利用测试框架开启测试时会自动使用test编译模式。 |
| [buildOption](ide-hvigor-build-profile-app.md#section14222051575) | 对象 | 可选 | 构建模式使用的具体配置信息。 |

## capabilities

capabilities是应用开通的开放能力，具体开通方式请参考[关联注册应用进行签名](ide-signing-auto.md#section6333421192714)。

**表11** capabilities

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| bundleName | 字符串 | 必选 | 当前开放能力归属的包名。 |
| [config](ide-hvigor-build-profile-app.md#section746298142519) | 对象数组 | 必选 | 具体的开放能力配置。 |

### config

**表12** config

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 开放能力名称。 |
| capability | 字符串 | 可选 | 开放能力的唯一标识符。如果subCapabilities不存在，则该值必填。 |
| [subCapabilities](ide-hvigor-build-profile-app.md#table98912388270) | 对象数组 | 可选 | 具体的子开放能力。如果存在子开放能力，则该值必填。 |

**表13** subCapabilities

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 子开放能力名称。 |
| capability | 字符串 | 必选 | 子开放能力的唯一标识符。 |

## buildOption

buildOption是构建使用的具体配置信息，buildModeSet和products下均支持配置buildOption。此外，模块级build-profile.json5中也支持配置buildOption。工程级别buildOption配置会与模块级别的buildOption进行合并，具体合并规则和优先级请参考[合并编译选项规则](ide-hvigor-compilation-options-customizing-guide.md#section1727865610255)。

**表14** buildOption

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [packOptions](ide-hvigor-build-profile-app.md#section03812484215) | 对象 | 可选 | 打包相关配置项。 |
| debuggable | 布尔值 | 可选 | 当前编译产物是否为可调试模式：   * true：可调试。构建的产物包的ets目录下存在sourceMaps.map文件，此文件包含源码映射等信息。 * false：不可调试。   如果未配置debuggable字段，使用release的编译模式时，默认值为false，使用其他编译模式时，默认值为true。 |
| generateSharedTgz | 布尔值 | 可选 | 编译HSP模块时是否生成tgz包。   * true：生成。 * false：不生成。   如果未配置generateSharedTgz，根据debuggable字段决定是否生成tgz包。debuggable为true时，不生成tgz包，debuggable为false时，生成tgz包。  从DevEco Studio 5.1.1 Beta1版本开始支持。  说明：  该字段配置后仅对HSP模块生效。 |
| [resOptions](ide-hvigor-build-profile-app.md#section5494153192911) | 对象 | 可选 | 资源编译配置项。 |
| [externalNativeOptions](ide-hvigor-cpp.md#section0721057575) | 对象 | 可选 | Native编译配置项。 |
| [sourceOption](ide-hvigor-build-profile-app.md#section15753419515) | 对象 | 可选 | 源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。 |
| [nativeLib](ide-hvigor-cpp.md#section15889929155720) | 对象 | 可选 | Native 库（.so）相关配置。 |
| [napiLibFilterOption](ide-hvigor-build-profile-app.md#section1488712919295) | 对象 | 可选 | NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用[nativeLib/filter](ide-hvigor-cpp.md#section15889929155720)。 |
| [arkOptions](ide-hvigor-build-profile-app.md#section111543473013) | 对象 | 可选 | ArkTS 编译配置。 |
| [strictMode](ide-hvigor-build-profile-app.md#section13181758123312) | 对象 | 可选 | 严格模式。 |
| nativeCompiler | 字符串 | 可选 | 指定Native编译时使用的编译器，包括：   * Original（缺省默认值）：原有的OpenHarmony Native编译器。 * BiSheng：使用[毕昇编译器](bisheng-compiler.md)进行Native编译。   说明：  升级到DevEco Studio 5.1.1 Release版本后，新建Native C++工程默认使用毕昇编译器，打开历史工程会弹窗提示，点击**立即体验**可以切换使用毕昇编译器。 |
| [removePermissions](ide-hvigor-build-profile-app.md#section99591415322) | 对象数组 | 可选 | 编译HAP/HSP模块时，指定需要删除的依赖包中的冗余权限，模块本身的权限不会被删除。 |
| preloadSystemSo | 布尔值 | 可选 | 是否收集应用入口所使用的系统so，收集的系统so会在应用冷启动时进行预加载，优化应用的冷启动性能。   * true：收集。 * false（缺省默认值）：不收集。   从DevEco Studio 6.0.0 Beta3版本开始支持。  说明：  * 应用入口：在module.json5的module下配置的srcEntry标签，或者在module.json5的abilities中配置了具有入口能力的skills标签（即配置了entity.system.home和ohos.want.action.home）。 * 仅支持HAP和字节码HAR，编译HAP时，被应用入口import的文件或者源码HAR，如果存在系统so，也会被收集；字节码HAR在被集成时，系统so会被合并到HAP中。 * 变量动态import不支持收集。 * preloadSystemSo和hvigor-config.json5文件的ohos.arkCompile.singleFileEmit字段互斥，不支持同时设置为true。 |

### packOptions

packOptions是打包相关配置项。

**表15** packOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| buildAppSkipSignHap | 布尔值 | 可选 | 构建APP时，是否跳过生成签名HAP：   * true：跳过，即不生成签名HAP。 * false（缺省默认值）：不跳过，即生成签名HAP。   编译构建APP时，无需生成签名HAP，可将此参数修改为true，从而提升编译构建性能。 |
| fastBuildApp | 布尔值 | 可选 | 构建APP时，是否在模块下生成HAP/HSP产物。   * true：不生成HAP/HSP产物，直接生成APP产物，可加快构建速度。 * false（缺省默认值）：生成HAP/HSP产物，同时生成APP产物。   说明：  * 当fastBuildApp配置为true时，无论buildAppSkipSignHap配置为true还是false，都不会生成HAP产物。 * 当fastBuildApp配置为false时，是否生成HAP产物，以buildAppSkipSignHap配置为准。 |
| enableSourceCodeCheck | 布尔值 | 可选 | 是否检查HAP/HSP/HAR包（不包括未开启混淆的源码HAR）产物中的源码文件，如果检查，当产物中存在源码文件时，编译时会进行Warning提示。   * true（缺省默认值）：检查。 * false：不检查。   从DevEco Studio 6.0.0 Beta3版本开始支持。  说明：  * 源码文件是指包含以下后缀的文件：['.c', '.h', '.cpp', '.cs', '.java', '.rs', '.py', '.go', '.ets', '.js', '.ts']。 * [release模式编译的混淆源码har包](ide-hvigor-build-har.md#section19788284410)中的'.js', '.ts'和'.d.ets'文件不会被检查。 * resources目录下的'.js'文件不会被检查。 |
| deduplicateHar | 布尔值 | 可选 | 构建APP/HAP/HSP时，当HAP/HSP依赖相同的HAR时（包括HAP和HSP依赖相同的HAR，多个HSP依赖相同的HAR），是否去除HSP中重复的HAR，减少包体积。   * true：去除，HAR仅会打包到HAP中，同时需要配置以下字段。   + 工程级build-profile.json5中配置[idDefinedFilePath](ide-hvigor-build-profile-app.md#section5494153192911)。   + 工程级build-profile.json5的useNormalizedOHMUrl配置为true。   + [module.json5](module-configuration-file.md)的libIsolation配置为false。 * false（缺省默认值）：不去除，HAR会打包到每个HAP/HSP中。   说明：  * 从DevEco Studio 6.0.1 Beta1版本开始支持，并且设备系统需要升级到6.0.1(21)，工程级build-profile.json5的compatibleSdkVersion需要配置为6.0.1(21)。 * 多个HSP依赖相同的HAR时，依赖HSP的HAP需要显式配置依赖该HAR。 * 仅支持本地HSP模块，不支持已打包的HSP包。 * 不支持去除重复HAR的场景：   + 一个应用包含多个HAP时   + 单独运行或调试HSP   + 仪器测试和本地单元测试   + 预览场景 |
| appWithSignedPkg | 布尔值 | 可选 | 构建APP时，除了默认的app包之外，是否额外生成产物名称带all的app包（xxx-all-unsigned.app和xxx-all-signed.app），app包里的hap和hsp都是签名的包。   * true：除了默认的app包之外，额外生成产物名称带all的app包，包里的hap和hsp都是签名的包。 * false（缺省默认值）：只生成默认的app包，包里的hap和hsp都是未签名的包。   从DevEco Studio 6.0.2 Beta1版本开始支持。  说明：  要生成xxx-all-unsigned.app和xxx-all-signed.app，除了appWithSignedPkg配置为true之外，需要确保已配置签名材料，并且hvigor-config.json5中的enableSignTask未配置为false。 |
| enableIncrementalSoCompress | 布尔值 | 可选 | 构建HAP/HSP时，如果工程中包含大量so并开启了压缩so体积的配置开关（module.json5的compressNativeLibs或hvigor-config.json5的ohos.pack.compressLevel），可以开启此开关复用上一次构建已经压缩好的so，加快打包速度。   * true：开启增量压缩，如果so包内容未改变，HAP/HSP将会复用已经压缩好的so包。 * false（缺省默认值）：不开启增量压缩，每次构建对所有so重新进行压缩。   从DevEco Studio 6.1.0 Beta1版本开始支持。 |
| deduplicateSo | 布尔值 | 可选 | 构建APP时，是否去除HAP和HSP中重复的so文件，以减小APP包体积。   * true：去除，so文件只保留一份，并且随机打包在HAP或HSP中。 * false（缺省默认值）：不去除。   从26.0.0版本开始支持。  说明：  OpenHarmony工程不支持配置此字段。 |

```json5
"buildOption": {
  "packOptions": {
    "buildAppSkipSignHap": true,
    "fastBuildApp": false,
  }
}
```

### resOptions

resOptions是资源编译配置项。

**表16** resOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [compression](ide-hvigor-build-profile-app.md#section2095319147103) | 对象 | 可选 | 对工程预置图片资源进行纹理压缩的编译配置参数。 |
| resCompileThreads | 整型数值 | 可选 | 资源编译的线程数量 ，最小为1，最大为主机的CPU核数。  该字段从DevEco Studio 5.1.0 Release版本开始支持。 |
| [copyCodeResource](ide-hvigor-build-profile-app.md#table263894423012) | 对象 | 可选 | 对模块的src/main/ets目录下的资源文件（非源码文件）拷贝的编译配置参数。  说明：  该字段对[不开启混淆的源码HAR](ide-hvigor-build-har.md#section197792874110)不生效。 |
| ignoreResourcePattern | 字符串数组 | 可选 | 根据glob语法，对资源目录resources或开发者自定义的资源目录下的文件/文件夹名称进行过滤，匹配到的文件不会被打包到产物中。  从DevEco Studio 5.1.1 Beta1版本开始支持。  说明：  * 如果规则中带有路径（例如./src/main/a.png），该规则不生效。 * 如果未配置该字段，打包HAP/HSP时存在默认的过滤规则：默认不打包.git、.svn、.scc、.ds\_store、desktop.ini、picasa.ini、cvs、thumbs.db以及以.开头的隐藏文件/目录和以~结尾的文件。 * 配置该字段后，会覆盖默认的过滤规则；如果字段配置为空数组，则不应用任何过滤规则，即全部资源都打包。 |
| excludeHarRes | 字符串数组 | 可选 | 编译HAP/HSP模块时，指定不参与资源编译的三方HAR包的包名，配置后，依赖HAR包中的资源不会被打包到产物中，支持直接依赖和间接依赖。  从DevEco Studio 6.0.0 Beta2版本开始支持。  说明：  该字段仅对编译HAP/HSP生效。 |
| includeAppScopeRes | 布尔值 | 可选 | 编译HSP时，是否将AppScope目录下的资源打包到产物中。   * true（缺省默认值）：打包。 * false：不打包。   从DevEco Studio 6.0.0 Beta2版本开始支持。  说明：  * 该字段仅对HSP模块生效。 * 配置为false后，app.json5的icon和label字段不再对HSP模块生效。 |
| idDefinedFilePath | 字符串 | 可选 | 使用HAR包去重能力时（即工程级build-profile.json5的deduplicateHar配置为true），指定用户自定义的json5文件路径，用于固定资源id，支持绝对/相对路径，文件示例如下。  去除重复的HAR包后，HAR仅会打包到HAP中，因此HSP需要通过这些固定的id，跨包访问HAP中的资源。  从DevEco Studio 6.0.1 Beta1版本开始支持。 |

idDefinedFilePath指定的固定资源id的json5文件示例：

```json5
// id-config.json5
{
  "record": [{
    "type": "string",        // 资源类型，推荐应用内所有的资源都固定id
    "name": "app_name",      // 资源名称
    "id": "0x01000000"       // 用户自定义的资源id，仅支持十六进制，支持的id范围是[0x01000000, 0x06FFFFFF]，[0x08000000, 0xFFFFFFFF]
  }, {
    "type": "float",
    "name": "float1",
    "id": "0x01000001"
  }, {
    "type": "media",
    "name": "background",
    "id": "0x01000002"
  }, {
    "type": "profile",
    "name": "profile1",
    "id": "0x01000003"
  }]
}
```

**表17** copyCodeResource

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| enable | 布尔值 | 可选 | 是否将src/main/ets目录下的资源文件（.ets/.ts/.js以外的其他文件）打包到产物中。   * true（缺省默认值）：打包。 * false：不打包。 |
| includes | 字符串数组 | 可选 | * 当enable为true时，用于指定打包的资源文件，其他资源文件均不会打包到产物中，支持glob语法，以"\*\*/"开头。 * 当enable为false时，includes不生效。   从DevEco Studio 6.0.0 Beta2版本开始支持。  说明：  includes和excludes互斥，只能配置一个。 |
| excludes | 字符串数组 | 可选 | * 当enable为true时，用于指定不打包的资源文件，其他资源文件均会打包到产物中，支持glob语法，以"\*\*/"开头。 * 当enable为false时，excludes不生效。 |

**注意** 

* 模块的src/main/ets目录下，编译时仅处理.ets/.ts/.js文件，其他文件会被当作资源文件打包进产物中，不会进行混淆或加密，如需过滤请配置excludes字段。
* 请勿将源码等文件放在以.开头的系统隐藏目录中，可能会导致过滤规则失效，会将src/main/ets目录下的所有文件作为资源文件打包进产物中，不会进行混淆或加密。

resOptions字段示例：

```json5
"buildOption": {
  "resOptions": {
    "resCompileThreads": 2,
    "copyCodeResource": {
      "enable": true,
      "excludes": ['**/entry/src/main/ets/component/big_picture.png', '**/*.yml', '**/subDir/**'],   // includes字段配置方式相同
    },
    "ignoreResourcePattern": ['*.png' ,'abc.json'],
    "excludeHarRes": ['har'],
    "idDefinedFilePath": "./id-config.json5",    // 支持绝对路径和相对路径
  }
}
```

### sourceOption

sourceOption是源码相关配置，使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。

**表18** sourceOption

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| workers | 字符串数组 | 可选 | 指定使用node.js工作器的JS/TS源代码，源代码在构建过程中单独处理。 |

sourceOption字段示例：

```json5
"buildOption": {
  "sourceOption": {
    "workers": [
      "./src/main/ets/common/constants/CommonConstants.ets"
    ]
  }
}
```

### napiLibFilterOption

napiLibFilterOption是NAPI库（.so）文件的筛选选项，字段已废弃，不建议使用，推荐使用[nativeLib/filter](ide-hvigor-cpp.md#section15889929155720)。

**表19** napiLibFilterOption

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| excludes | 字符串数组 | 可选 | 排除的.so文件。罗列的NAPI库将不会被打包。 |
| pickFirsts | 字符串数组 | 可选 | 按照.so文件的优先级顺序，打包最高优先级的.so文件。 |
| pickLasts | 字符串数组 | 可选 | 按照.so文件的优先级顺序，打包最低优先级的.so文件。 |
| enableOverride | 布尔值 | 可选 | 是否允许当.so文件重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件：   * true：允许。 * false（缺省默认值）：不允许。 |

### arkOptions

arkOptions是ArkTS编译配置。

**表20** arkOptions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [buildProfileFields](ide-hvigor-get-build-profile-para.md) | 对象 | 可选 | 用于ArkTS的构建配置。自定义类型，key可由数字、英文、下划线、中划线组成，value类型仅支持string、number、boolean。 |
| [types](arkoptions-guide.md#types) | 字符串数组 | 可选 | 自定义类型，可配置包名或d.ts/d.ets文件路径。 |
| [tscConfig](ide-hvigor-build-profile-app.md#table1714014154115) | 对象 | 可选 | 与编译TS语法相关的配置选项。 |
| autoLazyImport | 布尔值 | 可选 | 编译时是否自动将符合lazy-import语法规范的import语句添加"lazy"关键字。仅支持在源码中添加"lazy"关键字，不包含依赖的字节码HAR包或HSP。关于lazy-import的介绍及相关影响请参考[延迟加载（lazy import）](arkts-lazy-import.md)。   * true：添加。 * false（缺省默认值）：不添加。   说明：  * 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。 * 仅支持Stage模型。 |
| [autoLazyFilter](ide-hvigor-build-profile-app.md#table1551310818378) | 对象 | 可选 | 自定义添加"lazy"关键字的模块，仅当build-profile.json5中的autoLazyImport或hvigor-config.json5中的ohos.defaults.autoLazyImport配置为true时生效。  从DevEco Studio 6.0.1 Beta1版本开始支持。 |
| reExportCheckMode | 字符串 | 可选 | 针对以下场景，编译时是否进行拦截报错：使用lazy import导入的变量，在同文件中被再次导出。   * noCheck（缺省默认值）：不检查，不报错。 * compatible：兼容模式，报Warning。 * strict：严格模式，报Error。   该字段从DevEco Studio 5.0.5 Release版本开始支持。 |
| branchElimination | 布尔值 | 可选 | 是否启用代码分支裁剪，减少编译产物大小，开启后，在release编译模式下，不会被执行到的代码分支会被裁剪掉，示例请参考[branchElimination示例](ide-hvigor-build-profile-app.md#li12224142193612)。   * true：启用（将导致使用"ApplyChanges"功能时，对const声明的常量的值进行的修改可能不生效）。 * false（缺省默认值）：不启用。   说明：  * 仅支持API 11及以上的Stage模型。 * HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。 * 仅支持const声明的bool类型常量和const声明的string/number类型常量的判断表达式。 * 不支持间接导入，例如A文件中定义const变量A1，B文件导入A1，导出B1，ets导入B1进行判断，无法进行裁剪。 |
| skipOhModulesLint | 布尔值 | 可选 | 是否跳过工程中oh\_modules目录的[ArkTS规则检查](typescript-to-arkts-migration-guide.md)。从DevEco Studio 6.0.0 Beta1版本开始支持。   * true：跳过。 * false（缺省默认值）：不跳过。 |
| [expandImportPath](ide-hvigor-build-profile-app.md#table81640115915) | 对象 | 可选 | import路径展开相关配置选项。  从DevEco Studio 6.0.0 Beta3版本开始支持。 |
| apPath | 字符串 | 可选 | 说明：  API 11及以上版本不再支持，即该字段配置后不再生效。  应用热点信息文件路径。 |
| hostPGO | 布尔值 | 可选 | 是否启用配置文件引导优化功能：   * true：启用。 * false（缺省默认值）：不启用。   从API 10开始废弃，由于partial模式可能存在兼容性问题，请使用Target AOT能力，不建议使用Host AOT。 |

* branchElimination字段配置为true时，代码分支的裁剪情况示例如下：

  ```ts
  // 编译生成的BuildProfile文件
  export const DEBUG = false;
  export const VERSION_CODE = 100;
  // 开发者自定义的ets文件
  import { DEBUG } from 'BuildProfile';
  import { VERSION_CODE } from 'BuildProfile';
  if (DEBUG)
    {XXX} // 该分支会被裁剪掉
  else
    {XXX}
  if (VERSION_CODE){XXX} // 该语法发生了类型转换，不支持代码裁剪。
  if (VERSION_CODE === 100){XXX} // 若需要裁剪代码，使用该方式，显式指定判断条件为boolean类型。
  ```

**表21** tscConfig

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| targetESVersion | 字符串 | 可选 | 指定TS语法编译产物的目标运行时EcmaScript版本，包括：   * ES2017 * ES2021（缺省默认值）。 |
| maxFlowDepth | 整型数值 | 可选 | 设置最大控制流递归深度，范围为[2000,65535]，默认为2000。  该字段从DevEco Studio 5.1.0 Release版本开始支持。  说明：  maxFlowDepth不支持动态修改，即在hvigorfile.ts/hvigorconfig.ts文件中，不支持通过[setBuildProfileOpt](ide-build-expanding-context.md#section16692151412211)方法设置maxFlowDepth。 |
| tsImportSoCheck | 布尔值 | 可选 | 在.ts文件导入.so文件中的符号，编译时是否对导入的符号进行类型解析。   * false（缺省默认值）：不解析，导入的符号在使用时默认是any类型，可能会导致编译失败。 * true：解析，.ts文件可以获取到符号的准确类型并且编译成功。   从26.0.0版本开始支持。 |

**表22** autoLazyFilter

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| include | 字符串数组 | 可选 | * 当autoLazyImport或ohos.defaults.autoLazyImport为true时，指定自动添加"lazy"关键字的包名（即oh-package.json5中的name），其他包不会添加"lazy"关键字，支持正则语法。 * 当autoLazyImport为false时，include不生效。   说明：  * include和exclude互斥，只能配置一个。 * include不支持配置空数组或空字符串，至少配置一个包名，并且包名不能重复。 |
| exclude | 字符串数组 | 可选 | * 当autoLazyImport或ohos.defaults.autoLazyImport为true时，指定不添加"lazy"关键字的包名，其他包都会添加"lazy"关键字，支持正则语法。 * 当autoLazyImport为false时，exclude不生效。   说明：  * include和exclude互斥，只能配置一个。 * exclude不支持配置空数组或空字符串，至少配置一个包名，并且包名不能重复。 |

**表23** expandImportPath

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| enable | 布尔值 | 可选 | 是否启用import路径展开，启用后可以提升应用的运行时性能。关于import路径展开的原理及开启后的副作用请参考[通过import路径展开优化性能](arkts-module-side-effects.md#通过import路径展开优化性能)。   * true：启用。 * false（缺省默认值）：不启用。   说明：  * import XXX from 'A'，A必须为本地HAR模块，并且仅当A为包名时支持进行展开，A为相对路径或包名+路径都不支持展开。 * HAR模块单独编译时不生效。 |
| exclude | 字符串数组 | 可选 | 配置oh-package.json5中的依赖别名，用于指定不展开import语句的依赖，仅支持本地HAR模块。 |

arkOptions字段示例：

```json5
"buildOption": {
  "arkOptions": {
    "buildProfileFields": {
      "targetData": "TargetData",
      "data": "DataTargetDefault"
    },
    "tscConfig": {
      "targetESVersion": "ES2021",
      "maxFlowDepth": 3000,
    },
    "autoLazyImport": true,
    "autoLazyFilter": {
      "include": ['entry']
    },
    "reExportCheckMode": "compatible",
    "branchElimination": true,
    "expandImportPath": {
      "enable": true,
      "exclude": ['localhar']
    },
  }
}
```

### strictMode

strictMode用于定义严格模式。

**表24** strictMode

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| noExternalImportByPath | 布尔值 | 可选 | 是否严格检查绝对路径导入方式和相对路径跨模块导入方式。   * true：严格检查。 * false：不严格检查。   说明：  从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当工程级build-profile.json5中useNormalizedOHMUrl配置为true时，noExternalImportByPath缺省默认值为true；当useNormalizedOHMUrl配置为false时，noExternalImportByPath缺省默认值为false。 |
| useNormalizedOHMUrl | 布尔值 | 可选 | 是否使用标准化的OHMUrl（OHMUrl的定义参考以下说明）格式，标准化的OHMUrl统一了原有OHMUrl的格式。使用集成态HSP和[字节码HAR](ide-hvigor-build-har.md#section16598338112415)需使用标准化的OHMUrl格式。   * true：使用标准化的OHMUrl格式。 * false（缺省默认值）：不使用标准化的OHMUrl格式。   说明：  * 从API 12开始支持。 * 一个ets文件在编译后会成为安装包的一部分，这个ets文件对应的字节码称为一个字节码段，OHMUrl是用来定位一个字节码段的标识。 * 若工程引用了HAR/HSP，需确保工程的useNormalizedOHMUrl配置和HAR/HSP的useNormalizedOHMUrl配置保持一致，同时配置为true或false。 * 当useNormalizedOHMUrl设置为true时，可能对本地源码HAR的混淆产生影响，具体请参考[本地源码HAR包](source-obfuscation-practice.md#本地源码har包)。 * 当useNormalizedOHMUrl设置为true时，文件路径中不能包含"&"字符。 * 从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当useNormalizedOHMUrl设置为true时，不允许通过相对路径跨模块或绝对路径导入文件，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致，具体的适配指导请参考[变更说明](../harmonyos-releases/ide-changelog-500-release.md#section1130320228353)。 |
| caseSensitiveCheck | 布尔值 | 可选 | 导入文件是否严格校验大小写，支持相对路径和软链接。   * true：严格校验。 * false（缺省默认值）：不严格校验。 |
| duplicateDependencyCheck | 布尔值 | 可选 | 是否校验本地HSP模块有无依赖相同的HAR。仅在Build App(s)起效。   * true：如果本地HSP模块依赖了相同的HAR（包括本地/远程、直接/间接），则编译报错。（注意：当依赖链中存在远程HSP，则该远程HSP及其依赖链不参与校验）。 * false（缺省默认值）：不启用校验。 |
| harLocalDependencyCheck | 布尔值 | 可选 | 是否对HAR产物启用本地依赖校验。   * true：如果oh-package.json5中的dependencies、dynamicDependencies存在本地依赖，则编译报错。 * false（缺省默认值）：不启用校验。   说明：  除HAR模块外，HSP模块编译时也会生成HAR产物，该配置同样生效。 |
| enableStrictCheckOHModule | 布尔值 | 可选 | 调用远程HAR/HSP包中的方法时，是否严格校验传入参数的类型。   * true：严格校验，如果参数类型是undefined/null，报Error错误。 * false（缺省默认值）：不严格校验，如果参数类型是undefined/null，报Warning告警。   从DevEco Studio 6.0.1 Beta1版本开始支持。 |
| disableStrictCheckPaths | 字符串数组 | 可选 | 指定不需要严格检查的三方库目录名称，未配置时，默认是['node\_modules', 'build', '.preview', 'oh\_modules']。  如果同时开启strictMode下的enableStrictCheckOHModule，disableStrictCheckPaths数组中的oh\_modules会被移除，即oh\_modules目录要严格检查。  从26.0.0版本开始支持。 |
| disableSendableCheckRules | 字符串数组 | 可选 | 指定需要关闭校验的Sendable规则，当前仅支持配置"arkts-sendable-class-decorator"，表示支持在Sendable class上使用自定义装饰器。具体检查规则请参考[Sendable类和Sendable函数禁止使用除@Sendable外的装饰器](sendable-constraints.md#sendable类和sendable函数禁止使用除sendable外的装饰器)。  从DevEco Studio 6.0.2 Beta1版本开始支持。 |
| strictCheckerOnly | 布尔值 | 可选 | 是否对.ets文件仅执行严格语法检查。   * false（缺省默认值）：对.ets文件执行两次语法检查，一次非严格语法检查和一次严格语法检查，两次语法检查结果合并输出。 * true：对.ets文件仅执行一次严格语法检查，跳过非严格语法检查，可以减少端到端编译时间，提升编译性能。   从DevEco Studio 6.1.1 Release版本开始支持。 说明：  开启strictCheckerOnly选项之后，由于工具链类型校验能力增强，因此对存量代码进行更严格的检查，可能需要开发者进行少量适配，参考[strictCheckerOnly适配示例](ide-hvigor-build-profile-app.md#li25608201227)。 |
| apiCompatibilityCheck | 字符串 | 可选 | 设置ArkTS API兼容性检测级别。   * warn（缺省默认值）：如果调用的ArkTS API 的起始版本高于工程的compatibleSdkVersion，构建时会报Warning告警。 * error：如果调用的ArkTS API 的起始版本高于工程的compatibleSdkVersion，构建时会报Error错误。   从26.0.0版本开始支持。 |

* 在严格模式下（即strictCheckerOnly开关开启），存量代码中调用settings.getValueSync类似接口时会出现"This API is used only in FA Mode, but the current Mode is Stage."报错。严格模式下工具链类型校验能力增强，undefined类型变量无法直接匹配非undefined类型的函数参数，导致无法命中预期的重载声明，预期匹配[settings.getValueSync](../harmonyos-references/js-apis-settings.md#settingsgetvaluesync11)，实际匹配[settings.getValueSync](../harmonyos-references/js-apis-settings.md#settingsgetvaluesyncdeprecated)(deprecated)。

  **解决方案：**可通过为变量添加非空断言（!），告知编译器该变量一定存在值，使编译时能够正确匹配到目标函数重载。

  ```screen
  // 在这里的调用中，context可能是undefined，需要为参数（context）添加非空断言（!）
  let value = settings.getValueSync(context!, settings.display.SCREEN_BRIGHTNESS_STATUS, '10');
  ```

strictMode字段示例：

```json5
"buildOption": {
  "strictMode": {
    "useNormalizedOHMUrl": true,
    "caseSensitiveCheck": true,
    "disableStrictCheckPaths": ["pages"],
    "disableSendableCheckRules": ["arkts-sendable-class-decorator"],
    "apiCompatibilityCheck": "error",
  }
}
```

### removePermissions

removePermissions是一个对象数组，用于编译HAP/HSP模块时，指定需要删除的依赖包中的冗余权限，模块本身的权限不会被删除。

**表25** removePermissions

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 待删除的权限名称，需要包含在依赖包的module.json的requestPermissions中。 |

removePermissions字段示例：

```json5
"buildOption": {
  "removePermissions": [
    {
      "name": "ohos.permission.ABILITY_BACKGROUND_COMMUNICATION"
    },
    {
      "name": "ohos.permission.ACCELEROMETER"
    }
  ]
}
```

## compression

compression是对工程预置图片资源进行纹理压缩的编译配置参数。

**表26** compression

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [media](ide-hvigor-build-profile-app.md#section1915545641714) | 对象 | 可选 | 对资源目录下media目录的图片进行纹理压缩的配置参数。 |
| [filters](ide-hvigor-build-profile-app.md#section185719543186) | 对象数组 | 可选 | 文件过滤配置参数。  说明：  编译过程中会依次遍历图片文件，并与filters条件进行匹配，一旦匹配成功，则完成该图片的处理。当工程级和模块级同时配置时，先按照模块级的过滤条件匹配，一旦匹配成功，则忽略工程级的过滤条件；如果模块级的没有匹配成功，继续按工程级的条件进行匹配。 |

### media

media是对资源目录下media目录的图片进行纹理压缩的配置参数。

**表27** media

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| enable | 布尔值 | 可选 | 是否对media图片启用纹理压缩。   * true：启用。 * false（缺省默认值）：不启用。   说明：  * 在linux系统的构建场景下，请确认系统环境已[安装libGL1库](ide-command-line-building-app.md#section1478651816216)。 * 对图片进行纹理压缩会改变文件名称和内容，在[分层图标](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#layereddrawabledescriptor)以及二次编辑的场景下会引起图片显示异常，请进一步使用filters排除掉这部分文件。 |

### filters

filters是文件过滤配置参数。

**表28** filters

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| [method](ide-hvigor-build-profile-app.md#table1568916396220) | 对象 | 必选 | 纹理压缩的方式。 |
| [files](ide-hvigor-build-profile-app.md#table19762944112414) | 对象 | 可选 | 指定用来参与压缩的文件，与exclude字段配合使用。 |
| [exclude](ide-hvigor-build-profile-app.md#table6219104952519) | 对象 | 可选 | 从files中剔除掉不需要压缩的文件。 |

**表29** method

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| type | 字符串 | 必选 | 转换类型。   * astc（Adaptive Scalable Texture Compression）：自适应可变纹理压缩，一种对GPU友好的纹理格式，可在设备侧更快地显示，有更少的内存占用。 * sut（SUper compression for Texture） ：纹理超压缩，可在设备侧更快地显示，有更少的内存占用，相比astc具备更大压缩率和更少ROM占用。 |
| blocks | 字符串 | 必选 | astc/sut转换类型的扩展参数，决定画质和压缩率，当前仅支持"4x4"。 |

**表30** files

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| path | 字符串数组 | 可选 | 指定“按路径匹配”的过滤条件，符合glob规范，格式为相对路径。 |
| size | 二维数组 | 可选 | 指定“按大小匹配”的过滤条件，格式为[min,max]，闭区间，表示大小从min到max之间的文件。   * 每个数值可以填数字、字符串或字符串中带单位（大小写均可），如[0, '1k']。 * 单位K/k=1024，M/m=1024\*1024，G/g=1024\*1024\*1024，T/t=1024\*1024\*1024\*1024。 * 区间最大值可省略，表示无限大，如['3K']。 |
| resolution | 二维数组 | 可选 | 指定“按分辨率匹配”的过滤条件，配置示例：   ```json5 resolution:[   [     { width:32, height:32 },  // 最小宽高     { width:64, height:64 },  // 最大宽高   ],  // 分辨率在32*32到64*64之间的图片   [     { width:200, height:200 }, // 最小宽高     // 此处第2个不填表示最大宽高是无限大   ],  // 分辨率大于200*200的图片 ] ```  * width和height只能是数字。 * 最大宽高可以省略，表示无限大。 |

**表31** exclude

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| path | 字符串数组 | 可选 | 同files/path。 |
| size | 二维数组 | 可选 | 同files/size。 |
| resolution | 二维数组 | 可选 | 同files/resolution。 |

compression字段示例：

```json5
"buildOption": {
  "resOptions": {
    "compression": {
      "media": {
        "enable": true // 是否对media图片启用纹理压缩
      },
      // 纹理压缩文件过滤，非必填，不填会压缩资源目录中的所有图片
      "filters": [
        {
          "method": {
            "type": "sut", // 转换类型
            "blocks": "4x4" // 转换类型的扩展参数
          },
          // 指定用来参与压缩的文件，需要满足所有条件且不被exclude过滤的文件才会参与压缩
          "files": {
            "path": ["./**/*"], // 指定资源目录中的所有文件
            "size": [[0, '10k']], // 指定大小10k以下的文件
            // 指定分辨率小于2048*2048的图片
            "resolution": [
              [
                { "width": 0, "height": 0 }, // 最小宽高
                { "width": 2048, "height": 2048 } // 最大宽高
              ]
            ]
          },
          // 从files中剔除掉不需要压缩的文件，需要满足所有过滤条件的文件才会被剔除
          "exclude": {
            "path": ["./**/*.jpg"], // 过滤所有jpg文件
            "size": [[0, '1k']], // 过滤大小1k以下的文件
            // 过滤分辨率小于1024*1024的图片
            "resolution": [
              [
                { "width": 0, "height": 0 }, // 最小宽高
                { "width": 1024, "height": 1024 } // 最大宽高
              ]
            ]
          }
        }
      ]
    }
  }
}
```
