---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-batch-download
title: ohpm-repo batch_download
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > 数据迁移相关命令 > ohpm-repo batch_download
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0d1bd9f3d4be959db540d92d6ae326c713f7ff2a0e1b19de2b3e173e2aa9dc95
---

批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件。

## 前提条件

已成功执行[export\_pkginfo 命令](ide-ohpm-repo-export-pkginfo.md)，生成pkgInfo\_xxx.json文件。

## 命令格式

```screen
ohpm-repo batch_download <pkg_list>
```

## 功能描述

根据提供的包名列表批量下载ohpm-repo或OpenHarmony三方库中心仓的包文件，并导出zip文件。

**说明** 

执行[export\_pkginfo 命令](ide-ohpm-repo-export-pkginfo.md)生成的pkgInfo\_xxx.json文件中记录着ohpm-repo或OpenHarmony三方库中心仓中所有已上架的包，若仅需要批量下载部分包文件，可以修改pkgInfo\_xxx.json文件，命令只会批量下载pkgInfo\_xxx.json文件中指定的包，包如果有其他依赖，所依赖的包也会一并下载。

## 参数

### <pkg\_list>

* 类型：String
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

### --cert-verify

* 默认值：false

* 类型：Boolean

ohpm-repo 6.0.1版本开始支持在batch\_download命令后面配置--cert-verify，用于校验--public-registry仓库的认证证书。默认不校验认证证书。

### --ca-files

* 默认值：无

* 类型：String

ohpm-repo 6.0.1版本开始支持配置认证证书路径。在batch\_download命令后面配置--ca-files <string>，指定ca证书路径，当--cert-verify开启时，校验--public-registry仓库服务端证书需要的ca证书。可以设置多个证书路径，以英文逗号间隔。详情请见：[CA证书获取及配置](ide-ohpmrc.md#zh-cn_topic_0000001792216397_ca证书获取及配置)。

## 示例

执行以下命令从ohpm-repo中批量下载包文件：

```screen
ohpm-repo batch_download <pkgInfo_xxxx.json地址>
```

结果示例：

```screen
PS D:\> ohpm-repo batch_download D:\pkgInfo_1754733375315.json
[2025-08-09T18:33:30.349] [INFO] default - download "@ohos/test@1.0.0" from repository "ohpm" successfully".
[2025-08-09T18:33:30.367] [INFO] default - download "@ohos/test-two@1.0.0" from repository "ohpm" successfully".
...
[2025-08-09T18:33:30.466] [INFO] default - all "6" package(s) are successfully download.
[2025-08-09T18:33:30.466] [INFO] default - save the .zip file to : "D:\batch_download_1754735610304.zip".
[2025-08-09T18:33:30.467] [INFO] default - Clear the cache.
```

**说明** 

1. 生成的zip文件以仓库名作为目录，每个仓库目录中存在包文件和pkgInfo.json文件，pkgInfo.json文件记录每个包的**文件名**、**包名**、**组织**、**上传者**和**Tag标签**，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
2. 命令执行中，如果某个包的用户在ohpm-repo中不存在，将默认指定该包的上传用户为管理员用户或者组织的管理员用户。
3. ohpm-repo从5.3.0开始支持多仓库配置，当从OpenHarmony三方库中心仓下载包，生成的包zip文件，目录名为ohpm，在后续执行[batch\_publish](ide-ohpm-repo-batch-publish.md)命令时，默认导入ohpm-repo仓库名为ohpm的仓库中。
4. 若--public‑registry仓库的元数据及第三方包下载地址存在重定向场景，则重定向链路对应的认证证书同样需要配置至--ca‑files中。例如中心仓实体包下载地址会重定向到https://contentcenter-drcn.dbankcdn.cn，也需要配置认证证书。

```screen
batch_download_1754735610304.zip目录结构
+---ohpm
|       @ohos+test-two@1.0.0.har
|       @ohos+test@1.0.0.har
|       pkgInfo.json
|
+---one
|       @ohos+test-four@1.0.0.har
|       @ohos+test-three@1.0.0.har
|       pkgInfo.json
|
+---two
|       @ohos+test-five@1.0.0.har
|       @ohos+test-six@1.0.0.har
|       pkgInfo.json
```

```screen
batch_download_1754735610304.zip中ohpm目录中pkgInfo.json结构
{
  "packageArray": [
    {
      "packageFile": "@ohos+test@1.0.0.har",
      "packageName": "@ohos/test@1.0.0",
      "user": "admin",
      "userId": "",
      "group": "ohos",
      "distTags": []
    },
    {
      "packageFile": "@ohos+test-two@1.0.0.har",
      "packageName": "@ohos/test-two@1.0.0",
      "user": "admin",
      "userId": "",
      "group": "ohos",
      "distTags": []
    }
  ]
}
```

执行以下命令从OpenHarmony三方库中心仓中批量下载包文件：

```screen
ohpm-repo batch_download <pkgInfo_xxxx.json地址> --public-registry <OpenHarmony三方库中心仓registry地址> --http-proxy <配置代理地址> --not-use-proxy <配置不使用代理>
```

结果示例：

```screen
PS D:\> ohpm-repo batch_download D:\pkgInfo_1754734313921.json --public-registry https://ohpm.openharmony.cn/ohpm/
...
[2025-08-09T18:49:38.833] [INFO] default - A total of 95 package(s) successfully obtain download url.
[2025-08-09T18:49:38.834] [INFO] default - A total of 95 package(s) are successfully downloaded.
[2025-08-09T18:49:38.834] [INFO] default - A total of 95 package(s) are converted successfully.
[2025-08-09T18:49:38.834] [INFO] default - Packing the .zip file. . .
[2025-08-09T18:49:39.820] [INFO] default - save the .zip file to : "D:\batch_download_1754736519129.zip".
[2025-08-09T18:49:39.820] [INFO] default - Clear the cache.
```

**说明** 

1. 如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo网站页面中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。
2. 生成的zip文件中以仓库名作为目录，每个仓库目录中存在pkgInfo.json文件，其中记录了每个包的**文件名**、**包名**、**组织**、**上传者**和**Tag标签**，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
3. 当执行batch\_download命令时，某个中心仓包的组织为A，若为其指定ohpm-repo的数据库中某用户为其真实上传用户，ohpm-repo实例中不存在A组织，则该包的真实上传用户将设定为空，并且提醒用户手动创建A组织。之后执行批量上传时同样会提醒该包的A组织在ohpm-repo实例中不存在，需要先手动创建A组织。如果需要自动添加组织，使用batch\_publish命令的可选参数--force，将会选取一个管理员用户作为A组织负责人，自动创建A组织后进行该包的上传。
