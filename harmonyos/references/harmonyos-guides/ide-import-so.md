---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-so
title: 批量导入和批量移除so库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 批量导入和批量移除so库
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0849bb858fd48ed1be2409cf21d270ab7567f38411b7a0c7ff522479f5d14734
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/gZ7YSzGnTO2hSWDL1Mh3Sg/zh-cn_image_0000002808886457.png)

## 批量导入so库

1. 点击左侧导航栏的**Project**展开工程目录，将需要导入的so库文件复制到模块的libs目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/mwjxqUNGRUeVBxbl-RUZdw/zh-cn_image_0000002808886461.png)
2. 点击**File > Sync and Refresh Project**进行工程同步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/2gSqqiu2QsSw1irO12wJ1g/zh-cn_image_0000002808886465.png)
3. 在**External Libraries**上右键，点击**Import Source Code of .so Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/t6b4rNO-RLqBUGs5S-hIjA/zh-cn_image_0000002808766375.png)
4. 点击**.so Mapping File**尾部的文件夹图标，打开文件资源管理器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/rCfvcexNSgmOr2b0EE7PTw/zh-cn_image_0000002808766373.png)
5. 选择CMake项目的配置描述文件codemodel-v2-xxxx.json（文件路径为构建目录路径/.cmake/api/v1/reply/codemodel-v2-xxxx.json），点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/39Ummg3QSxW1wA56APWuCw/zh-cn_image_0000002779566790.png)
6. 工具自动解析并展示匹配的so库，可选择单个或多个so库，也可在搜索栏输入关键字搜索，勾选后点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/NMyyY4PyTTK4UwFD6Z3JHQ/zh-cn_image_0000002808886455.png)
7. 导入完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ZNbhUYI3SEqfpOz55fq3iQ/zh-cn_image_0000002808766383.png)
8. 点击**File > Sync and Refresh Project**进行工程同步， 等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/5-mj4aRVTCG8ePvtpjclKA/zh-cn_image_0000002779566796.png)

## 批量移除so库

1. 点击左侧导航栏的****Project****展开工程目录，在****External Libraries****上右键，点击**Remove SO**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ks2f3J1uRpmOaGDsx8RWiw/zh-cn_image_0000002808766377.png)
2. 在弹出的对话框中，列表仅展示已成功导入的so库，可直接勾选或通过搜索框过滤，选中需移除的so库，点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/4BioKnKNRoOfYyqx5RagBw/zh-cn_image_0000002779406822.png)
3. 移除操作完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ZwFJk-ncSnWOZq7rWXvHTA/zh-cn_image_0000002779406812.png)
4. 同步工程

   点击File，选择**Sync and Refresh Project**进行工程同步，然后等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/VgPjSyO6QcOG855RdBA1Ug/zh-cn_image_0000002808766385.png)
