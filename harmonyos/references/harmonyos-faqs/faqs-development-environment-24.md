---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-24
title: DevEco Studio代码编辑界面显示元素如何关闭
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio代码编辑界面显示元素如何关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:1161aef256e46851b46005670135ecaa57a88f8cddf80cb3235eecae0bc13fa7
---

## 问题现象

场景一：DevEco Studio中，代码开发界面显示的白竖线如何取消？

在这个白竖线附近时，代码就会自动折行显示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/gRY3u1DOSnqam0C7EGej1g/zh-cn_image_0000002710337997.png "点击放大")

场景二：DevEco Studio中，代码编辑界面的灯泡图标如何关闭？

## 背景知识

代码开发界面的白竖线是一个视觉分割线，它允许用户设置一个特定的列数作为代码的宽度限制。当代码行超过这个限制时，编程工具会自动将代码换行到下一行，从而保持代码的整洁和可读性。

## 解决方案

场景一：

可以使用如下两种解决方案：

* 完全取消分割线：

  在开发工具File->Settings->Editor->General->Appearance取消勾选show hard wrap and visual guides。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/U6U8p2tFQz2LRSoHk0nV0w/zh-cn_image_0000002710178153.png "点击放大")
* 增大代码的宽度限制：

  在开发工具File->Settings->Editor->Code Style中增大Hard wrap值，如将其值改为1000。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/b9GbZkr2SDmdTg9PX8wJSQ/zh-cn_image_0000002680498362.png "点击放大")

场景二：

在DevEco Studio中，选择File->Settings->Editor->General->Appearance，取消勾选Show intention bulb即可关闭灯泡图标。

## 常见FAQ

Q：过长的三元表达式会直接换行但不带缩进，是否有办法可以调节？

A：在IDE的setting中，Editor-Code Style-ArkTS下，找到Ternary operation，勾选下面的两个选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/7MDr1TeWTMeB3B524uP0-A/zh-cn_image_0000002680658264.png "点击放大")

Q：粘贴代码时，如何关闭编辑器自动格式化？

A：在IDE的setting中，Editor-General-Smart Keys下，找到Reformat on paste选项，下拉选择None。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/WV7YPLxbQquv1ZHJZTTuhQ/zh-cn_image_0000002710178187.png "点击放大")

Q：在File -> Settings -> Appearance -> Editor -> Font设置字体大小大于14（比如设置为16），在File -> Settings -> Editor -> Color Scheme修改任意类型代码颜色，预览器颜色错乱。

A：设置代码颜色后需要按回车确认。

Q：如何使用快捷键批量注释代码？

A：选中需要注释的代码，按住ctrl + /键方可批量注释。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/OoVon6DOTNeHgROI0Dt8fw/zh-cn_image_0000002680498394.png "点击放大")
