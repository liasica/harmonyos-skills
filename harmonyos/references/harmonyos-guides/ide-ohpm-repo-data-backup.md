---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-data-backup
title: 数据备份
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 数据备份
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:48+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:9668bfab323287f0b89dde01ebf586cebbab4479f4beaadf54443821d1112e9e
---

数据迁移或者版本升级之前请务必进行数据备份，以免重要数据丢失，无法回滚。备份的内容包括**ohpm-repo**中**<deploy\_root**>部署根目录内的数据、db元数据以及store三方包数据。

## 备份deploy\_root部署根目录

**说明** 

<deploy\_root>：ohpm-repo部署根目录，默认的路径为：

* windows系统：~/AppData/Roaming/Huawei/ohpm-repo
* 其他操作系统：~/ohpm-repo

ohpm-repo在版本1.1.0之前不支持配置<deploy\_root>，都采用默认值，若您的ohpm-repo支持且配置了<deploy\_root>，请找到对应目录，并使用常用的压缩工具打包备份该目录。

如果配置文件中db，storage，logs和uplink的存储路径可配置，且存储位置不在ohpm-repo部署根目录<deploy\_root>中，请找到对应目录进行数据备份。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/oiPUk4zuS2OfeeNZyudJmg/zh-cn_image_0000002808764973.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=3713F3B30A5E1A5917BF3215C9559E6AB54922123A27D70A1159045503BD607E "点击放大")

## 备份<包存储目录>和<mysql>

**说明** 

如果您使用的是本地存储（配置文件中db为filedb本地存储，store为fs本地存储），在备份<deploy\_root>时已经完成db和store的备份，请忽略该步骤。

* 如果您的配置项db使用了mysql存储，请根据配置的数据库名，备份结构和数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/KaFtYz42T7qJ3ZhQ3VDGJg/zh-cn_image_0000002808885055.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=75522B3529BEA6EBEC3EC97CF784D10401D4824AD9135F629BF02A69F3E78E98 "点击放大")

* 如果您的配置项store使用了Sftp存储或自定义存储插件存储，请根据配置的存储目录，进行备份（图片以sftp存储举例）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/dHwPAYwbQIeYnJ8suZbgOg/zh-cn_image_0000002808764967.png?HW-CC-KV=V1&HW-CC-Date=20261114T004702Z&HW-CC-Expire=31536000000&HW-CC-Sign=51F1684CB835D27BD86966C766CFA4CD588CCC80A0643D1867F8D633CB7B9B6C "点击放大")
