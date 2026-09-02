---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-56
title: 如何导出并查看数据库文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何导出并查看数据库文件
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2252f15afaa1e2061515772876dd3af5b58ef49958b823ca4496f09e92df1c0e
---

## 问题现象

开发者在开发数据库过程中，通常会碰到需要将数据库文件导出查看，以便确认表格创建、数据增删改查的成功。本文介绍了在HarmonyOS侧如何将数据库文件导出并查看。

## 背景知识

HarmonyOS侧提供了关系型数据库（Relational Database，RDB）供开发者实现数据的持久化。关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的本地数据库管理机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。详情请参考[通过关系型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-rdb-store.md)。

## 解决方案

查看已持久化的数据库文件可分为两步，**导出**与**查看**。

**导出**数据库文件需先了解数据库文件的存放路径，通过参考[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)中的应用el2级别加密数据库目录，可知数据库文件的存放路径为：/data/app/el2/100/database/{bundleName}/entry/rdb。

导出数据库文件可通过以下两种方式来实现：

* 通过hdc命令导出，参考如下命令：

  hdc file recv 数据库所在目录 导出的目的路径 。

  例：hdc file recv /data/app/el2/100/database/{bundleName}/entry/rdb D:\rdb

  **说明** 

  hdc命令可参考[hdc命令列表](../harmonyos-guides/hdc.md#hdc命令列表)。
* 通过DevEco Studio导出。打开DevEco Studio使用自带的Device File Browser找到数据库存放的路径，选中文件->右键->Save As导出。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/t9O0IFmISMq6eccqTYfFKQ/zh-cn_image_0000002659138353.png "点击放大")
* 使用三方库[@hadss/debug-db](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fdebug-db)实现,项目中集成debug-db后，通过浏览器访问可视化页面查看并操作数据，点击Download下载数据库文件（db文件+wal文件+shm文件）。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/cTcMDk7PSom0Q5qYWsUTXw/zh-cn_image_0000002629059002.png "点击放大")

  **说明** 

  **导出数据库文件（db文件+wal文件+shm文件）三个都要导出。**

**查看**数据库文件，HarmonyOS侧未给出官方的可视化工具，可通过第三方数据库工具查看如（DB Browser for SQLite、SQLitestudio等）或者集成三方库@hadss/debug-db，通过可视化页面查看。下图以DB Browser for SQLite工具为例，打开了名为database.db的数据库文件，可看到对应的数据库结构及表数据，使用系统默认加密的数据库不支持导出到本地使用数据库工具查看。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2OXFiYZFRlunSXvTF2Wu_g/zh-cn_image_0000002628899084.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/gXZ-5SvVQxuzPJ-GbiItBA/zh-cn_image_0000002659258295.png "点击放大")
