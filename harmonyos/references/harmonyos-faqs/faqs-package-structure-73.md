---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-73
title: HAR、HSP、HAP三者的区别和使用场景
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR、HSP、HAP三者的区别和使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:0aae12c4717bce1127d7183aa79a82ebe8da6fcbca94dc9b0bc85859f6ee9571
---

## 问题现象

在项目中经常会接触到HAR、HSP、HAP，这三者有什么区别，它们的使用场景分别是什么？

## 背景知识

[HAP](../harmonyos-guides/hap-package.md)：是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。应用程序包可以只包含一个基础的entry包，也可以包含一个基础的entry包和多个功能性的feature包。

[HAR](../harmonyos-guides/har-package.md)：是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。

* 支持应用内共享，也可以发布后供其他应用使用。
* 作为二方库，发布到OHPM私仓，供公司内部其他应用使用。
* 作为三方库，发布到OHPM中心仓，供其他应用使用。
* 多包（HAP/HSP）引用相同的HAR时，会造成多包间代码和资源的重复拷贝，从而导致应用包变大。

[HSP](../harmonyos-guides/in-app-hsp.md)：是动态共享包，可以包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。HSP不支持独立发布，而是跟随其宿主应用的APP包一起发布，与宿主应用同进程，具有相同的包名和生命周期。多个HAP/HSP共用的代码和资源放在同一个HSP中，可以提高代码、资源的可重用性和可维护性，同时编译打包时也只保留一份HSP代码和资源，能够有效控制应用包大小。

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* 集成态HSP：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于应用内HSP。

## 解决方案

| 对比维度 | HAP | HAR | HSP |
| --- | --- | --- | --- |
| 定义 | 应用安装和运行的基本单元，包含代码、资源、配置等，  分 entry（主模块，必须存在）和 feature（动态特性模块，可选） | 静态共享包，用于复用代码/资源（如UI组件、工具类） | 动态共享包，运行时被多个模块共享 |
| 跨应用共享 | 不可共享 | 可发布至OHPM中心仓/私仓 | 仅限应用内共享 |
| 资源复用方式 | 不涉及 | 编译时复制到引用模块 | 运行时动态加载 |
| 多模块引用影响 | 不涉及 | 代码/资源重复拷贝 → 包体积增大 | 仅保留一份→ 节省空间 |
| 典型使用场景 | 1、主入口模块（entry）：实现应用启动页、核心功能；  2、动态特性模块（feature）：可选扩展功能（如视频播放、支付模块），支持动态部署（按需下载安装）。 | 1、公共UI组件库、工具类封装；  2、跨团队/企业共享：发布至OHPM中心仓或私仓供其他应用调用。 | 1、多模块共用大资源（如图片、视频），避免重复打包、拷贝；  2、元服务分包预加载，提升性能；  3、解决HAR导致的包膨胀问题。 |
| 调试打包 | 调试时需生成.hap文件，通过DevEco Studio或命令行直接安装到设备。 | 直接打包到HAP中，调试时无需单独安装。 | 避免重复拷贝，需与宿主HAP同进程运行，测试时需先安装HSP再装HAP。 |
| 关键限制 | 1、不支持声明Ability/Page，但可通过Navigation跳转包含的页面；  2、禁止循环依赖，不能引用AppScope资源。 | 1、需与宿主HAP版本号严格一致；  2、不能独立发布到应用市场。 | 不可作为共享包给其他应用使用。 |

## 常见FAQ

Q：多模块使用同一个HAR，APP中会有多个HAR包还是只有一个？

A：会存在多份。每个使用方都会拷贝一份HAR到对应模块，造成包体积增大，如果是重复资源等大体积文件，建议使用HSP替换。

Q：在HAR包中是否可以创建AbilityStage，该AbilityStage的生命周期什么时候执行？

A：不能。AbilityStage与HAP包一一对应。具体关系可见下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/U6py1gXwTa2XzfO83PkVIA/zh-cn_image_0000002663796297.png "点击放大")

Q：HAR转HSP后，编译报错，该怎么排查？

A：[HAR转HSP包转换后](../harmonyos-guides/har-to-hsp.md#har转hsp的操作步骤)，需确保以下配置正确：

* 检查HAR下的module.json5中，是否设置"type": "shared"，并添加"deliveryWithInstall"。
* 检查module中hvigorfile.ts文件，是否将harTasks改为了hspTasks。
* HAR包的build-profile.json5默认会有"consumerFiles": './consumer-rules.txt' ，该项仅HAR模块可配置，为默认导出的混淆规则，需将其删除。

Q：多HSP引用同一个HAR，在A HSP中已经初始化过HAR中的值，在B HSP中使用的时候HAR中的值还是默认值，请问如何解决？

A：HAR被多个HSP引用后，会被拷贝多份至每个HSP中，所以不能多个模块共享一个HAR中实例。如涉及此场景建议用HSP替代HAR。

Q：什么场景下会用到多个HAP？

A：多个HAP主要是方便开发者模块化的管理应用，方便开发者将多HAP合理地组合并部署到不同的设备上，按需加载，减少包大小。例如支付类应用，有统一的主界面，主界面管理“扫一扫”、“收付款”、“消息”、“理财”等各个模块。其中主界面管理其他模块的逻辑在entry包中实现，而“扫一扫”、“收付款”、“消息”和“理财”等模块在不同的feature包中实现。可以同时开发多个feature包，能够实现feature包单独的开发测试，最终由entry包统一集成feature包的特性。

Q：HAP能作为共享包给其它应用使用吗？

A：不能，作为共享包给其它应用使用请使用HAR或集成态HSP。

Q：HSP怎么上传中心仓给其它三方应用使用？

A：OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。如需在应用内共享HSP，可将HSP共享包发布至私仓使用，请参考[ohpm私仓搭建工具](../harmonyos-guides/ide-ohpm-repo-overview.md)。

Q：项目中有一个entry类型的module，多个feature类型的module，如何在程序启动后指定加载feature类型的module？

A：程序启动入口module只能是entry类型，无法启动指定加载feature类型的module，但是各个module的类型可以在“entry”和“feature”之间随意指定，只要保证只有一个entry类型的module即可，程序启动就会加载这个module，可以在module的module.json5文件中修改[type属性](../harmonyos-guides/module-configuration-file.md#配置文件标签)。

Q：应用内共享HSP编译成.tgz包如何依赖外部的HAR包？

A：需要将依赖的HAR包内置于HSP包中一同编译成.tgz格式。

Q：应用内共享HSP编译成.tgz包如何依赖外部的HSP包？

A：需要将依赖的HSP包内置于HSP包中一同编译成.tgz格式或将依赖的HSP发布到私仓在共享HSP开发过程中通过版本号进行依赖。

Q：HAP可以设置为单独的进程吗？

A：在2in1和tablet设备上，针对UIAbility支持将HAP设置为独立进程，[模块独立进程](../harmonyos-guides/process-model-stage.md)。

Q：发布到应用市场APP包为什么会比HAP包小？

A：APP里编译的HAP包一般会比正常编译的HAP包小，编译APP包默认是非Debug模式，编译HAP包默认Debug模式，Debug版本相对于release版本包含了完整的调试信息和符号表，这些信息可以帮助开发者在调试过程中快速定位问题，查看变量值、函数调用栈等。此外，Debug版本没有进行混淆和优化导致包体积也会相对于release版本更大。

Q：安装时是先安装的HSP再安装的HAP。如果后续HAP有更新，是可以直接hdc install hap么？如果卸载HAP，相关依赖的HSP也会卸载吗？

A：直接hdc install xxx.hap即可，不需要卸载重装；不会卸载HSP，HSP是共享模块，可能被多个HAP共用。

Q：工程级oh-package.json中依赖A HAR模块，编译后A HAR会被打入B HSP中，实际B HSP并未依赖A HAR，且运行提示A、B循环依赖。

A：工程级oh-package.json中声明的依赖是整个项目的，会被所有模块依赖，当前不建议在工程级依赖中配置非devDependencies的依赖，即一个Hsp/Har模块的非开发态依赖都要在相应模块的dependencies和dynamicDependencies中声明。将工程级oh-package.json中声明的依赖在各自需要的模块的oh-package.json中按需声明即可。

Q：HAP依赖HSP、HAR，HSP不依赖HAR时，HSP可以使用HAR中资源吗？

A：HSP和HAR二者不存在依赖关系，HSP是不能使用HAR中资源的。

Q：在应用开发测试过程中，APP格式的包打出来没法给测试安装。

A：APP是应用市场发布格式（类似APK），包含所有HAP/HSP的压缩包，但设备无法直接安装，仅用于上架。调试阶段需将APP包拆分为散包（HAP/HSP），通过hdc工具或IDE安装，便于单模块更新。

Q：HAP/HAR/HSP是否都可以声明注册Ability和page？

A：HAP/HAR/HSP均支持在配置文件中声明abilities、extensionAbilities组件，HAP/HSP支持在配置文件中声明page页面。
