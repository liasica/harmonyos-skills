---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-upgrade-101_to_2xx
title: 升级版本1.0.1至2.X.X/5.X.X
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 版本升级 > 升级版本1.0.1至2.X.X/5.X.X
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:12dcffa67f8748c0a8940c2aa037f7b5ec9dd40f8f18084cb3b91a7a5ebddab4
---

升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。

注意

在升级之前，请务必备份好ohpm-repo 私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括ohpm-repo中[<deploy\_root>](ide-upgrade-101_to_2xx.md#li10435216234)部署根目录内的数据、db元数据以及store三方包数据，详细可参考[数据备份](ide-ohpm-repo-data-backup.md)。

1. 旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.0.1版本ohpm-repo私仓工具包解压目录下的bin目录，执行stop。

   ```
   1. ohpm-repo stop
   ```

   注意

   若您想在其他目录使用ohpm-repo，请将对应版本ohpm-repo工具包解压目录中bin目录的路径配置到[系统环境变量](ide-ohpm-repo-faq.md#section24117279211)path中。

2. 下载并解压工具包：下载版本2.X.X的ohpm-repo私仓工具包，并解压（请解压到一个空文件夹中）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/e-Qvw2vbRhmEfLSPipm30A/zh-cn_image_0000002530751278.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=5647FFC43478B2BEF9C1F38BE76334E4B15ECC6F796886CF6B7E56A791CA97E5)

3. 安装完成之后，进入ohpm-repo 私仓工具包解压目录下的bin目录，执行如下命令：

   ```
   1. ohpm-repo -v
   ```

   终端输出版本号2.X.X，则表示解压成功。

4. 移植配置文件信息：版本2.X.X的配置文件与版本1.0.1相比有较大差异，需要提取旧版本配置文件信息至新版本配置文件中，移植的具体内容如下：

   说明

   * 如果ohpm-repo版本1.0.1使用的配置文件，配置项均为默认项，则无需移植配置文件信息，直接执行下一步启动操作。
   * 旧版本1.0.1配置文件路径为：`<deploy\_root>/conf/config.yaml`；新版本2.X.X配置文件路径为：<2.X.X版本ohpm-repo解压目录>/conf/config.yaml。
   * <deploy\_root>：ohpm-repo部署根目录
     1. windows系统: ~/AppData/Roaming/Huawei/ohpm-repo
     2. 其他操作系统：~/ohpm-repo

   * **[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)**：旧版本listen值拷贝替换到新版本listen中。如果旧版本是在执行start时指定的listen值，需要把对应的listen值填入新版本配置文件中，新版本中listen值不支持命令行指定。
   * **[https](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_https)**：如果listen配置的协议是https，需要拷贝https的值：旧版本https.key和https.cert路径信息对应拷贝替换到新版本https\_key和https\_cert中。

     ```
     1. # 旧版本 `1.0.1`
     2. https:
     3. key: ./ssl/server.key
     4. cert: ./ssl/server.crt

     6. # 新版本 `2.X.X`
     7. https_key: ./ssl/server.key
     8. https_cert: ./ssl/server.crt
     ```
   * **[server](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_server)**： 旧版本server有八个参数信息，对应拷贝到新版本server numeric limit section模块下，拷贝替换对应数字。

     说明

     + 版本1.1.0开始，新增参数api\_timeout。
     + 版本升级时，参数信息会有变化，具体信息可在<解压目录>/conf/config.yaml文件中获取。

     ```
     1. # 旧版本 `1.0.1`
     2. server:
     3. max_package_size: 10
     4. max_extract_size: 50
     5. max_extract_file_num: 10240
     6. user_rate_limit: 100
     7. fetch_timeout: 60
     8. keep_alive_timeout: 60
     9. upload_lock_hour: 24
     10. upload_max_times: 100

     12. # 新版本 `2.X.X`
     13. max_package_size: 10
     14. max_extract_size: 50
     15. max_extract_file_num: 10240
     16. user_rate_limit: 100
     17. fetch_timeout: 60
     18. keep_alive_timeout: 60
     19. api_timeout: 60
     20. upload_lock_hour: 24
     21. upload_max_times: 100
     ```
   * **[db](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_db)**：旧版本仅支持本地filedb存储，不支持mysql，故使用新版本db.type为filedb的模板，拷贝替换旧版本db.plugin\_config.path路径信息至新版本db.config.path中。

     ```
     1. # 旧版本 `1.0.1`
     2. db:
     3. plugin_name: ohpm-repo-plugin-filedb
     4. plugin_config:
     5. path: ./db

     7. # 新版本 `2.X.X`
     8. db:
     9. type: filedb
     10. config:
     11. path: ./db
     ```
   * **[store](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_store)**：旧版本仅支持本地storage存储，不支持sftp，故使用新版本store.type为fs的模板，拷贝替换旧版本store.plugin\_config.path路径信息和store.plugin\_config.server值至新版本对应的store.config.path和 store.config.server中。

     注意

     在ohpm-repo 2.0.0版本中，listen的默认值已更改为listen: 0.0.0.0:8088，如果listen的host配置为0.0.0.0，则字段store.config.server不可省略**，必须**配置为详细地址，例如*http://localhost:8088*。

     ```
     1. # 旧版本 `1.0.1`
     2. store:
     3. plugin_name: ohpm-repo-plugin-fs
     4. plugin_config:
     5. path: ./storage
     6. #server: http://localhost:8088

     8. # 新版本 `2.X.X`
     9. store:
     10. type: fs
     11. config:
     12. path: ./storage
     13. #server: http://localhost:8088
     ```
   * **[uplink](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_uplink)**：拷贝旧版本uplink.store\_path路径信息和uplink.cache\_time缓存时间信息至新版本对应的uplink\_store\_path和uplink\_cache\_time中

     ```
     1. # 旧版本 `1.0.1`
     2. uplink:
     3. store_path: ./uplink
     4. cache_time: 168

     6. # 新版本 `2.X.X`
     7. uplink_store_path: ./uplink
     8. uplink_cache_time: 168
     ```
5. （可选项）新版本如果需要使用新的部署目录<new\_deploy\_root>，需要手动迁移数据。
   * 解压与替换配置信息：按照步骤1-4，解压和拷贝替换配置文件信息。
   * 建立新部署目录：判断指定的新部署目录<new\_deploy\_root>是否存在，不存在则新建，新部署目录需存在且为空。
   * 拷贝数据文件：拷贝旧版本部署目录[<deploy\_root>](ide-upgrade-101_to_2xx.md#li10435216234)下的全部文件至新部署目录<new\_deploy\_root>中。
   * 修改新版本ohpm-repo配置文件：打开新版本ohpm-repo 2.0.0的解压目录，进入conf目录下，修改新配置文件config.yaml，修改配置项deploy\_root为新的部署目录<new\_deploy\_root>。

   注意

   在使用新部署目录时，旧版本部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。
6. 新版本服务启动：正确拷贝替换配置文件信息后，进入ohpm-repo私仓工具包解压目录下的bin目录，执行下面语句启动新版本服务：
   * 执行安装命令：

     ```
     1. ohpm-repo install
     ```

     结果示例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Z0WJ-QViQNa14TlAeybYSA/zh-cn_image_0000002530911274.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=3EA0907417061ECA89071B1C04EFA0DCAF7705B22158F3433A582062323ED6DA "点击放大")
   * 刷新环境变量：安装成功后，必须根据给出的提示信息刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式：

     说明

     + Windows系统： 关闭当前窗口，重新开启一个窗口
     + Linux系统或Mac系统：在命令行中执行刷新命令：*source ~/.bashrc*或者. *~/.bashrc*。
   * 执行启动start命令：

     ```
     1. ohpm-repo start
     ```

     结果示例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/sNX2RH91Sf-xjtUCDMk3oA/zh-cn_image_0000002561831195.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=764321CDF6430ADD1A97A186FC295EB6C84086132CD3895AEEE4E79B38EE180D "点击放大")

     说明

     版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
