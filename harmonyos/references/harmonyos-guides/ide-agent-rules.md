---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:22d9b2383ebd79bdc17a90aaa82ba9826e7b9694bef76ea98078172ce01cae09
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

**Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。

**Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

说明

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/meFaYAQqTJeD2FCMOt7upQ/zh-cn_image_0000002561752687.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=4776F6F76EE8606D20EA75D9305B92899245FA951CDC7FF1D2EC2765DD4AAA35)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/_ouQD-bQQYevN0V_WZqw2w/zh-cn_image_0000002530752736.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=C14C27CA570BA106C1CDF440754BB95DA3E16DE05BB6FA93F9880AAE0748F0AB)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/SLzcJRvPSj23wl0RLHlSGg/zh-cn_image_0000002575092879.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=F8CF335C2489016A74233ADE12070BBDF8C31F969126694F7B5DA7DE9D085DC1)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/L5d99MKaQByIJuss89H6yA/zh-cn_image_0000002574933315.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=5D4FB48F28D1D13FB9CB4A1F6696514F44836266F1AB398FA010AB6F7B6F539E)
3. 以有网络为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ZTXvf3WKQxmHOE9AS82OPw/zh-cn_image_0000002530752750.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=A4D446AD74FAF3D4DCBAC56D55B69F5F2C9626449C32F4F1D3049102A1847834)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/TpxLs8pvROqzpVtOhWcZtg/zh-cn_image_0000002530912740.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=5E83F14F99652528E1D721DA4A33335CAF192CC5AC560AF172A3B4A5799D4225)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/zOPhv_NFReyzir3jQZ4Y0A/zh-cn_image_0000002530752734.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=661F40DC28B1A1A351CE15D079CB1FD2D9FC01C22E9FF1B2BAD7CF0B4B652BE3)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Wfk4qKyJSNmMNMGYmoFajw/zh-cn_image_0000002530752752.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=B959726A3E0655AAA16E3BA1058C57C35BFD48D14B2D63D57A523ACB8B495D07)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Dpsx983STz2MCQ3pd3XFjw/zh-cn_image_0000002561832647.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=E32AC5D2A043487A0C170841B8CC5C84624627BE2D6F37F772CACA5BD6BDEE68)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/8SdiYP4pTmKkeD8EZCQyCg/zh-cn_image_0000002530752738.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=B3D76972DC40795A3A1CBDFA1317610EBFDB5F6452655DE55A39BC1403C4A55F)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/UCKRD-fVTNS4gZyMuZndsg/zh-cn_image_0000002530752726.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=7A4DCD485206A42D84AC9F1F1C5C5019909624E3C4BE68AD2E37570FA3B0B17A)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/uYvAowrgRN-OfIZrnGhV0w/zh-cn_image_0000002561752681.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=876F6C0F9C2D31B99D9A25FB2E74134D70F9DE950B9A1BDB3CB4BB6D72478DF8)
