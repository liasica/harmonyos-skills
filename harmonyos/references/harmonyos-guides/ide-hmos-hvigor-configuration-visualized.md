---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-configuration-visualized
title: 可视化配置
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 配置文件 > 可视化配置
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:22+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:7ad9baf7b3106f8ee93a3867bebc9407f1879f3aad369793f14278d5a7953cfc
---

鸿蒙电脑DevEco Studio为开发者提供配置文件的可视化操作，在可视化配置界面中配置相关字段后，会自动同步到对应配置文件中。可视化界面支持对工程级[app.json5](app-configuration-file.md)、[build-profile.json5](ide-hmos-hvigor-build-profile-app.md)、[oh-package.json5](ide-hmos-oh-package-json5.md)文件和模块级[module.json5](module-configuration-file.md)、[build-profile.json5](ide-hmos-hvigor-build-profile.md)、[oh-package.json5](ide-hmos-oh-package-json5.md)文件部分字段的可视化配置。

点击菜单栏**文件** **> 项目结构**进入配置文件可视化界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/Yd7ljcUhTnqVp2DUBx2-5A/zh-cn_image_0000002779728991.png)

① Project可视化配置：配置应用信息，包含基础信息、构建信息等。

② Product可视化配置：配置工程级build-profile.json5中products、targets及products.buildOption等字段。

③ Module可视化配置：配置模块信息，包含基本信息、构建信息等。

④ Target可视化配置：配置模块级build-profile.json5中targets、buildOptionSet、buildModeBinder、targets.config.buildOption等字段。

在可视化配置界面，点击文件名称跳转至对应映射文件查看配置字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/v50tU6FbSJGSbkaqOhD-9w/zh-cn_image_0000002779608845.png)

可视化配置内容及映射文件如下表所示：

| 层级 | 分类 | 说明 | 映射文件 |
| --- | --- | --- | --- |
| Project | App信息 | 配置应用的全局信息，包含应用名称、开发厂商、版本号等基本信息。 | 工程级app.json5文件 |
| 编译模式 | 配置工程级build-profile.json5中buildModeSet字段。 | 工程级build-profile.json5文件 |
| 依赖 | 配置工程级依赖相关字段。 | 工程级oh-package.json5文件 |
| Product | 产品信息 | 配置工程级build-profile.json5中products、targets字段。 | 工程级build-profile.json5文件 |
| 签名配置 | 配置工程签名。 | 工程级build-profile.json5文件 |
| 编译选项 | 配置工程级build-profile.json5的products中buildOption字段。 | 工程级build-profile.json5文件 |
| Module | 模块信息 | 配置模块类型、描述、API类型等基本信息。 | 模块级module.json5文件 |
| 编译配置 | 配置模块级build-profile.json5的buildOption字段。 | 模块级build-profile.json5文件 |
| 依赖 | 配置模块级依赖相关字段。 | 模块级oh-package.json5文件 |
| Target | Target信息 | 配置模块级build-profile.json5中targets字段。 | 模块级build-profile.json5文件 |
| 编译模式 | 配置模块级build-profile.json5的buildOptionSet、buildModeBinder字段。 | 模块级build-profile.json5文件 |
| 编译选项 | 配置模块级build-profile.json5中的targets.config.buildOption。 | 模块级build-profile.json5文件 |
