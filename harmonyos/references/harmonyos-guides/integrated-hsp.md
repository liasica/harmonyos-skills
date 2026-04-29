---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/integrated-hsp
title: 集成态HSP
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 集成态HSP
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb7050a4db44f2c4099c42666ee1cfab9f96c6ef3e5b1125d5bbc9a9d1a81d0d
---

集成态HSP是应用内HSP的中间编译产物，用于解决使用方的bundleName和签名之间的强耦合问题。

说明

HSP只能给bundleName一样的工程使用，集成态HSP可以给不同的bundleName的工程集成使用。

使用方使用集成态HSP时，需要采用使用方的签名文件对集成态HSP重新签名，且需要优先安装重新签名后的集成态HSP。

## 使用场景

如果存在多个应用包含相同的基础能力，例如日志打印模块，为节约开发成本并实现代码和资源的共享，多个应用可以共用一个日志模块。此时，可以通过应用内HSP方式提供能力。由于应用内HSP的限制，每个应用在使用前都需要调整其bundleName，并使用当前应用的签名重新签名，构建一个新的HSP提供给当前应用使用。这意味着，每增加一个应用，就需要进行一次调整bundleName和重新签名的操作，导致签名和打包过程繁琐。

而集成态HSP在DevEco Studio编译过程中，bundleName和重签名的动作会自动完成，开发者无需关注重复签名的操作，可以专注于功能业务的开发。

## 约束限制

* 集成态HSP只支持[Stage模型](application-package-structure-stage.md)。
* 从API version 12开始，支持使用集成态HSP。
* 使用集成态HSP要求使用标准化的OHMUrl格式。需要在工程级的[build-profile.json5文件](ide-hvigor-build-profile-app.md)中，将[strictMode](ide-hvigor-build-profile-app.md#section13181758123312)下的useNormalizedOHMUrl字段设置为true。

## 开发使用说明

### 配置集成态HSP

1. 工程配置：配置工程级的build-profile.json5文件，将useNormalizedOHMUrl字段设置为true。

   ```
   1. {
   2. "app": {
   3. "signingConfigs": [
   4. ],
   5. "products": [
   6. {
   7. "name": "default",
   8. "signingConfig": "default",
   9. "targetSdkVersion": "5.1.1(19)",
   10. "compatibleSdkVersion": "5.1.1(19)",
   11. "runtimeOS": "HarmonyOS",
   12. "buildOption": {
   13. "strictMode": {
   14. // ...
   15. "useNormalizedOHMUrl": true,
   16. }
   17. }
   18. }
   19. ],
   20. // ...
   21. },
   22. // ...
   23. }
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/IntegratedHsp/build-profile.json5#L15-L77)
2. 模块配置：修改模块级构建配置文件[build-profile.json5](ide-hvigor-build-profile.md)，将integratedHsp配置项设置为true，指定构建的HSP模块为集成态HSP。

   ```
   1. // library/build-profile.json5
   2. {
   3. "apiType": "stageMode",
   4. // ...
   5. "buildOptionSet": [
   6. {
   7. // ...
   8. "arkOptions": {
   9. "integratedHsp": true,
   10. // ...
   11. },
   12. },
   13. ],
   14. // ...
   15. }
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/IntegratedHsp/library/build-profile.json5#L15-L57)
3. 打包配置（tgz包）。

   (1) 配置项目签名信息，详情请参见[应用/元服务签名](ide-signing.md)。

   (2) 配置release模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/cWsfBdbcTDup7ja5H7JYGw/zh-cn_image_0000002558763972.png?HW-CC-KV=V1&HW-CC-Date=20260429T052534Z&HW-CC-Expire=86400&HW-CC-Sign=A1D4C6158ACE5DC19570E97EBA25642E4CEE0FC957C2A08910A89F313D01783F)

   (3) 选择library目录，执行Build -> Make Module 'library'。

### 使用方集成

1. 创建目录并拷贝文件：在entry目录下新建libs目录，将集成态打包产物tgz包拷贝到libs目录下。
2. 工程依赖配置：在使用方主模块的oh-package.json5配置文件中添加依赖。

   ```
   1. "dependencies": {
   2. "library": "file:./libs/library-default.tgz"
   3. },
   ```

   [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/IntegratedHsp/entry/oh-package.json5#L23-L27)
3. 工程配置：在工程级的build-profile.json5文件中，将useNormalizedOHMUrl字段设置为true。

   ```
   1. {
   2. "app": {
   3. "signingConfigs": [
   4. ],
   5. "products": [
   6. {
   7. "name": "default",
   8. "signingConfig": "default",
   9. "targetSdkVersion": "5.1.1(19)",
   10. "compatibleSdkVersion": "5.1.1(19)",
   11. "runtimeOS": "HarmonyOS",
   12. "buildOption": {
   13. "strictMode": {
   14. // ...
   15. "useNormalizedOHMUrl": true,
   16. }
   17. }
   18. }
   19. ],
   20. // ...
   21. },
   22. // ...
   23. }
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/IntegratedHsp/build-profile.json5#L15-L77)
4. 配置签名。

   安装和运行应用前，必须配置项目签名信息，详见[应用/元服务签名](ide-signing.md)。
5. [安装和运行](ide-run-device.md)。
