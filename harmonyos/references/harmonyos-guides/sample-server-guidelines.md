---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sample-server-guidelines
title: 示例服务器开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 升级服务 > 示例服务器开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:56b392882eaa4f4d567c67b4a296d764b919ad37ad1ba9d15462d6d67ea895ad
---

## 功能介绍

示例服务器：在线升级本地仿真环境

本工具旨在模拟生产环境中的搜包服务器，基于SSL协议构建安全通信通道。它支持版本检测与升级包元数据查询，能够返回升级包的版本详情，文件校验值及大小等关键数据，帮助开发者在零依赖本地环境下模拟在线升级流程。

核心应用场景：

* 功能开发调试：为在线升级模块提供独立的测试数据源。
* 流程本地验证：在无需联网的情况下，全流程验证从检测更新到下载升级包的逻辑闭环。
* 包格式兼容性测试：快速验证不同格式升级包解析与处理的正确性。

## 开发步骤

示例服务器的开发，需要完成以下步骤：

### 准备SSL证书。

生成serverKey.pem和serverCert.cer两个文件，用于示例服务器的SSL协议通信。

```shell
openssl req -newkey rsa:2048 -nodes -keyout serverKey.pem -x509 -days 365 -out serverCert.cer -subj "/C=CN/ST=GD/L=GZ/O=abc/OU=defg/CN=hijk/emailAddress=test.com"
```

**说明** 

SSL证书用于保障服务器与设备之间的通信安全，证书有效期建议设置为365天以上。

### 修改bundle.json。

在build字段新增一个sub\_component。

```json
"sub_component": [
    "//base/update/updateservice/server_sample:testserver",
    ...
],
```

### 建立代码目录。

进入到update\_updateservice目录下，执行以下命令，建立代码目录。

```shell
mkdir server_sample                            // 建立示例服务器server_sample目录
touch server_sample/BUILD.gn                   // 创建BUILD.gn编译文件
mkdir server_sample/include                    // 建立示例服务器头文件include目录
touch server_sample/include/server_process.h   // 创建server_process.h头文件
mkdir server_sample/src                        // 建立示例服务器c/c++文件src目录
touch server_sample/src/server_process.c       // 创建server_process.c文件
touch server_sample/src/main.cpp               // 创建main.cpp文件
```

### 编写编译文件BUILD.gn。

文件BUILD.gn一共编译两个ohos组件，一个是ohos\_shared\_library库文件libserver\_process.z.so，另一个是ohos\_executable可执行文件testserver。

```gn
import("//build/ohos.gni")

ohos_shared_library("server_process") {
    sources = [
        "//base/update/updateservice/server_sample/src/server_process.c",
    ]

    include_dirs = [
        "//base/update/updateservice/server_sample/include",
        "//third_party/openssl/include",
    ]

    deps = [
        "//base/update/updater/services/log:libupdaterlog",
        "//third_party/bounds_checking_function:libsec_static",
        "//third_party/openssl:crypto_source",
        "//third_party/openssl:ssl_source",
        "//utils/native/base:utils",
    ]

    part_name = "update_service"
}

ohos_executable("testserver") {
    sources = [
        "//base/update/updateservice/server_sample/src/main.cpp",
    ]

    include_dirs = [
        "//base/update/updateservice/server_sample/include",
    ]

    deps = [
        "//base/update/updateservice/server_sample:server_process",
    ]

    part_name = "update_service"
}
```

### 编写头文件server\_process.h。

文件server\_process.h声明了示例服务器的接口。

```
#ifndef __SERVER_PROCESS_H__
#define __SERVER_PROCESS_H__

/*
 Init函数：用于创建socket环境，并预设置一些属性
 */
int Init();

/*
 SetParam函数：所有插件参数设置的统一接口
 */
int SetParam(const char *key, const char *value);

/*
 GetParam函数：所有插件参数获取的统一接口
 */
int GetParam(const char *key, char *value);

/*
 ReverseSetParamCallback函数：回调
 */
int ReverseSetParamCallback(int(*setParam)(const char *key, const char *value));

/*
 Open函数：用于服务打开的接口
 */
int Open();

/*
 MainLoop函数：每隔100ms调用一次
 */
int MainLoop();

/*
 Close函数，用于关闭服务并释放资源
 */
int Close();

#endif // __SERVER_PROCESS_H__
```

### 编写server\_process.c、main.cpp。

文件server\_process.c主要声明了服务器的返回报文格式respondContent，main.cpp可参考普通SSL协议的服务器编写，注意包含相关头文件，同时加载serverKey.pem和serverCert.cer两个证书。

```c
#include "server_process.h"

#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include "openssl/err.h"
#include "openssl/ssl.h"

#define SERVER_PEM "/data/sdcard/serverKey.pem"  // 使用绝对路径
#define SERVER_CER "/data/sdcard/serverCert.cer" // 使用绝对路径

#define LOG_PRINT(fmt, ...) printf("[ServerProcess][%s:%d] " fmt "\n", __func__, __LINE__, ##__VA_ARGS__)
#define DO_CHECK(cond, log, ...) \
if (!(cond)) {\
    LOG_PRINT(log);\
    __VA_ARGS__;\
    return -1;\
}

// 请参考server_process.h的接口予以实现，注意服务器返回的内容格式。
respondContent = "{"
    "\"searchStatus\": 0,"
    "\"errMsg\": \"success\","
    "\"checkResults\": [{"
        "\"versionName\": \"sampleVersionName\","
        "\"versionCode\": \"sampleVersionCode\","
        "\"verifyInfo\": \"sampleVerifyInfoSha256Value\","
        "\"size\": 1234567,"
        "\"packageType\": 1,"
        "\"descriptPackageId\": \"abcdefg1234567ABCDEFG\","
    "}],"
    "\"descriptInfo\": [{"
        "\"descriptionType\": 0,"
        "\"content\": \"This package message is used for sampleContent\""
    "}]"
"}";
```

### 编译输出产物。

编译输出目录会新增testserver和libserver\_process.z.so两个文件。

### 升级包制作。

参考[update\_packaging\_tools仓](https://gitcode.com/openharmony/update_packaging_tools)制作升级包。

### 启动搜包服务器。

建议在开发板上新建一个纯英文路径，然后将testserver、libserver\_process.z.so、serverCert.cer和serverKey.pem放到同一个目录下，进入该目录，执行以下启动命令即可启动搜包服务器。

```shell
./testserver ./libserver_process.z.so &
```

## 调试说明

示例服务器启动后，可通过以下方式进行调试验证：

1. **确认服务器启动成功**：执行启动命令后，服务器进程会在后台运行，可通过ps -ef | grep testserver命令查看进程状态。
2. **验证SSL通信**：确保serverKey.pem和serverCert.cer证书文件路径正确，证书文件应放置于/data/sdcard目录下。
3. **检查端口监听**：示例服务器默认监听端口需与设备端搜包接口配置一致，可通过netstat -an | grep <端口号>确认端口监听状态。
4. **日志查看**：服务器运行日志可通过logcat或串口日志查看，关键接口调用会打印[ServerProcess]前缀的日志信息。

**说明** 

示例服务器仅用于开发调试，不建议在生产环境直接使用。生产环境的升级服务器需要根据实际业务需求进行定制开发，包括权限验证、包管理、版本管控等完整功能。
