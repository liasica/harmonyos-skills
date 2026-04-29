---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-mirror_storage
title: ohpm-repo mirror_storage
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo mirror_storage
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:41+08:00
doc_updated_at: 2026-01-27
content_hash: sha256:a7a0a3dacf67599a053892b5d1dd8ce489c13226dbfb4e83561aa1ffbb4f4d7a
---

同步sftp存储的包。

## 前提条件

* 已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。
* 数据存储db模块的类型必须为mysql，文件存储store模块的类型必须为sftp。

## 命令格式

```
1. ohpm-repo mirror_storage <source_sftp> <target_sftp> <target> [options]
```

## 功能描述

该命令必须配置文件存储插件模块为sftp。命令会将**源sftp**目录下满足<target>条件的包同步到**目标sftp**目录下。

## 参数

### <source\_sftp>

* 类型：String
* 必填参数

必须在mirror\_storage命令后面配置<source\_sftp>参数，指定**源sftp**配置的名字。

### <target\_sftp>

* 类型：String
* 必填参数

必须在mirror\_storage命令后面配置<target\_sftp>参数，指定**目标sftp**配置的名字。

### <target>

* 类型：String
* 必填参数
* 格式： [<@scope>/]<pkg>[<@version>] 或 @all
* 说明： <@scope>和<@version>是可选的， <pkg>是包名。

必须在mirror\_storage命令后配置<target>参数，指定满足条件的包；或使用@all指定所有包。

## 选项

### failed

* 默认值：无
* 类型：无

可以在mirror\_storage命令后面配置--failed选项，则只同步在下载错误日志中未被处理的且满足<target>条件的包，如果同步成功，则相应的错误日志会被设置成handled。

## 示例

执行以下命令，同步包repo\_sftp2\_mirror\_gxy07056@2.0.0：

```
1. ohpm-repo mirror_storage test_one_sftp test_two_sftp repo_sftp2_mirror_gxy07056@2.0.0
```

说明：将名为test\_one\_sftp的sftp目录中repo\_sftp2\_mirror\_gxy07056@2.0.0包同步到名为test\_two\_sftp的sftp目录中。

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/-FVwbsUOSJmNwh1qGEiqhA/zh-cn_image_0000002530751296.png?HW-CC-KV=V1&HW-CC-Date=20260429T054440Z&HW-CC-Expire=86400&HW-CC-Sign=C720E2A55026B6BBAF6C7AE3923B9ECB030633D5532DB95334023C29FC3B2660)
