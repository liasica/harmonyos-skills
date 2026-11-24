---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-so
title: 批量导入和批量移除so库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 批量导入和批量移除so库
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:99fb0db45eb4ad5400277e08f3a1c9468198a2404663f4c2e5b204578023efce
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/IzygmkkmQzKypaJD-_6YFA/zh-cn_image_0000002808886457.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2E433B8FC62EE05538317A408660B80BC3AD3EBA0028BEEAE986EC9728580A3)

## 批量导入so库

1. 点击左侧导航栏的**Project**展开工程目录，将需要导入的so库文件复制到模块的libs目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/9Wa-a7-PQ9SiSRmuqoMuzw/zh-cn_image_0000002808886461.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9EFD68D2C465FADB8A2F0385921028324C1B2E4D13A7F710B166AAC475C7410)
2. 点击**File > Sync and Refresh Project**进行工程同步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/EQ_VQwvmQLWzQlYNKPVJ6Q/zh-cn_image_0000002808886465.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BB9E31B07CBFFF869F04433C36E5A03C03977DD26887EF0175ABBDEB0ED53E5)
3. 在**External Libraries**上右键，点击**Import Source Code of .so Library**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/JiZlIePxQ_W-nh9Exsdt5A/zh-cn_image_0000002808766375.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1846CDB787BF76C725ED3F22B60B58B592DBEA831BBFCD41270A052B0B49276)
4. 点击**.so Mapping File**尾部的文件夹图标，打开文件资源管理器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/CIeNlWU-R52wMXI5W8NeUw/zh-cn_image_0000002808766373.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=70F422685C38C0748FE65BBA40E4EB7A6903C1D6CAEC972F10B4EB250D2EA923)
5. 选择CMake项目的配置描述文件codemodel-v2-xxxx.json（文件路径为构建目录路径/.cmake/api/v1/reply/codemodel-v2-xxxx.json），点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/hiHCgqDETf22daXOc8w0RQ/zh-cn_image_0000002779566790.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=045A193E6B2FEEDEADF55736B9D146C5026C5AD13F463A61A692223D53124593)
6. 工具自动解析并展示匹配的so库，可选择单个或多个so库，也可在搜索栏输入关键字搜索，勾选后点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/EjlRBgAYQNmFPCxzsDYT5g/zh-cn_image_0000002808886455.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=421E56CAEB6219744AB52F6E300F4792B2019737152C1A2465AC556E64109FFA)
7. 导入完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/0W8UrVS2T-yPgtlN3LfkLA/zh-cn_image_0000002808766383.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=984F19C530448617744B1BD7F1AE204AAD34142620DABF651853232CFEDC4930)
8. 点击**File > Sync and Refresh Project**进行工程同步， 等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/G_NUHNEHR_e_i4IlFtZ-ng/zh-cn_image_0000002779566796.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B85F315D0B0677B7EC50AA3FC6DB8D564DEF38AC77794F00186916FEE4B7464)

## 批量移除so库

1. 点击左侧导航栏的****Project****展开工程目录，在****External Libraries****上右键，点击**Remove SO**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/u2t7wRojTRKCDPW255lHUA/zh-cn_image_0000002808766377.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=B80AE8CD96E1EB8926F8D773211F2E82EE6ED868DF4178A121C9EB58DDEE8CB0)
2. 在弹出的对话框中，列表仅展示已成功导入的so库，可直接勾选或通过搜索框过滤，选中需移除的so库，点击**OK**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/ZmpeEI-pSt6d83yP_NxgYQ/zh-cn_image_0000002779406822.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2BB2DA4D7126FD52086C48733481EDF0F6287B572ED83DE18334C10DA473C81)
3. 移除操作完成后，点击**OK**确认。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Y5Y4_timQoaf_ma5ImedBw/zh-cn_image_0000002779406812.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A22C68AF263A99E6D95C399C31BBDFC4D639889AE0D1B994DDA02D229E10B795)
4. 同步工程

   点击File，选择**Sync and Refresh Project**进行工程同步，然后等待索引完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/H1LoNU9PRXqd4n7KC0WfeA/zh-cn_image_0000002808766385.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=D21550A1F55308211F8520297F575D81A2B154ECD249FDAD5DEB6CE296CD43B0)
