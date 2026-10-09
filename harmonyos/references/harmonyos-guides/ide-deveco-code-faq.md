---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-faq
title: 常见问题
breadcrumb: 指南 > DevEco Code > 常见问题
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:69830e3ace73e3f721efa20d948ff5751871d4086ef50c828890e75b80bb946d
---

## 在鸿蒙电脑版DevEco Code执行命令时，提示“Permission denied：node”

**问题现象**

执行安装命令或检验环境搭建等命令时，提示没有node权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/OqhCUkUxT9-EYSg03t0yhA/zh-cn_image_0000002749157632.png)

**可能原因**

配置环境变量时，未使用命令行解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，直接鼠标右键解压，导致压缩包中的文件执行权限和软链接丢失，Node.js环境变量添加失败。

**解决措施**

在终端中执行以下命令，对命令行工具解压。更多请参考[搭建环境（鸿蒙电脑）](ide-deveco-code-install.md#section193914295163)。

```shell
tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
```

## 启动鸿蒙电脑版DevEco Code时，提示"Local credentials are corrupted"

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/s0rzkXOwRgqMA57E3b_u-Q/zh-cn_image_0000002748997754.png)

**可能原因**

在鸿蒙电脑终端Shell和DevEco Studio中使用DevEco Code时，登录信息独立存放。

当终端Shell和DevEco Stuido交叉使用DevEco Code时，在一个平台登录，需先清除另一个平台的登录信息。

**解决措施**

1. 在终端中执行以下命令清除登录信息。

   ```screen
   deveco auth reset
   ```
2. 打开环境变量配置文件。

   ```screen
   vim ~/.zshrc
   ```
3. 添加XDG\_CONFIG\_HOME环境变量，使鸿蒙电脑终端Shell和DevEco Stuido中的DevEco Code的登录信息存放到同一个位置。

   ```shell
   export XDG_CONFIG_HOME=~/.config    # ~/.config用户可自定义为其它路径
   ```

## 在鸿蒙电脑执行npm install -g @deveco/deveco-code@stable命令报错

**问题现象**

在鸿蒙电脑上执行npm install -g @deveco/deveco-code@stable命令安装DevEco Code时，有报错提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/HdXSn2bWTGiGcdKSBjZHmA/zh-cn_image_0000002749173362.png)

**可能原因**

鸿蒙电脑版DevEco Code只发布了尝鲜版，未发布稳定版。

**解决措施**

通过npm install -g @deveco/deveco-code命令安装尝鲜版。
