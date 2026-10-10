---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-faq
title: 常见问题
breadcrumb: 指南 > DevEco Code > 常见问题
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:26+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:774e68e80a614638e4efce1eba18aa1ea436cb19b92c401861c769d86d2399b3
---

## 在鸿蒙电脑版DevEco Code执行命令时，提示“Permission denied：node”

**问题现象**

执行安装命令或检验环境搭建等命令时，提示没有node权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/v7V_zsr0QN-VEnCO4coJ0w/zh-cn_image_0000002749157632.png)

**可能原因**

配置环境变量时，未使用命令行解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，直接鼠标右键解压，导致压缩包中的文件执行权限和软链接丢失，Node.js环境变量添加失败。

**解决措施**

在终端中执行以下命令，对命令行工具解压。更多请参考[搭建环境（鸿蒙电脑）](ide-deveco-code-install.md#section193914295163)。

```shell
tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
```

## 启动鸿蒙电脑版DevEco Code时，提示"Local credentials are corrupted"

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/jRlj8fsiSs2XGzC5GTkfHA/zh-cn_image_0000002748997754.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ZcGO0m4HS8uzYKJYw8WwtQ/zh-cn_image_0000002749173362.png)

**可能原因**

鸿蒙电脑版DevEco Code只发布了尝鲜版，未发布稳定版。

**解决措施**

通过npm install -g @deveco/deveco-code命令安装尝鲜版。

## 在鸿蒙电脑DevEco Studio中安装DevEco Code时，提示“无法运行来自非应用市场的扩展程序”

**问题现象**

在鸿蒙电脑DevEco Studio中安装DevEco Code时，弹窗提示“无法运行来自非应用市场的扩展程序”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/_JMtxzVGRVKW7_xmHUa0RQ/zh-cn_image_0000002785060491.png)

**可能原因**

鸿蒙电脑的安全策略与防护机制，导致无法直接运行非应用市场的扩展程序。

**解决措施**

点击弹窗中的**去设置 >** **隐私和安全**，开启**运行来自非应用市场的扩展程序**后，重新安装DevEco Code。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/r8ObCGCbRa6f4im7BpWebw/zh-cn_image_0000002755421580.png)
