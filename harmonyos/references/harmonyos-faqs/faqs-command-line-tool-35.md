---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-35
title: 如何通过命令行或流水线脚本方式构建并安装应用
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何通过命令行或流水线脚本方式构建并安装应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:45ea2785a9ebfdc243431433fc9dd61d7e5a9a9b18335683ddee26da355e3aa4
---

## 问题现象

通过命令行方式如何打包构建并安装应用？通过搭建流水线通过脚本如何打包构建并安装应用？

## 背景知识

* [命令行工具Command Line Tools](../harmonyos-guides/ide-commandline-get.md)可调用[hvigor](../harmonyos-guides/ide-hvigor-commandline.md)任务通过命令行的方式构建应用，可用于构筑CI（Continuous Integration）流水线实现自动化的构建。
* [搭建流水线](../harmonyos-guides/ide-command-line-building-app.md)：除了使用DevEco Studio一键式构建应用/元服务外，还可以使用命令行工具来调用Hvigor任务进行构建。通过命令行的方式构建应用或元服务，可用于构建CI（Continuous Integration）流水线，按照计划时间自动化地构建HAP/APP、签名、安装运行等操作。

## 解决方案

* **使用命令行方式打包构建并安装应用。**
  1. 使用ohpm安装依赖。

     ohpm install --all
  2. 使用hvigorw命令执行打包构建。

     hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon
  3. 构建完成后，模块下build目录中会生成相应的hap编译产物。
  4. 如果构建时已配置签名文件，会分别生成带签名的.hap包和不带签名的.hap包。如果未配置签名文件，需要使用签名工具对包进行重签名。

     java -jar hap-sign-tool.jar sign-app -keyAlias "demo\_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "/path/demo.cer" -profileFile "/path/demo.p7b" -inFile "/path/hap-unsigned.hap" -keystoreFile "/path/demo.p12" -outFile "/path/hap-signed.hap" -keyPwd "test123" -keystorePwd "test123"
  5. 通过hdc工具将HAP推送到真机设备上进行安装。

     hdc shell bm install -p "xxx.hap"
* **搭建流水线通过脚本方式打包构建并安装应用。**
  1. 搭建流水线过程参考：[搭建流水线](../harmonyos-guides/ide-command-line-building-app.md)。
  2. 示例脚本可以参考：[示例脚本](../harmonyos-guides/ide-command-line-building-app.md#section14397105115226)。

## 常见FAQ

Q：HarmonyOS应用完成打包后，是否有上传到应用市场审核的相关脚本，实现发布管理自动化的构建。

A：可以通过[Publishing API（HarmonyOS）](../AppGallery-connect-References/agcapi-publishingapi-harmonyos-0000002093065194.md)完成HarmonyOS应用/元服务的发布管理工作，包括上传应用的版权版号等信息、编辑应用的简介等基本信息、更新应用视频等版本信息、提交应用发布或撤销审核等。

Q：Command Line Tools工具解压的目录太长会报文件名太长的错误，如何解决？

A：工具放到一个较短的路径，如C:/tools。
