---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-detection
title: 开发态性能检测
breadcrumb: 最佳实践 > 性能 > 性能检测 > 开发态性能检测
category: best-practices
scraped_at: 2026-11-14T08:54:13+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:a639fa93885f145a1232e7e7bedf4983cce026cc06386cd65de5e645ac4b42e6
---

## 简介

调优是通过优化应用程序提高运行速度、资源利用效率和响应时间的过程。通过对应用程序进行细致的调优，可以使应用程序更高效、更稳定。在当今数字化时代，随着应用程序变得越来越复杂和庞大，调优变得尤为重要。一个经过有效调优的应用程序不仅可以更高效地运行，还能提高应用的稳定性，提升程序的效率，减少资源的浪费，从而为用户带来更好的体验。因此，了解调优的方法和常用工具对于开发人员至关重要。

调优的过程通常包括现场复现、问题分析、确定解决方案和性能测试这几个关键步骤。现场复现是指在具体环境中复现问题，以便更好地分析和解决。问题分析阶段则是深入分析应用程序的性能瓶颈和问题根源，为后续优化提供指导。确定解决方案是根据问题分析的结果，制定具体的优化方案和措施。最后，性能测试是验证调优效果的关键步骤，通过对优化后的应用程序进行性能测试，评估改进效果。

为了有效进行调优工作，需要借助一些常用的工具。例如，性能分析工具DevEco Profiler可以监测应用的性能指标、录制Trace记录，开发者可以通过分析Trace数据，发现代码中的性能瓶颈，进而优化性能。

本文将介绍调优的方法和常用工具，帮助开发者更好地分析和解决应用程序中的性能问题，提升用户体验，实现应用程序的高效稳定运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/zh_pnBw1Ss2omd0_NGZqTQ/zh-cn_image_0000002416519594.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6379BE35B3480B03F448D5B92D332AB65FC8D95BC868FA1A1F797F4C73B907A "点击放大")

性能调优贯穿于HarmonyOS应用开发的整个生命周期中，开发前有性能最佳实践和指南等赋能套件让开发者快速上手学习，开发过程中有性能工具开发套件覆盖应用开发各阶段，应用开发完成上架后有专业的性能测试工具检查测试应用性能指标。目前DevEco Studio主要集成了四种性能工具，在不同的开发阶段各有侧重，主要分为性能问题检测类工具和性能问题分析类工具。本文重点介绍使用**性能问题检测类工具**来检测应用性能问题。

## 静态扫描工具检测应用性能问题

### Code Linter

**介绍**

静态检测工具，白盒检查代码性能问题。可配置开发者关注的性能规则，扫描结果支持跳转到代码，性能规则详情或者官网的最佳性能实践指导。

**使用方法**

在已打开的代码编辑器窗口单击右键点击Code Linter，或在工程管理窗口中鼠标选中单个或多个工程文件/目录，右键选择Code Linter > Full Linter执行代码全量检查。如图所示输入@performance，过滤性能检查结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/5BpDDKD-RUCwWJemslkoug/zh-cn_image_0000002404124977.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=902F2BDF44BC5ECF9321BEA8C44E6A63D27C7781EA64960D90C341F26401C8D3 "点击放大")

详细使用指导见：

[Code Linter代码检查](../harmonyos-guides/ide-code-linter.md)

静态性能规则全集见：

[性能规则@performance](../harmonyos-guides/ide-performance.md)

**说明** 

* 若未配置代码检查规则文件，直接执行Code Linter，将按照默认的编程规范规则对.ets文件进行检查。
* 注意[规则变更说明](../harmonyos-guides/ide-codelinter-rules-change.md)。

## 动态运行工具检测应用性能问题

### AppAnalyzer

**介绍**

应用与元服务体检工具用于对应用和元服务进行本地测试体检，并给出体检报告、分析指导以及修改建议，帮助开发者提升应用与元服务质量。在体检过程中，工具会收集应用或元服务的trace信息、代码栈、内存快照以及应用或元服务页面的截屏，并保存在本地工程目录.appanalyzer下，帮助开发者快速进行问题分析定位。

**使用方法**

启动DevEco Studio，连接设备，打开应用，依次执行以下操作：

**说明** 

在使用AppAnalyzer工具前，请确保完成以下准备工作：

1、应用已配置签名[signingConfigs](../harmonyos-guides/ide-hvigor-build-profile-app.md#section153288223224)。

2、确认模块Product配置正确。

3、关闭代码混淆：在模块级build-profile.json5配置文件中关闭代码混淆，详见：[字段说明](../harmonyos-guides/ide-build-obfuscation.md#section88021016154414)。

4、将编译模式Build Mode设置为release。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/TUKb1-rTQ9G9ob-8_FQ7xw/zh-cn_image_0000002474188572.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=7497B9498C3C06C5BBB508E3CA49C49AD41F1E7DFA4C164FB8C734B8DBD6F888)

1. 点击菜单栏Tools，选择AppAnalyzer进入AppAnalyzer页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/67F1lUQISd-DZ-tU131ofA/zh-cn_image_0000002510905945.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF6DB7770F254E581F8C6E74CAA34BA721B226DC8915C7006E8DB2769CDC45DB "点击放大")
2. 在AppAnalyzer页面，默认选择场景化体检。以页面间转场场景为例，点击“手动性能页面间转场体检”即可进入体检界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/5sK50sS6QUeVjUG-MVuTxw/zh-cn_image_0000002510868387.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE947EBB5DB5F5A2F2EC5D1687975A626A48E92F4A405A909C682AF7149E0542 "点击放大")
3. 在准备体检时，开发者需要保持手机解锁状态，待被检测应用自动安装并运行后，即表示准备完成。然后操作手机至检测页面，点击开始按钮开始体检。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/z0BX5lDcSG2EgjCbByrocg/zh-cn_image_0000002478830250.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CDA7FDE56508FFFEEA9B96B16EABF3B5751C7CA4859982E76B67415B3EB2081 "点击放大")
4. 等待界面出现“体检中，请操作手机”时，开始操作手机，等待体检工具录制和分析。操作完成后，可以点击结束按钮结束体检。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/SbxUiUZFROqAwPh-BSKgWg/zh-cn_image_0000002510870683.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=941F47A425D6675AC34CE4E4B4BAB6738A873F928236E517487EE157AC2971E4 "点击放大")
5. 等待体检工具生成报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/vPjo0bvFTrmHMwNxOZrAlA/zh-cn_image_0000002478830890.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=9004AB4C59998D426FB26CE8700DF5BB4C791F39F06B58FA5AEE67C8F6514EF9 "点击放大")
6. 查看检测结果报告，点击展开检测报告中的“页面间转场”，如果体检不为满分100，点击展开体检检测结果，若显示诊断异常（如下图中出现黄色、红色警告），则表示存在页面间转场的性能问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/CexLaOi6Ri-Fh5wIRqZIfA/zh-cn_image_0000002478831568.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=38B72F755B96D877D6972FEDBAA8D8E1A44639A9A912DD245976B009A9B5506B "点击放大")
7. 检测存在故障时，开发者可通过点击“可能故障原因”，查看详细测试结果及优化建议。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/EnPPFBSCSDWWBhAeee0YwA/zh-cn_image_0000002510871505.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=975249FD87906E0CBC80D63F1BC33D4CCB3EACDCC8CC2261362062B3BDCE080C "点击放大")

详细使用指导见：

[应用与元服务体检](../harmonyos-guides/ide-app-analyzer.md)

应用体检工具集成性能规则见：

[规则体检](../harmonyos-guides/ide-app-analyzer-rules.md)

## Testing测试报告导入体检工具分析

[DevEco Testing](../harmonyos-guides/deveco-testing.md)为开发者提供了稳定性、性能、应用基础质量等专项测试服务。通过DevEco Testing进行场景化性能测试，可检测出应用相关场景的性能问题，生成测试报告。为进一步分析定位应用问题，可将Testing测试报告导入至体检工具AppAnalyzer，从而对应用进行本地测试体检与优化。

**图1** Testing测试报告导入体检工具分析流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Lrl-VD-uSc2946Q98EDv6w/zh-cn_image_0000002416522370.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AD525B14D7433A0E2A12A50DFA144F96A4686A3B51E45E31F280A56ADA910D1 "点击放大")

Testing测试报告导入体检工具分析的过程主要包括以下步骤。

1. **DevEco Testing测试**

   使用DevEco Testing进行场景化性能测试，支持编写测试脚本和自定义测试场景对应用性能进行评估。具体使用方法和指导请见：[场景化性能测试](../harmonyos-guides-V13/perf-testing-V13.md#section12324184817324)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/hDVNDhxLSieulQiVH6yvnA/zh-cn_image_0000002416681522.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7A84BE501DAB1BA53F8D9F1D9E9ABAC8874DEF8AAB76CEED54EC455A6A413C4 "点击放大")

   **查看测试结果**

   根据DevEco Testing检测结果，查看是否存在页面间转场等场景不达标的问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/wu8a5Q-GSZOx57N08Miw2g/zh-cn_image_0000002450160661.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=A366ADABFD029213269DDFA7E0B06119159F39D43C415ECDC51F05E584A96248 "点击放大")

   **获取测试报告**

   点击导出IDE体检文件按钮，跳转至报告文件本地路径，获取DevEco Testing体检测试报告。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/bTV5AcXiQtaO5ZIB7YS0KA/zh-cn_image_0000002416521718.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DFA2B5B25A0C6BF0A44AD028EA1CB1ECF8818D2F0D93CE7A0912D864595DE47 "点击放大")
2. **体检报告导入AppAnalyzer**

   通过DevEcoTesting发现问题后，为深入分析问题，可将获取的体检报告导入体检工具AppAnalyzer进行具体定位和优化。打开DevEcoStudio，点击AppAnalyzer图标进入AppAnalyzer页面，随后点击“体检历史”按钮，跳转至历史记录页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/tpQe4fknREuiquXfnoBY0w/zh-cn_image_0000002478836312.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFCF6EFC2A2D29772C4976A54CE6F84D8DB6CED0C3AD7E213464A93DDB94129A "点击放大")

   点击“导入报告”，即可将Testing测试诊断出的体检文件导入体检工具进行解析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/z0425p4pTQKXE8JNZaa65A/zh-cn_image_0000002478833510.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=67C0F6DF8BE0DCDAFD800F9B724DEC46312116A9B03482E16773B46D8B030F17 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/UdlcSKcCRUe0LOgCZwErEg/zh-cn_image_0000002478838010.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=8345341C46757E95B422FC65051186EF5E85B2A64DBF14378DD8B220914F786D "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/GbS56F3QRPK59sxvnWklIQ/zh-cn_image_0000002510917261.png?HW-CC-KV=V1&HW-CC-Date=20261114T005128Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C29AFB34CFC3D8D2118E4CD34C939B3B635240B87331241156C87873EF2EF25 "点击放大")

   **说明** 

   检测报告导入前注意事项：

   1、请导入和当前工程包名一致的检测报告文件。

   2、请确认当前工程代码和被检测应用的版本是否一致。如果不一致，会导致诊断报告源码跳转代码行功能不准确。

   3、如果被检测应用为应用市场上架版本，无法获取应用堆栈，会导致某些诊断规则无法执行。
3. **问题分析和修复**

   解析完成后，会生成测试报告和详情报告。通过测试报告，可以定位出性能问题的页面截图、检测指标和检测结果等。

## 附录：工具检查规则项汇总表

静态检测工具

**表1**

| 规则ID（@规则集/规则） | 针对的性能场景 | 级别 | 规则描述与参考优化方案链接 |
| --- | --- | --- | --- |
| @performance/sparse-array-check | 通用性能场景-ArkTs编程规范 | suggestion | 建议[避免使用稀疏数组](bpta-arkts-high-performance.md#section986811417525)。 |
| @performance/number-init-check | 通用性能场景-ArkTs编程规范 | suggestion | 该规则将检查[number是否正确使用](../harmonyos-guides/arkts-high-performance-programming.md#number类型变量避免整型和浮点型混用)。 |
| @performance/typed-array-check | 通用性能场景-ArkTs编程规范 | suggestion | [数值数组推荐使用TypedArray](../harmonyos-guides/arkts-high-performance-programming.md#数值数组推荐使用typedarray)。 |
| @performance/hp-arkui-image-async-load | 丢帧-通用丢帧 | suggestion | 建议[大图片使用异步加载](bpta-click-to-click-response-optimization.md#section715115119192)。 |
| @performance/hp-arkui-load-on-demand | 丢帧-滑动丢帧 | warn | 建议[使用按需加载](bpta-best-practices-long-list.md#section69931513103314)。 |
| @performance/hp-arkui-remove-container-without-property | 丢帧-通用丢帧 | suggestion | 建议尽量[布局优化指导](../doccenter-capabilities/arkts-layout-optimization-guidance.md)。 |
| @performance/hp-performance-no-closures | 通用性能场景-ArkTs编程规范 | suggestion | 建议[函数内部变量尽量使用参数传递](bpta-arkts-high-performance.md#section493912404613)。 |
| @performance/hp-arkui-avoid-empty-callback | 通用性能场景-ArkUI编程规范 | suggestion | [避免设置空的系统回调监听](bpta-time-optimization-of-the-main-thread.md#section1193294163616)。 |
| @performance/hp-arkui-no-state-var-access-in-loop | 丢帧-通用丢帧 | warn | [在for、while等循环逻辑中频繁读取状态变量导致性能下降](../doccenter-capabilities/arkts-state-management-faq-inner-component.md#在forwhile等循环逻辑中频繁读取状态变量导致性能下降)。 |
| @performance/hp-arkui-use-local-var-to-replace-state-var | 丢帧-通用丢帧 | warn | 建议查看[状态管理常见问题](../doccenter-capabilities/arkts-state-management-faq.md)。 |
| @performance/hp-arkui-use-row-column-to-replace-flex | 丢帧-通用丢帧 | suggestion | 建议[合理使用布局组件](../doccenter-capabilities/arkts-layout-optimization-guidance.md#合理使用布局组件)。 |
| @performance/hp-arkui-combine-same-arg-animateto | 丢帧-动效丢帧 | warn | 建议[多次animateTo时统一更新状态变量](../doccenter-capabilities/arkts-animation-usage-guide.md#多次animateto时统一更新状态变量)。 |
| @performance/hp-arkui-no-func-as-arg-for-reusable-component | 丢帧-滑动丢帧 | warn | [避免使用函数作为复用的自定义组件创建时的入参](https://developerlf.hwcloudtest.cn/consumer/cn/doc/best-practices/bpta-component-reuse#section18721184816136)。 |
| @performance/hp-arkui-set-cache-count-for-lazyforeach-grid | 丢帧-滑动丢帧 | suggestion | 建议在Grid下使用LazyForEach时[设置合理的cacheCount](bpta-best-practices-long-list.md#section11667144010222)。 |
| @performance/hp-arkui-use-object-link-to-replace-prop | 丢帧-通用丢帧 | warn | 建议[使用@Link/@ObjectLink替代@Prop以减少深拷贝](../doccenter-capabilities/arkts-component_reuse.md#使用linkobjectlink替代prop以减少深拷贝)。 |
| @performance/hp-arkui-use-reusable-component | 丢帧-滑动丢帧 | warn | 建议复杂组件的定义，尽量使用[自定义组件复用开发实践](../doccenter-capabilities/arkts-component_reuse.md)。 |
| @performance/hp-arkui-use-scale-to-replace-attr-animateto | 丢帧-动效丢帧 | warn | 建议[使用图形变换属性变化组件](../doccenter-capabilities/arkts-animation-usage-guide.md#使用图形变换属性变化组件)。 |
| @performance/hp-arkui-use-word-break-to-replace-zero-width-space | 通用性能场景-ArkUI编程规范 | suggestion | 建议[使用word-break替换零宽空格(\u200b)](bpta-time-optimization-of-the-main-thread.md#section193673511440)。 |
| @performance/hp-arkui-remove-redundant-nest-container | 丢帧-通用丢帧 | suggestion | [避免冗余的嵌套](bpta-component-nesting-optimization.md)。 |
| @performance/high-frequency-log-check | 通用性能场景-高耗时函数处理 | warn | [不建议在高频函数中使用Hilog](bpta-time-optimization-of-the-main-thread.md#section10112623611)。 |
| @performance/hp-arkui-use-grid-layout-options | 丢帧-通用丢帧 | warn | 建议[在指定位置时使用GridLayoutOptions提升Grid性能](bpta-improve_grid_performance.md)。 |
| @performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse | 丢帧-通用丢帧 | suggestion | [避免对@Link/@ObjectLink/@Prop等自动更新的状态变量，在aboutToReuse()中重复赋值](../doccenter-capabilities/arkts-component_reuse.md#避免对linkobjectlinkprop等自动更新的状态变量在abouttoreuse中重复赋值)。 |
| @performance/hp-arkui-replace-nested-reusable-component-by-builder | 丢帧-通用丢帧 | warn | 建议[使用@Builder替代嵌套的自定义组件](bpta-component-nesting-optimization.md#section1012953161217)。 |
| @performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component | 丢帧-滑动丢帧 | warn | 建议[使用reuseId标记布局发生变化的组件](../doccenter-capabilities/arkts-component_reuse.md#使用reuseid标记布局发生变化的组件)。 |
| @performance/hp-arkui-use-onAnimationStart-for-swiper-preload | 丢帧-滑动丢帧 | warn | 建议[Swiper预加载机制搭配 OnAnimationStart 接口回调使用](bpta-swiper_high_performance_development_guide.md#section8783121513246)。 |
| @performance/hp-arkui-no-stringify-in-lazyforeach-key-generator | 丢帧-滑动丢帧 | warn | [在使用LazyForEach进行组件复用的key生成器函数里，不要使用stringify](bpta-lazyforeach-optimization.md#section68711519072)。 |
| @performance/start-window-icon-check | 响应时延-冷启动响应时延 | suggestion | [启动页图标分辨率建议不超过256 \* 256](bpta-application-cold-start-optimization.md#section5953164714132)。 |
| @performance/waterflow-data-preload-check | 丢帧-滑动丢帧 | suggestion | 建议[对waterflow子组件进行数据预加载](bpta-waterflow-performance-optimization.md#section12893102412329)。 |
| @performance/hp-arkui-use-attributeUpdater-control-refresh-scope | 丢帧-通用丢帧 | suggestion | 建议[使用attributeUpdater实现组件属性的部分刷新](../doccenter-capabilities/arkts-component_reuse.md#使用attributeupdater实现组件属性的部分刷新)。 |
| @performance/hp-arkui-use-id-in-get-resource-sync-api | 通用性能场景-高耗时函数处理 | suggestion | 建议[在使用API getColorSync和getStringSync时建议使用带id版本](bpta-time-optimization-of-the-main-thread.md#section193673511440)。 |
| @performance/hp-arkui-use-transition-to-replace-animateto | 丢帧-动效丢帧 | warn | 建议[转场动画](../doccenter-capabilities/arkts-animation-transition.md)。 |
| @performance/hp-arkui-remove-redundant-state-var | 丢帧-通用丢帧 | suggestion | 建议[学习UI范式状态管理](../doccenter-capabilities/arkts-state-management.md)。 |
| @performance/hp-arkui-use-taskpool-for-web-request | 完成时延-应用内点击完成时延 | warn | 建议[网络资源的请求和返回使用taskpool线程池异步处理](bpta-time-optimization-of-the-main-thread.md#section32971936174416)。 |
| @performance/hp-arkui-remove-unchanged-state-var | 丢帧-通用丢帧 | suggestion | 建议查看[学习UI范式状态管理](../doccenter-capabilities/arkts-state-management.md)。 |
| @performance/hp-arkts-no-use-any-export-current | 完成时延-冷启动完成时延 | warn | [避免使用export \* 导出当前module中定义的类型和数据](bpta-application-cold-start-optimization.md#section584818173141)。 |
| @performance/hp-arkts-no-use-any-export-other | 完成时延-冷启动完成时延 | warn | [避免使用export \* 导出其他module中定义的类型和数据](bpta-application-cold-start-optimization.md#section584818173141)。 |
| @performance/hp-arkui-suggest-cache-avplayer | 音视频播放-启播速度 | warn | 建议[缓存AVPlayer实例減少起播时延](bpta-smooth-switching.md)。 |
| @performance/hp-arkui-suggest-use-effectkit-blur | 丢帧-通用丢帧 | suggestion | 建议[对比动态模糊与静态模糊](../doccenter-capabilities/ui-dynamic-vs-static-blur-examples.md)。 |
| @performance/multiple-associations-state-var-check | 丢帧-通用丢帧 | suggestion | 多个组件关联同一数据时，建议在组件中使用[@Watch装饰器：状态变量更改通知](../doccenter-capabilities/arkts-watch.md)。 |
| @performance/foreach-args-check | 丢帧-滑动丢帧 | warn | 建议[在ForEach参数中设置keyGenerator](../harmonyos-guides/arkts-rendering-control-foreach.md#渲染性能降低)。 |
| @performance/constant-property-referencing-check-in-loops | 通用性能场景-ArkTs编程规范 | suggestion | 在循环如需频繁访问某个常量，且该属性引用常量在循环中不会改变，建议提[取到循环外部，减少属性访问的次数](../harmonyos-guides/arkts-high-performance-programming.md#循环中常量提取减少属性访问次数)。 |
| @performance/hp-arkui-reduce-pangesture-distance | 响应时延-应用内点击响应时延 | suggestion | 建议[设置合理的拖动距离](bpta-application-latency-optimization-cases.md#section1116134115286)。 |

动态运行工具规则请参阅[规则总览](../harmonyos-guides/ide-app-analyzer-all-rules.md#section355112916333)。
