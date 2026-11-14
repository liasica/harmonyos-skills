---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-faq1
title: 迁移CodeGenie数据至DevEco Code常见问题
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 常见问题 > 迁移CodeGenie数据至DevEco Code常见问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:22+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:776b0c255251114b8a41ad406f98c3e056e0cc468498e4fd8ec1c574e6828adb
---

## CodeGenie数据迁移使用到的数据路径

**CodeGenie数据目录**

* macOS：~/Library/Application Support/Huawei/DevEcoStudio<版本>/codegenie/

* Windows：C:/Users/<用户名>/AppData/Roaming/Huawei/DevEcoStudio<版本>/codegenie/

**DevEco Code存储根目录**

* macOS：~/Library/Caches/Huawei/DevEcoStudio<版本>/deveco-code/v1/

* Windows：C:/Users/<用户名>/AppData/Local/Huawei/DevEcoStudio<版本>/deveco-code/v1/

## 迁移窗口提示迁移Skill或MCP配置到DevEco Code

**问题现象**

未配置CodeGenie数据，安装和打开DevEco Code插件后，出现迁移窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/G6pGSP7LQSuh9I_0DP5n1Q/zh-cn_image_0000002808766025.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6C65832E105A319AE0201E7192E7D7A9505A469B6859376A594BC21219B5B8D)

**解决措施**

打开[CodeGenie数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)确认是否存在需要迁移的数据，如果需要迁移，点击**Start Migration**；如果不需要迁移，点击**Don't remind me**。

## 迁移窗口提示中的DevEco Studio与打开的DevEco Studio版本号不一致

**问题现象**

迁移窗口提示中的DevEco Studio版本与本地打开的DevEco Studio版本号不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/1ERNiYPmQDSt3NqYcUeAMQ/zh-cn_image_0000002779566446.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D6D4E9D35B268BD1301BB3FC29779ECB6B9FA294FE593CFCB39DC13F9C31E77)

**解决措施**

该标注仅用于标识迁移数据来源的DevEco Studio版本，用户不用关注版本号问题。

打开[CodeGenie数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)确认是否存在需要迁移的数据，如果需要迁移，点击**Start Migration**；如果不需要迁移，点击**Don't remind me**。

## 迁移窗口显示不同的数据来源信息

**问题现象**

迁移窗口显示的数据来源信息有多种情况：

* 情况一：不显示版本号
* 情况二：显示一个版本号（如Global configuration from DevEco Studio 26.0）
* 情况三：显示两个版本号（如Global Skill from DevEco Studio 26.0，MCP from DevEco Studio 6.1）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/HeZzIVmPQce5jR4XTn0-Cg/zh-cn_image_0000002808886109.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=A67A39FC95844D86B0E539F68A7FD4E925159CD1BB7612D0AABDDD7D4768437E)

**可能原因**

Skill和MCP是两类独立的数据，迁移时独立判断数据来源，可能分属不同的DevEco Studio版本。

迁移窗口数据来源信息的显示规则如下：

* 不显示版本号：Skill、MCP数据都来自于当前使用的DevEco Studio。
* 显示Global configuration from DevEco Studio X：Skill、MCP数据来自同一个非当前使用的其他版本的DevEco Studio。
* 显示Global Skill from DevEco Studio X，MCP from DevEco Studio Y：Skill、MCP数据来自不同版本的DevEco Studio。
* 显示Global Skill/MCP from DevEco Studio X：只有Skill/MCP中一类数据，仅显示其对应的DevEco Studio版本。

**解决措施**

该标注仅用于信息展示。

打开[CodeGenie数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)确认是否存在需要迁移的数据，如果需要迁移，点击**Start Migration**；如果不需要迁移，点击**Don't remind me**。

## 从DevEco Studio版本的数据目录中迁移CodeGenie数据

**问题现象**

本地多个DevEco Studio版本数据目录中有CodeGenie数据，从哪个DevEco Studio版本的数据目录中迁移CodeGenie数据？

**解决措施**

显示的迁移数据来源规则如下，仅用于迁移信息展示。

1. Global Skill：取自有Skill文件的最高版本的DevEco Studio[数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)。
2. Project Skill：取自当前工程根目录下.codegenie/skills/。
3. MCP：取自数据库有真实数据存在的高版本的DevEco Studio[数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)。

## 点击迁移窗口中Don't remind me后，需再次重新迁移

**问题现象**

点击迁移窗口中Don't remind me后，需再次重新迁移。

**解决措施**

点击Don't remind me后，迁移标记文件（codegenie-migration.json）会记录当前工程的抑制状态，该文件位于[DevEco Code存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)的config子目录下：

* macOS：~/Library/Caches/Huawei/DevEcoStudio<版本>/deveco-code/v1/config/codegenie-migration.json
* Windows：C:\Users\<用户名>\AppData\Local\Huawei\DevEcoStudio<版本>\deveco-code\v1\config\codegenie-migration.json

删除迁移标记文件，以及在工具左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/AHfJL7kkQiqWm1Qjhxq2ag/zh-cn_image_0000002808886097.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=64724E5897A473B17005EFC028188044A9BDCE8E934FFE4F047CE5708F0A554C)按钮，折叠再展开DevEco Code，迁移窗口会重再次出现。

删除该文件不会影响已经迁移的数据。

## 未配置MCP，迁移报告中有MCP解密失败、数据库不可读等相关报错，提示再次迁移

**问题现象**

未配置MCP，迁移报告中有MCP解密失败、数据库不可读等相关报错，迁移失败，迁移窗口会再次出现，提示再次迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/i9truHaISG62_fXpbQjuSQ/zh-cn_image_0000002808886113.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AEAC234243585AFE4DF9156E07301EEBF69F0BBA656E7135976AA1217978FC3)

**可能原因**

CodeGenie把MCP配置加密存储在数据库中，解密需要本机的密钥文件（material）。

出现解密失败或数据库不可读的可能原因：密钥材料缺失或损坏；数据库文件损坏或被占用。

**解决措施**

方式一：退出和重新登录CodeGenie，重建密钥材料，点击**Retry Migration**。再迁移时，自动跳过成功条目，重新迁移失败条目。

方式二：在失败项详情页确认不需要迁移失败条目，则点击**Ignore Failed Items**，以及点击**Retry Migration****/Don't remind me**关闭迁移提示窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/IdhrUmfZS9OOdW0cPigeEA/zh-cn_image_0000002779406460.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=16CCE93DB10BFF14EC9D2C7DE94B7C6AC882E15C1417936507F69ED5E7555440)

## 迁移结束后，迁移窗口再次出现

**问题现象**

现象一：已经完成迁移，打开另一个工程项目时，迁移窗口再次出现，提示Start Migration。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/nKnduRFIRgG7vVXkIXAMdA/zh-cn_image_0000002779406470.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=348619B68D67C6B26964AE8382ED7C1E89F1BA83C3C90F3719F31FF0B6AB7920)

现象二：迁移出现失败项，迁移窗口再次出现，提示Retry Migration。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Z0M_-Fj8RHOi8UL1kHAHsw/zh-cn_image_0000002779406468.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B8788112DBA10DE084D8C4DFD3E073DF8E2AC87CADB783E13840D8F158B238D)

**可能原因**

现象一：打开了一个含有工程技能的新工程。迁移完成标记是按工程记录的，MCP配置和全局技能只迁一次，而工程技能由每个工程项目单独记录。打开一个含有未迁移的工程技能的项目时，迁移窗口会再次出现。

现象二：上一次的迁移中有失败项，迁移窗口会再次出现提示用户Retry Migration。

**解决措施**

现象一：按提示对当前项目完成迁移即可。

现象二：对于失败项，可以在迁移详情窗口中选择忽略失败项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ozvtGg6DSTmOcuD-wVPI9g/zh-cn_image_0000002779566432.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=49DE6CE8992B8638E347E95D8F2BE5A63C9386A2001E7BAB340AA5F11FD091FC)

## 迁移后，Skill和MCP在哪里查看和管理

**问题现象**

迁移后，不清楚Skill和MCP在哪里查看和管理。

**解决措施**

Skill与MCP都存储在[DevEco Code 存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)的config子目录下：

1. SKill

   全局Skill在<[存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)>/config/skills/<技能名>

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/-wV2_TYTTqa5EDX2A9y3Ng/zh-cn_image_0000002808766021.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=D72BB7CD84D18CDF1DFFEE92324FBDF6D08F4D1888AC3E6DAF41C8066C44E6D2)

   工程Skill在<[存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)>/config/projects/<工程Hash>/.deveco/skills/<技能名>

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/mwPW8TikTHKuT70YnkUZlw/zh-cn_image_0000002808886093.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=221A7EAF7AAA5AB8703C06D5247795DE545D080358B0132DBAC56310ABA2D2CA)
2. MCP 配置

   MCP配置信息存储在<[存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)>/config/deveco.jsonc的mcp字段中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/GOUaN_8nTou5qJi2KsQWaw/zh-cn_image_0000002808886105.png?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=F73408FFAD5172D559351D9280D5EB1AF86ED1EC0F72BB83FB89B903703E2397)
