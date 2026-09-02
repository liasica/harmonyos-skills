---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-emulator
title: 模拟器工具（Emulator）
breadcrumb: 指南 > 命令行工具 > 模拟器工具（Emulator）
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6b368c146e36aa11bea9559e8e9ce21f49f66b9310d9cf1245cfbb328955ca76
---

从6.1.0 Release版本开始，Command Line Tools集成Emulator工具，支持Windows和macOS平台，可独立进行模拟器创建、启动、关闭、镜像下载等操作。

从26.0.0版本开始，支持在Linux平台上使用Emulator，具体使用方式请参考[使用Linux版本Emulator工具](ide-commandline-emulator.md#section15887175165919)。

**说明** 

在macOS上使用命令行工具时，如果弹框提示Emulator无法验证开发者，可以在系统的**设置 > 隐私与安全性**中选择**仍要打开Emulator，**或者使用[DevEco Studio目录下的Emulator工具](ide-emulator-command-line.md)。

## 环境准备

Emulator工具在command-line-tools安装目录的emulator目录下，有两种执行命令的方式。

* 方式一：在命令行终端中进入emulator目录下，执行命令。
* 方式二：配置环境变量后，在任意目录下执行命令。
  + Windows环境变量设置方法：

    在系统或者用户的PATH变量中，添加路径{command-line-tools安装目录}/emulator，配置完成后重新打开命令行窗口使环境变量生效。
  + macOS/Linux环境变量设置方法：

    打开命令行终端，执行以下命令。

    ```bash
    export PATH={command-line-tools安装目录}/emulator:$PATH
    ```

## 模拟器命令

Emulator命令请参考[通过命令行使用模拟器](ide-emulator-command-line.md)。

## 在模拟器上推包调试

可通过hdc工具在模拟器上进行推包调试。

1. 使用时需要先确认模拟器和hdc的连接状态，模拟器的IP和端口号是127.0.0.1:5555，如果端口号已经被占用，则从5555起递增2，例如5555、5557、5559，端口号范围在5555-15555之间。

   ```bash
   hdc list targets
   ```
2. 如果未连接，执行命令`hdc tconn {IP:端口号}`连接模拟器，例如：

   ```bash
   hdc tconn 127.0.0.1:5555
   ```
3. 连接成功后，通过hdc在模拟器上安装、卸载应用等，更多使用方式请参考[SDK命令行工具](command-line-tools-overview.md)。

## 使用Linux版本Emulator工具

从26.0.0版本开始，支持在Linux平台使用模拟器工具。

### 环境准备

当前仅支持Ubuntu 18.04及以上的Linux系统，使用前需要安装相关的依赖，以Ubuntu 18.04操作系统为例，执行命令：

```bash
apt install -y libatomic1 libpulse0 libegl1 libgbm1 libgl1 libpng16-16 libfontconfig1 libfreetype6 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libsm6 libice6 libxkbcommon-x11-0 libxkbcommon0 libglib2.0-0
```

### 使用约束

* Linux模拟器依赖系统kvm能力，需要手动将Emulator程序当前用户加入/dev/kvm所在的组中。
* Linux模拟器图形渲染依赖/dev/dri下的设备渲染节点，如card0、renderD128等，需要手动将Emulator程序当前用户加入相关节点的用户组中。
* 如需使用第三方远程桌面工具操作Linux，请确保工具可使用的图形驱动支持OpenGL4.1或以上版本。

### 模拟器命令差异

针对无图形界面的Linux环境，[启动模拟器命令](ide-emulator-command-line.md#section1986131715236)必须添加-noWindow参数。除此之外，其他命令和Windows/macOS相同，详细命令请参考[通过命令行使用模拟器](ide-emulator-command-line.md)。
