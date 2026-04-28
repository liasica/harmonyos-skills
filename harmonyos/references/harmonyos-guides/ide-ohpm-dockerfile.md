---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dockerfile
title: 基于Dockerfile部署ohpm-repo私仓
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > 基于Dockerfile部署ohpm-repo私仓
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9e389b8aa03feaa3823e4f94e74df1542d06af01236271b54f7cacb3ca49435c
---

Dockerfile是构建Docker镜像的文本文件，其中包含了构建镜像的命令和说明，可以实现如下功能：

* 指定基础镜像。
* 创建项目目录。
* 修改config.yaml配置。
* 设置环境变量。
* 创建用户，设置文件权限。
* 运行install命令，更新环境变量。
* 运行start命令，启动私仓服务。

本文档介绍在Linux系统中如何使用Docker命令搭建ohpm-repo私仓。

**环境准备**

1. 下载[Docker镜像](https://www.docker.com/)，并进行环境搭建。
2. 下载ohpm-repo工具包，将下载的工具包重命名为ohpm-repo.zip，[点击链接获取](https://developer.huawei.com/consumer/cn/download/ohpm-repo)。
3. 将Dockerfile文件和ohpm-repo.zip放在同一目录下。

   Dockerfile文件模板如下：

   ```
   1. # 使用官方 Node.js 18 镜像
   2. FROM node:18
   3. COPY ./ohpm-repo.zip /tmp/ohpm-repo.zip
   4. RUN mkdir -p /opt/ohpm-repo && \
   5. unzip /tmp/ohpm-repo.zip -d /opt/ohpm-repo && \
   6. rm -f /tmp/ohpm-repo.zip
   7. # 修改conf/config.yaml的listen配置，不能用localhost和127.0.0.1，必须使用0.0.0.0
   8. RUN if [ -f /opt/ohpm-repo/conf/config.yaml ]; then \
   9. sed -i 's/listen: [^ ]*/listen: 0.0.0.0:8088/g' /opt/ohpm-repo/conf/config.yaml; \
   10. fi
   11. ENV OHPM_REPO_BIN_DIR="/opt/ohpm-repo/bin"
   12. ENV PATH="${OHPM_REPO_BIN_DIR}:${PATH}"
   13. # 创建用户，不允许使用root用户来运行ohpm-repo install和ohpm-repo start命令
   14. RUN useradd -m myuser && \
   15. chown -R myuser:myuser /opt/ohpm-repo && \
   16. chmod -R 755 /opt/ohpm-repo
   17. USER myuser
   18. RUN ohpm-repo install
   19. ENV OHPM_REPO_DEPLOY_ROOT="/home/myuser/ohpm-repo"
   20. CMD ["ohpm-repo", "start"]
   ```

**搭建私仓服务**

1. 在当前Dockerfile文件目录下，构建镜像。

   ```
   1. docker build -t ohpm-repo .
   ```
2. 启动服务，包括前台运行命令、后台运行命令两种形式。

   ```
   1. # 前台运行命令
   2. docker run -it -p 8088:8088 ohpm-repo
   3. # 后台运行命令
   4. docker run -d --restart=unless-stopped --name ohpm-repo -p 8088:8088 ohpm-repo
   ```
3. 浏览器访问IP地址8088，使用私仓服务。
