---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-incremental-debugging
title: 增量调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > 增量调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:39+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:a958cc2d70c56ff4b3ac894f84b250058f1fe65652a6113c7c4746e9bb94ff8f
---

对于大型应用来说，每次修改代码后需要重新构建、推包、安装，整个流程耗时较长。针对该场景，在DevEco Studio和命令行场景中分别提供增量运行调试功能，支持开发者在真机上调试应用时，修改代码后，会识别出代码差异，构建增量包，增量运行调试时只推送增量包，减少大型应用调试推包时间。

**说明** 

C++代码增量调试支持API 11及以上版本Stage模型的工程；ArkTS代码增量调试仅支持API 12及以上版本Stage模型工程的资源文件修改。

## 使用DevEco Studio增量调试

### 调试C++代码

1. 在工具栏中，选择调试的设备，并单击**Run**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/r_CZq6-2QvOgnwN1aTT_Pw/zh-cn_image_0000002779407094.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D311DE7B18A189A3B90D9A3E431696D79070CBCE00CA5FD9531A3B862E2FC8E)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/YELlzZeWRw-ut8wWYwMWIw/zh-cn_image_0000002779407096.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=9151EE3B86408D31E1A2A827CE2764CA4E609D825B3B5921E13AB4247B06A8C0)启动工程。
2. 在修改完代码后，点击**Apply Changes**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/czeuEiVeSeqyA2-AzUpzjQ/zh-cn_image_0000002808766651.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=51C5BF97CA441B8ED6AFF7A3225796579036DF93B7DC196D99C4EE11D2B7B63E)推送增量包安装至设备。

   点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/AdkKv683QzKZgS5-GjKrwA/zh-cn_image_0000002808886731.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA51047A0B27942187A02F497ED745F6D05E39E7325B72E4A50EA0F29DD55D7E)

   **说明** 

   当前增量运行Apply Changes功能，不支持新建和删除代码文件，不支持修改装饰器相关的代码，不支持在代码中使用import新增引用文件。

### 调试rawfile/resfile资源

从DevEco Studio 5.1.0 Release版本开始支持增量调试rawfile资源。

1. 在工具栏中，选择调试的设备，并单击**Run**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/nyefgEFITPiy1TnLy0g2Ww/zh-cn_image_0000002779567074.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A88E2FFE2FD516452E6D6D8363566DFDBC8B15FF1D340E317B54BFC8D406055)或**Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/qsHd3ftiQ_i1Vk4H1dqAXQ/zh-cn_image_0000002779567076.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A998FBF54C731DB87329EE6D492AAE7EBABCA0428D797F4282AE61C8B4407A6)启动工程。
2. 在工程的资源resources文件目录下的resfile或rawfile目录下，新增或者修改资源文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/gAN82iszTESYmEejnBzeKg/zh-cn_image_0000002808886739.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BE78738152DC6688784EC31CF2794DB123C2FA2879E3B5C7030EB7118EB828B)

   **说明** 

   当前对rawfile/resfile资源的增量调试，仅支持代码中直接调用的资源文件。
3. 点击**Apply Changes**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/IK71ZFVfR1-Ddj130Fby-Q/zh-cn_image_0000002779407092.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A4D9F00E5F795F25FDB97734A10ECD556BC8D97D165F389F7E0DCA47FA7B644)推送增量包安装至设备。

   点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。

## 使用命令行增量调试

### 通过hvigorw构建hqf包

1. 检查待运行模块和依赖模块下是否存在build/config/buildConfig.json文件，如果不存在，先通过DevEco Studio全量运行工程，生成该文件。

   **说明** 

   如果已执行步骤1，则步骤2和3无需再执行。
2. 根据运行所需的模块，及模块的product、target，编写命令行执行HAP/HSP编译任务，如entry模块依赖HSP模块library：

   ```bash
   hvigorw --mode module -p module=entry@default,library@default -p product=default assembleHap assembleHsp --info --no-daemon
   ```

   关于命令行的使用指导请参考[hvigorw](ide-hvigor-commandline.md)。
3. 执行hdc命令安装HAP、HSP，关于hdc工具的使用指导请参考[hdc](hdc.md)。

   ```bash
   $ hdc shell mkdir data/local/tmp/99c24fdc44694c05be12491d0a48e139
   $ hdc file send library-default-signed.hsp "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
   $ hdc file send entry-default-signed.hap "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
   $ hdc shell bm install -p "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
   $ hdc shell rm -rf data/local/tmp/99c24fdc44694c05be12491d0a48e139
   $ hdc shell aa start -a {abilityName} -b {bundleName}
   ```

   * abilityName：应用的ability名称。
   * bundleName：应用包名。
4. 如果修改了HAP/HSP模块的rawfile或resfile目录下的资源文件，则需要在对应模块的build/default/intermediates/patch/default目录下新建changedFileList.json并写入修改的文件；如果修改了HAR模块的资源文件，则需要在依赖该HAR的模块下写入修改的文件，示例如下。

   ```json
   {
     "resources": {
       "resFile": [
         {
           "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
           "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
         }
       ],
       "rawFile": [
         {
           "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
           "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
         }
       ]
     }
   }
   ```
5. 修改C++代码后，执行hqf打包命令，执行完成后可在entry和library模块的输出目录build/default/outputs/default中，找到对应的产物entry-default-signed.hqf和library-default-signed.hqf。

   ```bash
   hvigorw --mode module -p module=entry@default,library@default -p product=default assembleDevHqf --info --no-daemon
   ```
6. 执行hdc命令安装hqf。

   ```bash
   $ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
   $ hdc file send library-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
   $ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
   $ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
   ```

### 通过SDK工具构建hqf包

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/QFZIo1s3RlqFIkUqZdbHoQ/zh-cn_image_0000002779567070.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB190BA30D481A5C4666F573803A9C8F39C55117111903D495BBAE4728980836 "点击放大")

1. 全量编译应用并安装到设备。

   ```bash
   hdc bm install {hap_path} // 安装包在电脑上，使用该命令，hap_path是安装包路径
   hdc shell bm install -p {hap_path}  // 安装包在设备上，使用该命令
   ```
2. 开发者通过独立的构建流程，识别出希望构建增量hqf包的so，根据ABI编译环境（可查看build-profile.json5的[abiFilters](ide-hvigor-cpp.md#section0721057575)字段），汇总到某一目录下，例如汇总在change\_test目录下，编译环境是arm64-v8a，示例如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/IzbuxcdzTcm7EGPFI1ClHw/zh-cn_image_0000002779567072.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=969C05153D36B164C33869D9236B64D1ED0ED4D6E9EF620FBDEBCF117C8EB872)
3. （可选）进行资源文件修改。如果修改了HAP/HSP模块的rawfile或resfile目录下的资源文件，则需要在对应模块的build/default/intermediates/patch/default目录下新建changedFileList.json并写入修改的文件；如果修改了HAR模块的资源文件，则需要在依赖该HAR的模块下写入修改的文件，示例如下。

   ```json
   {
     "resources": {
       "resFile": [
         {
           "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
           "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
         }
       ],
       "rawFile": [
         {
           "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
           "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
         }
       ]
     }
   }
   ```
4. 提前准备与已安装应用一致的签名文件。

   可以从工程的build-profile.json5文件中获取到对应的签名文件。
5. 准备patch.json文件，示例如下。

   ```json
   {
       "app" : {
           "bundleName" : "com.ohos.quickfix",
           "versionCode" : 1000000, // 应用版本号
           "versionName" : "1.0.0",
           "patchVersionCode" : 1000000, // 补丁版本号，在每次进行增量调试前，将版本号+1，确保此次增量调试补丁包版本号大于上次增量调试补丁包版本号
           "patchVersionName" : "1000000"  // 与补丁版本号保持一致
       },
       "module" : {
           "name" : "entry",
           "type" : "patch",
           "deviceTypes" : [
               "phone",
               "tablet"
           ],
           "originalModuleHash" : "" // 待修复HAP包的sha256值，置空即可
       }
   }
   ```
6. 在hqf[打包工具](packing-tool.md#hqf打包指令)目录下（默认在DevEco Studio安装目录\sdk\default\openharmony\toolchains\lib下），执行命令打包，示例如下。

   ```bash
   java -jar app_packing_tool.jar --mode hqf --json-path D:\MyApplication\entry\patch.json --lib-path D:\MyApplication\entry\change_test --resources-path D:\MyApplication\entry\src\main\resources --out-path entry-default-unsigned.hqf --force true
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **json-path**：指定增量包信息patch.json路径，必选，参考[步骤5](ide-incremental-debugging.md#li13802124619204)。
   * **lib-path**：指定希望构建打包的so路径，参考[步骤2](ide-incremental-debugging.md#li13802194642015)，注意路径不能带上ABI编译环境。
   * **resources-path**：指定希望构建打包的resources资源目录，包含rawfile和resfile目录。
   * **out-path**：指定输出hqf包路径。
7. 在签名工具目录下（默认在DevEco Studio安装目录\sdk\default\openharmony\toolchains\lib下），进行签名，示例如下。

   ```bash
   java -jar hap-sign-tool.jar sign-app -keyAlias "OpenHarmony Application Release" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "OpenHarmonyApplication.cer" -profileFile "ohos_provision_release.p7b" -inFile "entry-default-unsigned.hqf" -keystoreFile "OpenHarmony.p12" -outFile "entry-default-signed.hqf" -keyPwd "123456Abc" -keystorePwd "123456Abc"
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

   ```bash
   $ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
   $ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
   $ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
   ```
