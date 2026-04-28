---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f65bbf6a73ab2619127ca6d5b463968e5b4eb9d3d5a11b16ba1518b780175eb2
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/ihhFmoq1SCOp2qjNrUkO6g/zh-cn_image_0000002561752899.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=67F906DF0E94790FEE0407923847581E3D06F56837024C0C73EA6C804FE905D8)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/FkUDTcXTQJKRrGNjz9TIhA/zh-cn_image_0000002530912952.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=0798023759A4A8BAFE09BD6E479B1D28D10191FF417731F93711727D1B6E51AD)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/DfjIJy8FSHKblPS9KVNl8g/zh-cn_image_0000002561832877.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=62A69EBCFE7886404DF3A717782C88C275C4933246679C51AE3FF525CC871177)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原；以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

以DevEco Studio 6.0.2 Release和DevEco Studio 6.0.1 Release版本为例说明，如下。

**DevEco Studio 6.0.2 Release**

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/G9H8LM5rSnKCSZpCZOB5cQ/zh-cn_image_0000002530752966.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=032EE06BBF5FF10A17FED849B85027AF1811CD4108ED46656A0FA824CBFADBCB)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Oia7jMeaQxGqXNxWvB9TKQ/zh-cn_image_0000002561752891.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=FC39AAC7FC143E1854C0DEBB33EBDE6FB414155A9E4F641C4CA403E5985C735F)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/vig4ftjjTCOT6zp5K2_jKg/zh-cn_image_0000002530912954.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=FAE94FA4A0C0AFDE15BDB8D6676F8A5DF77D10239AF59DAB162F4043C6F9F7BA "点击放大")

**DevEco Studio 6.0.1 Release****版本**

**操作步骤**

在对话区域输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/hWLh4ZimRmeDZgL6jCroZQ/zh-cn_image_0000002530752960.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=06DDF1CBB2C303F09D95C5F211C26D709EB607BB9E8A2EF2D0C044FDFE0F324C)发送，将自动生成符合要求的代码段，将代码段一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/kGdjYNjpReewKopwQmpEtg/zh-cn_image_0000002530752956.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=E0FC76C6494D9075299340925DE3B6EA84605680405EECE1D250BF9C36DE358C)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/Dl8uN94xQKuNefFbiXuuUw/zh-cn_image_0000002561832885.png?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=44BF692C094D2EA1EB027E8B29360EE592851AAC8B0BC3E21007408F94CB0C92)至编辑区当前光标位置。

**示例**

使用ArkTs语言写一段代码，在页面中间部分插入Swiper组件，其中有3个Image组件，其图片资源名分别为app.media.phone，app.media.watch，app.media.glasses。这些Image组件的宽度撑满父布局，高度为600，图片缩放类型为保持图片宽高比不变，将图片完全显示在边界内。 Swiper组件设置为自动播放，播放时间间隔为2秒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/goLDI26dRxSO463CZnFLOw/zh-cn_image_0000002530752958.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235512Z&HW-CC-Expire=86400&HW-CC-Sign=646B11ACC0B13D82CD63B57F1FBC8E780F3A28234E6756ED3D512DE62C511CD0 "点击放大")
