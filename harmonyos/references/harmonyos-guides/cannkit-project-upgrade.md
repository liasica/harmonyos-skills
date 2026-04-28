---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-project-upgrade
title: 如何升级工程到最新版本
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 如何升级工程到最新版本
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:98c7c851335ef2e0433bdf85479abb845e8fd5b208e554ac979834dc7964083a
---

## 工具描述

使用5.0.2.0版本DDK tools包生成的算子工程，若想用新版本的DDK tools包进行调试，需要升级算子工程，否则编译时会有如下报错。

```
1. /usr/bin/ld: cannot find -lPLATFORM-NOTFOUND: No such file or directory
2. // ...
3. CMake Error at cmake_install.cmake:78 (file):
4. file INSTALL cannot find
5. "***/build_out/libcustom_op.so":
6. No such file or directory.

9. make: *** [Makefile:100: install] Error 1
```

## 命令汇总

执行如下命令，将算子工程升级为当前工具适配的版本。其中${install\_path}为ddk工具的安装目录

```
1. chmod +x ${install_path}/ddk/tools/tools_ascendc/upgrade_project.sh
2. ${install_path}/ddk/tools/tools_ascendc/upgrade_project.sh <path>
```

**表1** 工程升级参数说明

| 参数名称 | 参数描述 | 是否必选 |
| --- | --- | --- |
| <path> | 自定义算子工程根路径 | 是 |
| -h，--help | 输出帮助信息。 | 否 |

例如安装目录为/usr/local/，创建的算子工程目录为/home/AddCustom，对应的命令行为：

```
1. chmod +x  /usr/local/ddk/tools/tools_ascendc/upgrade_project.sh
2. /usr/local/ddk/tools/tools_ascendc/upgrade_project.sh /home/AddCustom
```
