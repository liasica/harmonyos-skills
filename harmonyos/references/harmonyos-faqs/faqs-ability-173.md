---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-173
title: 三方应用如何添加到控制中心中
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 三方应用如何添加到控制中心中
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:e8398123de4c52c053aa4afe3ed7d8669a57c8c91bc8989b5b5e580d9c917ae9
---

## 问题现象

开发者希望安装完成后的应用能够自动添加到用户手机的控制中心内，实现用户快速打开应用，提高用户使用体验。

## 背景知识

* 控制中心：手机在亮屏情况，在摄像头右侧从屏幕顶侧向下滑动，可以打开控制中心。系统将用户高频使用的设置功能集成到控制中心中，如“声音模式”、“手电筒”、“旋转锁定”、“移动数据”等等。
* 智慧生活：华为IoT智能设备统一管理应用平台，可以发现、连接和管理华为8+N智能产品，实现智能设备之间的互联互通，打造专属的智慧场景。

## 解决方案

控制中心提供了编辑功能，可以将智慧生活的自定义场景添加到控制中心内。所以如果应用希望添加到控制中心，可以自己实现配置引导，让用户自己实现控制中心的定制，最终将应用添加到控制中心。具体步骤如下：

* **步骤一**：打开“智慧生活”App，选择下方的“场景”页签。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/wk6RS3xaTm23UbnL2dBhNQ/zh-cn_image_0000002633969786.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3EBF8DA5C167F826F8F75D9A054825FEAF6D0EE0792325B01692254C155BECE "点击放大")
* **步骤二**：点击场景上方的“+”号创建场景。
  + 条件支持“语音控制”、“手动点击”、“指定位置”等等，我们这里选择“手动点击”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/qM1joS_aR6GGyKvxh-OjZA/zh-cn_image_0000002664169127.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=62A4545B863ECB5920EA4B9E741A043431C1F49BB303A900A7BB21C9EAD6BE99 "点击放大")
  + “添加任务”选择“应用服务”，然后选择“控制应用”-“打开应用”选择手机上已经安装的应用。这里我们选择“计算器”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/PC-tK31lRoWpYTokYrYugw/zh-cn_image_0000002664169203.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=A035AFDD22ED155C06D809DD1F6355B5B6ABEAD9C9B4996936981F4F0E99194E "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-TKds-ngS5OydQk5yAXOTg/zh-cn_image_0000002633810146.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=0905EC0B2BDCD0444DECCC5B320F0F89FA08D446D70F1C550EFE1F427591A33C "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/6ydAHI59T5CXsgd820wmKg/zh-cn_image_0000002664289281.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=30B9429CCAAEB9D9E63236CE4AFBD40F51C8146459D0A13FBDB8EE509ED8FD57 "点击放大")
  + 点击右上方“√”完成场景创建。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LsdQuzVbQGe_-AFDVjxvlw/zh-cn_image_0000002633810246.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A73D60E059D5D75B560E2CF3F9C23568BEF66983AB87F3AB7CA4C7FE848D13F "点击放大")
* **步骤三**：打开控制中心，点击左上方编辑按钮，然后在页面最下方点击“+”号，添加上面创建的“计算器”场景。点击右上方“√”完成控制中心编辑。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/TZJ_Tt8ySQOi4RAKHrbVhw/zh-cn_image_0000002633970336.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=514D14F900810561118FC4D075532C63C1E5A07E8996E3676429EF8C145A78F0 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/S1pTgc-0R8Ol7HDxBmYI5Q/zh-cn_image_0000002664169477.png?HW-CC-KV=V1&HW-CC-Date=20261112T233142Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0E9BF2D06AB9B3ECB9192E69E995E1C43BFDF0FC0D4CEFD852880BA0E869FA0 "点击放大")

## 常见FAQ

Q：为什么控制中心打开应用后不会自动收起，系统的视频应用打开后却可以收起？

A：当前该能力因安全问题不对三方应用开放，开放后可能会导致恶意应用持续调用接口关闭控制中心，影响用户使用。

## 总结

开发者可以在应用内通过上述步骤引导用户在控制中心添加，这种由用户来主动添加的方式既可以实现应用添加的灵活性，又可以保障控制中心的纯净。
