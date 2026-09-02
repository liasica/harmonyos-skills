---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-29
title: 新建项目运行报错ROR:node
breadcrumb: FAQ > DevEco Studio > 环境准备 > 新建项目运行报错ROR:node
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e8a349e7f72c258512f9ffad7999530bdadb33de83ee66a08a358e4f3e1576c9
---

## 问题现象

下载安装DevEco Studio并新建工程后运行项目，PC配置信息：Mac M1 Pro。

报错信息如下：

```txt
ROR:  node: *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[__NSCFString _stringByResolvingSymlinksInPathUsingCache:]: unrecognized selector sent to instance 0x60000385c000'
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/aOQRkh2-SC6YnjtmeXsqVw/zh-cn_image_0000002628405084.png "点击放大")

## 背景知识

HUAWEI DevEco Studio（获取工具请单击[链接下载](https://developer.huawei.com/consumer/cn/download/deveco-studio)，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用及元服务。

DevEco Studio提供开箱即用的开发体验，将HarmonyOS SDK、Node.js、Hvigor、OHPM、模拟器平台等进行合一打包，简化DevEco Studio安装配置流程。

## 问题定位

1. 排查PC设备是否存在多Node，命令行输入node -v，排查Node版本是否低于18。
2. 查看NODE\_HOME是否配置：
   * Windows环境：在系统或者用户的PATH变量中查看NODE\_HOME。
   * MacOS环境：终端输入echo $SHELL。

## 分析结论

1. Mac中Node.js版本与IDE自带的Node.js 18x有冲突。
2. 未配置Node环境。

## 修改建议

1. 重新下载一个Node.js18的版本。
2. 通过Help -> Edit Custom Properties...打开ide.node.location，将node的bin目录配置上去，参考如下：

* Windows环境：存放在node目录下。

  ide.node.location= node路径
* MacOS环境：存放在node/bin目录下。

  ide.node.location= node路径/bin
