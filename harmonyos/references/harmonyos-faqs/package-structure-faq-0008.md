---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/package-structure-faq-0008
title: HAR包使用常见问题排查
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 常见问题 > HAR包使用常见问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a959225c0e0464a9114c92042fe8b7b5005b9b1321579f1be31f5cccb0c17856
---

**Q：每次是否都要先打包成HAR包再引用？**

**A**：不需要每次先打包成HAR包再引用，可以直接引用源码，如entry模块需要依赖foo模块的源码方式如下。在需要引入本地模块源码的模块的oh-package.json5中设置源码依赖项，即entry模块的oh-package.json5中，添加如下配置：

```json
"dependencies": {
    "foo": "file:path/to/foo"  // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
  },
```

**Q：是否可以将java或jar文件打包成HAR包？**

**A**：当前不支持将java或jar打包成HAR包。HAR包是静态共享包，可以包含ArkTs/ts代码、C++库、资源和配置文件。

**Q：HAR包会被重复打包如HAR包中有so库，引用此HAR包的每个module都会拷贝一份此so库，造成包体积非常大，如何优化？**

**A**：推荐将公共资源替换成HSP动态共享包。在多包场景下，如果应用的多个HAP或HSP包使用HAR包实现代码和资源的共享，那么打包后的每个HAP或HSP包中都会存在一份共享HAR包的拷贝，导致APP包中存在冗余代码和资源。如下图示例，应用模块HAP1和HAP2/HSP1都引用了HAR2和HAR3，打包后，APP包中HAR2和HAR3存在多份重复拷贝，体积较大。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/wFZrdl40SwWW9bJTsjUW1Q/zh-cn_image_0000002802054445.png "点击放大")

这种场景下，推荐开发者使用HSP代替HAR实现代码和资源共享。如下图示例，使用HSP2对原应用进行升级改造，打包后，APP包中HAR2和HAR3只存在一份拷贝，HAR2、HAR3总大小大于HSP时，可以减小应用包大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/S4EU4cQ-S6GoO6vmnZ-Mew/zh-cn_image_0000002772854674.png "点击放大")

**Q：一个应用有多个模块，多个模块中引用同一个HAR包的不同版本是否有影响，怎么指定统一的版本？**

**A**：没有影响，每个模块都会将各自的HAR包拷贝到自己的模块，不会影响其它模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/-_6Xf4zPQ76y3wkOuhMJvQ/zh-cn_image_0000002772694692.png)

ohpm客户端在1.4.0版本开始支持[Override机制](../harmonyos-guides/ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)，可以在项目级别的oh-package.json5（即项目根目录下的oh-package.json5）文件中添加overrides配置，可以将HAR包指定统一的版本。替换的版本既可以是一个具体的版本号，也可以是一个模糊版本，还可以是本地存在的HAR包或源码目录。

**须知** 

overrides必须配置在项目级别的oh-package.json5中，配置在模块级别的oh-package.json5中将不会生效。

* 如项目指定foo统一版本为1.0.1，在项目级的oh-package.json5中配置如下：

  ```json
  "overrides": {
      "foo": "1.0.1"
    },
  ```
* 若本地存在foo的源码或者HAR包，想确保foo始终使用您本地的版本，可以在项目级的oh-package.json5中如下配置：

  ```json
  "overrides": {
      // 本地存在"foo"的源码目录，如项目根目录下的foo目录
      // "foo": "file:./foo"
      // 本地存在"foo"的HAR文件，如项目根目录下的libs目录中的foo.har
      "foo": "file:./libs/foo.har"
    },
  ```

**Q：一个应用存在多个HAR模块，例如存在模块HARA、模块HARB、模块HARC和模块HARD，HARB中依赖并引用了HARA，HARC中依赖并引用了HARB和HARA，HARD中依赖并引用了HARC、HARB和HARA，现在希望打包完成后的包中只包含一份HARA、HARB、HARC、HARD，避免生成的HAR包冗余重复，该如何实现？**

**A**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NuC6NUvoTTS0pjhIbU931Q/zh-cn_image_0000002802134805.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/sNQEr8qdQ2u5Wb9lYONGVw/zh-cn_image_0000002802055095.png "点击放大")

* 由于存在多个HAR模块，这些模块之间又存在重复依赖和引用的关系，由于同一个工程下，不同HAR模块之间存在继承依赖的关系，即对于工程下的模块HARA、模块HARB、模块HARC和模块HARD，先将模块中的方法、类和接口等通过export方式暴露出去，使得工程下其他模块能够访问。
* 让HARB中依赖HARA，HARC中依赖HARB，HARD中依赖HARC，从而使四个模块构成继承依赖的关系，就可以实现在HARD引用HARC、HARB和HARA，在HARC中引用HARB和HARA，在HARB中引用HARA，这样就避免生成重复HAR包的情况。
* 将最外层的HAR模块HARD先转化成HSP模块，参考链接进行相关配置[HAR转HSP指导](../harmonyos-guides/har-to-hsp.md)。由于HSP模块只能供应用内其他HAP模块或HSP模块引用，如果需要共其他应用的模块使用，还需要将HSP模块转化成[集成态HSP](../harmonyos-guides/integrated-hsp.md)，参考链接进行相关配置集成态HSP。
* 对集成态HSP模块HARD进行打包，提供给其他应用使用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Hs3xH_rpQ3WrHVO9vWULQQ/zh-cn_image_0000002772694976.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/eGPZkfu4TOexLpLRbhxl7A/zh-cn_image_0000002802134807.png "点击放大")

**Q：多模块依赖场景下，如何直接打包最外层HAR包而无需逐层打包子模块HAR包？**

**A**：在多模块工程中，模块间存在多层依赖关系（如模块A依赖模块B和模块C，模块B依赖模块D和模块E，模块E依赖模块F和模块G），若使用HAR包仓库管理依赖，需要从底层模块开始逐层打包HAR包并发布到仓库，再逐层修改依赖为HAR包版本号依赖，操作步骤繁琐且耗时。通过在oh-package.json5中使用@module依赖语法，可以将模块间的依赖关系声明为源码依赖，这样在打包最外层HAR包时，所有依赖模块的源码会自动编译并包含在最终HAR包中，无需逐层打包和发布子模块HAR包。

在需要依赖其他模块的模块的oh-package.json5中，将dependencies中的依赖项配置为@module语法。例如，项目中存在名称为Foo的模块（即build-profile.json5文件中modules节点下存在名称为Foo的模块），且该模块Foo的oh-package.json5中name为foo\_test，则在依赖方的oh-package.json5中添加如下配置：

```json
"dependencies": {
    "foo_test": "@module:Foo"
  },
```

通过这种方式，所有模块间依赖均以源码方式引用，直接打包最外层模块的HAR包即可，无需逐层构建和发布子模块HAR包。参考[oh-package.json5配置说明](../harmonyos-guides/ide-oh-package-json5.md#section2016910347161)。

**Q：SDK的HAR包通过dependencies依赖了其他库，使用该SDK的应用即使不使用该依赖，最终产物包中也会自动包含该依赖的内容，如何解耦？**

**A**：将不需要打包进最终产物的依赖配置在oh-package.json5的devDependencies字段中，而非dependencies字段中。devDependencies中声明的依赖仅在开发阶段使用，不会被打包进HAR包产物。参考[oh-package.json5字段说明](../harmonyos-guides/ide-oh-package-json5.md#section02162312018)。如果SDK除了该依赖还有其他内容需要使用，但代码中不需要该依赖，则需要将整个HAR包打包进去。
