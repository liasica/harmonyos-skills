---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-6
title: 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决
breadcrumb: FAQ > AI功能开发 > 计算平台 > 智能体框架（Agent Framework） > 小艺开放平台云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”如何解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fda19fe7c56ba8a0c8aadd6123ba5d914a26cc212e9dd37d108e4effbc8ccc95
---

## 问题现象

1. 小艺开放平台中使用云插件调用云函数报错“域名只支持HTTPS和WSS协议，且须为公网地址”，域名可通过apifox测试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Z_oofk1iRhWYUZ826Y_qAw/zh-cn_image_0000002628394846.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/gJlOmqP4SaKqnYDmQkqD-w/zh-cn_image_0000002628554742.png "点击放大")
2. 小艺开放平台调用云函数，填写URL后报错“域名只支持HTTPS和WSS协议，且须为公网地址”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/SfW2a9qnRQWmC7hr2ol2aA/zh-cn_image_0000002658914067.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/188oF3PJTCez_m-PvVL7sA/zh-cn_image_0000002658794113.png "点击放大")

## 解决方案

1. 云插件URL是强制匹配，在apifox成功的前提下，URL后面不可以带任何多余字符串，若URL后存在空格，则会报错“域名只支持HTTPS和WSS协议，且须为公网地址”，删除URL路径中空格后正常请求云函数：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/b8yTBKNzQiGTk3mXcrSEow/zh-cn_image_0000002628394848.png "点击放大")
2. API URL地址和工具路径拼起来需要是一个完整的API地址，同时也是要跟最终需要的函数地址相同，正确填写URL后可正常调用云函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/YCmIL_hDSBCmqf2nxOyyYg/zh-cn_image_0000002628554744.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/a1fGxdAFR_y0QlNBMo1-XA/zh-cn_image_0000002658914069.png "点击放大")
