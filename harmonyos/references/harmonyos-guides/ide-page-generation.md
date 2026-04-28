---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-page-generation
title: 页面生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 页面生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb8fbafda181ac19ba7c2049515a288813554819ebe86868dbb5622fc331f56f
---

CodeGenie当前支持生成美食、旅游、购物、新闻和教育五大垂域的页面。通过自由输入、快捷模板、上传页面参考图片的方式生成应用/元服务可用的页面代码，生成结果支持实时预览，帮助开发者快速完成页面搭建。

从DevEco Studio 6.0.1 Beta1开始，在输入框新增页面生成的入口。

从DevEco Studio 6.0.2 Beta1开始，在模块右键新增页面生成的入口Generate Pages with AI。

从DevEco Studio 6.1.0 Beta1开始，生成页面后，预览时支持切换亮色和暗色模式。

从DevEco Studio 6.1.0 Beta2开始，不支持在对话框输入"/"调出命令，选择Generate UI Code进入页面生成窗口的功能；页面生成时支持使用和切换模型。使用三方模型，预览时仅支持亮色模式；使用内置模型，预览时支持暗色和亮色模式切换；用户完成一轮会话，保存工程或清空会话后，可切换模型；支持查看历史生成信息，以及支持生成文件信息查看。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下三种方式进入页面生成窗口：
   * 在对话框输入"/"调出命令，选择**Generate UI Code**。从DevEco Studio 6.1.0 Beta2开始不支持。
   * 在对话框左下角下拉框选择**Generate UI Code****。**
   * 在模块右键选择**New > Page** **>** **Generate Pages with AI**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/c29j3-ouRD-lQBuIiFsWxA/zh-cn_image_0000002530753720.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=9024C662BF09710D0F062CB54831102F10997CD56F0256D29F37E58AC6C7A925)
2. 可以通过如下方式生成页面：
   * 在对话框输入页面主题要求，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/4n_33zXrS8uWkuMLYaYzog/zh-cn_image_0000002530753724.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=AA4EC04421D22A5480D6D68EB2D71249E7C60C93DB7F60D78F2E718844E38350)图标，等待生成页面；
   * 勾选模板中的APP分类（APP Category）和功能模块（Feature Modules），点击**Generate Prompt**，根据提示信息生成页面；
   * 点击对话框中 **@Add Context** **> Add Image**，直接上传一张页面参考图片，等待生成页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Rz6efv_eQVWekCaiKbKBwA/zh-cn_image_0000002561753659.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=630BB56F56A2B418D27D14E0C7ECA85D9426CA7B762F7121B00556F0E51FDB92)
3. 对生成的页面进行预览，预览时支持切换亮色和暗色模式；点击历史对话中的**Back to Current Session**回退到之前的页面；点击**Generate** **UI files**查看生成的UI文件内容；新增和修改页面/页面中的关键信息，通过多轮对话完善页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/qycy3IDlR0SQOV9Unh-gzg/zh-cn_image_0000002530913714.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=6744C037194FBC53F95CDF1D8FA6572B26608963E43427A3DC1250D9C0EF583A)
4. 点击**Save to Project**，在弹窗中设置页面名称及指定页面所保存的模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/jly40nMjSAitD2iffbm2WA/zh-cn_image_0000002561833639.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=324BE790D58189046D5A7997DCA67D170FF33A01EBA92654AAAF109474E4371E)
5. 点击**Next**将生成的代码文件及资源保存至工程中。弹窗中绿色文件为新增，蓝色文件表示该文件存在更改，点击**Finish**完成添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/YjiUP3N3R9y2Y7h6VEmueQ/zh-cn_image_0000002561753661.png?HW-CC-KV=V1&HW-CC-Date=20260427T235514Z&HW-CC-Expire=86400&HW-CC-Sign=2FD9E00E35C08B3478872EC8675BF2E8EF93685D07F5C90A6A5ADC0EED0DCD85)
