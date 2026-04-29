---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation
title: 代码生成
breadcrumb: 指南 > 使用AI智能辅助编程 > 智能执行 > 代码生成
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d57deefb4343691d8fcac47e2c6cb61135e882c97ef7b53d65f466205714ebc9
---

CodeGenie具备自然语言代码生成能力，在**对话框内**输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/peW83QgOQJ-1DdPvU-nolw/zh-cn_image_0000002561752899.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=BD0F847CB9376F78592FF4C27C3DBF40A7BAE102C9ABC991A568B887C7993240)发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/G9eKhlcDRMaHvO_oD6f0IA/zh-cn_image_0000002530912952.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=0096B5ED4A37AAD027207617793DCA497C4B234CF3F8790FFC04B4CBB4FBACFD)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ymoZVPBnTuarze9g-4DR2g/zh-cn_image_0000002561832877.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=4851343CF9B2D1B39C94E9C6B78FF080AFF45835568EDD160731047448F057C8)至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原；以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在**Changed Files**中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

以DevEco Studio 6.0.2 Release和DevEco Studio 6.0.1 Release版本为例说明，如下。

**DevEco Studio 6.0.2 Release**

**操作步骤**

1. 选择HarmonyOS Act智能体，在对话框输入功能描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/fZ5p_rlXTlmxFuXDx_iBmA/zh-cn_image_0000002530752966.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=5FEA351A0C0D7B8BAE9304992F73256F64D6E6F75210F7766053309BF2038367)发送，等待生成。
2. 在问答区域的**Changed Files**可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/FqcO6PqLRC2_--myGafc4g/zh-cn_image_0000002561752891.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=89AD2C40630115FDBDE2A69467249FE26D5BD77EC64E355A75EC658C8A1963B6)可接受或拒绝该文件的修改；点击**Accept All****/Reject All**按钮，接受或拒绝所有文件的修改；在编辑器右键**Local History** > **Show History**，查看历史修改文件还原代码。
3. 点击问答区中**Run**，可以编译验证；开启**Auto Run**开关，可以开启自动编译验证。Auto Run更多描述可参考[Agent配置](ide-agent-use.md#section2075893021715)。

**示例**

在index页面中添加一个可以跳转至另外页面的按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/6PzPIanbTmelWGx-dv8vPA/zh-cn_image_0000002530912954.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=ABA58102DD5E9C76116667EC1E31D867CA9297DAAF7D1B83B97CF3BAC83F03B9 "点击放大")

**DevEco Studio 6.0.1 Release****版本**

**操作步骤**

在对话区域输入代码需求描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/D7MIjC9BTP-ikmwKeycJBw/zh-cn_image_0000002530752960.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=95D7143BEFBAA4FC85432D4D830772F3D884F213C6A5BA1CE011A5A6ABD94F14)发送，将自动生成符合要求的代码段，将代码段一键复制![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/6ehqnTgsSUOW-riCvKKiDg/zh-cn_image_0000002530752956.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=EA36599A9E16F7082AD68987DD718DFA9EEAAD20CDB7BE25B19F895C512B343B)或一键插入![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ivMl3MwqSsGiTNnrA3H2ww/zh-cn_image_0000002561832885.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=0A70637B8EEB208E484550B357C47AF340239E2A20CEDF1A4F49F32EAEB40560)至编辑区当前光标位置。

**示例**

使用ArkTs语言写一段代码，在页面中间部分插入Swiper组件，其中有3个Image组件，其图片资源名分别为app.media.phone，app.media.watch，app.media.glasses。这些Image组件的宽度撑满父布局，高度为600，图片缩放类型为保持图片宽高比不变，将图片完全显示在边界内。 Swiper组件设置为自动播放，播放时间间隔为2秒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/8KTYr6ybRPePF3fYgCsMzQ/zh-cn_image_0000002530752958.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=B5AC0CFC0FF2215D9452E1C57AF1B4F30450DF0E2D8B57C7152EB145A2855076 "点击放大")
