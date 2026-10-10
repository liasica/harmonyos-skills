---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts
title: 自定义提示词库（Prompts）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 自定义提示词库（Prompts）配置
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:13+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:286cd0304f2e0eb40623c00524ba2f36e214d4ce98ba3d61884550e06b80fd26
---

## 功能介绍

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

## 操作步骤

1. 点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
   * 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/vbOllmbrRAu89Fev2Wpw8A/zh-cn_image_0000002701663234.png)按钮，选择**Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/yoSHxGYATw28yadmdmfkmw/zh-cn_image_0000002731382461.png)
   * 在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/HctggMEERQGZNpvEYVYnrQ/zh-cn_image_0000002701663242.png)
2. 点击**Add Now**进入Prompts配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/b9sjNX77RnSEZZmeeIxoOA/zh-cn_image_0000002731542433.png)
3. 填写提示词名称、提示词内容等，点击**Save**进行保存。
   * **Title**：提示词名称，长度不超过20个字符。
   * **Prompt**：提示词的具体内容，长度不超过5000个字符。
   * **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
   * **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/5XvJKQ8_RR-Rf4feH7QqCg/zh-cn_image_0000002731382457.png)发送。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Ms5Ua85iQ0SnE5ixSjYuaA/zh-cn_image_0000002731542425.png)

   将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Wnvdy2OSR_msK8znRJLxfA/zh-cn_image_0000002701823150.png)
4. 选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/eqJr4OgBSUCL-qYz4J4k_w/zh-cn_image_0000002731382451.png)
