---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-build-har
title: 构建HAR
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 配置构建流程 > 构建HAR
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:47+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:0034ff45d9dd5bb67769f6ac03f7f1cc863b00411c7143f10bde9c8682a846b3
---

构建模式：鸿蒙电脑DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。

产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。

DevEco Studio默认构建字节码HAR，用于提升发布产物的安全性。

## 使用约束

HAR自身的构建不建议引用本地模块，可能导致其他模块依赖该HAR包时安装失败，如果安装失败，需要在工程级oh-package.json5中配置[overrides](ide-hmos-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)。

## 创建模块

1. 新建工程，工程创建完成后，新建“Static Library”模块。模块创建方法可参考[添加模块](ide-hmos-add-new-module.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/oTBWbj4VSfC4rDobdrdD-g/zh-cn_image_0000002820721257.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=2686CB9BA4DB22ECE6ECDEB3E820D111A4AD7C799D6D45484788F15B350890DA)
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

* 字节码HAR使用的依赖需要配置在本模块的oh-package.json5的dependencies或dynamicDependencies中，如果不配置，后续字节码HAR被集成时可能会出现运行时异常。如果出现异常，部分场景可通过在hvigor-config.json5中配置ohos.byteCodeHar.integratedOptimization后重新编译，具体请参考[编译行为差异说明](ide-hmos-hvigor-dependencies.md#section957371853712)。
* 字节码HAR的oh-package.json5中配置的依赖名和依赖包的包名（即包内oh-package.json5中的name）需要保持一致。
* 依赖字节码HAR包时，该工程的build-profile.json5中的[useNormalizedOHMUrl](ide-hmos-hvigor-build-profile-app.md#section13181758123312)必须设置为true。
* HAP/HSP/HAR依赖字节码HAR包时，HAP/HSP/HAR的oh-package.json5中配置的依赖名和字节码HAR包的oh-package.json5中的name需要保持一致。
* HAP/HSP/HAR代码中import使用字节码HAR包时，`import xxx from 'yyy'`的依赖名yyy要和本模块oh-package.json5中配置的依赖名保持一致（包括大小写）。
* 依赖字节码HAR包时，字节码HAR的compatibleSdkVersion不能大于工程的compatibleSdkVersion。

### 操作步骤

1. 将工程级build-profile.json5的useNormalizedOHMUrl设置为true。

   **说明** 

   工程级build-profile.json5中useNormalizedOHMUrl字段默认为true，byteCodeHar缺省默认值为true。

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
3. 点击DevEco Studio界面上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/6_ADA5BZRrm8L5XApHVpwQ/zh-cn_image_0000002792001284.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC447E379BE43B2710D74FD0308DA6F63480B68A3493BF387D5E144314232F77)右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/BCBO66YCSpC6f4nvgShqhA/zh-cn_image_0000002791841312.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=321D7EBFE21203C79641C7BE8C11FE01612FB24A5DDACFF5E7A6CDC6109D7730)，选择**Product配置** **> 构建模式**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/MfeTsMNBR9CqVtTnSFaPZQ/zh-cn_image_0000002820721265.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=62560733BD9E9430EB414C835F6B5D81273460B22F6D1B3560531F1D586CF7CC)
4. （可选）在构建模式为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[混淆加固](ide-hmos-build-obfuscation.md)。

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
               // true表示进行混淆，false表示不进行混淆。
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
6. 选中HAR模块的根目录，点击鼠标右键 **> 构建模块**启动构建。

   **说明** 

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**构建 > 清理项目**操作，再重新进行构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/qpXrg-oUTNi9XAOvu9o4cw/zh-cn_image_0000002820681259.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=E06FB2A2BA0B84356E593BBA62CF969D5B2FD30D31F53D0E96797F9F373FEA49)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/2gWa294cRcmmhGA8lAYucQ/zh-cn_image_0000002820721263.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D00D4489F0DB56788C066328336BEFFC38C7FE5E73400C23253685F41A11D21)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ahnnfu1RRIG53Vqc_0tnLw/zh-cn_image_0000002792001292.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=D470B48DC293EF5441CB48293006EA2DB99F628AC6745D658CEFFD41F21D3818)

## 源码HAR

### 以debug模式构建

产物是包含源码的HAR包，其中包含源码、资源文件以及配置文件等，方便开发者进行本地调测，不包含build、node\_modules、oh\_modules、.cxx、.preview、.hvigor、.gitignore、.ohpmignore、.gitignore/.ohpmignore中配置的文件、cpp工程的CMakeLists.txt。

**说明** 

* 源码HAR包中包含源代码，请谨慎分发，避免造成源代码泄露。

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
2. 点击DevEco Studio界面上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/9apmtNYSTGiRZxc5LLN5JA/zh-cn_image_0000002820681255.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=30F122C94CFE84349CFBA85CEA87FDC2EA8DD0FE19FBED9BECE9FCCEBF866388)右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/mtBIuF6LQDO75FsmOjnZCw/zh-cn_image_0000002791841322.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=779085D1DDDD2EFE94710126B9D9F4E58A1A4DF2519574C166022B52B75D3D48)，选择**Product配置**，**构建模式**选择**debug**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/r8dtuONiR-G0ykUAMuz1_A/zh-cn_image_0000002791841314.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DFFF0660223D9C8E879BF700BA816BF17D1DF174AFA309DB15F96235C0D953F)
3. （可选）若部分工程源文件无需构建到HAR包中，可在模块目录下新建.ohpmignore文件，或者在模块目录下的.gitignore文件中，配置打包时要忽略的文件，.ohpmignore文件中支持正则表达式写法，.gitignore文件中支持glob语法。DevEco Studio构建时将过滤掉.ohpmignore或.gitignore文件中所包含的文件/文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/J2pShgQ9S3qkTBXvQcdr8w/zh-cn_image_0000002820681247.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=14B458EBB809A6B93986519E7D4FC167F83EA2C0B07C8FBA1A6CF1317670BF8A)
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
5. 选中HAR模块的根目录，点击**鼠标右键 > 构建模块**启动构建。

   **说明** 

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**构建 > 清理项目**操作，再重新进行构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/Ffr84lVLTrChCztaN5vs-w/zh-cn_image_0000002791841310.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=7857A8265C3BAEE94C7E8B0B63C23A0B216C2316DFA8D5DBE2DE1D9D77131794)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/vnXBC1pcT8ybboZ7s313xw/zh-cn_image_0000002820721255.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=F939490F03E3F184C68FDA23FDC0E0F1EA630756FEE0B72BEFCA868B857C1B43)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/A1D4HUpZTcyHbPvlQCoPTA/zh-cn_image_0000002791841318.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=9ADEBD6871BE52DAC41B562B6F6CD63103E5943E96775429F221383DFA5A3511)

### 以release模式构建

DevEco Studio默认不开启混淆，以release模式构建时，构建产物和debug模式相同，请参考[以debug模式构建](ide-hmos-hvigor-build-har.md#section197792874110)。

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
2. 点击DevEco Studio界面上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Xqk_E_xqToq3qbTib437iw/zh-cn_image_0000002792001298.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=8EAACF11E5AA610D3818F67F5E12FACD7214EE57EC24BDEF2773BBA17639F86C)右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/HK6E9NtwRE-EMQD6DZncAw/zh-cn_image_0000002791841320.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=108FF09B37EFE1FB84A19B8A15CC46C029A44D6219CA1F52BC24108F150A008B)，选择**Product配置**，**构建模式**选择**release**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/pD4ptUc3TbeddrEzvC5wCw/zh-cn_image_0000002820721259.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE61ACEA1D0359D3952C30069705454133357600394B79E34901D948523A6CFF)
3. 在构建模式为release时，为保护代码资产，建议开启混淆，在模块级build-profile.json5文件的release的buildOptionSet配置中，将obfuscation/ruleOptions下的enable字段设置为true。混淆相关能力和具体规则请参考[混淆加固](ide-hmos-build-obfuscation.md)。

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
               // true表示进行混淆，false表示不进行混淆。
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
5. 选中HAR模块的根目录，点击鼠标右键 **> 构建模块**启动构建。

   **说明** 

   若修改了HAR模块级oh-package.json5文件的version字段，请先执行**构建 > 清理项目**操作，再重新进行构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/keFVa2KYTK6o8ticao4hnQ/zh-cn_image_0000002792001294.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=63DED2C3A2C6D6F56580A97814912901FF3B9064AECF4923237A9FCF9D1EF87E)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/cF8zXeYlQPuaOUV2-X1YJQ/zh-cn_image_0000002820681249.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=0301C85EAF2D2797DC1B62AC2FE21982D8BB14C74363A328B14CC17161E80329)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/AbKfA1wqSdaW-ggdXWhMWw/zh-cn_image_0000002792001290.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=21B1E58FE6D2D92A2DE81590639A31B99ADA8DC16A2A938123B3153ED3B0D4ED)

## 多HAR合并打包

SDK厂商在对外发布SDK（HAR包）时，有时需要隐藏内部实现细节及依赖，仅暴露必要的接口。Hvigor支持将字节码HAR及其所有依赖合并打包，生成一个无外部依赖、可直接使用的独立HAR包。

### 配置方法

在HAR模块的build-profile.json5文件中，配置bundle字段可以实现多HAR合并打包的能力。bundle下包含bundledDeclare和bundledAllDependencies两个字段，是[bundledDependencies](ide-hmos-hvigor-build-profile.md#section8368152412552)的增强版。使用时，不能同时配置bundle和bundledDependencies。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/jH4k5Wx7QP-3D6MKtMCM7w/zh-cn_image_0000002820681253.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9561D401E304BCD8D3F879A0DE22EA48E7CAB199889122CE6BD5CE06D93CD75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/hG6gv1g0R3u0GeN3OXJ9fw/zh-cn_image_0000002792001288.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=801F9B53113A7A61DBC88EBE68F439BE5881CBAFE7C785E8B11C944001F96FB4)

配置bundledAllDependencies为true后，HAR包的oh-package.json5中的dependencies也会被消除：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/JZAc81k_TOuLCGJfFZbzUQ/zh-cn_image_0000002820681257.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=E246966F19BB0A9C059907087EEEF0B30A0A29BFF624F92E5C29ED58C364709E)
