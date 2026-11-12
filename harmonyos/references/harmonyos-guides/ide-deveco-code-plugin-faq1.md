---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-faq1
title: 迁移CodeGenie数据至DevEco Code常见问题
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 常见问题 > 迁移CodeGenie数据至DevEco Code常见问题
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:26+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:c7ba43cb266ae249ed5194472138c70f8d0e85c57b640fa25a0acfd6df4d4969
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/PiZxDaqoQnuD6w4QedG2JQ/zh-cn_image_0000002808766025.png)

**解决措施**

打开[CodeGenie数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)确认是否存在需要迁移的数据，如果需要迁移，点击**Start Migration**；如果不需要迁移，点击**Don't remind me**。

## 迁移窗口提示中的DevEco Studio与打开的DevEco Studio版本号不一致

**问题现象**

迁移窗口提示中的DevEco Studio版本与本地打开的DevEco Studio版本号不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/HLAEPGR5QdOeRSN5CXN9lA/zh-cn_image_0000002779566446.png)

**解决措施**

该标注仅用于标识迁移数据来源的DevEco Studio版本，用户不用关注版本号问题。

打开[CodeGenie数据目录](ide-deveco-code-plugin-faq1.md#section1772610318144)确认是否存在需要迁移的数据，如果需要迁移，点击**Start Migration**；如果不需要迁移，点击**Don't remind me**。

## 迁移窗口显示不同的数据来源信息

**问题现象**

迁移窗口显示的数据来源信息有多种情况：

* 情况一：不显示版本号
* 情况二：显示一个版本号（如Global configuration from DevEco Studio 26.0）
* 情况三：显示两个版本号（如Global Skill from DevEco Studio 26.0，MCP from DevEco Studio 6.1）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/1ytPmUV3TYOWbyUgNpr52g/zh-cn_image_0000002808886109.png)

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

删除迁移标记文件，以及在工具左侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/BhDJnIv5R0yCXHEGbft7IA/zh-cn_image_0000002808886097.png)按钮，折叠再展开DevEco Code，迁移窗口会重再次出现。

删除该文件不会影响已经迁移的数据。

## 未配置MCP，迁移报告中有MCP解密失败、数据库不可读等相关报错，提示再次迁移

**问题现象**

未配置MCP，迁移报告中有MCP解密失败、数据库不可读等相关报错，迁移失败，迁移窗口会再次出现，提示再次迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/rMH-qk_HQy-mWrD15Z8Law/zh-cn_image_0000002808886113.png)

**可能原因**

CodeGenie把MCP配置加密存储在数据库中，解密需要本机的密钥文件（material）。

出现解密失败或数据库不可读的可能原因：密钥材料缺失或损坏；数据库文件损坏或被占用。

**解决措施**

方式一：退出和重新登录CodeGenie，重建密钥材料，点击**Retry Migration**。再迁移时，自动跳过成功条目，重新迁移失败条目。

方式二：在失败项详情页确认不需要迁移失败条目，则点击**Ignore Failed Items**，以及点击**Retry Migration****/Don't remind me**关闭迁移提示窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/YOi09oPfRLqpBFTmVo-S6w/zh-cn_image_0000002779406460.png)

## 迁移结束后，迁移窗口再次出现

**问题现象**

现象一：已经完成迁移，打开另一个工程项目时，迁移窗口再次出现，提示Start Migration。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/csnHzfKmQbGfOgOZyRIFFg/zh-cn_image_0000002779406470.png)

现象二：迁移出现失败项，迁移窗口再次出现，提示Retry Migration。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/7FiD5YitQ3eRSy8gpv3Sbg/zh-cn_image_0000002779406468.png)

**可能原因**

现象一：打开了一个含有工程技能的新工程。迁移完成标记是按工程记录的，MCP配置和全局技能只迁一次，而工程技能由每个工程项目单独记录。打开一个含有未迁移的工程技能的项目时，迁移窗口会再次出现。

现象二：上一次的迁移中有失败项，迁移窗口会再次出现提示用户Retry Migration。

**解决措施**

现象一：按提示对当前项目完成迁移即可。

现象二：对于失败项，可以在迁移详情窗口中选择忽略失败项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/aBuFud0gTYapM1oSu5kxSQ/zh-cn_image_0000002779566432.png)

## 迁移后，Skill和MCP在哪里查看和管理

**问题现象**

迁移后，不清楚Skill和MCP在哪里查看和管理。

**解决措施**

Skill与MCP都存储在[DevEco Code 存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)的config子目录下：

1. SKill

   全局Skill在<[存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)>/config/skills/<技能名>

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/TXbnBYaFTt6RarHS-nWd4Q/zh-cn_image_0000002808766021.png)

   工程Skill在<[存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)>/config/projects/<工程Hash>/.deveco/skills/<技能名>

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/gLNIoEJVQU-BPBJucQNz7A/zh-cn_image_0000002808886093.png)
2. MCP 配置

   MCP配置信息存储在<[存储根](ide-deveco-code-plugin-faq1.md#section1772610318144)>/config/deveco.jsonc的mcp字段中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/EcW5i6FmTYW_j9PFelGZcg/zh-cn_image_0000002808886105.png)
