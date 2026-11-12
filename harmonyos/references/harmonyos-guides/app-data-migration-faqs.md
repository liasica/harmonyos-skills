---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:035dbe002f89b57fe0dec4c6bfadc1bb953c3efb151648939a027b159c58849f
---

## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/K-TjZHcjRjqKnL_ycaJkhQ/zh-cn_image_0000002786359504.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEB31772A0190A3EC8664F71D40A74420B502F5C1FF830C957C78342A36CD671)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/jgqTRK5MRYOPtLtCDxU7wA/zh-cn_image_0000002815558925.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8504D04B80DF87112BF77B254C77FC7E7536DA4F6D7B538A9809F3D60DB8919)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/P6-xtrhVTeSaFPSj4hE27g/zh-cn_image_0000002815399009.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0CEE510740E5B9CF166B504FCFDE93F72C983AD4B1E5A58943A3194C2245DF0)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/HXkPtbC_ScygKRq-hLNM-w/zh-cn_image_0000002786519434.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0421C178CF0B25961DC7EF56A4D6F93CC98E81527EC5C5942DABC807B605B79)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Z62s9m7CTPG9_UbXTocnpQ/zh-cn_image_0000002815399007.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9628C5E78A668FC97CDE8F6E0E4AB9522D0640AA18909E44E8F4BDDA5BB672F)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

**说明** 

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。

## 启动迁移按钮无法点击

**问题现象**

在迁移调试界面，输入应用包名后启动迁移按钮无法点亮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/u7xL6z3aQVy5KQNpw_U7gg/zh-cn_image_0000002786359506.png?HW-CC-KV=V1&HW-CC-Date=20261112T233221Z&HW-CC-Expire=31536000000&HW-CC-Sign=83740256D7B2C3199B86E7373CEDFD6104CA00545A5BE22DA812B3D5F981460A)

**可能原因**

迁移调试工具版本过低（版本号低于6.0.0.190）。

**解决方法**

请参考[开发者自验证](adaptation-process.md#开发者自验证)下“迁移调试”工具获取方式，申请最新版迁移调试工具。
