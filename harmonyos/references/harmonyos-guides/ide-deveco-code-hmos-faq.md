---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-hmos-faq
title: 鸿蒙电脑版DevEco Code常见问题
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > 常见问题 > 鸿蒙电脑版DevEco Code常见问题
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:25+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:88cefa01c236f9427e4cc19f11ae8dc0cfcf5ea73fae349b61be13dc46315763
---

## 在鸿蒙电脑版DevEco Code执行命令时，提示“Permission denied：node”

**问题现象**

执行安装命令或检验环境搭建等命令时，提示没有node权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/b7r95pxTSYGyrg_IssDjwQ/zh-cn_image_0000002808886377.png)

**可能原因**

配置环境变量时，未使用命令行解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，而是直接鼠标右键解压，导致压缩包中的文件执行权限和软链接丢失，Node.js环境变量添加失败。

**解决措施**

在终端中执行以下命令，对命令行工具解压。更多请参考[搭建环境（鸿蒙电脑）](ide-deveco-code-install.md#section193914295163)。

```shell
tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
```

## 启动鸿蒙电脑版DevEco Code时，提示"Local credentials are corrupted"

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/hMfIz9sLRESrU39Lq2OrtQ/zh-cn_image_0000002808766297.png)

**可能原因**

在鸿蒙电脑终端Shell和DevEco Studio中使用DevEco Code时，登录信息独立存放。

当终端Shell和DevEco Studio交叉使用DevEco Code时，在一个平台登录，需先清除另一个平台的登录信息。

**解决措施**

1. 在终端中执行以下命令清除登录信息。

   ```screen
   deveco auth reset
   ```
2. 打开环境变量配置文件。

   ```screen
   vim ~/.zshrc
   ```
3. 添加XDG\_CONFIG\_HOME环境变量，使鸿蒙电脑终端Shell和DevEco Studio中的DevEco Code的登录信息存放到同一个位置。

   ```shell
   export XDG_CONFIG_HOME=~/.config    # ~/.config用户可自定义为其它路径
   ```

## 在鸿蒙电脑执行npm install -g @deveco/deveco-code@stable命令报错

**问题现象**

在鸿蒙电脑上执行npm install -g @deveco/deveco-code@stable命令安装DevEco Code时，有报错提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Dd2KImefQfejOyGcFZJKqA/zh-cn_image_0000002808766301.png)

**可能原因**

鸿蒙电脑版DevEco Code只发布了尝鲜版，未发布稳定版。

**解决措施**

通过npm install -g @deveco/deveco-code命令安装尝鲜版。

## 在鸿蒙电脑DevEco Studio中安装DevEco Code时，提示“无法运行来自非应用市场的扩展程序”

**问题现象**

在鸿蒙电脑DevEco Studio中安装DevEco Code时，弹窗提示“无法运行来自非应用市场的扩展程序”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/mDTE9LShSAqquUq78yBLdw/zh-cn_image_0000002808766293.png)

**可能原因**

鸿蒙电脑的安全策略与防护机制，导致无法直接运行非应用市场的扩展程序。

**解决措施**

点击弹窗中的**去设置 >** **隐私和安全**，开启**运行来自非应用市场的扩展程序**后，重新安装DevEco Code。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/MTZg_QiJTniCtRYlsR2DXw/zh-cn_image_0000002808886379.png)

## 在鸿蒙电脑DevEco Studio中安装DevEco Code时，提示“由于网络问题，DevEco Code安装失败，请调整网络后再次尝试”

**问题现象**

在鸿蒙电脑DevEco Studio中安装DevEco Code时，报安装失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/TBpgcnOeQPmZGW9J2GAvgQ/zh-cn_image_0000002808886381.png)

**可能原因**

原因一：安装时，使用npm官方源或淘宝镜像源外的其他镜像源，导致安装失败。

原因二：安装时使用npm官方源，由于国内网络访问npm官方仓库速度较慢，导致安装失败。

**解决措施**

方式一：安装时使用淘宝镜像源，提升访问npm仓库速度。

```screen
npm install -g @deveco/deveco-code --registry=https://registry.npmmirror.com
```

方式二：将全局替换为淘宝镜像后，再执行安装命令，提升访问npm仓库速度。

```screen
npm config set registry https://registry.npmmirror.com
npm install -g @deveco/deveco-code
```

## 在鸿蒙电脑DevEco Studio中升级或卸载DevEco Code失败

**问题现象**

在鸿蒙电脑DevEco Studio中升级或卸载DevEco Code失败，显示method为unknown。

* 升级：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/dI32HjspSGW1cjGKKY088g/zh-cn_image_0000002808886383.png)
* 卸载：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/eDrCbRO7R1ibUajyfgHG-g/zh-cn_image_0000002808766295.png)

**可能原因**

使用其他来源（如DevNode-OH）的node，未使用DevEco Studio或Command Line Tools中自带的node。

**解决措施**

重新配置环境变量，具体请参考[搭建环境（鸿蒙电脑）](ide-deveco-code-install.md#section193914295163)。
