---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-upgrade-2xx_to_2xx
title: 2.X.X与5.X.X版本升级
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 版本升级 > 2.X.X与5.X.X版本升级
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:54+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:77ff05581fcd7b509a4b6248c721ee811047e442cb6f9e5b1fbcc0e990aa13ee
---

如需将ohpm-repo版本2.X.X/5.X.X版本升级到更高版本，可参考此文档。

注意

1. 在升级之前，请务必备份好ohpm-repo私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括[<deploy\_root>](ide-upgrade-110_to_2xx.md#li10435216234)ohpm-repo部署根目录内数据，db元数据以及store三方包数据，详细可参考[数据备份](ide-ohpm-repo-data-backup.md) 。

2. 如果您想要改变db元数据和store三方包的存储方式，可在正确升级后参考[数据迁移文档指导](ide-ohpm-repo-data-migration.md)修改。

1. 旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，执行stop。

   ```
   1. ohpm-repo stop
   ```

   注意

   * 如果部署的是多实例，升级前需要停下所有机器中的ohpm-repo服务，再进行升级操作。
   * 若想在其他目录使用ohpm-repo，请将对应版本ohpm-repo工具包解压目录中bin目录的路径配置到[系统环境变量](ide-ohpm-repo-faq.md#section24117279211)path中。
2. 下载并解压工具包：下载新版本的ohpm-repo私仓工具包，并解压（请解压到一个空文件夹中）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/6KM6nTMHRtK_6e5UdVy-wA/zh-cn_image_0000002530911554.png?HW-CC-KV=V1&HW-CC-Date=20260427T235452Z&HW-CC-Expire=86400&HW-CC-Sign=4AA655A5EE62B4A9B5CDD8DFFD141AA0D842FE14D6805EEAFD912FDBD2238624)
3. 安装完成之后，进入ohpm-repo私仓工具包解压目录下的bin目录，执行如下命令：

   ```
   1. ohpm-repo -v
   ```

   终端输出为新版本的版本号，则表示解压成功。
4. 移植配置文件信息：ohpm-repo的版本更新前后都保持在2.X.X/5.X.X范围内，新版本配置文件可以直接复用旧版本配置文件。
   * 找到ohpm-repo旧版本的配置文件：如果旧版本未指定配置文件，使用默认配置文件：旧版本ohpm-repo解压根目录/conf/config.yaml。
   * 拷贝旧版本配置文件至新版本：复制旧版本的配置文件到新版ohpm-repo解压目录下的conf文件夹，覆盖新版本中的默认配置文件。
5. （可选项）新版本如果需要使用新的部署目录<new\_deploy\_root>，需要手动迁移数据。
   * 升级ohpm-repo：按照步骤1-4，解压ohpm-repo并拷贝替换配置文件信息。
   * 建立新部署目录：判断指定的新部署目录<new\_deploy\_root>是否存在，不存在则新建，新部署目录需存在且为空。
   * 拷贝数据文件：拷贝旧版本部署目录<deploy\_root>下的全部文件至新部署目录中。
   * 修改新版本ohpm-repo配置文件：打开新版本ohpm-repo的解压根目录，进入conf目录下，修改配置文件config.yaml中配置项deploy\_root为新的部署目录<new\_deploy\_root>。

   注意

   在使用新部署目录时，旧版本的部署目录中meta文件必须要迁移到新版本部署目录中，否则将导致使用meta加密组件加密的数据无法被正确解密。

6. 新版本服务启动：正确拷贝替换配置文件信息后，进入ohpm-repo私仓工具包解压目录下的bin目录，执行以下命令启动新版本ohpm-repo服务。
   * 执行安装命令：

     ```
     1. ohpm-repo install
     ```

     结果示例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/3tdlKxOsSy-NuZdwD7m3gA/zh-cn_image_0000002561831481.png?HW-CC-KV=V1&HW-CC-Date=20260427T235452Z&HW-CC-Expire=86400&HW-CC-Sign=DD2D4D43F294B87D298F9276E3857E2017D0ECFE5551DBECE713B10354CBE50D "点击放大")
   * 刷新环境变量：安装成功后，必须根据给出的提示信息刷新环境变量，Windows系统和Linux/Mac 系统，有不同处理方式：
     + Windows系统： 关闭当前窗口，重新开启一个窗口。
     + Linux/Mac系统：

       - 5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者.~/.bashrc ；
       - 5.0.1及以后版本：

         在命令行中执行刷新命令：当shell为bash时，执行*source ~/.bashrc*或者. *~/.bashrc* ；当shell为zsh时，执行*source ~/.zshrc*或者.*~/.zshrc* 。
   * 执行start命令：

     ```
     1. ohpm-repo start
     ```

     结果示例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Ge421ZoXT9u7DPbZrXYwow/zh-cn_image_0000002530751558.png?HW-CC-KV=V1&HW-CC-Date=20260427T235452Z&HW-CC-Expire=86400&HW-CC-Sign=F454AFEB047C6805EA9E18218B84A66712B4BE73A3CE6E56F92D298870F09401 "点击放大")

     说明

     版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
7. 多实例部署机器快速升级：在多实例部署中，其他机器同步骤1-6进行快速升级操作。
