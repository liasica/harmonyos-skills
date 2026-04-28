---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-daemon
title: 守护进程
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 守护进程
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a49b044cae922a46d0c3fd2fb4e87a16af9b6e650d7e10dfaaa04b9b789ce2e4
---

守护进程是作为后台进程运行而不是在交互式用户的直接控制下运行的计算机程序。Hvigor守护进程是一个持续存在的后台进程，可以减少运行构建所需的时间。

## 了解守护进程

Hvigor客户端发送Daemon构建信息，如命令行参数、工程目录和环境变量等，以便于运行构建。客户端和守护进程之间的通信通过本地套接字进行连接，正在运行的守护进程最多开启8个，状态为非停止或中断的守护进程最多开启6个。

## 启用禁用守护进程

Hvigor默认启用守护进程，您也可以通过以下几种方式来控制是否启用守护进程：

* 通过DevEco Studio菜单栏构建：
  + 点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选或取消勾选字段**Enable the Daemon for tasks**。
* 通过命令行构建：
  + 执行命令，其中<task>替换为具体任务名：

    ```
    1. // 启用守护进程
    2. hvigorw <task> --daemon
    3. // 关闭守护进程
    4. hvigorw <task> --no-daemon
    ```
  + 在[hvigor-config.json5](ide-hvigor-set-options.md)中配置execution.daemon选项。

## 设置守护进程内存

守护进程最大的老生代内存默认是8192MB，对绝大多数构建来说已经足够了。如果您想自定义守护进程最大的老生代内存，可以通过以下两种方式修改，建议您参考本地剩余内存进行调整设置。其中命令行方式优先级高于hvigor-config.json5配置文件。

* 修改[hvigor-config.json5文件](ide-hvigor-set-options.md)中的nodeOptions.maxOldSpaceSize配置。
* 执行命令修改守护进程内存，示例如下：

  ```
  1. hvigorw assembleHap --max-old-space-size=12345
  ```

守护进程新生代内存最大的半空间大小默认是16MB，通过设置最大的半空间大小，可以改变Node.js的垃圾收集频率，进而影响性能，同时也会改变消耗的内存大小。可以通过以下两种方式修改，其中命令行方式优先级高于hvigor-config.json5配置文件。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

* 修改[hvigor-config.json5文件](ide-hvigor-set-options.md)中的nodeOptions.maxSemiSpaceSize配置。
* 执行命令修改守护进程内存，示例如下：

  ```
  1. hvigorw assembleHap --max-semi-space-size=32
  ```

## 检查守护进程状态

如果您想获取正在运行的守护进程及其状态的列表，可以使用以下命令查看：

```
1. hvigorw --status-daemon
```

```
1. > hvigor PID    STATUS  PORT    ROOT_PATH
2. > hvigor 11072  idle    45001   D:\Demo1
3. > hvigor 18836  stopped 45000   D:\Demo2
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

```
1. hvigorw --stop-daemon
```

如果您想停止所有守护进程，可以使用以下命令：

```
1. hvigorw --stop-daemon-all
```

## 性能影响

当您重复构建同一项目时，守护进程能够缩短构建时间。多次构建时，守护进程只会一次性将hvigor加载到内存中，而不会在每次构建时都进行加载。
