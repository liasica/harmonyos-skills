---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fileio-guidelines
title: 应用文件访问(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用文件访问与管理 > 应用文件访问(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d2bff9f969736249dcc38ba00bc30645e874791f01a3be96482f5324603166f
---

## 场景介绍

FileIO模块提供了部分文件基础操作能力，其他能力请参考[libc标准库](../harmonyos-references/musl.md)/[c++标准库](../harmonyos-references/cpp.md)。

## 约束限制

进行文件操作之前，必须保证传入正确有效的URI或path。

## 接口说明

接口的详细说明，请参考[FileIO](../harmonyos-references/capi-oh-fileio-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| FileManagement\_ErrCode OH\_FileIO\_GetFileLocation(char \*uri, int uriLength, FileIO\_FileLocation \*location) | 获取文件存储位置。 |
| enum FileIO\_FileLocation FileIO\_FileLocation | 文件存储位置枚举值。 |
| enum FileManagement\_ErrCode FileManagement\_ErrCode | 文件管理模块错误码。 |

## 开发步骤

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```txt
target_link_libraries(sample PUBLIC libohfileio.so)
```

**添加头文件**

```
#include <cstdio>
#include <cstring>
#include <filemanagement/fileio/oh_fileio.h>
```

调用OH\_FileIO\_GetFileLocation接口获取文件存储位置。示例代码如下所示：

```
void GetFileLocationExample(char *uri)
{
    FileIO_FileLocation location;
    FileManagement_ErrCode ret = OH_FileIO_GetFileLocation(uri, strlen(uri), &location);
    if (ret == 0) {
        if (location == FileIO_FileLocation::LOCAL) {
            printf("Succeeded in getting file location, this file is on local.");
        } else if (location == FileIO_FileLocation::CLOUD) {
            printf("Succeeded in getting file location, this file is on cloud.");
        } else if (location == FileIO_FileLocation::LOCAL_AND_CLOUD) {
            printf("Succeeded in getting file location, this file is on  local and cloud.");
        }
    } else {
        printf("Failed to get file location, error code is %d", ret);
    }
}
```
