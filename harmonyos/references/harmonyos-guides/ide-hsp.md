---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hsp
title: 开发动态共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发及发布共享包 > 开发动态共享包
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cff1dd72a13eaffb6c4a1c6b9d671acff56a7d76cc8b53d166b5ec097a266f80
---

DevEco Studio支持开发动态共享包[HSP（Harmony Shared Package）](in-app-hsp.md)。在应用/元服务开发过程中部分功能按需动态下载，或开发元服务场景时需要分包加载，可使用HSP实现相应功能。当有多个安装包需要资源共享时，也可利用HSP减少公共资源和代码重复打包。

说明

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* 集成态HSP：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名。

## 使用约束

* HSP及其使用方都必须是API 10及以上版本Stage模型。
* HSP及其使用方都必须使用[模块化编译](ide-hvigor-esmodule-compile.md)模式。
* 从DevEco Studio 6.0.1 Beta1开始，创建HSP模块时支持选择C++版本。

## 开发动态共享包

### 创建HSP模块

1. 通过如下两种方法，在工程中添加新的Module。
   * 方法1：鼠标移到工程目录顶部，单击鼠标右键，选择**New > Module**，开始创建新的Module。
   * 方法2：选中工程目录中任意文件，然后在菜单栏选择**File > New > Module**，开始创建新的Module。
2. 模板类型选择**Shared Library**，点击**Next**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/0R6DYC-wRUap_F3ct8reNA/zh-cn_image_0000002561832851.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=DF54EBA340A3E95A04E83B79C06D7CC25F3748958B4743B14CAFE2D94385A438)
3. 在**Configure New Module**界面中，设置新添加的模块信息，设置完成后，单击**Finish**完成创建。从DevEco Studio 6.0.1 Beta1开始，支持选择C++版本。
   * **Module name**：新增模块的名称，如设置为library。
   * **Device type**：支持的设备类型。
   * **Enable native**：是否创建一个用于调用C++代码的模块。
   * **C++ Standard：**C++标准库，取值包括：Toolchain Default、C++11、C++14。仅打开Enable native时需要配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/wjUrjnLAT0ajss66__8Wfw/zh-cn_image_0000002530912920.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=605E1E391BAA792CB15419096B698935775CBDC986ED1A557D31E014B4540BDE)

   创建完成后，会在工程目录中生成HSP模块及相关文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/SpqiIbCSRty8hUp6-zGe1A/zh-cn_image_0000002530752918.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=47EF9886D2395BBC2CAD61A3BD47F480853BECFA26993095C930B5F42FBC4D2C)

### 编译HSP模块

说明

如果HSP未开启[混淆](ide-build-obfuscation.md)，则后续HSP被集成使用时，将不会再对HSP包进行混淆。

参考[应用内HSP开发指导](in-app-hsp.md)开发完HSP模块后，选中模块名，然后通过DevEco Studio菜单栏的**Build > Make Module ${libraryName}**进行编译构建，生成HSP。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/BNYtWtwmQZ-W8r4BmprzgQ/zh-cn_image_0000002530912916.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=A49BD44E0768AE2E2E4DE0B36CDD3035D76CA3AD1ED4E9A19245DF0F2C8BE295)

打包HSP时，会同时默认打包出HAR，在模块下build目录下可以看到\*.har和\*.hsp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/4CFS_ZivRQWhIQGPju2pQA/zh-cn_image_0000002530912922.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=30AAE717EB74A5AD47FDDA7E4922B4DBBBDABBE5CC77E8CB5130F03B74B66AE0)

如需在应用内共享HSP，请将HSP共享包上传至私仓（请参考[将三方库发布到 ohpm-repo](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_从ohpm-repo获取三方库)），请先按以下操作编译生成\*.tgz包。

1. 点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/f4jUH7N8S5SV0GRAd8VwTQ/zh-cn_image_0000002530912906.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=2A8E5523068138EFEDED074C19703F687A7DAD24F243EEF77320FFF077297261)图标将编译模式切换成release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/NTick6tHTYiMwuKPkEENcQ/zh-cn_image_0000002530752914.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=4683F66FF925B5DB8C77A9E7AF941914FC93102D84D5BE1AD38E366C57013312)
2. 选中HSP模块的根目录，点击**Build > Make Module ${libraryName}**启动构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/o_8MUHWPRJe9HYdJXdEonQ/zh-cn_image_0000002561832835.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=3918D64C26BECB59B5A2D7D65914382AB70333D3B5B42B8CB06EBC58F291B1EF)

   构建完成后，build目录下生成HSP包产物，其中.tgz用来上传至私仓。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/AN0MP2ehTzCwD7ZHzpVqDA/zh-cn_image_0000002530752934.png?HW-CC-KV=V1&HW-CC-Date=20260429T054434Z&HW-CC-Expire=86400&HW-CC-Sign=1046A7924451A8B69C115407E9C81C7E1988490F30CF5B67553B8BD808A0D1F1)
