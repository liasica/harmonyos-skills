---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a8da3ab67d7a6cd60dcb17b0db5fa8f7857649ebd129fe874aa6b03cd651db81
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

**Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。

**Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

说明

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/1vYsD615T6mDPiQwcQvhug/zh-cn_image_0000002561752687.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=9D1BF9027066101214C7BEF0DEAED685BEF20B4F2A2EE69195CB4352B61ABCD3)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/_M9Ae45NSfC31Fuf7XAGNQ/zh-cn_image_0000002530752736.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=6FD092F28E69FA8D2C3F8C4728106F99F6D1BACFA751B220F4A8D5081DBB928A)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/PxfSuuivTM6mRNcH_byLPA/zh-cn_image_0000002575092879.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=48B2BE4B0ED54C3B6924C089D3DA6160674045F755AD37D6D37C8ED134BEC470)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/mMbtbz2HTVGeLHjYbjuHZQ/zh-cn_image_0000002574933315.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=35930ECCF564F31CF26BC6BB8F1C35E7E810CACB256B68957E79967FC71246CD)
3. 以有网络为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/V5tujzC4St-zoEgZn-dsXg/zh-cn_image_0000002530752750.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=2B361A8B121C5C26224FEA692A69E43BFC4967C3501F7CE985D181E348338316)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/IOLHdoMNTVWmgRLol9TuUw/zh-cn_image_0000002530912740.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=7016318946EB626E03B704AF080186C74473F2848EBBDE262B700776C8D45291)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/41YMiGM-SWyaHQ_XE6uBIQ/zh-cn_image_0000002530752734.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=A4DA14D2EF0959204AA0B36C1904D8B996CC45BD4470C230D603231831281041)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/u8UY9by4R2Sq6Zr0_XcgvQ/zh-cn_image_0000002530752752.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=EC4D59FAEF8305ED9B07788AAA73D0C70C5E0160485FDDA8D9602C1840DE2B40)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/b0t10qtUT3uJCRCwLPX5_w/zh-cn_image_0000002561832647.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=CB8568689916F128C161B2DED5B7871AA3E1BE258F99DEDA3B49CEC9B4B86A56)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/AwFgDBteTLOGWIZKRuhGTw/zh-cn_image_0000002530752738.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=ED5338BCD98D2D5DF75A2579E8BC3D80C6DD991B38E7CA2D8E5BE0E7917ED106)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/qrsX-vtXT5-yfU0hzAtGvg/zh-cn_image_0000002530752726.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=8BD1745B060AA83ED033C136A909363DFC74680334DA6FD4FB1D17BB81FD5743)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/pIFNueCjRryivpEY4b6zoA/zh-cn_image_0000002561752681.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=CA0E4BF1B86920410CBC8553B3117A318C2D3E920B89CDAA6C9C1DD8A2040FDB)
