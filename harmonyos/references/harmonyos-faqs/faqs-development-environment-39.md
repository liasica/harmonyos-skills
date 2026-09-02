---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-39
title: Mac安装运行DevEco Studio异常问题汇总
breadcrumb: FAQ > DevEco Studio > 环境准备 > Mac安装运行DevEco Studio异常问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:035879d5fd93292922eab2b873406ccfeb884ae5a26dc0a7761cd682ad23d6c6
---

## 问题现象

Mac DevEco Studio使用出现异常，原因有哪些。

## 背景知识

* idea.properties用于定制化DevEco Studio运行参数，基于IntelliJ平台扩展了HarmonyOS开发专属配置项，需通过菜单栏Help > Edit Custom Properties修改。

  | 参数 | 说明 | 默认值 | 风险提示 |
  | --- | --- | --- | --- |
  | grs\_url | 设置云端环境连接地址 | - | 需确保地址合法性 |
  | npm\_config\_strict\_ssl | 控制npm的HTTPS证书校验(true=开启校验，false=关闭) | true | 关闭后存在安全风险 |
  | ohpm\_config\_strict\_ssl | 控制ohpm的HTTPS证书校验(true=开启校验，false=关闭) | true | 关闭后存在安全风险 |
  | arkts.server.max.old.space.size | 设置Node进程内存上限（单位：MB）示例：arkts.server.max.old.space.size=12288 | 8192 (8GB) | 需根据物理内存调整 |

## 问题定位

* **Mac DevEco Studio无法正常使用，可能有多种现象和原因，汇总如下：**

  | 问题现象 | 问题原因 |
  | --- | --- |
  | 引用时出现延迟 需要等待一会才会找到命名的常量 | 内存溢出导致的卡顿 |
  | Mac DevEco Studio新建工程就报错: 00302013 Script Error | 用户Home目录中安装了hvigor |
  | Mac DevEco Studio 5.1.1 更新后 build报错 | 服务器的运行应用程序的打开文件的最大数及最大进程数设置 |
  | Mac DevEco Studio 的编辑器无法打开预览器和构建应用，报错 | IDE显示了Mac 系统中由 Finder 自动生成的隐藏文件DS\_Store |
* **场景一：引用时出现延迟,需要等待一会才会找到命名的常量：**

  命名常量，引用时出现延迟，需要等待一会才会找到命名的常量。
* **场景二：Mac DevEco Studio新建工程就报错:00302013\_Script\_Error：**

  Mac DevEco Studio新建工程就报错:00302013\_Script\_Error:

  ```txt
  > hvigor ERROR: 00302013 Script Error
  Error Message: The root node is not yet available for build. At file: hvigorfile.ts or hvigorconfig.ts
  *Try the following:
  > Check if the hvigorconfig.ts or hvigorfile.ts is configured correctly.
  > Check if the build-profile.json5 is configured correctly.
  > hvigor ERROR: BUILD FAILED in 1 s 114 ms
  ```
* **场景三：Mac DevEco Studio 5.1.1更新后build报错：**

  Mac DevEco Studio 5.1.1提示更新，升级后版本号为5.1.1.823，之前正常开发中的项目rebuild后报错如下，重装以及退回5.1.0版本报同样错误:

  ```txt
  > hvigor ERROR: Failed :entry:default@PackageHap... 
  > hvigor ERROR: Tools execution failed.
  Command failed with exit code null: java -Dfile.encoding=utf-8 -jar /Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/lib/app_packing_tool.jar --mode hap --force true --lib-path 
  /Users/MyProject/entry/build/default/intermediates/stripped_native_libs/default --json-path /Users/MyProject/entry/build/default/intermediates/package/default/module.json --resources-path /Users/MyProject/entry/build/default/intermediates/res/default/resources --index-path /Users/MyProject/entry/build/default/intermediates/res/default/resources.index --pack-info-path /Users/MyProject/entry/build/default/outputs/default/pack.info --out-path /Users/MyProject/entry/build/default/outputs/default/entry-default-unsigned.hap --ets-path /Users/MyProject/entry/build/default/intermediates/loader_out/default/ets --pkg-context-path /Users/MyProject/entry/build/default/intermediates/loader/default/pkgContextInfo.json
  ```
* **场景四：Mac DevEco Studio无法打开预览器和构建应用，报错hvigor ERROR:Failed：**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/DBFbyR-pTDWPx2zxoHEexA/zh-cn_image_0000002658924637.png "点击放大")

## 分析结论

* **场景一：内存溢出导致的卡顿。**
* **场景二：用户Home目录中安装了hvigor，执行编译命令找到的hvigor是用户Home下的，而不是DevEco Studio中自带的hvigor。**
* **场景三：服务器的运行应用程序的打开文件的最大数及最大进程数默认值较小。**
* **场景四：IDE显示了Mac系统中由Finder自动生成的隐藏文件DS\_Store 。**

## 修改建议

* **场景一：建议根据工程代码量和机器内存大小设置内存上限：**

  设置方法，打开DevEco Studio，通过菜单栏的Help > Edit Custom Properties...，打开idea.properties配置文件。在文件中新增一行arkts.server.max.old.space.size=12288，然后重启DevEco Studio。具体数值可以视情况增大或减小。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/M-kst18zSoSMjaZZvX46YQ/zh-cn_image_0000002658804701.png)
* **场景二：**
  1. 删除用户Home目录下的hvigor，即删除下列文件：
     + /Users/xxx/node\_modules；
     + /Users/xxx/package-lock.json；
     + /Users/xxx/package.json。
  2. 清理IDE缓存和项目缓存。
  3. 重启IDE。
* **场景三：**

  默认值相对较小默认为4096，需要改一下/etc/security/limits.conf的配置。

  添加两行配置：
  + soft nofile 327680和hard nproc 327680。
* **场景四：**

  更改硬盘格式至APFS可以使编辑器不显示DS\_Store文件从而解决此问题。
