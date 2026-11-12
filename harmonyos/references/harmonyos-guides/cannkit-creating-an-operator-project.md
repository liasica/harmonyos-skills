---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-creating-an-operator-project
title: AscendC算子工程创建
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子实现 > AscendC算子工程开发 > AscendC算子工程创建
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5d9d074213a3cb7375f059c86d44bc678e2cf20ef89fcf71939c6e3a8bde9172
---

开发者可以基于鸿蒙CANN社区recipe仓提供的工程模板创建算子开发工程，工程中包括**算子host侧代码实现文件**、**算子kernel侧实现文件**以及**工程编译配置文件等**。

**简要说明：**

创建算子工程之前，需要参考[环境准备](cannkit-environment-preparation.md)章节安装驱动固件和CANN软件包，完成开发环境和运行环境的准备。

同时需要配置CANN工具包环境变量，示例如下。

```shell
source ${install_path}/cann-${cann_version}/set_env.sh
```

创建算子开发工程的步骤如下。

1. 获取工程模板。

   从[鸿蒙CANN社区recipe仓](https://gitcode.com/cann/cann-recipes-harmony-infer/blob/master/README.md)获取算子工程模板，将仓内的样例单算子工程（如AddCustom算子，位于仓内"ops/ascendc/src/add\_custom"目录下）拷贝到本地作为算子开发工程。

   ```shell
   git clone https://gitcode.com/cann/cann-recipes-harmony-infer.git
   cp -r ./cann-recipes-harmony-infer/ops/ascendc/src/add_custom ./AddCustom
   ```

   **说明** 

   鸿蒙CANN社区recipe仓的更多介绍请参见[仓工程模板说明](https://gitcode.com/cann/cann-recipes-harmony-infer/blob/master/README.md)。
2. 以AddCustom算子为例，拷贝得到的算子工程目录结构如下所示：

   ```text
   AddCustom
   ├── CMakeLists.txt // 算子工程的CMakeLists.txt
   ├── CMakePresets.json // 编译配置项
   ├── framework // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
   ├── op_host // host侧实现文件
   │   ├── **add_custom_tiling.h** // 算子tiling定义文件
   │   ├── **add_custom.cpp** // 算子原型注册、shape推导、信息库、tiling实现等内容文件
   │   ├── CMakeLists.txt
   ├── op_kernel // kernel侧实现文件
   │   ├── CMakeLists.txt
   │   ├── **add_custom.cpp** // 算子代码实现文件
   └── scripts // 自定义算子工程打包相关脚本所在目录
   ```

   **说明** 

   * 上述目录结构中的粗体文件为后续算子开发过程中需要修改的文件，其他文件无需修改。样例工程的实际目录结构以仓内工程为准。
   * 开发其他算子时，建议在样例工程基础上同步调整工程名、文件名以及算子名，使工程命名与算子保持一致，从而得到新算子的开发工程。

工程目录中的op\_kernel和op\_host包含了算子的核心实现文件。op\_kernel下存放[Kernel侧算子实现](cannkit-operator-implementation-on-the.md)。op\_host下存放host侧代码实现，包括[算子原型定义实现](cannkit-operator-prototype-definition.md)、[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)。其中kernel侧算子实现和host侧tiling实现在[算子实现](cannkit-operator-implementation-overview.md)章节已经介绍了其核心的实现方法，在该章节会侧重于介绍接入DDK框架后的编程模式和API的使用。工程目录中的CMakePresets.json，用于开发者完成工程编译相关配置，之后即可进行编译部署。
