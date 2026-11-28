---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-so
title: 批量导入和批量移除so库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 批量导入和批量移除so库
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:da2456350427ed0b73cb229c5cd82197c2c4ef0d8b01b0dda923539d90d94061
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/zcy1571vSfOuI-itqg7Hjg/zh-cn_image_0000002808886457.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBF7756D0DC651BC5178E99D4EF5D2731B670C1F180B55721D56B5757BCADE68)

## 批量导入so库

1. 点击左侧导航栏的**Project**展开工程目录，将需要导入的so库文件复制到模块的libs目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/T9GRtxZsTVe7Tb7cF2_k4A/zh-cn_image_0000002808886461.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=910ED2D1980032B27D986F86BF86A5A0D702CEC16F3DCD38B5482D126F93C24F)
2. 点击**File > Sync and Refresh Project**进行工程同步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/7naBl5s0SfyH7S5BGMybNQ/zh-cn_image_0000002808886465.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=64C0F92F885391D53B73866E1C3A45CEA6CDA1F883105B903FF9FAC1B967CC45)
3. 在**External Libraries**上右键，点击**Import Source Code of .so Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/lHxvwozBQ-6_aku98LCTYg/zh-cn_image_0000002808766375.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=D287F5AF940DDFF6977E4CB985A2F5EE1994370EFBE497F3F9CDDF734C9341AE)
4. 点击**.so Mapping File**尾部的文件夹图标，打开文件资源管理器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/uLD6x6w4TZGf5SoDNHENZw/zh-cn_image_0000002808766373.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=6562A1A7CD81293ACDBBE2457B948EFA589E15238B297D12F9F22ADB8AD7E888)
5. 选择CMake项目的配置描述文件codemodel-v2-xxxx.json（文件路径为构建目录路径/.cmake/api/v1/reply/codemodel-v2-xxxx.json），点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ZQxBGqLjSzOKW3LUd90-Hw/zh-cn_image_0000002779566790.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEA36A13DB7408F7A218EB83EA0698B8410AA5256345B6D41F674F86140FCFF9)
6. 工具自动解析并展示匹配的so库，可选择单个或多个so库，也可在搜索栏输入关键字搜索，勾选后点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/sg6_cRfMTDGJPH2S9NJqkQ/zh-cn_image_0000002808886455.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EF4B9B3D884C1D07E36AEB15D896322F4923A231041A9ACA7D5B7B300E91E5E)
7. 导入完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-cagDHGtRweyNRYEl6sfvA/zh-cn_image_0000002808766383.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7650804B98BD01493F16052346779E868D7D1DE0865322B021F0CE66A5A118D)
8. 点击**File > Sync and Refresh Project**进行工程同步， 等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/SVl8Zs8zSxK8Yhjz0LiEnQ/zh-cn_image_0000002779566796.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=872D1934A8D7C5343886C22134468B608B2FFA257DD6DA52FBD10A98A8496D85)

## 批量移除so库

1. 点击左侧导航栏的****Project****展开工程目录，在****External Libraries****上右键，点击**Remove SO**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/CvHiknSTR_e3a-o3VqNrhQ/zh-cn_image_0000002808766377.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A694AE83E50394E8E5DEF99ACE55DB1A516DCE1143599E6F3E781036F30998B)
2. 在弹出的对话框中，列表仅展示已成功导入的so库，可直接勾选或通过搜索框过滤，选中需移除的so库，点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/oetVaATTRIOVAomldOVxGg/zh-cn_image_0000002779406822.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB461D01AF6B1EACC4E9A66A511FB0C792E453B150F06A11570D9967C63E2407)
3. 移除操作完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/xZd6EcjYQsGzk3o0sK-nOg/zh-cn_image_0000002779406812.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=C41F7CE130795442016EEFBA86E9852053CC2D284E4ABC560F7A12EC78543F12)
4. 同步工程

   点击File，选择**Sync and Refresh Project**进行工程同步，然后等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/4-N8_Z4YT2yy5FdkfnLokQ/zh-cn_image_0000002808766385.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=563551571EB8D29E255FCE421781CAB2DFDD06B103F307DC14824C4BD5BAD7B6)
