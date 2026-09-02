---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dependency-check
title: ohpm dependency-check
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm dependency-check
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e30c9d3f8df80b47395909e0aba16dc4a24115aa7a1b5e67e522fda613e4fb17
---

从ohpm 6.1.1.830版本开始，ohpm命令支持查询三方库的版本更新信息。

## 命令格式

```screen
ohpm dependency-check [options] [<@group>/<pkg>]
```

**说明** 

* @group：三方库的命名空间，可选。
* pkg：三方库名称，可选。

## 功能描述

用于检查当前引入的三方库版本的更新信息。

## Options

### registry

* 默认值：""
* 类型：URL

可以在 dependency-check 命令后面配置 --registry <registry> 参数，指定仓库地址。如果不配置该参数，从配置中获取仓库地址。

### fetch\_timeout

* 默认值：60000
* 类型：Number
* 别名：ft

可以在 dependency-check 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，用以设置查询操作的超时时间，单位为ms。如果不配置该参数，超时时间为60000ms。

### strict\_ssl

* 默认值：true
* 类型：Boolean

可以在dependency-check命令后面不配置参数、配置--strict\_ssl或--strict\_ssl true参数时，开启校验HTTPS证书。

从ohpm 26.0.0.630版本开始，如需关闭校验，可配置--no-strict\_ssl或--strict\_ssl false参数，推荐使用--no-strict\_ssl参数。

### retry\_times

* 默认值：1
* 类型：Number
* 别名：rt

可以在 dependency-check 命令后面配置 --rt <number> 或者 --retry\_times <number> 参数，设置失败时的重试次数。如果不配置该参数，默认重试1次。

### retry\_interval

* 默认值：1000
* 类型：Number
* 别名：ri

可以在 dependency-check 命令后面配置 --ri <number> 或者 --retry\_interval <number> 参数，设置重试的间隔时间，单位为ms。如果不配置该参数，默认等待时间为1000ms。

### all-modules

* 默认值：false
* 类型：Boolean
* 别名：all

可以在 dependency-check 命令后面配置 --all 或者 --all-modules 参数，获取所有模块（包括工程根目录）下的三方库版本的更新信息。

### modules

* 默认值：""
* 类型：String
* 别名：m

可以在 dependency-check 命令后面配置 -m <string> 或者 --modules<string> 参数，string可以是一个或多个模块名称，多个模块时使用英文逗号隔开，用来获取模块下三方库版本的更新信息。

### project

* 默认值：false
* 类型：Boolean
* 别名：p

可以在 dependency-check 命令后面配置 -p 或者 --project 参数，获取工程级目录下三方库版本的更新信息。

### dev

* 默认值：false
* 类型：Boolean
* 别名：d

可以在 dependency-check 命令后面配置 -d 或者 --dev 参数，获取 oh-package.json5 文件的 devDependencies 中的三方库更新版本的信息。默认获取 oh-package.json5 文件的 dependencies 中的三方库版本的更新信息。

### json

* 默认值：false
* 类型：Boolean
* 别名：j

可以在 dependency-check 命令后面配置 -j 或者 --json 参数，获取的三方库版本更新信息以json格式输出在控制台，且会输出到工程级目录下的 dependency-check-output.json 文件中。不配置此参数时，以表格形式输出在控制台或者dependency-check-output.txt文件中。

### long

* 默认值：false
* 类型：Boolean
* 别名：l

可以在 dependency-check 命令后面配置 -l 或者 --long 参数，获取三方库版本的详细更新信息。不配置此参数时，获取三方库版本的简要更新信息。详细更新信息和简要更新信息展示的内容可参考[示例](ide-ohpm-dependency-check.md#section1495275683016)。

### console

* 默认值：false
* 类型：Boolean
* 别名：c

可以在 dependency-check 命令后面配置 -c 或者 --console 参数，默认会将获取到的三方库更新信息输出到工程级目录下的 dependency-check-output.txt 文件中，配置此参数可以将获取到的三方库更新信息同时输出到控制台。

**说明** 

查询三方库的版本更新信息规则如下：

* 指定全部模块查询时，如果指定了三方库名称pkg，则查询全部模块（包括工程根目录）下该三方库更新信息。如果没有指定三方库名称，则查询全部模块（包括工程根目录）下所有三方库更新信息。
* 指定模块查询时，如果指定了三方库名称pkg，则查询指定模块下该三方库更新信息。如果没有指定三方库名称，则查询指定模块下所有三方库更新信息。
* 指定工程查询时，如果指定了三方库的名称pkg，则查询指定工程下该三方库更新信息。如果没有指定三方库名称，则查询指定工程下所有三方库更新信息。
* 当同时配置all-modules、modules、project命令时，按照all-modules > modules > project的优先级查询三方库更新信息。当均不配置时，以project范围查询三方库版本更新信息。

## 示例

### 示例1

查询三方库的版本详细更新信息，执行以下命令。

```screen
ohpm dc --all -c -l
```

结果示例如下：

```screen
package                installed   wanted      latest  type   description     dependedBy  dependencyType  homepage                                                 
----------------------------------------------------------------------------------------------------------------------
checkupdate_pkgc3      1.2.0       1.2.0       1.2.0   match  update to date  library     prod            http://a.c
checkupdate_pkgc5      0.1.1       0.1.1       0.1.2   match  update to date  library     prod            http://a.c
checkupdate_pkgc2      2.0.0       2.0.0       2.0.0   match  update to date  library     prod            http://a.c
checkupdate_pkgea4     1.0.0       1.0.0       1.0.0   match  update to date  project     prod
@js-joda/core          5.5.2       5.5.2       5.6.0   match  update to date  project     prod            https://c.d
test-check-update      3.8.9-beta  3.8.9-beta  4.0.0   match  update to date  project     prod            https://a.y
Here are the recommended replacement packages for the following dependent packages :
checkupdate_pkgea4->checkupdate_test@2.0.0-beta, 三方测试库
checkupdate_pkgea4->@fdddd/test@1.1.5, 三方测试库
@js-joda/core->checkupdate_test@2.0.0-beta, 三方测试库
@js-joda/core->@fdddd/test@1.1.5, 三方测试库
test-check-update->checkupdate_test@2.0.0, 三方测试库
Here is the security update information: 2 package container 2 vulnerabilities，2 malwares
checkupdate_pkgea4@1.0.0, CVE-xxxx-xxxx test 跨站脚本漏洞,
checkupdate_pkgea4@1.0.0, asfasdf
test-check-update@3.8.9-beta, CVE-xxxx-xxxxx test 跨站脚本漏洞
test-check-update@3.8.9-beta, virusxxx
```

### 示例2

查询三方库的版本简要更新信息，执行以下命令。

```screen
ohpm dc --all -c
```

结果示例如下：

```screen
package                installed   wanted      latest  type     dependedBy                                                   
----------------------------------------------------------------------------
checkupdate_pkgc3      1.2.0       1.2.0       1.2.0   match    library     
checkupdate_pkgc5      0.1.1       0.1.1       0.1.2   match    library     
checkupdate_pkgc2      2.0.0       2.0.0       2.0.0   match    library     
checkupdate_pkgea4     1.0.0       1.0.0       1.0.0   match    project     
@js-joda/core          5.5.2       5.5.2       5.6.0   match    project     
test-check-update      3.8.9-beta  3.8.9-beta  4.0.0   match    project     
Here are the recommended replacement packages for the following dependent packages :
checkupdate_pkgea4->checkupdate_test@2.0.0-beta, 三方测试库
checkupdate_pkgea4->@fdddd/test@1.1.5, 三方测试库
@js-joda/core->checkupdate_test@2.0.0-beta, 三方测试库
@js-joda/core->@fdddd/test@1.1.5, 三方测试库
test-check-update->checkupdate_test@2.0.0, 三方测试库
Here is the security update information: 2 package container 2 vulnerabilities，2 malwares
checkupdate_pkgea4@1.0.0, CVE-xxxx-xxxx test 跨站脚本漏洞,
checkupdate_pkgea4@1.0.0, asfasdf
test-check-update@3.8.9-beta, CVE-xxxx-xxxxx test 跨站脚本漏洞
test-check-update@3.8.9-beta, virusxxx
```
