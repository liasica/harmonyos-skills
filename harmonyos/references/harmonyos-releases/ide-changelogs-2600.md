---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-2600
title: 变更说明
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95ee23a465f019d99bb4d6ac66bf2d5eadb62bc5a378029946f86c041b116678
---

## DevEco Studio 26.0.0 Beta2引入的变更

### DevEco Studio底座升级，默认启用新UI，插件需适配新底座

DevEco Studio适配IntelliJ 2026.1.1底座升级后，默认启用新UI，界面及交互方式发生变更；底座默认携带的JDK由21升级到25，插件需适配新底座。

**变更影响**

1. 新UI默认启用：升级至IntelliJ 2026.1.1底座后，默认启用新UI，界面布局、图标样式及部分交互方式发生变更。如需使用经典UI，需手动开启。
2. 插件适配：如果插件未适配IntelliJ 2026.1.1版本，可能会出现不可使用的情况。
3. 部分菜单路径位置调整：
   * Server Certificates

     变更前：Settings > Tools > Server Certificates

     变更后：Settings > Appearance & Behavior > System Settings > Server Certificates
   * Required Plugins

     变更前：Settings > Build, Execution, Deployment > Required Plugins

     变更后：Settings > Appearance & Behavior > Required Plugins
   * Trusted Locations

     变更前：Settings > Build, Execution, Deployment > Trusted Locations

     变更后：Settings > Appearance & Behavior > Trusted Locations

**适配指导**

1. 如需切换回经典UI，在菜单栏进入 **File** **> Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选 **Enable new UI** 并点击 **Apply**，在弹窗中点击 **Restart** 重启即可完成UI切换。建议优先适配新UI风格，后续版本将不再支持经典UI。
2. 请更换使用已适配新底座IntelliJ 2026.1.1的插件版本。

### ArkUI-X工程配套的gradle版本变更

升级到DevEco Studio 26.0.0 Beta2及以上版本，历史版本创建的ArkUI-X工程会构建失败。

**变更影响**

如果ArkUI-X工程是使用DevEco Studio 26.0.0 Beta2以下版本创建的，升级到Beta2及以上版本，编译会失败，并提示Could not open settings generic class cache for settings file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vfkNus7XQ9G27CX4QPffIw/zh-cn_image_0000002659368057.png)**适配指导**

* **方式一：适配升级gradle**

  修改gradle-wrapper.properties中的distributionUrl，升级为9.4.0版本，并修改代码进行相应的适配。

  ```screen
  distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-9.4.0-bin.zip
  ```
* **方式二：指定使用jdk21**

  如果本地有jdk21，可以在gradle.properties中通过org.gradle.java.home变量指定使用jdk21。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/TeQBYVDxS22J-OEmFhr60g/zh-cn_image_0000002662851951.png)

## DevEco Studio 26.0.0 Beta1引入的变更

### Node.js版本升级

DevEco Studio & Command Line Tools携带的Node.js版本由18升级到24；ohpm-repo同步适配Node.js 24。

**变更影响**

1. 若基于hvigor & ohpm开发了自定义插件，插件需要适配Node.js 24版本。
2. 部署ohpm-repo时，需部署Node.js 24版本。

**适配指导**

1. hvigor & ohpm自定义插件参考Node.js 24的官方Release Notes分析影响点并进行适配。
2. 部署ohpm-repo时，使用Node.js 24版本进行部署。
