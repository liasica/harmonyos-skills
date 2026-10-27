---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-173
title: 三方应用如何添加到控制中心中
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 三方应用如何添加到控制中心中
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:49+08:00
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/wk6RS3xaTm23UbnL2dBhNQ/zh-cn_image_0000002633969786.png "点击放大")
* **步骤二**：点击场景上方的“+”号创建场景。
  + 条件支持“语音控制”、“手动点击”、“指定位置”等等，我们这里选择“手动点击”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/qM1joS_aR6GGyKvxh-OjZA/zh-cn_image_0000002664169127.png "点击放大")
  + “添加任务”选择“应用服务”，然后选择“控制应用”-“打开应用”选择手机上已经安装的应用。这里我们选择“计算器”。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/PC-tK31lRoWpYTokYrYugw/zh-cn_image_0000002664169203.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/-TKds-ngS5OydQk5yAXOTg/zh-cn_image_0000002633810146.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/6ydAHI59T5CXsgd820wmKg/zh-cn_image_0000002664289281.png "点击放大")
  + 点击右上方“√”完成场景创建。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LsdQuzVbQGe_-AFDVjxvlw/zh-cn_image_0000002633810246.png "点击放大")
* **步骤三**：打开控制中心，点击左上方编辑按钮，然后在页面最下方点击“+”号，添加上面创建的“计算器”场景。点击右上方“√”完成控制中心编辑。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/TZJ_Tt8ySQOi4RAKHrbVhw/zh-cn_image_0000002633970336.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/S1pTgc-0R8Ol7HDxBmYI5Q/zh-cn_image_0000002664169477.png "点击放大")

## 常见FAQ

Q：为什么控制中心打开应用后不会自动收起，系统的视频应用打开后却可以收起？

A：当前该能力因安全问题不对三方应用开放，开放后可能会导致恶意应用持续调用接口关闭控制中心，影响用户使用。

## 总结

开发者可以在应用内通过上述步骤引导用户在控制中心添加，这种由用户来主动添加的方式既可以实现应用添加的灵活性，又可以保障控制中心的纯净。
