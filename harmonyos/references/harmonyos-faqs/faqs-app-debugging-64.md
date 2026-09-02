---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-64
title: HAP包在真机上安装失败如何解决
breadcrumb: FAQ > DevEco Studio > 应用调试 > HAP包在真机上安装失败如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eafcb5caa3c8141a4e243ddb0c7bf1f5c132b862cc0f892e819b2b16b370fd78
---

## 问题现象

* **问题一**：报9568263错误。

  在AGC中配置了真机的udid，并应用了更新后的p7b文件、证书文件进行sign后重新打包，使用hdc命令始终无法安装新HAP包。其他机器均正常安装。

  ```txt
  [Info]App install path:xxx.hap, queuesize:0, msg:error: failed to install bundle. code:9568263 error: install version downgrade.
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/iTdWl79-TTm6Eoxn9vSk-Q/zh-cn_image_0000002628569312.png)

* **问题二**：报9568283错误。

  先安装老包，修改build-profile.json5中的API版本后，再安装新包，报错如下:

  ```txt
  Install Failed: error: failed to install bundle.
  code:9568283
  error: install releaseType compatible not same.
  ```

## 背景知识

* [HAP打包](../harmonyos-guides/hap-package.md)相关指导请参见官网指南。
* [hdc命令](../harmonyos-guides/hdc.md)如何清除应用数据请参见官网指南。
* [调试命令](../harmonyos-guides/bm-tool.md)相关请参见官网指南。
* BMS的检验逻辑为：当两个版本的versionCode相同时，会检查apiReleaseType、minAPIVersion、targetAPIVersion是否一致，如果不一致则会报错。
* 错误码[9568263](../harmonyos-guides/bm-tool.md#section9568263-无法降级安装)：无法降级安装。

## 问题定位

* **问题一**：
  1. 查看日志返回的错误信息code:9568263 error: install version downgrade。正在安装的应用的版本号versionCode小于系统已安装的该应用的版本号。
  2. 如何修改应用的版本号versionCode。

     Stage模型修改app.json5中的versionCode字段。
* **问题二**：

  检查修改API版本前后的两个包对应的打包产物的versionCode、apiReleaseType、minAPIVersion、targetAPIVersion的一致性。打包产物查看路径：工程目录“build/default/outputs/default/”，找到对应.hap包后，打开module.json文件可核对相关字段。

## 分析结论

* **问题一**：由报错信息可以看到是待安装应用的版本号小于已安装的同应用的版本号。
* **问题二**：由于只修改了API版本号，两个版本的versionCode相同，但apiReleaseType、minAPIVersion、targetAPIVersion两个产物中的值不都分别一致，导致报错。

## 修改建议

* **问题一：**

  桌面直接卸载原版本应用（PC/2in1设备需要确保所有用户下都卸载完成，手机/平板侧需要关注隐私空间和主用户下是否卸载完成），重新执行安装。
  1. 手机界面直接卸载应用。
  2. 重新执行hdc install命令。

  使用命令卸载工具再重装。

  1. 切换到可执行hdc命令目录下，一般是DevEco Studio工具的SDK目录toolchains中会有hdc.exe的可执行文件。
  2. 先执行hdc shell bm dump -a <应用bundleName>检查下看是否之前的包还存在，如果存在就执行hdc uninstall <应用bundleName>卸载。
  3. 重新执行hdc install命令。
* **问题二：**修改app.json5中的versionCode值，使新包中的值大于老包中的值。
