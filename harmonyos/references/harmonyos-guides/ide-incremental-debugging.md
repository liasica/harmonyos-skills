---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-incremental-debugging
title: 增量调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 增量调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6cc33e492f97f3248a2611d385dd66834d5f1c9e93bab991a852310f4b3b83da
---

对于大型应用来说，每次修改代码后需要重新构建、推包、安装，整个流程耗时较长。针对该场景，在DevEco Studio和命令行场景中分别提供增量运行调试功能，支持开发者在真机上调试应用时，修改代码后，会识别出代码差异，构建增量包，增量运行调试时只推送增量包，减少大型应用调试推包时间。

说明

C++代码增量调试支持API Version 11及以上版本Stage模型的工程；ArkTS代码增量调试仅支持API Version 12及以上版本Stage模型工程的资源文件修改。

## 使用DevEco Studio增量调试

### 调试C++代码

1. 在工具栏中，选择调试的设备，并单击**Run**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/E-qzKXGSRPCSOcGX2YknLg/zh-cn_image_0000002561833247.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=BBC48103297430193BAC5751E799E8EBE7265D906620900609C64389A1D3D4B5)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/OCimhXtpTniqAyPO0fMOPQ/zh-cn_image_0000002530753334.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=2A78329D27B663886CD6106DF9A04691BD3E50A6ED44F326143D03CF1C06FAC0)启动工程。
2. 在修改完代码后，点击**Apply Changes**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/QrQ-ImUASfaxyPykpKNwUg/zh-cn_image_0000002530913316.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=5CCB6EDD2E15BAC2AD996FC03420033BFF60C0F89EC07DF283BDE1907FAF03F2)推送增量包安装至设备。

   点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/3RhHer1gTFSagMVpj0XFBg/zh-cn_image_0000002561753255.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=B287669374AA0FB8E678DD7CEED4987E8D8513E940783903B16D25457C35ECB0)

   说明

   当前增量运行Apply Changes功能，不支持新建和删除代码文件，不支持修改装饰器相关的代码，不支持在代码中使用import新增引用文件。

### 调试rawfile/resfile资源

从DevEco Studio 5.1.0 Release版本开始支持增量调试rawfile资源。

1. 在工具栏中，选择调试的设备，并单击**Run**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/AwJILa3kQpuFIq-a6Xl6Ew/zh-cn_image_0000002561833249.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=FE8183210C3150D101BC62EB5DEC7B7261779DC99BE1473C03644F3A29C71B7D)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/jywkYIgESUi2mtmYlWb_8g/zh-cn_image_0000002561833255.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=3DABAB8C9CBC40CDAA4ECE0AE0E191AB327B917E2C1904DBBC00B4B6ED336597)启动工程。
2. 在工程的资源resources文件目录下的resfile或rawfile目录下，新增或者修改资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/0DQRMTOrR92dgsMVSNx4XQ/zh-cn_image_0000002530913330.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=54B5B68185F48D44502CCF265A23026182E35A6313BE690D9605CE7B8BA63EB1)

   说明

   当前对rawfile/resfile资源的增量调试，仅支持代码中直接调用的资源文件。
3. 点击**Apply Changes**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/hAUfH7cvQOah3lyVZXFCkQ/zh-cn_image_0000002530753324.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=76ADE74B6C10F1B4D1E863D3C6EC694C6F10950CE7F798B3676E9994D8AF38FA)推送增量包安装至设备。

   点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。

## 使用命令行增量调试

### 通过hvigorw构建hqf包

1. 检查待运行模块和依赖模块下是否存在build/config/buildConfig.json文件，如果不存在，先通过DevEco Studio全量运行工程，生成该文件。

   说明

   如果已执行步骤1，则步骤2和3无需再执行。
2. 根据运行所需的模块，及模块的product、target，编写命令行执行HAP/HSP编译任务，如entry模块依赖HSP模块library：

   ```
   1. hvigorw --mode module -p module=entry@default,library@default -p product=default assembleHap assembleHsp --info --no-daemon
   ```

   关于命令行的使用指导请参考[hvigorw](ide-hvigor-commandline.md)。
3. 执行hdc命令安装HAP、HSP，关于hdc工具的使用指导请参考[hdc](hdc.md)。

   ```
   1. $ hdc shell mkdir data/local/tmp/99c24fdc44694c05be12491d0a48e139
   2. $ hdc file send library-default-signed.hsp "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
   3. $ hdc file send entry-default-signed.hap "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
   4. $ hdc shell bm install -p "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
   5. $ hdc shell rm -rf data/local/tmp/99c24fdc44694c05be12491d0a48e139
   6. $ hdc shell aa start -a {abilityName} -b {bundleName}
   ```

   * abilityName：应用的ability名称。
   * bundleName：应用包名。
4. 如果修改了HAP/HSP模块的rawfile或resfile目录下的资源文件，则需要在对应模块的build/default/intermediates/patch/default目录下新建changedFileList.json并写入修改的文件；如果修改了HAR模块的资源文件，则需要在依赖该HAR的模块下写入修改的文件，示例如下。

   ```
   1. {
   2. "resources": {
   3. "resFile": [
   4. {
   5. "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
   6. "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
   7. }
   8. ],
   9. "rawFile": [
   10. {
   11. "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
   12. "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
   13. }
   14. ]
   15. }
   16. }
   ```
5. 修改C++代码后，执行hqf打包命令，执行完成后可在entry和library模块的输出目录build/default/outputs/default中，找到对应的产物entry-default-signed.hqf和library-default-signed.hqf。

   ```
   1. hvigorw --mode module -p module=entry@default,library@default -p product=default assembleDevHqf --info --no-daemon
   ```
6. 执行hdc命令安装hqf。

   ```
   1. $ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
   2. $ hdc file send library-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
   3. $ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
   4. $ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
   ```

### 通过SDK工具构建hqf包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qc9Ecdm9SkCPMbces4lGHQ/zh-cn_image_0000002530913312.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=0941BF73A50D9DCEC1C49E927B7871DFCDBB810E511BA9290E7D4CF24757ED3C "点击放大")

1. 全量编译应用并安装到设备。

   ```
   1. hdc bm install {hap_path} // 安装包在电脑上，使用该命令，hap_path是安装包路径
   2. hdc shell bm install -p {hap_path}  // 安装包在设备上，使用该命令
   ```
2. 开发者通过独立的构建流程，识别出希望构建增量hqf包的so，根据ABI编译环境（可查看build-profile.json5的[abiFilters](ide-hvigor-cpp.md#section0721057575)字段），汇总到某一目录下，例如汇总在change\_test目录下，编译环境是arm64-v8a，示例如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/SG3-1SpXTXGTqIokTurhNw/zh-cn_image_0000002530753326.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=59A93D6DD51EB9F2C24EDF68B8D20E9CCA908B618A9BFCC9E69446DC084A23CD)
3. （可选）进行资源文件修改。如果修改了HAP/HSP模块的rawfile或resfile目录下的资源文件，则需要在对应模块的build/default/intermediates/patch/default目录下新建changedFileList.json并写入修改的文件；如果修改了HAR模块的资源文件，则需要在依赖该HAR的模块下写入修改的文件，示例如下。

   ```
   1. {
   2. "resources": {
   3. "resFile": [
   4. {
   5. "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
   6. "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
   7. }
   8. ],
   9. "rawFile": [
   10. {
   11. "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
   12. "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
   13. }
   14. ]
   15. }
   16. }
   ```
4. 提前准备与已安装应用一致的签名文件。

   可以从工程的build-profile.json5文件中获取到对应的签名文件。
5. 准备patch.json文件，示例如下。

   ```
   1. {
   2. "app" : {
   3. "bundleName" : "com.ohos.quickfix",
   4. "versionCode" : 1000000, // 应用版本号
   5. "versionName" : "1.0.0",
   6. "patchVersionCode" : 1000000, // 补丁版本号，在每次进行增量调试前，将版本号+1，确保此次增量调试补丁包版本号大于上次增量调试补丁包版本号
   7. "patchVersionName" : "1000000"  // 与补丁版本号保持一致
   8. },
   9. "module" : {
   10. "name" : "entry",
   11. "type" : "patch",
   12. "deviceTypes" : [
   13. "phone",
   14. "tablet"
   15. ],
   16. "originalModuleHash" : "" // 待修复HAP包的sha256值，置空即可
   17. }
   18. }
   ```
6. 在hqf[打包工具](packing-tool.md#hqf打包指令)目录下（默认在DevEco Studio安装目录\sdk\default\openharmony\toolchains\lib下），执行命令打包，示例如下。

   ```
   1. java -jar app_packing_tool.jar --mode hqf --json-path D:\MyApplication\entry\patch.json --lib-path D:\MyApplication\entry\change_test --resources-path D:\MyApplication\entry\src\main\resources --out-path entry-default-unsigned.hqf --force true
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **json-path**：指定增量包信息patch.json路径，必选，参考[步骤5](ide-incremental-debugging.md#li13802124619204)。
   * **lib-path**：指定希望构建打包的so路径，参考[步骤2](ide-incremental-debugging.md#li13802194642015)，注意路径不能带上ABI编译环境。
   * **resources-path**：指定希望构建打包的resources资源目录，包含rawfile和resfile目录。
   * **out-path**：指定输出hqf包路径。
7. 在签名工具目录下（默认在DevEco Studio安装目录\sdk\default\openharmony\toolchains\lib下），进行签名，示例如下。

   ```
   1. java -jar hap-sign-tool.jar sign-app -keyAlias "OpenHarmony Application Release" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "OpenHarmonyApplication.cer" -profileFile "ohos_provision_release.p7b" -inFile "entry-default-unsigned.hqf" -keystoreFile "OpenHarmony.p12" -outFile "entry-default-signed.hqf" -keyPwd "123456Abc" -keystorePwd "123456Abc"
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **keyAlias**：密钥别名。
   * **appCertFile**：申请的调试证书文件，格式为.cer。
   * **profileFile**：申请的调试Profile文件，格式为.p7b。
   * **inFile**：通过打包工具生成的未携带签名信息的hqf。
   * **keystoreFile**：密钥库文件，格式为.p12。
   * **outFile**：经过签名后生成的携带签名信息的hqf。
   * **keyPwd**：密钥密码。
   * **keystorePwd**：密钥库密码。
8. 安装增量hqf包。

   ```
   1. $ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
   2. $ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
   3. $ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
   ```

## 常见问题

### 在其他的开发工具中修改打包so库文件，无法使用DevEco Studio的增量调试功能

**问题现象**

如果开发者在其他的开发工具中修改打包so库文件，在使用DevEco Studio 4.1 Canary2版本的增量调试功能时，出现无法使用增量调试功能的现象。

**解决措施**

导致这个问题的原因是在DevEco Studio 4.1 Canary2版本上，对于超过16KB的Native文件，在命中其中的断点后，LLDB调试器会默认持有文件句柄，导致调试过程中无法修改保存该文件。

开发者可通过以下两种方式处理：

* 方式一：使用以下LLDB命令关闭LLDB调试器源码缓存机制。执行如下命令后，LLDB调试器将不再持有文件句柄。

  ```
  1. settings set use-source-cache false
  ```
* 方式二：建议开发者升级至DevEco Studio 5.1.0 Beta1版本。
