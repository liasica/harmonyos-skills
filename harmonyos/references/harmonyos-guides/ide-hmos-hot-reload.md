---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hot-reload
title: Hot Reload
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Hot Reload
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:ec1aa66f100992162e94a2e58d72c2e22ac2e7a40649a27481ecc29dbaea9f31
---

鸿蒙电脑DevEco Studio提供Hot Reload（热重载）能力，支持开发者在真机或多设备预览器上运行/调试应用时，修改代码并保存后无需重启应用，在真机或预览器上即可使用最新的代码，帮助开发者更快速地进行调试。

针对大多数代码修改场景，热重载均能提供支持，但是一些特殊场景需要通过热重载+重启应用后方可生效，因此，DevEco Studio提供基于热重载的增强能力——热重启。开启热重启开关后，DevEco Studio在遇到热重载不支持的场景时，将自动切换至热重启以获取更强的支持能力。

热重载和热重启均不支持C++文件和资源文件的修改，针对该问题，DevEco Studio提供基于热重启的增强能力——冷重载。开启冷重载开关后，并且设备版本在API 24及以上，DevEco Studio在增量调试C++代码及资源文件时，会自动切换至冷重载。

**说明** 

Hot Reload不支持卡片，不建议在hotReload模式下执行与卡片相关的操作。

## 热重载、热重启、完全重启的区别

* **热重载**：不重启应用，可保留应用状态，但整个过程会重新运行入口文件内的逻辑。
* **热重启**：在运行流程上，与热重载相比，主要区别在于会重启应用，不保留应用状态，支持更广泛的ArkTs代码修改快速生效。一旦执行了热重启，后续热重载流程均会被热重启取代。
* **完全重启**：会完全重新运行应用，该任务较为耗时，因为它会重新全量编译代码和资源文件。

## 使用约束

**表1** **表1** 热重载/热重启的修改文件支持范围

| 修改文件 | 热重载 | 热重启 | 说明 |
| --- | --- | --- | --- |
| 修改Entry入口模块内ets、ts代码文件 | 支持 | 支持 | - |
| 修改Entry直接或间接依赖的Har模块内代码文件 | 支持 | 支持 | Har模块与Entry模块间无Hsp |
| 修改Entry直接或间接依赖的Hsp模块内代码文件 | 不支持 | 不支持 | - |
| 引入的其他工程Har模块内代码文件 | 支持 | 支持 | Har模块与Entry模块间无Hsp |
| 引入的其他工程Hsp模块内代码文件 | 不支持 | 不支持 | - |
| 修改worker线程文件 | 不支持 | 不支持 | - |
| 修改模块目录下Index文件 | 支持 | 支持 | - |
| 启动应用后新增的代码文件 | 不支持 | 不支持 | - |
| C++、so文件 | 不支持 | 不支持 | - |
| resource资源文件（如修改string.json文件的内容） | 不支持 | 不支持 | 支持对资源引用的修改，例如把$r('app.color.greenColor')改成$r('app.color.redColor') |

**表2** 热重载/热重启的代码元素支持范围

| 代码元素 | 变更行为 | 热重载 | 热重启 | 说明 |
| --- | --- | --- | --- | --- |
| UI代码(如修改字号、颜色等) | 新增、修改、删除 | 支持 | 支持 | - |
| UI相应事件(如添加onClick事件等) | 新增、修改、删除 | 支持 | 支持 | - |
| import | 新增 | 部分支持 | 部分支持 | 不支持从启动应用时未加载的文件中import模块。 |
| 修改、删除 | 支持 | 支持 | - |
| 动态import  lazy import  napi\_load\_module  napi\_load\_module\_with\_info | 新增 | 部分支持 | 部分支持 | 不支持从启动应用时未加载的文件中import模块。 |
| 修改、删除 | 支持 | 支持 | - |
| export | 新增 | 部分支持 | 部分支持 | 新增export default语句时应同步在调用文件内新增对应import语句，否则将失败。 |
| 修改、删除 | 支持 | 支持 | - |
| 装饰器(@State、@Prop等) | 新增、修改、删除 | 部分支持 | 部分支持 | 热重载、热重启：@Entry修饰的文件支持@Styles新增、修改、删除  热重启：@Entry修饰的文件支持@State新增、修改和删除 |
| declare声明变量 | 新增、修改、删除 | 支持 | 支持 | - |
| Struct代码块 | 新增 | 部分支持 | 支持 | @Entry修饰的文件内不支持新增Struct代码块热重载，其他文件支持。 |
| 修改 | 部分支持 | 支持 | @Entry修饰的文件不支持成员变量、成员函数热重载，其他文件支持。 |
| 删除 | 支持 | 支持 | - |
| 类 | 新增 | 部分支持 | 支持 | @Entry修饰的文件内不支持新增包含成员函数的class，其他文件支持。 |
| 修改 | 部分支持 | 支持 | @Entry修饰的文件内class不支持新增成员函数，其他文件支持。 |
| 继承 | 部分支持 | 支持 | @Entry修饰的文件内不支持类继承及被继承场景，其他文件支持。 |
| 删除 | 支持 | 支持 | - |
| 接口 | 新增、删除 | 支持 | 支持 | - |
| 修改 | 部分支持 | 支持 | @Entry修饰的文件内不支持接口对象修改，其他文件支持。 |
| 枚举 | 新增、修改 | 部分支持 | 支持 | @Entry修饰的文件内不支持新增枚举，不支持修改枚举的键和值，其他文件支持。 |
| 删除 | 支持 | 支持 | - |
| 匿名函数 | 新增、修改、删除 | 支持 | 支持 | - |
| Lambda函数 | 新增、修改、删除 | 支持 | 支持 | - |
| 闭包函数 | 新增、修改、删除 | 支持 | 支持 | - |
| 闭包变量 | 新增、删除 | 部分支持 | 部分支持 | 热重载仅支持顶层闭包变量（不包括this变量）的新增或删除。  热重启不支持首次新增this变量或删除所有this变量。 |
| 修改 | 部分支持 | 支持 | 热重载不支持顶层闭包变量的修改 |
| 自定义组件 | 新增、修改、删除 | 部分支持 | 支持 | 热重载：@Entry修饰的文件内仅支持通过import方式引入的自定义组件的新增和修改。 |

**表3** **表3** 其他场景

| 场景 | 热重载 | 热重启 | 说明 |
| --- | --- | --- | --- |
| 命中断点时 | 不支持 | 不支持 | 点击Resume Program继续执行后再进行热重载/热重启 |
| 修改跳转的其他ability页面 | 不支持 | 支持 | 修改代码并执行热重载后，重新拉起该ability页面可生效 |

## 开启热重启/冷重载（可选）

如果需要使用热重启或冷重载的能力，先打开对应开关：点击菜单栏点击**文件 > 设置** **>** **扩展 > 热重载**，勾选以下选项。

* **启用热重启**：热加载并重启应用。
* **启用冷重****载**：增量构建并重启应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/IUnkXPpWTVOclXhrJ3wjqQ/zh-cn_image_0000002750169704.png)

## 操作步骤

1. 连接真机设备或多设备预览器。
2. 在下拉菜单中，将运行/调试配置切换为**Hot Reload**的配置![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/okaby55QS3qgOHi9pAIkJw/zh-cn_image_0000002750169708.png "点击放大")。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/YDUxW79sQhmRqZ97CZf1Yg/zh-cn_image_0000002750169706.png "点击放大")
3. 运行/调试应用，请参考[使用本地真机运行应用/元服务](ide-hmos-run-device.md)或[使用多设备预览器运行应用/元服务](ide-hmos-run-previewer.md)。
4. 修改代码后，可以通过如下操作，查看设备上修改后的显示效果。
   * 方式一：点击热重载![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/8EBy42PgQYy9oTCDQ7u4aA/zh-cn_image_0000002779608731.png)按钮：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/HEQXO8MGQriYlD9Fp9OTPg/zh-cn_image_0000002779728883.png)
   * 方式二：通过快捷键方式触发热重载：需要先在菜单栏点击**文件 > 设置** **>** **扩展 > 热重载**，勾选**保存时执行热重载**。修改代码后通过快捷键**Ctrl + S**或**失焦**即可触发热重载。

     方式二不支持冷重载，如需使用冷重载功能，请使用方式一。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/Ionq-4KVSF2PYFsknpzliA/zh-cn_image_0000002750169710.png)

   成功执行热重载后，控制台会打印以下内容：

   ```screen
   Performing hot reload...
   Syncing files to device xxx
   Reloaded 1 files in x s xxx ms.
   ```

   成功执行热重启后，控制台中会打印以下内容：

   ```screen
   Performing hot restart...
   $ hdc shell aa force-stop com.xx.xx
   Syncing files to device xxx
   Reloaded 1 files in x s xxx ms.
   $ hdc shell aa start -a EntryAbility -b com.xxx.xxx in xxx ms
   ```

   成功执行冷重载后，控制台中会打印以下内容：

   ```screen
   Performing apply change...
   $ hdc shell aa force-stop com.xx.xx
   Syncing files to device xxx
   Reloaded 1 files in x s xxx ms.
   $ hdc shell aa start -a EntryAbility -b com.xxx.xxx in xxx ms
   ```
5. 点击停止按钮终止运行/调试运行，退出Hot Reload模式。
