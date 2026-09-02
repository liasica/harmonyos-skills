---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-25
title: LSP Client Warning
breadcrumb: FAQ > DevEco Studio > 环境准备 > LSP Client Warning
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05b54b5c7e96ec22018372889f214ab3d5ff8744f8d174b44c33130d13d11de8
---

## 问题现象

从代码仓中将整个项目拉下来之后，在Windows系统下Sync一直报错。

错误信息如下：

```log
LSP Client Warning
Sync failed. The CPP language service will be provided using the cached compile_commands.json file, which may result in exceptions in certain cases. For the CPP language service to work correctly, make sure the sync is successful.
```

Sync虽然一直报错，但是构建打包都能正常使用（确认产物都正常输出了），Sync项目就是不成功。另外此问题在旧版本IDE上只报黄，最新版本的IDE会报红并在一段时间运行后出现NODE进程异常占用。

## 解决方案

可以尝试安装当前官方最新版本IDE，并新建一个项目，把新建module的配置文件复制过来解决，或者也可以把module目录下的.cxx和项目根目录下的.idea/.deveco/cxx/compile\_commands.json删除重试，具体步骤如下：

1. 手动替换modules或者删除.cxx缓存。
2. 重新尝试构建工程（Build->Build Haps），能够构建成功且.cxx缓存文件输出正常。
3. 此时再尝试全局同步工程（File->Sync and Refresh Project），IDE右下角C++的服务状态灯成功显示并且为绿色。
