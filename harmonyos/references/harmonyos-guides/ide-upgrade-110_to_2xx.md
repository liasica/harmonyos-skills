---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-upgrade-110_to_2xx
title: 升级版本1.1.0至2.X.X/5.X.X
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 版本升级 > 升级版本1.1.0至2.X.X/5.X.X
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:50+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fa41e994f06b74fb778e91d956433fa3a9662e05853e9a3fbabf11ea95e7c61c
---

升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。

注意

在升级之前，请务必备份好ohpm-repo私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括ohpm-repo中[<deploy\_root>](ide-upgrade-110_to_2xx.md#li10435216234)部署根目录内的数据、db元数据以及store三方包数据，详细可参考[数据备份](ide-ohpm-repo-data-backup.md)。

1. 旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.1.0版本ohpm-repo私仓工具包解压目录下的bin目录，执行stop

   ```
   1. ohpm-repo stop
   ```

   注意

   * 如果部署的是多实例，升级前需要停下所有机器中的ohpm-repo服务，再进行升级操作。
   * 若想在其他目录使用ohpm-repo，请将对应版本ohpm-repo工具包解压目录中bin目录的路径配置到[系统环境变量](ide-ohpm-repo-faq.md#section24117279211)path中。

2. 下载并解压工具包：下载版本2.X.X的ohpm-repo私仓工具包，并解压（请解压到一个空文件夹中）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/U6tCm2BSQ1iEmoLIaMEPgg/zh-cn_image_0000002561831207.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=9EF657BDB344BD873F5B735D55165F5A8053A23108009B5DF99E0CA84182A796)
3. 安装完成之后，进入ohpm-repo私仓工具包解压目录下的bin目录，执行如下命令：

   ```
   1. ohpm-repo -v
   ```

   终端输出为版本号2.X.X，则表示解压成功。
4. 移植配置文件信息：版本2.X.X的配置文件与版本1.1.0相比有较大差异，需要提取旧版本配置文件信息至新版本配置文件中，移植的具体内容如下：

   注意

   * 如果ohpm-repo版本1.1.0使用的配置文件，配置项均为默认项，则无需移植配置文件信息，直接执行下一步启动操作。
   * 旧版本1.1.0配置文件路径为：<deploy\_root>/conf/config.yaml；新版本2.X.X配置文件路径为：<2.X.X版本ohpm-repo解压目录>/conf/config.yaml。
   * <deploy\_root>：ohpm-repo部署目录，可通过1.1.0版本ohpm-repo私仓工具包解压目录下的.deploy\_root文件查看。

   * **[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)**：旧版本listen值拷贝替换到新版本listen中。如果旧版本是在执行start时指定的listen值，需要把对应的listen值填入新版本配置文件中，新版本中listen值不支持命令行指定。
   * **[https](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_https)**：如果listen配置的协议是https，拷贝https的值：拷贝旧版本https.key和https.cert路径信息至新版本对应的https\_key和https\_cert中。

     ```
     1. # 旧版本 `1.1.0`
     2. https:
     3. key: ./ssl/server.key
     4. cert: ./ssl/server.crt
     5. # 新版本 `2.X.X`
     6. https_key: ./ssl/server.key
     7. https_cert: ./ssl/server.crt
     ```
   * **[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_deploy_root)**：打开1.1.0版本ohpm-repo私仓工具包解压目录下的.deploy\_root文件，拷贝文件中的路径信息至新版本配置文件中配置项deploy\_root 处。

     注意

     如果1.1.0版本ohpm-repo的部署目录deploy\_root使用的是默认路径，即可省略此操作。

     + <deploy\_root>：ohpm-repo部署目录：
       1. windows系统默认路径: ~/AppData/Roaming/Huawei/ohpm-repo
       2. 其他操作系统默认路径：~/ohpm-repo
   * **[server](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_server)**： 旧版本server有九个参数信息，拷贝移动到新版本server numeric limit section模块下对应九个参数中。

     说明

     + 版本1.1.0开始，新增参数api\_timeout。
     + 版本升级时，参数信息会有变化，具体信息可在<解压目录>/conf/config.yaml文件中获取。

     ```
     1. # 旧版本 `1.1.0`
     2. server:
     3. max_package_size: 10
     4. max_extract_size: 50
     5. max_extract_file_num: 10240
     6. user_rate_limit: 100
     7. fetch_timeout: 60
     8. keep_alive_timeout: 60
     9. api_timeout: 60
     10. upload_lock_hour: 24
     11. upload_max_times: 100

     13. # 新版本 `2.X.X`
     14. max_package_size: 10
     15. max_extract_size: 50
     16. max_extract_file_num: 10240
     17. user_rate_limit: 100
     18. fetch_timeout: 60
     19. keep_alive_timeout: 60
     20. api_timeout: 60
     21. upload_lock_hour: 24
     22. upload_max_times: 100
     ```
   * **[db](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_db)**： 如果数据存储到本地磁盘中，拷贝替换旧版本db.plugin\_config.path路径信息至新版本db.config.path中；如果数据存储到mysql中，拷贝旧版本db.plugin\_config中各项信息至新版本db.config中。

     ```
     1. # 旧版本 `1.1.0`: 本地存储
     2. db:
     3. plugin_name: ohpm-repo-plugin-filedb
     4. plugin_config:
     5. path: ./db
     6. # 新版本 `2.X.X`: 本地存储
     7. db:
     8. type: filedb
     9. config:
     10. path: ./db
     ```

     ```
     1. # 旧版本 `1.1.0`: mysql存储
     2. db:
     3. plugin_name: ohpm-repo-plugin-mysqlDB
     4. plugin_config:
     5. host: "localhost"
     6. port: 3306
     7. username: "root"
     8. password: "password"
     9. database: "repo"
     10. # 新版本 `2.X.X`: mysql存储
     11. db:
     12. type: mysql
     13. config:
     14. host: "localhost"
     15. port: 3306
     16. username: "root"
     17. password: "password"
     18. database: "repo"
     ```
   * **[store](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_store)**： 如果文件存储在本地磁盘中 ，拷贝替换旧版本store.plugin\_config.path路径信息和store.plugin\_config.server值至新版本对应的store.config.path和store.config.server中；如果文件存储在sftp中，拷贝旧版本 store.plugin\_config中各项信息至新版本store.config中。

     注意

     在ohpm-repo 2.0.0版本中，listen的默认值已更改为listen: 0.0.0.0:8088，如果listen的host配置为0.0.0.0，则字段store.config.server不可省略**，必须**配置为详细地址，例如*http://localhost:8088*。

     ```
     1. # 旧版本 `1.1.0`: 本地存储
     2. store:
     3. plugin_name: ohpm-repo-plugin-fs
     4. plugin_config:
     5. path: ./storage
     6. #server: http://localhost:8088
     7. # 新版本 `2.X.X`: 本地存储
     8. store:
     9. type: fs
     10. config:
     11. path: ./storage
     12. #server: http://localhost:8088
     ```

     ```
     1. # 旧版本 `1.1.0`: sftp存储
     2. store:
     3. plugin_name: ohpm-repo-plugin-sftp
     4. plugin_config:
     5. location:
     6. -
     7. name: test_one_sftp
     8. host: "localhost"
     9. port: 22
     10. read_username: "read"
     11. read_password: "encrypted_password"
     12. write_username: "write"
     13. write_password: "encrypted_password"
     14. path: /source22
     15. -
     16. name: test_two_sftp
     17. host: "localhost"
     18. port: 24
     19. read_username: "read"
     20. read_password: "encrypted_password"
     21. write_username: "write"
     22. write_password: "encrypted_password"
     23. path: /source24
     24. #server: http://localhost:8088

     26. # 新版本 `2.X.X`: sftp存储
     27. store:
     28. type: sftp
     29. config:
     30. location:
     31. -
     32. name: test_one_sftp
     33. host: "localhost"
     34. port: 22
     35. read_username: "read"
     36. read_password: "password"
     37. write_username: "write"
     38. write_password: "password"
     39. path: /source22
     40. -
     41. name: test_two_sftp
     42. host: "localhost"
     43. port: 24
     44. read_username: "read"
     45. read_password: "password"
     46. write_username: "write"
     47. write_password: "password"
     48. path: /source24
     49. #server: http://localhost:8088
     ```
   * **[uplink](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_uplink)**: 拷贝旧版本uplink.store\_path路径信息uplink.cache\_time缓存时间信息至新版本对应的uplink\_store\_path和uplink\_cache\_time中。

     ```
     1. # 旧版本 `1.1.0`
     2. uplink:
     3. store_path: ./uplink
     4. cache_time: 168

     6. # 新版本 `2.X.X`
     7. uplink_store_path: ./uplink
     8. uplink_cache_time: 168
     ```
   * **[logs](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_logs)**：拷贝旧版本logs\_path路径信息至新版本logs\_path中。
   * **[loglevel](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_loglevel)**：拷贝旧版本loglevel.run， loglevel.operate和loglevel.access至新版本对应的loglevel\_run，loglevel\_operate和loglevel\_access中。

     ```
     1. # 旧版本 `1.1.0`
     2. loglevel:
     3. run: info
     4. operate: info
     5. access: info

     7. # 新版本 `2.X.X`
     8. loglevel_run: info
     9. loglevel_operate: info
     10. loglevel_access: info
     ```

   说明

   新版本配置文件还添加了很多信息的配置，例如[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_deploy_root)和[logs\_path](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_logs)等，此类信息在升级过程中可不改变，使用默认项。
5. （可选项）新版本如果需要使用新的部署目录<new\_deploy\_root>，需要手动迁移数据。
   * 升级ohpm-repo：按照步骤1-4，解压和拷贝替换配置文件信息。
   * 建立新部署目录：判断指定的新部署目录<new\_deploy\_root>是否存在，不存在则新建，新部署目录需存在且为空。
   * 拷贝数据文件：拷贝旧版本部署目录[<deploy\_root>](ide-upgrade-110_to_2xx.md#li194741894251)下的全部文件至新部署目录中。
   * 修改新版本ohpm-repo配置文件：打开新版本ohpm-repo 2.X.X的解压目录，进入conf目录下，修改新配置文件config.yaml，修改配置项deploy\_root为新的部署目录<new\_deploy\_root>。

   注意

   在使用新部署目录时，旧版本的部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。
6. 新版本服务启动：正确拷贝替换配置文件信息后，进入ohpm-repo私仓工具包解压目录下的bin目录，执行以下命令启动新版本ohpm-repo服务：

   * 执行安装命令：

     ```
     1. ohpm-repo install
     ```

     结果示例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/tiQpDLZmSaCyRmA-__2K_w/zh-cn_image_0000002561751235.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=83A5438B6B379EAE79F9964963842EEF2E7D449660C70A365169043727CE8E4F "点击放大")
   * 刷新环境变量：安装成功后，必须根据给出的提示信息刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式：
     + Windows系统： 关闭当前窗口，重新开启一个窗口
     + Linux系统或Mac系统： 在命令行中执行刷新命令：source ~/.bashrc或者 . ~/.bashrc。
   * 执行start命令：

     ```
     1. ohpm-repo start
     ```

     结果示例：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/7DZwdvqmQxu6eeOGFoFfqw/zh-cn_image_0000002530751292.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=1629E3A45AB0D5BE0D71EDAD112723F5E08D91B5EFE25EDC6DE0B67FF2771757 "点击放大")
7. 多实例部署机器快速升级

   在多实例部署中，可先升级一台机器，然后拷贝其配置文件到其他机器中进行快速升级，具体步骤如下

   注意

   该方法要求部署的多实例机器之间，使用的配置文件除根目录deploy\_root外，其他配置项必须完全相同。

   * 第一台多实例机器根据步骤一至步骤五完成版本的升级，然后复制新版本解压目录中conf目录下的配置文件config.yaml。
   * 复制 新版本配置文件到其他需要升级的机器中。
   * 在需要升级的机器中，首先停止旧版本服务：

     停止旧版本服务

     ```
     1. ohpm-repo stop
     ```

     注意

     若您想在其他目录使用ohpm-repo，请将对应版本ohpm-repo根目录中bin目录的路径配置到[系统环境变量](ide-ohpm-repo-faq.md#section24117279211)path中。
   * 下载并解压工具包：下载版本*`2.X.X`*的ohpm-repo私仓工具包，并解压。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/2_9KWpPZRTi6JfGaty-Pqg/zh-cn_image_0000002561751229.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=6C7C27FF3B0CF9E2772911E9658BA17F9DE309F8E53D35163324938337E12864)
   * 版本检查：进入ohpm-repo私仓工具包解压目录下的bin目录，执行版本查看命令：

     ```
     1. ohpm-repo -v
     ```

     终端输出为版本号2.X.X，则表示安装成功。
   * 替换配置文件：获取复制获得的新版本配置文件，与2.X.X版本ohpm-repo私仓工具包解压目录中conf目录下的配置文件做替换。
   * 保留旧配置文件的部署目录：打开1.1.0版本ohpm-repo私仓工具包解压目录下的.deploy\_root文件，拷贝文件中的路径信息至替换后的新版本配置文件中配置项deploy\_root处。
   * 新版本ohpm-repo的服务启动：进入ohpm-repo私仓工具包解压目录下的bin目录，执行以下命令启动新版本ohpm-repo服务：
     1. 执行安装命令：

        ```
        1. ohpm-repo install
        ```

        结果示例：

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/SRbQ7HTaR6Ki6YFL_82SbA/zh-cn_image_0000002530911280.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=C00AA6C590F14B46C8B9872AB100E78F1B346DC2B02DB7BDC9FE825635AD9B26 "点击放大")
     2. 刷新环境变量：安装成功后，必须根据给出的提示信息刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式

        说明

        + Windows系统： 关闭当前窗口，重新开启一个窗口
        + Linux系统或Mac系统： 在命令行中执行刷新命令：source ~/.bashrc或者. ~/.bashrc。
     3. 执行 start 命令：

        ```
        1. ohpm-repo start
        ```

        结果示例：

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/K1rYzAwyQIO15tlP7x1GHw/zh-cn_image_0000002561831213.png?HW-CC-KV=V1&HW-CC-Date=20260429T054448Z&HW-CC-Expire=86400&HW-CC-Sign=42E2CB1966204FD455894A581804CFDAC6482B47BA98CE9AC74221C65A3DB962 "点击放大")

        说明

        版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。
