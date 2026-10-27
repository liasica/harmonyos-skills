---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-faq-0010
title: HarmonyOS 开发者中心应用信息与图标配置常见问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 常见问题 > HarmonyOS 开发者中心应用信息与图标配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:14aa59bfba55d177c1eb60fc71ffc4319c3ef5b103caae343c729616968bb53d
---

**Q：应用审核过程中，会提示【应用未配置图标的前景图和后景图，标准要求尺寸1024px\*1024px且需下载使用最新版本HUAWEI DevEco Studio进行图标再处理】的问题，不符合UX设计规范，该如何解决？**

**A**：解决方案如下：

* 审核出现问题中的提示是因为应用中配置的图标不符合UX设计规范。应用图标资源需分层，尺寸需满足规范要求：应用图标资源必须分为前景图和背景图两层，尺寸要求必须为1024px\*1024px，资源不允许自行裁剪圆角，不允许在资源内添加内间距。可参照通用应用UX体验标准中'[视觉风格](../design-guides/ux-guidelines-general-0000001760708152.md#section1353515481417)-2.1.4.3图标'章节里的判定标准。
* 官方文档[配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)引导开发者在app.json5配置文件中配置icon和label，由于module.json5配置文件中配置的icon会覆盖app.json5配置文件中的icon，需要检查是否在module.json5配置文件中也配置了icon和label：
  + 如果module.json5配置文件中的icon和label非必需，可以直接删去，减少冗余配置和错误几率。在DevEco Studio 5.0.3.800版本及之后，module.json5配置文件中的icon和label不再强制要求配置。
  + 如果使用到的某些系统API，对module.json5配置文件中的icon和label存在依赖，例如：[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)，则需要在app.json5和module.json5配置文件都配置正确的icon和label。
* 下载使用HUAWEI DevEco Studio 5.0.5.315或以上版本进行再打包，发布应用。
* 处理步骤可参考[配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)和[配置优先级和生成策略](../harmonyos-guides/layered-image.md#配置优先级和生成策略)。

**Q：按照[配置分层图标](../harmonyos-guides/layered-image.md#配置分层图标和应用名称)配置图标后，上架审核时还是会出现应用未配置图标的前景图和背景图问题。**

**A**：module.json5中的图标和标签配置优先级高于app.json5中的图标和标签配置，需确认应用的图标和标签配置引用。

**Q：应用配置图标不符合UX设计规范问题在本地解决后，如何确认已修复完成？**

**A**：可以使用HarmonyOS 开发者中心平台上的[UX测试](../app/agc-help-cloudtest-uxtest-0000002289534109.md)，UX测试完成后，可从测试报告获知修复结果。

**Q：背景图一定要纯色的吗？**

**A**：背景图要纯色的，但不能是透明的。

**Q：配置前景图背景图后，应用图标出现细微的栅格点，是什么原因？如下图所示：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/rju7RAl-RmOdA-_vcY77SQ/zh-cn_image_0000002771925300.png "点击放大")

**A**：查看前景图后发现透明区域都是栅格点，且图片不是PNG格式，导致透明区域的栅格点都显现出来，整改图片确保透明区域100%透明度，图片格式为PNG后，可解决问题。

**Q：使用uniapp开发HarmonyOS项目时，在HBuilder中配置了应用图标且尺寸和前景图要求均符合规范，但仍然提示应用未配置图标的前景图和后景图，如何解决？**

**A**：检查在uniapp内配置的图标路径是否为相对路径，相对路径配置可参考[uniapp HarmonyOS图标配置](https://uniapp.dcloud.net.cn/collocation/manifest.html#app-harmony-icons)。同时确认前景图为透明的PNG格式，后景图为纯色，尺寸符合1024px\*1024px，且不得进行裁剪。

**Q：智慧屏应用中，鼠标移到图标上时，图标后面的阴影显示为方块，如何调整？**

**A**：可参考[图标资源规范](../design-guides/application-icon-0000001953444009.md#section19341328132817)，排查图片的格式、分辨率、背景透明等是否正常。

**Q：使用1024px的双层图标后，用Image Asset生成的不同dpi的圆角图标是否还需要？是否可以删除？**

**A**：如果未使用到这些圆角图标资源，可以删除。

**Q：在HarmonyOS 开发者中心控制台对应用的自定义隐私协议链接进行修改更新后，已上线的应用客户端是否必须发布新版本并通过审核，新的隐私协议链接才可生效。**

**A**：需要更新应用版本并重新提交审核。

在HarmonyOS 开发者中心中，隐私协议链接属于“应用信息”配置范畴。根据操作规范：

1. 如需修改应用信息，点击“APP与元服务”，选择需要更改的应用，点击左侧导航栏“应用信息”进行编辑，完成后点击“下一步”，进入“新版本-准备提交”页面。
2. 在“准备提交”隐私声明中更新隐私协议链接。
3. 提交审核后，华为应用市场审核通过才会生效。

**Q：想在应用图标右上角增加数字（角标），是否可以？**

**A**：不可以。在应用图标上增加数字或版本显示文案不符合应用上架规范，审核会驳回。应用图标有严格的UX设计规范要求（必须使用分层图标、不允许在资源内添加内间距、前景图仅包含应用主体图形等），且审核指南要求图标不得包含误导性、不相关、不恰当的信息，版本号属于不相关信息。
