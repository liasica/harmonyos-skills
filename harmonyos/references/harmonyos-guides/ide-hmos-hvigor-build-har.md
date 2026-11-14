---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-build-har
title: 构建HAR
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 配置构建流程 > 构建HAR
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:18+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:44e31bc01f1da299929f5f97481dc34da6f7ca74a9f3d1ca0b6cb7f29d504cb3
---

构建模式：鸿蒙电脑DevEco Studio默认提供debug和release两种构建模式，同时支持开发者自定义构建模式。

产物格式：构建出的HAR包产物分为包含源码的HAR、包含js中间码的HAR以及包含字节码的HAR三种产物格式。

DevEco Studio默认构建字节码HAR，用于提升发布产物的安全性。

## 使用约束

HAR自身的构建不建议引用本地模块，可能导致其他模块依赖该HAR包时安装失败，如果安装失败，需要在工程级oh-package.json5中配置[overrides](ide-hmos-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)。

## 创建模块

1. 新建工程，工程创建完成后，新建“Static Library”模块。模块创建方法可参考[添加模块](ide-hmos-add-new-module.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/lyRcLGr6Ql-dp5sMYirp-w/zh-cn_image_0000002781311156.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=03E8BF191A6C53707E4E8BD5A911C22F2A426F4C66AF64CDD44E0082F66AF3EF)
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
3. 点击DevEco Studio界面上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YCAWBNk2RieuaIPB8FKV5A/zh-cn_image_0000002810750743.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=06876354A10764C05796FC38508ABC6AC199069B76A7E8692A1D1F3D518BAA6B)右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/WH4O2ab8RiOwPm36PvNwbw/zh-cn_image_0000002810630629.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=33C272B67753DDF1C5E53AF77161AF5D617E4FEA93ABD61978B337C800233C23)，选择**Product配置** **> 构建模式**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/g13eqUrPQgCXt5yP8ADthA/zh-cn_image_0000002781471072.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=094C69F613583B7C97F13A83A43FD2C433A297865059249E74329E8B5154FF99)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/CVCSY0m7QO-QMReoi62zVQ/zh-cn_image_0000002781471086.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF04C9920C643B2270B786BAECBB279D4509C81ED5A268F91D19F3E3168A16FE)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/c9jym-xZQAeD0hhXKuf6pg/zh-cn_image_0000002781471076.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=2ECFA8BD022ED64B293ED0D4FD8A95F1BA44EE0ACE0F5AB2E9D196D06964AD28)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/5fxIun_QS7ClroAyMn2suA/zh-cn_image_0000002781311150.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=454360573E8AFF73EEE50666DEE032BF322738D52781DA84529B2CDFCE536BA2)

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
2. 点击DevEco Studio界面上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7PCM_bQAQ0aDeYiInA_ZEQ/zh-cn_image_0000002810630643.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E9D1FFBD7037EC61B3531CF76D51EAC7EC453AF53FF50F277E415B98DA569F6)右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/e3JAReLwSSGZsbc--E6skQ/zh-cn_image_0000002781471084.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=F68EFA4388D31F924D52DE93ADDE799BD2875054DA16D1A8DC449754E70B5412)，选择**Product配置**，**构建模式**选择**debug**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Vb0Ht18oSrW-74ANYqnj_Q/zh-cn_image_0000002810750739.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B6BB092CDD06FEBD698B62C8DD003FB1C64AEB36A70D823159A3C8780BC5406)
3. （可选）若部分工程源文件无需构建到HAR包中，可在模块目录下新建.ohpmignore文件，或者在模块目录下的.gitignore文件中，配置打包时要忽略的文件，.ohpmignore文件中支持正则表达式写法，.gitignore文件中支持glob语法。DevEco Studio构建时将过滤掉.ohpmignore或.gitignore文件中所包含的文件/文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Mwd-JI0PRqSSaDFDnPYohQ/zh-cn_image_0000002810750735.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=3896C09B4212AF11D273411E350D2675E49F439964D1EC9055562FAA7A512D76)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/25rocRIiRaybJbKYyiJTLw/zh-cn_image_0000002810750741.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3CD6D5FAE47AF7F4391488BD42CB739F503EAF0A1FFCEE3804C9C3AE5CFBCF0)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/u_uaXEDfTsWk_LfkbZY7eg/zh-cn_image_0000002810750747.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=30D520381A4F9C5D735DB381FB21DA8B155B31C361CAF6E11A4C9F56C0388E1D)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/hiuJE2BFSymgr1OFBp1OFA/zh-cn_image_0000002781311152.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF14AE2E484FEDD687A6454C41767CE3F2764297BD49971404D5B79F095717A4)

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
2. 点击DevEco Studio界面上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/KTDRUBTMR9Wk1b5XxdLoXw/zh-cn_image_0000002781471074.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=6233CD68EA4A4E8F1851832933C66BF05BF1A6637633711D72973901D9529303)右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/G_-rsBReTr-bHurudCEV2Q/zh-cn_image_0000002810630641.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD0B99F80B892FA2DB6F07CB44E3F51AF770357D4874AFF685A0D3CEB052B3DC)，选择**Product配置**，**构建模式**选择**release**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/V8GsYtscTXaMpa12SZXGpQ/zh-cn_image_0000002810630635.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3C081A93095ABF77B35F186FF162E8A89855DEE455B06948472307C15AAD98B)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/-AoGFkpcQ3Cgs7lW6uC21Q/zh-cn_image_0000002781471080.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF8D8DF2090069D2B34919B79552A497F210ECA2B923DCBD01C729527EB1ECA7)

   构建完成后，build目录下生成HAR包产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/nO9oJrH0SA2DwLT6DXBgGA/zh-cn_image_0000002810750749.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=C338F29296BE2B4C2A799E37D9FC51C0F3D348E081B2FB3840A0058B5BFD4EEF)

   HAR包产物解压后，结构如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/TNjww4YVQCmmz1nuVYat7g/zh-cn_image_0000002781311144.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC710940A62DD3A1FA683A769AB1F55D3F1E13C0BDCC7D427581F1E191C18F6)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/P33z5M9HQMCtTk9gaRU3pw/zh-cn_image_0000002781311154.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FF4DF187774BA22A68042C4A91453517E4C119A61BC41303FA934B2F10C9231)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/1esFXkEeTte8evRygvHrJA/zh-cn_image_0000002810750737.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=64C32D6566331E926D833A779E1235A84E7A31B98ED55D2D77C1F6B6A4FA92E0)

配置bundledAllDependencies为true后，HAR包的oh-package.json5中的dependencies也会被消除：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/zDK__MqkSnmzLntK48yOog/zh-cn_image_0000002781471082.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=043877A1ADD7B498F0A805B3C8460C3632CE6EB368C6F95E1FCFFD01E0AB2A99)
