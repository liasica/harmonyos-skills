---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules
title: 规则（Rules）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 规则（Rules）配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1a7d9e3ab981d0de2309e64759d28388516a67b33372abb60c529a8039d57e70
---

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

* **Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。
* **Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

**说明** 

* 规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
* 默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

## Global Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/uMVMNWqCQi2lMI5tOFbrbw/zh-cn_image_0000002779406532.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EDFAE4AFFCEA9AE09FA06E0F3C8B5688E22ACF2563869192CB9F55B3BC4BFCE)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/q7YPjKBdRs-cjyGYrd5GKQ/zh-cn_image_0000002779566500.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B21206D93DA37D2FAD5EA3BABB57D7FEE82DC764DBEC2A7C036E6C1343EDF91)按钮，选择**Rules**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/rumTxbKZTVKxq9lbhDTw8Q/zh-cn_image_0000002779406524.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=029C4012BF0BE247C92D6DD65EA58A4D22FCCC92192BA081895CE87708AC051A)
2. 选择规则长度限制，包括**Quality first**、**Token efficiency first**，默认为Token efficiency first。DevEco Studio 6.1.0 Beta2版本新增。
   * Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
   * Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/M5DMX2UtQX-d7Oba_TA7lg/zh-cn_image_0000002779566494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE926F735CE03D44235878399F2B4C28A2A357FD240BC1ABF2E39A8D94DE11E0)
3. 以有网络环境为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/0DqvON32RLen3sZmxuzhUg/zh-cn_image_0000002779566512.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=C82FACF2F95EE154564DC7BB430944750FC05532C3D84051D2792BE849B5F81E)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/dkE8V13ZRwe4mFnU8rRnkg/zh-cn_image_0000002779566508.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AE283898FF152ED6F9B4A8C6C8FACC2C8F3246595CDD547314A6B92439CAEFC)
4. 选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
   * 将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/fNpMcJE5QVOqZeNhO_HIZg/zh-cn_image_0000002779406520.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1A071949B3444F530F087969A7794545B1727727EB0BD22429ECB1A0E3643E4)编辑图标，开发者可查看具体规则内容。
   * 将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/43Oxh9cRQzqrpOVeQK4L9g/zh-cn_image_0000002779406536.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=A35C8B5D1F1B93C62B0921361D44BBEE6C7A815A0F0D6A77FB72FDC1C7827576)

## Project Rules配置

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/6aN7m8LsQkKvRpqMyCc8aA/zh-cn_image_0000002808766077.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BBF9972506280E91DB4631CE7F75C076EFACD742EF3FD1630463B4282AD74D0)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/AGEV9jxgQASCAXvc-0KMyw/zh-cn_image_0000002779566504.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8F93C12A2E23C5EA60C963CD9FAB1B9BD45ED59D7E54FF5135202B118DD1E37)按钮，选择**Rules**，进入配置页面。
2. 创建或导入Rule文件。
   * 创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
   * 导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/9p9QW3wQRcaLgX-Nx_hwoQ/zh-cn_image_0000002779406516.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=87AE403733253DB7B66471F7038B7F620175F4228CDAFE841D015C46AEEE3A15)
3. 管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/A6tFfh5cT_GV556sWq0Iwg/zh-cn_image_0000002779406528.png?HW-CC-KV=V1&HW-CC-Date=20261114T004909Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F315F1ED238831A12FB53B84BB19272272E8839B29FFA1CFEC0C4717BCFDC86)
