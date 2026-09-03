---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-deploy-single-instance
title: 单点部署
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 部署指导 > 单点部署
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:05+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:49e89f66fedcdfd8a6a7c756b4365acbebfb1288d398e7013aee8c1f339006a0
---

**说明** 

ohpm-repo私仓不允许在Linux或macOS系统中使用root用户启动，请使用普通用户安装运行。

## 安装ohpm-repo工具

1. ohpm-repo依赖于Node运行，请提前安装Node.js，并完成环境变量的配置。具体安装请参考[Node.js官方网站](https://nodejs.org/download/release/latest/)。

   **说明** 

   ohpm-repo和Node.js的配套版本如下：

   * ohpm-repo 5.4.4之后版本，推荐使用Node.js 24.x版本。
   * ohpm-repo 5.4.4及之前版本，当数据存储类型为mysql且文件存储类型为sftp模式时，支持Node.js版本范围为[18.x,22.x]。
2. 下载ohpm-repo工具包，[点击链接获取](https://developer.huawei.com/consumer/cn/download/ohpm-repo)**。**
3. 解压ohpm-repo私仓工具包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/ebrqejjmQmW-5SkKXgbxvw/zh-cn_image_0000002701662228.png)

4. 请将ohpm-repo工具包解压目录中bin目录的路径配置到[系统环境变量](ide-ohpm-repo-faq.md#section24117279211)path中，执行如下查询命令:

   ```screen
   ohpm-repo -v
   ```

   终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考[FAQ](ide-ohpm-repo-faq.md#section82-执行命令-ohpm-repo-command报错-ohpm-repo-不存在或者-command-命令不存在)解决。

   **注意** 

   针对Linux和Mac系统，建议使用bash作为命令行界面。
5. 进入ohpm-repo解压目录的conf目录中，修改配置文件config.yaml：
   * 检查[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)配置，默认配置为localhost:8088 ，表示仅支持监听本机地址；如果希望其他机器通过ip/域名访问，则建议修改listen配置为ohpm-repo部署机器的ip：

     ```yaml
     listen: <部署ohpm-repo机器的ip>:8088
     ```
   * 检查[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_deploy_root)配置：如果选择不配置，会存储在默认地址中。禁止该路径配置为ohpm-repo解压根目录。
   * 数据存储db模块使用filedb：

     ```yaml
     db:
       type: filedb
       config:
         path: ./db
     ```
   * 文件存储store模块使用fs：

     ```yaml
     store:
       type: fs
       config:
         path: ./storage
         #server: http://localhost:8088
     ```
   * 检查是否配置了[store.config.server](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_store)，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考[server: 仓库内容的下载地址](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_li922300957171146)。如果[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的host为本机指定的ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<指定部署机器的ip/域名>:8088。

     **说明** 

     + 如果为ohpm-repo服务配置了反向代理服务器，则[store.config.server](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_store)必须填写为反向代理服务器的ip/域名地址，且需要配置[use\_reverse\_proxy](ide-ohpm-repo-configuration.md#section1074004784011)值为true。
     + config.yaml中各项配置的详细描述请见：[配置文件](ide-ohpm-repo-configuration.md)。
6. 进入ohpm-repo解压目录的bin目录下，执行安装命令:

   ```screen
   ohpm-repo install
   ```

   **说明** 

   不配置参数--config，默认使用ohpm-repo根目录中conf目录内自带的配置文件config.yaml。

   启动成功日志信息示例如下：

   ```screen
   PS D:\> ohpm-repo install
   [2025-08-26T14:29:15.153] [WARN] default - "listen" protocol is set to 'http' in "config.yaml" file, which is insecure, advise to use the more secure 'https' protocol instead.
   [2025-08-26T14:29:15.178] [INFO] default - initialize encryption component successfully.
   [2025-08-26T14:29:15.179] [INFO] default - initialize "file database" successfully.
   [2025-08-26T14:29:15.184] [INFO] default - initialize "file storage" successfully.
   [2025-08-26T14:29:15.194] [INFO] console - install successfully.
   [2025-08-26T14:29:15.195] [INFO] default - "deploy_root" environment variables: "OHPM_REPO_DEPLOY_ROOT = C:\Users\xxx\AppData\Roaming\Huawei\ohpm-repo".
   ```
7. 安装成功后，必须根据给出的提示信息及时刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式：

   **说明** 

   * Windows系统： 关闭当前窗口，重新开启一个窗口。
   * Linux系统或Mac系统： 在命令行中执行刷新命令：当shell为bash时执行***source ~/.bashrc*** 或者 . ***~/.bashrc*** ；当shell为zsh时，执行*source ~/.zshrc* 或者 . *~/.zshrc* 。

## 启动ohpm-repo

执行start命令启动ohpm-repo。

```screen
ohpm-repo start
```

启动成功日志信息如下：

```screen
PS D:\> ohpm-repo start
[2025-08-26T14:31:22.209] [WARN] default - "listen" protocol is set to 'http' in "config.yaml" file, which is insecure, advise to use the more secure 'https' protocol instead.
[2025-08-26T14:31:22.211] [INFO] default - config file path: "C:\Users\xxx\AppData\Roaming\Huawei\ohpm-repo\conf\config.yaml".
[2025-08-26T14:31:22.216] [INFO] default - initialize "file database" successfully.
[2025-08-26T14:31:22.217] [INFO] default - initialize "file storage" successfully.
[2025-08-26T14:31:22.237] [INFO] console - http address - localhost:8088 - ohpm-repo/5.1.5.
```
