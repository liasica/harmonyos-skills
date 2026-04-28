---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app
title: 搭建流水线
breadcrumb: 指南 > 命令行工具 > 搭建流水线
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:91a0bd1460600b341b57848c1086e24b928c1f72737ceb2f4237359c9f1828e0
---

除了使用DevEco Studio一键式构建应用/元服务外，还可以使用命令行工具来调用Hvigor任务进行构建。通过命令行的方式构建应用或元服务，可用于构建CI（Continuous Integration）流水线，按照计划时间自动化地构建HAP/APP、签名、安装运行等操作。

通过命令行方式构建应用或元服务，可在Windows、Linux和macOS下调用相应命令来执行，本文将以Linux系统为例进行讲解，包括准备构建环境、构建HAP、签名运行等操作。在调用命令行任务上，Windows/macOS系统与Linux系统没有区别，仅在搭建构建环境上存在差异。

说明

* 如果开发者所使用的电脑处于完全无网络的环境中，搭建构建环境请参考[无网络流水线搭建](ide-command-line-building-app.md#section15767113454814)。
* HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。
* 请在执行命令行之前，保证当前工程是可信任的，确保安全编译。

## 系统平台要求

* Linux：64位操作系统
* GLIBC：2.28或更高版本
* 内存：推荐使用16GB及以上，最小8GB
* 硬盘：100GB及以上

## 预置条件

### 配置JDK

1. 下载JDK，支持JDK 17版本。
2. 在Terminal里，进入JDK软件包目录，执行如下命令，解压已经下载好的安装包，其中jdk-17.0.6\_linux-x64\_bin.tar.gz为软件包名称，请根据实际配置进行修改。

   ```
   1. tar -xvf jdk-17.0.6_linux-x64_bin.tar.gz
   ```
3. 配置JDK环境变量。

   ```
   1. #jdk
   2. export JAVA_HOME=/opt/jdk-17.0.6_linux-x64_bin
   3. export PATH=$PATH:$JAVA_HOME/bin
   ```
4. 执行如下命令，检查JDK安装结果。

   ```
   1. java -version
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/TXIY_sLTQFGuplksSj9IyQ/zh-cn_image_0000002561752785.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=E821BFBB25D639E91981BD4ECED007CC44B96188BC7522465ECED4DE8CC99159)

### 获取命令行工具

1. [命令行工具获取](ide-commandline-get.md#section21298572437)。其他系统(Windows/macOS)请根据实际情况下载对应版本。
2. 执行如下命令，解压命令行工具commandline-tools-linux-xxx.zip，工具名称请根据实际情况进行修改。

   ```
   1. unzip commandline-tools-linux-x64-5.0.3.XXX.zip
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/wh_1X-CYQDKZ872WI6Nu4w/zh-cn_image_0000002530752854.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=0095692DDE125D63582F8405BF401F153109749CF2524A45654F3498DFBE708B)
3. 将解压后所在的路径定义为COMMANDLINE\_TOOL\_DIR，在后续配置Node、hdc、hvigor、ohpm工具环境变量时使用。例如解压在/opt路径下。

   ```
   1. export COMMANDLINE_TOOL_DIR=/opt
   ```

### 配置Node.js环境变量

命令行工具包含了配套的Node.js，按照以下步骤配置环境变量。

1. 配置Node.js环境变量。

   ```
   1. # 此处以Linux系统举例，不同系统Node.js路径不同，具体以实际路径为准
   2. export NODE_HOME=${COMMANDLINE_TOOL_DIR}/command-line-tools/tool/node
   3. export PATH=$PATH:$NODE_HOME/bin
   ```

   说明

   不同系统的Node.js所在路径不同，Windows存放在tool/node目录下，Linux和macOS存放在tool/node/bin目录下。
2. 执行如下命令，查询Node.js版本信息，确认配置成功。

   ```
   1. node -v
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Pdh5lkcBRKWA00kFPTiJ2w/zh-cn_image_0000002561832775.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=0FB4B7E980DF92E74762C51081801C6D51AEA7946EDD79F17C3EEE321DB3EB6F)

说明

建议使用命令行工具中自带的Node.js工具，若另外单独下载配置其他版本的Node.js，推荐使用v18版本。

### 配置hdc环境变量

hdc命令行工具是调试HarmonyOS应用/元服务的工具，该工具存放在命令行工具自带的sdk下的toolchains目录中。为方便使用hdc命令行工具，请将其添加到环境变量中。

1. 请先完成[获取命令行工具](ide-command-line-building-app.md#section88316312414)。
2. 添加hdc路径到环境变量，指令如下。

   hdc工具存放路径示例：${COMMANDLINE\_TOOL\_DIR}/command-line-tools/sdk/default/openharmony/toolchains。

   ```
   1. export HDC_HOME=${COMMANDLINE_TOOL_DIR}/command-line-tools/sdk/default/openharmony/toolchains
   2. export PATH=$PATH:$HDC_HOME
   ```

### 配置hvigor环境变量

1. 请先完成[获取命令行工具](ide-command-line-building-app.md#section88316312414)。
2. 添加hvigorw路径到PATH环境变量，指令如下。

   ```
   1. export PATH=${COMMANDLINE_TOOL_DIR}/command-line-tools/bin:$PATH
   ```
3. 切换到工程根目录，执行如下命令，查询Hvigor版本信息，确认安装成功。

   ```
   1. hvigorw -v
   ```

### 配置npm镜像仓库

若您的工程在hvigor/hvigor-config.json5文件中依赖npm三方组件，流水线中则需要配置npm镜像地址，编译时才能正确地下载它。

```
1. npm config set registry https://repo.huaweicloud.com/repository/npm/
2. npm config set "@ohos:registry" https://repo.harmonyos.com/npm/
```

### 安装ohpm

1. 请先完成[获取命令行工具](ide-command-line-building-app.md#section88316312414)。
2. 添加ohpm路径到环境变量，指令如下。

   ```
   1. export PATH=${COMMANDLINE_TOOL_DIR}/command-line-tools/bin:$PATH
   ```
3. 执行如下命令，查询ohpm版本信息，确认安装成功。

   ```
   1. ohpm -v
   ```
4. 配置仓库地址（可指定多个地址，','号分割），指令如下。

   ```
   1. ohpm config set registry https://ohpm.openharmony.cn/ohpm/
   2. ohpm config set strict_ssl false
   ```

### 安装libGL1库

在linux系统的构建场景下，使用[纹理压缩](ide-hvigor-build-profile-app.md#section2095319147103)功能需要安装libGL1库。例如Ubuntu/Debian上安装libgl1-mesa-dev，CentOS/RHEL上安装mesa-libGL-devel。

以libgl1-mesa-dev为例，执行以下命令安装，其他系统请替换成实际的包名。

```
1. apt install -y libgl1-mesa-dev
```

## 构建应用

### 安装工程及模块依赖

使用命令行进行构建前，需要分别进入工程及各个模块下执行ohpm install命令，安装**工程及各个模块**依赖的三方库。

1. 定义ohpm安装函数，示例如下。

   ```
   1. # 切换到指定目录$1并执行ohpm install指令
   2. function ohpm_install() {
   3. cd $1              # $1：函数第一个参数, 必须是路径
   4. ohpm install --all # 安装所有依赖
   5. }
   ```
2. 定义变量 **PROJECT\_PATH**，表示工程目录路径，示例如下。

   ```
   1. PROJECT_PATH=xxx/xxx/project_name  # 工程路径
   ```

   注意

   工程目录不要存放在隐藏目录下，即工程路径的每一级目录中不要以.开头，例如xxx/.xxx/project，否则构建时可能会将模块中的代码和配置文件等作为资源打包进产物中，不会进行混淆或加密。
3. 安装工程及各个模块的三方库依赖，示例如下。

   ```
   1. # 根据业务情况安装ohpm三方库依赖
   2. ohpm_install "${PROJECT_PATH}"
   3. ...
   ```

### 执行Hvigor命令进行构建

使用hvigorw命令行工具执行构建命令，构建完成后，工程或模块下build目录中会生成相应的hap/hsp/har/app产物。

```
1. # 根据业务情况，执行相应的构建命令, 示例如下

3. # clean工程
4. hvigorw clean --no-daemon

6. # 构建Hap, 生成产物：${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/xxx.hap
7. hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon

9. # 构建Hsp, 生成产物：${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/(xxx.har | xxx.hsp)
10. hvigorw assembleHsp --mode module -p module=library@default -p product=default --no-daemon

12. # 构建Har, 生成产物：${PROJECT_PATH}/{moduleName}/build/{productName}/outputs/{targetName}/outputs/xxx.har
13. hvigorw assembleHar --mode module -p module=library1@default -p product=default --no-daemon

15. # 构建App, 生成产物: ${PROJECT_PATH}/build/outputs/{productName}/xxx.app
16. hvigorw assembleApp --mode project -p product=default -p buildMode=debug --no-daemon
```

* 本文使用Linux作为流水线构建环境，Linux环境会对大小写敏感，如果您的代码引用中有大小写错误（例如代码中import funcA from './aaa'，而实际文件为AAA.ets），而且开发环境是Windows或者Mac，那么有可能出现Windows或者Mac环境下编译通过，而Linux环境下编译不通过的现象。通过在项目级的build-profile.json5文件中配置caseSensitiveCheck为true来打开大小写敏感，保持Windows或者Mac环境编译与Linux环境编译结果一致。

  ```
  1. // build-profile.json5文件
  2. {
  3. "name": "default",
  4. "compatibleSdkVersion": "6.1.0(23)",
  5. "runtimeOS": "HarmonyOS",
  6. "buildOption": {
  7. "strictMode": {
  8. "caseSensitiveCheck" : true
  9. }
  10. }
  11. }
  ```
* 如果在非daemon模式下，需要修改node内存配置，可在command-line-tools的hvigor/bin/hvigorw文件中取消第15行的注释，并配置对应的数值。如将node内存配置为10240，示例如下：

  ```
  1. NODE_OPTS="--max-old-space-size=10240"
  ```
* 如果是在daemon模式下，请参考[设置守护进程内存](ide-hvigor-daemon.md#section327617383145)。

编译构建常见的任务和扩展参数如下，更多关于Hvigor命令行参数详见：[常用命令](ide-hvigor-commandline.md#section16300629103)。

**表1** HarmonyOS应用构建常用扩展参数

| 选项 | 说明 |
| --- | --- |
| -p buildMode={debug | release} | 采用debug/release模式进行编译构建。  缺省时：构建Hap/Hsp/Har时为debug模式，构建App时为release模式。  关于构建模式的详细说明，请参考[指定构建模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)。针对HAR构建，请参考[构建HAR](ide-hvigor-build-har.md)。 |
| -p product={ProductName} | 指定product进行编译, 编译product下配置的module target。  缺省时：默认为default。 |
| -p module={ModuleName}@{TargetName} | 指定模块及target进行编译，可指定多个相同类型的模块进行编译，以逗号隔开；TargetName不指定时默认为default。  限制：此参数需要与--mode module参数搭配使用。  缺省时：执行AssembleHap任务会编译工程下所有模块，默认指定target为default。 |
| -p ohos-test-coverage={true | false} | 执行测试框架代码覆盖率插桩编译。 |

**表2** HarmonyOS应用编译构建相关任务

| 选项 | 说明 |
| --- | --- |
| clean | 清理构建产物 |
| assembleHap | 构建Hap应用 |
| assembleApp | 构建App应用 |
| assembleHsp | 构建Hsp包 |
| assembleHar | 构建Har包 |

## 运行应用

如果构建时已配置签名文件，会分别生成已签名包（如xxx-signed.hap）和未签名包（如xxx-unsigned.hap），已签名包可直接在真机设备上运行，无需重新签名。如果需要对包进行重签名，可使用签名工具对未签名包进行签名，步骤如下。

### 准备申请签名所需文件

准备好申请签名所需3个文件：密钥（.p12文件）、数字证书（.cer文件）、Profile（.p7b文件）。

**生成密钥和证书请求文件**

使用JDK携带的Keytool工具生成密钥和证书请求文件。

1. 参考[配置JDK](ide-command-line-building-app.md#section195447475220)步骤配置环境变量后，打开命令行终端，执行如下命令，生成密钥库文件。例如，生成的密钥库名称为demo.p12，存储到path目录下。

   ```
   1. keytool -genkeypair -alias "demo_key" -keyalg EC -groupname secp256r1 -sigalg SHA256withECDSA -dname "C=CN,O=HUAWEI,OU=HUAWEI IDE,CN=demo_key"  -keystore /path/demo.p12 -storetype pkcs12 -validity 9125 -storepass 123456Abc -keypass 123456Abc
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **alias**：密钥的别名信息，用于标识密钥名称。
   * **dname**：证书基本信息。
     + C：国家/地区代码，如CN。
     + O：组织名称，如HUAWEI。
     + OU：组织单位名称，如HUAWEI IDE。
     + CN：名字与姓氏，建议与别名一致。
   * **keystore**：密钥库文件，请将"/path/demo.p12"修改为实际路径。
   * **validity**：证书有效期，例如设置为9125（25年）。
   * **storepass**：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。
   * **keypass**：设置密钥的密码，请与**storepass**保持一致。
2. 执行如下命令，执行后需要输入**storepass**密码，生成证书请求文件。

   ```
   1. keytool -certreq -alias "demo_key" -sigalg SHA256withECDSA -keystore /path/demo.p12 -storetype pkcs12 -file /path/demo.csr
   ```

   生成证书请求文件的参数说明如下：

   * **alias**：与上一步骤中输入的**alias**保持一致。
   * **keystore**：与上一步骤中输入的**keystore**保持一致。
   * **file**：生成的证书请求文件名称，后缀为.csr，请将"/path/demo.csr"修改为实际路径。

**申请调试****数字证书和Profil****e****文件**

生成证书请求文件后，在AppGallery Connect中申请、下载调试数字证书和Profile文件，具体请参考[申请调试证书](ide-signing.md#section081822416419)和[申请Profile文件和添加权限信息](ide-signing.md#section89479413571)。

### 对未签名的HAP/APP进行签名

1. 准备好签名工具hap-sign-tool.jar，在${COMMANDLINE\_TOOL\_DIR}/command-line-tools/sdk/default/openharmony/toolchains/lib下。
2. 在签名工具目录下，使用如下命令进行签名。详细的签名工具指导请参考[Hap包签名工具](https://gitcode.com/openharmony/developtools_hapsigner)。

   ```
   1. java -jar hap-sign-tool.jar sign-app -keyAlias "demo_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "/path/demo.cer" -profileFile "/path/demo.p7b" -inFile "/path/hap-unsigned.hap" -keystoreFile "/path/demo.p12" -outFile "/path/hap-signed.hap" -keyPwd "123456Abc" -keystorePwd "123456Abc"
   ```

   关于该命令中需要修改的参数说明如下，其余参数不需要修改：

   * **keyAlias**：密钥别名。
   * **appCertFile**：申请的调试证书文件，格式为.cer。
   * **profileFile**：申请的调试Profile文件，格式为.p7b。
   * **inFile**：通过Hvigor打包生成的未携带签名信息的HAP。
   * **keystoreFile**：密钥库文件，格式为.p12。
   * **outFile**：经过签名后生成的携带签名信息的HAP。
   * **keyPwd**：密钥密码。
   * **keystorePwd**：密钥库密码。

   说明

   如果要对APP进行签名，只需将**inFile**和**outFile**参数修改为APP包即可。

### 运行应用

通过[hdc工具](hdc.md)将HAP推送到真机设备上进行安装，需要注意的是，推送的HAP必须是携带签名信息的，否则会导致HAP安装失败。

推送HAP的命令如下：

```
1. # 将打包好的hap包推送至设备中
2. hdc file send "{PROJECT_PATH}/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
3. # 安装hap包
4. hdc shell bm install -p "data/local/tmp/entry-default-signed.hap"
5. # 删除hap包
6. hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
```

在设备上运行HAP的命令如下：

```
1. hdc shell aa start -a EntryAbility -b com.example.myapplication -m entry
```

## 示例脚本

说明

此脚本无法直接运行，仅供参考，业务要根据自己的情况来进行适配。

```
1. #!/bin/bash
2. set -ex

4. JAVA_HOME=xxx #指定JDK的安装目录
5. COMMANDLINE_TOOL_DIR=xxx #命令行工具的安装目录

7. #配置hvigor、ohpm环境变量
8. export PATH=${COMMANDLINE_TOOL_DIR}/command-line-tools/bin:$PATH

10. #下载并配置JDK
11. function init_JDK() {
12. if [ ! -d "${JAVA_HOME}" ]; then
13. mkdir "${JAVA_HOME}"
14. fi
15. cd ${JAVA_HOME}
16. wget --no-check-certificate -q "${jdk下载路径}" -O jdk-linux.tar.xz #下载jdk，需要替换jdk下载路径
17. tar -vxf jdk-linux.tar.xz
18. JDK_DIR=xxx #jdk压缩包文件里面的目录
19. cd ${JDK_DIR}
20. mv -f ./* .[^.]* ../
21. cd ..
22. rm -rf JDK_DIR jdk-linux.tar.xz
23. export JAVA_HOME=${JAVA_HOME}
24. export PATH=$JAVA_HOME/bin:$PATH
25. java -version
26. }

28. #配置hdc环境变量
29. function init_hdc() {
30. export HDC_HOME=${COMMANDLINE_TOOL_DIR}/command-line-tools/sdk/default/openharmony/toolchains #设置hdc工具的环境变量，hdc工具在toolchains所在路径下
31. export PATH=$HDC_HOME:$PATH
32. }

34. # 安装ohpm, 若镜像中已存在ohpm，则无需重新安装
35. function init_ohpm() {
36. ohpm -v
37. # 配置ohpm仓库地址
38. ohpm config set registry https://ohpm.openharmony.cn/ohpm/
39. }

41. # 初始化相关路径
42. PROJECT_PATH=xxx  # 工程目录
43. # 进入package目录安装依赖
44. function ohpm_install {
45. cd $1
46. ohpm install
47. }
48. # 环境适配
49. function buildHAP() {
50. # 根据业务情况安装ohpm三方库依赖
51. ohpm_install "${PROJECT_PATH}"
52. ohpm_install "${PROJECT_PATH}/entry"
53. ohpm_install "${PROJECT_PATH}/xxx"
54. # 根据业务情况，采用对应的构建命令，可以参考DevEco Studio构建日志中的命令
55. cd ${PROJECT_PATH}
56. hvigorw clean --no-daemon
57. hvigorw assembleHap --mode module -p product=default -p debuggable=false --no-daemon # 流水线构建命令建议末尾加上--no-daemon
58. }
59. function install_hap() {
60. hdc file send "${PROJECT_PATH}/entry/build/default/outputs/default/entry-default-signed.hap" "data/local/tmp/entry-default-signed.hap"
61. hdc shell bm install -p "data/local/tmp/entry-default-signed.hap"
62. hdc shell rm -rf "data/local/tmp/entry-default-signed.hap"
63. hdc shell aa start -a MainAbility -b com.example.myapplication -m entry
64. }

66. # 使用ohpm发布har
67. function upload_har {
68. ohpm publish pkg.har
69. }

71. function main {
72. local startTime=$(date '+%s')
73. init_JDK
74. init_hdc
75. init_ohpm
76. buildHAP
77. install_hap
78. upload_har
79. local endTime=$(date '+%s')
80. local elapsedTime=$(expr $endTime - $startTime)
81. echo "build success in ${elapsedTime}s..."
82. }
83. main
```

## 无网络流水线搭建

如果开发者使用的电脑处于完全无网络的环境中，可参考以下步骤搭建流水线环境。

### 安装pnpm插件

1. 请在可访问网络的电脑上创建一个空文件夹，在文件夹中创建一个package.json文件，在文件中填写如下内容：

   ```
   1. {
   2. "dependencies": {
   3. "pnpm": "8.13.1"
   4. }
   5. }
   ```
2. 先配置[环境变量](ide-environment-config.md#zh-cn_topic_0000001056725590_li358362302311)，再打开[命令行工具](ide-commandline-get.md)，在文件夹下执行 npm install 命令，会生成node\_modules文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/-NW3YAggQn6PSPUfDQBMZA/zh-cn_image_0000002530752848.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=4811BF2CE358FD4B2A6C7AFF47615F481D749F77B953E3A913BD023C0BF50F50)
3. 将node\_modules文件夹和package.json文件拷贝到无网络电脑的C:\Users\*用户名目录*\.hvigor\wrapper\tools下（若当前无该目录，请手动创建）。
4. 在无网络电脑上执行如下命令，设置npm离线模式：

   ```
   1. npm config set offline true
   ```

### 安装npm依赖插件

1. 请在可访问网络的电脑上创建一个空文件夹，在文件夹中创建一个package.json文件，配置npm依赖，示例如下：

   ```
   1. {
   2. "dependencies": {
   3. "ajv": "latest"
   4. }
   5. }
   ```
2. 打开[命令行工具](ide-commandline-get.md)，在文件夹下执行 npm install 命令，会生成node\_modules文件夹。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/LfW-iFwMT-aNCO83P0XUeA/zh-cn_image_0000002530752850.png?HW-CC-KV=V1&HW-CC-Date=20260427T235750Z&HW-CC-Expire=86400&HW-CC-Sign=B83001013882ACC15B5A797D1BD56E43229B9AB68D12B0E4228995ACD81A374C)
3. 将node\_modules文件夹拷贝到无网络电脑的工程根目录下。

### 安装ohpm依赖插件

请参考[安装三方库](ide-no-network.md#section208435578175)。

### 安装libGL1库

在linux系统的构建场景下，使用[纹理压缩](ide-hvigor-build-profile-app.md#section2095319147103)功能需要安装libGL1库。

请在可访问网络的电脑上下载libGL1库，例如Ubuntu/Debian下载libgl1-mesa-dev，CentOS/RHEL下载mesa-libGL-devel，并将安装包拷贝到无网络电脑中进行安装。
