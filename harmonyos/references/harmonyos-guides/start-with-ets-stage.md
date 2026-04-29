---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-with-ets-stage
title: 构建第一个HarmonyOS应用（ArkTS）
breadcrumb: 指南 > 基础入门 > 快速入门 > 构建第一个HarmonyOS应用（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:27+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7637910a4a6277d929e6d3e2d74473d69a8f3bc9d2482b986e414edcdc5565b1
---

说明

为确保运行效果，本文以使用[DevEco Studio 6.1.0 Release版本](https://developer.huawei.com/consumer/cn/download/)为例。

## 创建ArkTS工程

1. 若首次打开**DevEco Studio**，请单击**Create Project**创建工程。如果已经打开了一个工程，请在菜单栏选择**File** > **New** > **Create Project**来创建一个新工程。
2. 选择**Application**应用开发（本文以应用开发为例，[Atomic Service](glossary.md#section10825114113817)对应为元服务开发），选择模板**Empty Ability**，单击**Next**进行下一步配置。

   若开发者需要进行Native相关工程的开发，请选择**Native C++** 模板，更多模板的使用和说明请见[工程模板介绍](ide-template.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/AM-GY5m5Qp2v2cpl_aH7BQ/zh-cn_image_0000002558763960.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=394026DF6301C2DFA737BF6C6A23E67A2F23F958C1EC2151937CC73E540CE3EA)
3. 进入配置工程界面，**Compatible SDK**表示兼容的最低API Version，此处以选择**6.1.0(23)** 为例，其他参数保持默认设置即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/5lfvP650RvSN0ozhYqhwhg/zh-cn_image_0000002558604304.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=871C42013819EA9D3B185FBAE76C9BF888E1BE57E32A93B0FBB60FBB4A2E0A4A)
4. 单击**Finish**，工具会自动生成示例代码和相关资源，等待工程创建完成。

## ArkTS工程目录结构（Stage模型）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/xey6Vf5YQwyu60MKGbojOg/zh-cn_image_0000002589323829.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=D24B20559C1E7D17886723086DD1E79E783770F8FD5BBB0AD3B4C0832891A8AD)

* **AppScope > app.json5**：应用的全局配置信息，详见[app.json5配置文件](app-configuration-file.md)。
* **entry**：HarmonyOS工程模块，编译构建生成一个[HAP](application-package-glossary.md#hap)包。

  + **src > main > ets**：用于存放ArkTS源码。
  + **src > main > ets > entryability**：应用/服务的入口。
  + **src > main > ets > entrybackupability**：应用提供扩展的备份恢复能力。
  + **src > main > ets > pages**：应用/服务包含的页面。
  + **src > main > resources**：用于存放应用/服务所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件，详见[资源分类与访问](resource-categories-and-access.md)。
  + **src > main > module.json5**：[模块](application-package-glossary.md#module)配置文件。主要包含HAP包的配置信息、应用/服务在具体设备上的配置信息以及应用/服务的全局配置信息。具体的配置文件说明，详见[module.json5配置文件](module-configuration-file.md)。
  + **build-profile.json5**：当前的模块信息 、编译信息配置项，包括buildOption、targets配置等。
  + **hvigorfile.ts**：模块级编译构建任务脚本。
  + **obfuscation-rules.txt**：混淆规则文件。混淆开启后，在使用Release模式进行编译时，会对代码进行编译、混淆及压缩处理，保护代码资产。详见[开启代码混淆](ide-build-obfuscation.md)。
  + **oh-package.json5**：用来描述包名、版本、入口文件（类型声明文件）和依赖项等信息。
* **oh\_modules**：用于存放三方库依赖信息。
* **build-profile.json5**：工程级配置信息，包括签名signingConfigs、产品配置products等。其中products中可配置当前运行环境，默认为HarmonyOS。
* **hvigorfile.ts**：工程级编译构建任务脚本。
* **oh-package.json5**：主要用来描述全局配置，如：依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等。

## 构建第一个页面

1. 使用文本组件。

   工程同步完成后，在**Project**窗口，单击**entry > src > main > ets > pages**，打开**Index.ets**文件，将页面从RelativeContainer相对布局修改成Row/Column线性布局。

   针对本文中使用文本/按钮来实现页面跳转/返回的应用场景，页面均使用[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)组件来组建布局。对于更多复杂元素对齐的场景，可选择使用[RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)组件进行布局。更多关于UI布局的选择和使用，可见[如何选择布局](arkts-layout-development-overview.md#如何选择布局)。

   **Index.ets**文件的示例如下：

   ```
   1. // Index.ets
   2. @Entry
   3. @Component
   4. struct Index {
   5. @State message: string = 'Hello World';

   7. build() {
   8. Row() {
   9. Column() {
   10. Text(this.message)
   11. .fontSize(50)
   12. .fontWeight(FontWeight.Bold)
   13. }
   14. .width('100%')
   15. }
   16. .height('100%')
   17. }
   18. }
   ```
2. 添加按钮。

   在默认页面基础上，我们添加一个Button组件，作为按钮响应用户onClick事件，从而实现跳转到另一个页面。**Index.ets**文件的示例如下：

   ```
   1. // Index.ets
   2. @Entry
   3. @Component
   4. struct Index {
   5. @State message: string = 'Hello World';

   7. build() {
   8. Row() {
   9. Column() {
   10. Text(this.message)
   11. .fontSize(50)
   12. .fontWeight(FontWeight.Bold)
   13. // 添加按钮，以响应用户onClick事件
   14. Button() {
   15. Text('Next')
   16. .fontSize(30)
   17. .fontWeight(FontWeight.Bold)
   18. }
   19. .type(ButtonType.Capsule)
   20. .margin({
   21. top: 20
   22. })
   23. .backgroundColor('#0D9FFB')
   24. .width('40%')
   25. .height('5%')
   26. }
   27. .width('100%')
   28. }
   29. .height('100%')
   30. }
   31. }
   ```
3. 在编辑窗口**右上角**的侧边工具栏，单击**Previewer**，打开预览器。第一个页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/KGoB4YyMS-KpvSOEGTJYHQ/zh-cn_image_0000002589243767.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=E581DE8A3F1822692E8714DF5305EBE79B1BD418D367EA7DE0DDE380C54F5CBD)

## 构建第二个页面

1. 创建第二个页面。

   * 新建第二个页面文件。在**Project**窗口，打开**entry > src > main > ets**，右键单击**pages**文件夹，选择**New > ArkTS File**，命名为**Second**，单击**回车键**。可以看到文件目录结构如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/ugjH5nJZTbeh_z_p1ketlg/zh-cn_image_0000002558763962.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=3230ADF00BEC3E3D9C9C17557F971B6C9F509D5D0289B119255F129165675938)

     说明

     开发者也可以在右键单击**pages**文件夹时，选择**New > Page** **> Empty Page**，命名为**Second**，单击**Finish**完成第二个页面的创建。使用此种方式则无需再进行下文中第二个页面路由的手动配置。
   * 配置第二个页面的路由。在**Project**窗口，打开**entry > src > main > resources > base > profile**，在main\_pages.json文件中的"src"下配置第二个页面的路由"pages/Second"。示例如下：

     ```
     1. {
     2. "src": [
     3. "pages/Index",
     4. "pages/Second"
     5. ]
     6. }
     ```
2. 添加文本及按钮。

   参照第一个页面，在第二个页面添加Text组件、Button组件等，并设置其样式。**Second.ets**文件的示例如下：

   ```
   1. // Second.ets
   2. @Entry
   3. @Component
   4. struct Second {
   5. @State message: string = 'Hi there';

   7. build() {
   8. Row() {
   9. Column() {
   10. Text(this.message)
   11. .fontSize(50)
   12. .fontWeight(FontWeight.Bold)
   13. Button() {
   14. Text('Back')
   15. .fontSize(30)
   16. .fontWeight(FontWeight.Bold)
   17. }
   18. .type(ButtonType.Capsule)
   19. .margin({
   20. top: 20
   21. })
   22. .backgroundColor('#0D9FFB')
   23. .width('40%')
   24. .height('5%')
   25. }
   26. .width('100%')
   27. }
   28. .height('100%')
   29. }
   30. }
   ```

## 实现页面间的跳转

页面间的导航可以通过[页面路由router](../harmonyos-references/arkts-apis-uicontext-router.md)来实现。页面路由router根据页面url找到目标页面，从而实现跳转。

如果需要实现更好的转场动效，推荐使用[Navigation](arkts-navigation-navigation.md)。

1. 第一个页面跳转到第二个页面。

   在第一个页面中，跳转按钮绑定onClick事件，单击按钮时跳转到第二页。**Index.ets**文件的示例如下：

   ```
   1. // Index.ets
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'Hello World';

   9. build() {
   10. Row() {
   11. Column() {
   12. Text(this.message)
   13. .fontSize(50)
   14. .fontWeight(FontWeight.Bold)
   15. // 添加按钮，以响应用户onClick事件
   16. Button() {
   17. Text('Next')
   18. .fontSize(30)
   19. .fontWeight(FontWeight.Bold)
   20. }
   21. .type(ButtonType.Capsule)
   22. .margin({
   23. top: 20
   24. })
   25. .backgroundColor('#0D9FFB')
   26. .width('40%')
   27. .height('5%')
   28. // 跳转按钮绑定onClick事件，单击时跳转到第二页
   29. .onClick(() => {
   30. console.info(`Succeeded in clicking the 'Next' button.`)
   31. // 获取UIContext
   32. let uiContext: UIContext = this.getUIContext();
   33. let router = uiContext.getRouter();
   34. // 跳转到第二页
   35. router.pushUrl({ url: 'pages/Second' }).then(() => {
   36. console.info('Succeeded in jumping to the second page.')

   38. }).catch((err: BusinessError) => {
   39. console.error(`Failed to jump to the second page. Code is ${err.code}, message is ${err.message}`)
   40. })
   41. })
   42. }
   43. .width('100%')
   44. }
   45. .height('100%')
   46. }
   47. }
   ```
2. 第二个页面返回到第一个页面。

   在第二个页面中，返回按钮绑定onClick事件，单击按钮时返回到第一页。**Second.ets**文件的示例如下：

   ```
   1. // Second.ets
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. @Entry
   5. @Component
   6. struct Second {
   7. @State message: string = 'Hi there';

   9. build() {
   10. Row() {
   11. Column() {
   12. Text(this.message)
   13. .fontSize(50)
   14. .fontWeight(FontWeight.Bold)
   15. Button() {
   16. Text('Back')
   17. .fontSize(30)
   18. .fontWeight(FontWeight.Bold)
   19. }
   20. .type(ButtonType.Capsule)
   21. .margin({
   22. top: 20
   23. })
   24. .backgroundColor('#0D9FFB')
   25. .width('40%')
   26. .height('5%')
   27. // 返回按钮绑定onClick事件，单击按钮时返回到第一页
   28. .onClick(() => {
   29. console.info(`Succeeded in clicking the 'Back' button.`)
   30. // 获取UIContext
   31. let uiContext: UIContext = this.getUIContext();
   32. let router = uiContext.getRouter();
   33. try {
   34. // 返回第一页
   35. router.back()
   36. console.info('Succeeded in returning to the first page.')
   37. } catch (err) {
   38. let code = (err as BusinessError).code;
   39. let message = (err as BusinessError).message;
   40. console.error(`Failed to return to the first page. Code is ${code}, message is ${message}`)
   41. }
   42. })
   43. }
   44. .width('100%')
   45. }
   46. .height('100%')
   47. }
   48. }
   ```
3. 打开**Index.ets**文件，单击预览器中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/eMZKaBjERyK5Z8bw8VAQ0Q/zh-cn_image_0000002558604306.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=C361D33E1134B78CF0F6A6FE7191438F0425A82CDF406BFFFFFC9B81BC4901CF)按钮进行刷新。效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/i8vuQvQvRw-wqVeI4PBQAg/zh-cn_image_0000002589323831.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=C85EEDD9DD8C6A1C7B24639EDCF25ABC0747363BC4A2394C6F38956F0FA91BD8)

## 使用真机运行应用

1. 将搭载HarmonyOS系统的真机与电脑连接。具体指导及要求，可查看[使用本地真机运行应用/服务](ide-run-device.md)。
2. 进入**File > Project Structure... > Project > Signing Configs**界面，勾选“**Automatically generate signature**”，即可完成签名。如果未登录，请先单击**Sign In**进行登录，然后自动完成签名。具体请见[配置调试签名](ide-signing.md#section151231211105010)。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Msdqi8qNTH-uG7HHSo6fcA/zh-cn_image_0000002589243769.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=E2D38F1B19A11BFFCF88F50C02F6119540C65A775E97AF129B0268C46FE35EE4)
3. 在编辑窗口右上角的工具栏，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/OubFx_fMTbavz-7K5Ju6xA/zh-cn_image_0000002558763964.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=1AC4FC9ACE963107DE9E51186D15CB20BB19D88F7F6E745A4EE566D7D5BCA82C)按钮运行。效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/r4GJxBoCSRquVsTvRDoknQ/zh-cn_image_0000002558604308.png?HW-CC-KV=V1&HW-CC-Date=20260429T052227Z&HW-CC-Expire=86400&HW-CC-Sign=CA48A945F13B40526B75AF74234E3110BB03084802494BA31D95FA9AAB95E245)

恭喜您已经基于ArkTS语言构建完成第一个HarmonyOS应用，快来探索更多的HarmonyOS功能吧。
