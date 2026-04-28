---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-data-backup
title: 数据备份
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 数据备份
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:56+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:b3258df673a1b9fde2f7e5ae0b3fd244db1459bca3625aba7aaeee62921f0755
---

数据迁移或者版本升级之前请务必进行数据备份，以免重要数据丢失，无法回滚。备份的内容包括**ohpm-repo**中**<deploy\_root**>部署根目录内的数据、db元数据以及store三方包数据。

## 备份deploy\_root部署根目录

说明

<deploy\_root>：ohpm-repo部署根目录，默认的路径为：

windows系统：~/AppData/Roaming/Huawei/ohpm-repo

其他操作系统：~/ohpm-repo

ohpm-repo在版本1.1.0之前不支持配置<deploy\_root>，都采用默认值，若您的ohpm-repo支持且配置了<deploy\_root>，请找到对应目录，并使用常用的压缩工具打包备份该目录。

注意

如果配置文件中db，storage，logs和uplink的存储路径可配置，且存储位置不在ohpm-repo部署根目录<deploy\_root>中，请找到对应目录进行数据备份。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/K7v1_O6PQ6KmhtPJMa5wjg/zh-cn_image_0000002561751237.png?HW-CC-KV=V1&HW-CC-Date=20260427T235454Z&HW-CC-Expire=86400&HW-CC-Sign=9D754B66114FE5CB1E8077951F977091DEEFD51E4958DD921FBDCC35C86BF076 "点击放大")

## 备份<包存储目录>和<mysql>

说明

如果您使用的是本地存储（配置文件中db为filedb本地存储，store为fs本地存储），在备份<deploy\_root>时已经完成db和store的备份，请忽略该步骤。

* 如果您的配置项db使用了mysql存储，请根据配置的数据库名，备份结构和数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/zRo5u7GbTwKLT1_IIis9AA/zh-cn_image_0000002530911286.png?HW-CC-KV=V1&HW-CC-Date=20260427T235454Z&HW-CC-Expire=86400&HW-CC-Sign=CBDA45A88E9FBFB59B460A38397213102CA9ABCC6C8AF3E3A724FD8F1938512C "点击放大")

* 如果您的配置项store使用了Sftp存储或自定义存储插件存储，请根据配置的存储目录，进行备份（图片以sftp存储举例）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/1xMFiu6ASZSR6p75P0BaZA/zh-cn_image_0000002530911288.png?HW-CC-KV=V1&HW-CC-Date=20260427T235454Z&HW-CC-Expire=86400&HW-CC-Sign=2D30CCF678C2EA08DBF87D8F84BCD7A1358D9B85067BC877345C19ED15FC8609 "点击放大")
