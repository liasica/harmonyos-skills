---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-batch-download
title: ohpm-repo batch_download
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo batch_download
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ba9ce4eb2c9bb59d249095797d1c3ea173b1200a3135bc2631fd56a487a8ef7
---

批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件。

## 前提条件

已成功执行[export\_pkginfo 命令](ide-ohpm-repo-export-pkginfo.md)，生成pkgInfo\_xxx.json文件。

## 命令格式

```
1. ohpm-repo batch_download <pkg_list>
```

## 功能描述

根据提供的包名列表用于批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件，并导出zip文件。

说明：执行[export\_pkginfo 命令](ide-ohpm-repo-export-pkginfo.md)生成的pkgInfo\_xxx.json文件中记录着ohpm-repo或OpenHarmony三方库中心仓中所有已上架的包，若仅需要批量下载部分包文件，可以手动修改pkgInfo\_xxx.json文件，命令只会批量下载pkgInfo\_xxx.json文件中指定的包，包如果有其他依赖，所依赖的包也会一并下载。

## 参数

### <pkg\_list>

* 类型： String
* 必填参数

必须在batch\_download命令后面配置<pkg\_list>参数，指定执行[export\_pkginfo 命令](ide-ohpm-repo-export-pkginfo.md)导出的json文件。

## 选项

### --public-registry

* 默认值：无
* 类型：URL

在batch\_download命令后面配置--public-registry <string>，指定OpenHarmony三方库中心仓registry地址下载包文件。

### --http-proxy

* 默认值：无
* 类型：String

在batch\_download命令后面配置--http-proxy <string>，发起请求时将为上面配置的--public-registry地址设置代理。

### --not-use-proxy

* 默认值：无
* 类型：String

在batch\_download命令后面配置--not-use-proxy <string>，发起请求时不会为指定的地址设置代理，如果有多个地址请使用英文逗号隔开，并使用url编码转换特殊字符。

## 示例

执行以下命令从ohpm-repo中批量下载包文件：

```
1. ohpm-repo batch_download <pkgInfo_xxxx.json地址>
```

结果示例：

```
1. PS D:\> ohpm-repo batch_download D:\pkgInfo_1754733375315.json
2. [2025-08-09T18:33:30.349] [INFO] default - download "@ohos/test@1.0.0" from repository "ohpm" successfully".
3. [2025-08-09T18:33:30.367] [INFO] default - download "@ohos/test-two@1.0.0" from repository "ohpm" successfully".
4. ...
5. [2025-08-09T18:33:30.466] [INFO] default - all "6" package(s) are successfully download.
6. [2025-08-09T18:33:30.466] [INFO] default - save the .zip file to : "D:\batch_download_1754735610304.zip".
7. [2025-08-09T18:33:30.467] [INFO] default - Clear the cache.
```

说明

1、生成的zip文件以仓库名作为目录，每个仓库目录中存在包文件和pkgInfo.json文件，pkgInfo.json文件记录每个包的**文件名**、**包名**、**组织**、**上传者**和**Tag标签**，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。

2、命令执行中，如果某个包的用户在ohpm-repo中不存在，将默认指定该包的上传用户为管理员用户或者组织的管理员用户。

3、ohpm-repo从5.3.0开始支持多仓库配置，当从OpenHarmony三方库中心仓下载包，生成的包zip文件，目录名为ohpm，在后续执行[batch\_publish](ide-ohpm-repo-batch-publish.md)命令时，默认导入ohpm-repo仓库名为ohpm的仓库中。

```
1. batch_download_1754735610304.zip目录结构
2. +---ohpm
3. |       @ohos+test-two@1.0.0.har
4. |       @ohos+test@1.0.0.har
5. |       pkgInfo.json
6. |
7. +---one
8. |       @ohos+test-four@1.0.0.har
9. |       @ohos+test-three@1.0.0.har
10. |       pkgInfo.json
11. |
12. +---two
13. |       @ohos+test-five@1.0.0.har
14. |       @ohos+test-six@1.0.0.har
15. |       pkgInfo.json
```

```
1. batch_download_1754735610304.zip中ohpm目录中pkgInfo.json结构
2. {
3. "packageArray": [
4. {
5. "packageFile": "@ohos+test@1.0.0.har",
6. "packageName": "@ohos/test@1.0.0",
7. "user": "admin",
8. "userId": "",
9. "group": "ohos",
10. "distTags": []
11. },
12. {
13. "packageFile": "@ohos+test-two@1.0.0.har",
14. "packageName": "@ohos/test-two@1.0.0",
15. "user": "admin",
16. "userId": "",
17. "group": "ohos",
18. "distTags": []
19. }
20. ]
21. }
```

执行以下命令从OpenHarmony三方库中心仓中批量下载包文件：

```
1. ohpm-repo batch_download <pkgInfo_xxxx.json地址> --public-registry <OpenHarmony三方库中心仓registry地址> --http-proxy <配置代理地址> --not-use-proxy <配置不使用代理>
```

结果示例：

```
1. PS D:\> ohpm-repo batch_download D:\pkgInfo_1754734313921.json --public-registry https://ohpm.openharmony.cn/ohpm/
2. ...
3. [2025-08-09T18:49:38.833] [INFO] default - A total of 95 package(s) successfully obtain download url.
4. [2025-08-09T18:49:38.834] [INFO] default - A total of 95 package(s) are successfully downloaded.
5. [2025-08-09T18:49:38.834] [INFO] default - A total of 95 package(s) are converted successfully.
6. [2025-08-09T18:49:38.834] [INFO] default - Packing the .zip file. . .
7. [2025-08-09T18:49:39.820] [INFO] default - save the .zip file to : "D:\batch_download_1754736519129.zip".
8. [2025-08-09T18:49:39.820] [INFO] default - Clear the cache.
```

说明

1. 如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo网站页面中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。
2. 生成的zip文件中以仓库名作为目录，每个仓库目录中存在pkgInfo.json文件，其中记录了每个包的**文件名**、**包名**、**组织**、**上传者和****Tag标签**，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
3. 当执行batch\_download命令时，某个中心仓包的组织为A，若为其指定ohpm-repo的数据库中某用户为其真实上传用户，ohpm-repo实例中不存在A组织，则该包的真实上传用户将设定为空，并且提醒用户手动创建A组织。之后执行批量上传时同样会提醒该包的A组织在ohpm-repo实例中不存在，需要先手动创建A组织。如果需要自动添加组织，使用batch\_publish命令的可选参数--force，将会选取一个管理员用户作为A组织负责人，自动创建A组织后进行该包的上传。
