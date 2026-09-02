---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon
title: 守护进程
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 默认特性 > 守护进程
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:09b1e5afba0d37655dbb72d121972a5988363e23d5ee68230c5af4435cd62f0a
---

守护进程是作为后台进程运行而不是在交互式用户的直接控制下运行的计算机程序。Hvigor守护进程是一个持续存在的后台进程，可以减少运行构建所需的时间。

## 了解守护进程

Hvigor客户端发送Daemon构建信息，如命令行参数、工程目录和环境变量等，以便于运行构建。客户端和守护进程之间的通信通过本地套接字进行连接，正在运行的守护进程最多开启8个，状态为非停止或中断的守护进程最多开启6个。

## 启用或关闭守护进程

Hvigor默认启用守护进程，您也可以通过以下几种方式来控制是否启用守护进程：

* 通过DevEco Studio菜单栏构建：
  + 点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选或取消勾选字段**Enable the Daemon for tasks**。
* 通过命令行构建：
  + 执行命令，其中<task>替换为具体任务名：

    ```bash
    // 启用守护进程
    hvigorw <task> --daemon
    // 关闭守护进程
    hvigorw <task> --no-daemon
    ```
  + 在[hvigor-config.json5](ide-hvigor-set-options.md)中配置daemon选项。

## 设置守护进程内存

守护进程最大的老生代内存默认是8192MB，对绝大多数构建来说已经足够了。如果您想自定义守护进程最大的老生代内存，可以通过以下两种方式修改，建议您参考本地剩余内存进行调整设置，其中命令行方式优先级高于hvigor-config.json5配置文件。

* 修改[hvigor-config.json5文件](ide-hvigor-set-options.md)中的maxOldSpaceSize配置。
* 执行命令修改守护进程内存，示例如下：

  ```bash
  hvigorw assembleHap --max-old-space-size=12345
  ```

守护进程新生代内存最大的半空间大小默认是16MB，通过设置最大的半空间大小，可以改变Node.js的垃圾收集频率，进而影响性能，同时也会改变消耗的内存大小。可以通过以下两种方式修改，其中命令行方式优先级高于hvigor-config.json5配置文件。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

* 修改[hvigor-config.json5文件](ide-hvigor-set-options.md)中的maxSemiSpaceSize配置。
* 执行命令修改守护进程内存，示例如下：

  ```bash
  hvigorw assembleHap --max-semi-space-size=32
  ```

## 设置守护进程最大空闲时长

守护进程最大空闲时长默认是3小时，从最后一次构建任务完成开始计算，超过3小时则守护进程退出。从26.0.0版本开始，支持自定义守护进程最大空闲时长，可以通过以下两种方式修改，其中命令行方式优先级高于hvigor-config.json5配置文件。

* 修改[hvigor-config.json5文件](ide-hvigor-set-options.md)中的hvigor.daemon.idleTimeout配置。
* 执行命令修改守护进程最大空闲时长，示例如下：

  ```bash
  hvigorw assembleHap -c properties.hvigor.daemon.idleTimeout=10800000
  ```

## 检查守护进程状态

如果您想获取正在运行的守护进程及其状态的列表，可以使用以下命令查看：

```bash
hvigorw --status-daemon
```

```txt
> hvigor PID    STATUS  PORT    ROOT_PATH
> hvigor 11072  idle    45001   D:\Demo1
> hvigor 18836  stopped 45000   D:\Demo2
```

| 守护进程状态 | 状态描述 |
| --- | --- |
| idle | 闲置 |
| half\_busy | 半忙碌 |
| busy | 忙碌 |
| canceled | 取消 |
| stopReq | 停止请求 |
| stopped | 停止 |
| broken | 中断 |

## 停止守护进程

在更改关于守护进程内存设置或调试故障时，重启守护进程是必要的。

您可用以下命令停止运行守护进程，这将停止该工程下的守护进程：

```bash
hvigorw --stop-daemon
```

如果您想停止所有守护进程，可以使用以下命令：

```bash
hvigorw --stop-daemon-all
```

## 性能影响

当您重复构建同一项目时，守护进程能够缩短构建时间。多次构建时，守护进程只会一次性将hvigor加载到内存中，而不会在每次构建时都进行加载。
