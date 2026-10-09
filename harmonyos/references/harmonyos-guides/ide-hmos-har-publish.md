---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-har-publish
title: 发布共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 发布共享包
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8192472bc4d4f1a68727f17c7ab0fcb6bd44e8d7b37c44e699b6ec5efa561389
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
   3. OHPM包管理器只支持加密密钥认证，请在生成公私钥时输入密码。
4. 登录[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)官网，单击主页右上角的**个人中心，** 新增OHPM公钥，将公钥文件（mykey.pub）的内容粘贴到公钥输入框中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/WCfR7OCQQ4etLClQh7zmSg/zh-cn_image_0000002779082759.png "点击放大")
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

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Mt-1UBDpS6KE7yedv8remA/zh-cn_image_0000002749323820.png)图标，在下拉菜单中选择**Product配置**，将**构建****模式**切换成**release**模式。更多请参考[指定构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/x6OCo6nQTG2re7-a80o4iw/zh-cn_image_0000002779082761.png "点击放大")
2. 选中HSP模块的根目录，鼠标右键点击**构建模块**，启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/IMEHubXNTHaRrzs3fWeslQ/zh-cn_image_0000002749323822.png)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/fgqaHHsCRjOqGlujnogvmQ/zh-cn_image_0000002749323824.png "点击放大")
3. 将HSP共享包上传至私仓，具体参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_将三方库发布到ohpm-repo)。
