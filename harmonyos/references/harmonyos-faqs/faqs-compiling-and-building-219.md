---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-219
title: 如何进行App加固操作
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何进行App加固操作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:3fc4cd48466fb155764774674b02c314aeab218051f47ff62b2231b1f9dc12e3
---

## 问题现象

开发的过程中，为了保护开发的App不被恶意破解，如何对App进行加密，混淆操作？

## 背景知识

* HarmonyOS[反编译](faqs-data-prevention-9.md)安全性提供基础的应用加固安全能力，包括混淆、加密和代码签名，保护代码免受反编译和反调试。高级混淆功能目前由第三方支持。
* 当前提供的加固方式有：混淆，加密。
  + [代码混淆](../harmonyos-guides/ide-build-obfuscation.md)：在编译的过程中，IDE根据配置的混淆规则对项目代码进行混淆处理。
  + [应用加密](../harmonyos-guides/code-protect.md)：应用加密特性在应用上架时加密，应用运行时按需解密安全增强的同时，确保开发者、消费者无感的安全体验，避免应用开发者适配工作，保障用户无感的纯净安全体验。

## 解决方案

* 代码混淆：代码混淆是一种软件安全技术，旨在增加代码的复杂性和模糊性，从而增加攻击者分析和理解代码的难度。
  1. 开启混淆能力：Stage模型的工程在**Release编译模式**下[使能混淆](../harmonyos-guides/ide-build-obfuscation.md#section18326541833)，从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，默认不开启混淆。
  2. 混淆配置能力：混淆配置文件obfuscation-rules.txt默认开启了四项推荐的混淆选项：**-enable-property-obfuscation**、**-enable-toplevel-obfuscation**、**-enable-filename-obfuscation**和 **-enable-export-obfuscation**，开发者可以根据需要进一步修改混淆配置。如果存在多个混淆规则文件，则可以参考[混淆规则合并策略](../best-practices/bpta-app-code-ob.md#section1842224516252)。
  3. 配置保留选项：代码中可能有部分字段，方法不希望被混淆，这个时候可以通过配置混淆白名单，参考[保留选项](../harmonyos-guides/source-obfuscation-keep-options.md)。混淆常见案例汇总可以查看[扫描任务](../harmonyos-guides/ide-build-obfuscation.md#section18125192133818)中的混淆示例。
* 应用加密：为了保护应用代码安全，保护开发者的核心资产，HarmonyOS提供了端到端的应用代码保护机制，该机制以系统安全为基础，构建内核级应用生命周期内的代码安全保护能力。 **开发者向应用市场提交上架申请，上传应用包后可选择是否加密。选择加密的应用，在经过应用市场审核后，应用市场会对上架应用做代码加密。** 应用在设备上安装时，安装文件落盘后仍是处于加密状态，有效的保护应用程序；当应用程序启动时按需解密。应用加密采用标准AES加密算法，解密后的明文只存在于内存中，不会存储到设备。

## 常见FAQ

Q：使用官方提供的代码加密能力后，应用代码是否需要其它的代码保护措施吗？

A：应用加密特性可以有效提高应用代码文件逆向分析的难度，但应用代码防逆向是一个持续攻防对抗的过程，如对代码文件保护有更高的要求，需要结合其他安全加固措施，进一步提高逆向分析应用的难度。比如使能混淆能力、使能三方安全加固能力等。

Q：如果不使用代码加密能力，还能采取什么手段来保护应用代码资产？

A：使能混淆能力、使能三方安全加固能力等，请参考[应用资产保护设计-保护应用代码场景](../best-practices/bpta-app-asset-protection-design.md#section24320461547)。

Q：代码加密会对应用包产生什么影响？

A：加密后的应用在程序启动和运行过程中可能会小幅度增加性能开销；加密后的应用相比于不加密的应用体积更大，可能会小幅度增加下载和安装时间。

Q：App中依赖了其他自研so库，如何对so进行加固？

A：在HarmonyOS开发场景下，应用的代码分为C/C++等实现的代码，最终的编译产物主要为.so文件。其中.so文件由于反编译难度较大，代码逆向困难。so的加固可以使用三方提供的应用安全加固保护，部分[三方安全厂商](https://developer.huawei.com/consumer/cn/market/prod-list/a97c5f2de7df49f49c139a32125fa4c8/categoryL2_202404220005?categoryIdL3=categoryL3_202403120002)已支持HarmonyOS系统，具体方法请参考[使用第三方加固](../harmonyos-guides/source-obfuscation-apply-code.md#使用第三方加固)。

Q：使用三方加固包加固签名后，App上传解析失败，报错993。

A：非自研SDK被混淆影响应用市场审核相关SDK的指纹信息，不允许混淆非自研的SDK，对非自研SDK配置混淆白名单。

Q：HarmonyOS系统中三方SDK需要单独加固吗。

A：机制上代码混淆是支持SDK的，业务上自己做功能加固。

Q：开启混淆后，使用jadx反编译modules.abc文件可看到class中的属性名称，如何混淆属性名称？

A：混淆属性名称需要在项目混淆规则文件中配置[-enable-property-obfuscation](../harmonyos-guides/bytecode-obfuscation.md#section-enable-property-obfuscation)。

Q：在应用加密的基础上是否还有必要做加固？应用加密的安全等级如何？能否避免防逆向、防调试吗？

A：原则上不建议做加固，安全是相对的，当前阶段应用加密可以保证防逆向和防调试。

Q：由于应用开发内部流程需要在应用上架前进行反编译等逆向风险加固，如何处理？

A：因为应用加密是应用提交上架申请时选择触发，所以上架前的应用加固可以使用三方加固工具进行，可参考已支持HarmonyOS系统的[三方安全风控类SDK](https://developer.huawei.com/consumer/cn/market/prod-list/a97c5f2de7df49f49c139a32125fa4c8/categoryL2_202404220005?categoryIdL3=categoryL3_202403120002)。

Q：国标"6.3.1客户端应用程序自身安全"提到：采取防动态调试、代码混淆、防逆向等技术措施，HarmonyOS应用加密是否满足要求？

A：HarmonyOS系统具备反调试，反篡改，反逆向功能。其中，反逆向是通过代码加密保护；反篡改主要是应用市场上架的签名保护，安装应用时会校验应用签名，被篡改的应用验签过不了无法安装；反调试是系统本身对调试就做了限制，通过系统限制达到反调试的目的。

Q：开启代码混淆后，安装包解压仍能看到配置文件中的明文内容，如何处理？

A：代码混淆主要针对JS/TS代码生效，无法对配置文件中的明文内容进行混淆。若需进一步提升代码安全性，建议使用第三方安全厂商提供的高级混淆与加固能力，具体可参考[使用第三方加固](../harmonyos-guides/source-obfuscation-apply-code.md#使用第三方加固)。
