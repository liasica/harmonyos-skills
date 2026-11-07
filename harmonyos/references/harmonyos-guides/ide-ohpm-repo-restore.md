---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restore
title: ohpm-repo restore
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 相关命令 > ohpm-repo restore
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:12+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ec3f58658237b743216947f3d68564a46b9ca948fa9a332777afe12d271e7b81
---

将ohpm-repo pack打包产物替换<deploy\_root>目录下相应文件，重启服务。

## 前提条件

* 已成功执行[start 命令](ide-ohpm-repo-start.md)或者[restart 命令](ide-ohpm-repo-restart.md)，ohpm-repo服务启动成功。
* 已获得由[pack 命令](ide-ohpm-repo-pack.md)打包的.zip 文件。

## 命令格式

```screen
ohpm-repo restore <file_path>
```

## 功能描述

该命令会停止当前ohpm-repo服务，并用打包文件<file\_path>中的内容替换ohpm-repo部署根目录<deploy\_root>的相应文件，然后重启ohpm-repo服务。该命令执行前必须已执行过ohpm-repo实例启动命令ohpm-repo start。

**说明** 

* <file\_path>：由ohpm-repo pack命令得到的打包产物。

支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

* <deploy\_root>：ohpm-repo部署根目录 执行install命令后，会创建一个名为OHPM\_REPO\_DEPLOY\_ROOT的环境变量，记录的是[ohpm-repo私仓部署目录](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)。

## 参数

### <file\_path>

* 类型：String
* 必填参数

指定待解压的打包文件路径。

## 示例

执行以下命令：

```screen
ohpm-repo restore "D:\pack_1702625827995.zip"
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/m73Z9tE3RD6_W2MA6ZJ3ww/zh-cn_image_0000002731541779.png "点击放大")
