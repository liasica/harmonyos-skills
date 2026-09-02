---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-14
title: ohpm install下载三方库时报错
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm install下载三方库时报错
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c53d95b0723ad3611e89edc992f7ecdd82034772ee551e35607edff0d86374a1
---

## 问题现象

执行ohpm install XXX命令下载库失败。

```log
fetch meta info of package '@mpaas/antui' failed - GET https://repo.harmonyos.com/ohpm/@mpaas/antui 404( Not Found )
```

## 背景知识

* [ohpm](../harmonyos-guides/ide-ohpm-cli.md)作为OpenHarmony三方库的包管理工具，支持OpenHarmony共享包的发布、安装和依赖管理。
* .ohpmrc是ohpm的配置文件，ohpm从命令行和.ohpmrc文件中获取其配置设置。ohpm config命令可用于修改用户级.ohpmrc文件的内容。更多配置文件知识可以参考：[ohpmrc](../harmonyos-guides/ide-ohpmrc.md)。

## 解决方案

1. 排查.ohpmrc中是否配置了正确的中心仓地址。

   项目级配置文件：/path/to/my/project/.ohpmrc。

   用户级配置文件：

   MacOS默认位置：~/.ohpm/.ohpmrc。

   windows操作系统默认位置：C:\Users\用户名\.ohpm\.ohpmrc。

   仓库配置，支持配置多个地址，使用英文逗号分隔。

   ```txt
   registry=https://ohpm.example.com/ohpm,https://repo.example.com/ohpm
   ```
2. 若无法访问中心仓，需要确认当前网络连接是否正常，保证可以访问公网。
3. 排查网络代理问题，如网络环境需要使用代理，ohpm代理信息，在http\_proxy和https\_proxy中，将user、password、proxyserver和port按照实际代理服务器进行修改。

   ```txt
   http_proxy=http://用户名:密码@域名或IP:端口
   ```

   ```screen
   https_proxy=http://用户名:密码@域名或IP:端口
   ```

   **说明** 

   如果password中存在特殊字符，如@、#、\*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

   | 特殊符号 | ASCII码 |
   | --- | --- |
   | ! | %21 |
   | @ | %40 |
   | # | %23 |
   | $ | %24 |
   | & | %26 |
   | \* | %2A |
4. 确认以上配置成功后，正常就可以下载[OpenHarmony三方库中心仓](https://ohpm.openharmony.cn/#/cn/home)中的库，但是如果想要下载的库没有上传到官方中心仓，例如阿里云的mPaas，需要在.ohpmrc中根据group指定组织的仓库地址。支持多个仓库地址，以英文逗号间隔，且优先级大于registry配置，多个仓库地址的优先级按照配置顺序排序。

   registry=https://ohpm.example.cn/ohpm,https://repo.example.com/ohpm

   指定仓库地址

   @mpaas:registry=https://mpaas-ohpm.example.com/meta
5. ohpm默认忽略SSL证书校验，如果需要开启，则需要在.ohpmrc中配置有效的证书路径，否则也会导致下载失败。

   strict\_ssl=true

   ca\_files=/path/to/cert

## 常见FAQ

Q：执行ohpm install安装依赖成功，但是没看到安装的依赖。

A：注意执行ohpm install的路径，oh-package.json5分为模块级和工程级，需要在执行安装命令的路径下查看oh-package.json5和oh\_modules。

Q：显示connect ETIMEDOUT连接超时是什么原因？怎么解决？

A：ETIMEDOUT表示客户端在尝试连接远程服务器时，在指定时间内未能建立连接。具体可能原因和解决方法如下，开发者可以按序排查：

1. 代理配置问题：
   * 代理设置错误或未生效：

     表现：[环境诊断](../harmonyos-guides/ide-environment-config.md#section1912218441119)报错。

     解决方案：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)，[配置NPM代理](../harmonyos-guides/ide-environment-config.md#section197296441787)，[配置OHPM代理](../harmonyos-guides/ide-environment-config.md#section10372836765)。

2. 网络与连接问题：
   * 网络不通或不稳定：

     表现：ping ohpm.openharmony.cn超时，curl请求失败。

     解决方案：切换网络（如改用手机热点）。
   * 防火墙或安全软件拦截：

     表现：即使网络正常，仍无法连接。

     解决方案：临时关闭防火墙或杀毒软件测试。

3. 服务端与本地环境问题：
   * ohpm服务端暂时不可用：

     表现：https://ohpm.openharmony.cn无法打开，或返回5xx/4xx错误。

     解决方法：建议稍后重试。
   * ohpm本地缓存损坏：

     表现：重复报错，清理后恢复正常。

     解决方法：运行指令：ohpm cache clean。
