---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-3
title: 环境诊断、创建工程/模块界面全部显示空白
breadcrumb: FAQ > DevEco Studio > 工程管理 > 环境诊断、创建工程/模块界面全部显示空白
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:08+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:379c7bc7ad5617af8c780617bb6c483df2fcbf7d9fab5f89c50d627c0797a4ac
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/JWjMs8VUSIOjCk3gwniwLQ/zh-cn_image_0000002327307086.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=1798B943E5F5684B8BF0291736FA3FDA9F82F683A6314807B465BED6EF4186C7)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/trwD5Uk9R5CQz9xtLEKsWA/zh-cn_image_0000002327147458.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=859F00E3836E424A77C2E41F22A1C810C0F464547DC2CCA8CEACC035755C64B6)

搜索gpu，找到ide.browser.jcef.gpu.disable，然后勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/X7NE6uhpStSEXyzGk3HZ4g/zh-cn_image_0000002361065777.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=E980767C346DAAC81F018B7D6944600833B01666904535717449601AFADC0447)

**可能原因二**

IntelliJ底座问题，没有权限启动JCEF。

**解决措施**

可能是DevEco Studio权限不足导致，找到DevEco Studio的启动图标，选中图标，然后右键 > 属性 > 兼容性 > 以管理员身份运行此程序 > 确定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/yNUNLNYETOWCErjgl7cOig/zh-cn_image_0000002327319882.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=FCED53996DE0801048312FC2B9F358B8F3DD8EF8231A15084BE72F55C117D7E5)

**可能原因三**

JCEF文件缺失，可能被杀毒软件误删除。

**解决措施**

检查JCEF文件是否缺失。

JCEF文件缺失，可能被杀毒软件误删除，导致JCEF进程无法拉起，查看这两个文件是否还存在，如果不存在，则需要重新安装DevEco Studio。

${DevEco Studio安装目录}/jbr/bin/server/jvm.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/n9v-nQqhStmYzzEErc3f_A/zh-cn_image_0000002327180308.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=1E11ED602EA87C76D24664D2346B534BB4A2ACCCEAA47E2DC8BC786420F07DD5)

${DevEco Studio安装目录}/jbr/bin/chrome\_elf.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/qHMY9pdBTV2cllWbQWo_pQ/zh-cn_image_0000002327341312.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=3CA61D6394B65F6056794754A274FB87B52F0CD67F535A1EF1791AB45F05EEE6 "点击放大")

**可能原因四**

JCEF沙箱环境与当前电脑环境冲突。

**解决措施**

JCEF沙箱环境与当前电脑环境冲突，导致JCEF无法正常工作。

点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/71SsEtbXStuF3XFbj5SRtA/zh-cn_image_0000002361164509.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=9516E822D6F91F4FE235B71B599E4CAAF31ECD5D953CC75787536F2521C4642B)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/BwVZ5wB5SGaqNJAqRC4NGw/zh-cn_image_0000002361164813.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=732D5389C220A8B23B5AA4E24720645CAA9502D8D989208761E8891BDD328343)

搜索sandbox，找到ide.browser.jcef.sandbox.enable，取消勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/iMhn5PNnTsWUFX9hvfFgAQ/zh-cn_image_0000002361165633.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=4CC76A93FDF89C892045C8216BFB653AAE2A5598B252CC84FE43EF6C41E82F90)
