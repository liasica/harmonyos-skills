---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-27
title: 使用Dockerfile搭建Command Line Tools流水线
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 使用Dockerfile搭建Command Line Tools流水线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fa247b61819f783e436ad2f2b525476ea55fbdca57ebe5723768f65db782c12b
---

## 问题现象

如何使用Dockerfile搭建Command Line Tools流水线？

## 背景知识

* [流水线搭建](../harmonyos-guides/ide-command-line-building-app.md)：流水线可通过命令行的方式搭建，包括准备构建环境、构建HAP、签名运行等操作。可在Windows、Linux和macOS下调用相应命令来执行。
* Dockerfile：是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明。
* [Command Line Tools](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)：集合了HarmonyOS应用开发所用到的系列工具，包括SDK管理sdkmgr、代码检查codelinter、三方库的包管理ohpm、命令行解析hstack。

## 解决方案

1. 指定基础镜像；
2. 设置工作目录；
3. 设置环境变量，设置时区、语言和字符集；
4. 更新APT源列表并安装基础工具；
5. 下载并安装多种开发工具和依赖项；
6. 设置环境变量。

```shell
#使用 Ubuntu 18.04 作为基础镜像，可以替换为其他版本的 Ubuntu 或其他 Linux 发行版
FROM --platform=linux/amd64 ubuntu:18.04

#并设置工作目录为 /home/openharmony，可以根据需要更改工作目录
WORKDIR /home/openharmony

#设置环境变量，设置时区、语言和字符集，并禁用交互式配置，可以根据需要更改时区、语言和字符集
ENV TZ=Asia/Shanghai LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 DEBIAN_FRONTEND=noninteractive 

#下边是更新APT源列表并安装基础工具，可以根据实际需求增减安装的工具和依赖项
RUN sed -i "s@https://.*archive.ubuntu.com@https://repo.huaweicloud.com@g" /etc/apt/sources.list \
	&& sed -i "s@https://.*security.ubuntu.com@https://repo.huaweicloud.com@g" /etc/apt/sources.list \
	&& apt-get update -y \
	&& apt-get install -y apt-utils binutils bison flex bc build-essential make mtd-utils gcc-arm-linux-gnueabi u-boot-tools python3.8 python3-pip python3.8-dev git zip unzip curl wget gcc g++ ruby=1:2.5.1 dosfstools mtools default-jre default-jdk scons python3.8-distutils perl openssl libssl-dev cpio git-lfs m4 ccache zlib1g-dev tar rsync liblz4-tool genext2fs binutils-dev device-tree-compiler e2fsprogs git-core gnupg gnutls-bin gperf lib32ncurses5-dev libffi-dev zlib* libelf-dev libx11-dev libgl1-mesa-dev lib32z1-dev xsltproc x11proto-core-dev libc6-dev-i386 libxml2-dev libxslt1-dev lib32z-dev libdwarf-dev \
	&& apt-get install -y grsync xxd libglib2.0-dev libpixman-1-dev kmod jfsutils reiserfsprogs xfsprogs squashfs-tools  pcmciautils quota ppp libtinfo-dev libtinfo5 libncurses5 libncurses5-dev libncursesw5 libstdc++6 python2.7 gcc-arm-none-eabi dialog tzdata \
	&& apt-get install -y vim ssh locales \
	&& rm -rf /etc/localtime \
	&& ln -s /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime \
	&& apt-get install -y --no-install-recommends\
		aapt=1:8.1.* \
        adb=1:8.1.* \
        libyaml-dev:amd64=0.1.* \
		xmlstarlet=1.6.* \
		libpq-dev=10.* \
		ninja-build=1.8.* \
		tcl=8.6.* \
        file=1:5.32* \
		dos2unix=7.3.* \
		wine-development=3.6-1 \
		time=1.7* \
		bindfs=* \
		clang-format-9=1:9-* \
		libasm-java=7.0-* \
		binutils-aarch64-linux-gnu=2.30-* \
		expect=* \
		cmake \
		g++-multilib=4:7.4.0* \
		gcc-multilib=4:7.4.0* \
	&& apt-get install -y doxygen \
	&& rm -rf /etc/localtime \
	&& locale-gen "en_US.UTF-8" \
        && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
        && echo $TZ > /etc/tunezone \
        && echo "y\ny\n" | unminimize \
	&& rm -rf /bin/sh /usr/bin/python /usr/bin/python3 /usr/bin/python3m \
	&& ln -s /bin/bash /bin/sh \
	&& ln -s /usr/bin/python3.8 /usr/bin/python3 \
	&& ln -s /usr/bin/python3.8 /usr/bin/python3m \
	&& ln -s /usr/bin/python3.8 /usr/bin/python \
	&& curl https://gitee.com/oschina/repo/raw/fork_flow/repo-py3 > /usr/bin/repo \
	&& chmod +x /usr/bin/repo \
	&& git clone https://gitee.com/liwentao_uiw/llvm-lnt  /home/openharmony/lnt \
	&& git clone https://gitee.com/liwentao_uiw/llvmopen-source-transfer-gitee.git -b ohos_toolchain /home/openharmony/test \ 
        && python3 /home/openharmony/lnt/setup.py install \
	&& pip3 install --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple requests setuptools pymongo kconfiglib pycryptodome ecdsa ohos-build pyyaml prompt_toolkit==1.0.14 redis json2html yagmail python-jenkins python-gitlab==3.11.0 lxml Swig==4.0.2 \
	&& pip3 install esdk-obs-python -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.org \
	&& pip3 install six --upgrade --ignore-installed six \
	&& pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pure-python-adb==0.3.0.dev0 \
                    javalang==0.13.0 \
                    tabulate==0.8.7 \
                    more-itertools==4.2.0 \
                    # scipy==1.5.4 \
                    dataclasses==0.6 \
                    esprima==4.0.1 \
		    protobuf==3.15.6 \		
	&& pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pytz==2016.10 pyyaml==5.1.2 \
	&& pip3 install --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple --upgrade pip \
	&& pip3 install --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple tensorflow==2.8.4 numpy==1.22.3 \
	
#下载并安装多种开发工具和依赖项，包括 Clang、HC-Gen、GCC RISC-V、Ninja、GN、Node.js、QEMU、OpenJDK、ccache 等。可以根据需要替换为其他版本或来源的下载链接并更改安装路径、工具版本等信息。
	&& mkdir -p /home/tools \
	&& mkdir -p /home/tools/gn \
        && mkdir -p /home/tools/jdk \
	&& wget -P /home/tools https://repo.huaweicloud.com/openharmony/compiler/clang/12.0.1-530132/linux/clang-530132-linux-x86_64.tar.bz2 \
	&& wget -P /home/tools https://repo.huaweicloud.com/harmonyos/compiler/hc-gen/0.65/linux/hc-gen-0.65-linux.tar \
	&& wget -P /home/tools https://repo.huaweicloud.com/harmonyos/compiler/gcc_riscv32/7.3.0/linux/gcc_riscv32-linux-7.3.0.tar.gz \
	&& wget -P /home/tools https://repo.huaweicloud.com/harmonyos/compiler/ninja/1.9.0/linux/ninja.1.9.0.tar \
	&& wget -P /home/tools https://repo.huaweicloud.com/harmonyos/compiler/gn/1717/linux/gn-linux-x86-1717.tar.gz \
	&& wget -P /home/tools https://mirrors.huaweicloud.com/nodejs/v14.19.1/node-v14.19.1-linux-x64.tar.xz \
	&& wget -P /home/tools https://hm-verify.obs.cn-north-4.myhuaweicloud.com/qemu-5.2.0.tar.xz \
        && wget -P /home/tools https://repo.huaweicloud.com/harmonyos/compiler/open-jdk/8u252/linux/jdk8u252+9-linux-amd64.tar.gz \
        && wget -P /home/tools https://github.com/ccache/ccache/releases/download/v4.7.4/ccache-4.7.4-linux-x86_64.tar.xz \
	&& tar -jxvf /home/tools/clang-530132-linux-x86_64.tar.bz2 -C /home/tools \
		&& mv /home/tools/clang-530132 /home/tools/llvm \
	&& tar -xvf /home/tools/hc-gen-0.65-linux.tar -C /home/tools \
	&& tar -xvf /home/tools/gcc_riscv32-linux-7.3.0.tar.gz -C /home/tools \
	&& tar -xvf /home/tools/ninja.1.9.0.tar -C /home/tools \
	&& tar -xvf /home/tools/gn-linux-x86-1717.tar.gz -C /home/tools/gn \
	&& tar -xJf /home/tools/node-v14.19.1-linux-x64.tar.xz -C /home/tools \
        && tar -xvf /home/tools/jdk8u252+9-linux-amd64.tar.gz -C /home/tools/jdk \
        && tar -xJf /home/tools/ccache-4.7.4-linux-x86_64.tar.xz -C /home/tools \
	&& cp /home/tools/node-v14.19.1-linux-x64/bin/node /usr/local/bin \
	&& ln -s /home/tools/node-v14.19.1-linux-x64/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
	&& ln -s /home/tools/node-v14.19.1-linux-x64/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx \
        && ln -s /home/tools/jdk/jdk8u252/bin/java /usr/local/bin/java \
	&& tar -xJf /home/tools/qemu-5.2.0.tar.xz -C /home/tools \
	&& sed -i '$aexport PATH=/home/tools/llvm/bin:$PATH' /root/.bashrc \
	&& sed -i '$aexport PATH=/home/tools/hc-gen:$PATH' /root/.bashrc \
	&& sed -i '$aexport PATH=/home/tools/gcc_riscv32/bin:$PATH' /root/.bashrc \
	&& sed -i '$aexport PATH=/home/tools/ninja:$PATH' /root/.bashrc \
	&& sed -i '$aexport PATH=/home/tools/node-v14.19.1-linux-x64/bin:$PATH' /root/.bashrc \
	&& sed -i '$aexport PATH=/home/tools/gn:$PATH' /root/.bashrc \
        && sed -i '$aexport PATH=/home/tools/jdk/jdk8u252/bin:$PATH' /root/.bashrc \
        && sed -i '$aexport PATH=/home/tools/ccache-4.7.4-linux-x86_64:$PATH' /root/.bashrc \
	&& sed -i '$aexport PATH=/root/.local/bin:$PATH' /root/.bashrc \
	&& export PATH=/home/tools/llvm/bin:$PATH \
	&& export PATH=/home/tools/hc-gen:$PATH \
	&& export PATH=/home/tools/gcc_riscv32/bin:$PATH \
	&& export PATH=/home/tools/ninja:$PATH \
	&& export PATH=/home/tools/node-v14.19.1-linux-x64/bin:$PATH \
	&& export PATH=/home/tools/gn:$PATH \
        && export PATH=/home/tools/jdk/jdk8u252/bin:$PATH \
        && export PATH=/home/tools/ccache-4.7.4-linux-x86_64:$PATH \
	&& export PATH=/root/.local/bin:$PATH \
	&& cd /home/tools/qemu-5.2.0 \
	&& mkdir build \
	&& cd build \
	&& ../configure --target-list=arm-softmmu \
	&& make -j \
	&& make install \
	&& cd /home/openharmony \
	&& rm -rf /home/tools/*.tar \
	&& rm -rf /home/tools/*.gz \
	&& rm -rf /home/tools/*.xz \
	&& rm -rf /home/tools/qemu-5.2.0 \
	&& npm install -g @ohos/hpm-cli --registry https://mirrors.huaweicloud.com/repository/npm/ \
        && cd /usr/lib/python3/dist-packages/ \
        && sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.cpython-38m-x86_64-linux-gnu.so \
        && sudo ln -fs apt_pkg.cpython-38m-x86_64-linux-gnu.so apt_pkg.so
		
#COPY ./clang+llvm-10.0.1-x86_64-linux-gnu-ubuntu-16.04.tar.xz /home/tools
#COPY ./cmake-linux-x86-3.16.5.tar.gz /home/tools

#设置环境变量，根据需要更改环境变量的值
ENV LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 PATH="/home/tools/llvm/bin:/home/tools/hc-gen:/home/tools/gcc_riscv32/bin:/home/tools/ninja:/home/tools/node-v14.19.1-linux-x64/bin:/home/tools/gn:/home/tools/jdk/jdk8u252/bin:/home/tools/ccache-4.7.4-linux-x86_64:/root/.local/bin:${PATH}"
```

## 常见FAQ

Q：该Dockerfile是否可在docker上直接运行？

A：以上Dockerfile已在Linux环境上验证。建议开发者升级到19以上版本运行该docker。若使用macOS环境需要自行根据环境修改Dockerfile进行适配。

Q：ARM主机如何使用Dockerfile搭建Command Line Tools流水线？

A：可以尝试使用qemu-user-static（qus）工具配置宿主机环境，运行针对异构架构的OCI镜像（即docker镜像）。
