---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-3
title: 环境诊断、创建工程/模块界面全部显示空白
breadcrumb: FAQ > DevEco Studio > 工程管理 > 环境诊断、创建工程/模块界面全部显示空白
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/IPjNu1jNTRa0RLwwOKroWQ/zh-cn_image_0000002624638324.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DDCEEA8B10F1237DCBB68D3D35E7A5924C395D0FAAAF20BA066241331BADCF6)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/xb0rBwM1SQySs3hjjViUOg/zh-cn_image_0000002654837731.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=14536FF14DAE11E687F92E76BF48289D87C05F4EE42BAA512B9043FC7E8D327D)

搜索gpu，找到ide.browser.jcef.gpu.disable，然后勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/A4d2YxfzSoiDrhXQTyOShg/zh-cn_image_0000002624478418.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8EC206E4F3D37DA57A30BE9CD1075CC24B78A50F52906A8028E1A6989241DA2)

**可能原因二**

IntelliJ底座问题，没有权限启动JCEF。

**解决措施**

可能是DevEco Studio权限不足导致，找到DevEco Studio的启动图标，选中图标，然后右键 > 属性 > 兼容性 > 以管理员身份运行此程序 > 确定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/zegrc4eFRca7rFiXmum8Qg/zh-cn_image_0000002654797785.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE68F9F9F51B4DF636E888867D2BD9587BE6BB63FC93C0CC6FC30FFF0867F19D)

**可能原因三**

JCEF文件缺失，可能被杀毒软件误删除。

**解决措施**

检查JCEF文件是否缺失。

JCEF文件缺失，可能被杀毒软件误删除，导致JCEF进程无法拉起，查看这两个文件是否还存在，如果不存在，则需要重新安装DevEco Studio。

${DevEco Studio安装目录}/jbr/bin/server/jvm.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/10Fd3AUaRVaEse1Sk8q5fQ/zh-cn_image_0000002624638326.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE5266209D47BA6730AD18BB9D4C0A0B55F8A31C1144BC5812E6A78242BE99D6)

${DevEco Studio安装目录}/jbr/bin/chrome\_elf.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/eOFx0zQxR4eRgSD5nnfc2A/zh-cn_image_0000002654837733.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD38515ACA5CEE3EA86153EA12C3C57618A75E386250D5EE82978A283D7678C9 "点击放大")

**可能原因四**

JCEF沙箱环境与当前电脑环境冲突。

**解决措施**

JCEF沙箱环境与当前电脑环境冲突，导致JCEF无法正常工作。

点击右上角的放大镜图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/zhP3n-o7Qse9yhEwRZ9D7A/zh-cn_image_0000002624478422.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA94FDABEFBB5FC179E12DB34D22D257F7886490F69B673D6C14C322155A87B6)

输入registry，点击下面的Registry...选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/lWNghupjSxmjBLwebwgLmA/zh-cn_image_0000002654797789.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9D113A88787A5CEE40B5709EB8C15B5A58E4048D1C0C6177366C916875C9520)

搜索sandbox，找到ide.browser.jcef.sandbox.enable，取消勾选这一项，最后重启DevEco Studio。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/1FylIHUlRcyNH1EaxGzkaQ/zh-cn_image_0000002624638330.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4617ED4C45EF169C3D04B220E9701DC606A9D493287432B2564F8D89F658073)
