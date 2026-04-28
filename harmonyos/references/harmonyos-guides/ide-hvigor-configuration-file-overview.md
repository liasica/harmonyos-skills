---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-configuration-file-overview
title: 配置文件概述
breadcrumb: 指南 > 构建应用 > 配置文件 > 配置文件概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0ca8a80f56d3eb219da10cb52076e3ff85a1549739c488d4abf7a7eb14931dc0
---

工程应用代码包含hvigor-config.json5、build-profile.json5等构建配置文件，用于配置构建环境，定制构建流程，包括构建工具版本和依赖、[多目标构建配置](ide-customized-multi-targets-and-products.md)等。

[hvigor-config.json5文件](ide-hvigor-set-options.md)在工程的hvigor目录下，主要包含以下内容：

* 指定当前工程的开发态构建工具版本号、构建任务和脚本的依赖版本等。
* 指定构建工具的相关能力，包括日志级别、执行策略等。
* 指定构建的运行时node的相关配置参数，以及其他传递给构建脚本的额外参数等。

build-profile.json5文件分为工程级与模块级，其中buildOption在工程级文件和模块级文件均可配置，其中相同字段以模块级的字段为准，不同字段模块级的buildOption配置会继承工程级配置。

[工程级build-profile.json5文件](ide-hvigor-build-profile-app.md)在工程根目录下，主要包含以下内容：

* 工程结构的信息，即应用工程中需要参与构建的所有模块，包括模块名、模块路径等。
* 应用构建所需基础配置信息，包括应用名、SDK版本、签名等。
* 构建多目标应用的定制化配置，包括product、buildMode等。

每个模块下也有一个[build-profile.json5文件](ide-hvigor-build-profile.md)，主要包含以下内容：

* 模块级配置信息，包括API模型类型、构建多目标产物target配置等。
* 模块在编译构建过程中的定制化配置，包括ArkTS/C++源码和资源的编译配置，打包配置等。
