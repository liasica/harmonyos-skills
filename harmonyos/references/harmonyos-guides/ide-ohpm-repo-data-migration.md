---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-data-migration
title: 数据迁移
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 数据迁移
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:53+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:dac323203995fee8c9ea4edc03089e5aa1343819d8f996ea7a70c6fda23061b8
---

ohpm-repo**2.2.0**版本开始支持数据迁移功能。在ohpm-repo配置文件中，db是元数据存储的配置项，store是文件存储的配置项，db和store不能随意搭配，需要符合下面表格中的匹配规范。如果需要改变db和store的存储方式，需要进行数据迁移操作。

| db：元数据存储 | **与db所适配的store：三方包文件存储** |
| --- | --- |
| filedb | file storage |
| mysql（ohpm-repo 1.1.0开始支持） | file storage，sftp storage（ohpm-repo 1.1.0开始支持），custom storage（ohpm-repo 2.2.0开始支持） |

## 流程概述

1. 为保证数据不丢失，请务必先进行[数据备份](ide-ohpm-repo-data-backup.md)。
2. 参考[升级指导文档](ide-ohpm-repo-upgrade.md)，升级ohpm-repo到目标版本。
3. [使用迁移命令导出数据](ide-ohpm-repo-data-migration.md#section397615294129)。
4. 修改配置文件中db和store的存储方式，以[新存储方式启动ohpm-repo](ide-ohpm-repo-data-migration.md#section1959530132115)。
5. [使用迁移命令导入数据](ide-ohpm-repo-data-migration.md#section17126124310255)。

## 备份ohpm-repo数据

请参考[数据备份指导文档](ide-ohpm-repo-data-backup.md)进行操作。

## 升级ohpm-repo到最新版本

请参考[升级指导文档](ide-ohpm-repo-upgrade.md)进行操作。

## 使用迁移命令导出数据

1. 导出DB数据

   使用[export\_userinfo](ide-ohpm-repo-export-userinfo.md)命令导出下面10张数据表的数据，并且导出加密组件，在命令执行目录生成打包export\_userInfo\_xxx.zip文件。

   * user
   * group\_member
   * public\_key
   * access\_token
   * uplink
   * uplink\_proxy
   * repo
   * repo\_permission
   * validation\_config
   * system\_security

   ```
   1. ohpm-repo export_userinfo
   ```

   ```
   1. PS D:\> ohpm-repo export_userinfo
   2. [2025-08-09T19:14:16.721] [INFO] default - initialize "file database" successfully.
   3. ...
   4. [2025-08-09T19:14:16.734] [INFO] default - export the "system_security" table done.
   5. [2025-08-09T19:14:16.761] [INFO] default - userinfo exported completed, save the .zip file to : "D:\export_userInfo_1754738056722.zip".
   ```
2. 导出已上架的包列表

   使用[export\_pkginfo](ide-ohpm-repo-export-pkginfo.md)命令，导出已上架的包列表。

   ```
   1. ohpm-repo export_pkginfo
   ```

   ```
   1. PS D:\> ohpm-repo export_pkginfo
   2. ...
   3. [2025-08-09T17:56:15.319] [INFO] default - export matched packages success: save to "D:\pkgInfo_1754733375315.json".
   ```
3. 批量下载包文件

   使用[batch\_download](ide-ohpm-repo-batch-download.md)命令，从ohpm-repo配置的store存储目录中批量下载包文件。

   使用第2步生成的pkgInfo\_xxxx.json作为[batch\_download](ide-ohpm-repo-batch-download.md)命令参数，批量下载har或tgz包，在命令执行目录生成batch\_download\_xxx.zip文件。

   注意

   如果不迁移所有的包，您可以在第2步生成的pkgInfo\_xxxx.json文件中删除掉不需要下载的包。

   ```
   1. ohpm-repo batch_download <pkgInfo_xxxx.json地址>
   ```

   ```
   1. PS D:\> ohpm-repo batch_download D:\pkgInfo_1754733375315.json
   2. [2025-08-09T18:33:30.349] [INFO] default - download "@ohos/test@1.0.0" from repository "ohpm" successfully".
   3. [2025-08-09T18:33:30.367] [INFO] default - download "@ohos/test-two@1.0.0" from repository "ohpm" successfully".
   4. ...
   5. [2025-08-09T18:33:30.466] [INFO] default - all "6" package(s) are successfully download.
   6. [2025-08-09T18:33:30.466] [INFO] default - save the .zip file to : "D:\batch_download_1754735610304.zip".
   7. [2025-08-09T18:33:30.467] [INFO] default - Clear the cache.
   ```

   batch\_download\_xxx.zip文件中以仓库名作为目录，每个仓库目录中存在pkgInfo.json文件，其中记录了每个包的**文件名**、**包名**、**组织**、**上传者**、**Tag标签**，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
4. 导出包权限数据

   ohpm-repo 5.4.0版本开始，支持使用[export\_pkgPermission](ide-ohpm-repo-export-pkgpermission.md)命令，导出包权限数据。

   ```
   1. ohpm-repo export_pkgPermission
   ```

   ```
   1. PS D:\> ohpm-repo export_pkgPermission
   2. ...
   3. [2025-09-16T14:58:24.806] [INFO] default - successfully exported all package permissions: saved to "D:\packagePermission_1758005904806.json".
   ```

## 新存储方式重启ohpm-repo

打开ohpm-repo压缩包解压根目录中配置文件config.yaml，修改db和store配置项，指定所需存储方式。

注意

修改db和store配置项后，需要您在配置文件中同时配置新的<deploy\_root>目录。

使用修改后的配置文件重新执行安装命令（这一步必须执行，初始化数据库和其他必要的配置）。

```
1. ohpm-repo install --config <配置文件路径>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/jr4svXAgTYueUGWOgZNapQ/zh-cn_image_0000002561751511.png?HW-CC-KV=V1&HW-CC-Date=20260427T235451Z&HW-CC-Expire=86400&HW-CC-Sign=B320B446B26D4AA2C5607FEDCCA226B7D8BDE37E0497B76EA5D68E7C8C093C62 "点击放大")

根据提示信息刷新环境变量，然后重新启动ohpm-repo。

```
1. ohpm-repo start
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/hFpc8hbaQGCzjjQyfFLQeA/zh-cn_image_0000002530911568.png?HW-CC-KV=V1&HW-CC-Date=20260427T235451Z&HW-CC-Expire=86400&HW-CC-Sign=A588A089DC516F3F750E0897F1AA574D3586F1F7356241A319A27FDD0F27CC00 "点击放大")

## 使用迁移命令导入数据

注意

* 若需要部署在新机器上，将上面ohpm-repo导出的**export\_userInfo\_xxx.zip**、**batch\_download\_xxx.zip****和****packagePermission\_xxx****.json**文件传到需要部署的机器中。
* 需要先导入DB数据，再进行批量上传，避免上传时找不到对应的用户和组织而报错。

1. 停止ohpm-repo服务。

   请在开始数据迁移前停止ohpm-repo服务，以防止迁移过程中因用户访问导致数据异常。
2. 导入DB数据。

   使用[import\_userinfo](ide-ohpm-repo-import-userinfo.md)命令将export\_userInfo\_xxx.zip中的数据导入数据库。

   ```
   1. ohpm-repo import_userinfo <zip_file> --clean-db
   ```

   ```
   1. PS D:\> ohpm-repo import_userinfo D:\export_userInfo_1754738056722.zip --clean-db
   2. [2025-08-09T19:19:31.623] [INFO] default - verifying the validity of the meta crypto component.
   3. [2025-08-09T19:19:31.633] [INFO] default - the meta crypto component is verified successfully.
   4. [2025-08-09T19:19:31.639] [INFO] default - initialize "file database" successfully.
   5. [2025-08-09T19:19:31.660] [INFO] default - all database data has been cleaned.
   6. [2025-08-09T19:19:31.660] [INFO] default - importing data in the 'user.json' file.
   7. ...
   8. [2025-08-09T19:19:31.673] [INFO] default - importing data in the 'system_security.json' file.
   9. [2025-08-09T19:19:31.674] [INFO] default - data import finished.
   ```

   说明

   1. '--clean-db' 表示在导入数据前会清空所有表数据，包括启动ohpm-repo时默认生成的admin用户。
   2. 如果不配置 '--clean-db'，导入过程中可能存在相同数据，默认会以兼容的方式跳过该数据的导入。例如：存在相同的admin用户，数据库中原本存在的admin用户假设为A1，导入数据中的admin用户设为A2。默认保留A1，如果A2的id在其他待导入表数据中存在，将会提前替换为A1的id。要注意的是，之后需要使用A1的密码进行登录。

   数据导入成功后，可启动ohpm-repo服务并登录管理页验证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Bzppu50USkqtuXk1Z65HTg/zh-cn_image_0000002530751574.png?HW-CC-KV=V1&HW-CC-Date=20260427T235451Z&HW-CC-Expire=86400&HW-CC-Sign=F4BB62EB9956937F449443CAF0F7B8C65FE3B344B235D6C6BEDCF6A4AF895F89 "点击放大")
3. 批量上传包到ohpm-repo配置的store目录。

   使用[batch\_publish](ide-ohpm-repo-batch-publish.md)命令，将批量下载生成的batch\_download\_xxx.zip中的包依次发布到ohpm-repo。

   ```
   1. ohpm-repo batch_publish <zip_file>
   ```

   ```
   1. PS D:\> ohpm-repo batch_publish D:\batch_download_1754735610304.zip
   2. ...
   3. [2025-08-09T19:12:01.497] [INFO] default - all 6 package(s) are successfully published
   4. [2025-08-09T19:12:01.497] [WARN] default - You are using "filedb" to store data. If you have already started a repository service, please run `ohpm-repo restart` to restart the service.
   ```

   所有包发布成功，进入ohpm-repo网站查看包数量和包详情是否正确。

   说明

   1. 在batch\_publish命令后面可以配置“--force”，如果进行批量上传时某个包的组织在ohpm-repo中不存在，将任意选取ohpm-repo中一位管理员用户作为组织负责人，自动创建组织。

   2. 当批量上传的zip文件中仅包含一个仓库目录，可在batch\_publish命令后面配置--target-repo <string>，指定所有包上传至目标ohpm-repo仓库。
4. 导入包权限数据。

   ohpm-repo 5.4.0版本开始，支持使用[import\_pkgPermission](ide-ohpm-repo-import-pkgpermission.md)命令，导入包权限数据。导入时有[三种导入模式](ide-ohpm-repo-import-pkgpermission.md#section8679814134119)，请根据不同模式的处理规则选择适合的导入模式。

   ```
   1. PS D:\> ohpm-repo import_pkgPermission D:\packagePermission_1758008466123.json --mode override
   2. ...
   3. [2025-09-17T14:44:38.451] [INFO] default - > start importing package permissions to the "ohpm" repository.
   4. [2025-09-17T14:44:38.459] [INFO] default - import package permissions completed.
   ```
