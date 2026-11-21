---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:20+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:e9e5c24897ee6067411731a3c6b1308472877dd673b87c33aad491d79c936cab
---

## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FASiFb4ORNO3qOHt9UOXUw/zh-cn_image_0000002821837123.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=28C79E4A0FA391260A828C8E7E1EC13B4D8A6D85E302AB6517D2C0EB195EE654)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/EXkr2uzVRbuESbZ0510EQA/zh-cn_image_0000002821757125.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8CEED595CAF9B752A8706DA278ECF29BC2FE83DEA85D0D7626DDD07056D87F5)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/TXvvvqxjRFKCN9-OajWJuw/zh-cn_image_0000002793037188.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=79C73E4AB19F1718062EB3953035C9F9355E8870C04B9BC143539D6C5D92EA97)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/9MehLa6OSpqarFoQWpLHsg/zh-cn_image_0000002792877218.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=684ABBCC15ED5EF8F6F211B6C4E197387FFE008F07B551E696C2FD4FCD90BC29)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/3m4qKmEmSFSTsc5JstC1Yg/zh-cn_image_0000002793037186.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FBB3CAC178A4C539DA3D521C9044C3FA31C1AE65C97BB8732E61DDC5D8A0203)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

**说明** 

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。

## 启动迁移按钮无法点击

**问题现象**

在迁移调试界面，输入应用包名后启动迁移按钮无法点亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/WBklTNbtQz2W3lEmeQX3Xg/zh-cn_image_0000002821837125.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=E52F4A264AF468A53456F21EB0C484FBDE82BD581114A876D0382C50B4415D87)

**可能原因**

迁移调试工具版本过低（版本号低于6.0.0.190）。

**解决方法**

请参考[开发者自验证](adaptation-process.md#开发者自验证)下“迁移调试”工具获取方式，申请最新版迁移调试工具。
