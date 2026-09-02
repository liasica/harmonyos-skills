---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-81
title: 应用在真机上安装时提示失败的原因有哪些
breadcrumb: FAQ > DevEco Studio > 应用调试 > 应用在真机上安装时提示失败的原因有哪些
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:a2be58191a529b3e62b6a80acc45c45203e8d5a18613c0eae783d1891f4844c9
---

## 问题现象

* 问题一：报9568263错误。

  在AGC中配置了真机的udid，并应用了更新后的p7b文件、证书文件进行sign后重新打包，使用hdc命令始终无法安装新HAP包。其他机器均正常安装。

  运行命令hdc install xxx.hap的报错信息如下：

  ```txt
  [Info]App install path:xxx.hap, queuesize:0, msg:error: failed to install bundle. code:9568263 error: install version downgrade.
  ```
* 问题二：报9568283错误。

  先安装老包，修改build-profile.json5中的API版本后，再安装新包，报错如下：

  ```txt
  Install Failed: error: failed to install bundle.
  code:9568283.
  error: install releaseType compatible not same.
  ```
* 问题三：项目配置了多个入口ability，运行项目报错，错误信息如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/fdBMHIZDRW-F8XjeIxvT-Q/zh-cn_image_0000002682761918.png "点击放大")
* 问题四：运行项目出现如下报错信息。

  ```txt
  Install Failed: error: failed to install bundle.
  code:9568320.
  error: no signature file.
  ```

  根据错误码[9568320](../harmonyos-guides/bm-tool.md#section9568320-签名文件不存在)提供的处理方案无法解决问题。
* 问题五：项目修改包名后安装失败，报错信息如下：

  ```txt
  hvigor ERROR: Failed :entry:default@SignHap...
  hvigor ERROR: BundleName in the project configuration does not match that in the SigningConfigs.
  Detail: Open the project-level build-profile.json5 file. Change the bundleName value.
  to that in the SigningConfigs. Otherwise, go to the app.json5 file and change the bundleName value there.
  at /Users/hmn/Desktop/xxx/ztyhm/build-profile.json5.
  hvigor ERROR: BUILD FAILED in 18 s 719 ms.
  ```
* 问题六：多设备部署时选择卸载重装，实际卸载的设备与预期不一致，且部分设备重新安装时报9568263错误。

## 背景知识

* [HAP打包](../harmonyos-guides/hap-package.md)相关指导请参见官网指南。
* [hdc命令](../harmonyos-guides/hdc.md)如何清除应用数据请参见官网指南。
* [调试命令](../harmonyos-guides/bm-tool.md)相关请参见官网指南。
* BMS的检验逻辑为：当两个版本的versionCode相同时，会检查apiReleaseType、minAPIVersion、targetAPIVersion是否一致，如果不一致则会报错。
* 错误码[9568263](../harmonyos-guides/bm-tool.md#section9568263-无法降级安装)：无法降级安装。
* 模块启动顺序：
  1. 拉起应用的入口模块。该模块加载时创建一个AbilityStage实例，用于初始化等操作。
  2. 模块初始化完成后，将启动对应的入口UIAbility。
  3. UIAbility加载完成后，生成一个WindowStage类实例并绑定。WindowStage作为应用进程内的窗口管理器，UIAbility通过它管理窗口，并在该窗口上加载首个ArkUI页面，呈现到设备上。
* [工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)的字段说明。

## 问题定位

* 问题一：

  查看日志返回的错误信息code:9568263 error: install version downgrade。正在安装的应用的版本号versionCode小于系统已安装的该应用的版本号。
* 问题二：

  检查修改API版本前后的两个包对应的打包产物的versionCode、apiReleaseType、minAPIVersion、targetAPIVersion的一致性。打包产物查看路径：工程目录build/default/outputs/default/，找到对应.hap包后，打开module.json文件可核对相关字段。
* 问题三：
  1. 检查项目中各个模块的module.json5是否配置了skills字段，配置了该字段则表示该模块为入口ability。确认项目的正确入口ability是哪个，一个项目只需要一个主入口即可。
  2. 检查IDE运行项目时的命令是否正确，如：hdc shell aa start -a EntryAbility -b com.example.myapplication中的入口模块EntryAbility是否与项目主入口ability相同。
* 问题四：

  检查工程级build-profile.json5文件中配置是否正确，是否缺少字段。
* 问题五：

  根据报错提示"BundleName in the project configuration does not match that in the SigningConfigs."可知：修改包名后需要同步修改签名信息。
* 问题六：

  DevEco Studio在部署应用时，检测到设备上已存在相同bundleName的应用包，会执行卸载命令hdc uninstall <包名>。第一个设备上已存在与正在安装应用bundleName相同的应用，因此执行了卸载操作。第二个设备也执行了卸载操作，但已安装应用的VersionCode大于正在安装应用的VersionCode，导致重新安装时报9568263错误。

## 分析结论

* 问题一：

  由报错信息可以看到是待安装应用的版本号小于已安装的同应用的版本号。卸载旧版本重新安装即可。
* 问题二：

  由于只修改了API版本号，两个版本的versionCode相同，但apiReleaseType、minAPIVersion、targetAPIVersion两个产物中的值不都分别一致，导致报错。
* 问题三：

  由于项目配置了多个入口ability，IDE运行项目时的默认入口ability错误，导致项目运行时启动报错。
* 问题四：

  工程级build-profile.json5文件的products配置项中缺少signingConfig字段。
* 问题五：

  修改包名后，需要同步修改签名信息。
* 问题六：

  多设备部署时，DevEco Studio会对每个检测到相同bundleName应用的设备执行卸载操作。当某设备上已安装应用的VersionCode高于正在安装应用的VersionCode时，卸载后重新安装会报9568263错误。

## 修改建议

* 问题一：
  + 桌面直接卸载原版本应用（PC/2in1设备需要确保所有用户下都卸载完成，手机/平板侧需要关注隐私空间和主用户下是否卸载完成），重新执行安装。
    1. 手机界面直接卸载应用。
    2. 重新执行hdc install命令。
  + 使用命令卸载工具再重装。
    1. 切换到可执行hdc命令目录下，一般是DevEco Studio工具的SDK目录toolchains中会有hdc.exe的可执行文件。
    2. 先执行hdc shell bm dump -a <应用bundleName>检查下看是否之前的包还存在，如果存在就执行hdc uninstall <应用bundleName>卸载。
    3. 重新执行hdc install命令。
* 问题二：
  + 修改app.json5中的versionCode值，使新包中的值大于老包中的值。
* 问题三：
  + 在运行报错时，把该命令中对应ability的module.json5中的skills字段去掉，不作为入口ability；
  + 在运行项目前，编辑运行配置，在Launch Options下手动选择项目的正确入口ability。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/XWWvJo0KQhOxmDtS8UCpOw/zh-cn_image_0000002682922108.png "点击放大")
* 问题四：

  在工程级build-profile.json5文件的products配置项中增加signingConfig字段的配置信息，例如："signingConfig": "default"。
* 问题五：

  在工程级build-profile.json5中把signingConfigs属性值删除，同步信息后重新签名。
* 问题六：
  + 提前在相关设备上卸载已存在的同bundleName应用（PC/2in1设备需要确保所有用户下都卸载完成，手机/平板侧需要关注隐私空间和主用户下是否卸载完成），保证设备上不存在与正在安装应用bundleName相同的应用，然后进行多设备部署。即使设备上有相同包名的应用，正在安装应用的VersionCode也应高于系统中已安装应用的VersionCode。
  + 若需降级安装，对于已安装的证书分发类型为app\_gallery或签名证书类型为debug的三方应用，可使用-d命令实现降级安装：hdc shell bm install -p /data/example.hap -d。
  + 多设备运行可参考[多设备运行](../harmonyos-guides/ide-run-debug-configurations.md#section109181222131217)。

## 常见FAQ

Q：编译报错"The type of the target device does not match the deviceType configured in the module.json5 file of the selected module"，手机设备已经连接上DevEco Studio并且module.json5的deviceTypes里已配置phone。

A：请参考如下步骤排查：

1. 指定target设备的类型与模块配置的设备类型不匹配，请参考[FAQ](faqs-compiling-and-building-141.md)排查。
2. DevEco Studio版本和设备版本不一致，具体参考：[所有HarmonyOS版本](../harmonyos-releases/overview-allversion.md)，[DevEco Studio下载地址](https://developer.huawei.com/consumer/cn/download/deveco-studio)。
