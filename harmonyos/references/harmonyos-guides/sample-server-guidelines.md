---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sample-server-guidelines
title: 示例服务器开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 升级服务 > 示例服务器开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5de7735a1b084cccaaaab69269475664161e838ec52a6ec3b7614de84fbd4f5a
---

## 开发步骤

1. 生成SSL证书

   生成serverKey.pem和serverCert.cer两个文件，用于示例服务器的SSL协议通信。

   ```
   1. openssl req -newkey rsa:2048 -nodes -keyout serverKey.pem -x509 -days 365 -out serverCert.cer -subj "/C=CN/ST=GD/L=GZ/O=abc/OU=defg/CN=hijk/emailAddress=test.com"
   ```
2. 修改bundle.json

   在build字段新增一个sub\_component。

   ```
   1. "sub_component": [
   2. "//base/update/updateservice/server_sample:testserver",
   3. ...
   4. ],
   ```
3. 建立代码目录

   进入到update\_updateservice目录下，执行以下命令，建立代码目录。

   ```
   1. mkdir server_sample                            // 建立示例服务器server_sample目录
   2. touch server_sample/BUILD.gn                   // 创建BUILD.gn编译文件
   3. mkdir server_sample/include                    // 建立示例服务器头文件include目录
   4. touch server_process.h                         // 创建server_process.h头文件
   5. mkdir server_sample/src                        // 建立示例服务器c/c++文件src目录
   6. touch server_sample/src/server_process.c       // 创建server_process.c文件
   7. touch server_sample/src/main.cpp               // 创建main.cpp文件
   ```
4. 编写编译文件BUILD.gn

   文件BUILD.gn一共编译两个ohos组件，一个是ohos\_shared\_library库文件libserver\_process.z.so，另一个是ohos\_executable可执行文件testserver。

   ```
   1. import("//build/ohos.gni")

   3. ohos_shared_library("server_process") {
   4. sources = [
   5. "//base/update/updateservice/server_sample/src/server_process.c",
   6. ]

   8. include_dirs = [
   9. "//base/update/updateservice/server_sample/include",
   10. "//third_party/openssl/include",
   11. ]

   13. deps = [
   14. "//base/update/updater/services/log:libupdaterlog",
   15. "//third_party/bounds_checking_function:libsec_static",
   16. "//third_party/openssl:crypto_source",
   17. "//third_party/openssl:ssl_source",
   18. "//utils/native/base:utils",
   19. ]

   21. part_name = "update_service"
   22. }

   24. ohos_executable("testserver") {
   25. sources = [
   26. "//base/update/updateservice/server_sample/src/main.cpp",
   27. ]

   29. include_dirs = [
   30. "//base/update/updateservice/server_sample/include",
   31. ]

   33. deps = [
   34. "//base/update/updateservice/server_sample:server_process",
   35. ]

   37. part_name = "update_service"
   38. }
   ```
5. 编写头文件server\_process.h

   文件server\_process.h声明了示例服务器的接口。

   ```
   1. #ifndef __SERVER_PROCESS_H__
   2. #define __SERVER_PROCESS_H__

   4. /*
   5. Init函数：用于创建socket环境，并预设置一些属性
   6. */
   7. int Init();

   9. /*
   10. SetParam函数：所有插件参数设置的统一接口
   11. */
   12. int SetParam(const char *key, const char *value);

   14. /*
   15. GetParam函数：所有插件参数获取的统一接口
   16. */
   17. int GetParam(const char *key, char *value);

   19. /*
   20. ReverseSetParamCallback函数：回调
   21. */
   22. int ReverseSetParamCallback(int(*setParam)(const char *key, const char *value));

   24. /*
   25. Open函数：用于服务打开的接口
   26. */
   27. int Open();

   29. /*
   30. MainLoop函数：每隔100ms调用一次
   31. */
   32. int MainLoop();

   34. /*
   35. Close函数，用于关闭服务并释放资源
   36. */
   37. int Close();

   39. #endif //__SERVER_PROCESS_H__
   ```
6. 编写server\_process.c、main.cpp

   文件server\_process.c主要声明了服务器的返回报文格式respondContent，main.cpp可参考普通SSL协议的服务器编写，注意包含相关头文件，同时加载serverKey.pem和serverCert.cer两个证书。

   ```
   1. #include "server_process.h"

   3. #include <netinet/in.h>
   4. #include <sys/types.h>
   5. #include <sys/socket.h>
   6. #include <arpa/inet.h>
   7. #include <unistd.h>
   8. #include <stdlib.h>
   9. #include <string.h>
   10. #include <stdio.h>

   12. #include "openssl/err.h"
   13. #include "openssl/ssl.h"

   15. #define SERVER_PEM "/data/sdcard/serverKey.pem"  //使用绝对路径
   16. #define SERVER_CER "/data/sdcard/serverCert.cer" //使用绝对路径

   18. #define LOG_PRINT(fmt, ...) printf("[ServerProcess][%s:%d] " fmt "\n", __func__, __LINE__, ##__VA_ARGS__)
   19. #define DO_CHECK(cond, log, ...) \
   20. if (!(cond)) {\
   21. LOG_PRINT(log);\
   22. __VA_ARGS__;\
   23. return -1;\
   24. }

   26. // 请参考server_process.h的接口予以实现，注意服务器返回的内容格式。
   27. respondContent = "{"
   28. "\"searchStatus\": 0,"
   29. "\"errMsg\": \"success\","
   30. "\"checkResults\": [{"
   31. "\"versionName\": \"sampleVersionName\","
   32. "\"versionCode\": \"sampleVersionCode\","
   33. "\"verifyInfo\": \"sampleVerifyInfoSha256Value\","
   34. "\"size\": 1234567,"
   35. "\"packageType\": 1,"
   36. "\"descriptPackageId\": \"abcdefg1234567ABCDEFG\","
   37. "}],"
   38. "\"descriptInfo\": [{"
   39. "\"descriptionType\": 0,"
   40. "\"content\": \"This package message is used for sampleContent\""
   41. "}]"
   42. "}";
   ```
7. 编译输出产物

   编译输出目录会新增testserver和libserver\_process.z.so两个文件。
8. 升级包制作

   参考[update\_packaging\_tools仓](https://gitcode.com/openharmony/update_packaging_tools)制作升级包。
9. 启动搜包服务器

   建议在开发板上新建一个纯英文路径，然后将testserver、libserver\_process.z.so、serverCert.cer和serverKey.pem放到同一个目录下，进入该目录，执行以下启动命令即可启动搜包服务器。

   ```
   1. ./testserver ./libserver_process.z.so &
   ```
