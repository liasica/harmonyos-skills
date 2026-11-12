---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-page-generation
title: 页面生成
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 页面生成
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c76f794ad497bc66dd8cca43363e2d9372708965dd3e8d547c0e39705cd55e4d
---

CodeGenie当前支持生成美食、旅游、购物、新闻和教育五大垂域的页面。通过自由输入、快捷模板、上传页面参考图片的方式生成应用/元服务可用的页面代码，生成结果支持实时预览，帮助开发者快速完成页面搭建。

从DevEco Studio 6.1.0 Beta1开始，生成页面后，预览时支持切换亮色和暗色模式。

从DevEco Studio 6.1.0 Beta2开始，页面生成时支持使用和切换模型。使用三方模型，预览时仅支持亮色模式；使用内置模型，预览时支持暗色和亮色模式切换；用户完成一轮会话，保存工程或清空会话后，可切换模型；支持查看历史生成信息，以及支持生成文件信息查看。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下三种方式进入页面生成窗口：
   * 在对话框输入"/"调出命令，选择**Generate UI Code**。从DevEco Studio 6.1.0 Beta2版本开始不支持。
   * 在对话框左下角下拉框选择**Generate UI Code****。**DevEco Studio 6.0.1 Beta1版本新增。
   * 在模块右键选择**New > Page** **>** **Generate Pages with AI**。DevEco Studio 6.0.2 Beta1版本新增。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/JZWlLUWDR3WaE6AsGDjMGg/zh-cn_image_0000002808767091.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5621A333E19035324CFD7CB638A8A4C7B07A62ED30429277FBF72450E55CED5 "点击放大")
2. 可以通过如下方式生成页面：
   * 在对话框输入页面主题要求，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Do7s0dWCQ0-t63wmsUj5ug/zh-cn_image_0000002808767089.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=3968ED674FB3108EF17DA98F1A82CFC6114D828DED55B3ABDA0CEE6511610970)图标，等待生成页面；
   * 勾选模板中的APP分类（APP Category）和功能模块（Feature Modules），点击**Generate Prompt**，根据提示信息生成页面；
   * 点击对话框中 **@Add Context** **> Add Image**，直接上传一张页面参考图片，等待生成页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/NQp_WfwGTOGBgdytWM0Twg/zh-cn_image_0000002808767093.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=81951CCDA9932108844C15A07C2C0C271787D59D26972D9692962045DA9A6C45 "点击放大")
3. 对生成的页面进行预览，预览时支持切换亮色和暗色模式；点击历史对话中的**Back to Current Session**回退到之前的页面；点击**Generate** **UI files**查看生成的UI文件内容；新增和修改页面/页面中的关键信息，通过多轮对话完善页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/lvrobGDdTuadJ6A6gUliDg/zh-cn_image_0000002808887179.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=83FE84721BA6852B11CAA77659B3BEED828F395ECB13E0D0D170F2418BCC152E "点击放大")
4. 点击**Save to Project**，在弹窗中设置页面名称及指定页面所保存的模块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/3zXjh9aJTjSt9X4LFKZ1BQ/zh-cn_image_0000002808887175.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C7A73789CEFA577DE0ADD96D10B37FA04F66BC399436AF2B7B8D61823E10F7F)
5. 点击**Next**将生成的代码文件及资源保存至工程中。弹窗中绿色文件为新增，蓝色文件表示该文件存在更改，点击**Finish**完成添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/iUFrHs5mT3uQ-sN-jbPKRQ/zh-cn_image_0000002808887177.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBE667E2FA5FD4E5C409F896710F0C4E1EC867065BC27C089CDF1916112E2238)
