---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har
title: 构建HAR
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 配置构建流程 > 构建HAR
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:33+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4576e2df9048e36054197769759debe7942296b2b62bf4ee232d0860a25eb2e3
---

构建模式：DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。

产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。

从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，默认构建字节码HAR，用于提升发布产物的安全性。

## 使用约束

HAR自身的构建不建议引用本地模块，可能导致其他模块依赖该HAR包时安装失败，如果安装失败，需要在工程级oh-package.json5中配置[overrides](ide-oh-package-json5.md#section13977152601510)。

## 创建模块

1. 新建工程时选择API 10及以上的Stage模型，工程创建完成后，新建“Static Library”模块。模块创建方法可参考[添加模块](ide-add-new-module.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/ccgmZeKJTHiUrPgPVKB8wQ/zh-cn_image_0000002808886669.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=67D78C46BFB8302336812AD496C968B6CF92CC62D84CCDA58CD9B08EA4ED611C)
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
3. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ZQszPXm4QdqEq_C3olcPpw/zh-cn_image_0000002779407034.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D123A3F23D665C147095F1562827AAF61973D8432484B1DBB81900DC30AEA71F)，选择**Build Mode，**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/4QIRVuoITeGUNML8FSjSzQ/zh-cn_image_0000002779407032.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA03585DB42AF6D15771293AA36576577A3B96CB7B4D8679B77C352D6B6F9A6E)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/QWfFVjhHQUKAUH-jnjQXCw/zh-cn_image_0000002779407030.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=68379C27E2BA18D4290BA3123C7B3A0007E36327E62294813200F5BD575619E8)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ecWOf2G9Q2OR3TpuLQKoaQ/zh-cn_image_0000002808766583.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ECC59599FB2117697123AE72FFCD9F85F1C9ED0DB376F8C1B0272E72AA65CFD)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/SOLw0XmXQO2Nzj0oTv0V6Q/zh-cn_image_0000002808766585.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9B5B1CCA876A58B851A45EB8A572CED0414CEB7B954E0076C49A686E0E928BC)

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
2. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/X9GXhkjDQX-an2hDP2nDRA/zh-cn_image_0000002808886665.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A17587D0D04982FD870553BF9B3188B54D191895B5B0CD5489CC19E38C2197C4)，**Build Mode**选择**debug。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Vi6XJMZDRgalpnJ0h5vVNA/zh-cn_image_0000002808766587.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B88DEC02C4D98B54BB13F4DCD81A52C08CA747656125DDC165B82DF21C8022F)
3. （可选）若部分工程源文件无需构建到HAR包中，可在模块目录下新建.ohpmignore文件，或者在模块目录下的.gitignore文件中，配置打包时要忽略的文件，.ohpmignore文件中支持正则表达式写法，.gitignore文件中支持glob语法。DevEco Studio构建时将过滤掉.ohpmignore或.gitignore文件中所包含的文件/文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/E3ckXeYDR2CGn32I012nEA/zh-cn_image_0000002779407028.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD5E2EBE5629A3C5EB651D1C8ECF1B712FDE3D4D22F8202C185E49C9B9E11CDE)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Mukf6ehQQtKGqYELI9b-hQ/zh-cn_image_0000002808886667.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=18C144086B0A72997F405DD56BD43861EC8EFDC0B163780C2C175B96C976AA4E)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/3WZmpJdKQTmjJ2SwdDbGpw/zh-cn_image_0000002779567012.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C8E6943335F7C9926DEA3BAEC5AFBE4FB063AD44F68190DDA42DE3BA2487163)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/52SzibjASSuhcrvVRP3IGQ/zh-cn_image_0000002808766589.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5D1F66B195CC143949B76D35529605E0B848195AB33DFFF4D2CF4E4480E25CD)

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
2. 点击DevEco Studio右上角图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/xRPCK9tbRTegXybebgN55Q/zh-cn_image_0000002808766599.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=908C8041912490160FF7A290B8FCAE60D9A42FB1B28D59E34636165D04B2AA3F)，**Build Mode**中选择**release。**默认为**<Default>**模式：在编译App时使用release模式，编译HAP/HSP/HAR时使用debug模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/jKujj8jyRmic642eEKTLKw/zh-cn_image_0000002808766595.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4999E8BB9C9D8D5BB28099A63E6EEF74F7DECC4FD802B9EDC60E9B9A68AB6EB)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Fe5Mq5ikQjuNx2x22UtVAA/zh-cn_image_0000002779567010.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0288B895C74FCD7040BEF88917358063BEBD1B0A222FB0E5B857CEE07090594)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Tn6o7qoSSkWeOuLA9ZHHvg/zh-cn_image_0000002779567008.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2B217A6D3F16CC45DA3B7BC1117460B28C7783E90D2C2948746C385D4C49EED)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-7o4DNRZQLCxQmqRYQpPuA/zh-cn_image_0000002779567016.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=113E1832D2ADA663F5B69BCF466F68A12146D6B55EA9EEE7A10F581F4673C515)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/KkFEbhhgQIW0PTLZVy9hBQ/zh-cn_image_0000002808886679.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C92FE556F998A7B78DBC43B91888E120ECD95D9E7DF40768D854A02C54DB0B73)

   构建完成后，build目录下生成签名HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/7xuUYxQwRAC_Iq0nTeJ9RQ/zh-cn_image_0000002808766601.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F81CB34E4274199A812E4ACA7E77FABACA1FB1332B3FABF4FB9621C6CD7C4D28)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/WCtVGmw1Qxmd5VP8UO09DQ/zh-cn_image_0000002808886671.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=60483D395AAB0FAFBF72D411893F0D941EECC23489FB8C59A98EEDFBA6B51D54)

配置bundledAllDependencies为true后，HAR包的oh-package.json5中的dependencies也会被消除：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/gyBdcwxBRt2vz50gsz_NIw/zh-cn_image_0000002779407024.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=790E76D859A5F89D379459260E11A7F1F3921DCC10B5786E588D5CF677F79FF7)
