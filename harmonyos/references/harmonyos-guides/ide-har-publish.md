---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-publish
title: 发布共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发及发布共享包 > 发布共享包
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:38+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:7c1aab9081202980b0d9334e9fa4b08d5cf3080dd3856827730e867e296b2a2c
---

发布打包的HAR，可供其他开发者安装和引用。接下来将介绍如何发布HAR共享包。

说明

OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。如需在应用内共享HSP，可将HSP共享包发布至私仓使用，请参考[ohpm私仓搭建工具](ide-ohpm-repo-overview.md)。

1. 在HAR模块中（与src文件夹同一级目录下），添加如下文件：
   * 新建README.md文件：在README.md文件中必须包含包的介绍和引用方式，还可以根据包的内容添加更详细介绍。
   * 新建CHANGELOG.md文件：填写HAR的版本更新记录。
   * 添加LICENSE文件：LICENSE许可文件。
2. 重新[编译HAR模块](ide-har.md#section7892044183814)，生成\*.har文件。

   说明

   若修改了HAR包模块级oh-package.json5文件中version字段信息，请先执行Build > Clean Project指令，再重新进行Build全量构建。
3. 利用工具ssh-keygen生成公、私钥，可执行以下命令：

   ```
   1. ssh-keygen -m PEM -t RSA -b 4096 -f ~/.ssh_ohpm/mykey
   ```

   说明

   1. ~/.ssh\_ohpm/mykey 为私钥文件 mykey 的文件路径，按照实际情况指定。指定的私钥存储目录必须存在。
   2. 追加了.pub后缀的相应公钥文件会存放在和私钥相同的目录下。
   3. OHPM包管理器只支持加密密钥认证，请在生成公私钥时输入密码。
4. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)官网，单击主页右上角的**个人中心，** 新增OHPM公钥，将公钥文件（mykey.pub）的内容粘贴到公钥输入框中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/EaRWGJWcRiq34noloWIgLQ/zh-cn_image_0000002530752702.png?HW-CC-KV=V1&HW-CC-Date=20260427T235437Z&HW-CC-Expire=86400&HW-CC-Sign=691B9DA71B0937340879E324A1D116F0A7D81F3AE2F8C67AD533F118E29C5914)
5. 打开命令行工具，将对应私钥文件路径配置到 .ohpmrc 文件中 key\_path 字段上，可执行以下命令进行配置：

   ```
   1. ohpm config set key_path  ~/.ssh_ohpm/mykey
   ```
6. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn)官网，单击主页右上角的**个人中心**，复制发布码，获取发布码并配置到 .ohpmrc 文件中，可执行如下命令：

   ```
   1. ohpm config set publish_id your_publish_id
   ```
7. 执行如下命令发布HAR，<HAR路径>需指定为.har文件的具体路径。

   ```
   1. ohpm publish <HAR路径>
   ```
