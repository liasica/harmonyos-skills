---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-71
title: 应用静态快捷方式如何接入X键
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 应用静态快捷方式如何接入X键
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:55+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:3220754654ac937e89c5e7fdb51532268752ec001b21e7eff0fc8e41c16c71b6
---

**现有机制：**

X键当前已经支持将应用的静态快捷方式，添加至X键的九宫格面板，后续用户可以通过单击X键呼出九宫格面板后，点击已添加进来的静态快捷方式图标，快速启动，一键直达。注：当前X键九宫格面板对所有应用开放静态快捷方式，X键双击/长按列表中只对部分应用开放静态快捷方式。

**适用场景：**

应用的功能入口深，操作步骤复杂。

**实现方案：**

应用的静态快捷方式可以接入X键的前提是，应用需要创建自己的静态快捷方式，创建出来的静态快捷方式，在桌面长按应用图标，图标上方会显示静态快捷方式（注：桌面上最多显示4个静态快捷方式），另外X键编辑界面中也会显示（注：X键编辑界面暂不限制应用静态快捷方式的显示数量），并且可以点击快捷方式后面的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/kuVFU5w_Sl6Msorbwakkkw/zh-cn_image_0000002537542426.png?HW-CC-KV=V1&HW-CC-Date=20260429T061454Z&HW-CC-Expire=86400&HW-CC-Sign=DCA6ACB68F58DCE84B032CA0CEE5A43B2C261B93D8B0B4C1ECD1818EFA131AC6)图标添加至X键九宫格面板，具体效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/rYlmSH3ZRJGl-LD5zd707Q/zh-cn_image_0000002568302199.png?HW-CC-KV=V1&HW-CC-Date=20260429T061454Z&HW-CC-Expire=86400&HW-CC-Sign=1220C6E2883755D5233162B2E2D58E25390556436CF7C96D81CDD19D3D977EE9)

**参考链接：**

[创建应用静态快捷方式](../harmonyos-guides/typical-scenario-configuration.md)
