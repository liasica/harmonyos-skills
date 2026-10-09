---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-har-import
title: 引用及管理共享包
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 开发环境搭建 > 工程创建 > 模块管理 > 开发发布与管理共享包 > 引用及管理共享包
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1b46ad39bbc372f6e10b598699023d435c81fbfb4f937b21b96a8053a5dd125a
---

引用三方HAR/HSP包（以下简称三方包），包括从ohpm仓库进行安装、从本地文件夹和本地压缩包中进行安装三种方式。

* 引用ohpm仓中的三方包，首先需要设置三方包的仓库信息，鸿蒙电脑DevEco Studio默认仓库地址为OpenHarmony三方库中心仓，如果您想设置自定义仓库，请在DevEco Studio的**Terminal**窗口执行如下命令进行设置（执行命令前，请确保已将ohpm配置到环境变量中，第一次配置环境变量后，需重启DevEco Studio）：

  ```screen
  ohpm config set registry your_registry1,your_registry2
  ```

  说明：ohpm支持多个仓库地址，采用英文逗号分隔。

  然后通过如下两种方式设置三方包依赖信息：
  + 方式一：在**Terminal**窗口中，切换到需要引入三方包的模块，如entry模块，执行如下命令安装三方包，DevEco Studio会自动在该模块的oh-package.json5中自动添加三方包依赖。

    ```screen
    cd path/to/your/project/entry
    ohpm install @ohos/lottie
    ```
  + 方式二：在需要引入三方包的模块的oh-package.json5中设置三方包依赖，配置示例如下：

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
      "foo": "file:path/to/foo" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
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
    - 引用HSP（\*.tgz包通过HSP模块在release模式下[编译](ide-hmos-hsp.md#section74681342185216)生成）：

      ```screen
      cd path/to/your/project/entry
      ohpm install path/to/package.tgz
      ```
  + 方式二：在需要引入三方包的模块的oh-package.json5中设置本地HAR/HSP包。以HAR/HSP包在工程根目录下为例，配置示例如下（实际配置时请以HAR/HSP包实际目录为准）：
    - 引用HAR：

      ```screen
      "dependencies": {
        "package": "file:path/to/package.har" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
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
