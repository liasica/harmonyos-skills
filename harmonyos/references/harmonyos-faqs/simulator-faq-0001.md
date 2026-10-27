---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/simulator-faq-0001
title: 模拟器真机预览器调试差异常见问题
breadcrumb: FAQ > DevEco Studio > 模拟器 > 常见问题 > 模拟器真机预览器调试差异常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:03+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:42f963d3ef5e60724fe3f8fa2647441fc0c54ba6614ef2a0da3815310a78642b
---

**Q：根据官方文档给出的示例[如何拉起浏览器应用](faqs-ability-58.md)，使用预览器查看Demo效果，控制台报错日志信息Error message:is not callable. 使用模拟器进行调试，也无法拉起浏览器应用。当前无真机设备。调试过程中，模拟器、真机、预览器具有哪些差异？**

**A**：编译方式和环境配置对比：

* 模拟器和真机：它们的编译方式更为严格，能够更准确地反映应用在实际设备上的运行情况。例如，它们可能会更严格地检查API使用是否符合设备的硬件和软件环境。
* DevEco Studio预览器：预览器的主要目的是提供快速的代码修改和界面预览，它可能不会进行完整的编译和安装过程，因此在某些情况下，预览器中运行的代码可能与在模拟器或真机上运行的结果不完全一致。

显示效果对比：

* 模拟器：
  + 通常旨在模仿特定设备的屏幕尺寸和分辨率，有时可能不会完全准确，特别是在处理特定设备的独有特性时。
  + 电脑屏幕的色域范围可能与移动设备不同，从而导致颜色显示不准确。
  + 模拟器不支持屏幕亮度调节。
* 真机：能够提供最真实的显示效果，因为它是实际的物理设备。
* DevEco Studio预览器：可能为了快速显示而简化了一些图形渲染过程，导致与模拟器或真机的显示效果有所不同。例如，预览器可能不会考虑所有的屏幕适配问题，或者不会完全模拟所有的硬件特性；一个预览器只能支持普通预览或预览调试模式，不可同时支持两种模式。使用预览器进行调试不支持以下场景：
  + 不支持Attach调试。
  + 不支持跨Ability调试。
  + 不支持C++调试。
  + 不支持Hot Reload。
  + 不支持多进程和worker/taskpool调试。

调试能力对比：

* 模拟器和真机：支持完整的调试功能，包括断点设置、代码步进、变量监控等。
* DevEco Studio预览器：虽然也支持一定的调试功能，如设置断点和调试执行，但不支持所有类型的调试，例如不支持Attach、跨Ability调试和C++调试。具体约束条件可查看官方文档：[使用预览器调试的特别说明](../harmonyos-guides/ide-debug-device.md)。

官方文档[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)清楚的描述了模拟器对各种Kit的支持情况，开发者在无真机或者模拟器不具备支持能力的情况时可以使用[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust?ha_source=sousuo&ha_sourceId=89000251)。

**Q：使用模拟器进行HarmonyOS NEXT系统调试都支持哪些设备类型？**

**A**：模拟器已支持的系统类型有：Windows(X86)和macOS(ARM)，已支持的设备类型为：手机（包括折叠屏）、平板、Wearable、2in1。具体可参考每版本的发布指南：[支持的设备类型](../harmonyos-guides/ide-emulator-devicetype.md)。

**Q：预览器支持哪些组件？NavDestination组件支持使用预览器吗？**

**A**：[NavDestination组件](../harmonyos-references/ts-basic-components-navdestination.md)支持使用预览器。支持使用预览器的ArkTS组件详见[官方指南](../harmonyos-guides/ide-previewer-api-list.md#section280418414305)。

**Q：引用了HSP的模块是否支持预览？**

**A**：预览不支持引用HSP。引用了HSP的模块不支持预览，需要直接在HSP内预览或模拟HSP。官方文档中已给出说明，详见[查看ArkTS/JS预览效果](../harmonyos-guides/ide-previewer-arkts-js.md)。

**Q：手机模拟器里面能否使用浏览器之类的搜索功能，或者通过应用市场之类的安装应用？**

**A**：手机模拟器不支持浏览器和应用市场，若场景需要可以使用真机或者[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust?ha_source=sousuo&ha_sourceId=89000251)。

**Q：点击了预览器中的Inspector后，就看不到界面的预览效果了，会出现这样的一个提示：add preview by decorating components。**

**A**：Inspector双向预览支持ets文件与预览器界面的双向预览。@Entry装饰器装饰的组件支持Inspector，@Preview不支持。使用双向预览功能时确保组件被@Entry修饰。

**Q：模拟器里无钱包服务App，导致依赖了钱包拉活SDK的应用，在模拟器里运行会发生异常。具体报错如下：**

```txt
LastFatalMessage:[default] [LoadJSPandaFile:108] resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit.hsp
```

**A**：该报错是因为Kit在模拟器不支持，可以参考：[Kit能力差异](../harmonyos-guides/ide-emulator-specification.md#section139481235225)。当前walletkit不支持在模拟器上使用，建议使用真机进行调试。如遇到因Kit能力不支持导致的应用闪退问题，可以使用[动态引入Kit](../harmonyos-guides/arkts-dynamic-import.md#动态import实绍介绍)的方式规避此异常问题。

**Q：模拟器能安装apk或卓易通吗？**

**A**：模拟器主要是提供给用户做HarmonyOS NEXT应用调试，不支持安装apk或卓易通。

**Q：DevEco Studio的预览器有深色模式吗？**

**A**：预览器暂不支持深色模式，请使用模拟器或真机进行测试。

**Q：模拟器是否支持开启root权限？**

**A**：模拟器暂不支持root。

**Q：模拟器可以使用WiFi吗？**

**A**：模拟器暂不支持通过连接WiFi访问互联网，模拟器上网实际走的是以太网，跟电脑共享同一网络。是否连接WiFi并不影响互联网连接。

**Q：华为轻量穿戴应用使用模拟器运行时提示页面.js超过48kb，怎么解决这个限制？**

**A**：由于设备上空间小，当前文件有大小限制，且这种限制不支持开发者自己修改，建议控制文件大小在限制的范围之内。

**Q：接入高德SDK，发现无法在模拟器上运行，是不支持在模拟器上运行吗？**

**A**：目前高德SDK不支持在模拟器上定位，请使用真机或者云调试。目前HarmonyOS 5及以上应用/元服务仅支持单机调试场景。单机调试：申请单台设备进行调试，用于调试应用在指定机型上的表现。

**Q：使用SafetyDetect进行设备安全检测，为什么调用checkSysIntegrity在真机(未root)运行正常，在模拟器中报错？**

**A**：该报错是因为SafetyDetect属于Device Security Kit（设备安全服务）而模拟器不支持该Kit，可以参考：[Kit能力差异-安全](../harmonyos-guides/ide-emulator-specification.md#section147193483010)。建议使用真机进行调试以规避该报错。

**Q：预览器是否支持根据module.json5的orientation配置自动切换横竖屏？**

**A**：预览器不支持页面自动旋转，预览器页面上提供了orientation按钮，可以点击该按钮切换设备的横竖屏状态。

**Q：使用API20模拟器加载ArkWeb组件时页面出现倒转？**

**A**：参考模拟器[使用环境要求](../harmonyos-guides/ide-emulator-requirements.md)，图形倒转是GPU显示驱动版本过低导致的，需要GPU支持OpenGL版本4.1及以上，AMD的GPU显示驱动版本不能低于24.1.1。

**Q：应用编译通过且能生成HAP/APP包，但使用模拟器调试时提示设备rpcid.json文件中不包含部分系统能力属性（如SystemCapability.Multimedia.Media.AVTranscoder、SystemCapability.Communication.Bluetooth.Core等），如何处理？**

**A**：该报错是模拟器的系统能力集不完整导致的，与应用编译是否通过无关。编译通过仅说明代码和SDK API编译通过，但推到模拟器调试时，IDE会检查设备rpcid.json中声明的SystemCapability，发现模拟器不具备应用或依赖库要求的能力时就会拒绝运行。常见不支持的能力包括多媒体转码、蓝牙、WiFi P2P、分布式设备管理、分布式KV、DRM、企业设备管理等。建议排查项目及依赖中是否直接或间接引入了相关Kit或三方库，如需调试这些能力请使用真机或[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust?ha_source=sousuo&ha_sourceId=89000251)，具体差异可参考[模拟器与真机的差异](../harmonyos-guides/ide-emulator-specification.md)。

**Q：在模拟器中实例化AgentController时应用崩溃，如何处理？**

**A**：[Agent Framework Kit](../harmonyos-guides/hmaf-introduction.md)暂不支持模拟器，在模拟器中实例化[AgentController](../harmonyos-references/hmaf-function-component.md#agentcontroller)会导致应用崩溃。建议使用真机进行调试，或在使用前判断当前运行环境，通过条件编译规避模拟器场景。

**Q：无真机设备时如何调试应用？**

**A**：可使用模拟器或云调试进行调试。模拟器使用方式详见[应用/元服务调试](../harmonyos-guides/ide-debug-app.md)，云调试使用方式详见[云调试](https://developer.huawei.com/consumer/cn/agconnect/cloud-adjust?ha_source=sousuo&ha_sourceId=89000251)。

**Q：没有真机和模拟器时，能否仅使用预览器完成开发？**

**A**：预览器可以承担纯UI界面的开发与调试，但对涉及网络请求、系统能力、Native代码的项目，仅靠预览器开发存在以下限制：

1. 网络请求验证结果不可信：预览器走宿主机网络栈，网络安全配置只在真机生效，预览器中网络请求成功不代表真机成功。
2. 大量组件与API无法预览：Video组件不支持实时渲染，Richtext、Web、XComponent组件受限，Ability、MultiMedia等模块API无法预览。
3. 错误难以发现和定位：超时、断网重试、错误码处理等异常路径无法触发，预览器不支持C++调试、Attach调试、跨Ability调试、Hot Reload、多进程和worker/taskpool调试。
4. 运行环境存在差异：预览器简化图形渲染，不执行完整编译安装流程，权限弹窗、系统资源调度行为均与真机不同。预览器仅用于纯UI阶段，涉及相机、定位、传感器、推送等系统能力的功能验证、Native C++调试、上架前最终测试，必须使用真机或模拟器。可参考[使用预览器调试应用](../harmonyos-guides/ide-previewer-debug.md)。

**Q：是否有以具体商用机型命名的模拟器？**

**A**：没有以具体商用机型命名的模拟器。模拟器是按设备形态/品类提供的，而非按具体商用机型命名。若需适配小折叠机型等折叠形态，可使用Foldable折叠屏模拟器进行折叠/展开场景的功能与布局测试，但需注意模拟器与真机在屏幕具体参数上存在差异，最终适配效果仍建议以真机验证为准。具体支持的设备类型可参考[支持的设备类型](../harmonyos-guides/ide-emulator-devicetype.md)。
