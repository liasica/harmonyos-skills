---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-path
title: 自定义.hvigor目录路径
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 自定义.hvigor目录路径
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce68fd08096af289957609c22377a495d50708924a07f1d98490b54a78562b0c
---

.hvigor目录默认位于用户目录下：

* Windows：C:\Users\username\.hvigor
* macOS：/Users/username/.hvigor
* Linux：
  + root用户：/root/.hvigor
  + 非root用户：/home/username/.hvigor

若默认目录的磁盘空间不足，开发者需要自定义.hvigor目录路径，可通过以下方式自行配置。

说明

自定义.hvigor目录时，不能包含空格。

* Windows环境变量设置方法：

  在系统或者用户的变量中，添加自定义.hvigor目录的绝对路径。

  变量名：HVIGOR\_USER\_HOME

  变量值：自定义存放.hvigor目录的绝对路径。如D:\HvigorUserHome

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/KuwjBT2fRG2tIcEjmICsyA/zh-cn_image_0000002530913062.png?HW-CC-KV=V1&HW-CC-Date=20260427T235715Z&HW-CC-Expire=86400&HW-CC-Sign=DE76EEA68DA427F4867415C06F098C2F1BAB50FD9C0CEF6F2C0F908B0D59F859)
* macOS环境变量设置方法：

  在macOS上为DevEco Studio设置环境变量需要使用launchd来设置。
  + 临时生效的设置方式：

    在终端中执行launchctl setenv语句并重新启动DevEco Studio即可。

    ```
    1. launchctl setenv HVIGOR_USER_HOME /Users/xx #本处路径请替换为.hvigor目录的绝对路径
    ```

    该设置方式在重启电脑后将失效。
  + 重启不失效的设置方式：

    说明

    在macOS上设置系统变量的方式因系统版本不同而存在多种差异，以下仅为在macOS上为DevEco Studio设置系统变量的一种示例，具体设置方式以系统版本为准。

    在/etc/launchd.conf（若该文件不存在，可自行创建）中添加如下内容。

    ```
    1. setenv HVIGOR_USER_HOME /Users/xx #本处路径请替换为.hvigor目录的绝对路径
    ```

    设置完成后，重启电脑后才可生效。
* Linux环境变量设置方法：

  打开终端工具，执行以下命令。

  ```
  1. vim ~/.bashrc
  ```

  添加HVIGOR\_USER\_HOME环境变量。

  ```
  1. export HVIGOR_USER_HOME=/home/xx  #本处路径请替换为.hvigor目录的绝对路径
  ```

  保存并关闭文件，使用source命令重新加载.bashrc配置文件。

  ```
  1. source ~/.bashrc
  ```
