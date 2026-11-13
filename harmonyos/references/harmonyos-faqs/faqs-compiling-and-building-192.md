---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-192
title: 三方SDK定制修改部分源码
breadcrumb: FAQ > DevEco Studio > 编译构建 > 三方SDK定制修改部分源码
category: harmonyos-faqs
scraped_at: 2026-11-13T09:06:48+08:00
doc_updated_at: 2026-11-12
content_hash: sha256:8f4ed4d8ce9df384cf5c81adfe2b4f33d43b6685c7231498294c7b290f3d04c5
---

**问题背景**

SDK使用方需在SDK上定制功能开发，SDK提供方仅希望提供SDK和部分源码文件。SDK使用方修改其中部分源码文件，并在编译时替换掉修改部分。

**解决措施**

从DevEco Studio 6.0.2 Beta1版本开始，提供替换abc中的部分文件能力，支持定制化文件的编译以及替换三方SDK中编译后的同名文件。

使用能力方式如下：

**SDK提供方：**

提供SDK（即[字节码HAR](../harmonyos-guides/ide-hvigor-build-har.md#section16598338112415)包），并提供待修改部分的源码文件。

**SDK使用方：**

新增"Static Library"模块A，要求模块A与提供方的SDK同packageName(oh-package.json5的name字段)和moduleName(module.json5的name字段)，并将模板A中的MainPage.ets源码文件删除。如下所示，拷贝提供方SDK中所有的声明文件、需要修改的源码文件、abc文件、和资源相关文件到模块A中。

1. 源码：
   1. 声明文件：将src/main/ets目录拷贝到模块A中，保持原目录结构不变。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/hxBdR1-1Q4m_sL2GNbzHMg/zh-cn_image_0000002654798081.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=D84F7205BACE324A8D73D7811EC92ADF99C9F4BB6459AD5EDC58AB62CC51F066)
   2. 需要修改的源码：按照提供方SDK中的目录层级增加需要修改的源码文件，保持和提供方目录结构一致。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/8K_NEJ_eRKuVgWTJLEkNqQ/zh-cn_image_0000002624638634.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8665E3703F239D48306B815D9965413E9D721F0C78BECAD3B046F5C75F6601C)
2. 资源文件：

   使用提供方SDK中的resources目录覆盖模块A中的resources目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/XQKEchvSRq61JDHk7cJ2GQ/zh-cn_image_0000002654838037.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=A60A214A3441C1CC3EC023EF5D7C746F7AFB6FC58F072038F6BEB1BAC403DF26)
3. 配置文件：
   1. 将提供方SDK的依赖配置（模块A的oh-package.json5中的dependencies字段）拷贝到模块A中的依赖配置中。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/F6aRB2_aS1KOOTIVwv6wgQ/zh-cn_image_0000002624478724.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A81D0E9D6FED47744750FF46AFCFD6E7F4E3E049B8237F516084FEC5992D8A9)
   2. 如果需要修改ability的srcEntry文件，就需要将提供方SDK中module.json对应的ability字段拷贝至模块A的module.json5的abilities中，再对ability的srcEntry文件进行修改

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/IvlDFmw2SnyHZWwmpwg3TA/zh-cn_image_0000002654798083.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=B253A6C73AEEC08ECCCBF13D952B85857FB87430D179A8FCF36FE9E578847EA5)
4. abc文件：

   将提供方产物中的modules.abc文件拷贝至模块A目录下，并在模块级build-profile.json5文件，buildOption->packingOptions字段中新增customizedOptions，增加basePackage字段指定abc的位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/-plsaQX0QO6kpHU2VOiLPg/zh-cn_image_0000002624638636.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=19ADEB8C78137D66218BD1E008362D57926CE4EC3C91CA1190393B8AD6F7AD1A)

   ```json
   "buildOption": {
       "packingOptions": {
         "customizedOptions": {
           "basePackage": "./basePackage/modules.abc" // 相对路径
         }
       }
     },
   ```
5. 修改代码后，选择Build菜单的Make Module 'xxx'选项，编译该模块。

**约束(SDK使用方)：**

1. hvigor-config.json5文件的properties下不能将ohos.compile.lib.entryfile配置为false。
2. 从提供方拷贝过来的文件名、资源名、方法名：支持新增，不支持修改、删除。
3. 如果工程中存在其他模块引用了提供方SDK，则需要在工程级别oh-package.json5文件中配置[overrides选项](../doccenter-deveco-studio/ide-oh-package-json5.md#section13977152601510)，改成本地依赖方式。
4. 不允许额外修改模块A配置文件（包括oh-package.json5，module.json5）。
5. 不支持C++源码的修改替换。
6. 仅支持Har的源码修改，不支持Hap和Hsp的源码修改替换。
7. 模块A的混淆规则需要继承提供方SDK中的混淆规则。（建议提供方SDK关闭混淆，如开启需要参考以下a、b进行额外操作）
   1. 需要将MainPage加入到混淆白名单，需要将需要修改的文件名配置白名单。
   2. 中间自动生成的文件moduleInfo.ts及其父目录均需要添加至白名单。
8. 使用该功能后，会遍历源码目录，将.d.ets和.d.ts文件打包到har产物中，请保证不要将重要信息存放在.d.ets及.d.ts文件中。
