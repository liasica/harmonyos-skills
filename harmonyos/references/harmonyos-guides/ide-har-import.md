---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import
title: 引用及管理共享包
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布和管理共享包 > 引用及管理共享包
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:197a97ee34fca5cbf64f5d67fe1875ec97f13490014735ea1ad0c86186c93759
---

引用三方HAR/HSP包（以下简称三方包），包括从ohpm仓库进行安装、从本地文件夹和本地压缩包中进行安装三种方式。

* 引用ohpm仓中的三方包，首先需要设置三方包的仓库信息，DevEco Studio默认仓库地址为OpenHarmony三方库中心仓，如果您想设置自定义仓库，请在DevEco Studio的**Terminal**窗口执行如下命令进行设置：

  ```screen
  ohpm config set registry your_registry1,your_registry2
  ```

  说明：ohpm支持多个仓库地址，采用英文逗号分隔。

  支持通过如下方式配置三方包依赖信息：
  + 方式一：在菜单栏点击**Tools >** **OHPM Index**，进入DevEco Studio内置的OpenHarmony三方库中心仓，选择需要的三方包，详情请参考[使用OpenHarmony开源中心仓管理三方包](ide-har-import.md#section1579838153916)。仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
  + 方式二：在**Terminal**窗口中，切换到需要引入三方包的模块，如entry模块，执行如下命令安装三方包，DevEco Studio会自动在该模块的oh-package.json5中添加三方包依赖。

    ```screen
    cd path/to/your/project/entry
    ohpm install @ohos/lottie
    ```
  + 方式三：在需要引入三方包的模块的oh-package.json5中设置三方包依赖，配置示例如下：

    ```screen
    "dependencies": {
      "@ohos/lottie": "^2.0.0"
    }
    ```

    依赖设置完成后，需要执行**ohpm install**命令安装依赖包，依赖包会安装到该模块的oh\_modules目录下。

    ```screen
    ohpm install
    ```
* 引用本地模块源码（该本地模块必须与宿主模块归属于同一个工程），如entry模块需要依赖foo模块的源码，有如下两种方式：
  + 方式一：在**Terminal**窗口中，切换到需要引入本地模块源码的模块，即entry模块下，执行如下命令进行安装，并会在该模块下的oh-package.json5中自动添加依赖。

    ```screen
    cd path/to/your/project/entry
    ohpm install path/to/foo
    ```
  + 方式二：在需要引入本地模块源码的模块的oh-package.json5中设置源码依赖项，即entry模块的oh-package.json5中，添加如下配置：

    ```screen
    "dependencies": {
      "foo": "file:path/to/foo"  // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
    }
    ```

    依赖设置完成后，需要执行**ohpm install**命令安装依赖包，模块foo的源码会安装在entry模块的oh\_modules目录下。

    ```screen
    ohpm install
    ```

* 引用本地三方包，有如下两种方式：
  + 方式一：在**Terminal**窗口中，切换到需要引入本地HAR/HSP包的模块，如entry模块，执行如下命令进行安装，并会在oh-package.json5中自动添加依赖。以HAR/HSP包在工程根目录下为例，配置示例如下（实际配置时请以HAR/HSP包实际目录为准）：
    - 引用HAR：

      ```screen
      cd path/to/your/project/entry
      ohpm install path/to/package.har
      ```
    - 引用HSP（\*.tgz包通过HSP模块在release模式下[编译](ide-hsp.md#section1833373964217)生成）：

      ```screen
      cd path/to/your/project/entry
      ohpm install path/to/package.tgz
      ```
  + 方式二：在需要引入三方包的模块的oh-package.json5中设置本地HAR/HSP包。以HAR/HSP包在工程根目录下为例，配置示例如下（实际配置时请以HAR/HSP包实际目录为准）：
    - 引用HAR：

      ```screen
      "dependencies": {
        "package": "file:path/to/package.har" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径。 
      }
      ```

      **说明** 

      代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。
    - 引用HSP：

      ```screen
      "dependencies": {
        "package": "file:path/to/package.tgz" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
      }
      ```

依赖设置完成后，需要执行**ohpm install**命令安装依赖包，依赖包会安装在该模块的oh\_modules目录下。

```screen
ohpm install
```

另外，在安装或卸载共享包时，可在模块或工程的oh-package.json5文件中增加钩子设置，以管理install、uninstall命令的生命周期，配置示例如下：

```screen
 "hooks": {
    "preInstall": "echo 00 preInstall", // install命令执行之前
    "postInstall": "echo 00 postInstall", // install命令执行之后
    "preUninstall": "echo 00 preUninstall", // uninstall命令执行之前
    "postUninstall": "echo 00 postUninstall"  // uninstall命令执行之后
  }
```

**说明** 

* 目前只支持执行当前模块或工程的oh-package.json5文件中hooks，不支持执行依赖中hooks。
* 在引用共享包时，请注意当前只支持在模块和工程下的oh-package.json5文件中声明dependencies依赖，才会被当做依赖使用，并在编译构建过程中进行相应的处理。

## 使用OpenHarmony三方库中心仓管理三方包

**说明** 

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

从DevEco Studio 6.0.0 Beta5版本开始，新增OHPM Index入口，提供OpenHarmony三方库中心仓的高效筛选和管理能力，提升开发者选型开发效率，消减因软件信息不对称导致的选型使用风险，快速选择与定位所需的开源三方库。

1. 在菜单栏点击**Tools >** **OHPM Index**，进入OpenHarmony三方库中心仓。
2. 在左侧搜索框可查询三方包名称，或点击目录树，根据分类查看不同分类下推荐的依赖包信息。选定所需要安装的三方包，点击右上角蓝色按钮**Install**进行安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/HFvCaPpsQbahKTOm8ylskA/zh-cn_image_0000002731542135.png)
3. 安装过程中，如出现下方弹窗，点击**Add**按钮，将OpenHarmony三方库中心仓地址添加到.ohpmrc文件中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/fV9Zr0bJTO62xInOOYBuZA/zh-cn_image_0000002701822866.png)
4. 三方包安装完成后，在工程级oh-package.json5文件中可以看到已安装的三方包名称及版本信息，oh\_modules中将同时添加该三方包。
5. 点击页面左上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/55uZEULHRoib8_IfaJJCtQ/zh-cn_image_0000002701822862.png "点击放大")图标，展示当前已安装的三方包信息。若当前三方包非最新版本，可以点击右上角**Update**按钮，更新至最新版本；点击**Delete**按钮，可以删除当前已安装的三方包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/6YyrZY3MR9qh1X1kUe5pdQ/zh-cn_image_0000002731542139.png)
6. 若对于已使用的三方包依赖存在推荐的同类三方包，可点击编辑界面中黄色灯泡图标，在弹框中选择**Replace selected with recommended library**，将当前依赖替换为推荐的三方包依赖；或选择**Replace all with recommended libraries**，一键替换当前文件中所有同类推荐三方包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ksKSxa_TTQ2uo2yWg5ooVg/zh-cn_image_0000002731542137.png)
