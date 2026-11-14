---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-so
title: 批量导入和批量移除so库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 批量导入和批量移除so库
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6de0ea50a0a13d38f456673936b047f4c693794dadcac9a5b2251979c39e4185
---

从26.0.1版本开始，DevEco Studio支持批量导入和批量移除基于CMake工程构建生成的so库。若当前工程引用了其他工程模块构建的so库，开发者在当前工程中批量导入so库后，可直接查看so库的源码，实现代码阅读、断点调试与问题定位等功能，避免在多个工程间来回切换，提升开发效率。

## 使用说明

导入其他工程模块so库时，DevEco Studio根据so库的CMake工程的构建信息，将so库的源码关联到当前工程。

CMake工程的构建目录中需包含compile\_commands.json文件、CMake File API的请求文件、CMake File API的响应文件，具体说明如下：

| 文件 | 说明 |
| --- | --- |
| compile\_commands.json | 编译数据库文件，用于记录每个源文件的编译命令、头文件路径和宏定义。  存放路径：构建目录/compile\_commands.json。 |
| CMake File API的请求文件 | 用来通知CMake在配置阶段所需的构建信息。  存放路径：构建目录/.cmake/api/v1/query/codemodel-v2。 |
| CMake File API的响应文件 | 由CMake在配置阶段自动生成，以.json格式文件描述构建系统的结构信息，提供给DevEco Studio解析，实现代码阅读、断点调试与问题定位等功能。  存放路径：构建目录/.cmake/api/v1/reply/。 |

执行如下命令生成compile\_commands.json文件和codemodel的相关文件：

1. 在工程目录内创建构建目录，如build\_ohos。

   ```screen
   mkdir build_ohos
   ```
2. 创建CMake File API的请求文件。

   ```screen
   cmake -E make_directory build_ohos/.cmake/api/v1/query
   cmake -E touch build_ohos/.cmake/api/v1/query/codemodel-v2
   ```
3. CMake配置。

   ```screen
   cmake -S entry/src/main/cpp -B build_ohos -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_TOOLCHAIN_FILE="deveco安装目录/deveco-studio/sdk/default/openharmony/native/build/cmake/ohos.toolchain.cmake" -G Ninja
   ```
4. 编译。

   ```screen
   cmake --build build_ohos
   ```
5. 构建目录结构如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/DKdzKeTcRm2eFQs1uXHPLA/zh-cn_image_0000002808886457.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE6CF74EB3FD296AC27DB5CFDF4998AF6CADF1DAD2D12470E4CE8DF7FE22D3AB)

## 批量导入so库

1. 点击左侧导航栏的**Project**展开工程目录，将需要导入的so库文件复制到模块的libs目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/tnldTT2ASla74Ntvo1wcsQ/zh-cn_image_0000002808886461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F6640546D21C2D58105FA2BDF2B4D432E2FF9275230FA34D4C7F58E426F5FAD)
2. 点击**File > Sync and Refresh Project**进行工程同步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/8P87j1UURMWJ3zK0TAgYwQ/zh-cn_image_0000002808886465.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BA56E510839A91C9310AC2F5C2141FACD7552616E87B2098227DC7802B4A174)
3. 在**External Libraries**上右键，点击**Import Source Code of .so Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/_ePTUSNpSfiLnyLtOQ3beg/zh-cn_image_0000002808766375.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6E50B530892AE4AA2CC6BB8046A5AACDD2144840629FB3B0E1252390C21EC7D)
4. 点击**.so Mapping File**尾部的文件夹图标，打开文件资源管理器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/8dbZLyRETz6RdLAncz68lw/zh-cn_image_0000002808766373.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF6196CB85D6FDAAA726912DF5C4E8DBDC53F09ACD15C9B5CFB7FE9916D815F8)
5. 选择CMake项目的配置描述文件codemodel-v2-xxxx.json（文件路径为构建目录路径/.cmake/api/v1/reply/codemodel-v2-xxxx.json），点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/_iVmkUqOTQ29rNZovzS5Vw/zh-cn_image_0000002779566790.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=D04882FDCA2149F3DD9EDCE284CCB01DC2FD46D6D095F9C8A6382A12FEF9A4A0)
6. 工具自动解析并展示匹配的so库，可选择单个或多个so库，也可在搜索栏输入关键字搜索，勾选后点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/uSkPLimoTQumRVnYnrZ3Rw/zh-cn_image_0000002808886455.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF3A82F1040A0B7EB681ED07A5573C0217FC91953B41D7064C64E0D8B66AA91A)
7. 导入完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/JJv7JYw8QwWPC1dHHILzQQ/zh-cn_image_0000002808766383.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=266289945E43D148FD74926E6E75EC5DD2E47FF533425512533A514DB4B5B1D0)
8. 点击**File > Sync and Refresh Project**进行工程同步， 等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/YAO0ILlIRuCukCUTvWwGjg/zh-cn_image_0000002779566796.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=12F91D91FB8293D2834FC4B614344F10F0EA40D95567EEA8144FA060F527E48E)

## 批量移除so库

1. 点击左侧导航栏的****Project****展开工程目录，在****External Libraries****上右键，点击**Remove SO**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/uW6JajZ_S4id_FOYT7chCw/zh-cn_image_0000002808766377.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=0736B54E936EBA2BED184795AC8D0F69C5A249D9112A2B1A475C96AA3DE6E365)
2. 在弹出的对话框中，列表仅展示已成功导入的so库，可直接勾选或通过搜索框过滤，选中需移除的so库，点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/KmSlAQJFTfazY9ZcElTYdQ/zh-cn_image_0000002779406822.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=175ADD2E84E308F601AF9273593046ADC80878B54C8D1BB7F7086302673DFD18)
3. 移除操作完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/g325Q2a1RRm-BWKm3fvmSA/zh-cn_image_0000002779406812.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7860F5BAE4EB7D8C8C4C76EA0106043471C9AE4CA95ACB2ABD907584FC55BEC)
4. 同步工程

   点击File，选择**Sync and Refresh Project**进行工程同步，然后等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/E4nTxuE7TTm9aX6VLr7eqg/zh-cn_image_0000002808766385.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BC86A19EAD63FBB3BE889FC40192DC0B63A1AAD3DD35EF8F7B49140180F4BB1)
