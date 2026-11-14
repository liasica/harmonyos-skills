---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-network
title: 离线环境配置指导
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 离线环境配置指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6d8e43449eff405f0defa7592c68c8125f792d560d21b620d7fa9d6cb976ff8f
---

如果开发者所使用的电脑处于完全无网络的离线环境中，需要先在一台可访问网络的电脑上准备好以下文件，将这些文件拷贝到无网络电脑中。

## 安装hypium

工程模板的工程级oh-package.json5文件中默认配置了hypium依赖，因此需要安装hypium，如果配置了其他依赖，也可参考以下步骤安装。

在可访问网络的电脑上创建一个空文件夹（如命名为third\_library），在文件夹中创建一个oh-package.json5文件，配置hypium依赖，配置如下：

```screen
{
  "dependencies": {
    "@ohos/hypium": "1.0.18"
  }
}
```

[配置环境变量并打开命令行工具](ide-commandline-get.md#section17776863449)，执行ohpm install命令，会生成oh\_modules文件夹和oh-package-lock.json5文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/lNk8dseDRySRfvnh7g0e2Q/zh-cn_image_0000002779407304.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2CCA72F5141732B38C5FCFB6CE83FAD6AAC8A1C19792C3C043C7ACF32A8F6B7)

将oh\_modules文件夹和oh-package-lock.json5文件拷贝到无网络电脑的工程根目录下。

**说明** 

有网环境和无网环境下使用的ohpm版本需保持一致，否则可能导致oh-package-lock.json5文件不生效。

## 安装三方库

通过如下两种方式使用三方库：

* 方式一：使用[ohpm-repo](ide-ohpm-repo.md)搭建私仓，将需要依赖的三方包发布至私仓中，并将[.ohpmrc文件](ide-ohpmrc.md#section11112159104)中的registry配置项的值替换为该私仓地址，以此从私仓中获取依赖。
* 方式二：在可访问网络的电脑上创建一个空文件夹（如命名为third\_library），在文件夹中创建一个oh-package.json5文件，设置三方包依赖，配置示例如下：

  ```screen
  {
    "dependencies": {
      "@ohos/hypium": "1.0.17",
      "@ohos/lottie": "^2.0.0" 
    }
  }
  ```

  打开命令行工具，执行ohpm install命令，会生成oh\_modules文件夹和oh-package-lock.json5文件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/4rC0NUCWRX6Yd_1u6qjsWg/zh-cn_image_0000002779407306.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=16787A521E7DB1ED5CFC59A299BF1987F8848B94A21492BF8DC2CCB47A7493C8)

  将oh\_modules文件夹和oh-package-lock.json5文件拷贝到无网络电脑的工程根目录下。

  **注意** 

  使用方法二时，需要确保可访问网络的电脑与无网络电脑中ohpm版本是一致的，以避免因oh-package-lock.json5文件版本不匹配而导致oh-package-lock.json5文件失效的问题。

## 部署模拟器

请参考[离线部署模拟器](ide-emulator-no-network.md)。
