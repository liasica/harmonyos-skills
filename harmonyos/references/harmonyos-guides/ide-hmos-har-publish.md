---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-har-publish
title: 发布共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 发布共享包
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:41+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:36399fa3e5858c91f4a9cfb0f4bb73c91e7866ed1f03b0016b9a1ce4de1297c8
---

## 发布HAR共享包

发布打包的HAR，可供其他开发者安装和引用。接下来将介绍如何发布HAR共享包。

**说明** 

OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。

1. 在库模块中（与src文件夹同一级目录下），添加如下文件：
   * 新建README.md文件：在README.md文件中必须包含包的介绍和引用方式，还可以根据包的内容添加更详细介绍。
   * 新建CHANGELOG.md文件：填写HAR的版本更新记录。
   * 添加LICENSE文件：LICENSE许可文件。
2. 重新[编译库模块](ide-hmos-har.md#section7892044183814)，生成\*.har文件。
3. 利用工具ssh-keygen生成公、私钥，可执行以下命令：

   ```screen
   ssh-keygen -m PEM -t RSA -b 4096 -f ~/.ssh_ohpm/mykey
   ```

   **说明** 

   1. ~/.ssh\_ohpm/mykey 为私钥文件 mykey 的文件路径，按照实际情况指定。指定的私钥存储目录必须存在。
   2. 追加了.pub后缀的相应公钥文件会存放在和私钥相同的目录下。
   3. ohpm包管理器只支持加密密钥认证，请在生成公私钥时输入密码。
4. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)官网，单击主页右上角的**个人中心，** 新增OHPM公钥，将公钥文件（mykey.pub）的内容粘贴到公钥输入框中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/E4u4kCWiTHibkvOHG8bLLw/zh-cn_image_0000002792000978.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=97580923F1FB5D14666253BAA3EABF859F8E140F81BFC2436626B7F8060F3BF3 "点击放大")
5. 打开命令行工具，将对应私钥文件路径配置到 .ohpmrc 文件中 key\_path 字段上，可执行以下命令进行配置：

   ```screen
   ohpm config set key_path  ~/.ssh_ohpm/mykey
   ```
6. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn)官网，单击主页右上角的**个人中心**，复制发布码，获取发布码并配置到 .ohpmrc 文件中，可执行如下命令：

   ```screen
   ohpm config set publish_id your_publish_id
   ```
7. 执行如下命令发布HAR，<HAR路径>需指定为.har文件的具体路径。

   ```screen
   ohpm publish <HAR路径>
   ```

## 发布HSP共享包

如需在应用内共享HSP，需编译生成\*.tgz包后，将HSP共享包上传至私仓。

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/OPjS2kQkRcOSV5tGZhiIqA/zh-cn_image_0000002792000980.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7700F41BC0B7A64D82DA8FA404203C3830D7D4C854A6C71074E08BAA4FF7DD5)图标，在下拉菜单中选择**Product配置**，将**构建****模式**切换成**release**模式。更多请参考[指定构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/s7BavSpISaq8ER3sOZOeRA/zh-cn_image_0000002820720943.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=33D9D530C567532B930DE9AF074057E1978B0F6CB4ECCCF1B9D98EEAB1959563 "点击放大")
2. 选中HSP模块的根目录，鼠标右键点击**构建模块**，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/TBOhAJwDS4CXP6jtktmm-g/zh-cn_image_0000002792000974.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=73A244D9B9EA50C8477609E6DA0E0FAFE1CCF8488322369A902BD0E62C67708E)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ecZkctFmRJyZUNiRzRS5BA/zh-cn_image_0000002820720947.png?HW-CC-KV=V1&HW-CC-Date=20261124T044241Z&HW-CC-Expire=31536000000&HW-CC-Sign=598B512B3E204B5D920AAF9A328B81DD4B6A0AE02050DB95C39C23CC592F2EB0 "点击放大")
3. 将HSP共享包上传至私仓，具体参考[将三方库发布到 ohpm-repo](../doccenter-deveco-studio/ide-ohpm-repo-quickstart.md#section1710514092415)。
