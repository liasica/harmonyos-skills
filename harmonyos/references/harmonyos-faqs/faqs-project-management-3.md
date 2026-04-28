---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-3
title: 环境诊断、创建工程/模块界面全部显示空白
breadcrumb: FAQ > DevEco Studio > 工程管理 > 环境诊断、创建工程/模块界面全部显示空白
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:56+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c7d76eecc097b9d9b9d6f1ab68ac5d35d5c3f01abf473e387224e1dfa6bc18e5
---

**问题现象**

打开环境诊断界面，选择工程或模块模板时，界面显示为空；工程预览界面同样为空。

**原因分析**

这些页面都是使用JCEF绘制的，JCEF无法正常启动会导致这种问题。

**可能原因一**

JCEF窗口组件的GPU兼容性有问题。

**解决措施**

关闭JCEF的GPU渲染。

解决JCEF窗口组件的GPU兼容性问题，点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/JWjMs8VUSIOjCk3gwniwLQ/zh-cn_image_0000002327307086.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=A40EFA80947BDA16EF8BDA08BB0A44E8F3FF41B37A14314721BC26FEA1F84616)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/trwD5Uk9R5CQz9xtLEKsWA/zh-cn_image_0000002327147458.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=F4DD179DBD616C883FCFFD4195D4557692FE87EAE7D5AA50E6E1617823B48B8B)

搜索gpu，找到ide.browser.jcef.gpu.disable，然后勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/X7NE6uhpStSEXyzGk3HZ4g/zh-cn_image_0000002361065777.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=7023D6A76A33B4E8707813DA3EFA2C64A7AB49DB08292085D039C9BA9157DA24)

**可能原因二**

IntelliJ底座问题，没有权限启动JCEF。

**解决措施**

可能是DevEco Studio权限不足导致，找到DevEco Studio的启动图标，选中图标，然后右键 > 属性 > 兼容性 > 以管理员身份运行此程序 > 确定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/yNUNLNYETOWCErjgl7cOig/zh-cn_image_0000002327319882.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=FB6CFCD1C50A5253784F9CA465D494817FC5C73ED2915081101301116DA1F05D)

**可能原因三**

JCEF文件缺失，可能被杀毒软件误删除。

**解决措施**

检查JCEF文件是否缺失。

JCEF文件缺失，可能被杀毒软件误删除，导致JCEF进程无法拉起，查看这两个文件是否还存在，如果不存在，则需要重新安装DevEco Studio。

${DevEco Studio安装目录}/jbr/bin/server/jvm.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/n9v-nQqhStmYzzEErc3f_A/zh-cn_image_0000002327180308.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=68BB264A351E29447B8D53417A6F47F852069F3896432DF0F1FE2CA172947011)

${DevEco Studio安装目录}/jbr/bin/chrome\_elf.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/qHMY9pdBTV2cllWbQWo_pQ/zh-cn_image_0000002327341312.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=5479A58BA574B2E8240E4C2887131543EF88CDDAC1843A2C2211B1D0F16F13A1 "点击放大")

**可能原因四**

JCEF沙箱环境与当前电脑环境冲突。

**解决措施**

JCEF沙箱环境与当前电脑环境冲突，导致JCEF无法正常工作。

点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/71SsEtbXStuF3XFbj5SRtA/zh-cn_image_0000002361164509.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=E4ADE9BAA81C851B24F9FD629D19E5C1A9FBC26FAEDA32E07C50527E2A70E38D)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/BwVZ5wB5SGaqNJAqRC4NGw/zh-cn_image_0000002361164813.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=31ACA343322C274D1EFFA459B46823BE6F013FCD7CC351157A67ADFCEB116527)

搜索sandbox，找到ide.browser.jcef.sandbox.enable，取消勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/iMhn5PNnTsWUFX9hvfFgAQ/zh-cn_image_0000002361165633.png?HW-CC-KV=V1&HW-CC-Date=20260428T002855Z&HW-CC-Expire=86400&HW-CC-Sign=5E633F373C088E1077B1908A25AABD2BD30BDE9BD60AFD3FE1E17D3FD80001D5)
