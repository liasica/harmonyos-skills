---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-3
title: 环境诊断、创建工程/模块界面全部显示空白
breadcrumb: FAQ > DevEco Studio > 工程管理 > 环境诊断、创建工程/模块界面全部显示空白
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:49+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b588499aeb5804fa25692904107854aa9e8e898f1367b0f5055f8d4f884781e5
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/IPjNu1jNTRa0RLwwOKroWQ/zh-cn_image_0000002624638324.png)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/xb0rBwM1SQySs3hjjViUOg/zh-cn_image_0000002654837731.png)

搜索gpu，找到ide.browser.jcef.gpu.disable，然后勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/A4d2YxfzSoiDrhXQTyOShg/zh-cn_image_0000002624478418.png)

**可能原因二**

IntelliJ底座问题，没有权限启动JCEF。

**解决措施**

可能是DevEco Studio权限不足导致，找到DevEco Studio的启动图标，选中图标，然后右键 > 属性 > 兼容性 > 以管理员身份运行此程序 > 确定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/zegrc4eFRca7rFiXmum8Qg/zh-cn_image_0000002654797785.png)

**可能原因三**

JCEF文件缺失，可能被杀毒软件误删除。

**解决措施**

检查JCEF文件是否缺失。

JCEF文件缺失，可能被杀毒软件误删除，导致JCEF进程无法拉起，查看这两个文件是否还存在，如果不存在，则需要重新安装DevEco Studio。

${DevEco Studio安装目录}/jbr/bin/server/jvm.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/10Fd3AUaRVaEse1Sk8q5fQ/zh-cn_image_0000002624638326.png)

${DevEco Studio安装目录}/jbr/bin/chrome\_elf.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/eOFx0zQxR4eRgSD5nnfc2A/zh-cn_image_0000002654837733.png "点击放大")

**可能原因四**

JCEF沙箱环境与当前电脑环境冲突。

**解决措施**

JCEF沙箱环境与当前电脑环境冲突，导致JCEF无法正常工作。

点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/zhP3n-o7Qse9yhEwRZ9D7A/zh-cn_image_0000002624478422.png)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/lWNghupjSxmjBLwebwgLmA/zh-cn_image_0000002654797789.png)

搜索sandbox，找到ide.browser.jcef.sandbox.enable，取消勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/1FylIHUlRcyNH1EaxGzkaQ/zh-cn_image_0000002624638330.png)
