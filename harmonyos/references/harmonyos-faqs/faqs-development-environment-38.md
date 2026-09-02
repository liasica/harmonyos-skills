---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-38
title: 安装依赖的hvigor插件报错问题汇总
breadcrumb: FAQ > DevEco Studio > 环境准备 > 安装依赖的hvigor插件报错问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a27fda7e855283b259c7a8396c01165efca484b48f05ecbe2ab1846bb72dc516
---

## 问题现象

安装依赖的hvigor插件报错，问题有哪些？

## 背景知识

* [开发hvigor插件](../harmonyos-guides/ide-hvigor-plugin.md#section627771916612)：hvigor主要提供了两种方式来实现插件：基于hvigorfile脚本开发插件、基于typescript项目开发。
* [配置npm代理](../harmonyos-guides/ide-environment-config.md#section197296441787)：hvigor、ohpm在初始化时需要从npm仓库下载依赖，如果需要代理才能访问网络，请配置npm的代理。

## 问题定位

* **场景一：执行指令npm install -force安装依赖时卡住进度条不动。**
* **场景二：执行指令npm install，报错connect ETIMEDOUT 104.16.25.34:443：**

  ```log
  npm ERR! code ETIMEDOUT
  npm ERR! syscall connect
  npm ERR! errno ETIMEDOUT
  npm ERR! network request to https://registry.npmjs.org/@react-navigation%2Fnative failed, reason: connect ETIMEDOUT 104.16.25.34:443
  npm ERR! network This is a problem related to network connectivity.
  npm ERR! network In most cases you are behind a proxy or have bad network settings.
  ```
* **场景三：执行指令npm install，出现警告WARN using --force Recommended protections disabled：**

  ```log
  C:\rohdemo\zxxx>npm install --force
  npm WARN using --force Recommended protections disabled.
  ] / idealTree:zgyt_oa_app_3: sill idealTree buildDeps
  ```
* **场景四：基于typescript项目开发hvigor插件依赖声明报错，执行npm install报错ERR! notarget a package version that does not exist**：

  ```log
  npm ERR! code ETARGET
  npm ERR! notarget No matching version found for @ohos/hvigor-ohos-plugin@5.0.0
  npm ERR! notarget In most cases you or one of your dependencies are requesting
  npm ERR! notarget a package version that does not exist.
  ```

## 分析结论

* **场景一和三：npm缓存问题。**
* **场景二和四：镜像源配置不正确，插件版本与hvigor不一致。**

## 修改建议

* **场景一和场景三解决方案：**
  1. 检查网络连接，确保网络连接稳定。
  2. 清除npm缓存。

     npm cache clean --force
  3. 删除package-lock.json或者yarn-lock.json文件。
* **场景二解决方案：**
  1. 报错显示无法连接镜像源，在C盘用户目录下检查.npmrc文件镜像源配置，确保镜像源配置可用。
* **场景四的解决方案：**
  1. 配置npm镜像：

     在用户目录下创建或打开.npmrc文件，配置如下信息：

     registry=https://repo.huaweicloud.com/repository/npm/

     @ohos:registry=https://repo.harmonyos.com/npm/

     打开package.json添加devDependencies配置并保存。

     **说明** 

     @ohos/hvigor-ohos-plugin的版本需要与当前@ohos/hvigor的版本保持一致。
  2. 执行npm install命令安装依赖。
  3. 查看自定义的目录下是否生成node\_modules目录，node\_modules目录下是否有安装的相关依赖目录，都存在说明依赖下载成功。
