---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-install
title: ohpm install
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm install
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:52+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:00c38ae34cbda90e99034c5e74bbfc953fd7fa707a93d4fc2f95e3898de7db69
---

安装三方库。

## 命令格式

```
1. ohpm install [options] [[<@group>/]<pkg>[@<version> | @tag:<tag>]] ...
2. ohpm install [options] <folder>
3. ohpm install [options] <har file>
4. alias: i
```

说明

* @group：三方库的命名空间，可选。
* pkg：三方库名称，可选；当 install 后面没有指定三方库名称时，会根据当前目录下 oh-package.json5 定义的依赖关系进行全量安装。
* version：三方库的版本号，可选。
* tag：三方库的标签，标签会标记三方库的某个版本号，可选。

## 功能描述

用于安装指定组件或 oh-package.json5 文件中所有的依赖。如果存在 oh-package-lock.json5 文件，安装将取决于 oh-package-lock.json5 文件中锁定的版本。

* ohpm install

  将依赖项安装到本地 oh\_modules 文件夹中，并将所有依赖项作为 dependencies，写入 oh-package.json5 文件。
* ohpm install <folder>

  安装本地文件夹，则默认会创建一个软链接指向该文件夹。

  示例：

  ```
  1. ohpm install ../folder
  ```
* ohpm install <har file>

  安装压缩包，请注意压缩包的要求：

  1. 文件名必须使用 .tar, .tar.gz, .tgz, .har 作为扩展名；
  2. 压缩包里面包含子文件 package；
  3. 子文件夹 package 下面必须包含 oh-package.json5 文件，且配置文件中必须有 name 和 version 字段。

  示例：

  ```
  1. ohpm install ./package.har
  ```

## Options

### install\_all

* 默认值：true
* 类型：Boolean
* 别名：all

可以在 install 命令后面配置 --all或者--install\_all 参数，安装您项目下所有模块在其 oh-package.json5 中配置的全部依赖项。

### save-dynamic

* 默认值：false
* 类型：Boolean

可以在 install 命令后面配置 --save-dynamic 参数，安装的三方库信息将会写入 oh-package.json5 文件的 dynamicDependencies 中。

### save-dev

* 默认值：false
* 类型：Boolean

可以在 install 命令后面配置 --save-dev 参数，安装的三方库信息将会写入 oh-package.json5 文件的 devDependencies 中。

### save-prod

* 默认值：true
* 类型：Boolean

可以在 install 命令后面配置 --save-prod 参数，安装的三方库信息将会写入 oh-package.json5 文件的 dependencies 中，这是 ohpm 的默认行为。

### no-save

* 默认值：false
* 类型：Boolean

可以在 install 命令后面配置 --no-save 参数，安装的三方库信息将不会写入 oh-package.json5 文件中。

### prefix

* 默认值：""
* 类型： string

可以在 install 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。

### parameterFile

* 默认值：无
* 类型： string
* 别名：pf

可以在 install 命令后面配置 --pf <string> 或者 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。

### registry

* 默认值：""
* 类型：URL

可以在 install 命令后面配置 --registry <registry> 参数，指定仓库地址；如果没有指定，默认从配置中获取仓库地址。

### fetch\_timeout

* 默认值：60000
* 类型： Number
* 别名：ft

可以在 install 命令后面配置 --ft <number> 或者 --fetch\_timeout <number> 参数，设置操作的超时时间，如果没有指定，默认超时时间为60000ms。

### strict\_ssl

* 默认值：true
* 类型： Boolean

可以在 install 命令后面配置 --strict\_ssl true 参数，校验 https 证书；配置 --strict\_ssl false 参数，不校验 https 证书。

### max\_concurrent

* 默认值：50
* 类型： Number
* 别名：mc

可以在 install 命令后面配置 --mc <number> 或者 --max\_concurrent <number> 参数，设置最大活动并发请求数（即ohpm操作期间任何时间的最大网络请求数），如果没有指定，默认最大并发请求数为50次。

### retry\_times

* 默认值：1
* 类型： Number
* 别名：rt

可以在 install 命令后面配置 --rt <number> 或者 --retry\_times <number> 参数，设置操作失败前的最大重试次数，如果没有指定，默认最大重试次数为1次。

### retry\_interval

* 默认值：1000
* 类型： Number
* 别名：ri

可以在 install 命令后面配置 --ri <number> 或者 --retry\_interval <number> 参数，设置重试失败前的等待时间，如果没有指定，默认等待时间为1000ms。

### experimental-concurrently-safe

* 默认值：true
* 类型：Boolean

可以在 install 命令后面配置 --experimental-concurrently-safe 参数，并发安全地安装依赖。这是一个实验性选项。

### target\_path

* 默认值：无
* 类型：string

可以在 install 命令后面配置 --target\_path <string> 参数，用来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。在执行ohpm install时，ohpm会优先安装<target\_path>/<moduleName>/oh-package.json5文件中依赖。详情参见[target\_path](ide-ohpm-install.md#section79331822125611)。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 install 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### lockfile\_stable\_order

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 install 命令后面配置 --lockfile\_stable\_order 参数，当oh-package.json5文件未变更时，当前已生成的oh-package-lock.json5各字段内容不变。

### odm\_r2\_project\_root

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 install 命令后面配置 --odm\_r2\_project\_root 参数。当存在overrideDependencyMap配置，且其配置项对应的配置文件内存在相对路径的依赖配置时，ohpm会基于工程根路径解析和查询相对路径，详情参见[odm\_r2\_project\_root](ide-ohpmrc.md#section136621053184912)。

### enable\_cross\_process\_lock

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 install 命令后面配置 --enable\_cross\_process\_lock 参数，由于oh\_modules目录结构限制，ohpm不支持在同一个工程下并行运行多个ohpm install、ohpm update或ohpm uninstall命令。若需要在同一个工程下执行多个ohpm install、ohpm update或ohpm uninstall命令，可将该配置设置为true，使多个命令以串行的方式运行。

### resolve\_conflict\_strict

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 install 命令后面配置 --resolve\_conflict\_strict 参数，ohpm会按照严格模式处理依赖版本冲突，详情参见[resolve\_conflict\_strict](ide-ohpmrc.md#section1942983310492)。

### resolve\_conflict

* 默认值：false
* 类型：Boolean

从ohpm 6.0.2.636版本开始，可以在 install 命令后面配置 --resolve\_conflict 参数，ohpm会自动处理依赖版本冲突，详情参见[resolve\_conflict](ide-ohpmrc.md#section368717475562)。

### cache

* 默认值：无
* 类型：String

从ohpm 6.0.2.636版本开始，可以在 install 命令后面配置 --cache <string> 参数，设置缓存路径。

## 示例

安装 lottie 三方库，执行以下命令：

```
1. ohpm install @ohos/lottie
```

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/zIRw_y2KTcmf5m83F_wzWg/zh-cn_image_0000002530913590.png?HW-CC-KV=V1&HW-CC-Date=20260429T054751Z&HW-CC-Expire=86400&HW-CC-Sign=C6BB652639A1D77607E6AD8FBB5BAF4B412888B55B518431DC9E217252E6ED98 "点击放大")

## oh\_modules

### ohpm 1.0.0~1.3.0

使用 ohpm 安装时，项目中各 Module 的依赖项被统一安装在 Module 根目录下的 oh\_modules 目录中，Module 中所有直接依赖和间接依赖都以平铺的方式存储在 oh\_modules 目录下的 .ohpm 目录中，Module 的直接依赖则以软链接的方式添加进 oh\_modules 文件夹的根目录中。因此，相同依赖项只会安装一次，从而减少磁盘使用空间，加快安装速度。

### ohpm 1.4.x

ohpm 客户端从 1.4.0 版本开始，同一项目下所有 Module 的依赖都会被统一安装在项目根目录下的 oh\_modules 目录中，同时会在项目各 Module 根目录下的 oh\_modules 中生成该 Module 的直接依赖的软链接，这些软链接会指向**项目根目录**下 oh\_modules 中的 .ohpm 目录下依赖实际存储目录。

## target\_path

为了支持在构建过程中针对不同的产物定制不同的依赖，Hvigor会在构建时根据目标产物target为各模块自动生成定制的依赖配置文件（oh-package.json5），开发者可以在ohpm install时使用target\_path选项来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。

ohpm会优先安装<target\_path>/moduleName/oh-package.json5文件中配置的依赖，并在<project\_root>/moduleName下生成对应的oh-package-<targetName>-lock.json5文件。当指定target\_path时，默认会开启依赖版本冲突自动处理功能，在依赖安装完成后，ohpm还会根据实际安装的依赖版本在<target\_path>/resolve-conflict/moduleName目录下生成新的oh-package.json5文件。

target\_path目录结构示例：

```
1. +---default                   // <targetName>默认为default
2. |   |   dependencyMap.json5   // 记录在特定target语境下的各模块依赖配置文件路径
3. |   +---module1               // 在特定target语境下某模块的依赖配置文件的存储目录，与原模块根目录同名
4. |   |       oh-package.json5  // 在特定target语境下某模块依赖配置文件
5. |   +---module2
6. |   |       oh-package.json5
7. |   |   oh-package.json5      // 在特定target语境下生成的工程级依赖配置文件
```

dependencyMap.json5内容示例：

```
1. {
2. targetName: "default",
3. rootDependency: "./oh-package.json5",
4. dependencyMap: {
5. "module1": "./module1/oh-package.json5",
6. "module2": "./module2/oh-package.json5"
7. }
8. }
```

**ohpm install指定target\_path时依赖配置优先级说明：**

1、<target\_path>/dependencyMap.json5中rootDependency配置的oh-package.json5的优先级高于<project\_root>/oh-package.json5。

2、.ohpmrc中projectPackageJson指定的项目级配置文件中overrides、overrideDependencyMap配置优先级同时高于<target\_path>/dependencyMap.json5中rootDependency配置的oh-package.json5中对应配置 和 <project\_root>/oh-package.json5中对应配置。

3、<target\_path>/moduleName/oh-package.json5的优先级高于overrideDependencyMap中的依赖配置文件。

4、overrides中的依赖版本优先级高于<target\_path>/moduleName/oh-package.json5中对应的依赖版本。

注意

仅当<target\_path>/dependencyMap.json5中targetName的值不为空且不等于'default'时，<project\_root>/moduleName目录下生成的lock文件名才会变更为：oh-package-targetName-lock.json5。
