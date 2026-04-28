---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-system-platform
title: 系统平台要求
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 系统平台要求
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:39+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f58ec638ee829183aa32190b68f899a874555a9bd835c878188355cd5fe2f763
---

ohpm支持在Windows、macOS、Linux操作系统下使用。

ohpm通过软链接或符号链接的方式构建依赖关系。不同操作系统需满足如下要求：

**Windows：**

* 工程代码文件所在文件系统类型需为NTFS（Windows系统下默认为NTFS）；
* 使用源码依赖时，依赖的源码模块与被依赖的源码模块需要在同一个盘符下，不允许配置跨盘符依赖。

**macOS**：

* 工程代码文件所在文件系统类型需为APFS（macOS系统下默认为APFS）。
* 如在macOS上挂载了其他不支持符号链接的文件系统（如FAT32或exFAT），则无法在其上创建符号链接。

**Linux**：

* EXT4、Btrfs、XFS、ZFS等常见Linux文件系统类型均满足要求。
* 部分较老或简单的文件系统（不支持符号链接），可能存在无法在其上创建或正确解析软链接的情况。
