---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har
title: 构建HAR
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 配置构建流程 > 构建HAR
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1e6b3ccbe000f9aecaf0f12afbeb9b62445762bb36b115afe995a1afe0582231
---

构建模式：DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。

产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。

从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，默认构建字节码HAR，用于提升发布产物的安全性。

## 使用约束

HAR自身的构建不建议引用本地模块，可能导致其他模块依赖该HAR包时安装失败，如果安装失败，需要在工程级oh-package.json5中配置[overrides](ide-oh-package-json5.md#section13977152601510)。

## 创建模块

1. 新建工程时选择API 10及以上的Stage模型，工程创建完成后，新建“Static Library”模块。模块创建方法可参考[添加模块](ide-add-new-module.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/pZPLULptSwSUSK7PsAuv4A/zh-cn_image_0000002808886669.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=51ED393918F23A7F7A35AB1024B94F52D63CE6735D16DC59BCA95D535FC436C3)
2. 编写代码。

   ```txt
     library  // HAR根目录
     ├─libs  // 存放用户自定义引用的Native库，一般为.so文件
     └─src
     │   └─main
     │     ├─cpp
     │     │  ├─types  // 定义Native API对外暴露的接口  
     │     │  │  └─liblibrary  
     │     │  │      ├─index.d.ts
     │     │  │      └─oh-package.json5 
     │     │  ├─CMakeLists.txt  // CMake配置文件  
     │     │  └─napi_init.cpp  // C++源码文件
     │     └─ets  // ArkTS源码目录
     │     │  └─components
     │     │     └─MainPage.ets
     │     ├─resources  // 资源目录，用于存放资源文件，如图片、多媒体、字符串等  
     │     └─module.json5  // 模块配置文件，包含当前HAR的配置信息  
     ├─build-profile.json5  // Hvigor编译构建所需的配置文件，包含编译选项
     ├─hvigorfile.ts  // Hvigor构建脚本文件，包含构建当前模块的插件、自定义任务等
     ├─Index.ets  // HAR的入口文件，一般作为出口定义HAR对外提供的函数、组件等   
     └─oh-package.json5  // HAR的描述文件，定义HAR的基本信息、依赖项等
   ```
3. 在oh-package.json5中“main”字段定义导出文件入口。若不设置“main”字段，默认以当前目录下Index.ets为入口文件，依据.ets>.ts>.js的顺序依次检索。以将ets/components/MainPage.ets文件设置为入口文件为例：

   ```ts
   {
     "main": "./src/main/ets/components/MainPage.ets",
   }
   ```

## 字节码HAR

默认产物是包含字节码的HAR包，其中包含abc字节码、资源文件、配置文件、readme、changelog声明文件、license证书文件，提升发布到ohpm中心仓产物的安全性。

字节码HAR包中包含的是编译后的abc字节码，当字节码HAR被其他应用模块(HAP/HSP)依赖时，执行应用模块的编译构建，不需要再对依赖的HAR进行语法检查和编译等操作，相比源码HAR，可以有效提升应用模块的编译构建效率，提高安全性，降低代码泄露的风险。

**说明** 

由于构建字节码HAR需要生成二进制的格式，所以单独构建字节码HAR会比构建非字节码HAR耗时更多。

### 收益

* 字节码HAR可以降低代码泄露的风险，增加反编译获取代码逻辑的难度。

* 采用ArkTS/TS语言开发的字节码HAR，被HAP/HSP集成时，可以减少语法检查、转换的耗时，提高构建性能。
* 字节码HAR可以减少编译时node的进程占用，有效降低内存占用。
* 通过其他代码生成工具生成的js语言HAR包，编译构建成字节码HAR后，被HAP/HSP集成时，可以减少编译阶段处理的文件和代码数量，降低内存，提高构建性能。

### 使用场景

从功能上来说所有的源码HAR包都可以按照任意顺序切换成字节码HAR。但是由于字节码HAR编译和集成的特点，按照推荐场景或顺序来逐步切换字节码HAR可能会获得比较好的性能、内存收益。以下场景中推荐切换使用字节码HAR：

* 适用于SDK厂商对外提供SDK，以及高安全的场景，字节码HAR可以降低源码泄露的风险。
* 采用multi-repo的开发模式，在被主工程合并集成时，所有依赖的HAR均可以发布成字节码HAR，从而提高主HAP的构建效率。
* 采用mono-repo的开发模式，工程中含有单个代码文件较大，或通过代码生成工具生成的代码量较大的ArkTS/TS/JS 的二方、三方SDK(HAR包)时，可考虑将这些HAR包构建成字节码HAR。
* 对内存要求较高的场景，可以通过切换字节码HAR，降低内存的占用。
* 通过ArkTS/TS/JS编写的HAR，且在依赖链条中处于较为底层的叶子节点，含有较少的源码依赖时，切换为字节码HAR会有较好的收益。

### 约束条件

* 字节码HAR使用的依赖需要配置在本模块的oh-package.json5的dependencies或dynamicDependencies中，如果不配置，后续字节码HAR被集成时可能会出现运行时异常。如果出现异常，部分场景可通过在hvigor-config.json5中配置ohos.byteCodeHar.integratedOptimization后重新编译，具体请参考[编译行为差异说明](ide-hvigor-dependencies.md#section957371853712)。
* 字节码HAR的oh-package.json5中配置的依赖名和依赖包的包名（即包内oh-package.json5中的name）需要保持一致。
* 依赖字节码HAR包时，该工程的build-profile.json5中的[useNormalizedOHMUrl](ide-hvigor-build-profile-app.md#section13181758123312)必须设置为true。
* HAP/HSP/HAR依赖字节码HAR包时，HAP/HSP/HAR的oh-package.json5中配置的依赖名和字节码HAR包的oh-package.json5中的name需要保持一致。
* HAP/HSP/HAR代码中import使用字节码HAR包时，`import xxx from 'yyy'`的依赖名yyy要和本模块oh-package.json5中配置的依赖名保持一致（包括大小写）。
* 依赖字节码HAR包时，字节码HAR的compatibleSdkVersion不能大于工程的compatibleSdkVersion。

### 操作步骤

1. 将工程级build-profile.json5的useNormalizedOHMUrl设置为true。

   **说明** 

   从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，工程级build-profile.json5中useNormalizedOHMUrl字段默认为true，byteCodeHar缺省默认值为true，无需执行步骤1和2。

   ```json5
   {
     "app": {
       "products": [
         {
            "buildOption": {
              "strictMode": {
                "useNormalizedOHMUrl": true
              }
            }
         }
       ]
     }
   }
   ```
2. 在HAR模块的build-profile.json5中，将byteCodeHar设置为true。

   ```json5
   {
     "buildOption": {
       "arkOptions": {
         "byteCodeHar": true
       }
     }
   }
   ```
3. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ic2v31DmTxGnTkrW5izMgw/zh-cn_image_0000002779407034.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6EAE1955F1CF761B475D6C7368DB7154A2C8E46F45B34E87971A881BC91F735)，选择**Build Mode，**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/pqBvA1psTECLXr-Qy51NuA/zh-cn_image_0000002779407032.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=28AAB616B4AF102CB9B176B2F20D4B52BEA91ED76E575D5DA2C41986E2D96270)
4. （可选）在编译模式为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[代码混淆](ide-build-obfuscation.md)。

   ```json5
   {
     "apiType": "stageMode",
     "buildOption": {
     },
     "buildOptionSet": [
       {
         "name": "release",
         "arkOptions": {
           // 混淆相关参数
           "obfuscation": {
             "ruleOptions": {
               // true表示进行混淆，false表示不进行混淆。5.0.3.600及以上版本默认为false
               "enable": true,
               // 混淆规则文件
               "files": [
                 "./obfuscation-rules.txt"
               ]
             },
             // consumerFiles中指定的混淆配置文件会在构建依赖这个library的工程或library时被应用
             "consumerFiles": [
               "./consumer-rules.txt"
             ]
           }
         },
       },
     ],
     "targets": [
       {
         "name": "default"
       }
     ]
   }
   ```
5. （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。

   ```json5
   "buildOption": {
     "packingOptions": {
       "asset": {
         "include": ["./src/router.json5","router.json5"],    // 配置打包到HAR产物中的文件
         "exclude": ["./config/*"]     // 配置不打包到HAR产物中的文件
       }
     }
   }
   ```

   **说明** 

   * 配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
   * 配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
6. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   **说明** 

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/07dYxIBHRwOg5lZ6VNaR8w/zh-cn_image_0000002779407030.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD1832D95AD46092ED56EA4A0CADE0AED645D1B5F00C38B00CF92C620835A711)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/uAGJR_A5SP68pyAdgzCmrQ/zh-cn_image_0000002808766583.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DB2E95B0814933A1BE439CA30144A4BF7B0B34FF0CFF8D8FDFF52DBB2E3BCC6)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/2QxERsZLRDuGle4zTQsm7g/zh-cn_image_0000002808766585.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=272514ECB660697E3761AB740F9103165D5EDB42EA16BDA6DF2AE871135DD76E)

## 源码HAR

### 以debug模式构建

产物是包含源码的HAR包，其中包含源码、资源文件以及配置文件等，方便开发者进行本地调测，不包含build、node\_modules、oh\_modules、.cxx、.preview、.hvigor、.gitignore、.ohpmignore、.gitignore/.ohpmignore中配置的文件、cpp工程的CMakeLists.txt。

**说明** 

* 源码HAR包中包含源代码，请谨慎分发，避免造成源代码泄露。
* 如果是native工程，以debug模式构建的native产物中不包含调试信息和符号表，如需调试，请参考[三方源码调试](ide-source-code-debugging.md)。
* 从5.0.3.403版本开始，不再建议使用相对路径跨模块引用代码文件，若历史工程存在此场景的跨模块引用，会出现warning告警，请尝试将该文件移至本模块内，再重新进行编译。
* 从5.0.3.403版本开始，以debug/release模式构建HAR的流程使用相同的语法校验规则，若历史工程出现ArkTS语法报错，请按照报错信息修改代码，以符合ArkTS语言规范。

1. 在HAR模块的build-profile.json5中，将byteCodeHar设置为false。

   ```json5
   {
     "buildOption": {
       "arkOptions": {
         "byteCodeHar": false
       }
     }
   }
   ```

   **说明** 

   使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，模块级build-profile.json5的byteCodeHar字段的缺省默认值为false，无需执行本步骤。
2. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/jVXrXctQSWCa2un4ha2VPA/zh-cn_image_0000002808886665.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=927457CF18777D18C543F949A07A3E83D5F7FCD1618DCCBC7D29A39EED0A8079)，**Build Mode**选择**debug。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/2pP3mTWvSCyEx8bfoD3MEA/zh-cn_image_0000002808766587.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B05CEEF657D088DB39E02CA67D933BE977787C9CD9290E9D543170401B4E9D8B)
3. （可选）若部分工程源文件无需构建到HAR包中，可在模块目录下新建.ohpmignore文件，或者在模块目录下的.gitignore文件中，配置打包时要忽略的文件，.ohpmignore文件中支持正则表达式写法，.gitignore文件中支持glob语法。DevEco Studio构建时将过滤掉.ohpmignore或.gitignore文件中所包含的文件/文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ABIPSp1DTA2rflmY9UrigQ/zh-cn_image_0000002779407028.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=90F1D27D21677EC95085ECD19019AB30BA22B0769883F89B76F3C0B3214F2D5D)
4. （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。配置include或exclude字段后，.gitignore和.ohpmignore文件将不再生效。

   ```json5
   "buildOption": {
     "packingOptions": {
       "asset": {
         "include": ["./src/router.json5","router.json5"],    // 配置打包到HAR产物中的文件
         "exclude": ["./config/*"]     // 配置不打包到HAR产物中的文件
       }
     }
   }
   ```

   **说明** 

   * 配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
   * 配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
5. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   **说明** 

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/j0oGPpW1SAaLto9GOc7RJw/zh-cn_image_0000002808886667.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF23EE3178EFC4714307DAF302705EBB2C01DDFA7BBEE2FA5F6D55E70CA7CDE5)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/OJqXvkXWQOOiKPv3PE-ewg/zh-cn_image_0000002779567012.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2875A9B2E4F7440EC64C3CCC827D626BE909AF95F7D937E2D76AA87552889FD)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/qtE1RMSUTc2oeS5PEzYNZA/zh-cn_image_0000002808766589.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F5CBDCA63AFB515B79BA0EA51BCD2740032EB2733A2D76528C47E8B5EB52806)

### 以release模式构建

从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认不开启混淆，构建产物和debug模式相同，请参考[以debug模式构建](ide-hvigor-build-har.md#section197792874110)。

为保护代码资产，建议开启混淆，开启后，构建产物是包含js中间码的HAR包，其中包含源码混淆后生成的js中间码文件、资源文件、配置文件、readme、changelog声明文件、license证书文件，用于发布到ohpm中心仓。

1. 在HAR模块的build-profile.json5中，将byteCodeHar设置为false。

   ```json5
   {
     "buildOption": {
       "arkOptions": {
         "byteCodeHar": false
       }
     }
   }
   ```

   **说明** 

   使用DevEco Studio NEXT Beta1（5.0.3.800）之前的版本，模块级build-profile.json5的byteCodeHar字段的缺省默认值为false，无需执行本步骤。
2. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/ojhs1BtKSuWW3NDnu-zusw/zh-cn_image_0000002808766599.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=28916CA9DA438ED4271709CA99AB9CC4110CE90B5D7E0F7E5B058E54F5CB49AA)，**Build Mode**中选择**release。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Y2tPM4NSSIeu76TfPHvZJQ/zh-cn_image_0000002808766595.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9936C8D016DBF83774D2B2844651B9E0A4DE8B0F52DA4E37B4518F9B9719E0C6)
3. 在[编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[代码混淆](ide-build-obfuscation.md)。

   ```json5
   {
     "apiType": "stageMode",
     "buildOption": {
     },
     "buildOptionSet": [
       {
         "name": "release",
         "arkOptions": {
           // 混淆相关参数
           "obfuscation": {
             "ruleOptions": {
               // true表示进行混淆，false表示不进行混淆。5.0.3.600及以上版本默认为false
               "enable": true,
               // 混淆规则文件
               "files": [
                 "./obfuscation-rules.txt"
               ]
             },
             // consumerFiles中指定的混淆配置文件会在构建依赖这个library的工程或library时被应用
             "consumerFiles": [
               "./consumer-rules.txt"
             ]
           }
         },
       },
     ],
     "targets": [
       {
         "name": "default"
       }
     ]
   }
   ```
4. （可选）如果开发者希望自定义打包到HAR产物中的文件，可在HAR模块的build-profile.json5文件中，配置include或exclude字段，支持glob语法。

   ```json5
   "buildOption": {
     "packingOptions": {
       "asset": {
         "include": ["./src/router.json5","router.json5"],    // 配置打包到HAR产物中的文件
         "exclude": ["./config/*"]     // 配置不打包到HAR产物中的文件
       }
     }
   }
   ```

   **说明** 

   * 配置include字段时，以下目录不生效，即不会被打包到产物中：node\_modules、oh\_modules、.preview、build、.cxx、.test。
   * 配置exclude字段时，以下文件不生效，默认会打包：oh-package.json5。
5. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   **说明** 

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**Build > Clean Project**操作，再重新进行Build全量构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/L8DdloktTd-Ol7-315fLCw/zh-cn_image_0000002779567010.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=922B4FCC49DC5BB1D3466888AEFD7030198A6B54AA96207AE12C50E0B3296ED1)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/fB6r1tV-SkKogr4RCZhp7g/zh-cn_image_0000002779567008.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=867C2A4197F8AF093DFA7BE7C391D2E5A8C6607F263D86D2C0C331373D2147A1)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/eKrbIZCWQouHCuxQ9S5ujw/zh-cn_image_0000002779567016.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=853BB20C375C0DFE4F1B5D599A2675A3BE5EE820E71FDC923E68163E433F2E55)

## 对HAR进行签名

DevEco Studio在构建HAR流程的基础上，支持对HAR进行签名。签名后的HAR包后续可用于接入生态市场，接入流程请参考[上架SDK说明与指南](../start/dev-mall-marketplace-sdk-entry-explain-and-guide-0000002411013129.md)。

**说明** 

1. 该能力只在Compatible SDK 5.0.0(12)及以上版本的SDK中支持。

2. 该能力需开启Hvigor的Daemon能力，请确保当前工程开启了Daemon，打开**File > Settings**（macOS为**DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor**，勾选字段**Enable the Daemon for tasks**。

1. 在hvigor-config.json5中，开启构建签名HAR开关：

   ```screen
   {
     "properties": {
       "ohos.sign.har": true
     }
   }
   ```
2. 配置工程签名信息，配置流程请参考[配置签名信息](ide-publish-app.md#section793484619307)。
3. 选中HAR模块的根目录，点击**Build > Make Module '<module-name>'**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/_igImlP6S6GVDp_XSAUWhw/zh-cn_image_0000002808886679.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2363E314E310753095327FF586F7D928304D3C51EBC62D4ABCAF55DB67CA374F)

   构建完成后，build目录下生成签名HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/nSw2R2qyQVKgRgbqttK93A/zh-cn_image_0000002808766601.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF2FC7FD13CC6FD677870B68331BCB1687847B93266123F1EB12882B69FE094E)

## 多HAR合并打包

SDK厂商在对外发布SDK（HAR包）时，有时需要隐藏内部实现细节及依赖，仅暴露必要的接口。从26.0.0版本开始，Hvigor支持将字节码HAR及其所有依赖合并打包，生成一个无外部依赖、可直接使用的独立HAR包。

### 配置方法

在HAR模块的build-profile.json5文件中，配置bundle字段可以实现多HAR合并打包的能力。bundle下包含bundledDeclare和bundledAllDependencies两个字段，是[bundledDependencies](ide-hvigor-build-profile.md#section8368152412552)的增强版。使用时，不能同时配置bundle和bundledDependencies。

```json5
// HAR模块build-profile.json5
"buildOption": {
  "arkOptions": {
    "bundle": {
      "bundledDeclare": true,
      "bundledAllDependencies": true
    }
  }
}
```

**表1** bundle字段说明

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| bundledDeclare | 布尔值 | 可选 | 构建字节码HAR或HSP时，是否生成bundle化的声明文件。   * true：生成。 * false（缺省默认值）：不生成。   说明：  bundledDeclare开启后，产物HAR中，默认只会生成oh-package.json5中main字段和oh-exports字段所指向源码文件的声明文件。如未配置oh-exports字段，则只生成main字段源码的声明文件。 |
| bundledAllDependencies | 布尔值 | 可选 | 构建字节码HAR时，是否将所有依赖打包到产物中。   * true：打包。 * false（缺省默认值）：不打包。 |

**说明** 

* bundledAllDependencies会将dependencies和dynamicDependencies所有依赖都打包，而bundledDependencies只会将dependencies和dynamicDependencies依赖的源码HAR打包。
* bundledAllDependencies为true，devDependencies中配置的HAR包的资源/so不会打包。
* bundledAllDependencies为true，bundledDeclare也必须配置为true。
* bundledAllDependencies为true，且hvigor-config.json5的ohos.byteCodeHar.integratedOptimization为true时，工程级oh-package.json5中的本地模块依赖的资源/so不会打包。
* bundledAllDependencies为true，依赖中不支持配置HSP类型的依赖。
* bundledAllDependencies为true，若依赖没有被调用，则最终会被裁剪，不会打包到最终的HAR中。

### 使用效果说明

关于bundledDeclare字段的使用效果，示例代码如下：

```json5
// oh-package.json5
"dependencies": {
  "shop": "1.0.0"
}
```

```ets
// Index.ets
export { live } from './src/main/ets/components/Live';
export { shop } from 'shop';
```

* bundledDeclare不配置，或配置为false时，编译的字节码HAR或者编译HSP生成的HAR中的声明文件如下：

  ```ets
  // Index.d.ets
  export { live } from './src/main/ets/components/Live';
  export { shop } from 'shop';
  ```
* 配置bundledDeclare为true后编译：

  ```ets
  // Index.d.ets
  export declare function live(game: string): void;
  export declare function shop(product: string): void;
  ```

关于bundledAllDependencies字段的使用效果，示例代码如下，以live模块为例：

```json5
// oh-package.json5
"dependencies": {
  "shop": "1.0.0"
}
```

```ets
// Index.ets
export { live } from './src/main/ets/components/Live';
export { shop } from 'shop';
```

将bundledAllDependencies配置为true（此时bundledDeclare也必须配置为true）编译，除了Index.d.ets会被bundle合并外，依赖的shop源代码文件也会被合并到live的modules.abc中，资源文件/so文件也会合并打包到live包中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/VHt5EszjSg-sH7sjAkXtDQ/zh-cn_image_0000002808886671.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=67E8518F8E74D81DBA82FBB9E1286C671C4FC882D4848E3B1338A029658C591B)

配置bundledAllDependencies为true后，HAR包的oh-package.json5中的dependencies也会被消除：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/vUoWktrXSV6IvOCowYgMqA/zh-cn_image_0000002779407024.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0AE0518F0EEE0575CFF63FFD12BB0EC238C9066DFC9F5BED9AF67A2F3E03F8B)
